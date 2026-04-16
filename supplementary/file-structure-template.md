# Supplementary: File Structure Template

This template documents the project folder structure for systematic AI authorship workflows in sociology and adjacent social sciences. Two variants are described: the literature-only variant (for papers that work exclusively with published sources) and the empirical variant (for papers with primary data). The folder hierarchy is the same in both cases; the difference is the presence and configuration of the `data/` subtree.

---

## Full project structure

```
project/
├── CLAUDE.md                        ← project context; loaded automatically by Claude Code
├── .claudeignore                    ← paths excluded from AI context (see below)
├── .gitignore                       ← paths excluded from version control
├── data/                            ← empirical projects only; omit for literature-only work
│   ├── raw/                         ← original data; never AI-readable; immutable after receipt
│   ├── interim/                     ← intermediate files after cleaning/anonymisation
│   ├── processed/                   ← analysis-ready datasets; script-generated only
│   └── external/                    ← third-party reference data (SSB, Eurostat, etc.)
├── scripts/                         ← analysis code (R, Python, Stata)
├── outputs/                         ← tables and figures; reproducible from scripts
├── literature/
│   ├── automated_literature_searches/
│   │   ├── boolean-searches.md      ← search strings, result counts, screening decisions
│   │   ├── fulltext_scores.csv      ← relevance scores for full-text screening
│   │   └── filter_tidying/          ← intermediate screening files
│   └── notebooklm/
│       ├── upload_folders/          ← PDF sets uploaded to notebooks (by theme)
│       └── notebooklm_summaries/    ← grounded synthesis outputs
├── notes/                           ← working notes and argument sketches
│   └── used/                        ← notes moved here once content is incorporated
├── outline.md                       ← working outline
├── draft/                           ← manuscript versions
├── logs/
│   ├── log-index.md                 ← running index of all sessions
│   ├── YYYY-MM-DD.md                ← decision log (one per date)
│   ├── YYYY-MM-DD-author-input.md   ← paired author-input record
│   └── YYYY-MM-DD-session-summary.md ← session-start transition summary
├── supplementary/                   ← replication package materials
│   ├── file-structure-template.md   ← this file
│   ├── boolean-search-guide.md      ← search strategy documentation
│   ├── example-skill-reviewer.md    ← reviewer skill template
│   └── example-prompt-templates.md  ← prompt template examples
└── dismissed_ideas/                 ← archived approaches with reasons
```

---

## Key configuration files

### CLAUDE.md

`CLAUDE.md` at the project root is loaded automatically by Claude Code whenever it is opened in that directory. It encodes the project scope, core argument, key conceptual distinctions, writing instructions, and file structure so that every session inherits the same context without requiring re-specification. It is a first-class component of the replication package: a reviewer can assess whether the project context encodes appropriate scope commitments and whether the persistent instructions are epistemically sound.

For empirical projects, `CLAUDE.md` must include explicit data handling rules (see below).

### .claudeignore

`.claudeignore` functions analogously to `.gitignore` for version control, but governs which paths the AI context can access. Paths listed in `.claudeignore` are excluded from the AI's working context even if the files are present on disk. The result is a structural guarantee — not a per-session convention — that excluded paths cannot be read by the AI regardless of how the tool is used in a given session.

Minimum contents for empirical projects:

```
data/raw/
data/interim/
*.env
credentials/
```

For literature-only projects, `.claudeignore` can be omitted or left minimal; there are no sensitive data directories to protect.

### .gitignore

`.gitignore` governs what is committed to version control. It should exclude raw data, large binary files, and locally installed configurations. `.gitignore` and `.claudeignore` serve different functions and overlap only partially: `.gitignore` prevents accidental commits; `.claudeignore` prevents accidental AI context exposure.

---

## Empirical projects: data folder conventions

### Immutability norm

`data/raw/` is immutable. Once data is received or downloaded, it must not be modified — not manually, not by scripts, not by AI. Raw data is a transparency artefact: the replication of any result begins from the declared raw data, and silent modification of that starting point breaks the audit trail.

Encode this as an explicit rule in `CLAUDE.md`:

```markdown
## Data handling rules

- `data/raw/` is read-only. Never use Write or Edit on files in this folder.
- All transformations must go through scripts in `scripts/` and output to `data/interim/` or `data/processed/`.
- `data/raw/` and `data/interim/` are listed in `.claudeignore` and are excluded from AI context.
```

Set file permissions at the operating system level where possible (read-only for the `data/raw/` directory) as a second layer of enforcement.

### Three-zone data model

| Zone | Folder | Identifiers | AI access |
|------|--------|-------------|-----------|
| Raw | `data/raw/` | Present | Blocked (`.claudeignore` + hook) |
| Pseudonymised | `data/interim/` | Removed or replaced | Blocked by default; permitted after manual screening |
| Anonymised | `data/processed/` | Absent | Unrestricted |

