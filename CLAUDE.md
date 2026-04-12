# CLAUDE.md — Project: Structured AI Use in Sociological Research

## Project overview

This paper argues for a principled distinction between *structured* and *unstructured* AI use in academic research, develops a practical workflow implementing structured use across the full research process, and draws implications for journal policy. The target journal is **Sociological Science** (open access, Diamond OA).

The paper is both descriptive (here is a workflow) and softly normative (structured use is epistemically and ethically preferable to unstructured use, and current journal policies do not make this distinction). It must be framed as a **methodological contribution**, not a commentary — Sociological Science expects substantive sociological scholarship, not opinion pieces.

## Core argument

1. The structured/unstructured distinction — not AI use versus non-use — is the epistemically relevant axis for policy.
2. Structured AI use forces explicit articulation of tacit research decisions, functioning analogously to pre-registration.
3. This produces transparency artefacts (prompt templates, skill configurations, search logs) that are open-science compatible.
4. Current journal policies are blunt instruments that inadvertently penalise good practice.
5. A documentation-based policy framework is preferable to blanket restriction or blanket permission.

## Key conceptual distinctions (use consistently throughout)

- **Structured use**: tool configurations with explicit criteria, built-in human verification at each stage, documented outputs
- **Unstructured use**: accepting AI outputs without systematic verification or explicit criteria
- **Skills / reviewer skills**: configured AI personas with discipline-specific review criteria
- **Transparency artefacts**: prompt templates, skill files, search logs, NotebookLM source sets — shareable as supplementary materials

## Argument requiring empirical grounding (literature tasks)

The following claims need support from the literature search:

- That sociology has been slow to engage with AI tools methodologically (relative to other fields)
- That current journal policies vary widely and are largely binary (permit/prohibit)
- That making reasoning explicit has epistemic value (connects to pre-registration, tacit knowledge, open science literature)
- That structured workflows improve reliability and thoroughness in analogous contexts

## Writing instructions

- Use the `skardhamar-style` skill for all prose drafting and review
- First-person, explicitly argumentative stance throughout
- Hedging hierarchy must be strictly observed (see style skill)
- No bullet points in running prose — use natural language enumeration
- Concessive moves required before any critique of journal policies or existing AI guidance
- Scope limitations stated at point of relevance, not batched
- Literature review in the paper itself must be **short and concise** — cite to support claims, do not survey. The extensive background work done here feeds the argument, not the prose.
- Frame consistently as a **methodological contribution**: the paper demonstrates a workflow, argues for its epistemic properties, and draws policy implications. It is not a think-piece or a commentary.

## File structure

```
ai-sociology-paper/
├── CLAUDE.md                        ← this file
├── logs/
│   ├── log-index.md                 ← running index of all sessions
│   └── YYYY-MM-DD.md                ← one log file per date, sections per work stage
├── literature/
│   ├── boolean-searches.md          ← search terms and strategy
│   ├── notes-ai-in-social-science.md
│   ├── notes-explicit-reasoning.md
│   ├── notes-grey-literature.md
│   └── [imported sources as needed]
├── notes/
│   ├── [topic].md                   ← working notes (see notes instructions below)
│   └── used/                        ← notes moved here once content is incorporated
├── outline.md                       ← working outline (exists)
├── scripts/                         ← reusable workflow scripts
│   ├── search_openalex.R            ← OpenAlex + Semantic Scholar search
│   ├── download_pdfs.R              ← Unpaywall PDF retrieval
│   └── copy_pdfs_from_zotero.py    ← copy PDFs from Zotero storage
├── draft/
│   ├── v1-draft.md
│   └── [subsequent versions]
├── supplementary/
│   ├── example-skill-reviewer.md
│   ├── example-prompt-templates.md
│   ├── file-structure-template.md
│   └── boolean-search-guide.md
└── dismissed_ideas/                 ← archived approaches with reasons (see DISMISSED_LOG.md)
```

---

## Notes instructions

When asked to make a note, save it as a `.md` file in `notes/`. Name the file after the topic (e.g. `notes/pre-registration-analogy.md`). Notes are informal — they can be fragments, observations, argument sketches, or reminders to self.

**When drafting begins**, treat `notes/` as a primary source of content alongside the literature notes. Check `notes/` before drafting any section to see if relevant material has already been captured.

