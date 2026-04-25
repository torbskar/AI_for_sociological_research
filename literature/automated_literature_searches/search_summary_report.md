# Search and Screening Summary Report

**Project:** Structured AI Use in Sociological Research
**Date:** 2026-04-22
**Pipeline version:** v2 (final run 2026-04-06; PLOS ONE removed 2026-04-11)

---

## Combined pipeline (all search strings)

The search pipeline runs across all search strings simultaneously and produces a single combined pool, which is then scored against each theme separately.

| Stage | N |
|---|---|
| Records retrieved (strings A, B, C, H, D, E, G + venue queries) | 1,479 |
| Retained after abstract screening | 1,407 |
| PDFs successfully downloaded and full-text screened | 1,205 |
| PDFs corrupt/empty (skipped) | 133 |

---

## Per topic — full-text scoring and upload to NotebookLM

| Topic | Description | Full-text score ≥ 3 | Uploaded to NotebookLM |
|---|---|---|---|
| A | Structured AI use in research practice | 470 | 48 |
| B | Explicit reasoning, pre-registration, open science | 428 | 49 |
| C | Journal and publication policy on AI | 443 | 46 |

Upload folders contain the top-scoring papers per theme after deduplication, supplemented by a small number of manually retrieved papers.

---

## Theme overlap

Papers scoring ≥ 3 on more than one theme:

| Overlap | N |
|---|---|
| A ∩ B | 300 |
| A ∩ C | 216 |
| B ∩ C | 185 |
| A ∩ B ∩ C | 136 |

---

## Notes

- Search strings A, B, H (Block 1) primarily target AI in research practice (feeds Theme A).
- Search strings D, E, G (Block 2) primarily target explicit reasoning and open science (feeds Theme B).
- Search string C (Block 1) primarily targets journal policy (feeds Theme C).
- All strings contribute to the shared pool; theme assignment is determined by full-text scoring, not by search string.
- String F (structured workflows) was planned but not executed; coverage considered sufficient via D and G.
- PLOS ONE venue query (103 records) was removed on 2026-04-11 due to systematic false positives in Theme C scoring.
- See `boolean-searches.md` for full query strings and search log; `fulltext_report.md` for score distributions and top papers per theme.
