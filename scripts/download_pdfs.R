# download_pdfs.R
# Purpose: Query Unpaywall API for open access PDFs from a filtered reference list,
#          download available PDFs into per-search-string subfolders, and report
#          what could not be retrieved.
# Project: Structured AI Use in Sociological Research
# Date:    2026-04-05
#
# Requirements:
#   - roadoi package (Unpaywall API wrapper)
#   - combined_results.csv produced by search_openalex.R (after Haiku screening)
#     Must contain columns: doi, query_label
#
# Output:
#   - PDFs downloaded to literature/pdfs/[A|B|C|...]/
#   - literature/pdf_manifest.csv  (doi, filepath, search_letter, query_label, status)
#   - literature/missing_pdfs.csv  (papers not retrieved, for manual follow-up)

library(tidyverse)
library(roadoi)

# ------------------------------------------------------------------------------
# CONFIGURATION
# ------------------------------------------------------------------------------

EMAIL        <- "torbskar@uio.no"
CSV_PATH     <- "literature/automated_literature_searches/openalex_retained.csv"
PDF_BASE     <- "literature/pdfs"
MANIFEST_PATH <- "literature/automated_literature_searches/pdf_manifest.csv"
MISSING_PATH <- "literature/automated_literature_searches/missing_pdfs.csv"

# ------------------------------------------------------------------------------
# LOAD REFERENCES AND BUILD DOI → SEARCH-LETTER MAP
# ------------------------------------------------------------------------------

refs <- read_csv(CSV_PATH, show_col_types = FALSE)

# query_label format: "Block 1A: ..." → extract the letter following the digit
doi_to_label <- refs |>
  filter(!is.na(doi), doi != "") |>
  mutate(
    doi_bare = str_remove(doi, "^https?://doi\\.org/"),
    # "Block 1A: ..." → "A"; "Block 1H: ..." → "H"; "Venue: Science" → "Venue"
    search_letter = case_when(
      str_detect(query_label, "^Venue:")  ~ "Venue",
      TRUE ~ str_extract(query_label, "(?<=\\d)[A-Z]")
    )
  ) |>
  select(doi_bare, query_label, search_letter)

dois <- doi_to_label$doi_bare

message(paste0("Loaded ", length(dois), " references with DOIs"))

# ------------------------------------------------------------------------------
# SKIP PREVIOUSLY PROCESSED DOIs
# ------------------------------------------------------------------------------
# Consults the existing manifest so that:
#   - Previously downloaded DOIs are not re-queried or re-downloaded (file may
#     have been renamed, so file.exists() alone cannot detect them)
#   - Previously failed DOIs are not re-attempted (they typically fail again)
#   - Only DOIs absent from the previous manifest are sent to Unpaywall

prev_manifest <- if (file.exists(MANIFEST_PATH)) {
  read_csv(MANIFEST_PATH, show_col_types = FALSE)
} else {
  NULL
}

if (!is.null(prev_manifest)) {
  dois_prev_ok   <- prev_manifest |>
    filter(status %in% c("downloaded", "already_exists")) |>
    pull(doi)
  dois_prev_fail <- prev_manifest |>
    filter(status == "failed") |>
    pull(doi)

  n_skip_ok   <- length(intersect(dois, dois_prev_ok))
  n_skip_fail <- length(intersect(dois, dois_prev_fail))
  dois_to_query <- setdiff(dois, c(dois_prev_ok, dois_prev_fail))

  message(paste0(
    "Previous manifest found: skipping ", n_skip_ok, " already downloaded",
    " and ", n_skip_fail, " previously failed. ",
    length(dois_to_query), " new DOIs to process."
  ))
} else {
  dois_to_query <- dois
  prev_manifest  <- NULL
  message("No previous manifest found — processing all DOIs.")
}

# ------------------------------------------------------------------------------
# QUERY UNPAYWALL
# ------------------------------------------------------------------------------

