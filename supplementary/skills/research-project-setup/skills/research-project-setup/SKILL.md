---
name: research-project-setup
description: This skill should be used when the user asks to "set up a research project", "initialize project structure", "check my project setup", "audit project scaffold", "create a new research project", "set up logging", "check what's missing in my project", or wants to establish the folder structure, CLAUDE.md files, logging system, and literature search infrastructure for a structured AI-assisted sociological or social science research project.
version: 0.1.0
---

# Research Project Setup

This skill initializes or audits a structured AI-assisted research project following the conventions developed in Skardhamar (2026). It works on both new projects (scaffolding from scratch) and existing ones (detecting and patching gaps). The skill encodes a three-file logging system that produces transparency artefacts documenting the human-AI division of intellectual labour — a core requirement for structured, epistemically defensible AI use in social science research.

## Core conventions

**Structured vs. unstructured AI use**: The project infrastructure is designed to make AI use *structured* — explicit criteria, human verification at each stage, documented outputs. Every setup decision should reinforce this.

**Writing**: All prose drafting uses the `skardhamar-style` skill. Invoke it explicitly before drafting any manuscript section.

**Draft versioning**: `vN-draft.md` for Claude output; `vN-draft - manualEdit.md` for author-edited versions. Increment version number only on author request or when continuing from a manualEdit file.

**Notes lifecycle**: Save as `notes/[topic].md`. Move to `notes/used/` once incorporated into a draft, skill, or other artefact.

---

## Phase 1: Detect project state

On invocation, check what is already present before asking any questions.

### Required components checklist

Run Glob and Read tools to verify each item:

| Component | Expected path | Check |
|---|---|---|
| Root CLAUDE.md | `CLAUDE.md` | Exists and has project overview |
| Logs CLAUDE.md | `logs/CLAUDE.md` | Exists and has logging protocol |
| Draft CLAUDE.md | `draft/CLAUDE.md` | Exists and has versioning convention |
| Notes CLAUDE.md | `notes/CLAUDE.md` | Exists and has notes lifecycle |
| Literature CLAUDE.md | `literature/CLAUDE.md` | Exists and has scope statement |
| Directory: logs | `logs/` | Present |
| Directory: draft | `draft/` | Present |
| Directory: notes | `notes/` | Present |
| Directory: notes/used | `notes/used/` | Present |
| Directory: literature | `literature/` | Present |
| Directory: scripts | `scripts/` | Present |
| Directory: supplementary | `supplementary/` | Present |
| Directory: dismissed_ideas | `dismissed_ideas/` | Present |
| Log index | `logs/log-index.md` | Exists and has four-column table |
| Session script | `scripts/log_session_meta.sh` | Exists and is executable |
| Search script (R) | `scripts/search_openalex.R` | Exists |
| Filter script (Python) | `scripts/filter_results.py` | Exists |
| Literature pipeline | `literature/PIPELINE.md` | Exists |
| Boolean search guide | `supplementary/boolean-search-guide.md` | Exists |

### Log file pairing check

For every `logs/YYYY-MM-DD.md` found, check for:
- `logs/YYYY-MM-DD-author-input.md`
- `logs/YYYY-MM-DD-claude-contribution.md`

Report any dates where one or both paired files are missing.

### Log-index column check

The log-index table must have four columns: Date, Decision log, Author-input, Claude-contribution, Key decisions. Check whether the existing table (if any) has the claude-contribution column.

---

## Phase 2: Report and ask about gaps

After checking, report findings grouped by category:

1. **Project structure** (CLAUDE.md files, directories)
2. **Logging system** (log-index format, file pairing, session script)
3. **Literature infrastructure** (scripts, PIPELINE.md, boolean-search-guide)
4. **Log file pairing gaps** (missing author-input or claude-contribution files for past dates)

For each category with gaps, ask: **fix now or mark as TODO?**

Do not ask one question per missing file. Ask per category, listing what is missing within it.

**For new projects** (no CLAUDE.md found at root), ask 3–4 focused questions before scaffolding:
1. Research topic and paper title (working)
2. Target journal and its key requirements
3. Author name(s) for CLAUDE.md header
4. Whether to set up literature search infrastructure now or defer

---

## Phase 3: Initialize or patch

Execute the choices from Phase 2.

**For new projects**: Use templates from `references/project-structure.md` and the `examples/` directory. Adapt all templates to the specific project (journal, topic, author names).

**For existing projects**: Create only what is missing. Do not overwrite existing files.

**For log-index updates**: If the table lacks the claude-contribution column, add it. Do not alter existing data rows — just extend the header and add the new column to each existing row as `—` where the file does not exist.

**For missing paired log files**: If an existing decision log has no author-input or claude-contribution file, create skeleton files with a note that they were reconstructed retroactively. Do not fabricate content.

---

## Logging system

Every session produces up to three files in `logs/`. All three are required for sessions where substantive intellectual work occurred.

### Decision log: `YYYY-MM-DD.md`

Records what was decided. See `references/log-formats.md` for the full format spec and `examples/YYYY-MM-DD.md` for an annotated example.

Key fields: decisions (outcome + reasoning if non-obvious), superseded decisions (backward pointer), open questions, closed questions.

### Author-input file: `YYYY-MM-DD-author-input.md`

Records what the author brought to the session — intellectual origin of the work.

