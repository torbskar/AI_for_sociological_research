# Claude contribution: 2026-05-07

## v10 defence-gap assessment

*Initiated by author query — requested evaluation of v10 against simulation reviews and adversarial attacks.*

Claude produced notes/v10-defence-gap-assessment.md, assessing v10-draft.md against draft/simulation-reviews/synthesis-personas-reviews.md and draft/simulation-reviews/asshole-reviewer/four_attacks.md. The document identifies six specific gaps, each mapped to the simulation-review or attack that surfaces it, with a priority ranking and effort estimate. The positive assessment (what v10 has right) is included to anchor the gap list against the structural objections that have already been resolved. This structure — confirming resolved issues before identifying remaining gaps — was Claude's framing choice, not specified in the author's query.

---

## v10 targeted edits

*Initiated by gap assessment recommendations; author confirmed scope.*

Claude executed ten targeted edits to v10-draft.md based on the gap assessment priorities:

- Collins (2010) and Polanyi (1958/1966) citations inserted at the externalisation-of-tacit-commitments passage. Claude identified the specific sentence requiring the citations, selected the most parsimonious phrasing, and determined placement without further author instruction.

- Pruschak & Hopp (2022) paragraph added to §1 at the ICMJE criterion 4 introduction. Claude drafted the sentence positioning ICMJE as a motivating analogue/evidentiary standard (not a normative source) and integrated the Pruschak & Hopp citation for adoption evidence.

- Writing-as-thinking bridge sentence drafted and inserted. Claude identified the drafting-stage caveat as the appropriate concessive move (most contested at drafting; most defensible for search, screening, and analytical tasks) and located the insertion point in the systematic-use section.

- "Not a stronger form" sentence drafted for the pre-registration analogy discussion, sharpening the private/public distinction already in the text.

- Jones (2025) and Davidson & Karell (2025) policy paragraph drafted for §6. Claude identified the specific contribution of the paper's tiered framework (organised along systematic/unsystematic process axis rather than tool type or disclosure status) and characterised Jones and Davidson & Karell as moves in the right direction that the paper both acknowledges and supersedes.

- Sibbald (2025) sentence drafted for the enforcement-gap discussion, citing performance/practice distinction.

- "Not all AI must be systematic" paragraph drafted as a scope clarification, confining the systematic-use requirement to AI use that constitutes a research contribution.

- Sant'Anna footnote added with author flag for URL verification.

*Author query as intellectual contribution* — the gap assessment framework (mapping draft gaps to specific adversarial attacks) was specified in the author's initial query. The priority ranking in the assessment document was Claude's analytical judgment.

---

## CLAUDE.md update — Social Epistemology

*Initiated by author decision to change target journal.*

Claude rewrote the target journal section of CLAUDE.md from the prior SMR entry to a full Social Epistemology entry, incorporating confirmed IFA details once the author pasted the instructions text. Key changes: word limit updated (SMR 10,000 → Social Epistemology 6,000–8,000 inclusive of references); abstract format updated (SMR structured → unstructured ≤200 words); reference format updated (prior 18th-edition placeholder → Chicago AD 17th, confirmed from tf_chicagoad.pdf); T&F AI disclosure requirements recorded; British English requirement noted. Writing instructions updated to reflect philosophical audience.

---

## Chicago AD 17th reference reformatting

*Initiated by author instruction.*

Claude converted the full reference list in v10-draft.md from APA to Chicago AD 17th, applying: article titles in quotation marks; journal names italicised; year immediately after author name without comma (in-text) and on its own position (reference list); "and" before final author; all authors listed for entries with ten or fewer. Six parenthetical in-text citations corrected (comma between author and year removed). Three three-author narrative citations spelled out in full: Hicks, Humphries, and Slater (2024); Barrie, Palmer, and Spirling (2025); Ludwig, Mullainathan, and Rambachan.

*Author query as intellectual contribution* — the decision to check British English spelling and other formalities simultaneously with the reference reformat was an efficient bundling that Claude noted but the author specified.

---

## literature/chicago_references.md

*Initiated by author query specifying upload_theme_*/ scope.*

Claude proposed using rename_mappings.json + openalex_retained.csv as the primary data source rather than reading PDFs directly — this approach is faster and avoids OCR errors. The author accepted. Claude matched upload-folder filenames to DOI-based originals via rename_mappings.json, retrieved full bibliographic metadata from openalex_retained.csv, and fell back to PDF reading for entries not in the OpenAlex data (manually added papers not captured by the search pipeline, including Davidson & Karell and Jones). The resulting file (literature/chicago_references.md) contains Chicago AD 17th entries for all unique PDFs across the three upload theme folders.

Six draft reference entries were completed from this source: Davidson & Karell (2025), Jones (2025), Cheng et al. (2026), Ganjavi et al. (2024), Peters & Chin-Yee (2025), Syed (2024). For each, Claude identified the gap (missing pages, partial author list, missing DOI) and supplied the complete details.

Two flags were raised that require author resolution: the Mitchell et al. discrepancy (two papers with similar titles and partially overlapping authors — only the author can determine which was intended); and the Kosch and Feger ACM venue (DOI added, but final volume/issue not confirmed). Claude inserted explicit flags in the reference entries rather than silently inserting possibly incorrect details.
