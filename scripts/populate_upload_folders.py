"""
populate_upload_folders.py — Copy top N papers per theme into upload_theme_[a/b/c]/ folders.

Reads the three theme CSVs produced by screen_fulltexts.py and copies the top N PDFs
(by theme score) from literature/pdfs/ into the corresponding upload folders, ready for
direct upload to NotebookLM.

Each upload folder is cleared before populating so the contents always match the current run.

Usage:
    python scripts/populate_upload_folders.py [--top-n 50]
    python scripts/populate_upload_folders.py --top-n 40
    python scripts/populate_upload_folders.py --dry-run
"""

import argparse, csv, shutil
from pathlib import Path

THEME_CSVS = {
    "a": "literature/automated_literature_searches/fulltext_theme_a.csv",
    "b": "literature/automated_literature_searches/fulltext_theme_b.csv",
    "c": "literature/automated_literature_searches/fulltext_theme_c.csv",
}

UPLOAD_DIRS = {
    "a": "literature/notebooklm/upload_theme_a",
    "b": "literature/notebooklm/upload_theme_b",
    "c": "literature/notebooklm/upload_theme_c",
}

SCORE_COLS = {"a": "score_a", "b": "score_b", "c": "score_c"}

PDF_DIR = Path("literature/pdfs")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--top-n", type=int, default=50,
                        help="Papers to copy per theme (default 50, NotebookLM limit)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Print what would be copied without copying")
    args = parser.parse_args()

    for theme in ("a", "b", "c"):
        csv_path  = Path(THEME_CSVS[theme])
        upload_dir = Path(UPLOAD_DIRS[theme])
        score_col  = SCORE_COLS[theme]

        if not csv_path.exists():
            print(f"\nTheme {theme.upper()}: {csv_path} not found — run screen_fulltexts.py first")
            continue

        with open(csv_path, encoding="utf-8") as f:
            rows = list(csv.DictReader(f))

        # Sort by this theme's score descending, take top N
        rows.sort(key=lambda r: int(r[score_col]), reverse=True)
        selected = rows[:args.top_n]

        print(f"\nTheme {theme.upper()}: {len(selected)} papers selected (score_col={score_col})")

        if not args.dry_run:
            # Clear existing PDFs in upload folder
            upload_dir.mkdir(parents=True, exist_ok=True)
            for existing in upload_dir.glob("*.pdf"):
                existing.unlink()

        copied = 0
        missing = 0
        for rank, r in enumerate(selected, 1):
            src = PDF_DIR / r["subfolder"] / r["file"]
            dest = upload_dir / r["file"]
            score = r[score_col]
            composite = r["composite"]

            if not src.exists():
                print(f"  [{rank:2d}] MISSING  [{score:>3}] {r['file']}")
                missing += 1
                continue

            if args.dry_run:
                print(f"  [{rank:2d}] would copy [{score:>3}] {r['file']}")
            else:
                shutil.copy2(str(src), str(dest))
                print(f"  [{rank:2d}] copied   [{score:>3}] (composite {composite}) {r['file']}")
            copied += 1

        if args.dry_run:
            print(f"  -> dry run: {copied} would be copied, {missing} missing")
        else:
            print(f"  -> {copied} copied to {upload_dir}  ({missing} missing)")

    if args.dry_run:
        print("\nDry run complete. Re-run without --dry-run to copy files.")
    else:
        print("\nDone. Upload each folder to its NotebookLM notebook:")
        print("  upload_theme_a  ->  Notebook A (Structured AI use)")
        print("  upload_theme_b  ->  Notebook B (Explicit reasoning / open science)")
        print("  upload_theme_c  ->  Notebook C (Journal and publication policy)")


if __name__ == "__main__":
    main()
