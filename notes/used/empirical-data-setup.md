# Empirical data setup — systematic AI authorship in quantitative and qualitative projects

## Purpose of this note
The paper's workflow demonstration uses a literature-based project. A section or subsection is needed covering how systematic AI authorship applies to empirical research — survey data, register data, qualitative interview material. This note captures the key elements for that section and for the supplementary file-structure template.

---

## Data folder hierarchy

Adopt the Cookiecutter Data Science standard structure:

```
data/
├── raw/          ← immutable. Read-only. Never edited by scripts or manually after receipt.
├── interim/      ← intermediate files after cleaning/anonymisation, before analysis.
├── processed/    ← analysis-ready datasets. Inputs to statistical scripts.
└── external/     ← third-party reference data (SSB, Eurostat, linked registers, etc.)
```

This structure is standard in reproducible data science and maps directly onto the replication package logic: `data/raw/` is the declared data input, `scripts/` transforms it, `data/processed/` is what the analysis consumes. A replication reader can reproduce every step.

---

## Immutable raw data principle

Raw data is a transparency artefact, not a working file. Once received or downloaded, it must not be modified — not manually, not by scripts, not by AI.

**In Claude Code terms:** `data/raw/` is read-only. Claude should only use the `Read` tool on files in `data/raw/`. `Write` and `Edit` are prohibited in that folder. This must be stated explicitly in the project's CLAUDE.md:

```
## Data handling rules
- data/raw/ is read-only. Never use Write or Edit on files in this folder.
- All transformations must go through scripts in scripts/ and output to data/interim/ or data/processed/.
```

**Why this matters for systematic authorship:** If raw data can be silently overwritten during analysis, the audit trail breaks. The immutability norm is the data equivalent of the pre-registration norm: it prevents post-hoc manipulation of the starting conditions.

---

## AI-written scripts — the accessibility principle

AI should write the transformation and analysis scripts (R or Python), but they must be readable and verifiable by a researcher without deep programming expertise. The measure of success is: can the researcher understand what the script does and why, step by step?

**Practical requirements:**
- Scripts numbered sequentially to make execution order explicit:
  `01_import.R`, `02_clean.R`, `03_anonymize.R`, `04_analyse.R`, `05_tables.R`
- Each script has a short header comment specifying: inputs, outputs, purpose, and any key decisions made
- Transformation logic expressed as sequential, named steps — not complex one-liners or nested calls
- Intermediate outputs saved to `data/interim/` after each major step, so the researcher can inspect the data at each stage without re-running the full pipeline
- Comments in plain language explaining *why* each step is taken, not just *what* it does

**Connection to systematic authorship:** The researcher's intellectual contribution is in specifying what the script should do — the inclusion/exclusion criteria, the variable definitions, the analytical strategy. The AI executes the specification. This is query authorship in the empirical register: the criteria, not the code, are the intellectual contribution. But the code must be legible enough for the researcher to verify that their criteria have been correctly implemented.

---

## GDPR and PII — hooks for participant data

For projects involving personal data (survey respondents, interview participants, administrative records with identifiers), raw data must never be sent to a cloud AI API without PII screening.

**Implementation via Claude Code hooks:**
Configure a `PreToolUse` hook in `.claude/settings.json` that runs a local Python script before any file operation:

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

The hook scans the target file for PII patterns and either blocks the read operation or logs a warning. This means Claude cannot accidentally read a file containing identifiable participant data and send it to the API.

**Available tools for PII screening:**
- **Microsoft Presidio** (open-source, Python): recognises names, emails, phone numbers, national IDs across multiple languages and locales. Can be configured for Norwegian identifiers.
- **Custom regex patterns** for Norwegian-specific identifiers: fødselsnummer (11-digit CPR), D-numbers, PREG IDs (from the Medical Birth Registry), Folkeregister IDs
- **ScrubDuck**: simpler CLI tool for basic redaction

**The three-zone data model for participant data:**
- `data/raw/`: original data with identifiers — read-only, never sent to API
- `data/interim/`: pseudonymised or anonymised data — can be used for AI-assisted cleaning and variable construction
- `data/processed/`: fully anonymised analysis-ready data — can be used freely for AI-assisted analysis and reporting

**GDPR compliance note:** Under GDPR, sending personal data to a cloud processor (including an AI API) requires a data processing agreement (DPA) with the provider, and the data must be necessary for the stated purpose. The hook approach supports a stronger position: by preventing raw personal data from leaving the local machine, it avoids the DPA requirement for that data stage entirely. Anonymised data in `data/interim/` and `data/processed/` is no longer personal data under GDPR and can be used without restriction.

---

## Connection to the paper's argument

Each of these practices is a configured, documented safeguard — an instance of systematic AI authorship:
- The immutability rule is a written, enforceable constraint (in CLAUDE.md and file permissions)
- The accessibility principle is a specification that the researcher authors and AI implements
- The PII hook is a configured technical barrier that prevents a class of errors regardless of individual vigilance

The alternative — accepting AI-transformed data without verification, sending raw participant files to the cloud without screening, running undocumented analyses — is unsystematic AI authorship. It may produce excellent results, but it is unaccountable and, in the case of participant data, potentially illegal.

This is where the systematic/unsystematic distinction has consequences that go beyond epistemic quality into legal compliance and research ethics. Systematic AI authorship is not just better science; for certain research types, it is also the legally required approach.

---

## For the paper and supplementary materials

**Paper section:** A subsection under the workflow section (currently §4) covering: data folder hierarchy, immutability norm, accessibility-oriented AI script writing, GDPR hooks. Scope explicitly to quantitative and qualitative empirical projects; note that the paper's own production is literature-based and that this section is anticipatory guidance rather than demonstrated practice.

**Supplementary file-structure template:** Update `supplementary/file-structure-template.md` to include the `data/` hierarchy alongside the existing `literature/`, `notes/`, `draft/`, `scripts/`, `logs/` structure. Add a note on the immutability rule and GDPR hooks.
