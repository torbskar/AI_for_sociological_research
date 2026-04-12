"""
screen_fulltexts.py — Full-text relevance screening for literature PDFs

Scores each PDF on three themes relevant to the paper argument:
  A: Structured / systematic AI use in research practice
  B: Explicit reasoning, pre-registration, open science, tacit knowledge
  C: Journal and publication policy on AI

Reads first 3 pages + middle 2 pages + last 2 pages of each PDF
(~8,000 chars) so screening is fast without sacrificing coverage.

Outputs:
  literature/fulltext_scores.csv      — all PDFs, all scores, sorted by composite
  literature/fulltext_theme_a.csv     — top N for Theme A
  literature/fulltext_theme_b.csv     — top N for Theme B
  literature/fulltext_theme_c.csv     — top N for Theme C
  literature/fulltext_report.md       — summary report

Usage:
    python scripts/screen_fulltexts.py [--top-n 75] [--pdf-dir literature/pdfs]
"""

import argparse, csv, sys, re
from pathlib import Path
from collections import defaultdict

try:
    import fitz  # PyMuPDF
except ImportError:
    print("PyMuPDF not installed. Run: pip install pymupdf")
    sys.exit(1)

# ---------------------------------------------------------------------------
# Theme term dictionaries  (term: weight)
# Higher weight = stronger signal for that theme
# ---------------------------------------------------------------------------

THEME_A_TERMS = {
    # Core structured-use concepts
    "structured ai use": 5, "unstructured ai": 5, "structured use of ai": 5,
    "structured workflow": 4, "systematic ai": 4, "ai workflow": 3,
    "prompt template": 4, "skill configuration": 4, "reviewer skill": 4,
    "human verification": 4, "human-in-the-loop": 3, "human oversight": 3,
    "explicit criteria": 4, "documented reasoning": 4,
    "transparency artefact": 5, "replication package": 3,
    "ai methodology": 3, "ai-assisted research": 3, "ai in research": 2,
    # Tacit / explicit knowledge
    "tacit knowledge": 5, "tacit dimension": 5, "polanyi": 5,
    "explicit knowledge": 3, "codified knowledge": 3,
    # Epistemic / research quality angle
    "epistemic": 3, "epistemolog": 3,
    "reproducib": 3, "replicab": 3, "transparency": 2,
    "pre-registr": 3, "preregistr": 3,
    # General AI-in-research (weak signals — presence necessary but not sufficient)
    "generative ai": 1, "large language model": 1, "llm": 1,
    "chatgpt": 1, "gpt-4": 1, "claude": 1,
    "research practice": 2, "research workflow": 2, "research tool": 2,
    "academic writing": 1, "scholarly writing": 1,
}

THEME_B_TERMS = {
    # Pre-registration / open science core
    "pre-registration": 5, "preregistration": 5, "pre-register": 5,
    "registered report": 5, "open science": 4, "open research": 3,
    "replication crisis": 5, "reproducibility crisis": 5,
    "publication bias": 4, "file drawer": 4, "p-hacking": 4,
    "researcher degrees of freedom": 4, "questionable research practice": 4,
    "qrp": 3, "harking": 3,
    "open data": 3, "data sharing": 3, "code sharing": 3,
    "preprint": 2, "osf": 2, "open materials": 3,
    # Tacit / explicit reasoning (overlaps A intentionally)
    "tacit knowledge": 5, "explicit reasoning": 5, "tacit": 3,
    "making reasoning explicit": 4, "articulate": 2,
    # Epistemology / philosophy of science
    "epistemic": 3, "epistemolog": 3, "philosophy of science": 3,
    "knowledge production": 3, "scientific knowledge": 2,
    "inference": 2, "validity": 2, "causal inference": 3,
    # Research integrity
    "research integrity": 4, "scientific integrity": 4,
    "metascience": 4, "meta-science": 4, "science of science": 4,
    "systematic review": 2, "review protocol": 3,
    "transparency": 2, "reproducib": 3,
}

