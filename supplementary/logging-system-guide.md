# Session Logging System — Setup Guide

This guide describes the session logging system used in this project and provides everything needed to replicate it in a new project. The system produces three types of contemporaneous record per session — a decision log, an author-input record, and a Claude-contribution record — along with a running index and a version-tracking file. Together these constitute the process-integrity tier of the replication package.

---

## Design philosophy

The logging system is not conventional automation. It does not run independently; it runs because Claude Code reads persistent instructions and follows them. The key design choice is that logging instructions live in a file (`logs/CLAUDE.md`) that Claude loads at session start, which means the instructions are active in every session without the researcher having to remember to invoke them. The only pieces that run without Claude's active involvement are a shell script (for version capture) and an optional background cron job (for mid-session reminders). Everything else — drafting the log entries, writing the author-input file, maintaining the index — is Claude following written instructions.

This design has a specific epistemic purpose: the logs are contemporaneous records of decisions as they were made, not retrospective summaries. Their value as transparency artefacts depends on being written during or immediately after the work, not reconstructed later.

---

## System components

| Component | Location | Purpose |
|-----------|----------|---------|
| Logging instructions | `logs/CLAUDE.md` | Tells Claude when, what, and how to log |
| Decision log | `logs/YYYY-MM-DD.md` | Substantive decisions made in each session |
| Author-input record | `logs/YYYY-MM-DD-author-input.md` | What the author brought and initiated |
| Claude-contribution record | `logs/YYYY-MM-DD-claude-contribution.md` | What Claude contributed and reasoned |
| Log index | `logs/log-index.md` | Running table of all session files |
| Version log | `logs/version-log.md` | Claude Code CLI version and model per session |
| Version-capture script | `scripts/log_session_meta.sh` | Shell script; run at session start |

---

## Step 1 — Create `logs/CLAUDE.md`

This file is the core of the system. Claude Code loads it automatically because it is inside the project directory. Its content tells Claude what to do at the start of every session and what to write into the log files.

Create `logs/CLAUDE.md` with the following content, adapting the session-start protocol to your project's needs:

```markdown
# CLAUDE.md — logs/

## Logging instructions

Create a log entry whenever a work stage completes or a substantive decision is made. 
Do not wait for end of conversation. If a conversation produces no decisions and 
completes no work stage, no log entry is needed.

Each date has one log file and one author-input file. If a session produces multiple 
work stages or decisions, add them as sections within the same daily file. Create a 
new file in `logs/` named `YYYY-MM-DD.md` and update `logs/log-index.md`.

### What to log

- **Decisions**: Record every substantive decision — argument framing, scope changes, 
  structural choices, journal targeting, tool choices. These are always logged.
- **Consequential reasoning**: Log reasoning only when it is non-obvious or when the 
  rejected alternative matters. If a decision was straightforward, state the decision 
  without the reasoning.
- **Open questions**: Carry forward any unresolved questions explicitly. Mark resolved 
  questions as closed in the next log that resolves them.
- **Search and source events**: Log when searches are executed, what they returned, 
  and what was retained. Do not log search mechanics in detail — just outcomes and 
  decisions.

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
- [YYYY-MM-DD log, brief description of original decision] — superseded by: 
  [new decision, documented above]

### Open questions
- [question] — carried from [date] if applicable

### Closed questions
- [question] — resolved: [outcome]
```

`### Superseded decisions` is optional — only include it when a prior decision from 
an earlier log is being reversed or significantly modified. The new decision goes in 
`### Decisions` as normal; this section just adds a backward pointer so the audit 
trail is continuous. For approaches that are fully abandoned rather than replaced, 
use `dismissed_ideas/` instead.

### Author-input file

Every session log must be accompanied by a paired `YYYY-MM-DD-author-input.md` file. 
This file documents what the author brought to the session — ideas, framings, 
arguments, redirections, and pushbacks — in first-person prose, written as a 
contemporaneous record.

**Purpose:** To document the intellectual origin of the work. The decision log records 
what was decided; the author-input file records who originated what. This is essential 
for transparency about the human-AI division of labour and defends against the 
criticism that the work is AI-generated rather than AI-assisted.

**What to include:**
- Ideas, framings, and arguments the author introduced
- Redirections and corrections the author made to AI suggestions
- Pushbacks — cases where the author rejected or modified AI output and why
- Decisions that originated with the author rather than from AI elaboration

**What to exclude:**
- Ideas that originated with the AI and were accepted without modification
- Routine confirmations and procedural exchanges

**Format:** Continuous prose, first person. Not a list. The tone is that of a research 
memo to oneself — precise but not formal.

### Claude-contribution file

