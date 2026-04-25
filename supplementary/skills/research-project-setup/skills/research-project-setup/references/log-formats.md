# Log File Formats

All three files are created for each session where substantive intellectual work occurred. They are paired by date and indexed in `logs/log-index.md`.

---

## 1. Decision log: `YYYY-MM-DD.md`

Records what was decided. Written by Claude during and after the session.

### Format

```markdown
# Log: YYYY-MM-DD
## Previous log: [filename or "none"]

---

## [Work stage or topic]

### Decisions
[Decision label]: [outcome]. [Reasoning only if non-obvious or rejected alternative matters.]

[Decision label]: [outcome].

### Superseded decisions
- [YYYY-MM-DD log, brief description of original decision] — superseded by: [new decision, documented above]

### Open questions
- [question] — carried from [date] if applicable
- [question]

### Closed questions
- [question] — resolved: [outcome]
```

### Notes on fields

**`## Previous log:`** Links the audit trail. Use the filename (`YYYY-MM-DD.md`), not a full path.

**`### Decisions`** is required when the session produced any. State the decision first, reasoning second. If the decision was straightforward, state it without reasoning. Never summarize what was discussed — record what was decided.

**`### Superseded decisions`** is optional. Include only when a prior decision from an earlier log is being reversed or significantly modified. The new decision goes in `### Decisions` as normal; this section adds a backward pointer. For approaches that are fully abandoned rather than replaced, use `dismissed_ideas/` instead.

**`### Open questions`** carries forward unresolved questions. Include the date they were first opened. Remove questions from this section only when they appear in `### Closed questions`.

---

## 2. Author-input file: `YYYY-MM-DD-author-input.md`

Records the intellectual origin of the work from the author's side. Written by the author, or reconstructed by Claude on the author's instruction.

### Format

```markdown
# Author input: YYYY-MM-DD

[Continuous prose, first person, contemporaneous research memo tone. Not a list.]

[Paragraph 1: what the author initiated in this session — ideas, framings, arguments introduced.]

[Paragraph 2: any redirections or corrections — cases where the author pushed back on AI suggestions, modified AI output, or changed direction.]

[Paragraph 3 (if applicable): decisions that originated with the author rather than from AI elaboration — what the author's own judgment settled.]
```

### What to include

- Ideas, framings, and arguments the author introduced
- Redirections and corrections the author made to AI suggestions
- Pushbacks — cases where the author rejected or modified AI output, with brief note of why
- Decisions that originated with the author rather than from AI elaboration

### What to exclude

- Ideas that originated with the AI and were accepted without modification
- Routine confirmations and procedural exchanges
- Content summaries of what was produced (that lives in the decision log)

### Tone

First-person, contemporaneous, precise but not formal. Write as a research memo to oneself. The purpose is to document intellectual origin, not to narrate the session.

---

## 3. Claude-contribution file: `YYYY-MM-DD-claude-contribution.md`

Records what Claude contributed intellectually. The counterpart to the author-input file. Written by Claude at the end of each session.

### Format

```markdown
# Claude contribution: YYYY-MM-DD

## [Work stage or topic — mirrors the decision log section]

[For each substantive contribution:]

**[Topic or decision]** — [Initiative attribution: "Initiated by author query" or "Claude initiative"]

[What Claude proposed or decided, and the reasoning behind it. State the decision without reasoning when it was straightforward. Only include reasoning that is non-obvious or where a rejected alternative matters.]

[If the author's query itself was the intellectual contribution, add the query-authorship annotation:]
*Author query as intellectual contribution — [brief description of what the query contributed: e.g., "introduced the framing of X as analogous to Y", "specified the exclusion criteria for Z", "identified the diagnostic question about W"]*

---

[Repeat for each substantive contribution in the session.]
```

### Initiative attribution

Every substantive contribution must carry one of two labels:

- **Initiated by author query**: Claude executed on a direction the author specified. The author's query drove the intellectual move.
- **Claude initiative**: Claude introduced a framing, argument, connection, or approach not present in the author's query.

Use "Claude initiative" sparingly and accurately. Most contributions in a well-run structured session should be "Initiated by author query" — that is the point of structured AI use.

### Query-authorship annotation

When the author's query constitutes an intellectual contribution in its own right — not just an instruction to execute, but an original framing, a precise diagnostic question, a specification of criteria, or a structural insight — add the annotation:

> *Author query as intellectual contribution — [what the query contributed]*

This annotation implements the query-authorship concept: it places the author's prompts in the transparency record as intellectual contributions, not merely as instructions. This is especially important for:

- Queries that introduce a new argument or framing
- Queries that specify evaluation criteria or review protocols
- Queries that identify a conceptual problem or diagnostic question
- Queries that redirect work based on the author's own reasoning

### What to exclude

- Routine file operations (reading, writing, renaming)
- Formatting and structural tasks
- Trivial tool calls and confirmations
- Summaries of what was already decided elsewhere

### Tone

Neutral third-person academic register. Not first person. Describe Claude's contributions as one would describe any research assistant's contributions in a CRediT-style declaration — accurate, specific, without inflation.

---

## Log index: `log-index.md`

Running table maintained in `logs/log-index.md`. Add a row at the end of each session.

### Format

```markdown
# Log index

| Date | Decision log | Author-input | Claude-contribution | Key decisions |
|------|------|------|------|---------------|
| 2026-01-15 | 2026-01-15.md | 2026-01-15-author-input.md | 2026-01-15-claude-contribution.md | Project scaffold initialized; logging system set up |
| 2026-01-16 | 2026-01-16.md | 2026-01-16-author-input.md | 2026-01-16-claude-contribution.md | First draft section written; scope narrowed to sociology |
```

Use `—` in any column where a file does not exist (e.g., retroactively added dates where the claude-contribution file was not yet in use).

**Key decisions** should be a single line summarizing the most consequential decision of the session — the one a future reader would most want to know when scanning the index.
