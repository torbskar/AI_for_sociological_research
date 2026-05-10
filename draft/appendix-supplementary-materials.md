# Appendix: Supplementary Materials — Illustrative Extracts

The extracts below are illustrative samples from the project's transparency artefacts. They are not exhaustive: the complete replication package — all R and Python scripts, skill configuration files, search logs, session decision records, and NotebookLM prompt templates — is available at [repository URL — to be made available upon acceptance]. Together these materials constitute the transparency artefacts described in the paper: documented, shareable records of the choices made at each stage of the workflow. The extracts are presented in workflow order, from project configuration through literature search, AI tool configuration, synthesis protocol, and session logging.

---

## A. Project configuration

*Source: `CLAUDE.md` (project root)*

The root `CLAUDE.md` file functions as the project's standing instruction set — the document the AI assistant reads at the start of every session. It encodes the paper's epistemic commitments in operational terms, functioning analogously to a pre-registration document in that it fixes the framing, conceptual distinctions, and criteria before any analytic work begins. The following two sections are reproduced in full.

```
## Core argument

1. The systematic/unsystematic distinction — not AI use versus non-use — is the
   epistemically relevant axis for policy.
2. Systematic AI use forces explicit articulation of tacit research decisions,
   functioning analogously to pre-registration.
3. This produces transparency artefacts (prompt templates, skill configurations,
   search logs) that are open-science compatible.
4. Current journal policies, even the more sophisticated tiered approaches,
   organise disclosure along the wrong axis — what was used and whether it was
   disclosed, rather than whether the process was epistemically sound.
5. A documentation-based framework, organised around the systematic/unsystematic
   distinction, is the appropriate instrument — and existing replication-package
   infrastructure already supports it.

## Key conceptual distinctions (use consistently throughout)

- Systematic use: tool configurations with explicit criteria, built-in human
  verification at each stage, documented outputs
- Unsystematic use: accepting AI outputs without explicit criteria, verification,
  or documentation
- Query authorship: the intellectual contribution in AI-assisted research resides
  in the query — search criteria, screening rubrics, analytical specifications,
  reviewer configurations — not in the generated text
- Skills / reviewer skills: configured AI personas with discipline-specific
  review criteria
- Transparency artefacts: prompt templates, skill files, search logs,
  session records — shareable as documentation package / replication materials
```

---

## B. Systematic workflow across the research pipeline

*Sources: `literature/PIPELINE.md`; `CLAUDE.md`; `supplementary/skills/`*

The systematic workflow spans the full research process: literature identification and screening, synthesis and conceptual development, drafting, and review. Each stage applies the same structural logic — explicit criteria encoded in advance, human verification checkpoints at designated intervals, documented outputs — but the specific implementation differs by stage. The literature search stage involves a scripted multi-step pipeline and is documented here in detail. The drafting and review stages operate through skill configurations (see Section C) and standing `CLAUDE.md` instructions; selected session logs illustrate the human verification record (see Section E).

### Literature search pipeline

The pipeline runs from OpenAlex database query to NotebookLM synthesis export across eight steps. The overview table below shows the full sequence; the two detailed extracts that follow show the human checkpoint at Step 4 and the thematic scoring criteria at Step 7. Human checkpoints (marked *[H]*) are built into the pipeline design: the workflow halts for manual review before proceeding, ensuring that automated decisions are subject to human verification.

#### Overview

Full file paths are as documented in `literature/PIPELINE.md` in the project repository.

| Step | Script / action                          | Output                       |
| ---- | ---------------------------------------- | ---------------------------- |
| 1    | `search_openalex.R`                      | `combined_results.csv`       |
| 2    | `filter_results.py --extract`            | `filter_candidates.json`     |
| 3    | `screen_candidates.py`                   | `filter_decisions.json`      |
| 4    | `filter_results.py --apply`              | `openalex_retained.csv`      |
| 4    | *[H]* Spot-check excluded                | —                            |
| 5    | `download_pdfs.R`                        | `pdfs/[A–G]/`                |
| 5    | *[H]* Review missing PDFs                | —                            |
| 6    | `rename_pdfs.py --extract/--apply`       | renamed PDFs                 |
| 7    | `screen_fulltexts.py`                    | `fulltext_scores.csv`        |
| 7b   | `populate_upload_folders.py`             | `notebooklm/upload_[a/b/c]/` |
| 7b   | *[H]* Upload theme folders to NotebookLM | —                            |
| 7c   | *[H]* Write search summary report        | `search_summary_report.md`   |
| 8    | `export_notebooklm.py`                   | `notebooklm_export/`         |
| 8    | *[H]* Review composite export            | —                            |

