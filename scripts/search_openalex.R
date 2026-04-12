# search_openalex.R
# Purpose: Query OpenAlex (primary) and optionally Semantic Scholar (secondary)
#          using search terms defined in boolean-searches.md.
#          Outputs raw metadata with abstracts and OA URLs for downstream screening.
#
# Project: Structured AI Use in Sociological Research
# Date:    2026-04-05
#
# Requirements:
#   install.packages(c("openalexR", "tidyverse", "httr", "jsonlite"))
#
# Search terms are read from: literature/boolean-searches.md
# Outputs:
#   literature/openalex_results.csv      — raw OpenAlex results
#   literature/semscholar_results.csv    — raw Semantic Scholar results (if run)
#   literature/combined_results.csv      — merged and deduplicated

library(tidyverse)
library(openalexR)
library(httr)
library(jsonlite)

# ------------------------------------------------------------------------------
# CONFIGURATION
# ------------------------------------------------------------------------------

EMAIL             <- "torbskar@uio.no"   # Polite pool identifier for OpenAlex
SEARCH_TERMS_PATH <- "literature/automated_literature_searches/boolean-searches.md"
OUTPUT_DIR        <- "literature/automated_literature_searches"
YEAR_FROM         <- 2020L                 # Adjust as needed
MAX_RESULTS       <- 400L                  # Per query

# Semantic Scholar API key (register at https://www.semanticscholar.org/product/api)
# Set to NULL to skip Semantic Scholar queries
SS_API_KEY        <- NULL

# Which search blocks to run — corresponds to block names in boolean-searches.md
# Options: "block1", "block2"  (block3 is grey literature, handled separately)
# Venue queries (Science, Nature, PNAS, NHB) always run alongside block queries
# PLOS ONE removed: high volume + standard template text produces many false positives
# in full-text screening (especially Theme C), with little payoff for this project.
BLOCKS_TO_RUN     <- c("block1", "block2")

# Interdisciplinary journals for venue-specific queries
# ISSN (print) used as stable identifier
VENUE_JOURNALS <- list(
  list(name = "Science",                issn = "0036-8075"),
  list(name = "Nature",                 issn = "0028-0836"),
  list(name = "PNAS",                   issn = "0027-8424"),
  list(name = "Nature Human Behaviour", issn = "2397-3374")
)

# Search string for venue queries — short; ISSN filter does the field restriction
VENUE_SEARCH <- "artificial intelligence large language model ChatGPT generative AI research"
VENUE_MAX_RESULTS <- 200L  # Per journal; unlikely to hit ceiling for these outlets

# ------------------------------------------------------------------------------
# PARSE SEARCH TERMS FROM MARKDOWN
# ------------------------------------------------------------------------------

# Search terms are stored as plain strings in boolean-searches.md under headers
# matching "Search string [A-Z]". This function extracts them by label.
# OpenAlex uses its own query syntax (not Boolean) -- terms are passed as
# keyword searches and filtered by concept. See notes below.

parse_search_terms <- function(path) {
  lines <- read_lines(path)

  # Extract lines that follow "**Search string" headers
  # Returns named list: list(A = "...", B = "...", etc.)
  term_lines <- lines[str_detect(lines, "^\\*\\*Search string [A-Z]")]
  term_indices <- which(str_detect(lines, "^\\*\\*Search string [A-Z]"))

  terms <- map(seq_along(term_indices), \(i) {
    label <- str_extract(lines[term_indices[i]], "(?<=Search string )[A-Z]")
    # Code block follows the header -- extract content between ``` markers
    start <- term_indices[i] + 2  # skip header and opening ```
    end_candidates <- which(lines == "```")
    end <- min(end_candidates[end_candidates > start]) - 1
    content <- str_c(lines[start:end], collapse = " ")
    list(label = label, query = content)
  })

  set_names(map(terms, "query"), map_chr(terms, "label"))
}

# Note: Boolean search strings from the .md file are written for Scopus/WoS syntax.
# OpenAlex uses a simpler keyword search -- extract the core concept terms and
# pass them as search strings. Manual adjustment of extracted terms is expected
# before a production run.

# Manually define OpenAlex-compatible search strings here, derived from
# boolean-searches.md. OpenAlex does not support field-specific Boolean syntax
# in the same way as Scopus.

