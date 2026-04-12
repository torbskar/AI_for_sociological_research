# Dismissed Ideas Log

This folder archives approaches that were tried and abandoned, along with the reasons.
Files remain here for transparency — they document the intellectual history of the project.

---

## 2026-04-06 — Intermediate Haiku-agent filter scripts

**Moved from:** project root

**Files:**
- `filter_script.py`
- `filter_part4.py`
- `process_filter.py`

**Reason:** Experimental scripts written during attempts to run Haiku sub-agents for
abstract screening. Superseded by `scripts/screen_candidates.py` (keyword-based
screener that runs directly in the main session without Bash sub-agent dependency).

---

## 2026-04-05 — Scopus and Web of Science export approach

**Moved from:** `literature/` (Scopus CSV exports and derived files), project root (screening scripts)

**Files:**
- `literature/A_scopus_export_*` and derived `_screened`, `_retained`, `_excluded` files (string A: 309 records, 213 retained)
- `literature/B_scopus_export_*` and derived files (string B: 202 records, 54 retained)
- `literature/C_scopus_export_*` and derived files (string C: 681 records, 261 retained)
- `literature/all_retained_for_zotero.csv`, `literature/all_retained.ris` (515 deduplicated records)
- `literature/SCREENING_REPORT.md`, `literature/RELEVANCE_ASSESSMENT.md`, `literature/spot-check-report.md`
- `literature/assessment*.json`, `literature/sample*.json`, `literature/final_assessment.json`
- `literature/pdfs_manifest.csv`
- `literature/B_retained_summary.txt`, `literature/B_SCREENING_REPORT.txt`
- `screen_literature.py`, `screen_literature_v2.py` (root-level screening scripts)

**Reason (author):** Using output from Scopus and Web of Science with AI tools infringes their database permissions. Their terms prohibit automated bulk processing regardless of whether the tool is local or cloud-based and regardless of training data opt-outs. We restrict to sources that explicitly permit such use. OpenAlex replaces this approach as the primary database (open API, explicit research-use permission).

**Note on PDFs:** The PDFs in `literature/pdfs/` were retrieved via Unpaywall (open access copies) and are legally retained. They remain in `literature/pdfs/`. The manifest linking them to Scopus records (`pdfs_manifest.csv`) is archived here.

---