# roadoi wrapper: normalises has_repository_copy (Unpaywall returns it as
# logical or character inconsistently, causing bind_rows() to fail).
# Falls back to one-at-a-time if a batch fails.
safe_oadoi_fetch <- function(dois, email, batch_size = 50) {
  normalise <- function(df) {
    if (!is.null(df) && "has_repository_copy" %in% names(df))
      df$has_repository_copy <- as.character(df$has_repository_copy)
    df
  }
  batches <- split(dois, ceiling(seq_along(dois) / batch_size))
  map(batches, \(batch) {
    tryCatch(
      normalise(oadoi_fetch(dois = batch, email = email)),
      error = \(e) {
        message("  Batch failed, retrying one-at-a-time...")
        map(batch, \(d) {
          tryCatch(normalise(oadoi_fetch(dois = d, email = email)),
                   error = \(e2) { message("  Skipped: ", d); NULL })
        }) |> compact() |> list_rbind()
      }
    )
  }) |> list_rbind()
}

if (length(dois_to_query) == 0) {
  message("Nothing new to download.")
  oa_results <- tibble()
} else {
  message(paste0("Querying Unpaywall API for ", length(dois_to_query), " DOIs..."))
  oa_results <- safe_oadoi_fetch(dois_to_query, EMAIL)
}

# ------------------------------------------------------------------------------
# EXTRACT BEST PDF URL AND JOIN SEARCH LETTER
# ------------------------------------------------------------------------------

# roadoi's best_oa_location is a 1-row data frame per record.
# Fields: url (best direct link), url_for_landing_page.
# There is no separate url_for_pdf column -- url IS the direct link when available.

if (nrow(oa_results) > 0) {
  pdf_urls <- oa_results |>
    mutate(
      pdf_url = map_chr(best_oa_location, \(x) {
        if (is.null(x) || !is.data.frame(x) || nrow(x) == 0) return(NA_character_)
        x$url[1] %||% x$url_for_landing_page[1] %||% NA_character_
      })
    ) |>
    select(doi, title, is_oa, oa_status, pdf_url) |>
    left_join(doi_to_label, by = c("doi" = "doi_bare")) |>
    mutate(search_letter = coalesce(search_letter, "unknown"))
} else {
  pdf_urls <- tibble(doi = character(), title = character(), is_oa = logical(),
                     oa_status = character(), pdf_url = character(),
                     query_label = character(), search_letter = character())
}

n_available <- sum(!is.na(pdf_urls$pdf_url))
n_missing   <- sum(is.na(pdf_urls$pdf_url))

message(paste0(
  "Unpaywall found URLs for ", n_available, " new papers. ",
  n_missing, " not available via open access."
))

# ------------------------------------------------------------------------------
# DOWNLOAD PDFS INTO PER-LETTER SUBFOLDERS
# ------------------------------------------------------------------------------

# Filename: DOI with / and : replaced by _ to avoid path issues
safe_doi_filename <- function(doi) {
  paste0(str_replace_all(doi, "[/:]", "_"), ".pdf")
}

to_download <- pdf_urls |>
  filter(!is.na(pdf_url)) |>
  mutate(
    subdir   = file.path(PDF_BASE, search_letter),
    filepath = file.path(subdir, safe_doi_filename(doi))
  )

# Create subdirectories
walk(unique(to_download$subdir), \(d) {
  if (!dir.exists(d)) dir.create(d, recursive = TRUE)
})

message(paste0("Downloading ", nrow(to_download), " PDFs..."))

download_results <- to_download |>
  mutate(
    status = map2_chr(pdf_url, filepath, \(url, path) {
      if (file.exists(path)) {
        message(paste0("  Already exists, skipping: ", basename(path)))
        return("already_exists")
      }
      tryCatch(
        {
          download.file(url, path, mode = "wb", quiet = TRUE)
          message(paste0("  Downloaded: ", basename(path)))
          "downloaded"
        },
        error = \(e) {
          message(paste0("  Failed: ", basename(path), " -- ", e$message))
          "failed"
        }
      )
    })
  )

n_success <- sum(download_results$status %in% c("downloaded", "already_exists"))
n_new     <- sum(download_results$status == "downloaded")
n_failed  <- sum(download_results$status == "failed")

message(paste0(
  "Downloads complete. New: ", n_new, ". Already existed: ",
  n_success - n_new, ". Failed: ", n_failed, "."
))

# ------------------------------------------------------------------------------
# WRITE MANIFEST AND MISSING LIST
# ------------------------------------------------------------------------------

# Combine new download results with entries carried forward from previous manifest
new_entries <- download_results |>
  select(doi, filepath, search_letter, query_label, status, title, is_oa, oa_status, pdf_url)