Every session log must also be accompanied by a `YYYY-MM-DD-claude-contribution.md` 
file. This is the counterpart to the author-input file: it documents what Claude 
contributed intellectually to the session, written in neutral third-person academic 
register by Claude at the end of the session.

**Purpose:** To complete the transparency record of the human-AI division of 
intellectual labour. The author-input file records the author's contributions; this 
file records Claude's. Together they allow a full account of who originated what — 
essential for query-authorship transparency and for any CRediT-style disclosure.

**What to include:**
- Decisions Claude proposed and the reasoning behind them (only when non-obvious)
- Initiative attribution for each substantive contribution: *Initiated by author 
  query* or *Claude initiative*
- Query-authorship annotations when the author's query itself was an intellectual 
  contribution — a framing, criteria specification, diagnostic question, or 
  structural insight: *Author query as intellectual contribution — [description]*

**What to exclude:**
- Routine file operations and formatting
- Trivial tool calls and confirmations
- Session narrative — record intellectual output, not process

**Format:** Neutral third-person, structured by work stage (mirroring the decision 
log). Typical length: 300–600 words for a substantive session.

### Session-start protocol

At the start of each new session (i.e. when today's date differs from the most 
recent log entry), do the following before any other work:

1. Run `bash scripts/log_session_meta.sh` from the project root to capture CLI and 
   model version. If the output says "Version change logged", note the new version 
   in today's decision log.
2. Read `logs/log-index.md` to identify the most recent log date.
3. Check whether log files exist for every date between the most recent log and 
   today. If any dates are missing, check whether project files were modified on 
   those dates (e.g. notes created, CLAUDE.md edited, scripts changed). If so, 
   reconstruct the missing log and author-input files from available evidence before 
   proceeding.
