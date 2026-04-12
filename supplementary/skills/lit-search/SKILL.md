---
name: lit-search
description: >
  Run a structured literature search and screening pipeline for any research project.
  Use this skill whenever the user says /lit-search, "run the literature search",
  "start the search", "run the OpenAlex search", "execute the lit search", or wants to
  retrieve and filter academic literature. Runs search_openalex.R to query OpenAlex,
  screen_candidates.py for keyword-based abstract screening, download_pdfs.R to fetch
  open-access PDFs organised by search letter, screen_fulltexts.py for full-text scoring,
  and export_notebooklm.py for NotebookLM upload preparation. Human checkpoints after
  filtering and after download. All outputs go to literature/ in the project root.
  Run all scripts from the project root directory (not from scripts/).
---

# Literature Search Pipeline

Full pipeline from OpenAlex query to renamed PDFs and NotebookLM export.
All outputs go to `literature/` in the project root.
Run all scripts from the project root: `python scripts/script_name.py`

---

## Step 0: Create folder structure

If the folder structure does not yet exist, create it now:

```powershell
mkdir literature
mkdir literature\automated_literature_searches
mkdir literature\automated_literature_searches\filter_tidying
mkdir literature\notebooklm
mkdir literature\notebooklm\notebooklm_configurations
mkdir literature\notebooklm\notebooklm_export
mkdir literature\notebooklm\notebooklm_summaries
mkdir literature\notebooklm\upload_theme_a
mkdir literature\notebooklm\upload_theme_b
mkdir literature\notebooklm\upload_theme_c
mkdir literature\pdfs
mkdir literature\Elicit_export
```

On Linux/macOS use `mkdir -p` instead:

```bash
mkdir -p literature/automated_literature_searches/filter_tidying
mkdir -p literature/notebooklm/{notebooklm_configurations,notebooklm_export,notebooklm_summaries,upload_theme_a,upload_theme_b,upload_theme_c}
mkdir -p literature/pdfs literature/Elicit_export
```

---

## Step 1: Run OpenAlex search

```powershell
Rscript scripts/search_openalex.R
```

Output: `literature/automated_literature_searches/combined_results.csv`

Check the summary at the end of output: total records, records with abstracts, records with OA URLs.

---

## Step 2: Prepare filter candidates

```powershell
python scripts/filter_results.py --extract
```

Output: `literature/automated_literature_searches/filter_tidying/filter_candidates.json`

Note the number of candidates printed to screen.

---

## Step 3: Abstract screening

**Script:** `scripts/screen_candidates.py`

```powershell
python scripts/screen_candidates.py
```

Applies keyword-based exclusion rules to all records in
`literature/automated_literature_searches/filter_tidying/filter_candidates.json`
and writes a decision for each. RETAIN when in doubt — full-text screening (Step 7) handles
precision.

Output: `literature/automated_literature_searches/filter_tidying/filter_decisions.json`

> **Note:** Haiku sub-agents cannot execute Bash and will fail at this step. Use the script
> directly in the main session.

**Exclusion criteria applied by the script — EXCLUDE if the title/abstract clearly indicates:**

1. NLP/text processing as primary focus: NLP, text mining, sentiment analysis, named entity
   recognition, AI-assisted qualitative coding as a technical pipeline
2. School or K-12 context: primary/secondary school, K-12, pupils, schoolchildren — unless
   about higher education or academic research practice
3. AI affecting a non-research outcome: business productivity, HR, supply chain, healthcare
   delivery, clinical diagnosis, customer service, financial forecasting
4. Big data/digitisation frame: "big data analytics", "digital transformation", "Industry 4.0",
   "smart city" — where AI is unrelated to research practice
5. Prediction or forecasting as primary purpose: ML predicting crime, stock prices, health
   outcomes, recidivism — where AI is the applied method, not the subject of inquiry
6. Pedagogical effectiveness: AI improving student learning, grades, tutoring — include if
   about research or scholarly writing, not student learning outcomes

---

## Step 4: Apply filter decisions

Preview first:
```powershell
python scripts/filter_results.py --apply --dry-run
```

If reasonable, execute:
```powershell
python scripts/filter_results.py --apply
```

Outputs:
- `literature/automated_literature_searches/openalex_retained.csv`
- `literature/automated_literature_searches/openalex_excluded.csv`
- `literature/automated_literature_searches/filter_tidying/filter_report.md`

**Human checkpoint**: Spot-check ~30 records from `openalex_excluded.csv` for false negatives
before proceeding. If false negatives found, edit `filter_decisions.json` and re-run `--apply`.

---

## Step 5: Download PDFs

```powershell
Rscript scripts/download_pdfs.R
```