carried_forward <- if (!is.null(prev_manifest)) {
  prev_manifest |>
    filter(doi %in% c(dois_prev_ok, dois_prev_fail)) |>
    select(any_of(names(new_entries)))
} else {
  tibble()
}

manifest <- bind_rows(carried_forward, new_entries) |>
  distinct(doi, .keep_all = TRUE)

write_csv(manifest, MANIFEST_PATH)
message(paste0("Manifest written to ", MANIFEST_PATH,
               " (", nrow(new_entries), " new + ", nrow(carried_forward), " carried forward)"))

# Missing list: new failures + new no-OA + carried-forward failures
missing <- bind_rows(
  pdf_urls |>
    filter(is.na(pdf_url)) |>
    mutate(reason = "No open access version found via Unpaywall"),
  download_results |>
    filter(status == "failed") |>
    select(doi, title, is_oa, oa_status, pdf_url, search_letter, query_label) |>
    mutate(reason = "Download failed despite OA URL"),
  if (!is.null(prev_manifest))
    prev_manifest |>
      filter(status == "failed", doi %in% dois) |>
      select(any_of(c("doi", "title", "is_oa", "oa_status", "pdf_url",
                      "search_letter", "query_label"))) |>
      mutate(reason = "Previously failed — not retried")
  else
    tibble()
)

write_csv(missing, MISSING_PATH)
message(paste0(nrow(missing), " papers written to ", MISSING_PATH, " for manual follow-up."))

# Write a _missing.md log into each search-letter subfolder listing papers
# not retrieved, so the folder is self-documenting without opening the manifest.
missing_by_letter <- bind_rows(
  # Papers with no OA URL -- assign letter from pdf_urls via doi match
  pdf_urls |>
    filter(is.na(pdf_url)) |>
    mutate(reason = "No open access version found via Unpaywall"),
  # Papers where download was attempted but failed
  download_results |>
    filter(status == "failed") |>
    select(doi, title, is_oa, oa_status, pdf_url, search_letter, query_label) |>
    mutate(reason = "Download failed (403 or network error) — retrieve manually")
) |>
  filter(!is.na(search_letter), search_letter != "unknown")

for (letter in sort(unique(missing_by_letter$search_letter))) {
  subdir  <- file.path(PDF_BASE, letter)
  if (!dir.exists(subdir)) dir.create(subdir, recursive = TRUE)
  log_path <- file.path(subdir, "_missing.md")

  rows <- missing_by_letter |> filter(search_letter == letter)

  lines <- c(
    paste0("# Missing PDFs — Search string ", letter),
    paste0("Generated: ", Sys.time()),
    paste0("Total not retrieved: ", nrow(rows)),
    "",
    "| Title | DOI | OA status | Reason |",
    "|-------|-----|-----------|--------|"
  )

  for (i in seq_len(nrow(rows))) {
    r     <- rows[i, ]
    title <- coalesce(r$title, "Unknown title")
    doi   <- coalesce(r$doi, "")
    oas   <- coalesce(r$oa_status, "")
    rsn   <- r$reason
    lines <- c(lines, paste0("| ", title, " | ", doi, " | ", oas, " | ", rsn, " |"))
  }

  writeLines(lines, log_path, useBytes = FALSE)
  message(paste0("  Missing log written: ", log_path, " (", nrow(rows), " papers)"))
}

# ------------------------------------------------------------------------------
# SUMMARY
# ------------------------------------------------------------------------------

message("\n--- Summary ---")
message(paste0("Total DOIs in retained set:  ", length(dois)))
message(paste0("Skipped (prev. downloaded):  ", if (exists("n_skip_ok"))   n_skip_ok   else 0))
message(paste0("Skipped (prev. failed):      ", if (exists("n_skip_fail")) n_skip_fail else 0))
message(paste0("New DOIs processed:          ", length(dois_to_query)))
message(paste0("  OA URLs found:             ", n_available))
message(paste0("  Newly downloaded:          ", n_new))
message(paste0("  Download failures:         ", n_failed))
message(paste0("  No OA version available:   ", n_missing))
total_on_disk <- sum(manifest$status %in% c("downloaded", "already_exists"))
message(paste0("Total PDFs on disk (all runs): ", total_on_disk))

message("\n--- Per search string ---")
download_results |>
  count(search_letter, status) |>
  arrange(search_letter, status) |>
  as.data.frame() |>
  print()