4. Read the most recent log file, author-input file, and claude-contribution file.
5. Write a brief summary of the previous session as 
   `logs/YYYY-MM-DD-session-summary.md` (where the date is today's date). The 
   summary should cover: what was worked on, what decisions were made, what the 
   author initiated, and what Claude initiated. Keep it to a short paragraph — this 
   is a transition record, not a full recap.
6. Set up a background log-check cron job: every 2 hours at :17, check whether a 
   log file exists for today and create one if substantive work has occurred in the 
   conversation. This job is session-only and must be recreated each session.
7. After completing steps 1–6, ask: "The previous session has been summarised in 
   `logs/YYYY-MM-DD-session-summary.md`. Would you like to run `/clear` to start 
   with a clean context? All state is stored in project files."

**Rationale:** The project is designed so that all needed state lives on disc. 
Starting each session by summarising the prior one and then clearing context keeps 
the working memory lean, prevents context drift, and ensures the author-input logs 
form a continuous record across sessions. The missing-log check catches sessions 
that closed before a log was written. The cron job catches long sessions where 
logging is forgotten mid-conversation.

### Log index format

`log-index.md` maintains a single running table:

| Date | Decision log | Author-input | Claude-contribution | Key decisions |
|------|------|------|------|---------------|
| YYYY-MM-DD | filename | filename | filename | one-line summary |
```

---

## Step 2 — Create `logs/log-index.md`

This is a manually maintained running table. Create it once and let Claude maintain it:

```markdown
# Log Index

## Project: [Your project title]

| Date | Decision log | Author-input | Claude-contribution | Key decisions |
|------|------|------|------|---------------|
```

Claude appends a new row to this table at the end of each session.

---

## Step 3 — Create `logs/version-log.md`

Create this file once. It will be appended to automatically by the shell script:

```markdown
# Version Log

Records Claude Code CLI version and model in use. A new entry is appended only 
when either value changes from the previous session. This file is part of the 
replication package.

| Field | What it captures |
|-------|-----------------|
| Claude Code | CLI tool version (`claude --version`) |
| Model | Configured model identifier |
| Git commit | Project repo state at the time of the version change |
```

---

## Step 4 — Create `scripts/log_session_meta.sh`

This shell script detects the current Claude Code version and configured model, and appends an entry to `logs/version-log.md` only when either value has changed since the last run. It is run by Claude at step 1 of the session-start protocol.

```bash
#!/usr/bin/env bash
# Logs Claude Code version and model to logs/version-log.md.
# Appends a new entry only when version or model has changed since last run.
# Run from the project root at session start.

set -euo pipefail

LOG_FILE="logs/version-log.md"

TIMESTAMP=$(date '+%Y-%m-%d %H:%M')
CLAUDE_VERSION=$(claude --version 2>/dev/null | head -1 || echo "unknown")

# Model: check ANTHROPIC_MODEL env var, then settings files, then fall back to 
# advisory message. Claude Code does not expose the active model via CLI, so 
# per-session model switching cannot be detected automatically.
MODEL="${ANTHROPIC_MODEL:-}"
if [ -z "$MODEL" ]; then
    MODEL=$(python3 -c "
import json, os
for f in [os.path.expanduser('~/.claude/settings.json'), '.claude/settings.json', 
          '.claude/settings.local.json']:
    if os.path.exists(f):
        try:
            d = json.load(open(f))
        except Exception:
            continue
        m = d.get('model') or d.get('preferredModel') or ''
        if m:
            print(m)
            exit()
print('')
" 2>/dev/null || echo "")
fi
[ -z "$MODEL" ] && MODEL="not configured — annotate in session log (Opus / Sonnet / Haiku)"

GIT_COMMIT=$(git rev-parse HEAD 2>/dev/null || echo "no-git")
GIT_BRANCH=$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo "")

# Extract last recorded values for change detection
LAST_VERSION=$(grep '^\- \*\*Claude Code:\*\*' "$LOG_FILE" 2>/dev/null | tail -1 \
    | sed 's/.*\*\* //' | tr -d '\r' || echo "")
LAST_MODEL=$(grep '^\- \*\*Model:\*\*' "$LOG_FILE" 2>/dev/null | tail -1 \
    | sed 's/.*\*\* //' | tr -d '\r' || echo "")

if [ "$CLAUDE_VERSION" = "$LAST_VERSION" ] && [ "$MODEL" = "$LAST_MODEL" ]; then
    echo "Version unchanged ($CLAUDE_VERSION / $MODEL) — no log entry written."
    exit 0
fi

{
    echo ""
    echo "## $TIMESTAMP"
    echo "- **Claude Code:** $CLAUDE_VERSION"
    echo "- **Model:** $MODEL"
    echo "- **Git commit:** \`$GIT_COMMIT\` ($GIT_BRANCH)"
} >> "$LOG_FILE"

echo "Version change logged: $CLAUDE_VERSION / $MODEL"
```

Make it executable:

```bash
chmod +x scripts/log_session_meta.sh
```

---

## Step 5 — The cron job (session-only)

The session-start protocol instructs Claude to set up a background cron job at the start of each session. This job runs every two hours (at minute :17) and checks whether a log file for the current date already exists. If substantial work has occurred in the session but no log has been written yet, Claude writes one.

**Important**: this cron job is session-only. It does not persist between Claude Code sessions. Step 6 of the session-start protocol must be executed at the start of every new session.

Claude sets this up using the `CronCreate` tool (a Claude Code built-in scheduling mechanism). The instruction in `logs/CLAUDE.md` triggers Claude to invoke `CronCreate` with a prompt along these lines:

> Check whether a log file exists for today's date in `logs/`. If today's date is present in `logs/log-index.md`, no action is needed. If not, and if substantive work has occurred in this conversation, write the decision log, author-input, and claude-contribution files for today and update `logs/log-index.md`.

The cron job schedule used in this project is: **every 2 hours at minute :17** (i.e., 09:17, 11:17, 13:17, etc.). The :17 offset is arbitrary but ensures the check does not coincide exactly with the hour boundary.

**If you are not using Claude Code's scheduling tools**, the cron job step can be omitted. Replace it with a manual end-of-session reminder in your `CLAUDE.md`: "At the end of every session, write the decision log, author-input, and claude-contribution files before closing."

---

## Step 6 — Add the session-start instruction to the root `CLAUDE.md`

The session-start protocol in `logs/CLAUDE.md` is loaded by Claude, but it must also be referenced from the root `CLAUDE.md` so that Claude knows to read it. Add this line near the top of your root `CLAUDE.md`:

```markdown
**Session-start protocol**: see `logs/CLAUDE.md`. Run it at the start of every 
session before any other work.
```

This is the trigger. When Claude opens the project, it reads the root `CLAUDE.md`, sees this instruction, reads `logs/CLAUDE.md`, and follows the session-start protocol.

---

## What triggers logging — summary

| Trigger | Who acts | What is written |
|---------|----------|-----------------|
| Substantive decision made during session | Claude, following `logs/CLAUDE.md` | Entry added to `logs/YYYY-MM-DD.md` |
| Session ends | Claude, following `logs/CLAUDE.md` | Complete decision log + author-input + claude-contribution |
| Session starts (new date) | Claude, following session-start protocol | Session summary for previous session; version check |
| Every 2 hours during session | Cron job, set up by Claude via `CronCreate` | Log written if missing and work has occurred |
| Claude Code version or model changes | `log_session_meta.sh`, run by Claude | New entry in `logs/version-log.md` |

Nothing in this system runs automatically without Claude being active in a session, except the cron job — and that only works because Claude set it up at session start.

---

## What the three log files look like in practice

### Decision log (`YYYY-MM-DD.md`)

```markdown
# Log: 2026-04-25
## Previous log: 2026-04-23.md

---

## Literature synthesis — writing-as-thinking sources

### Decisions

**Source selection:** Emig (1977) selected as primary theoretical source for the 
deliberate-semantics mechanism. Sommers (1981) selected for the 
revision-as-discovery framing. Donnelly (2018) excluded: citation count too low 
to carry argumentative weight independently.

**Draft edit:** Two paragraphs in the drafting section replaced with tighter text 
grounded in Emig and Sommers. Prain & Hand (2016) retained alongside Quitadamo & 
Kurtz (2007) as empirical support.

### Closed questions

- Hindawi 8000+ figure: author confirmed Retraction Watch (2023) carries the 
  figure. Reference added.

### Open questions

- None carried forward.
```

### Author-input record (`YYYY-MM-DD-author-input.md`)

```markdown
# Author input: 2026-04-25

Today I identified a gap in the draft: the writing-as-thinking argument was 
asserted rather than argued, and the extension to configuration work lacked 
grounding. I directed attention to the writingThinking NotebookLM source file 
as the material to draw on.

After reviewing the assessment, I made the source selection decisions myself: 
Emig and Sommers as primary, Quitadamo & Kurtz as empirical support. I 
explicitly excluded Donnelly (citation count too low) and Warner (YouTube video, 
not peer-reviewed). The structural decision to introduce the sources in the 
unsystematic section first — as a critique — and then invoke them in the 
drafting section was mine; Claude had proposed treating them primarily as 
positive support in the drafting section.
```

### Claude-contribution record (`YYYY-MM-DD-claude-contribution.md`)

```markdown
# Claude contribution: 2026-04-25

## Literature assessment — writing-as-thinking sources

*Initiated by author query.*

Claude read the NotebookLM summary of eight sources and produced a note 
assessing each for relevance. The assessment identified Emig (1977) as the 
most theoretically useful source and Sommers (1981) as most directly applicable 
to the specification-work argument. The concessive-then-turn structure using 
Warner was Claude's suggestion; the author rejected it.

*Author query as intellectual contribution — the two-stage introduction 
structure (unsystematic section first, then drafting section) was the author's 
framing. Claude's initial assessment proposed integrating the sources primarily 
in the drafting section.*

## Draft edits

*Initiated by author instruction.*

Claude executed four edits to the draft, replacing the existing paragraphs with 
text grounded in Emig's deliberate-semantics mechanism and Sommers' 
heuristic framing. Five new references added to the reference list.
```

---

## Minimal setup checklist

To replicate this system in a new project:

- [ ] Create `logs/` directory
- [ ] Create `logs/CLAUDE.md` with the full content from Step 1
- [ ] Create `logs/log-index.md` with header and empty table
- [ ] Create `logs/version-log.md` with header
- [ ] Create `scripts/log_session_meta.sh` with the script from Step 4; make executable
- [ ] Add the session-start pointer to root `CLAUDE.md` (Step 6)
- [ ] On first session: run `bash scripts/log_session_meta.sh` manually to create the first version-log entry; then let Claude follow the session-start protocol from there

The system is self-maintaining once these files are in place. Claude reads `logs/CLAUDE.md` at the start of every session and follows the protocol.

---

## Design notes for replication

**Why three files per session, not one?** The decision log records outcomes; the author-input records intellectual origin from the author's side; the claude-contribution records what the AI reasoned and proposed. These are different kinds of information and serve different purposes in a transparency audit. Combining them into one file would make it harder to separate the "what was decided" question from the "who originated what" question.

**Why first-person for author-input?** The author-input file is a contemporaneous research memo, not a formal record. First-person prose is faster to write under cognitive load and reads as a genuine record rather than a performance. The test is whether a reader can tell what the author brought versus what the AI generated.

**Why neutral third-person for claude-contribution?** The file documents an AI system's outputs. Third-person academic register makes it clear that Claude is the subject of the record, not the author. It also makes the initiative-attribution format — "Initiated by author query" — grammatically and semantically natural.

**Why session-only cron job?** Claude Code does not persist state between sessions, so any automated task must be re-established at session start. The cron job is a safety net, not the primary logging mechanism: most logs are written because Claude follows the instructions in `logs/CLAUDE.md`, not because the cron job fires. The job catches long sessions where logging is forgotten mid-conversation.

**Why version tracking?** AI models are updated without notice. The same prompt run against a different model version may produce substantively different outputs. Without a version record, the documentation cannot be reproduced under equivalent conditions. The version log links each session's work to a specific CLI version and — to the extent it is configurable — model identifier.
