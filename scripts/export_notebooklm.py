"""
export_notebooklm.py — Copy top N papers per search-letter subfolder to a
single export folder for upload to NotebookLM.

Reads fulltext_scores.csv, takes the top N by composite score within each
subfolder (A, B, C, D, E, G), and copies the PDFs to:
    literature/notebooklm_export/

Use --total-n to cap the total export at exactly N papers (by composite score
across all subfolders), regardless of per-subfolder balance.

Also writes a manifest: literature/notebooklm_export/_manifest.csv

Usage:
    python scripts/export_notebooklm.py [--top-n 10]
    python scripts/export_notebooklm.py [--total-n 50]
"""

import argparse, csv, shutil, sys
from pathlib import Path

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--top-n", type=int, default=10,
                        help="Papers to export per subfolder (default 10)")
    parser.add_argument("--total-n", type=int, default=None,
                        help="Cap total export at exactly N papers by composite score")
    parser.add_argument("--scores", default="literature/automated_literature_searches/fulltext_scores.csv")
    parser.add_argument("--pdf-dir", default="literature/pdfs")
    parser.add_argument("--out-dir", default="literature/notebooklm/notebooklm_export")
    args = parser.parse_args()

    scores_path = Path(args.scores)
    pdf_dir     = Path(args.pdf_dir)
    out_dir     = Path(args.out_dir)

    # Clear existing export (PDFs only, keep manifest from previous run until new one written)
    if out_dir.exists():
        for f in out_dir.glob("*.pdf"):
            f.unlink()
    out_dir.mkdir(parents=True, exist_ok=True)

    # Load scores
    with open(scores_path, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    # Group by subfolder, sort by composite desc
    by_folder = {}
    for r in rows:
        folder = r["subfolder"]
        by_folder.setdefault(folder, []).append(r)

    for folder in by_folder:
        by_folder[folder].sort(key=lambda r: int(r["composite"]), reverse=True)

    # If --total-n set, select top N globally by composite score
    if args.total_n:
        all_sorted = sorted(rows, key=lambda r: int(r["composite"]), reverse=True)
        selected = set()
        count = 0
        for r in all_sorted:
            if count >= args.total_n:
                break
            src = pdf_dir / r["subfolder"] / r["file"]
            if src.exists():
                selected.add((r["subfolder"], r["file"]))
                count += 1
        for folder in by_folder:
            by_folder[folder] = [r for r in by_folder[folder]
                                  if (r["subfolder"], r["file"]) in selected]
        print(f"Selecting top {args.total_n} papers by composite score across all subfolders")

    # Copy selected papers
    manifest = []
    total = 0
    for folder in sorted(by_folder.keys()):
        top = by_folder[folder] if args.total_n else by_folder[folder][:args.top_n]
        if top:
            print(f"\nFolder {folder}: exporting {len(top)}")
        for rank, r in enumerate(top, 1):
            src = pdf_dir / folder / r["file"]
            if not src.exists():
                print(f"  [{rank:2d}] NOT FOUND: {r['file']}")
                continue
            # Prefix filename with subfolder so names stay unique in flat dir
            dest_name = f"{folder}_{r['file']}"
            dest = out_dir / dest_name
            shutil.copy2(str(src), str(dest))
            print(f"  [{rank:2d}] [{r['composite']:>3}] {r['file']}")
            manifest.append({
                "rank_in_folder": rank,
                "subfolder": folder,
                "composite": r["composite"],
                "score_a": r["score_a"],
                "score_b": r["score_b"],
                "score_c": r["score_c"],
                "original_file": r["file"],
                "export_file": dest_name,
                "hits_a": r["hits_a"],
                "hits_b": r["hits_b"],
                "hits_c": r["hits_c"],
            })
            total += 1

    # Write manifest
    manifest_path = out_dir / "_manifest.csv"
    fieldnames = ["subfolder", "rank_in_folder", "composite",
                  "score_a", "score_b", "score_c",
                  "original_file", "export_file",
                  "hits_a", "hits_b", "hits_c"]
    with open(manifest_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(manifest)

    print(f"\nTotal exported: {total} PDFs -> {out_dir}")
    print(f"Manifest: {manifest_path}")

if __name__ == "__main__":
    main()
