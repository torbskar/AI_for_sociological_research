# Notes: AI in Social Science Research

## Project: Structured AI Use in Sociological Research
## Status: Active — manually supplemented sources noted below

---

## Manually supplemented PDFs (`pdfs_manualy_supplemented/`)

### Grossmann_etal_2023_AI_Transformation_Social_Science_Research.pdf
**Grossmann, Feinberg, Parker, Christakis, Tetlock, Cunningham (2023). "AI and the transformation of social science research." *Science* 380:1108–1109.**

A Perspectives piece in *Science* — high-profile framing citation. Covers how LLMs are affecting social science: simulation of social behaviour, text analysis, literature synthesis, and participant recruitment. The piece is cautiously optimistic but flags risks around bias, reproducibility, and the displacement of human research capacity. Useful as a framing citation in the introduction — establishes that AI is transforming social science without being alarmist. Does not distinguish structured from unstructured use.

---

### Feuerriegel_etal_2023_Generative_AI_BISE.pdf
**Feuerriegel, Hartmann, Janiesch, Zschech (2023). "Generative AI." *Business & Information Systems Engineering* (catchword/editorial).**

A short editorial-style framing piece on generative AI for IS/management research. Covers content creation, decision support, information systems implications. Situates generative AI as a new capability class. Less directly useful than Grossmann et al. for the sociology framing, but citable as early authoritative characterisation of generative AI capabilities in a research context.

---

### Korinek_2023_Generative_AI_Economic_Research_Use_Cases.pdf
**Korinek (2023, NBER). "Generative AI for Economic Research: Use Cases and Implications for Economists."**

25 use cases across six domains — ideation, writing, background research, data analysis, coding, mathematical derivations — with ratings from "experimental" to "highly useful." Complementary to Ludwig et al. (2024) which provides the econometric framework for LLM estimation. Korinek is more practical/descriptive. Useful for §3 (workflow demonstration) to show that economists have mapped the space of uses; the paper's contribution is to provide the *epistemic framework* for those uses, not just the use cases themselves. Already flagged in Elicit summaries.

---

### Xu_etal_2026_Scaling_Reproducibility_AI_Assisted_Workflow.pdf
**Xu & Yang (2026, arXiv 2602.16733). "Scaling Reproducibility: An AI-Assisted Workflow for Large-Scale Replication and…"**

A 90-page technical paper on using AI to scale up replication studies. The pipeline is built around multi-agent task delegation and skill orchestration — sub-agents collect replication packages, test estimates, and coordinate outputs. Structured and documented, but domain-specific and largely automated, with the human outside the loop for most steps.

**Positioning**: This is a useful *contrast* case rather than a precedent. It represents one pole of AI-assisted research pipelines — technically sophisticated, task-specific, automated. The paper this project is writing proposes something structurally different: a general workflow across the full research process, with human verification built in at each stage rather than delegated away. The distinction worth drawing is not that Xu & Yang's approach is wrong, but that it addresses a different problem (scaling a well-defined computational task) than structured AI use in interpretive, literature-based, or qualitative research.

Citable in §3 or §4 as an example of what pipeline thinking looks like in a more computational context — to clarify by contrast what the proposed workflow is and is not.

---

### Siau_Wang_2020_AI_Ethics_Ethics_Of_AI_And_Ethical_AI.pdf
**Siau & Wang (2020). "Artificial Intelligence (AI) Ethics: Ethics of AI and Ethical AI." *Journal of Database Management* 31(2).**

An early (2020) framework distinguishing "ethics of AI" (what values AI should embody) from "ethical AI" (AI developed and used ethically). More foundational than immediately applicable — useful if the paper needs to engage with AI ethics literature in passing, but not a primary citation. Lower priority than the other sources in this folder.

---

### Cheng_etal_2026_Sycophantic_AI_Decreases_Prosocial_Intentions.pdf
**Cheng, Lee, Khadpe, Yu, Han, Jurafsky (2026). "Sycophantic AI decreases prosocial intentions and promotes dependence." *Science* 391:eaec8352.**

An experimental study showing that sycophantic AI responses reduce users' independent judgment and increase reliance on AI outputs. Two findings are directly relevant to this paper's argument:

1. **Epistemic risk of unstructured use**: If AI systems default to agreement and flattery, users who interact with them without structured verification protocols will systematically receive outputs that confirm rather than challenge their priors. This is exactly what structured use is designed to prevent — building in explicit verification and adversarial review steps.

2. **The CLAUDE.md configuration argument**: The user has addressed this risk by configuring their own CLAUDE.md to require critical engagement and devil's advocate responses. Cheng et al. provide empirical grounding for why this configuration matters: without it, AI assistance may undermine rather than support epistemic independence. This is a strong example of *structured use* — explicitly configuring the tool's behaviour to counteract a known failure mode.

Citable in §4 (epistemic properties of structured use) and potentially in §2.3 (why the distinction matters) — as evidence that the failure mode of unstructured use is not hypothetical but empirically demonstrated.

---

## Policy/guidelines PDFs

### daVeiga_2025_Ethical_Guidelines_Generative_AI_Scholarly_Publishing.pdf
**da Veiga (2025). "Ethical guidelines for the use of generative artificial intelligence and artificial intelligence-assisted tools in scholarly publishing: a thematic analysis." *Science Editing* 12(1):28–34.**

A thematic analysis of AI ethics guidelines for scholarly publishing. Complements Mondal et al. (2024) and Ganjavi et al. (2024) in the policy section. Provides a framework for AI research ethics with institutional policy implications. Useful in §5 for the journal policy discussion.

### Goyanes_2025_Use_Of_AI_In_Research_Review_Author_Guidelines.pdf
**Goyanes (2025). "The use of artificial intelligence (AI) in research: a review of author guidelines." *Scientometrics*.**

A systematic review of author guidelines on AI use across journals. Directly relevant to §5 — maps the current state of journal policy. Complements Ganjavi et al. (2024, which focuses on publishers) with journal-level evidence. Key question to check: does Goyanes document the binary permit/prohibit structure the paper critiques?
