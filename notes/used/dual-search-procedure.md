# Dual Search Procedure

## The argument

The literature search for this paper uses two complementary routes, and both must be
documented in the methods section:

**Route 1 — OpenAlex automated pipeline** (documented in PIPELINE.md and scripts/)
- Keyword block queries + venue queries against OpenAlex API
- Automated abstract screening via keyword exclusion rules
- Open-access PDF download via Unpaywall
- Full-text relevance scoring across three themes
- Automatic retrieval rate: ~58% of retained records (429 missing)
- This route is fully reproducible: scripts, search strings, and decision logs are all
  in the supplementary materials

**Route 2 — Manual and Elicit searches**
- Elicit (elicit.com): semantic search against scientific literature, good for finding
  directly relevant papers that keyword searches miss
- Manual retrieval: key papers identified from citations, known authors, or targeted
  Google Scholar / database searches
- These searches found several papers that the OpenAlex pipeline did not retrieve,
  including Davidson & Karell (2025), Blanchard et al. (2025), Mondal et al., Zeng et al.,
  Ludwig et al., Törnberg et al.
- Elicit exports should be saved to literature/Elicit_export/ for transparency

## Why both are needed

The OpenAlex pipeline is good for breadth and reproducibility, but:
- Keyword queries miss papers that use different terminology
- PNAS/Nature venue queries help but not all flagship work is in those journals
- 42% of retained records have no open-access PDF, limiting full-text scoring
- The screener scores only papers with PDFs, so highly relevant paywalled papers
  are invisible to the automated ranking

Elicit and manual searches provide:
- Targeted retrieval of known important papers
- Semantic similarity rather than keyword matching
- Coverage of preprints and working papers not in OpenAlex

## Documentation requirements for the paper

The methods section should report:
1. Search strategy: OpenAlex (block + venue queries, strings documented in boolean-searches.md)
   supplemented by Elicit semantic searches and manual retrieval
2. Total records from automated search: 1,378 (after deduplication)
3. Records retained after abstract screening: 1,322 (95.9% retention rate)
4. PDFs retrieved automatically: ~770 (~58% of retained)
5. Full-text scored: 1,205 PDFs across three themes
6. Supplementary searches: Elicit (record the queries used) + manual (key papers listed)
7. All search strings, exclusion rules, and screening decisions available as supplementary
   materials (transparency artefact)

## Note on the coverage gap

The high retention rate (95.9%) with low exclusion suggests the keyword screening is
conservative (as intended — precision is handled by full-text scoring). The low automatic
download rate (~58%) is structural: Unpaywall retrieves only open-access PDFs, and many
relevant papers in sociology and adjacent fields are not open access. This is a limitation
to acknowledge, but does not undermine the approach — the most important papers can be
retrieved manually and the automated scoring covers the majority of the candidate set.

## Transparency artefact

The full search procedure constitutes a transparency artefact for the paper:
- `scripts/search_openalex.R` — exact queries reproducible
- `literature/automated_literature_searches/boolean-searches.md` — search strings documented
- `literature/automated_literature_searches/filter_tidying/filter_decisions.json` — all decisions
- `literature/Elicit_export/` — Elicit search exports (to be populated)
- `notes/manual-download-priorities.md` — manual retrieval targets

This is itself an example of structured, documented AI-assisted research practice —
the search procedure is an instance of the argument being made in the paper.