THEME_C_TERMS = {
    # Journal/editorial policy — strongest signals
    "journal policy": 5, "editorial policy": 5, "publication policy": 5,
    "ai policy": 5, "chatgpt policy": 5, "generative ai policy": 5,
    "ai guidelines": 4, "author guidelines": 3, "submission guidelines": 3,
    "manuscript preparation": 2,
    # Disclosure
    "ai disclosure": 5, "disclosure of ai": 4, "declare ai": 4,
    "disclose": 2, "transparency statement": 3,
    # Publication ethics bodies
    "cope": 3, "committee on publication ethics": 5,
    "wame": 4, "icmje": 4, "equator": 3,
    # Authorship / integrity
    "ai authorship": 5, "authorship ai": 5, "ai as author": 4,
    "ghost-writing": 3, "ghost writing": 3,
    "academic integrity": 3, "research misconduct": 3,
    "plagiarism": 3, "ithenticate": 4, "crosscheck": 4, "turnitin": 3,
    # Publishing process
    "peer review": 2, "editorial board": 2, "editor": 1,
    "academic publishing": 3, "scholarly publishing": 3,
    "retraction": 3, "correction": 2,
    # Journals as subject
    "sociological": 2, "sociology journal": 3,
    "social science journal": 3, "journal editor": 3,
}

# ---------------------------------------------------------------------------
# PDF text extraction
# ---------------------------------------------------------------------------

def extract_text(pdf_path, max_chars=9000):
    """
    Extract text from strategic sections of a PDF:
    pages 0-2 (abstract/intro), middle 2 pages, last 2 pages.
    Corrupted or non-PDF files return empty string.
    """
    try:
        doc = fitz.open(str(pdf_path))
        n = len(doc)
        pages_to_read = set()

        # First 3 pages
        for i in range(min(3, n)):
            pages_to_read.add(i)
        # Middle 2 pages
        if n > 6:
            mid = n // 2
            pages_to_read.update([mid, min(mid + 1, n - 1)])
        # Last 2 pages
        if n > 3:
            pages_to_read.update([max(0, n - 2), n - 1])

        parts = []
        for i in sorted(pages_to_read):
            parts.append(doc[i].get_text())
        doc.close()

        combined = " ".join(parts)
        # Normalise whitespace
        combined = re.sub(r'\s+', ' ', combined)
        return combined[:max_chars].lower()
    except Exception:
        return ""

# ---------------------------------------------------------------------------
# Scoring
# ---------------------------------------------------------------------------

def score_text(text, terms):
    """Return (score, list_of_matched_terms)."""
    score = 0
    hits = []
    for term, weight in terms.items():
        if term in text:
            score += weight
            hits.append(term)
    return score, hits

