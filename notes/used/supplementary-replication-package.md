# Note: Supplementary material / replication package contents

The replication package must include the actual files used in producing this paper, not sanitised examples. This is essential for the paper's own argument — claiming that structured AI use produces shareable transparency artefacts and then providing only hypothetical examples would be self-defeating.

## Must include

- **`skardhamar-style` skill** — the actual skill file used for drafting and prose review throughout this paper. This is both a transparency artefact and a demonstration of what a configured writing persona looks like in practice.
- **All reviewer skills used** — social science article reviewer, logic-language reviewer, qualitative theory reviewer (whichever are actually used in producing this paper).
- **`CLAUDE.md` project file** — the actual project instructions file in this folder, including the adversarial/devil's advocate configuration. This is directly relevant to the sycophancy argument (Cheng et al., 2026): the configuration is an instance of structured use countering a known failure mode.
- **Main `CLAUDE.md`** — the user-level Claude Code configuration file, insofar as it contains configurations relevant to research conduct (critical engagement, etc.). This documents the tool configuration at the system level, not just the project level.
- **Search scripts** — `search_openalex.R`, `download_pdfs.R`, `screen_candidates.py` — the actual executed scripts with parameters used.
- **`boolean-searches.md`** — the executed search strings, results counts, and screening decisions.
- **Screening logs** — `fulltext_scores.csv` or equivalent output documenting which papers were retained and on what basis.
- **Prompt templates** — any reusable prompt structures used in drafting, review, or analysis stages.

## Framing in the methods section

The replication package should be described not merely as a compliance requirement but as the natural output of structured use. The point is that these artefacts exist *because* the workflow was structured — they are not assembled post hoc for submission but accumulated during the research process itself. This is the open-science argument: structured use produces replication-ready materials as a byproduct.

Sociological Science's mandatory replication package requirement (since April 2023) is a strong fit: the requirement exists for statistical code and data, but the same logic applies to AI-assisted workflows. The paper can make this explicit.

## Practical reminder

Before submission: collect the current versions of all skill files from their installed locations (AppData path) and copy into `supplementary/`. Do not rely on the installed copies being stable across updates.
