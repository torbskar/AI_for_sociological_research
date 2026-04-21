#!/usr/bin/env bash
# Logs Claude Code version and model to logs/version-log.md.
# Appends a new entry only when version or model has changed since last run.
# Run from the project root at session start.

set -euo pipefail

LOG_FILE="logs/version-log.md"

TIMESTAMP=$(date '+%Y-%m-%d %H:%M')
CLAUDE_VERSION=$(claude --version 2>/dev/null | head -1 || echo "unknown")

# Model: check ANTHROPIC_MODEL env var, then settings files, then fall back to advisory message.
# Claude Code does not expose the active model via CLI, so per-session model switching
# (between Opus, Sonnet, Haiku) cannot be detected automatically. When no model is
# configured in settings, log a prompt to annotate the model manually in today's decision log.
MODEL="${ANTHROPIC_MODEL:-}"
if [ -z "$MODEL" ]; then
    MODEL=$(python3 -c "
import json, os
for f in [os.path.expanduser('~/.claude/settings.json'), '.claude/settings.json', '.claude/settings.local.json']:
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
LAST_VERSION=$(grep '^\- \*\*Claude Code:\*\*' "$LOG_FILE" 2>/dev/null | tail -1 | sed 's/.*\*\* //' | tr -d '\r' || echo "")
LAST_MODEL=$(grep '^\- \*\*Model:\*\*' "$LOG_FILE" 2>/dev/null | tail -1 | sed 's/.*\*\* //' | tr -d '\r' || echo "")

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
