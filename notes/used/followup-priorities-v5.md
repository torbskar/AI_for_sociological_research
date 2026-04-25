# Follow-up priorities after v5-draft - manualEdit

**Date:** 2026-04-22  
**Based on:** active notes in `notes/` checked against `v5-draft - manualEdit.md`

---

## Priority 1 — Fix before submission (blocking)

### 1.1 Verify Freese & Peterson attribution (§5.2)
**Source note:** `freese-peterson-attribution.md`

The sentence "Freese and Peterson (2017) identify sociology's engagement with open science norms as incomplete and point to the documentation of qualitative and interpretive decisions as a persistent gap" may over-attribute. The "documentation of qualitative and interpretive decisions" framing may be the author's inference, not their stated diagnosis.

**Action:** Read Freese & Peterson (2017) *Annual Review of Sociology* 43:147–165 and verify. If it is an inference, rephrase to:
> "Freese and Peterson (2017) argue that sociology's engagement with open science norms is incomplete; structured AI use, applied across the research pipeline, produces exactly the kind of decision documentation that their argument implies is missing."

---

### 1.2 Decide on appendix and replication package structure
**Source note:** `replication-package-appendix.md`

Three options documented in detail in the note. Decision still pending:

- **Option A:** GitHub repo as the full replication package (richest; harder to navigate)
- **Option B:** Curated supplement only (accessible; less complete)
- **Option C — Recommended:** GitHub repo as primary package + curated appendix with excerpts for in-paper accessibility

The draft mentions the GitHub URL in footnote [^2] (§4.1) and in §4.1 body, but the appendix structure is unresolved and §4.5 and §6.3 are written as if a supplement exists without specifying its form.

**Proposed appendix contents (from note):** opening pointer to repo; CLAUDE.md excerpt; annotated folder structure; search script excerpt; skill file excerpt; session log + author-input paired example; one NotebookLM query example.

**What to add to the draft once decided:**
- §4.5 or §4.6: one sentence specifying Option C and citing the GitHub repo as the primary replication package
- §6.3: adjust "deposited in a repository" language to specify what the submission actually contains
- §7: the closing sentence "the supplementary materials for this paper serve that function" needs to be more specific

---

## Priority 2 — Strengthen before final draft (non-blocking)

### 2.1 Legal considerations — two points for the paper
**Source note:** `legal-considerations.md`  
**Status:** Requires UiO library confirmation before including

Two insertions identified as relevant to the paper's argument:

1. **§4.2 (literature search) or §6.2 (binary policy problems):** The Scopus metadata export restriction illustrates the same policy bluntness the paper critiques — a blanket restriction that catches legitimate, structured research use. A sentence or two acknowledging that database licence terms have not kept pace with structured academic AI use. Short; can be hedged as "illustrative."

2. **§6.3 (documentation-based alternative):** The EU/EEA statutory TDM exception (EU Copyright Directive Art. 4) and the trend toward explicit TDM clauses in institutional agreements show that the *legal* infrastructure for systematic AI use is already more permissive than most researchers assume — supporting the claim that "no new infrastructure is needed." This can strengthen the conservative framing of §6.3.

**Action needed first:** Confirm with UiO library whether (a) Scopus institutional agreement covers computational metadata analysis, and (b) UiO has formally assessed the Art. 4 TDM exception for this type of workflow. See the five questions in the note.

---

### 2.2 Session metadata / version logging in supplementary
**Source note:** `gemini-Reproducibility in AI Research.md`

The note proposes a pre-flight shell script that logs tool version, model ID, temperature, and git commit to a session metadata file at the start of each session. §5.4 already mentions that "a complete supplementary material package... should include the model version string alongside prompt templates." The note extends this into a concrete implementation: a `log_env.sh` script and a "Version & Environment" section in the supplementary materials.

**Suggested addition:** One brief practical note in §5.4 or the supplementary appendix (once structure is decided per 1.2 above) illustrating what a session metadata record looks like — treating the AI model like "a laboratory reagent or a specific version of Stata/R." Does not require changes to the main argument; fits naturally in the non-determinism discussion or the replication package section.

---

### 2.3 Additional sociological references — selective, not comprehensive
**Source note:** `Sociological Framing for AI Authorship.md`

The note identifies five sociological authors that could deepen the paper's disciplinary grounding. Given Sociological Science's preference for short literature reviews, these should be introduced selectively:

| Author | Connection | Suggested location | Priority |
|--------|-----------|-------------------|----------|
| Latour & Woolgar (*Laboratory Life*) — "inscription devices" / "opening the black box" | Systematic workflow creates inscription artefacts; query authorship as a new inscription device | §3.2 or §5.1 — one sentence | Low–Medium |
| Fourcade & Healy ("Seeing like an Algorithm", 2017) | Un-steered algorithms reproduce ordinal biases; connects adversarial configuration to sociological concern about algorithmic sorting | §3.1 or §4.4 — one sentence | Low |
| Knorr-Cetina (*Epistemic Cultures*, 1999) | Tacit knowledge and "machineries of knowing"; systematic AI authorship as a shift in sociology's epistemic culture | §5.1 — optional supplement to Polanyi/Collins | Low |
| Mario Small (2009) | Logic of selection in qualitative research; justifies formalising screening rubrics as standard sociological practice | §5.2 — supplements Freese & Peterson | Low–Medium |

**Recommendation:** Add at most one or two. Latour/Woolgar is the strongest fit and least likely to inflate the literature discussion, since it could replace rather than add to existing framing. Small could usefully supplement the Freese & Peterson sentence once that attribution is verified (see 1.1). Defer Fourcade/Healy and Knorr-Cetina unless a reviewer requests deeper disciplinary grounding.

---

## Priority 3 — Can be closed or moved to used/

### 3.1 PSantanna reference — already incorporated
**Source note:** `psantanna-workflow-reference.md`

Already in the draft as footnote [^2] in §4.1. Move this note to `notes/used/`.

### 3.2 Abbott and Krippendorff detail notes — argument already in draft
**Source notes:** `notebooklm-Abbott_heuristic.md`, `notebooklm-Krippendorff_coding.md`

Both Abbott (§5.1, substantial paragraph) and Krippendorff (§5.1) are already well-handled in the draft. The notes confirm the claims and add granular detail (Abbott's heuristic types; Krippendorff's "analytical construct" and "computable model" language). The draft treatment is sufficient for the paper's argument. These notes could be drawn on for minor wording improvements in §5.1 if needed — e.g., adding "analytical construct" as Krippendorff's term — but no structural changes are needed.

Move to `notes/used/` after any minor §5.1 polish if desired.

---

## Summary table

| Item | Note file | Location in draft | Blocking? |
|------|-----------|-------------------|-----------|
| Verify Freese & Peterson attribution | `freese-peterson-attribution.md` | §5.2 | Yes |
| Decide replication package structure | `replication-package-appendix.md` | §4.5, §6.3, §7 | Yes |
| Legal considerations (Scopus + TDM) | `legal-considerations.md` | §4.2 or §6.2; §6.3 | No (pending library) |
| Session metadata / version logging | `gemini-Reproducibility in AI Research.md` | §5.4 or appendix | No |
| Sociological references (selective) | `Sociological Framing for AI Authorship.md` | §3.1, §3.2, §5.1, §5.2 | No |
| PSantanna — already done | `psantanna-workflow-reference.md` | — | Move to used/ |
| Abbott/Krippendorff detail — already done | `notebooklm-Abbott_heuristic.md`, `notebooklm-Krippendorff_coding.md` | §5.1 (minor polish only) | Move to used/ |