#### Step 4 — Apply filter decisions (human checkpoint)

```
Preview first:
    python scripts/filter_results.py --apply --dry-run

If reasonable, execute:
    python scripts/filter_results.py --apply

Outputs:
- literature/automated_literature_searches/openalex_retained.csv
- literature/automated_literature_searches/openalex_excluded.csv
- literature/automated_literature_searches/filter_tidying/filter_report.md

Human checkpoint: Spot-check ~30 records from openalex_excluded.csv for false
negatives before proceeding. If false negatives found, edit filter_decisions.json
and re-run --apply.
```

#### Step 7 — Full-text relevance screening

Scores each PDF against three themes using weighted keyword matching on strategic page samples (first 3 pages + middle 2 pages + last 2 pages).

**Themes:**

| Theme | Description                                                         |
| ----- | ------------------------------------------------------------------- |
| A     | Systematic / structured AI use in research practice                 |
| B     | Explicit reasoning, pre-registration, open science, tacit knowledge |
| C     | Journal and publication policy on AI                                |

**Parameters:**

| Parameter   | Default           | Notes                |
| ----------- | ----------------- | -------------------- |
| `--top-n`   | 75                | Papers per theme CSV |
| `--pdf-dir` | `literature/pdfs` | Source PDF directory |

What to check: Open `fulltext_report.md` for an overview. Then open each theme CSV — the `hits_[a/b/c]` column shows which terms triggered the score, which helps identify false positives (high-scoring papers that are not actually relevant).

#### Implementation for this paper

Three keyword searches were conducted using pre-specified boolean strings in OpenAlex via the `openalexR` package in R (Massimo et al., 2024), covering three topics: A) "Systematic AI use in research practice"; B) "Explicit reasoning, pre-registration, open science"; and C) "Journal and publication policy on AI". This yielded 1,479 hits, of which 1,407 were retained after first screening of titles and abstracts. 1,205 full-text articles were successfully downloaded and screened. Full-text screening produced a ranked shortlist; the top-scored articles were loaded into NotebookLM for grounded synthesis (topic A: 48, topic B: 49, topic C: 46). Articles not retrievable by automation: the ten highest-ranked titles within each topic were manually located and added to the notebooks. A structured synthesis for each topic was exported from NotebookLM. A parallel semantic search using Elicit.com produced topic-level reports retained alongside the NotebookLM synthesis outputs as drafting materials.

Human verification took two forms: the top-scored papers were read independently of the AI synthesis, with discrepancies flagged and investigated; and synthesis outputs were cross-checked against the cited sources. All search strings, screening criteria, relevance scores, and synthesis queries are available in the project repository.

### Drafting and review pipeline

Drafting operates under standing instructions encoded in the project's root `CLAUDE.md` (see Section A), which fix the argument structure, conceptual distinctions, and voice profile before any drafting session begins. Two skill configurations apply to the drafting and revision stages: a prose style skill encoding the author's established academic voice, and a logic-and-language reviewer skill encoding discipline-specific criteria for argument coherence, logical validity, and language precision. The reviewer skill is invoked at designated revision points rather than ad hoc; all suggestions are accepted or rejected by the author, with the reasoning recorded in the session decision log. The complete skill configurations are available in the project repository.

---

## C. Skill configuration

*Source: `supplementary/skills/lit-search/SKILL.md`*

A skill is a configuration file that encodes a workflow as an executable, repeatable set of instructions for the AI assistant. The extract below shows the frontmatter and first four steps of the literature search skill. The frontmatter specifies the trigger phrases that activate the skill and provides a description used by the assistant to recognise when the skill applies; the steps encode each stage of the pipeline with explicit decision rules and human checkpoints. Reviewer skills follow the same structure, substituting discipline-specific review criteria for search-step logic; the full reviewer skill configuration is available in the replication package.

