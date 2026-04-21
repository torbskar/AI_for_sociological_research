# Literature Search Pipeline — User Guide

**Project:** Structured AI Use in Sociological Research
**Last updated:** 2026-04-05
**Status:** Active — update this file when scripts or steps change

This guide describes the full literature search pipeline from database query to
NotebookLM export. It is written for the project author and for anyone seeking
to reproduce or extend the search.

The pipeline is also encoded as a Claude Code skill (`/lit-search`) which
executes the automated steps. This guide documents what that skill does and
what the user must do manually at each checkpoint.

---

## Prerequisites

### R packages

```r
install.packages(c("openalexR", "tidyverse", "roadoi", "jsonlite"))
```

### Python packages

```bash
pip install pymupdf
```

PyMuPDF (`fitz`) is required for Steps 7. All other scripts use only the
Python standard library.

### API credentials

- **OpenAlex**: No key required. Register a polite-pool email in
  `scripts/search_openalex.R` via `EMAIL <- "your@email.com"`.
- **Unpaywall** (roadoi): No key required, but an email must be provided.
  Set `UNPAYWALL_EMAIL` in `scripts/download_pdfs.R`.

---

## Overview of steps

| Step | Script / action | Output |
|------|----------------|--------|
| 1 | `search_openalex.R` | `literature/automated_literature_searches/combined_results.csv` |
| 2 | `filter_results.py --extract` | `literature/automated_literature_searches/filter_tidying/filter_candidates.json` |
| 3 | `screen_candidates.py` | `literature/automated_literature_searches/filter_tidying/filter_decisions.json` |
| 4 | `filter_results.py --apply` | `literature/automated_literature_searches/openalex_retained.csv` |
| 4 | ✋ Spot-check excluded | — |
| 5 | `download_pdfs.R` | `literature/pdfs/[A–G]/` |
| 5 | ✋ Review missing PDFs | — |
| 6 | `rename_pdfs.py --extract` then `--apply` | renamed PDFs |
| 7 | `screen_fulltexts.py` | `literature/automated_literature_searches/fulltext_scores.csv` |
| 7b | `populate_upload_folders.py` | `literature/notebooklm/upload_theme_[a/b/c]/` |
| 7b | ✋ Upload theme folders to NotebookLM | — |
| 8 | `export_notebooklm.py` | `literature/notebooklm/notebooklm_export/` |
| 8 | ✋ Review composite export | — |

---

## Step 1 — OpenAlex search

**Script:** `scripts/search_openalex.R`

```powershell
Rscript scripts/search_openalex.R
```

Runs six keyword queries against the OpenAlex API, deduplicates on DOI, and
writes a combined CSV.

### Key parameters (edit at top of script)

| Parameter | Default | Notes |
|-----------|---------|-------|
| `EMAIL` | `torbskar@uio.no` | Polite-pool identifier |
| `MAX_RESULTS` | `400L` | Records per block query |
| `VENUE_MAX_RESULTS` | `200L` | Records per venue journal query |
| `YEAR_FROM` | `2020` | Earliest publication year |

### Search blocks

| Label | Description |
|-------|-------------|
| Block 1A | AI in research practice (broad fields — includes economics, psychology) |
| Block 1B | AI in research methodology (expanded fields) |
| Block 1C | AI and journal/publication policy |
| Block 1H | AI and research practice — no field restriction (new in v2) |
| Block 2D | Pre-registration and explicit reasoning |
| Block 2E | Tacit knowledge |
| Block 2G | Structured prompts and epistemic quality |

### Venue queries (run automatically with block queries)

Separate content-based queries filtered to five interdisciplinary journals:
Science, Nature, PNAS, Nature Human Behaviour. (PLOS ONE removed: high volume and standard
template text produce false positives in full-text screening with little payoff.)
These use ISSN filtering in OpenAlex and a broader search string with no field restriction.
Results are combined with block queries before deduplication.

See `literature/boolean-searches.md` for full query strings.

### Output

`literature/automated_literature_searches/combined_results.csv` — columns:
`doi`, `title`, `abstract`, `publication_year`, `source_display_name`,
`cited_by_count`, `is_oa`, `oa_url`, `pdf_url`, `query_label`

### What to check

The script prints a summary at the end. Verify:
- Total records retrieved matches expectations (200 per query × 6 = 1,200 max before dedup)
- "With abstracts" is >90% of total (low abstract coverage indicates a problem with the query or API)
- "With OA URL" gives a sense of expected PDF coverage downstream

---

## Step 2 — Prepare filter candidates

**Script:** `scripts/filter_results.py --extract`

```powershell
python scripts/filter_results.py --extract
```

