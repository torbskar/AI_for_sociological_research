#!/usr/bin/env python3
"""
filter_results.py
Purpose: Filter OpenAlex search results before PDF download, removing articles
         that are clearly outside the scope of this project based on title/abstract.

Two-step workflow (run from project root):

  STEP 1 — Prepare candidates file (no API needed):
      python scripts/filter_results.py --extract
      Input:  literature/combined_results.csv   (output of search_openalex.R)
      Output: literature/filter_candidates.json

  STEP 2 — Run Haiku screening (in Claude Code session):
      Ask Claude Code: "Screen filter_candidates.json with Haiku and write filter_decisions.json"
      Output: literature/filter_decisions.json
      Format: [{"doi": "...", "decision": "RETAIN"|"EXCLUDE", "reason": "..."}, ...]

  STEP 3 — Apply decisions (no API needed):
      python scripts/filter_results.py --apply [--dry-run]
      Input:  literature/filter_decisions.json
      Output: literature/openalex_retained.csv   (input to download_pdfs.R)
              literature/openalex_excluded.csv   (for review)
              literature/filter_report.md        (summary)

Requirements: pip install pandas
"""

import sys, os, json, argparse, csv
from datetime import datetime
sys.stdout.reconfigure(encoding="utf-8")

try:
    import pandas as pd
except ImportError:
    print("ERROR: pip install pandas")
    sys.exit(1)

COMBINED_PATH   = "literature/automated_literature_searches/combined_results.csv"
CANDIDATES_PATH = "literature/automated_literature_searches/filter_tidying/filter_candidates.json"
DECISIONS_PATH  = "literature/automated_literature_searches/filter_tidying/filter_decisions.json"
RETAINED_PATH   = "literature/automated_literature_searches/openalex_retained.csv"
EXCLUDED_PATH   = "literature/automated_literature_searches/openalex_excluded.csv"
REPORT_PATH     = "literature/automated_literature_searches/filter_tidying/filter_report.md"

ABSTRACT_CHARS  = 400   # characters of abstract sent to Haiku per record
BATCH_SIZE      = 50    # records per Haiku call (suggested)

# ---------------------------------------------------------------------------
# EXCLUSION CRITERIA (for documentation and Haiku prompt)
# ---------------------------------------------------------------------------

EXCLUSION_CRITERIA = """
EXCLUDE the article if its title or abstract clearly indicates ANY of the following:

1. NLP/text processing as the focus: natural language processing, NLP, text mining,
   sentiment analysis, named entity recognition, coding of qualitative data using AI
   as a technical pipeline (not as a research assistant).

2. School or K-12 education context: primary school, secondary school, K-12, pupils,
   schoolchildren, classroom instruction — UNLESS the paper is about higher education
   or academic research practice.

3. AI affecting a specific non-research outcome: business productivity, talent
   development, HR, supply chain, healthcare delivery, clinical diagnosis, customer
   service, financial forecasting. The key test: is AI being studied as a tool for
   *doing research*, or is it just a topic applied to some other domain?

4. Big data, analytics, or digitisation as the primary frame: "big data analytics",
   "digital transformation", "Industry 4.0", "smart city" — where AI is one
   component of a broader digitalisation story unrelated to research practice.

5. Prediction or forecasting as the primary purpose: machine learning for prediction
   of outcomes (crime rates, stock prices, health outcomes, recidivism) where AI is
   the method applied to a substantive topic, not the subject of methodological inquiry.

6. Pedagogical effectiveness: whether AI helps students learn better, improves
   academic performance, automates grading, provides tutoring. Include papers that
   discuss AI tools in *research* or *scholarly writing*, not student learning outcomes.

RETAIN if the article:
- Discusses AI as a tool or method in academic research or scholarly writing
- Engages with methodological, epistemological, or ethical dimensions of AI use in research
- Addresses transparency, replication, or open science in the context of AI
- Discusses journal or publication policy regarding AI
- Is about pre-registration, tacit knowledge, or structured research workflows
  (even without AI as the direct subject)
- Is about AI in higher education in the context of research or academic writing

When in doubt, RETAIN.
"""

# ---------------------------------------------------------------------------
# STEP 1: EXTRACT
# ---------------------------------------------------------------------------

def cmd_extract():
    if not os.path.exists(COMBINED_PATH):
        print(f"ERROR: {COMBINED_PATH} not found. Run search_openalex.R first.")
        sys.exit(1)

    df = pd.read_csv(COMBINED_PATH, dtype=str).fillna("")
    print(f"Loaded {len(df)} records from {COMBINED_PATH}")

    candidates = []
    for _, row in df.iterrows():
        abstract = row.get("abstract", "")[:ABSTRACT_CHARS]
        candidates.append({
            "doi":         row.get("doi", ""),
            "title":       row.get("title", ""),
            "abstract":    abstract,
            "year":        row.get("publication_year", ""),
            "source":      row.get("source", ""),
            "query_label": row.get("query_label", ""),
        })

    with open(CANDIDATES_PATH, "w", encoding="utf-8") as f:
        json.dump(candidates, f, ensure_ascii=False, indent=2)

    print(f"Wrote {len(candidates)} candidates to {CANDIDATES_PATH}")
    print(f"\nSuggested batch size for Haiku: {BATCH_SIZE} records per call")
    print(f"Estimated calls needed: {-(-len(candidates) // BATCH_SIZE)} batches")
    print(f"\nExclusion criteria to pass to Haiku:\n{EXCLUSION_CRITERIA}")
    print(f"\nNext: ask Claude Code to screen {CANDIDATES_PATH} with Haiku.")
    print(f"Expected output format for {DECISIONS_PATH}:")
    print(json.dumps([
        {"doi": "10.xxx/yyy", "decision": "RETAIN", "reason": "Discusses AI in research methodology"},
        {"doi": "10.xxx/zzz", "decision": "EXCLUDE", "reason": "About NLP pipeline for text classification"},
    ], indent=2))


