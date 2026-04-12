# Boolean Search Terms and Strategy

## Project: Structured AI Use in Sociological Research
## Last updated: 2026-04-06
## Status: v2 strings updated 2026-04-06 — re-run pending. Previous run 2026-04-05 used v1 strings.

---

## SEARCH BLOCK 1: AI use in sociology and social science
### Purpose: Map existing literature on AI tools in sociological/social science research and writing
### Target databases: OpenAlex (primary). Date range: 2020–present.
### Notes: Restrict to peer-reviewed articles and reviews.

**Search string A — broad scope:**
```
("artificial intelligence" OR "large language model*" OR "generative AI" OR "ChatGPT" OR "LLM" OR "GPT")
AND
("research practice" OR "research workflow" OR "research methodology" OR "scientific method*" OR "academic research process")
AND
("social science*" OR "sociology" OR "economics" OR "psychology" OR "political science"
 OR "anthropology" OR "higher education" OR "scientific research" OR "academia" OR "researcher*")
```
*Change from v1: dropped "academic writing" (student/pedagogy noise); replaced with research-process terms;
added economics, psychology, higher education, scientific research, academia, researcher\* to field terms;
added GPT to AI terms.*

**Search string B — methodology focus:**
```
("artificial intelligence" OR "generative AI" OR "large language model*" OR "ChatGPT" OR "AI tool*" OR "AI-assisted")
AND
("research methodology" OR "qualitative research" OR "quantitative research" OR "mixed method*" OR "research design")
AND
("social science*" OR "sociology" OR "economics" OR "psychology" OR "behavioral science*"
 OR "criminology" OR "political science" OR "anthropology")
```
*Change from v1: added AI tool\*, AI-assisted to AI terms; added economics, psychology, behavioral science\*,
research design to field/context terms.*

**Search string C — journal policy focus:**
```
("artificial intelligence" OR "generative AI" OR "ChatGPT" OR "LLM")
AND
("journal polic*" OR "publication polic*" OR "editorial polic*" OR "research integrit*" OR "academic integrit*" OR "author guideline*")
AND
("social science*" OR "sociology" OR "higher education" OR "academic publishing" OR "psychology" OR "economics")
```
*Change from v1: added author guideline\*, psychology, economics.*

**Search string H — cross-disciplinary, no field restriction:**
```
("artificial intelligence" OR "large language model*" OR "generative AI" OR "ChatGPT" OR "LLM" OR "GPT")
AND
("research practice" OR "research workflow" OR "research transparency" OR "open science"
 OR "replication" OR "reproducibility" OR "research integrity" OR "scientific method*")
```
*New in v2. No field restriction — designed to capture interdisciplinary literature in Science, Nature,
PNAS, and similar outlets that do not self-identify with a discipline. Higher screening exclusion rate
expected. Complements the venue-specific OpenAlex queries (see search_openalex.R).*

### Expected yield
- Strings A and B: moderately noisy; screen for research-process focus vs. AI as subject matter
- String C: lower noise due to policy-specific middle term
- String H: higher noise than A–C; full-text screening is the precision gate
- Venue queries: lower noise, run directly in search_openalex.R against Science, Nature, PNAS, NHB (PLOS ONE removed — template text produces false positives in full-text screening)

---

## SEARCH BLOCK 2: Making reasoning explicit — related theoretical literature
### Purpose: Ground the argument that structured practice externalises tacit reasoning, connecting to pre-registration, open science, and epistemology of research
### Target databases: Web of Science, Scopus, Google Scholar (for older classics)
### Notes: This block spans several literatures; treat as targeted rather than exhaustive

**Search string D — pre-registration and explicit reasoning:**
```
("pre-registrat*" OR "preregistrat*" OR "registered report*")
AND
("reasoning" OR "transparency" OR "replicab*" OR "reproducib*" OR "open science")
AND
("social science*" OR "sociology" OR "psychology" OR "economics" OR "criminology")
```
*Change from v1: added economics (AEA registry, RCT pre-registration literature).*

**Search string E — tacit knowledge and explicit knowledge in research practice:**
```
("tacit knowledge" OR "implicit knowledge" OR "explicit knowledge")
AND
("research practice" OR "scientific practice" OR "academic writing" OR "knowledge production")
```
*Note: Polanyi (1966) "The Tacit Dimension" is a key reference — cite directly, not via search.*

**Search string F — structured workflows and research quality:**
```
("structured approach" OR "systematic workflow" OR "protocol*")
AND
("research quality" OR "research transparency" OR "reproducib*" OR "replicab*")
AND
("social science*" OR "qualitative research" OR "quantitative research")
```
*Note: String F was not executed in the 2026-04-05 OpenAlex run. Coverage of structured
workflows and research transparency is partially captured by strings D and G. Revisit if
a targeted supplementary search is needed.*