Reads `combined_results.csv` and writes a compact JSON file containing only
the fields needed for screening (DOI, title, 400-char abstract).

### Output

`literature/automated_literature_searches/filter_tidying/filter_candidates.json`

The script also prints a suggested batch size and exclusion criteria to use
in Step 3.

---

## Step 3 — Abstract screening

**Script:** `scripts/screen_candidates.py`

```powershell
python scripts/screen_candidates.py
```

Applies keyword-based exclusion rules to all records and writes a decision
for each (RETAIN or EXCLUDE with reason).

### Exclusion criteria

Records are excluded if the title/abstract clearly indicates any of:

1. **NLP/text processing** as primary focus: NLP, text mining, sentiment
   analysis, named entity recognition, qualitative coding pipeline
2. **K-12 school context**: primary/secondary school, K-12, pupils,
   schoolchildren — unless about higher education or research practice
3. **Non-research AI outcome**: business productivity, HR, supply chain,
   healthcare delivery, clinical diagnosis, customer service, financial
   forecasting
4. **Big data/digitisation frame**: "big data analytics", "digital
   transformation", "Industry 4.0", "smart city" — unrelated to research
   practice
5. **Prediction as primary purpose**: ML predicting crime, stock prices,
   health outcomes, recidivism as applied method
6. **Pedagogical effectiveness**: AI improving student learning or grades —
   include if the paper is about research or scholarly writing

**Default: RETAIN when in doubt.** The filter is conservative; the full-text
screen (Step 7) does the precision work.

### Output

`literature/automated_literature_searches/filter_tidying/filter_decisions.json` — array of `{doi, decision, reason}`

### Notes

The script uses pattern matching, not semantic inference. Papers may be
retained that a human would exclude and vice versa. The spot-check in Step 4
is the main quality gate.

---

## Step 4 — Apply decisions and spot-check

### 4a — Dry run

```powershell
python scripts/filter_results.py --apply --dry-run
```

Review the sample of excluded records printed to screen. If any look wrong,
edit `filter_decisions.json` and re-run.

### 4b — Apply

```powershell
python scripts/filter_results.py --apply
```

### Outputs

| File | Contents |
|------|----------|
| `literature/automated_literature_searches/openalex_retained.csv` | Records passed to PDF download |
| `literature/automated_literature_searches/openalex_excluded.csv` | Excluded records (for audit) |
| `literature/automated_literature_searches/filter_tidying/filter_report.md` | Summary by exclusion reason |

### ✋ Manual check

Open `literature/openalex_excluded.csv` and review a sample — ideally all
excluded records if the count is manageable (<100), otherwise a random sample
of ~30. Look for false negatives: clearly relevant papers that were excluded
by the keyword filter.

To recover false negatives: edit `filter_tidying/filter_decisions.json` (change EXCLUDE to
RETAIN for the affected DOIs) and re-run `filter_results.py --apply`.

---

## Step 5 — Download PDFs

**Script:** `scripts/download_pdfs.R`

```powershell
Rscript scripts/download_pdfs.R
```

Queries Unpaywall for open-access PDF URLs and downloads them. Downloads are
organised into subfolders matching the search letter (`A`–`G`).

### Outputs

| Path | Contents |
|------|----------|
| `literature/pdfs/[A–G]/` | Downloaded PDFs |
| `literature/pdfs/[letter]/_missing.md` | Papers not downloaded, per letter |
| `literature/automated_literature_searches/missing_pdfs.csv` | All missing papers combined |
| `literature/automated_literature_searches/pdf_manifest.csv` | Download status for every DOI |

Expected coverage: **40–70%** of retained records. Many failures are papers
with an OA URL in Unpaywall that nevertheless serve a redirect or login page
(HTTP 403). Corrupt downloads are moved to `_corrupt/` subfolders.

### ✋ Manual check

Open `literature/missing_pdfs.csv`. For papers you know are important,
retrieve them manually via:
- UiO library (Oria) — institutional Wiley, Elsevier, Sage access
- Unpaywall browser extension — try the DOI link directly
- Author's personal/institutional page
- Request via ResearchGate or email

Save any manually retrieved PDFs to the appropriate `literature/pdfs/[letter]/`
subfolder with the filename format `[DOI].pdf` (the rename step will handle
the rest).

Return to this step after adding manual papers before proceeding.

---

## Step 6 — Rename PDFs

Renames PDFs from DOI-based filenames to `[Author_etal]_[year]_[title].pdf`.

### 6a — Extract metadata

```powershell
python scripts/rename_pdfs.py --extract
```

Reads PDF metadata and first-page text for all files.
Output: `literature/automated_literature_searches/filter_tidying/rename_candidates.json`

### 6b — Generate mappings