**When a note's content has been used** — incorporated into the draft, implemented as a skill, encoded in a script, added to a template, or otherwise acted on — move the file to `notes/used/`. Files in `notes/used/` are archived and should not be drawn on again unless explicitly requested. Do not delete them.

---

## Logging instructions

Create a log entry whenever a work stage completes or a substantive decision is made. Do not wait for end of conversation. If a conversation produces no decisions and completes no work stage, no log entry is needed.

Each date has one log file and one author-input file. If a session produces multiple work stages or decisions, add them as sections within the same daily file. Create a new file in `logs/` named `YYYY-MM-DD.md` and update `logs/log-index.md`.

### What to log

- **Decisions**: Record every substantive decision — argument framing, scope changes, structural choices, journal targeting, tool choices. These are always logged.
- **Consequential reasoning**: Log reasoning only when it is non-obvious or when the rejected alternative matters. If a decision was straightforward, state the decision without the reasoning.
- **Open questions**: Carry forward any unresolved questions explicitly. Mark resolved questions as closed in the next log that resolves them.
- **Search and source events**: Log when searches are executed, what they returned, and what was retained. Do not log search mechanics in detail — just outcomes and decisions.

### What NOT to log

- Trivial exchanges and clarifications
- Drafting iterations (those live in `draft/`)
- Content summaries of sources (those live in `literature/notes-*.md`)
- Routine confirmations of prior decisions

### Log file format

```
# Log: YYYY-MM-DD
## Previous log: [filename or "none"]

## [Work stage or topic]

### Decisions
[Decision]: [outcome]. [Consequential reasoning only if non-obvious.]

### Open questions
- [question] — carried from [date] if applicable

### Closed questions
- [question] — resolved: [outcome]
```

### Author-input file

Every session log must be accompanied by a paired `YYYY-MM-DD-author-input.md` file. This file documents what the author brought to the session — ideas, framings, arguments, redirections, and pushbacks — in first-person prose, written as a contemporaneous record.

**Purpose:** To document the intellectual origin of the work. The decision log records what was decided; the author-input file records who originated what. This is essential for transparency about the human-AI division of labour and defends against the criticism that the work is AI-generated rather than AI-assisted.

**What to include:**
- Ideas, framings, and arguments the author introduced
- Redirections and corrections the author made to AI suggestions
- Pushbacks — cases where the author rejected or modified AI output and why
- Decisions that originated with the author rather than from AI elaboration

**What to exclude:**
- Ideas that originated with the AI and were accepted without modification
- Routine confirmations and procedural exchanges

**Format:** Continuous prose, first person. Not a list. The tone is that of a research memo to oneself — precise but not formal.

### Log index format

`log-index.md` maintains a single running table:

| Date | Decision log | Author-input log | Key decisions |
|------|------|------|---------------|
| YYYY-MM-DD | filename | filename | one-line summary |

## Target journal requirements (Sociological Science)

- Diamond open access (no APC)
- **No word limit** — but brevity is explicitly valued and long literature reviews are discouraged. Keep the literature review section short and concise; the extensive background work feeds the argument, not the prose.
- Abstract: 150 words maximum
- All sociological scholarship types welcomed, including novel theoretical ideas without empirical results
- **Replication package mandatory** (since April 2023): must submit statistical code and data sufficient to reproduce reported results as condition of publication. For this paper, the transparency artefacts (prompt templates, skill files, R scripts, search logs) serve as the replication package — this is a strong fit and should be noted explicitly in the methods section.
- Qualitative work: data analysis methods must be documented; anonymity and consent disclosures required
- Quantitative work: substantive effect sizes over statistical significance; graphical displays preferred; control variable tables in appendices
- No explicit AI policy — consistent with the paper's argument that current policies are underdeveloped
- Follows COPE Code of Conduct; CrossCheck/iThenticate similarity screening applies
- Check current author guidelines and Manuscript Preparation page before submission

## What this paper is NOT

- Not a review paper cataloguing all AI tools
- Not a technical paper about how AI works
- Not a polemic against journal policies
- Not a claim that AI replaces expert judgment

## Key things to avoid in drafting

- Overstating the reliability of AI outputs
- Treating the workflow as universally applicable (scope it to sociology and adjacent fields)
- Making the journal policy critique the main event — it is an implication, not the thesis
- Generic "AI is changing everything" framing in the introduction
- Long literature review sections — Sociological Science explicitly discourages them
- Commentary or opinion-piece tone — must read as methodological scholarship