Input: `literature/automated_literature_searches/openalex_retained.csv`
Output: `literature/pdfs/[A-G]/` (one subfolder per search letter)
Missing log: `literature/pdfs/[letter]/_missing.md` and
`literature/automated_literature_searches/missing_pdfs.csv`

Expected coverage: 40–70% depending on search block.

**Human checkpoint**: Review `literature/automated_literature_searches/missing_pdfs.csv` —
papers not retrieved via Unpaywall require manual retrieval via institutional access.

---

## Step 6: Rename PDFs

Extract metadata:
```powershell
python scripts/rename_pdfs.py --extract
```

Output: `literature/automated_literature_searches/filter_tidying/rename_candidates.json`

Generate rename mappings:
```powershell
python scripts/generate_rename_mappings.py
```

Parses metadata from `rename_candidates.json` to extract author surname, year, and short title.
Output: `literature/automated_literature_searches/filter_tidying/rename_mappings.json`

> **Note:** Haiku sub-agents cannot execute Bash. Use `generate_rename_mappings.py` directly.

Preview renames:
```powershell
python scripts/rename_pdfs.py --apply --dry-run
```

Execute renames:
```powershell
python scripts/rename_pdfs.py --apply
```

Log: `literature/automated_literature_searches/filter_tidying/rename_log.csv`

---

## Step 7: Full-text relevance screening

```powershell
python scripts/screen_fulltexts.py --top-n 75
```

Reads first 3 pages + middle + last 2 pages of each PDF. Scores against three themes:
- **A**: Structured / systematic AI use in research practice
- **B**: Explicit reasoning, pre-registration, open science, tacit knowledge
- **C**: Journal and publication policy on AI

Outputs:
- `literature/automated_literature_searches/fulltext_scores.csv` — all PDFs, all scores, sorted by composite
- `literature/automated_literature_searches/fulltext_theme_a.csv` — top 75 for Theme A
- `literature/automated_literature_searches/fulltext_theme_b.csv` — top 75 for Theme B
- `literature/automated_literature_searches/fulltext_theme_c.csv` — top 75 for Theme C
- `literature/automated_literature_searches/fulltext_report.md` — score distribution and theme overlap

**Note**: Screening uses weighted keyword matching across strategic page samples.
PyMuPDF required (`pip install pymupdf`).

---

## Step 7b: Populate NotebookLM upload folders

```powershell
python scripts/populate_upload_folders.py --top-n 50
```

Reads the three theme CSVs and copies the top 50 PDFs per theme into the corresponding
upload folder. Each folder is cleared first so contents always match the current run.
Papers are ranked by per-theme score, not composite, so each folder is theme-optimised.

Preview first:
```powershell
python scripts/populate_upload_folders.py --top-n 50 --dry-run
```

Outputs:
- `literature/notebooklm/upload_theme_a/` — top 50 for Theme A
- `literature/notebooklm/upload_theme_b/` — top 50 for Theme B
- `literature/notebooklm/upload_theme_c/` — top 50 for Theme C

**Human checkpoint**: Upload each folder to its corresponding NotebookLM notebook
(A = Structured AI use, B = Explicit reasoning / open science, C = Journal policy).
Upload from `upload_theme_*/`, NOT from `notebooklm_export/`.

---

## Step 8: Export to NotebookLM

```powershell
python scripts/export_notebooklm.py --top-n 50
```

Copies the top 50 PDFs by composite score from each search-letter subfolder
(A, B, C, D, E, G) to `literature/notebooklm/notebooklm_export/`. Files are
prefixed with their subfolder letter to keep the flat directory navigable.

Outputs:
- `literature/notebooklm/notebooklm_export/[letter]_[filename].pdf` — 300 PDFs total (50 × 6 subfolders)
- `literature/notebooklm/notebooklm_export/_manifest.csv` — scores and theme hits per file

**Human checkpoint**: Review `_manifest.csv` and the exported filenames before uploading.
Use `--total-n 50` instead of `--top-n 50` to select the globally best 50 papers rather than
50 per subfolder. Upload from the `upload_theme_[a/b/c]/` folders in `literature/notebooklm/`
(see PIPELINE.md Step 8b–8c).

---

## After completion

Update the search log table in `literature/automated_literature_searches/boolean-searches.md`
with: date, block, string, database, hits, screened, retained, notes.

Report summary to user:
- Total records retrieved from OpenAlex
- Records retained after abstract filter (and % retained)
- PDFs downloaded (N and %)
- PDFs renamed; corrupt files moved to `_corrupt/`
- Missing PDFs requiring manual retrieval (`literature/automated_literature_searches/missing_pdfs.csv`)
- Full-text screening: papers above composite threshold per theme
- NotebookLM export: N PDFs in `literature/notebooklm/notebooklm_export/`