def screen_pdf(pdf_path):
    text = extract_text(pdf_path)
    if not text or len(text) < 100:
        return None  # Skip corrupt / empty files

    sa, ha = score_text(text, THEME_A_TERMS)
    sb, hb = score_text(text, THEME_B_TERMS)
    sc, hc = score_text(text, THEME_C_TERMS)

    # Composite: sum of themes + small bonus for cross-theme relevance
    themes_hit = sum(1 for s in [sa, sb, sc] if s >= 3)
    composite = sa + sb + sc + themes_hit * 3

    return {
        "file": pdf_path.name,
        "subfolder": pdf_path.parent.name,
        "path": str(pdf_path.relative_to(pdf_path.parent.parent.parent)),
        "score_a": sa,
        "score_b": sb,
        "score_c": sc,
        "composite": composite,
        "themes_hit": themes_hit,
        "hits_a": "; ".join(ha[:6]),
        "hits_b": "; ".join(hb[:6]),
        "hits_c": "; ".join(hc[:6]),
    }

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf-dir", default="literature/pdfs")
    parser.add_argument("--out-dir", default="literature/automated_literature_searches")
    parser.add_argument("--top-n", type=int, default=75,
                        help="Top N per theme list (default 75; trim to 50 manually)")
    args = parser.parse_args()

    pdf_dir = Path(args.pdf_dir)
    out_dir = Path(args.out_dir)

    # Collect all PDFs, skipping _corrupt and _missing
    pdfs = [
        p for p in pdf_dir.rglob("*.pdf")
        if "_corrupt" not in p.parts and not p.name.startswith("_")
    ]
    print(f"Found {len(pdfs)} PDFs to screen")

    results = []
    failed = []
    for i, pdf in enumerate(pdfs, 1):
        if i % 50 == 0:
            print(f"  Screened {i}/{len(pdfs)}...")
        rec = screen_pdf(pdf)
        if rec:
            results.append(rec)
        else:
            failed.append(pdf.name)

    print(f"Screened {len(results)} PDFs ({len(failed)} skipped/corrupt)")

    # Sort by composite
    results.sort(key=lambda r: r["composite"], reverse=True)

    # --- Write main CSV ---
    main_csv = out_dir / "fulltext_scores.csv"
    fieldnames = ["subfolder", "file", "path", "composite", "themes_hit",
                  "score_a", "score_b", "score_c",
                  "hits_a", "hits_b", "hits_c"]
    with open(main_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)
    print(f"Main scores written to {main_csv}")

    # --- Theme-specific ranked CSVs ---
    for theme, key, label in [
        ("a", "score_a", "Structured AI use in research practice"),
        ("b", "score_b", "Explicit reasoning, pre-registration, open science"),
        ("c", "score_c", "Journal and publication policy on AI"),
    ]:
        ranked = sorted(results, key=lambda r: r[key], reverse=True)
        ranked = [r for r in ranked if r[key] >= 3]  # Minimum threshold
        top = ranked[:args.top_n]
        out_path = out_dir / f"fulltext_theme_{theme}.csv"
        with open(out_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(top)
        print(f"Theme {theme.upper()} ({label}): {len(top)} papers -> {out_path}")

    # --- Summary report ---
    report = out_dir / "fulltext_report.md"
    with open(report, "w", encoding="utf-8") as f:
        f.write("# Full-Text Screening Report\n\n")
        f.write(f"**Date:** 2026-04-05  \n")
        f.write(f"**PDFs screened:** {len(results)}  \n")
        f.write(f"**Skipped (corrupt/empty):** {len(failed)}  \n\n")
        f.write("## Score distribution\n\n")
        for threshold in [30, 20, 10, 5, 0]:
            n = sum(1 for r in results if r["composite"] >= threshold)
            f.write(f"- Composite ≥ {threshold}: {n} papers\n")
        f.write("\n## Per-theme summary\n\n")
        for theme, key, label in [
            ("A", "score_a", "Structured AI use in research practice"),
            ("B", "score_b", "Explicit reasoning, pre-registration, open science"),
            ("C", "score_c", "Journal and publication policy on AI"),
        ]:
            above = [r for r in results if r[key] >= 3]
            f.write(f"### Theme {theme}: {label}\n")
            f.write(f"Papers with score ≥ 3: **{len(above)}**  \n")
            if above:
                top5 = sorted(above, key=lambda r: r[key], reverse=True)[:5]
                f.write("Top 5:\n")
                for r in top5:
                    f.write(f"- `{r['file']}` (score {r[key]})\n")
                    if r[f'hits_{theme.lower()}']:
                        f.write(f"  Matches: {r[f'hits_{theme.lower()}']}\n")
            f.write("\n")
        f.write("## Theme overlap\n\n")
        ab = sum(1 for r in results if r["score_a"] >= 3 and r["score_b"] >= 3)
        ac = sum(1 for r in results if r["score_a"] >= 3 and r["score_c"] >= 3)
        bc = sum(1 for r in results if r["score_b"] >= 3 and r["score_c"] >= 3)
        abc = sum(1 for r in results if all(r[k] >= 3 for k in ["score_a","score_b","score_c"]))
        f.write(f"- A ∩ B: {ab}  \n- A ∩ C: {ac}  \n- B ∩ C: {bc}  \n- A ∩ B ∩ C: {abc}\n\n")
        f.write("## Suggested NotebookLM sets\n\n")
        f.write("Theme CSVs at `literature/automated_literature_searches/fulltext_theme_[a/b/c].csv` are pre-ranked. ")
        f.write("Take the top 50 from each for upload. Papers scoring high on multiple ")
        f.write("themes can go in all relevant notebooks.\n")
        if failed:
            f.write(f"\n## Skipped files ({len(failed)})\n\n")
            for fn in sorted(failed):
                f.write(f"- {fn}\n")

    print(f"Report written to {report}")
    print()
    print("--- Top 10 overall ---")
    for r in results[:10]:
        print(f"  [{r['composite']:3d}] A={r['score_a']} B={r['score_b']} C={r['score_c']}  {r['file']}")

if __name__ == "__main__":
    main()
