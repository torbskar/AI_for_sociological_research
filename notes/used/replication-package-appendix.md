# Note: Replication package, GitHub, and appendix structure

**Source:** Author reflection (2026-04-17)

---

## The replication package question

The paper already exists as a GitHub repository. This creates a genuine choice:

**Option A — GitHub repository as the full replication package.** The repository contains the complete project history: configuration files, search scripts, skill files, prompt templates, session logs, author-input files, draft versions, notes. This is richer than anything a constructed replication package could be. The main considerations are: (i) the repository may contain more than a reviewer or reader needs, and navigating it requires familiarity with the project structure; (ii) the paper claims that transparency artefacts serve the same function as statistical code and data — a GitHub repository with commit history is actually a *stronger* demonstration of this claim than a curated supplement, because it shows the iterative process rather than just the end state.

**Option B — Curated replication package as a separate supplement.** A selected subset of materials — CLAUDE.md, key skill files, example search strings, a sample session log and author-input file — constructed to be self-contained and readable without navigating the full repository. Less overwhelming; lower apparent barrier to adoption; easier for a reviewer to assess. The GitHub repository is then cited as "full project history available at [URL]."

**Option C — Hybrid.** The GitHub repository is the primary replication package (cited as such in the methods section or §6.3). A constructed appendix provides curated excerpts for in-paper accessibility (see below). This is probably the right answer: it satisfies the replication requirement fully, demonstrates the argument through the actual project history, and lowers the access barrier through the excerpts without pretending the excerpts are the package.

**Decision needed:** which option, and how to cite the repository in the paper.

---

## Git and version control — currently missing from the paper

Git is not mentioned anywhere in the draft, but it is integral to systematic AI authorship as actually practised here. Version control is what makes the working logs and file history independently verifiable — anyone can inspect the commit history to confirm that decisions were documented contemporaneously, not retroactively constructed. The `.gitignore` file already appears in the folder structure diagram (§4.1), but only as a label with no explanation.

**What should be added:**
- A sentence or two in §4.1 or §4.6 explaining that the project folder is a git repository and why this matters: commit timestamps make the contemporaneous character of logs independently verifiable; version history shows when configurations, skill files, and search strings were created relative to when analyses were run.
- `.gitignore` in the folder structure explanation should be given its own brief gloss alongside `.claudeignore` — they are analogous instruments but serve different purposes (version control exclusions vs AI context exclusions).
- The file structure template in `supplementary/file-structure-template.md` should note that the project folder is initialised as a git repository, and that `data/raw/` and credential files appear in both `.gitignore` and `.claudeignore`.

---

## Appendix structure

A traditional appendix — included in the submission, accessible without following a URL — serves a different purpose from the replication package. Its function is reader-facing: it makes the workflow concrete and the barrier to adoption feel manageable, not archival.

**Proposed structure:**

1. **Opening pointer.** One paragraph stating that the complete project — all configuration files, scripts, skill definitions, session logs, and version history — is available at [GitHub URL], and that the appendix provides selected excerpts to illustrate the key components.

2. **CLAUDE.md excerpt.** The project-level CLAUDE.md is the most important single file. An excerpt (or lightly trimmed full version) shows how the research question, key conceptual distinctions, and scope decisions are encoded as persistent context. This is the clearest demonstration of query authorship at the project level.

3. **Folder structure.** The annotated folder tree from §4.1 or the supplementary template, reproduced or cross-referenced, showing how the project is organised and how `.claudeignore` and `.gitignore` interact.

4. **Search script excerpt.** A few lines of the boolean search string or the OpenAlex API call, with the inclusion/exclusion criteria visible, showing what "explicit criteria before running" looks like in practice.

5. **Skill file excerpt.** A representative passage from the logic-language reviewer skill or the skardhamar-style skill, showing how a reviewer configuration encodes explicit evaluative standards. This is the most direct illustration of query authorship at the task level.

6. **Session log and author-input excerpt.** A paired example — one log entry and the corresponding author-input entry — showing the division of labour between what was decided and who originated what. This is the most directly relevant demonstration for the authorship criteria argument in §5.5.

7. **NotebookLM query example.** One grounded synthesis query with the formulation shown, illustrating how source-grounded queries differ from open-ended chatbot prompts. Short — the point is the query formulation, not the response.

**What to leave out:** Full skill files, complete CLAUDE.md, all search strings, full session logs. The appendix should illustrate, not reproduce. The reader who wants the full material has the GitHub repository.

---

## The balance problem

The core tension: the paper argues that the barrier to systematic AI authorship is low (no new infrastructure, extends existing open-science norms). An appendix that looks overwhelming contradicts this. An appendix that looks too thin doesn't demonstrate the claim.

The resolution is framing: the appendix should be introduced as "here is what this looks like in practice" rather than "here is what you must produce." Excerpts rather than full files; annotations that explain what each component does rather than leaving the reader to infer. The GitHub repository handles the "completeness" requirement; the appendix handles the "low barrier" claim.

---

## Defer to

Later edit pass. Decisions needed before drafting the appendix:
1. Option A / B / C for the replication package.
2. Whether §4.1 or §4.6 is the right location for the git/version-control addition to the draft.
3. Which skill excerpt best illustrates query authorship without requiring the reader to understand the full skill framework.
