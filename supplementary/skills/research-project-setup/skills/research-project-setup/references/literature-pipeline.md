# Literature Search Pipeline

An 8-step pipeline from database query to NotebookLM export. Steps marked ✋ require manual action; others are automated by script.

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

### API credentials

- **OpenAlex**: No key required. Register a polite-pool email in `scripts/search_openalex.R` via `EMAIL <- "your@email.com"`.
- **Unpaywall** (roadoi): No key required, but set `UNPAYWALL_EMAIL` in `scripts/download_pdfs.R`.

---

## Pipeline overview

| Step | Action | Output |
|------|--------|--------|
| 1 | `search_openalex.R` | `combined_results.csv` |
| 2 | `filter_results.py --extract` | `filter_candidates.json` |
| 3 | `screen_candidates.py` | `filter_decisions.json` |
| 4 | `filter_results.py --apply` | `openalex_retained.csv` |
| 4 | ✋ Spot-check excluded records | — |
| 5 | `download_pdfs.R` | `literature/pdfs/[A–H]/` |
| 5 | ✋ Review missing PDFs; download manually | — |
| 6 | `rename_pdfs.py --extract` then `--apply` | renamed PDFs |
| 7 | `screen_fulltexts.py` | `fulltext_scores.csv` |
| 7b | `populate_upload_folders.py` | `literature/notebooklm/upload_theme_[a/b/c]/` |
| 7b | ✋ Upload theme folders to NotebookLM | — |
| 7c | ✋ Write search summary report | `search_summary_report.md` |
| 8 | `export_notebooklm.py` | `literature/notebooklm/notebooklm_export/` |
| 8 | ✋ Review composite export | — |

---

## Step 1 — OpenAlex search

**Script:** `scripts/search_openalex.R`

```powershell
Rscript scripts/search_openalex.R
```

Runs keyword queries against the OpenAlex API, deduplicates on DOI, and writes a combined CSV.

### Key parameters (edit at top of script)

```r
EMAIL        <- "your@email.com"    # polite-pool identifier
MAX_RESULTS  <- 400L                # records per block query
OUTPUT_DIR   <- "literature/automated_literature_searches"
```

### Search block structure

Organize searches into keyword blocks (e.g., 6 blocks of related terms). Each block is a separate API call; results are combined and deduplicated. Also include venue-targeted queries for high-impact journals in the domain (e.g., Science, Nature, PNAS).

Document the full boolean strings in `supplementary/boolean-search-guide.md` as a transparency artefact.

---

## Step 2 — Extract candidates for screening

**Script:** `scripts/filter_results.py --extract`

```bash
python scripts/filter_results.py --extract \
  --input literature/automated_literature_searches/combined_results.csv \
  --output literature/automated_literature_searches/filter_tidying/
```

Extracts title, abstract, year, venue, and DOI into a JSON suitable for screening. Applies initial keyword-based pre-filtering to reduce screening burden.

---

## Step 3 — Apply exclusion criteria

**Script:** `scripts/screen_candidates.py`

```bash
python scripts/screen_candidates.py \
  --input literature/automated_literature_searches/filter_tidying/filter_candidates.json \
  --output literature/automated_literature_searches/filter_tidying/filter_decisions.json
```

Applies exclusion rules to generate retain/exclude decisions for each record. Rules should be documented in the script header and in `literature/PIPELINE.md`.

### Typical exclusion criteria

- NLP/computational linguistics papers not relevant to research methodology
- K-12 education AI papers
- Technical AI papers with no research methodology implications
- Non-English sources (if applicable)
- Pre-prints from non-peer-reviewed venues (if applicable)

---

## Step 4 — Apply decisions and spot-check

**Script:** `scripts/filter_results.py --apply`

```bash
python scripts/filter_results.py --apply \
  --decisions literature/automated_literature_searches/filter_tidying/filter_decisions.json \
  --input literature/automated_literature_searches/combined_results.csv \
  --output literature/automated_literature_searches/openalex_retained.csv
```

