"""
copy_pdfs_from_zotero.py
------------------------
Copies PDFs from a Zotero library to the project literature/pdfs/ folder,
matching records by DOI (primary) or title (fallback).

Optionally restricts matching to a named Zotero collection.

Usage
-----
  python scripts/copy_pdfs_from_zotero.py
  python scripts/copy_pdfs_from_zotero.py --collection all_retained
  python scripts/copy_pdfs_from_zotero.py --collection all_retained --dry-run

Arguments
---------
  --collection NAME   Restrict to items in this Zotero collection (default: all_retained)
  --all-library       Match against entire Zotero library, not a specific collection
  --zotero-dir PATH   Path to Zotero data directory (default: C:/Users/torbskar/Zotero)
  --retained CSV      Path to the retained records CSV (default: literature/all_retained_for_zotero.csv)
  --pdf-dir DIR       Output folder for PDFs (default: literature/pdfs)
  --manifest CSV      Output manifest file (default: literature/pdfs_manifest.csv)
  --dry-run           Report matches without copying files

Outputs
-------
  literature/pdfs/[ZOTERO_KEY].pdf   one file per matched PDF
  literature/pdfs_manifest.csv       maps filename -> title, authors, year, DOI, search string
"""

import argparse
import os
import shutil
import sqlite3
import sys
import tempfile
from pathlib import Path

import pandas as pd

# ── Defaults ──────────────────────────────────────────────────────────────────

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULTS = {
    "zotero_dir":  Path(r"C:\Users\torbskar\Zotero"),
    "retained":    PROJECT_ROOT / "literature" / "all_retained_for_zotero.csv",
    "pdf_dir":     PROJECT_ROOT / "literature" / "pdfs",
    "manifest":    PROJECT_ROOT / "literature" / "pdfs_manifest.csv",
    "collection":  "all_retained",
}

# ── Helpers ───────────────────────────────────────────────────────────────────

def open_db_copy(zotero_dir: Path) -> sqlite3.Connection:
    """Work on a copy of the SQLite database so Zotero can stay open."""
    src = zotero_dir / "zotero.sqlite"
    tmp = Path(tempfile.mktemp(suffix=".sqlite"))
    shutil.copy2(src, tmp)
    return sqlite3.connect(tmp), tmp


def get_collection_item_ids(cur: sqlite3.Cursor, collection_name: str) -> set[int]:
    """Return all itemIDs in the named collection (and its sub-collections)."""
    cur.execute(
        "SELECT collectionID FROM collections WHERE collectionName = ?",
        (collection_name,)
    )
    row = cur.fetchone()
    if row is None:
        available = [r[0] for r in cur.execute("SELECT collectionName FROM collections").fetchall()]
        print(f"ERROR: Collection '{collection_name}' not found.")
        print(f"Available collections: {available}")
        sys.exit(1)

    root_id = row[0]

    # Walk sub-collections recursively
    all_collection_ids = {root_id}
    queue = [root_id]
    while queue:
        parent = queue.pop()
        cur.execute("SELECT collectionID FROM collections WHERE parentCollectionID = ?", (parent,))
        children = [r[0] for r in cur.fetchall()]
        for c in children:
            all_collection_ids.add(c)
            queue.append(c)

    # Get all item IDs in those collections
    placeholders = ",".join("?" * len(all_collection_ids))
    cur.execute(
        f"SELECT itemID FROM collectionItems WHERE collectionID IN ({placeholders})",
        list(all_collection_ids)
    )
    return {r[0] for r in cur.fetchall()}


def build_lookup_maps(cur: sqlite3.Cursor, item_ids: set[int] | None):
    """Build DOI->itemID and title->itemID lookup maps, optionally filtered by item_ids."""
    filter_clause = ""
    if item_ids is not None:
        placeholders = ",".join("?" * len(item_ids))
        filter_clause = f"AND id.itemID IN ({placeholders})"
        filter_params = list(item_ids)
    else:
        filter_params = []

    cur.execute(
        f"""SELECT LOWER(TRIM(v.value)), id.itemID
            FROM itemData id
            JOIN itemDataValues v ON id.valueID = v.valueID
            WHERE id.fieldID = 59 {filter_clause}""",  # fieldID 59 = DOI
        filter_params
    )
    doi_map = {r[0]: r[1] for r in cur.fetchall()}

    cur.execute(
        f"""SELECT LOWER(TRIM(v.value)), id.itemID
            FROM itemData id
            JOIN itemDataValues v ON id.valueID = v.valueID
            WHERE id.fieldID = 1 {filter_clause}""",   # fieldID 1 = title
        filter_params
    )
    title_map = {r[0]: r[1] for r in cur.fetchall()}

    return doi_map, title_map


