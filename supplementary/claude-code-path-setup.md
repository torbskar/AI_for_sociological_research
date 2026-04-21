# Claude Code PATH setup on a new Windows computer

This note documents how to make `claude --version` (and hence `log_session_meta.sh`) work in Git Bash on a new Windows machine. It is needed because Claude Code installs into a versioned subdirectory that is not on the system PATH by default.

## Step 1 — find the claude.exe location

In Git Bash:

```bash
find "/c/Users/$USER/AppData/Roaming/Claude/claude-code" -name "claude.exe" 2>/dev/null
```

Expected output: something like

```
/c/Users/<username>/AppData/Roaming/Claude/claude-code/2.1.111/claude.exe
```

The version number (`2.1.111`) changes on every update, which is why we do not hard-code the path.

## Step 2 — add a dynamic PATH entry to ~/.bashrc

Append the following to `~/.bashrc` (create the file if it does not exist):

```bash
# Claude Code — dynamically resolves the latest installed version
_claude_dir=$(ls -d "/c/Users/$USER/AppData/Roaming/Claude/claude-code/"*/ 2>/dev/null | sort -V | tail -1)
[ -d "$_claude_dir" ] && export PATH="$PATH:${_claude_dir%/}"
unset _claude_dir
```

Using `$USER` instead of a hard-coded username makes the snippet portable across accounts.

## Step 3 — verify

Reload the shell and test:

```bash
source ~/.bashrc
claude --version
```

Expected output: `2.x.xxx (Claude Code)`

## Model logging

Claude Code does not expose the active model via CLI. `log_session_meta.sh` detects the model from the `ANTHROPIC_MODEL` environment variable or the `model` / `preferredModel` field in any of these settings files (checked in order):

1. `~/.claude/settings.json`
2. `.claude/settings.json` (project)
3. `.claude/settings.local.json` (project, local)

If none of those is set — which is the normal state when switching between Opus, Sonnet, and Haiku within a session — the script logs:

```
not configured — annotate in session log (Opus / Sonnet / Haiku)
```

In that case, note which model(s) you used in today's decision log manually. There is no automated way to recover per-task model information after the fact.

To pin a default model for a project, add to `.claude/settings.json`:

```json
{
  "model": "claude-sonnet-4-6"
}
```

Valid model IDs (as of April 2026): `claude-opus-4-7`, `claude-sonnet-4-6`, `claude-haiku-4-5-20251001`.