**Search string G — prompt engineering and structured AI as epistemology:**
```
("prompt engineering" OR "prompt design" OR "structured prompt*")
AND
("epistemic*" OR "reasoning" OR "knowledge production" OR "research quality" OR "reliability")
```
*Note: This block likely thin; may need to rely on preprints (check arXiv, SocArXiv, PsyArXiv)*

**Key works to retrieve directly (do not rely on search):**
- Nosek et al. on open science and pre-registration (Science, 2015; also OSF materials)
- Simmons, Nelson & Simonsohn on researcher degrees of freedom (Psychological Science, 2011)
- Freese & Peterson on replication in sociology (Annual Review of Sociology, 2017)
- Polanyi (1966) The Tacit Dimension — background theory
- Any systematic review of pre-registration effects on research outcomes

---

## SEARCH BLOCK 3: Grey literature — AI in academic research, policy and commentary
### Purpose: Map the policy landscape (journal policies, institutional guidance) and locate relevant commentary in outlets directed at academics
### Strategy: Targeted, not exhaustive — restrict aggressively to avoid noise

### 3A — Journal and publisher policy statements
**Strategy:** Direct retrieval, not database search. Check the following manually:
- Elsevier, Springer/Nature, Sage, Wiley, Taylor & Francis: search "[publisher] AI policy authors 2023 2024 2025"
- COPE (Committee on Publication Ethics): https://publicationethics.org — search for AI guidance
- ASA (American Sociological Association): check publications policy pages
- BSA (British Sociological Association): check ethics guidelines

**Google search strings for policy documents:**
```
"AI policy" "academic publishing" "authors" filetype:pdf 2023..2025
"generative AI" "journal policy" "social science" 2023..2025
"ChatGPT" "author guidelines" sociology OR "social science" 2024 2025
```

### 3B — Targeted outlet search
**Outlets to search manually or via site-specific Google:**
- *The Scholarly Kitchen* (site:scholarlykitchen.sspnet.org): search "AI research workflow" "structured AI" "generative AI methodology"
- *Chronicle of Higher Education* (site:chronicle.com): restrict to articles discussing AI tools in research *process*, not AI in education generally
- *Times Higher Education* (site:timeshighereducation.com): same restriction
- *Khrono* (site:khrono.no): Norwegian higher education — relevant for European policy context; search "kunstig intelligens forskning" and "KI akademisk"
- *Inside Higher Ed* (site:insidehighered.com): restrict to research workflow, not classroom use

**Restriction criteria — INCLUDE only if:**
- Discusses AI in the *research process* (not just teaching or student writing)
- Engages with methodological or epistemological implications
- Makes a structured or policy argument (not just opinion)
- Written by or for researchers, not students

**Restriction criteria — EXCLUDE:**
- Generic AI hype or fear pieces without methodological substance
- Student plagiarism/integrity pieces (unless they discuss researcher practice)
- Pieces about AI detection tools
- Vendor promotional content

### 3C — Preprint servers
**Databases:** SocArXiv (osf.io/preprints/socarxiv), PsyArXiv, arXiv (cs.DL — digital libraries)

```
("AI" OR "artificial intelligence" OR "LLM" OR "ChatGPT")
AND
("research workflow" OR "academic writing" OR "literature review" OR "research methodology")
AND
("sociology" OR "social science*")
```
*Note: Preprints move fast; this block may contain the most current methodological thinking.*

---

## File naming convention

All export and screening files are prefixed with the search string letter matching the strings defined in this document (A, B, C for Block 1; D, E, F, G for Block 2):

```
[String]_[database]_export_[YYYY-MM-DD]_[uuid].csv          ← raw export from database
[String]_[database]_export_[YYYY-MM-DD]_[uuid]_screened.csv ← Phase 1 output (all records + classification columns)
[String]_[database]_export_[YYYY-MM-DD]_[uuid]_retained.csv ← Phase 1 output (RETAIN records only)
```

Example: `B_scopus_export_2026-04-04_[uuid].csv`

---

