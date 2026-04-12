# Filter Report
Generated: 2026-04-11 09:42
Input: literature/automated_literature_searches/combined_results.csv  (1378 records)

## Summary
| Decision | N | % |
|----------|---|---|
| RETAIN | 1322 | 95.9% |
| EXCLUDE | 56 | 4.1% |

## By search block
| Query | RETAIN | EXCLUDE |
|-------|--------|---------|
| Block 1A: AI in research practice (broad fields) | 191 | 8 |
| Block 1B: AI in research methodology | 157 | 5 |
| Block 1C: AI and journal/publication policy | 171 | 5 |
| Block 1H: AI and research practice (no field restriction) | 187 | 13 |
| Block 2D: Pre-registration and explicit reasoning | 194 | 2 |
| Block 2E: Tacit knowledge | 187 | 13 |
| Block 2G: Structured prompts and epistemic quality | 179 | 9 |
| Venue: Nature | 16 | 1 |
| Venue: Nature Human Behaviour | 7 | 0 |
| Venue: PNAS | 31 | 0 |
| Venue: Science | 2 | 0 |

## Exclusion criteria applied
```
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
```

## Files
- Retained: `literature/automated_literature_searches/openalex_retained.csv` → input to `download_pdfs.R`
- Excluded: `literature/automated_literature_searches/openalex_excluded.csv` → for spot-check
- Decisions: `literature/automated_literature_searches/filter_tidying/filter_decisions.json` → transparency artefact