```yaml
---
name: lit-search
description: >
  Run a systematic literature search and screening pipeline for any research
  project. Use this skill whenever the user says /lit-search, "run the
  literature search", "start the search", "run the OpenAlex search", "execute
  the lit search", or wants to retrieve and filter academic literature. Runs
  search_openalex.R to query OpenAlex, screen_candidates.py for keyword-based
  abstract screening, download_pdfs.R to fetch open-access PDFs organised by
  search letter, screen_fulltexts.py for full-text scoring, and
  export_notebooklm.py for NotebookLM upload preparation. Human checkpoints
  after filtering and after download. All outputs go to literature/ in the
  project root. Run all scripts from the project root directory (not from
  scripts/).
---
```

```
## Step 1: Run OpenAlex search

    Rscript scripts/search_openalex.R

Output: literature/automated_literature_searches/combined_results.csv
Check the summary at the end of output: total records, records with abstracts,
records with OA URLs.

## Step 2: Prepare filter candidates

    python scripts/filter_results.py --extract

Output: literature/automated_literature_searches/filter_tidying/filter_candidates.json
Note the number of candidates printed to screen.

## Step 3: Abstract screening

    python scripts/screen_candidates.py

Applies keyword-based exclusion rules to all records and writes a decision for
each. RETAIN when in doubt — full-text screening (Step 7) handles precision.

Exclusion criteria — EXCLUDE if the title/abstract clearly indicates:
1. NLP/text processing as primary focus
2. School or K-12 context (unless about higher education or research practice)
3. AI affecting a non-research outcome (business productivity, HR, clinical
   diagnosis, etc.)
4. Big data/digitisation frame unrelated to research practice
5. Prediction or forecasting as primary purpose (ML as applied method)
6. Pedagogical effectiveness (AI improving student learning outcomes)

## Step 4: Apply filter decisions

Preview first:
    python scripts/filter_results.py --apply --dry-run

Human checkpoint: Spot-check ~30 records from openalex_excluded.csv for false
negatives before proceeding.
```

---

## D. NotebookLM synthesis protocol

*Source: `literature/notebooklm/notebooklm_summaries/notebooklm_report_B.md`*

The NotebookLM synthesis reports follow a structured query protocol. Standing instructions appear at the top of each report and apply to all subsequent queries; they specify citation requirements and impose a mandatory source-coverage check before synthesis begins. The Q0 query is submitted first in every notebook — it forces the AI to enumerate all uploaded sources and assess their relevance before any synthesis query is answered. This establishes which sources are available and confirms that none are silently ignored. The first six entries from the Q0 response in Notebook B (Theme: explicit reasoning, pre-registration, open science, tacit knowledge) are reproduced below.

### Standing instructions

```
STANDING INSTRUCTIONS — applies to all sections of this report:

This is a manual workflow. Submit each query (Q0, Q1, etc.) separately in
NotebookLM and paste the response into the corresponding section before
moving to the next query. Do not submit the whole document as a single prompt.

Citations: Every substantive claim must be cited in the text immediately after
the sentence it supports, using author-year format, e.g. (Smith et al., 2023).
If multiple sources support a claim, cite all of them. Do not group citations
at the end of a paragraph.

Source coverage: All sources in this notebook must be considered when answering
each query. Sources that are not informative for a given section should not
simply be ignored — they must be listed in the "Sources not drawn on" section
at the end of the report, with a brief explanation of why they did not
contribute (e.g. not relevant to the theme, too general, overlaps with a
stronger source, does not address the question asked).
```

### Q0 source-coverage check (query and excerpt from response)

```
Q0 — submit this exact text to NotebookLM before any other query:

> This notebook contains [N] sources. List ALL of them by title, one per line,
> numbered. For each, write one sentence on what it covers and whether it is
> relevant to open science, pre-registration, tacit knowledge, or the
> epistemology of research practice. Do not skip any source. If you cannot
> identify [N] distinct sources, say so explicitly and state how many you found.
>
> (Replace [N] with the actual number of sources uploaded before submitting.
> Later queries should reference: "drawing on all [N] sources listed in Q0,
> including those not yet cited in earlier sections.")

[Response excerpt — Notebook B, 46 sources confirmed:]

I have identified 46 distinct sources in this notebook. I could not identify a
47th distinct source based on the headers and metadata provided. The following
list identifies each source, summarizes its coverage, and specifies its
relevance to open science, pre-registration, tacit knowledge, or research
epistemology.

1. Cole et al. (2023): This source investigates enablers and barriers to
   reproducibility in qualitative research, focusing on the epistemological
   misalignment between open science practices and constructivist research
   paradigms.
2. Adjovi (2025): This bibliometric analysis tracks the worldwide production
   of research on ethics, providing a broad context for the sociological study
   of research integrity and responsibility in various disciplines.
3. Administrator (2024): This report audits current practices in human
   neuroscience, identifying how pre-registration and open science can guard
   against questionable practices like p-hacking and HARKing.
4. Van den Akker et al. (2023): This study assesses the practical value of
   pre-registration in psychology by comparing registered studies with
   equivalent non-registered ones to measure reporting consistency.
5. Al-Hoorie & Hiver (2021): This introduction to metascience in applied
   linguistics defines open science as transparency across the entire research
   process, covering open methods, reporting, and evaluation.
6. Torka et al. (2023): This paper addresses the low adoption rates of open
   science practices in management and organizational psychology, advocating
   for reform against publication bias and novelty-seeking.

[... 40 further entries ...]
```