```powershell
python scripts/generate_rename_mappings.py
```

Parses metadata to extract author surname, year, and short title.
Output: `literature/automated_literature_searches/filter_tidying/rename_mappings.json`

### 6c — Preview and apply

```powershell
python scripts/rename_pdfs.py --apply --dry-run   # preview
python scripts/rename_pdfs.py --apply             # execute
```

Log: `literature/automated_literature_searches/filter_tidying/rename_log.csv`

### Notes

Automatic renaming is imperfect. Common failure modes:
- Files that downloaded as redirect pages (renamed to `Unknown_XXXX_Redirecting.pdf`)
  — these are moved to `_corrupt/` automatically
- Books or reports without standard title-page metadata (year appears as `XXXX`)
- Multi-word institutional author names extracted as a single token

Rename quality is sufficient for filing; corrections can be made manually
for papers you intend to cite.

---

## Step 7 — Full-text relevance screening

**Script:** `scripts/screen_fulltexts.py`

```powershell
python scripts/screen_fulltexts.py --top-n 75
```

Scores each PDF against three themes using weighted keyword matching on
strategic page samples (first 3 pages + middle 2 pages + last 2 pages).

### Themes

| Theme | Description |
|-------|-------------|
| **A** | Structured / systematic AI use in research practice |
| **B** | Explicit reasoning, pre-registration, open science, tacit knowledge |
| **C** | Journal and publication policy on AI |

### Parameters

| Parameter | Default | Notes |
|-----------|---------|-------|
| `--top-n` | `75` | Papers per theme CSV. Set higher for wider coverage. |
| `--pdf-dir` | `literature/pdfs` | Source PDF directory |

### Outputs

| File | Contents |
|------|----------|
| `literature/automated_literature_searches/fulltext_scores.csv` | All PDFs scored, sorted by composite |
| `literature/automated_literature_searches/fulltext_theme_a.csv` | Top 75 for Theme A |
| `literature/automated_literature_searches/fulltext_theme_b.csv` | Top 75 for Theme B |
| `literature/automated_literature_searches/fulltext_theme_c.csv` | Top 75 for Theme C |
| `literature/automated_literature_searches/fulltext_report.md` | Score distribution and theme overlap |

### What to check

Open `fulltext_report.md` for an overview. Then open each theme CSV — the
`hits_[a/b/c]` column shows which terms triggered the score, which helps
identify false positives (high-scoring papers that are not actually relevant).

The scoring is conservative: a paper needs multiple matching terms to score
highly. Low scores do not necessarily mean irrelevant — they may simply be
papers that discuss the themes without using the exact terms.

---

## Step 7b — Populate NotebookLM upload folders

**Script:** `scripts/populate_upload_folders.py`

```powershell
python scripts/populate_upload_folders.py --top-n 50
```

Reads the three theme CSVs and copies the top 50 PDFs per theme into the corresponding
upload folder, clearing each folder first so contents always match the current run.

Preview before copying:

```powershell
python scripts/populate_upload_folders.py --top-n 50 --dry-run
```

### Parameters

| Parameter | Default | Notes |
|-----------|---------|-------|
| `--top-n` | `50` | Papers per theme. 50 = NotebookLM source limit per notebook. |
| `--dry-run` | off | Print what would be copied without copying |

### Outputs

| Folder | Contents |
|--------|----------|
| `literature/notebooklm/upload_theme_a/` | Top 50 PDFs for Theme A |
| `literature/notebooklm/upload_theme_b/` | Top 50 PDFs for Theme B |
| `literature/notebooklm/upload_theme_c/` | Top 50 PDFs for Theme C |

Papers are sorted by their per-theme score (not composite), so each folder contains
the papers most relevant to that specific theme.

> **Note:** `notebooklm_export/` (output of Step 8) is a separate flat dump by composite
> score used for review. Upload to NotebookLM from the `upload_theme_*/` folders, not
> from `notebooklm_export/`.

---

## Step 8 — Export to NotebookLM

**Script:** `scripts/export_notebooklm.py`

```powershell
python scripts/export_notebooklm.py --top-n 10
```

Copies the top `--top-n` PDFs by composite score from each search-letter
subfolder to a flat export directory.

### Parameters

| Parameter | Default | Notes |
|-----------|---------|-------|
| `--top-n` | `10` | Papers per subfolder. 10 × 6 subfolders = 60 total. |
| `--out-dir` | `literature/notebooklm/notebooklm_export` | Destination folder |

### Outputs

| File | Contents |
|------|----------|
| `literature/notebooklm/notebooklm_export/[letter]_[filename].pdf` | Exported PDFs |
| `literature/notebooklm/notebooklm_export/_manifest.csv` | Scores and hits per file |