# ---------------------------------------------------------------------------
# STEP 3: APPLY
# ---------------------------------------------------------------------------

def cmd_apply(dry_run: bool):
    if not os.path.exists(DECISIONS_PATH):
        print(f"ERROR: {DECISIONS_PATH} not found. Run the Haiku screening step first.")
        sys.exit(1)
    if not os.path.exists(COMBINED_PATH):
        print(f"ERROR: {COMBINED_PATH} not found.")
        sys.exit(1)

    df = pd.read_csv(COMBINED_PATH, dtype=str).fillna("")

    with open(DECISIONS_PATH, encoding="utf-8") as f:
        decisions = json.load(f)

    decision_map = {d["doi"]: d for d in decisions}

    n_in_csv      = len(df)
    n_in_decisions = len(decisions)
    n_matched     = sum(1 for doi in df["doi"] if doi in decision_map)
    n_unmatched   = n_in_csv - n_matched

    print(f"Records in CSV:       {n_in_csv}")
    print(f"Records in decisions: {n_in_decisions}")
    print(f"Matched by DOI:       {n_matched}")
    if n_unmatched:
        print(f"WARNING: {n_unmatched} records have no decision — they will be RETAINED by default")

    def get_decision(doi):
        d = decision_map.get(doi)
        if d is None:
            return "RETAIN", "No decision found — retained by default"
        return d.get("decision", "RETAIN"), d.get("reason", "")

    df["filter_decision"], df["filter_reason"] = zip(*df["doi"].map(get_decision))

    retained = df[df["filter_decision"] == "RETAIN"].drop(columns=["filter_decision", "filter_reason"])
    excluded = df[df["filter_decision"] == "EXCLUDE"].copy()

    n_retained = len(retained)
    n_excluded = len(excluded)

    print(f"\nRetained: {n_retained} ({round(n_retained/n_in_csv*100, 1)}%)")
    print(f"Excluded: {n_excluded} ({round(n_excluded/n_in_csv*100, 1)}%)")

    if dry_run:
        print("\nDRY RUN — no files written.")
        print("\nExclusion reasons (sample):")
        for _, row in excluded.head(10).iterrows():
            print(f"  [{row['filter_decision']}] {row['title'][:70]}")
            print(f"        Reason: {row['filter_reason']}")
        return

    retained.to_csv(RETAINED_PATH, index=False, encoding="utf-8")
    excluded.to_csv(EXCLUDED_PATH, index=False, encoding="utf-8")
    print(f"\nRetained written to: {RETAINED_PATH}")
    print(f"Excluded written to: {EXCLUDED_PATH}")

    # Per-query breakdown
    breakdown = df.groupby(["query_label", "filter_decision"]).size().unstack(fill_value=0)

    # Filter report
    lines = [
        f"# Filter Report",
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"Input: {COMBINED_PATH}  ({n_in_csv} records)",
        f"",
        f"## Summary",
        f"| Decision | N | % |",
        f"|----------|---|---|",
        f"| RETAIN | {n_retained} | {round(n_retained/n_in_csv*100, 1)}% |",
        f"| EXCLUDE | {n_excluded} | {round(n_excluded/n_in_csv*100, 1)}% |",
        f"",
        f"## By search block",
        f"| Query | RETAIN | EXCLUDE |",
        f"|-------|--------|---------|",
    ]
    for label, row in breakdown.iterrows():
        r = int(row.get("RETAIN", 0))
        e = int(row.get("EXCLUDE", 0))
        lines.append(f"| {label} | {r} | {e} |")

    lines += [
        f"",
        f"## Exclusion criteria applied",
        "```",
        EXCLUSION_CRITERIA.strip(),
        "```",
        f"",
        f"## Files",
        f"- Retained: `{RETAINED_PATH}` → input to `download_pdfs.R`",
        f"- Excluded: `{EXCLUDED_PATH}` → for spot-check",
        f"- Decisions: `{DECISIONS_PATH}` → transparency artefact",
    ]

    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Report written to:   {REPORT_PATH}")


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Filter OpenAlex results before PDF download")
    parser.add_argument("--extract", action="store_true",
                        help="Step 1: prepare filter_candidates.json from combined_results.csv")
    parser.add_argument("--apply",   action="store_true",
                        help="Step 3: apply filter_decisions.json → openalex_retained.csv")
    parser.add_argument("--dry-run", action="store_true",
                        help="Preview --apply without writing files")
    args = parser.parse_args()

    if args.extract:
        cmd_extract()
    elif args.apply:
        cmd_apply(args.dry_run)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