## Search log
| Date | Block | String | Database | Hits | Screened | Retained | Notes |
|------|-------|--------|----------|------|----------|----------|-------|
| 2026-04-04 | 1 | A | Scopus | 309 | 309 | 213 | Phase 1 + spot-check complete; 2 false negatives recovered |
| 2026-04-04 | 1 | B | Scopus | 202 | 202 | 54 | Phase 1 + spot-check complete; 1 false negative recovered |
| 2026-04-04 | 1 | C | Scopus | 681 | 681 | 261 | Phase 1 complete; 38.3% retain; 0 uncertain |
| 2026-04-05 | 1–2 | A | OpenAlex | 200 | 200 | 182 | v1 strings; MAX_RESULTS=200; keyword screen; spot-check clean |
| 2026-04-05 | 1–2 | B | OpenAlex | 200 | 200 | 196 | As above |
| 2026-04-05 | 1–2 | C | OpenAlex | 200 | 200 | 190 | As above |
| 2026-04-05 | 2 | D | OpenAlex | 200 | 200 | 179 | As above |
| 2026-04-05 | 2 | E | OpenAlex | 200 | 200 | 162 | As above |
| 2026-04-05 | 2 | G | OpenAlex | 200 | 200 | 164 | As above |
| 2026-04-05 | — | — | Combined | 1133 | 1133 | 1073 | v1 run total; 60 excluded (5.3%); 558 PDFs downloaded (52%) |
| 2026-04-06 | 1–2 | A | OpenAlex | 200 | 200 | — | v2 strings; economics/psychology added; capped at 200 |
| 2026-04-06 | 1–2 | B | OpenAlex | 200 | 200 | — | As above |
| 2026-04-06 | 1–2 | C | OpenAlex | 200 | 200 | — | As above |
| 2026-04-06 | 1 | H | OpenAlex | 200 | 200 | — | New; no field restriction |
| 2026-04-06 | 2 | D | OpenAlex | 200 | 200 | — | Economics added |
| 2026-04-06 | 2 | E | OpenAlex | 200 | 200 | — | Unchanged |
| 2026-04-06 | 2 | G | OpenAlex | 200 | 200 | — | Unchanged |
| 2026-04-06 | Venue | — | OpenAlex | 163 | 163 | — | Science:2 Nature:17 PNAS:34 NHB:7 PLOS ONE:103; ISSN filter |
| 2026-04-06 | — | — | Combined | 1479 | 1479 | 1407 | After dedup; 72 excluded (4.9%); 851 new PDFs downloaded; 1409 total on disk |

---

## Deduplication and screening protocol
1. Run `search_openalex.R` → `literature/automated_literature_searches/combined_results.csv`
2. Run `python scripts/filter_results.py --extract` → `literature/automated_literature_searches/filter_tidying/filter_candidates.json`
3. Run `python scripts/screen_candidates.py` → `literature/automated_literature_searches/filter_tidying/filter_decisions.json`
4. Run `python scripts/filter_results.py --apply` → `literature/automated_literature_searches/openalex_retained.csv`
5. Spot-check a sample of `openalex_excluded.csv` for false negatives
6. Run `download_pdfs.R` on `openalex_retained.csv`
7. Run `python scripts/rename_pdfs.py --extract`, then `python scripts/generate_rename_mappings.py`, then `rename_pdfs.py --apply`
8. Full-text screen PDFs; flag items bearing on (a) structured vs unstructured AI use, (b) explicit reasoning, (c) journal policy
9. Import flagged items to NotebookLM as source set for synthesis

## Exclusion criteria (applied at step 3 by screen_candidates.py)

**EXCLUDE if the title/abstract clearly indicates:**

1. **NLP/text processing as primary focus**: natural language processing, NLP, text mining, sentiment analysis, named entity recognition, AI-assisted coding of qualitative data as a technical pipeline
2. **School or K-12 context**: primary school, secondary school, K-12, pupils, schoolchildren — unless the paper discusses higher education or academic research practice
3. **AI affecting a specific non-research outcome**: business productivity, talent development, HR, supply chain, healthcare delivery, clinical diagnosis, customer service, financial forecasting — where AI is not being studied as a tool for *doing research*
4. **Big data / digitisation frame**: "big data analytics", "digital transformation", "Industry 4.0", "smart city" — where AI is one component of a broader digitalisation story unrelated to research practice
5. **Prediction or forecasting as primary purpose**: ML for predicting outcomes (crime rates, stock prices, health outcomes, recidivism) — where AI is the applied method, not the subject of methodological inquiry
6. **Pedagogical effectiveness**: whether AI helps students learn better, improves academic performance, automates grading, provides tutoring — include only if about research or scholarly writing, not student learning outcomes

**RETAIN when in doubt.**

---

## Notes and open questions
- Is there existing work distinguishing structured/unstructured AI use in this sense? Check Doshi-Velez & Kim (2017) on interpretable ML as a possible analogy.
- Sociology of science angle: is there a Latour/Woolgar-style ethnography of AI-in-research-practice yet? Probably not but worth checking.
- Wickham or similar on literate programming as a precursor to the "documented reasoning" argument?
