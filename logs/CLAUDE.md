# CLAUDE.md — logs/

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

### Superseded decisions
- [YYYY-MM-DD log, brief description of original decision] — superseded by: [new decision, documented above]

### Open questions
- [question] — carried from [date] if applicable

### Closed questions
- [question] — resolved: [outcome]
```

`### Superseded decisions` is optional — only include it when a prior decision from an earlier log is being reversed or significantly modified. The new decision goes in `### Decisions` as normal; this section just adds a backward pointer so the audit trail is continuous. For approaches that are fully abandoned rather than replaced, use `dismissed_ideas/` instead.

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

### Session-start protocol

At the start of each new session (i.e. when today's date differs from the most recent log entry), do the following before any other work:

1. Run `bash scripts/log_session_meta.sh` from the project root to capture CLI and model version. If the output says "Version change logged", note the new version in today's decision log.
2. Read `logs/log-index.md` to identify the most recent log date.
3. Check whether log files exist for every date between the most recent log and today. If any dates are missing, check whether project files were modified on those dates (e.g. notes created, CLAUDE.md edited, scripts changed). If so, reconstruct the missing log and author-input files from available evidence before proceeding.
4. Read the most recent log file and author-input file.
5. Write a brief summary of the previous session as `logs/YYYY-MM-DD-session-summary.md` (where the date is today's date). The summary should cover: what was worked on, what decisions were made, and what the author contributed or initiated. Keep it to a short paragraph — this is a transition record, not a full recap.
6. Set up a background log-check cron job: every 2 hours at :17, check whether a log file exists for today and create one if substantive work has occurred in the conversation. This job is session-only and must be recreated each session.
7. After completing steps 1–6, ask: "The previous session has been summarised in `logs/YYYY-MM-DD-session-summary.md`. Would you like to run `/clear` to start with a clean context? All state is stored in project files."

**Rationale:** The project is designed so that all needed state lives on disc. Starting each session by summarising the prior one and then clearing context keeps the working memory lean, prevents context drift, and ensures the author-input logs form a continuous record across sessions. The missing-log check catches sessions that closed before a log was written. The cron job catches long sessions where logging is forgotten mid-conversation.

### Log index format

`log-index.md` maintains a single running table:

| Date | Decision log | Author-input log | Key decisions |
|------|------|------|---------------|
| YYYY-MM-DD | filename | filename | one-line summary |
