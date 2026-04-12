# Literature Retrieval: Open Database Strategy
## Project: Structured AI Use in Sociological Research
## Date: 2026-04-05
## Status: Active — replaces Scopus bulk download approach

---

## Overview

This project uses OpenAlex as the primary source for bulk metadata and PDF retrieval,
supplemented by Semantic Scholar and CrossRef where needed. This replaces the original
plan to bulk-download from Scopus exports, which raised unresolved legal questions about
feeding exported data into AI analysis tools.

This is not a formal systematic review. Some coverage loss relative to Scopus is
acceptable. The goal is a thorough, documentable literature base, not exhaustive
systematic coverage.

---

## Primary database: OpenAlex

OpenAlex (https://openalex.org) is a fully open bibliographic database covering
200M+ works. It is built and maintained by OurResearch (same organisation as Unpaywall)
and explicitly permits programmatic access for research purposes. No scraping — it has
a documented REST API and an R package (openalexR).

### R package
```r
install.packages("openalexR")
```

### Key features relevant to this project
- Full API access, no authentication required (polite pool with email)
- Returns metadata including abstracts, DOIs, open access status, and OA URLs
- Can filter by concept, journal, year, citation count
- Directly links to Unpaywall for PDF retrieval
- Terms explicitly permit research use and programmatic access

### API documentation
https://docs.openalex.org

---

## Secondary databases

**Semantic Scholar API** (https://api.semanticscholar.org)
- Good coverage of CS and interdisciplinary AI literature
- Returns abstracts, tldr summaries, citation counts
- Free API, requires key (register at https://www.semanticscholar.org/product/api)
- Use for: AI/ML methodology literature that may be underrepresented in OpenAlex

**CrossRef API** (https://api.crossref.org)
- DOI-based metadata only, no abstracts
- Use for: resolving DOIs, filling metadata gaps, confirming publication details
- R package: rcrossref

---

## Workflow

### Step 1: Search OpenAlex
Run `search_openalex.R` with search terms from `boolean-searches.md`.
Output: `literature/openalex_results.csv`

### Step 2: Deduplicate and merge
If Semantic Scholar is also queried, deduplicate on DOI.
Output: `literature/combined_results.csv`

### Step 3: Abstract screening with Haiku
Pass title + abstract to Haiku for relevance classification.
Inclusion/exclusion criteria are defined in `boolean-searches.md`.
Output: `literature/screened_results.csv` with include/exclude/uncertain column

### Step 4: PDF retrieval
Run `download_pdfs.R` on the included set.
PDFs go to `literature/pdfs/`.
Missing papers logged to `literature/missing_pdfs.csv`.

### Step 5: Full text screening of uncertain cases
Pass full text (first 2 pages) of uncertain cases to Haiku.
Output: append final include/exclude decision to `screened_results.csv`.

### Step 6: Import to NotebookLM
Upload included PDFs to NotebookLM for source-grounded synthesis.
Retain `screened_results.csv` as the documented inclusion record.

---

## Instructions for Claude Code

When working on literature retrieval tasks in this project:

1. Search terms are always read from `literature/boolean-searches.md` — do not
   hardcode terms in scripts.

2. All outputs go to `literature/` with descriptive filenames and dates if
   multiple versions are produced.

3. Log retrieval events in `logs/` when a search run is completed:
   record database queried, search block used, number of results, date.

4. The screened_results.csv is the canonical inclusion record — it must always
   show which papers were included, excluded, or uncertain, with the reason.
   This is a transparency artefact for the paper's methods section.

5. Do not delete intermediate files — keep raw retrieval outputs separate from
   screened outputs so the screening decisions are auditable.

6. If coverage appears thin for a specific search block, flag it rather than
   silently broadening the search. Coverage gaps are documented, not hidden.