Under GDPR, sending personal data to a cloud AI API requires a data processing agreement (DPA) with the provider. The three-zone model supports a stronger position: by keeping raw and pseudonymised data outside AI context through `.claudeignore` and the PII hook (see below), the workflow avoids the DPA requirement for those stages entirely. Only fully anonymised data in `data/processed/` enters AI context, and anonymised data is not personal data under GDPR Article 4.

### Analysis scripts

AI-written analysis scripts should be structured for legibility and verification:

- **Numbered sequentially**: `01_import.R`, `02_clean.R`, `03_anonymise.R`, `04_analyse.R`, `05_tables.R` — execution order is unambiguous
- **Short header per script**: specifies inputs, outputs, and purpose
- **Intermediate outputs**: save to `data/interim/` after each major transformation so the researcher can inspect the data at each stage without re-running the full pipeline
- **Plain-language comments**: explain *why* each step is taken, not just *what* it does; the test is whether a researcher without deep programming expertise can follow the logic
- **Atomic steps**: avoid complex one-liners or deeply nested calls; each named step should do one identifiable thing

The intellectual contribution is the specification: the researcher authors the variable definitions, analytical strategy, inclusion criteria, and edge-case rules. The AI implements the specification. The legibility requirement exists so that the researcher can verify that the implementation is correct.

---

## GDPR and PII safeguards

### PreToolUse hook

Configure a `PreToolUse` hook in `.claude/settings.json` to run a local PII scanner before any file read operation:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Read",
        "hooks": [
          {
            "type": "command",
            "command": "python scripts/pii_screen.py --file \"$CLAUDE_TOOL_INPUT_PATH\" --block-on-pii"
          }
        ]
      }
    ]
  }
}
```

The hook runs before the file content is passed to the AI. If the scanner detects personal identifiers, the operation is blocked before any data reaches the API. This is a structural safeguard, not a session-level convention: it holds regardless of what the AI is asked to do on a given day.

### PII screening tools

- **Microsoft Presidio** (open-source, Python): detects names, emails, phone numbers, national IDs across multiple languages and locales. Configurable for Norwegian identifiers.
- **Custom regex patterns** for Norwegian-specific identifiers: fødselsnummer (11-digit, format DDMMYYXXXXX), D-numbers (first digit incremented by 4), PREG IDs (Medical Birth Registry), Folkeregister IDs.
- Combine both for maximum coverage: Presidio for general patterns, custom regex for Norwegian-specific formats.

### Minimum `pii_screen.py` structure

```python
#!/usr/bin/env python
"""PII screening hook for Claude Code PreToolUse events."""
import sys, argparse, re
from presidio_analyzer import AnalyzerEngine

# Norwegian identifier patterns
NORWEGIAN_PATTERNS = [
    r'\b\d{11}\b',           # fødselsnummer / D-number (11 digits)
    r'\b[4-7]\d{10}\b',      # D-number (first digit 4-7)
]

def screen_file(path: str, block: bool) -> int:
    with open(path, 'r', errors='replace') as f:
        text = f.read()
    
    # Presidio analysis
    analyzer = AnalyzerEngine()
    results = analyzer.analyze(text=text, language='nb')
    
    # Norwegian patterns
    matches = [m for p in NORWEGIAN_PATTERNS for m in re.findall(p, text)]
    
    if results or matches:
        print(f"PII detected in {path}: {len(results)} Presidio hits, {len(matches)} Norwegian ID matches", file=sys.stderr)
        return 1 if block else 0
    return 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', required=True)
    parser.add_argument('--block-on-pii', action='store_true')
    args = parser.parse_args()
    sys.exit(screen_file(args.file, args.block_on_pii))
```

---

## Replication package checklist

The replication package for a systematic AI authorship workflow contains two tiers of materials. Both tiers should be present and clearly labelled.

**Tier 1 — Process integrity (working logs)**

- `logs/` — all daily session decision logs and paired author-input files
- These document the process as it happened, including decisions revised and refined along the way. Analogous to a lab notebook: evidential weight lies in their contemporaneous character.

**Tier 2 — Replicability materials (end-state artefacts)**

- `supplementary/` — final skill files, prompt templates, search scripts, screening logs in the form another researcher would need to adopt or verify the workflow
- Specific required files:
  - Skill files (all versions in use): `skardhamar-style` and reviewer skills
  - `CLAUDE.md` — project-level configuration
  - Main user-level `CLAUDE.md` — system-level epistemological commitments
  - `scripts/search_openalex.R` and `scripts/download_pdfs.R` — search and download pipeline
  - `literature/automated_literature_searches/boolean-searches.md` — executed search strings and screening decisions
  - Screening outputs (`fulltext_scores.csv`, `rename_log.csv`)
  - `supplementary/file-structure-template.md` (this file)
  - `supplementary/boolean-search-guide.md`
  - For empirical projects: analysis scripts, codebooks, data management protocol, PII hook configuration

**Note before submission**: Copy installed skill files from their installed location (e.g., `AppData/` on Windows) into `supplementary/` — do not rely on installed copies being stable across machines or versions.