def build_pdf_map(cur: sqlite3.Cursor) -> dict[int, tuple[str, str]]:
    """Return parentItemID -> (zotero_key, original_filename) for all PDF attachments."""
    cur.execute(
        """SELECT ia.parentItemID, i.key, ia.path
           FROM itemAttachments ia
           JOIN items i ON ia.itemID = i.itemID
           WHERE ia.contentType = 'application/pdf'
           AND ia.path IS NOT NULL"""
    )
    pdf_map = {}
    for parent, key, path in cur.fetchall():
        filename = path.replace("storage:", "")
        pdf_map[parent] = (key, filename)
    return pdf_map


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--collection",  default=DEFAULTS["collection"], help="Zotero collection name to restrict search to")
    parser.add_argument("--all-library", action="store_true",            help="Match against entire library, ignoring --collection")
    parser.add_argument("--zotero-dir",  default=DEFAULTS["zotero_dir"], type=Path, help="Zotero data directory")
    parser.add_argument("--retained",    default=DEFAULTS["retained"],   type=Path, help="Retained records CSV")
    parser.add_argument("--pdf-dir",     default=DEFAULTS["pdf_dir"],    type=Path, help="Output folder for PDFs")
    parser.add_argument("--manifest",    default=DEFAULTS["manifest"],   type=Path, help="Output manifest CSV")
    parser.add_argument("--dry-run",     action="store_true",            help="Report matches without copying")
    args = parser.parse_args()

    args.pdf_dir.mkdir(parents=True, exist_ok=True)

    print(f"Zotero dir:      {args.zotero_dir}")
    print(f"Retained CSV:    {args.retained}")
    print(f"PDF output:      {args.pdf_dir}")
    if args.all_library:
        print("Scope:           entire library")
    else:
        print(f"Collection:      {args.collection}")
    if args.dry_run:
        print("Mode:            DRY RUN (no files copied)")
    print()

    # Open DB copy
    conn, tmp_path = open_db_copy(args.zotero_dir)
    cur = conn.cursor()

    # Get item IDs in scope
    if args.all_library:
        item_ids = None
    else:
        item_ids = get_collection_item_ids(cur, args.collection)
        print(f"Items in collection '{args.collection}': {len(item_ids)}")

    # Build lookup maps
    doi_map, title_map = build_lookup_maps(cur, item_ids)
    pdf_map = build_pdf_map(cur)
    conn.close()
    tmp_path.unlink(missing_ok=True)

    # Load retained records
    df = pd.read_csv(args.retained, encoding="utf-8-sig")
    print(f"Retained records: {len(df)}\n")

    copied, no_pdf, no_match = [], [], []

    for _, row in df.iterrows():
        doi   = str(row.get("DOI",   "") or "").strip().lower()
        title = str(row.get("Title", "") or "").strip().lower()

        zotero_id  = doi_map.get(doi) if doi else None
        match_type = "doi"
        if zotero_id is None:
            zotero_id  = title_map.get(title)
            match_type = "title"

        if zotero_id is None:
            no_match.append({"Title": row["Title"], "DOI": row.get("DOI", "")})
            continue

        if zotero_id not in pdf_map:
            no_pdf.append({"Title": row["Title"], "DOI": row.get("DOI", "")})
            continue

        key, orig_filename = pdf_map[zotero_id]
        src = args.zotero_dir / "storage" / key / orig_filename
        dst = args.pdf_dir / f"{key}.pdf"

        if src.is_file():
            already = dst.exists()
            if not args.dry_run and not already:
                shutil.copy2(src, dst)
            if args.dry_run:
                status = "would copy"
            elif already:
                status = "already exists"
            else:
                status = "copied"
            copied.append({
                "File":          f"{key}.pdf",
                "Zotero key":    key,
                "Match type":    match_type,
                "Status":        status,
                "Title":         row["Title"],
                "Authors":       row.get("Authors", ""),
                "Year":          row.get("Year", ""),
                "DOI":           row.get("DOI", ""),
                "Search string": row.get("Search string", ""),
            })
        else:
            no_pdf.append({"Title": row["Title"], "DOI": row.get("DOI", "")})

    # ── Summary ───────────────────────────────────────────────────────────────
    print(f"PDFs {'found' if args.dry_run else 'copied/present'}:  {len(copied)}")
    print(f"  — already in pdf_dir:  {sum(1 for r in copied if r['Status'] == 'already exists')}")
    print(f"  — newly copied:        {sum(1 for r in copied if r['Status'] == 'copied')}")
    print(f"In Zotero, no PDF:       {len(no_pdf)}")
    print(f"Not matched in Zotero:   {len(no_match)}")
    print(f"Total retained:          {len(df)}")

    if no_match:
        print(f"\nRecords not matched in collection '{args.collection}':")
        for r in no_match[:10]:
            print(f"  {r['Title'][:80]}")
        if len(no_match) > 10:
            print(f"  ... and {len(no_match) - 10} more")

    # ── Write manifest ────────────────────────────────────────────────────────
    if not args.dry_run:
        pd.DataFrame(copied).to_csv(args.manifest, index=False, encoding="utf-8-sig")
        print(f"\nManifest written: {args.manifest}")


if __name__ == "__main__":
    main()