### ✋ Manual steps — review, upload, and configure

**8a — Review export**

1. Open `literature/notebooklm_export/_manifest.csv`. Verify that the top
   papers in each subfolder are plausibly relevant (check composite score
   and `hits_a/b/c` columns).
2. Remove any obvious false positives from the export folder before uploading.

**8b — Create notebooks**

Create three separate notebooks in NotebookLM, one per theme:

| Notebook | Sources | Upload folder | Report template |
|----------|---------|--------------|----------------|
| A — Structured AI use | Top 50 from `fulltext_theme_a.csv` | `literature/notebooklm/upload_theme_a/` | `notebooklm_configurations/notebooklm_report_A.md` |
| B — Explicit reasoning / open science | Top 50 from `fulltext_theme_b.csv` | `literature/notebooklm/upload_theme_b/` | `notebooklm_configurations/notebooklm_report_B.md` |
| C — Journal policy | Top 50 from `fulltext_theme_c.csv` | `literature/notebooklm/upload_theme_c/` | `notebooklm_configurations/notebooklm_report_C.md` |

Papers scoring highly on multiple themes can be added to more than one notebook.

**8c — Upload PDFs**

For each notebook, upload from the corresponding `upload_theme_[a/b/c]/` folder
in `literature/notebooklm/`. These are pre-selected copies ready for one-click
upload. Files are sourced from `literature/pdfs/[subfolder]/[file]` per the
theme CSV.

**8d — Configure the chat window**

Before running any queries, set the notebook's instruction field using the
configuration in `literature/notebooklm/notebooklm_configurations/example-notebooklm-configuration.md`.
Use the full-version instruction for the relevant notebook (A, B, or C).
This must be done for each notebook separately.

**8e — Run queries and fill report template**

Open the corresponding report template (`literature/notebooklm/notebooklm_configurations/notebooklm_report_[A/B/C].md`)
and run the queries in sequence, pasting responses into the template as you go.
See the instructions block at the bottom of each template for query order and
follow-up guidance.

### NotebookLM notebook limit

NotebookLM currently supports up to 50 sources per notebook. With
`--top-n 10` and 6 subfolders the default export is 60 files — trim to 50
by removing the lowest-scoring papers from `_manifest.csv` before uploading,
or reduce `--top-n` to `8`.

---

## Key files reference

| File | Role |
|------|------|
| `literature/automated_literature_searches/boolean-searches.md` | Search terms, strategy, and search log |
| `literature/automated_literature_searches/combined_results.csv` | Raw OpenAlex results |
| `literature/automated_literature_searches/filter_tidying/filter_candidates.json` | Input to abstract screening |
| `literature/automated_literature_searches/filter_tidying/filter_decisions.json` | Screening decisions with reasons |
| `literature/automated_literature_searches/openalex_retained.csv` | Retained records passed to download |
| `literature/automated_literature_searches/openalex_excluded.csv` | Excluded records (auditable) |
| `literature/automated_literature_searches/filter_tidying/filter_report.md` | Exclusion summary |
| `literature/automated_literature_searches/pdf_manifest.csv` | Download status per DOI |
| `literature/automated_literature_searches/missing_pdfs.csv` | PDFs not retrieved — manual follow-up |
| `literature/automated_literature_searches/filter_tidying/rename_log.csv` | PDF rename record |
| `literature/automated_literature_searches/fulltext_scores.csv` | Full-text relevance scores (all PDFs) |
| `literature/automated_literature_searches/fulltext_theme_[a/b/c].csv` | Top papers per theme |
| `literature/automated_literature_searches/fulltext_report.md` | Full-text screening summary |
| `literature/notebooklm/notebooklm_export/_manifest.csv` | NotebookLM export contents |

---

## Running the full pipeline

The pipeline can be run step by step (as above) or via the Claude Code skill:

```
/lit-search
```

The skill runs Steps 1–8 in sequence, pausing at each ✋ checkpoint for
human review before continuing.

---

## Changelog

| Date | Change |
|------|--------|
| 2026-04-05 | Initial pipeline run: 1,133 records, 1,073 retained, 558 PDFs downloaded, Step 6 (renaming) skipped, 300 exported to NotebookLM (50 per subfolder) |
| 2026-04-05 | Added Steps 7–8 (full-text screening and NotebookLM export) |
| 2026-04-05 | Step 8 expanded with manual notebook setup, upload, configuration, and report template instructions |
| 2026-04-11 | Folder restructure: search outputs moved to `literature/automated_literature_searches/`; intermediate files to `filter_tidying/`; all NotebookLM materials to `literature/notebooklm/` with `upload_theme_[a/b/c]/` upload folders; all script paths and documentation updated accordingly |