✋ **Manual checkpoint**: Spot-check a sample of excluded records to verify the exclusion rules are not over-excluding. Document the spot-check outcome in the decision log.

---

## Step 5 — Download PDFs

**Script:** `scripts/download_pdfs.R`

```powershell
Rscript scripts/download_pdfs.R
```

Uses Unpaywall (via roadoi) to retrieve open-access PDFs. Organizes by search string block into `literature/pdfs/[A]/`, `literature/pdfs/[B]/`, etc.

✋ **Manual checkpoint**: Review PDFs that could not be downloaded automatically. Prioritize manual download for high-relevance records (e.g., those matching multiple search blocks or from high-impact venues).

---

## Step 6 — Rename PDFs

**Script:** `scripts/rename_pdfs.py`

```bash
# Extract metadata from PDFs
python scripts/rename_pdfs.py --extract \
  --dir literature/pdfs/

# Apply rename mappings
python scripts/rename_pdfs.py --apply \
  --dir literature/pdfs/
```

Extracts author, year, and title metadata from PDF content; generates standardized filenames (`Author_Year_ShortTitle.pdf`).

---

## Step 7 — Full-text relevance scoring

**Script:** `scripts/screen_fulltexts.py`

```bash
python scripts/screen_fulltexts.py \
  --dir literature/pdfs/ \
  --output literature/automated_literature_searches/fulltext_scores.csv
```

Scores each retained PDF for relevance to each thematic cluster. Scoring is keyword-based by theme.

### Theme structure

Define 2–4 themes corresponding to the paper's main claims requiring literature support. Example:

- **Theme A**: Structured AI use, workflow documentation, explicit criteria
- **Theme B**: Explicit reasoning, open science, pre-registration, reproducibility
- **Theme C**: Journal policy, AI disclosure, research integrity

Composite score = sum of theme scores. Top papers by composite score are prioritized for NotebookLM export.

---

## Step 7b — Populate NotebookLM upload folders

**Script:** `scripts/populate_upload_folders.py`

```bash
python scripts/populate_upload_folders.py \
  --scores literature/automated_literature_searches/fulltext_scores.csv \
  --pdf-dir literature/pdfs/ \
  --output-dir literature/notebooklm/ \
  --top-n 50
```

Copies top N PDFs per theme into `upload_theme_a/`, `upload_theme_b/`, `upload_theme_c/` subfolders.

✋ **Manual checkpoint**: Upload each theme folder to a separate NotebookLM notebook. Configure each notebook with a source-set instruction specifying the theme and the questions it should answer. Document the notebook IDs and configuration in `literature/PIPELINE.md`.

---

## Step 7c — Search summary report

✋ **Manual step**: Write `literature/automated_literature_searches/search_summary_report.md`.

Document: total records retrieved, records retained after screening, PDFs downloaded, PDFs exported to NotebookLM, and the date the search was completed. This is a transparency artefact and part of the replication package.

---

## Step 8 — Export top papers (composite)

**Script:** `scripts/export_notebooklm.py`

```bash
python scripts/export_notebooklm.py \
  --scores literature/automated_literature_searches/fulltext_scores.csv \
  --pdf-dir literature/pdfs/ \
  --output-dir literature/notebooklm/notebooklm_export/ \
  --top-n 50
```

Exports the top 50 papers by composite score (across all themes) to a single folder for a comprehensive NotebookLM notebook.

✋ **Manual checkpoint**: Review the composite export. Verify that no obviously irrelevant papers appear in the top 50, and that key papers identified through other means (citation chasing, known literature) are represented.

---

## Transparency artefacts produced

All of the following constitute the replication package for the literature search:

- Boolean search strings (documented in `supplementary/boolean-search-guide.md`)
- `combined_results.csv` — raw search results
- `filter_decisions.json` — screening decisions with reasons
- `openalex_retained.csv` — retained records after screening
- `fulltext_scores.csv` — relevance scores by theme
- `search_summary_report.md` — summary counts and dates
- `literature/PIPELINE.md` — this documentation
- `scripts/` — all search, filter, and scoring scripts