---

## E. Session logs — three-file system

*Sources: `logs/CLAUDE.md`; `logs/2026-04-04-author-input.md`; `logs/2026-04-23-claude-contribution.md`*

Every session produces three log files: a decision log recording what was decided and the reasoning behind non-obvious choices; an author-input file recording the intellectual contributions of the human author in first-person prose; and a claude-contribution file recording the AI's intellectual contributions with initiative attribution. The protocol is specified in `logs/CLAUDE.md`; the two excerpt sections that follow show example entries from the first and last logged sessions.

### E1. Log format specification (from `logs/CLAUDE.md`)

```
Author-input file

Every session log must be accompanied by a paired YYYY-MM-DD-author-input.md
file. This file documents what the author brought to the session — ideas,
framings, arguments, redirections, and pushbacks — in first-person prose,
written as a contemporaneous record.

Purpose: To document the intellectual origin of the work. The decision log
records what was decided; the author-input file records who originated what.
This is essential for transparency about the human-AI division of labour and
defends against the criticism that the work is AI-generated rather than
AI-assisted.

Claude-contribution file

Every session log must also be accompanied by a YYYY-MM-DD-claude-contribution.md
file. This is the counterpart to the author-input file: it documents what Claude
contributed intellectually to the session, written in neutral third-person
academic register by Claude at the end of the session.

Purpose: To complete the transparency record of the human-AI division of
intellectual labour. The author-input file records the author's contributions;
this file records Claude's. Together they allow a full account of who originated
what — essential for query-authorship transparency and for any CRediT-style
disclosure.

What to include:
- Decisions Claude proposed and the reasoning behind them (only when non-obvious)
- Initiative attribution for each substantive contribution:
  "Initiated by author query" or "Claude initiative"
- Query-authorship annotations when the author's query itself was an intellectual
  contribution — a framing, criteria specification, diagnostic question, or
  structural insight: "Author query as intellectual contribution — [description]"
```

### E2. Author-input example (2026-04-04)

```
The core idea for this paper is mine. I had been working with systematic AI
workflows in my own research for some time — building reviewer skills,
configuring tools for specific disciplinary standards, running the UiO guest
lecture on AI tools for sociology master's students — and I recognised that
what I was doing was methodologically distinct from the casual AI use that
journals were responding to with restrictive policies. The paper idea came from
that gap: sociology lacked a workflow paper written from inside the discipline
that could both describe what systematic use looks like and make an argument
for why it matters.

[...]

A note on attribution that applies across this project: when I ask for advice
on a course of action, it is typically because I already have an idea and am
testing it before committing. The asking is itself an intellectual act — I have
identified the question, named the candidate solution, and am seeking an
assessment. The decision that follows is mine. This pattern is different from
the AI proposing something unprompted that I then adopt.
```

### E3. Claude-contribution example (2026-04-23)

