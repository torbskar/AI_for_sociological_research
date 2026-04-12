#!/usr/bin/env python3
"""
rename_pdfs.py
Purpose: Rename downloaded PDFs to [Author_etal]_[year]_[short_title].pdf
         using Haiku to extract bibliographic info.

Two-step workflow (run from project root):

  STEP 1 — Extract text from each PDF (no API needed):
      python scripts/rename_pdfs.py --extract
      Output: literature/rename_candidates.json

  STEP 2 — Ask Claude Code to process the candidates:
      "Process rename_candidates.json with Haiku and write rename_mappings.json"
      Claude Code will spawn Haiku agents and write: literature/rename_mappings.json

  STEP 3 — Apply the mappings (no API needed):
      python scripts/rename_pdfs.py --apply [--dry-run]
      Output: files renamed in-place; literature/rename_log.csv written

Requirements:
    pip install pymupdf
"""

import sys, os, re, csv, json, argparse, unicodedata
sys.stdout.reconfigure(encoding="utf-8")

import fitz   # PyMuPDF

DEFAULT_PDF_DIR         = "literature/pdfs"
CANDIDATES_PATH         = "literature/automated_literature_searches/filter_tidying/rename_candidates.json"
MAPPINGS_PATH           = "literature/automated_literature_searches/filter_tidying/rename_mappings.json"
LOG_PATH                = "literature/automated_literature_searches/filter_tidying/rename_log.csv"
MAX_CHARS               = 2000   # chars of PDF text sent to Haiku


# ---------------------------------------------------------------------------
# PDF TEXT EXTRACTION
# ---------------------------------------------------------------------------

def extract_text(pdf_path: str) -> str:
    """Return metadata fields + first-page text, up to MAX_CHARS characters."""
    try:
        doc = fitz.open(pdf_path)
    except Exception as e:
        return f"[Could not open PDF: {e}]"

    parts = []
    meta = doc.metadata or {}
    for key in ("author", "title", "subject", "creationDate"):
        val = meta.get(key, "").strip()
        if val:
            parts.append(f"[metadata:{key}] {val}")

    try:
        first_page = doc[0].get_text("text").strip()
        parts.append("[first_page_text]")
        parts.append(first_page)
    except Exception:
        pass

    doc.close()
    return "\n".join(parts)[:MAX_CHARS]


# ---------------------------------------------------------------------------
# FILENAME CONSTRUCTION
# ---------------------------------------------------------------------------

def slugify(text: str, max_len: int = 60) -> str:
    text = unicodedata.normalize("NFKD", str(text))
    text = text.encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[^a-zA-Z0-9]+", "_", text).strip("_")
    return text[:max_len].rstrip("_")

def build_filename(info: dict, fallback_stem: str) -> str:
    author = info.get("author")
    year   = info.get("year")
    title  = info.get("title")
    multi  = info.get("multi_author", False)

    parts = []
    if author:
        parts.append(slugify(author) + ("_etal" if multi else ""))
    if year:
        parts.append(str(year))
    if title:
        parts.append(slugify(title, max_len=60))

    return ("_".join(parts) if parts else fallback_stem) + ".pdf"


# ---------------------------------------------------------------------------
# STEP 1: EXTRACT
# ---------------------------------------------------------------------------

def cmd_extract(pdf_dir: str):
    candidates = []
    for dirpath, _, filenames in os.walk(pdf_dir):
        for fname in sorted(filenames):
            if not fname.lower().endswith(".pdf"):
                continue
            fpath = os.path.join(dirpath, fname)
            rel   = os.path.relpath(fpath, pdf_dir)
            text  = extract_text(fpath)
            candidates.append({"file": rel, "text": text})
            print(f"  Extracted: {rel}")

    if not candidates:
        print("No PDFs found.")
        return

    with open(CANDIDATES_PATH, "w", encoding="utf-8") as f:
        json.dump(candidates, f, ensure_ascii=False, indent=2)

    print(f"\nWrote {len(candidates)} entries to {CANDIDATES_PATH}")
    print("\nNext: ask Claude Code to process the candidates:")
    print('  "Process rename_candidates.json with Haiku and write rename_mappings.json"')
    print("\nExpected format for rename_mappings.json:")
    print(json.dumps([{
        "file": "A/10.123_abc.pdf",
        "author": "Smith",
        "multi_author": True,
        "year": "2023",
        "title": "Short descriptive title"
    }], indent=2))