Written in first-person prose, contemporaneous research memo tone. Includes: ideas and framings the author introduced, redirections and corrections the author made to AI suggestions, pushbacks (where and why AI output was rejected or modified), decisions that originated with the author rather than from AI elaboration.

Excludes: ideas the AI originated and were accepted without modification; routine procedural exchanges.

### Claude-contribution file: `YYYY-MM-DD-claude-contribution.md`

Records what Claude contributed intellectually — the counterpart to the author-input file.

Written in neutral third-person academic register. Records two things:

**1. Decisions and reasoning**: What Claude proposed or decided, and the reasoning behind it. Only include reasoning that is non-obvious or where a rejected alternative matters. State the decision without reasoning when it was straightforward.

**2. Initiative attribution**: For each substantive contribution, note whether the direction originated from the author's query/prompt or from Claude's own elaboration:
- Mark as *Initiated by author query* when Claude executed on a direction the author specified
- Mark as *Claude initiative* when Claude introduced a framing, argument, or approach not present in the author's query

**Query-authorship annotation**: When the author's query itself constitutes the intellectual contribution — original framing, argument structure, criteria specification, diagnostic insight — annotate it:

> *Author query as intellectual contribution — [brief description of what the query contributed to the intellectual record]*

This documents the query-authorship concept: the author's prompts and configuration choices are transparency artefacts in their own right, not just instructions.

Excludes: routine file operations, formatting, trivial tool calls, confirmations of prior decisions.

See `references/claude-contribution-guide.md` for detailed guidance and `examples/YYYY-MM-DD-claude-contribution.md` for an annotated example.

### Log index: `logs/log-index.md`

Four-column table maintained as a running index:

```
| Date | Decision log | Author-input | Claude-contribution | Key decisions |
|------|------|------|------|---------------|
| YYYY-MM-DD | YYYY-MM-DD.md | YYYY-MM-DD-author-input.md | YYYY-MM-DD-claude-contribution.md | one-line summary |
```

### Session-start protocol

At the start of each new session (today's date differs from the most recent log entry):

1. Run `bash scripts/log_session_meta.sh` from the project root. Note any version change in today's log.
2. Read `logs/log-index.md` to identify the most recent log date.
3. Check for missing log files between the most recent log and today. If project files were modified on missing dates, reconstruct the missing logs from available evidence.
4. Read the most recent decision log, author-input file, and claude-contribution file.
5. Write `logs/YYYY-MM-DD-session-summary.md` (today's date). Cover: what was worked on, what decisions were made, what the author initiated, what Claude initiated. Keep to a short paragraph.
6. Set up a background log-check cron job: every 2 hours at :17, check whether a log file exists for today and create one if substantive work has occurred.
7. Ask: "The previous session has been summarised. Would you like to run `/clear` to start with a clean context? All state is stored in project files."

---

## Literature search infrastructure

When setting up literature search from scratch, use the script templates in `references/literature-pipeline.md`. The full 8-step pipeline is documented there.

### Script inventory

| Script | Language | Purpose |
|---|---|---|
| `scripts/search_openalex.R` | R | OpenAlex API keyword search, deduplication |
| `scripts/download_pdfs.R` | R | Unpaywall PDF retrieval |
| `scripts/filter_results.py` | Python | Abstract screening with keyword exclusion |
| `scripts/screen_candidates.py` | Python | Applies exclusion criteria, generates decisions |
| `scripts/rename_pdfs.py` | Python | Metadata extraction, PDF renaming |
| `scripts/screen_fulltexts.py` | Python | Full-text relevance scoring by theme |
| `scripts/populate_upload_folders.py` | Python | Copies top PDFs by theme to upload folders |
| `scripts/log_session_meta.sh` | Bash | Captures CLI and model version to audit trail |

### Directory structure under `literature/`

```
literature/
├── CLAUDE.md               ← scope statement: which claims need grounding
├── PIPELINE.md             ← 8-step pipeline documentation
├── pdfs/                   ← PDFs organized by search string (A/, B/, ... )
│   └── [A-H]/
├── automated_literature_searches/
│   ├── combined_results.csv
│   ├── filter_candidates.json
│   ├── filter_decisions.json
│   ├── openalex_retained.csv
│   ├── fulltext_scores.csv
│   └── search_summary_report.md
└── notebooklm/
    ├── upload_theme_a/     ← top PDFs for Theme A (structured AI use)
    ├── upload_theme_b/     ← top PDFs for Theme B (explicit reasoning / open science)
    ├── upload_theme_c/     ← top PDFs for Theme C (journal policy)
    └── notebooklm_export/
```

---

## Additional resources

### Reference files

For detailed content loaded as needed:
- **`references/project-structure.md`** — full folder tree and CLAUDE.md templates for each subfolder
- **`references/log-formats.md`** — complete format specifications for all three log files
- **`references/claude-contribution-guide.md`** — initiative attribution and query-authorship annotation guidance
- **`references/literature-pipeline.md`** — 8-step search pipeline with script parameters

### Example files

Working templates to copy when initializing:
- **`examples/root-CLAUDE.md`** — parameterized root CLAUDE.md template
- **`examples/YYYY-MM-DD.md`** — annotated decision log entry
- **`examples/YYYY-MM-DD-author-input.md`** — annotated author-input file
- **`examples/YYYY-MM-DD-claude-contribution.md`** — annotated claude-contribution file with query-authorship examples