```
## research-project-setup skill created

Skill architecture and content — Initiated by author query

*Author query as intellectual contribution — specified that the skill should
(a) cover CLAUDE.md subfolder splitting, skardhamar-style, naming conventions,
and literature search setup; (b) include logging, especially with a new
Claude-contribution file analogous to the author-input file; (c) treat queries
as intellectual contributions in accordance with query-authorship; and (d) check
existing state before asking targeted questions about gaps. This specification
determined the skill's scope, structure, and the conceptual distinction between
the three log file types.*

Proposed a plugin structure with SKILL.md, references/, and examples/ directories
following Claude Code's progressive disclosure design pattern. The references/
directory carries the detail (log formats, contribution guide, pipeline, project
structure templates) while SKILL.md stays lean (~1,800 words). This architecture
means the skill loads efficiently on trigger and pulls detail as needed.

## Three-file logging system formalization — Initiated by author query

*Author query as intellectual contribution — introduced the requirement for a
Claude-contribution file paired with the existing author-input file, and specified
that it should record decisions/reasoning and initiative attribution, treating
queries as intellectual contributions consistent with query-authorship.*

Designed the initiative attribution taxonomy (Initiated by author query / Claude
initiative) and the query-authorship annotation format. The annotation —
"Author query as intellectual contribution — [description]" — provides a specific
mechanism for documenting when the author's query was itself the intellectual
contribution rather than merely an instruction. This operationalizes
query-authorship within the transparency artefact system.
```

---

## F. Log index

*Source: `logs/log-index.md`*

The log index maintains a running table linking each session date to a one-line summary of key decisions. Each date has three associated files: a decision log, an author-input file, and a claude-contribution file, all named by date. Three rows are reproduced below; the full index covers all sessions from project initiation through final drafting.

| Date       | Key decisions                                                                                                                                                                                   |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2026-04-04 | Paper type; target journal; core distinction; file structure; logging convention; three-stage screening protocol; lit-screen skill; string A screened (309→211)                                 |
| 2026-04-05 | OpenAlex replaces Scopus/WoS; query authorship argument developed; target journal selected; full pipeline run (1,133 records → 300 exported); PIPELINE.md written; NotebookLM templates written |
| 2026-04-23 | research-project-setup skill created; logging system extended with claude-contribution file; log-index updated to four columns                                                                  |

---

## G. Session metadata record

*Source: `logs/version-log.md` + `scripts/log_session_meta.sh`*

At the start of each session, a shell script logs the tool version and model identifier to a running version log. This record serves the same function as reporting a software version in a quantitative study: it specifies the conditions under which the documented outputs were produced. The AI model version is treated like a laboratory reagent or a specific release of Stata or R — a change in version is a change in the instrument, and outputs produced under different versions may differ. The following entry is representative; new entries are appended only when the version or model changes from the previous session.

```
## 2026-04-20 13:14

- Claude Code: 2.1.97 (Claude Code)
- Model:       default (see CLI version)
- Git commit:  3e85f13811c19c7dc1f2a67c71785d214445a8f9 (master)
```

The git commit hash links each version record to the exact state of all configuration files, scripts, and drafts at the time the session ran, providing an independent timestamp that is substantially harder to fabricate than a manually written date. The version log is included in the replication package alongside the session decision logs and author-input files.

---

## H. Full project folder structure

*Source: project root (agentic AI configuration)*

A systematic workflow is supported by a project folder structure that makes the documentation package navigable and auditable.

A pile of artefacts with no structure is not meaningfully different from no artefacts: a reviewer who cannot locate the search log, or who cannot tell which prompt configuration corresponds to which draft version, cannot assess whether the process was sound. The structure is part of the epistemic argument.

The simplified folder tree in the paper's workflow section shows only the content folders. The full structure below adds the configuration files used in an agentic AI setup (Claude Code). Subfolder context files are omitted here; they follow the same pattern as the root file and are available in the project repository.

```
project/
├── CLAUDE.md         ← project context; loaded automatically at session start
├── .claudedocs/      ← persistent cross-project instructions (style, epistemological commitments)
├── .claudeignore     ← paths excluded from AI context (data/raw/, credentials, git metadata)
├── .gitignore        ← paths excluded from version control (bulk PDFs, local AI state)
├── .git/             ← version control; commit history timestamps all file changes
├── data/
│   ├── raw/          ← original data; never AI-readable; immutable after receipt
│   └── processed/    ← analysis-ready files; script-generated only
├── scripts/          ← analysis code (R, Python, Stata)
├── outputs/          ← tables and figures; reproducible from scripts
├── literature/       ← search logs, source sets, syntheses
├── notes/            ← working notes and argument sketches
├── draft/            ← manuscript versions with full edit history
├── logs/             ← session decision logs and author-input files
└── supplementary/    ← replication package materials
```

Researchers using chat-only interfaces implement the same functions manually: the project context is pasted at session start rather than loaded automatically; access controls are maintained by folder discipline rather than enforced by the tool; and version control requires an explicit commit step rather than automatic tracking.
