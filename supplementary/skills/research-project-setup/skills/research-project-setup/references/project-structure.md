# Project Structure Reference

## Standard folder tree

```
[project-root]/
├── CLAUDE.md                        ← project-wide context (required)
├── outline.md                       ← working outline
├── logs/
│   ├── CLAUDE.md                    ← logging protocol (required)
│   ├── log-index.md                 ← running four-column index
│   ├── YYYY-MM-DD.md                ← decision logs
│   ├── YYYY-MM-DD-author-input.md   ← author intellectual contributions
│   ├── YYYY-MM-DD-claude-contribution.md  ← Claude intellectual contributions
│   └── YYYY-MM-DD-session-summary.md      ← transition record (session-start)
├── draft/
│   ├── CLAUDE.md                    ← draft versioning protocol (required)
│   ├── vN-draft.md                  ← Claude-produced draft
│   └── vN-draft - manualEdit.md     ← author-edited version
├── notes/
│   ├── CLAUDE.md                    ← notes lifecycle protocol (required)
│   ├── [topic].md                   ← working notes (informal, can be fragments)
│   └── used/
│       └── [topic].md               ← archived after incorporation
├── literature/
│   ├── CLAUDE.md                    ← scope: which claims need grounding
│   ├── PIPELINE.md                  ← 8-step search pipeline documentation
│   ├── pdfs/
│   │   └── [A-H]/                   ← PDFs by search string block
│   ├── automated_literature_searches/
│   │   ├── combined_results.csv
│   │   ├── filter_candidates.json
│   │   ├── filter_decisions.json
│   │   ├── openalex_retained.csv
│   │   ├── fulltext_scores.csv
│   │   └── search_summary_report.md
│   └── notebooklm/
│       ├── upload_theme_a/
│       ├── upload_theme_b/
│       ├── upload_theme_c/
│       └── notebooklm_export/
├── scripts/
│   ├── log_session_meta.sh          ← CLI/model version capture
│   ├── search_openalex.R            ← OpenAlex keyword search
│   ├── download_pdfs.R              ← Unpaywall PDF retrieval
│   ├── filter_results.py            ← abstract screening
│   ├── screen_candidates.py         ← exclusion criteria application
│   ├── rename_pdfs.py               ← metadata extraction and renaming
│   ├── screen_fulltexts.py          ← full-text relevance scoring
│   └── populate_upload_folders.py   ← NotebookLM upload folder population
├── supplementary/
│   ├── boolean-search-guide.md      ← search strategy template
│   ├── file-structure-template.md   ← this structure, for other researchers
│   └── skills/                      ← installed skills as transparency artefacts
├── dismissed_ideas/                 ← archived approaches with reasons
└── outline.md                       ← working outline
```

---

## CLAUDE.md templates

### Root CLAUDE.md

```markdown
# CLAUDE.md — Project: [Project Title]

## Project overview

[One paragraph: what the paper argues, what kind of contribution it is, target journal.]

## Core argument

1. [Point 1]
2. [Point 2]
3. [Point 3]

## Key conceptual distinctions (use consistently throughout)

- **[Term]**: [definition]
- **[Term]**: [definition]

## Writing instructions

- Use the `skardhamar-style` skill for all prose drafting and review
- First-person, explicitly argumentative stance throughout
- No bullet points in running prose — use natural language enumeration
- [Any journal-specific constraints]

## File structure

[Paste the standard folder tree, adapted to the project]

**Session-start protocol**: see `logs/CLAUDE.md`. Run it at the start of every session before any other work.

## Target journal requirements ([Journal Name])

- [Key requirements relevant to manuscript preparation]
- Replication package requirements
- Word/abstract limits
- AI disclosure policy (if any)

## What this paper is NOT

- [Scope exclusion 1]
- [Scope exclusion 2]

## Key things to avoid in drafting

- [Framing or tone to avoid]
- [Overstating claims to avoid]
```

---

### logs/CLAUDE.md

```markdown
# CLAUDE.md — logs/

## Logging instructions

Create a log entry whenever a work stage completes or a substantive decision is made. Do not wait for end of conversation. If a conversation produces no decisions and completes no work stage, no log entry is needed.

Each date has one decision log, one author-input file, and one claude-contribution file. Add sections within the same daily file if a session produces multiple work stages.

### What to log

- **Decisions**: Every substantive decision — argument framing, scope changes, structural choices, journal targeting, tool choices.
- **Consequential reasoning**: Only when non-obvious or when the rejected alternative matters.
- **Open questions**: Carry forward unresolved questions explicitly.
- **Search and source events**: Outcomes and decisions, not mechanics.

### What NOT to log

- Trivial exchanges and clarifications
- Drafting iterations (those live in `draft/`)
- Content summaries of sources (those live in `literature/`)
- Routine confirmations of prior decisions

### Log file format

See `references/log-formats.md` in the skill package, or the examples in `examples/`.

### Session-start protocol

[Full protocol as per skill SKILL.md — copy here on initialization]

### Log index format

`log-index.md` maintains a four-column running table:

| Date | Decision log | Author-input | Claude-contribution | Key decisions |
|------|------|------|------|---------------|
| YYYY-MM-DD | filename | filename | filename | one-line summary |
```

---

### draft/CLAUDE.md

```markdown
# CLAUDE.md — draft/

## Draft versioning

Two suffixes distinguish authorship state:

- `vN-draft.md` — produced by Claude
- `vN-draft - manualEdit.md` — author has edited the Claude draft

**Protocol:**
- If the most recent file is `manualEdit`, create a new version as `v(N+1)-draft.md` — do not edit the manualEdit file in place
- If the most recent file is a Claude version, continue editing in place (no new version number)
- Increment the version number only on author request OR when continuing from a manualEdit file

**All prose drafting uses the `skardhamar-style` skill.** Invoke it before drafting any section.
```

---

### notes/CLAUDE.md

```markdown
# CLAUDE.md — notes/

## Notes management

Save working notes as `notes/[topic].md`. Notes can be informal — fragments, argument sketches, open questions, reference reminders.

Before drafting any manuscript section, check `notes/` for relevant material.

When a note's content has been incorporated (into a draft, skill, or other artefact), move the file to `notes/used/`. Files in `notes/used/` are archived; do not reuse unless explicitly requested.
```

---

### literature/CLAUDE.md

```markdown
# CLAUDE.md — literature/

## Claims requiring empirical grounding

The following claims from the paper's core argument need support from the literature search. Keep these in view when sourcing, screening, or annotating:

- [Claim 1 — e.g., the field has been slow to engage with X]
- [Claim 2 — e.g., current practice varies along dimension Y]
- [Claim 3 — connection to existing literature on Z]
- [Claim 4 — analogy or precedent in domain W]
```