# ---------------------------------------------------------------------------
# STEP 3: APPLY
# ---------------------------------------------------------------------------

def cmd_apply(pdf_dir: str, dry_run: bool):
    if not os.path.exists(MAPPINGS_PATH):
        print(f"ERROR: {MAPPINGS_PATH} not found. Run the Haiku step first.")
        sys.exit(1)

    with open(MAPPINGS_PATH, encoding="utf-8") as f:
        mappings = json.load(f)

    print(f"Applying {len(mappings)} mappings from {MAPPINGS_PATH}")
    if dry_run:
        print("DRY RUN — no files will be renamed.\n")

    log_rows = []
    for entry in mappings:
        rel      = entry["file"]
        old_path = os.path.join(pdf_dir, rel)
        folder   = os.path.dirname(old_path)
        old_name = os.path.basename(old_path)
        stem     = os.path.splitext(old_name)[0]

        if not os.path.exists(old_path):
            print(f"  NOT FOUND: {rel}")
            log_rows.append({"folder": os.path.relpath(folder, pdf_dir),
                              "old_name": old_name, "new_name": old_name,
                              "status": "not_found", **{k: entry.get(k) for k in ("author","year","title")}})
            continue

        new_name = build_filename(entry, stem)

        # Avoid collisions
        candidate = os.path.join(folder, new_name)
        counter   = 1
        while os.path.exists(candidate) and os.path.abspath(candidate) != os.path.abspath(old_path):
            base, ext = os.path.splitext(new_name)
            candidate = os.path.join(folder, f"{base}_{counter}{ext}")
            counter  += 1
        new_name = os.path.basename(candidate)

        status = "renamed" if new_name != old_name else "unchanged"
        print(f"  {old_name}\n    -> {new_name}  [{status}]")

        if not dry_run and new_name != old_name:
            os.rename(old_path, os.path.join(folder, new_name))

        log_rows.append({
            "folder":   os.path.relpath(folder, pdf_dir),
            "old_name": old_name,
            "new_name": new_name,
            "author":   entry.get("author"),
            "year":     entry.get("year"),
            "title":    entry.get("title"),
            "status":   status,
        })

    with open(LOG_PATH, "w", newline="", encoding="utf-8") as f:
        if log_rows:
            writer = csv.DictWriter(f, fieldnames=log_rows[0].keys())
            writer.writeheader()
            writer.writerows(log_rows)

    renamed   = sum(1 for r in log_rows if r["status"] == "renamed")
    unchanged = sum(1 for r in log_rows if r["status"] == "unchanged")
    not_found = sum(1 for r in log_rows if r["status"] == "not_found")
    print(f"\nDone. Renamed: {renamed} | Unchanged: {unchanged} | Not found: {not_found}")
    print(f"Log written to {LOG_PATH}")


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Rename PDFs via Haiku (two-step)")
    parser.add_argument("--extract", action="store_true",
                        help="Step 1: extract PDF text → rename_candidates.json")
    parser.add_argument("--apply",   action="store_true",
                        help="Step 3: apply rename_mappings.json → rename files")
    parser.add_argument("--dry-run", action="store_true",
                        help="Preview --apply without making changes")
    parser.add_argument("--dir",     default=DEFAULT_PDF_DIR,
                        help=f"PDF root directory (default: {DEFAULT_PDF_DIR})")
    args = parser.parse_args()

    if args.extract:
        print(f"Extracting text from PDFs in {args.dir}...\n")
        cmd_extract(args.dir)
    elif args.apply:
        cmd_apply(args.dir, args.dry_run)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
