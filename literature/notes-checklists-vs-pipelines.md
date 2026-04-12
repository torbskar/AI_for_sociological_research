# Notes: Checklists vs. pipelines in the AI-in-research literature

**Source**: Elicit.com searches, April 2026. Summaries in `literature/Elicit_export/`.

---

## The structural gap this paper exploits

The existing literature divides into two types:

1. **Reporting checklists** — post-hoc disclosure instruments organised by manuscript section. These tell authors *what to report* after the research is done. Numerous examples: PRISMA-trAIce, TRIPOD-LLM, MI-CLAIM-GEN, TITAN, CONSORT-AI, CLAIM, SPIRIT-AI. A systematic review of 24 such checklists (Zrubka et al., 2025) found item counts ranging from 10 to 66 — indicating no consensus on what "full disclosure" even means.

2. **Practical pipelines** — step-by-step workflow frameworks integrated into the research process itself. Far rarer. The Elicit searches found only a handful: Blanchard et al. (2025) for social science surveys/experiments, Frutuoso (2025) for clinical trials, Sušnjak (2025) for evidence synthesis, DataDreamer (Patel et al., 2024) for reproducible LLM workflows.

**The implication for this paper**: The checklist literature addresses *accountability after the fact*. This paper addresses *epistemic structure during the research process*. These are different problems. Most guidance is of the first type; the second type is almost entirely missing from sociology and adjacent social sciences. This is the gap.

---

## Why checklists are insufficient (and why the paper's framing is better)

Checklists assume the hard part is disclosure. But if AI use is unstructured — accepting outputs without systematic verification — then there is nothing epistemically sound to disclose. You can complete every item on PRISMA-trAIce while having done the underlying work badly.

The structured/unstructured distinction is more fundamental: it asks whether the research process itself embeds quality controls, not merely whether those controls are reported. Pre-registration is the analogy — it's not that registered studies are better because they disclose more, but because they force explicit commitment to decisions before outcomes are known.

---

## Empirical evidence supporting the epistemic argument

Three findings are directly usable in the paper:

**Zeng et al. (2025, EMNLP) — AIRepr**: Evaluated whether LLM-generated data analysis workflows were sufficiently documented to be reproduced. Tested 15 LLM pairs across 1,032 tasks. Finding: "higher reproducibility strongly correlates with improved accuracy." Structured prompting designed for reproducibility also produces better results — not just more transparent ones. This is the key empirical hook: structure is not just a disclosure mechanism, it improves the underlying epistemic quality of the work.

**Barrie, Spirling, Benoit et al. (political science)**: Rolling iterated replication design comparing crowdsourcing and LLMs across many months. Finding: LLMs can be accurate, but "the observed variance in performance is often unacceptably high" — and strict temperature control does not resolve it. Many LLM-based findings could not even be re-run, let alone replicated. Recommendation: use locally versioned open-source models for maximum replicability.

**Ludwig, Mullainathan & Rambachan (2024, NBER)**: For economic estimation problems using LLMs, "seemingly innocuous choices (which model, which prompt) can produce dramatically different parameter estimates." Without a human-coded validation sample, LLM outputs cannot be trusted for downstream analysis. The implication: unstructured use (pick a model, run a prompt, trust the output) produces unreliable inference even when the researcher is technically competent.

---

## Most relevant pipeline works for citation

**Social science:**
- Blanchard et al. (2025, *Journal of Marketing*): "New Tools, New Rules." Full research pipeline from literature review through instrument design, data collection, coding, and interpretation. Comes with reproducible R/SPSS templates and sample preregistrations at questionableresearch.ai. Most practical social science guide found.
- Törnberg (2024): "Best Practices for Text Annotation with LLMs." Covers model selection, prompt engineering, prompt stability analysis, and validation against human coders. Highly cited.
- Davidson & Karell (2025, *Sociological Methods & Research*): Special issue on integrating generative AI into social science research — measurement, prompting, simulation. Closest disciplinary home for this paper's argument.
- Lin (2025): Six-stage validity-guided workflow for psychology LLM research. Scales validity requirements to research ambition.

**Workflow/reproducibility tools:**
- DataDreamer (Patel et al., 2024, ACL): Python library for reproducible LLM workflows. Standardises logging of model versions, prompts, parameters, outputs.
- Sušnjak (2025): "Compiling prompts, not crafting them." Declarative task specifications + automated prompt optimisation for evidence synthesis. Version-controlled and verifiable pipelines.
- R-LAM (SureshKumar, 2026): Reproducibility-constrained framework for scientific workflow automation — structured action schemas, deterministic execution, provenance tracking.

**Checklists for citation (to show what exists and why it's insufficient):**
- PRISMA-trAIce (Holst et al., 2025, *JMIR AI*): Systematic reviews. 14 items, mandatory/recommended levels. Most formalized checklist for a specific workflow type.
- TITAN (Agha et al., 2025): General-purpose, covers declaration, purpose, configuration, data inputs, human oversight.
- Mondal et al. (2024): Cross-sectional audit of 20 major publishers' AI guidelines. Six recurring themes.

---

## What is NOT in the literature (= the paper's space)

- No sociology-specific workflow framework (Davidson & Karell is closest but is an SMR special issue framing, not a workflow guide)
- No framework distinguishing structured from unstructured use as the fundamental axis
- No treatment of AI tool configuration (skills, reviewer roles) as an epistemic mechanism analogous to pre-registration
- No discussion of transparency artefacts (prompt templates, skill files, search logs) as components of a replication package
- The checklist literature implicitly assumes use is already structured — it does not address the prior question of whether the research process embeds quality controls at all

---

## Note on the search

The Elicit search confirms the user's observation: the field has checklists in abundance and pipelines almost nowhere. The most actionable pipeline works are in clinical research (Frutuoso) and ML/NLP (DataDreamer, AIRepr, R-LAM) — social science equivalents are partial at best (Blanchard et al. is the closest). This strengthens the paper's claim to a genuine contribution.