openalex_queries <- list(

  # Block 1A -- AI tools in research practice, broad field coverage
  # Short string; field breadth comes from including economics and psychology
  block1_A = list(
    search = "artificial intelligence large language model ChatGPT generative AI research practice sociology economics psychology",
    label  = "Block 1A: AI in research practice (broad fields)"
  ),

  # Block 1B -- AI in research methodology, expanded fields
  block1_B = list(
    search = "generative AI ChatGPT research methodology qualitative quantitative social science economics psychology",
    label  = "Block 1B: AI in research methodology"
  ),

  # Block 1C -- Journal and publication policy on AI
  block1_C = list(
    search = "artificial intelligence ChatGPT journal policy research integrity academic publishing social science psychology economics",
    label  = "Block 1C: AI and journal/publication policy"
  ),

  # Block 1H -- Cross-disciplinary, no field restriction
  # Shorter string; no discipline terms so relevance scoring isn't diluted
  block1_H = list(
    search = "artificial intelligence large language model ChatGPT generative AI research practice transparency open science replication",
    label  = "Block 1H: AI and research practice (no field restriction)"
  ),

  # Block 2D -- Pre-registration and explicit reasoning
  block2_D = list(
    search = "pre-registration registered report open science transparency replication social science psychology economics",
    label  = "Block 2D: Pre-registration and explicit reasoning"
  ),

  # Block 2E -- Tacit knowledge and research practice
  block2_E = list(
    search = "tacit knowledge explicit knowledge research practice scientific practice knowledge production",
    label  = "Block 2E: Tacit knowledge"
  ),

  # Block 2G -- Prompt engineering and epistemic quality
  block2_G = list(
    search = "prompt engineering structured prompts epistemic reasoning knowledge production research quality reliability",
    label  = "Block 2G: Structured prompts and epistemic quality"
  )
)

# ------------------------------------------------------------------------------
# QUERY OPENALEX
# ------------------------------------------------------------------------------

query_openalex <- function(query_def, year_from, max_results, email) {

  message(paste0("Querying OpenAlex: ", query_def$label))

  # Calculate pages needed; per_page capped at 200 (API maximum)
  per_p  <- min(max_results, 200L)
  n_pages <- ceiling(max_results / per_p)

  tryCatch({
    results <- oa_fetch(
      entity      = "works",
      search      = query_def$search,
      from_publication_date = paste0(year_from, "-01-01"),
      per_page    = per_p,
      pages       = n_pages,
      mailto      = email,
      count_only  = FALSE,
      verbose     = FALSE
    )

    if (is.null(results) || nrow(results) == 0) {
      message(paste0("  No results for: ", query_def$label))
      return(NULL)
    }

    message(paste0("  Retrieved ", nrow(results), " records"))

    results |>
      slice_head(n = max_results) |>
      mutate(
        query_label  = query_def$label,
        # abstract is already a character string in current openalexR
        # pdf_url and oa_url are direct columns (no best_oa_location needed)
        best_pdf_url = coalesce(pdf_url, oa_url)
      ) |>
      select(
        doi, title, abstract, publication_year,
        source = source_display_name,
        cited_by_count,
        is_oa,
        oa_url    = best_pdf_url,
        query_label
      )
  }, error = \(e) {
    message(paste0("  Error querying OpenAlex for ", query_def$label, ": ", e$message))
    NULL
  })
}

oa_raw <- map(openalex_queries, \(q) {
  query_openalex(q, YEAR_FROM, MAX_RESULTS, EMAIL)
}) |>
  compact() |>
  list_rbind()

# ------------------------------------------------------------------------------
# VENUE-SPECIFIC QUERIES — interdisciplinary journals
# ------------------------------------------------------------------------------

query_openalex_venue <- function(journal, search_text, year_from, max_results, email) {

  message(paste0("Querying OpenAlex (venue): ", journal$name))

  per_p   <- min(max_results, 200L)
  n_pages <- ceiling(max_results / per_p)

  tryCatch({
    results <- oa_fetch(
      entity                         = "works",
      search                         = search_text,
      `primary_location.source.issn` = journal$issn,
      from_publication_date          = paste0(year_from, "-01-01"),
      per_page                       = per_p,
      pages                          = n_pages,
      mailto                         = email,
      count_only                     = FALSE,
      verbose                        = FALSE
    )

    if (is.null(results) || nrow(results) == 0) {
      message(paste0("  No results for: ", journal$name))
      return(NULL)
    }

    message(paste0("  Retrieved ", nrow(results), " records from ", journal$name))

    results |>
      slice_head(n = max_results) |>
      mutate(
        query_label  = paste0("Venue: ", journal$name),
        best_pdf_url = coalesce(pdf_url, oa_url)
      ) |>
      select(
        doi, title, abstract, publication_year,
        source = source_display_name,
        cited_by_count,
        is_oa,
        oa_url    = best_pdf_url,
        query_label
      )
  }, error = \(e) {
    message(paste0("  Error querying ", journal$name, ": ", e$message))
    NULL
  })
}

venue_raw <- map(VENUE_JOURNALS, \(j) {
  query_openalex_venue(j, VENUE_SEARCH, YEAR_FROM, VENUE_MAX_RESULTS, EMAIL)
}) |>
  compact() |>
  list_rbind()

