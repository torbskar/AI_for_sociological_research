# Supplementary: Literature Search and Screening Workflow

## Project: Structured AI Use in Sociological Research

---

## Overview

This document describes the structured workflow for literature retrieval, filtering,
and PDF management. It is a transparency artefact documenting the human-AI division
of labour in the search process.

The workflow uses OpenAlex as the primary database (open API, explicit research-use
permissions). All steps are reproducible from the scripts in `scripts/` and the
search terms in `literature/boolean-searches.md`.

**To execute the full pipeline:** use `/lit-search` in Claude Code.

---

## Part 1: Database and search execution

### Database

**Primary:** OpenAlex (`scripts/search_openalex.R`)
- Open API with explicit research-use permissions
- R package: openalexR
- Polite pool: email registered via `options(openalexR.mailto)`

**Secondary (optional):** Semantic Scholar
- Requires API key registration
- Used for AI/ML methodology literature potentially underrepresented in OpenAlex
- Configured in `search_openalex.R` via `SS_API_KEY`

### Search configuration

Search terms are defined in `literature/boolean-searches.md` and translated into
OpenAlex keyword queries in `scripts/search_openalex.R`. OpenAlex does not support
field-specific Boolean syntax; queries are free-text keyword searches.

Key parameters in `search_openalex.R`:
- `EMAIL`: registered email for polite pool (`torbskar@uio.no`)
- `MAX_RESULTS`: records per query (set to 500 for production; 5 for testing)
- `YEAR_FROM`: publication date floor (2020)
- `BLOCKS_TO_RUN`: which search blocks to execute

### Output

`literature/combined_results.csv` — columns: `doi`, `title`, `abstract`,
`publication_year`, `source`, `cited_by_count`, `is_oa`, `oa_url`, `query_label`

---

## Part 2: Haiku filtering

After the OpenAlex search, records are filtered using a Haiku sub-agent before
PDF download. This removes clearly out-of-scope records based on title and abstract.

### Steps

1. `python scripts/filter_results.py --extract`
   → `literature/filter_candidates.json` (title + 400 chars of abstract per record)

2. Haiku screening in Claude Code (batches of 50)
   → `literature/filter_decisions.json`

3. `python scripts/filter_results.py --apply`
   → `literature/openalex_retained.csv`
   → `literature/openalex_excluded.csv`
   → `literature/filter_report.md`

### Exclusion criteria

Records are excluded if the title/abstract clearly indicates:

1. **NLP/text processing focus**: NLP, text mining, sentiment analysis, named entity
   recognition, AI-assisted coding as a technical pipeline
2. **School or K-12 context**: primary/secondary school, K-12, pupils, schoolchildren
   (unless about higher education or academic research practice)
3. **AI affecting non-research outcomes**: business productivity, talent development,
   HR, supply chain, healthcare delivery, clinical diagnosis, customer service,
   financial forecasting
4. **Big data/digitisation frame**: "big data analytics", "digital transformation",
   "Industry 4.0", "smart city"
5. **Prediction or forecasting**: ML for predicting outcomes (crime, stock prices,
   health, recidivism) as the applied method
6. **Pedagogical effectiveness**: AI improving student learning, grades, or providing
   tutoring (unless about research or scholarly writing)

**RETAIN when in doubt.**

### Quality check

After filtering, spot-check a random sample of ~30 excluded records for false
negatives before proceeding to download. Add any false negatives back to retained
set by editing `filter_decisions.json` and re-running `--apply`.

---

## Part 3: PDF download

`Rscript scripts/download_pdfs.R`

Uses Unpaywall API (roadoi package) to retrieve open-access PDFs.

- Input: `literature/openalex_retained.csv`
- Output: `literature/pdfs/[search_letter]/` (one subfolder per search string)
- Missing: `literature/pdfs/[letter]/_missing.md` + `literature/missing_pdfs.csv`

Coverage is typically 40–70% depending on the search block. Papers not retrieved
via Unpaywall require manual retrieval via institutional access.

---

## Part 4: PDF renaming

PDFs are downloaded with DOI-based filenames. The rename step converts these to
`[Author_etal]_[year]_[title].pdf` format using Haiku to extract metadata.

1. `python scripts/rename_pdfs.py --extract`
   → `literature/rename_candidates.json`

2. Haiku extracts author, year, title from metadata + first page text
   → `literature/rename_mappings.json`

3. `python scripts/rename_pdfs.py --apply --dry-run` (preview)
4. `python scripts/rename_pdfs.py --apply` (execute)
5. Log: `literature/rename_log.csv`

---

## Part 5: Full-text screening

After PDF download and renaming, full-text screen retained items. Flag papers
bearing specifically on:

- **A1**: Structured vs. unstructured AI use in research
- **A2**: AI as tool for research (not subject of study)
- **A3**: Transparency, replication, or open science in AI-assisted research
- **C1**: Journal or publication policy regarding AI
- **C2**: Pre-registration or explicit reasoning in research practice
- **C3**: Tacit knowledge and research practice

Import flagged items to NotebookLM as source set for synthesis.

---

## Transparency artefacts produced

| File | Purpose |
|------|---------|
| `literature/boolean-searches.md` | Search terms and strategy |
| `literature/combined_results.csv` | Raw OpenAlex results |
| `literature/filter_candidates.json` | Input to Haiku filtering |
| `literature/filter_decisions.json` | Haiku decisions with reasons |
| `literature/filter_report.md` | Filtering summary by block |
| `literature/openalex_retained.csv` | Records passed to download |
| `literature/openalex_excluded.csv` | Excluded records for audit |
| `literature/pdf_manifest.csv` | Download status per record |
| `literature/missing_pdfs.csv` | Papers not retrieved |
| `literature/rename_log.csv` | PDF rename record |

These files constitute the replication package for the literature search component
and should be included as supplementary materials on submission.