message(paste0("Venue queries: ", nrow(venue_raw), " raw results across ",
               length(VENUE_JOURNALS), " journals"))

# Combine block queries and venue queries before deduplication
oa_all_raw <- bind_rows(oa_raw, venue_raw)

# Deduplicate on DOI, keeping record with most citations
oa_dedup <- oa_all_raw |>
  group_by(doi) |>
  slice_max(cited_by_count, n = 1, with_ties = FALSE) |>
  ungroup()

message(paste0(
  "OpenAlex: ", nrow(oa_all_raw), " raw results (",
  nrow(oa_raw), " block queries + ", nrow(venue_raw), " venue queries), ",
  nrow(oa_dedup), " after deduplication on DOI"
))

write_csv(oa_dedup, file.path(OUTPUT_DIR, "openalex_results.csv"))
message(paste0("Saved to ", file.path(OUTPUT_DIR, "openalex_results.csv")))

# ------------------------------------------------------------------------------
# QUERY SEMANTIC SCHOLAR (OPTIONAL)
# ------------------------------------------------------------------------------

query_semantic_scholar <- function(query_text, api_key = NULL, limit = 100) {

  headers <- c("Content-Type" = "application/json")
  if (!is.null(api_key)) headers["x-api-key"] <- api_key

  body <- list(
    query  = query_text,
    limit  = limit,
    fields = "title,abstract,year,authors,externalIds,openAccessPdf,citationCount,journal"
  )

  resp <- POST(
    "https://api.semanticscholar.org/graph/v1/paper/search/bulk",
    add_headers(.headers = headers),
    body    = toJSON(body, auto_unbox = TRUE),
    encode  = "raw"
  )

  if (http_error(resp)) {
    message(paste0("Semantic Scholar error: ", status_code(resp)))
    return(NULL)
  }

  content(resp, as = "parsed")$data |>
    map_dfr(\(p) tibble(
      doi              = p$externalIds$DOI %||% NA_character_,
      title            = p$title %||% NA_character_,
      abstract         = p$abstract %||% NA_character_,
      publication_year = p$year %||% NA_integer_,
      journal          = p$journal$name %||% NA_character_,
      cited_by_count   = p$citationCount %||% NA_integer_,
      oa_url           = p$openAccessPdf$url %||% NA_character_,
      is_oa            = !is.na(p$openAccessPdf$url)
    ))
}

ss_raw <- NULL

if (!is.null(SS_API_KEY)) {

  ss_queries <- list(
    "artificial intelligence sociology research workflow academic writing",
    "prompt engineering epistemic quality research transparency",
    "LLM academic research methodology social science"
  )

  message("Querying Semantic Scholar...")

  ss_raw <- map(ss_queries, \(q) {
    Sys.sleep(1)  # Polite rate limiting
    query_semantic_scholar(q, api_key = SS_API_KEY, limit = 100)
  }) |>
    compact() |>
    list_rbind() |>
    mutate(query_label = "Semantic Scholar supplementary") |>
    filter(!is.na(doi))

  write_csv(ss_raw, file.path(OUTPUT_DIR, "semscholar_results.csv"))
  message(paste0(
    "Semantic Scholar: ", nrow(ss_raw),
    " results saved to ", file.path(OUTPUT_DIR, "semscholar_results.csv")
  ))
}

# ------------------------------------------------------------------------------
# MERGE AND DEDUPLICATE
# ------------------------------------------------------------------------------

combined <- bind_rows(
  oa_dedup,
  ss_raw
) |>
  filter(!is.na(doi)) |>
  group_by(doi) |>
  slice_max(cited_by_count, n = 1, with_ties = FALSE) |>
  ungroup() |>
  arrange(desc(cited_by_count))

write_csv(combined, file.path(OUTPUT_DIR, "combined_results.csv"))

message(paste0(
  "\n--- Summary ---\n",
  "OpenAlex block queries:      ", nrow(oa_raw), " raw\n",
  "OpenAlex venue queries:      ", nrow(venue_raw), " raw (",
    paste(map_chr(VENUE_JOURNALS, "name"), collapse = ", "), ")\n",
  "OpenAlex deduplicated:       ", nrow(oa_dedup), "\n",
  "Semantic Scholar results:    ", if (is.null(ss_raw)) "not run" else nrow(ss_raw), "\n",
  "Combined (deduplicated):     ", nrow(combined), "\n",
  "With abstracts:              ", sum(!is.na(combined$abstract)), "\n",
  "With OA PDF URL:             ", sum(!is.na(combined$oa_url)), "\n",
  "Output:                      ", file.path(OUTPUT_DIR, "combined_results.csv")
))
