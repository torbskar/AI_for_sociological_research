# Outline: Structured AI Use in Sociological Research

**Status**: Working outline — not yet drafted  
**Last updated**: 2026-04-10  
**Target**: Sociological Science — methodological contribution

---

## Core argument (one sentence)

The epistemically relevant distinction is not between AI use and non-use but between *structured* and *unstructured* use, and a documentation-based framework that recognises this distinction is both more honest and more productive than current journal policy.

---

## Note on durability

The argument must be tool-agnostic throughout. The structured/unstructured distinction and the query authorship concept are durable; specific tool names (Claude, NotebookLM, ChatGPT) are illustrative and will date. This is both a rhetorical and a substantive point: the paper argues for a principle, not a platform.

---

## 1. Introduction

**Function**: Establish the problem; state the paper's move; no long literature review.

- The adoption of LLMs in academic research is rapid and uneven. Sociologists are using these tools; the question is not whether but how.
- Two responses have dominated: blanket restriction (many journals) and blanket permission with disclosure (publishers). Both treat AI use as a binary.
- The binary is wrong. What matters epistemically is not whether AI was used but whether its use was structured — embedded in explicit criteria, human verification at each stage, documented outputs.
- This paper: (1) develops the structured/unstructured distinction conceptually; (2) introduces the concept of *query authorship* — the intellectual contribution embedded in well-formed queries and tool configurations; (3) demonstrates a structured workflow for sociology across the full research pipeline; (4) argues that structured use has the epistemic properties of open-science practices; (5) draws implications for journal policy.
- Frame: methodological contribution. The paper demonstrates something and argues for its properties — it is not a think-piece.

**Scope limitation** (stated here, not batched): The workflow demonstrated is for text-heavy, literature-based, and qualitative/mixed social science research. Quantitative primary data collection stages are not addressed in detail. The argument is scoped to sociology and adjacent social sciences.

---

## 2. AI in research: the existing literature and the gap

**Function**: Brief literature grounding — not a survey. Maps what exists, names the gap, and positions the paper's contribution. Keep short; Sociological Science discourages long literature reviews.

**Methodological note for the outline**: This section's literature was identified using the structured pipeline described in §4 — OpenAlex API search across seven boolean strings, keyword-based abstract screening, full-text relevance scoring, and NotebookLM-assisted theme synthesis. The executed search strings, screening decisions, and full-text scores are documented in the replication package (`boolean-searches.md`, `filter_decisions.json`, `fulltext_scores.csv`). This means the literature review is itself an instance of the practice the paper defends: structured, documented, reproducible. That double function — substantive and demonstrative — should be made explicit in a brief methodological note at the end of this section or at the start of §4.

### 2.1 What the existing literature covers

- Rapid AI adoption in research is well-documented and cross-disciplinary — Grossmann et al. (2023, *Science*), Korinek (2023, NBER), Feuerriegel et al. (2023): social science, economics, information systems all engaged early. The question is no longer whether but how.
- The dominant institutional response has been **reporting checklists**: post-hoc disclosure instruments telling authors what to report after the research is done. Numerous variants — PRISMA-trAIce (Holst et al., 2025, systematic reviews), TITAN (Agha et al., 2025, general purpose), TRIPOD-LLM, CONSORT-AI, MI-CLAIM-GEN, and others. Zrubka et al. (2025) systematically reviewed 24 such checklists: item counts range from 10 to 66, indicating no consensus even on what "full disclosure" means.
- Publisher and journal guidance follows the same logic: Mondal et al. (2024) audited 20 major publishers; Ganjavi et al. (2024) and Goyanes (2025) map journal-level author guidelines. Six themes recur across all audits — all centred on disclosure and attribution, none on the epistemic structure of the process.
- **Social science pipeline work** exists but is partial: Törnberg (2024) on text annotation best practices and prompt stability; Davidson & Karell (2025, *SMR*) on integrating generative AI into social science research (measurement, prompting, simulation); Blanchard et al. (2025, *Journal of Marketing*) — the most complete pipeline found, with reproducible templates and pre-registration materials. Lin (2025) for psychology; DataDreamer (Patel et al., 2024) and Zeng et al. (2025, AIRepr) from NLP/data science.

### 2.2 The gap

- The checklist literature addresses accountability after the fact. It implicitly assumes the research process is already sound — it has nothing to say about whether it was. A researcher could complete every item on PRISMA-trAIce while having used AI in a wholly unstructured, unverifiable way.
- No existing framework treats the **structured/unstructured distinction** as the fundamental policy-relevant axis.
- No sociology-specific workflow framework exists. Davidson & Karell (2025) is the closest — but it is a special-issue framing piece, not a workflow guide. Blanchard et al. is the most practical pipeline, but in marketing.
- No existing work treats AI tool configuration (skill files, configured reviewer roles, system-level prompts) as an epistemic mechanism comparable to pre-registration or researcher-degrees-of-freedom disclosure.
- No existing work discusses transparency artefacts (prompt templates, search logs, skill configurations) as components of a replication package.
- **Summary**: The field has checklists in abundance and structured process thinking almost nowhere. The most actionable pipeline works are in clinical research and ML/NLP. Social science equivalents are partial. Sociology-specific work is absent.

---

## 3. The structured/unstructured distinction

**Function**: The paper's conceptual contribution. Must be crisp — not a literature review.

### 3.1 What unstructured AI use looks like

- Prompting without explicit criteria; accepting outputs without systematic verification; no documentation of process
- The problem is not that AI is unreliable but that without explicit criteria, errors are invisible and unrepeatable
- Ludwig, Mullainathan & Rambachan (2024): "seemingly innocuous choices (which model, which prompt) can produce dramatically different parameter estimates" — unstructured use makes this variance invisible
- Barrie et al.: "the observed variance in performance is often unacceptably high" even with temperature control — without logging, you cannot know whether your results would survive re-running
- Cheng et al. (2026, *Science*): sycophantic AI responses reduce independent judgment and promote dependence — unstructured use exposes researchers to systematic confirmation bias, not just random error. The failure mode is directional: AI outputs tend to confirm rather than challenge user priors. [First appearance — framing the problem; returns in §4.5]

### 3.2 What structured AI use looks like

- Tool configurations with explicit criteria built in (reviewer skills with discipline-specific standards)
- Human verification checkpoints at each stage — verification is part of the protocol, not an afterthought
- Documented outputs: prompt templates, skill configurations, search logs, screening decisions
- *Query authorship*: formulating a search string, screening rubric, or review prompt is an intellectual act — it encodes theoretical choices, scope commitments, and evaluation standards. These choices belong to the researcher, not the AI. Structured use makes them explicit and verifiable; unstructured use leaves them tacit and unauditable. [First appearance — see §5.1 for full development]
- Analogy to pre-registration: structured use forces explicit articulation of tacit decisions *before* results are known — which search terms? which inclusion criteria? which coding rules?

### 3.3 Why the distinction matters

- Epistemically: structured use makes errors visible and correctable; unstructured use does not
- Zeng et al. (2025, AIRepr): structured prompting designed for reproducibility *also produces better results* — not just more transparent ones. This is not a trade-off. [Note: this finding comes from data science tasks; the claim for sociology is suggestive, not demonstrated — hedge accordingly in §5.3]
- The existing literature has converged on reporting checklists (PRISMA-trAIce, TITAN, TRIPOD-LLM, etc.) — instruments for disclosing AI use after the fact. These assume the underlying process was sound. Structured use addresses the prior question: building soundness in. [Concessive: checklists are valuable; they are just insufficient.]
- The structured/unstructured axis is orthogonal to the use/non-use axis. A paper using AI in a structured way may be more epistemically sound than one not using AI at all but relying on undocumented, unverifiable manual judgements.
- The query authorship concept travels beyond the immediate AI context: it connects to existing debates about transparency in qualitative research (what counts as a decision? who made it?) and to the open-science argument for researcher degrees of freedom disclosure.

---

## 4. A structured workflow for sociology

**Function**: The demonstration. Shows what structured use looks like in practice across the full research pipeline. Descriptive — this is how it works, not why it is better (that comes in section 4).

### 4.1 Overview of the workflow

- Seven stages: literature search → candidate screening → full-text screening → source organisation → drafting → review → documentation
- At each stage: explicit input criteria, configured AI tool, human verification checkpoint, documented output
- Transparency artefacts produced at each stage: boolean search strings, screening rubrics, skill configurations, prompt templates, search logs, NotebookLM source sets, review records
- [Scope note here, briefly]: This is not an automated pipeline that delegates decisions to agents. Xu & Yang (2026) demonstrate that type — effective for scaling well-defined computational tasks. The workflow here keeps the researcher in the loop at every stage; AI handles execution within explicitly defined criteria, the researcher handles judgement. The distinction matters for sociology, where research questions, theoretical framings, and interpretive moves cannot be delegated.

### 4.2 Literature search and screening

**Double function**: This subsection describes the search process that produced the literature reviewed in §2. The section heading and content are descriptive (this is what was done); §2 carries the substantive findings. Making this connection explicit is itself part of the argument: the literature review was conducted via the documented pipeline, making it reproducible and auditable in exactly the way the paper advocates.

- Boolean search strategy with explicit inclusion/exclusion criteria documented in advance (analogous to systematic review protocol) — seven search strings across OpenAlex, supplemented by Elicit.com targeted searches
- OpenAlex API search via R script — reproducible, logged, shareable. OpenAlex chosen over licensed databases (Scopus, Web of Science) partly on legal grounds: database terms for bulk export vary by institutional agreement and may not cover computational analysis, while OpenAlex's open API has explicit research-use permission. [Brief point — signals awareness; legal detail not needed in the paper itself]
- Candidate screening via configured keyword-based screening rubric (explicit criteria, not impressionistic relevance judgement)
- Full-text relevance scoring across three themes — algorithmic, auditable
- Source synthesis via NotebookLM: top-scored PDFs uploaded to themed notebooks; queries documented and responses grounded in uploaded sources — contrast with asking a general-purpose chatbot (unverifiable, no source accountability)
- Outputs (all in replication package): `automated_literature_searches/boolean-searches.md`, `search_openalex.R`, `screen_candidates.py`, `automated_literature_searches/fulltext_scores.csv`, NotebookLM query logs

### 4.3 Drafting

- Skill-configured AI persona (skardhamar-style) with explicit style criteria — forces articulation of what the target voice is, not just "make it sound like me"
- Drafts are inputs to human revision, not outputs for direct use
- All prompts and skill configurations retained as artefacts

### 4.4 Review and adversarial configuration

- Discipline-specific reviewer skills (social science article reviewer, logic-language reviewer, qualitative theory reviewer)
- Each skill has explicit review criteria built in — not "does this seem good?" but "does this meet these specific standards?"
- Structured review produces legible, actionable feedback — not a vague sense of quality
- Tool configuration can counteract known failure modes: explicitly instructing the AI to be critical, raise objections, and play devil's advocate addresses the sycophancy problem identified by Cheng et al. (2026). The user-level configuration used in this project documents epistemological commitments (severity testing, falsifiability, researcher degrees of freedom) — making them explicit rather than tacit, and encoding them as a permanent constraint on the tool's review behaviour. [Second appearance of Cheng et al. — shows that structured use means configuring against failure modes; first appearance in §3.1 framing unstructured use]
- This is a concrete example of the structured/unstructured distinction: the same tool, identically prompted for content, produces epistemically different outputs depending on whether its review behaviour has been explicitly configured

### 4.5 Documentation and replication package

- All transparency artefacts compiled as supplementary material
- Sociological Science's mandatory replication package requirement: prompt templates, skill files, R scripts, search logs serve as the replication package — strong fit. The supplementary materials for a non-empirical methods paper are themselves a demonstration of the argument: structured use produces replication-ready materials as a natural byproduct. This is not additional overhead.
- **Two-tier documentation structure**: Working logs (daily session logs + author-input files) and final supplementary materials serve distinct functions. The logs document the process as it happened — iterative, with decisions revised and refined — and carry the evidentiary weight for process integrity, analogous to a lab notebook. The supplement presents the end-state artefacts in reusable, accessible form: what another researcher would need to adopt or verify the workflow. Both are present in the replication package; the paper should be explicit that they serve different purposes. [This mirrors how pre-registration works: the registered plan and the final methods section are both legitimate and neither substitutes for the other]
- **Author-input logs and authorship transparency**: The author-input files document what the author brought to each session — ideas, framings, redirections, pushbacks — in first-person prose. These serve a function analogous to authorship declarations in co-authored work: they document the human intellectual origin of the work and the human-AI division of labour. For this paper specifically, demonstrating this practice is the point. More generally, structured AI use with author-input logging enables transparent CRediT-style declarations of what was done by whom.

---

## 5. Epistemic properties of structured use

**Function**: The normative argument. Why structured use is epistemically preferable. Short, pointed, grounded in existing open-science literature.

### 5.1 The pre-registration analogy and query authorship

- Pre-registration does not improve research by restricting it — it improves research by forcing explicit commitment to decisions before outcomes are known
- Structured AI use does the same: explicit criteria must be articulated before the AI is run, not constructed post hoc to justify what the AI returned
- **Query authorship** is the conceptual heart of this: formulating a search string, a screening rubric, or a reviewer prompt is an intellectual act that encodes the researcher's theoretical choices, scope commitments, and evaluative standards. The AI executes; the researcher authors. Making these choices explicit — in the query, the configuration, the documented protocol — externalises tacit knowledge in exactly the way pre-registration externalises research design choices. Unstructured use leaves this authorship invisible, creating a false impression that outputs emerged from the AI rather than from the researcher's intellectual commitments working through the AI.
- Literature on epistemic value of making reasoning explicit (notes-explicit-reasoning.md): tacit knowledge problem; externalisable criteria are verifiable criteria
- The query authorship framing has implications for attribution and academic integrity beyond the AI context: it clarifies that the relevant intellectual contribution in AI-assisted research is the quality of the query, not the novelty of the output text.

### 5.2 Structured use as open science practice

- Transparency artefacts are shareable, versionable, and independently evaluable
- The Momeni et al. (2025) checklists for computational reproducibility in social science — developed with 180+ social scientists — cover data documentation, source sharing, methodological reporting; structured AI use satisfies these naturally
- Törnberg (2024) on prompt stability analysis: testing whether minor prompt changes alter results is only possible if prompts are documented — structured use makes this possible by default

### 5.3 The reliability finding — and its limits

- Zeng et al. (2025): reproducibility correlates with accuracy across 1,032 tasks — the discipline of structured prompting improves outputs, not just transparency. This is suggestive: structured use is not merely a transparency requirement but a mechanism for quality.
- **Scope limitation (stated here)**: The Zeng et al. finding comes from data science tasks; the paper cannot claim to have demonstrated the same for sociology research. The claim is that the logic is plausible and the adjacent evidence is consistent with it. This should be framed as "I suggest" rather than "I argue" — a hypothesis for future empirical validation, analogous to how Zeng et al. (2025) tested this formally in their domain.
- What this section can claim without overreach: structured use is a necessary condition for the kind of quality control that makes errors detectable; whether it also improves average output quality in sociology is an open empirical question.

### 5.4 What structured use cannot guarantee

- Structured use does not eliminate LLM error; it makes errors visible and correctable
- Non-determinism remains a challenge — same prompt, different output across runs. Mitigation: log outputs alongside prompts; treat AI output as input to human judgement, not as final product
- Structured use is a necessary condition for epistemic soundness, not a sufficient one

---

## 6. Implications for journal policy

**Function**: Application of the argument. Critical but concessive. Not the main event — an implication.

### 6.1 What current policies do

- [Concessive]: Journals responded rapidly and in good faith to genuine concerns about AI-generated content and undisclosed use
- Cross-sectional audit (Mondal et al., 2024) of 20 major publishers: six converging themes. The field has moved from silence to active guidance. Goyanes (2025) and da Veiga (2025) extend this picture to the journal level.
- But the guidance is binary: permit or prohibit. No policy distinguishes structured from unstructured use.
- Ganjavi et al. (2024): publishers' instructions focus on disclosure of AI use, not on the epistemic quality of that use

### 6.2 The problem with binary policies

- Blanket restriction penalises structured use — the researcher who built a documented, reproducible screening protocol is treated the same as one who asked ChatGPT to summarise their references
- Blanket permission with disclosure does not incentivise structured use — disclosure of "I used GPT-4 to assist with analysis" gives readers no information about whether the use was epistemically sound
- Both responses leave the structured/unstructured distinction invisible
- [Tone note throughout §5]: The critique must stay constructive — the target is the framework, not the good faith of editors or publishers. The goal is to propose a better instrument, not to impugn the existing ones.

### 6.3 A documentation-based alternative

- The relevant policy question is not "did you use AI?" but "can you show what you did?"
- **The conservative framing**: Extending existing replication package norms to AI-assisted workflows requires no new principle and no new infrastructure — only an expanded understanding of what "the materials needed to reproduce the analysis" includes. For a study using regression, that means code and data. For a study using a structured AI workflow, that means skill files, prompt templates, search scripts, and screening logs. Journals that already require replication packages for quantitative work (Sociological Science since April 2023) have accepted the underlying logic; they have no principled basis for treating AI workflow documentation differently. This makes the policy recommendation conservative rather than radical.
- Jones (2025, qualitative) and Davidson & Karell (2025, SMR) move in this direction — disclosure frameworks that specify *what* was done, not just *whether*
- This shifts the evaluative burden to peer review, where it belongs: reviewers can assess whether the structured process was appropriate, not just whether AI was used

---

## 7. Conclusion

- The structured/unstructured distinction changes the policy question
- The query authorship concept clarifies what the human contribution in AI-assisted research actually is — not the text, but the intellectual commitments encoded in the query. This is citable, auditable, and open-science compatible.
- Sociologists have the methodological vocabulary to engage with this — rigour, validity, transparency, replication are existing standards; structured AI use extends them into a new domain
- The transparency artefacts produced by structured use are already a recognised open-science format; journal infrastructure exists to accommodate them
- Open question for future work: formal validation studies comparing structured vs. unstructured AI use in sociology research tasks (analogous to Zeng et al. in data science)

---

## Supplementary materials (replication package)

Sociological Science requires a replication package as a condition of publication (mandatory since April 2023), normally understood as statistical code and data. For this paper, the transparency artefacts of the structured workflow serve the equivalent function — and the paper should say so explicitly in the methods section. This is not a workaround but a demonstration of the argument: structured use produces replication-ready materials as a natural byproduct.

**Two-tier structure**: The package contains both working logs (process integrity evidence) and final artefacts (replicability evidence). These serve distinct functions and should be clearly labelled as such in the package documentation.

The package must include the actual files used, not illustrative examples:

- **Skill files** (actual versions in use): `skardhamar-style`, all reviewer skills used during drafting and review
- **`CLAUDE.md`** — project-level configuration including adversarial/critical engagement instructions
- **Main user-level `CLAUDE.md`** — system-level tool configuration including epistemological commitments (relevant to the query authorship and sycophancy arguments)
- **`scripts/search_openalex.R`, `scripts/download_pdfs.R`, `scripts/screen_candidates.py`** — executed search and screening pipeline with parameters used
- **`literature/automated_literature_searches/boolean-searches.md`** — executed search strings, result counts, screening decisions
- **Screening outputs** — `literature/automated_literature_searches/fulltext_scores.csv` and `filter_tidying/rename_log.csv`, documenting inclusion/exclusion basis
- **`logs/`** — daily session logs and author-input files (process integrity record)
- **`supplementary/file-structure-template.md`** — project structure for reuse
- **`supplementary/boolean-search-guide.md`** — search strategy documentation

**Note before submission**: Copy installed skill files from AppData into `supplementary/` — do not rely on installed copies being stable.

---

## Key literature (to be cited; keep in-text citations minimal)

**The gap — checklists vs. pipelines:**
- Mondal et al. (2024) — publisher guidelines audit
- Zrubka et al. (2025) — systematic review of 24 AI reporting guidelines (10–66 items)
- Holst et al. / PRISMA-trAIce (2025) — most formalized checklist, systematic reviews only
- Goyanes (2025) — journal-level author guidelines survey [check: does it document binary permit/prohibit structure?]
- da Veiga (2025) — thematic analysis of AI ethics guidelines for scholarly publishing

**Epistemic cost of unstructured use:**
- Ludwig, Mullainathan & Rambachan (2024) — prompt choice affects parameter estimates
- Barrie et al. — LLM variance "unacceptably high" without versioning
- Zeng et al. (2025, AIRepr) — reproducibility correlates with accuracy [from data science; generalise cautiously]
- Cheng et al. (2026, *Science*) — sycophantic AI reduces independent judgment; empirical grounding for adversarial configuration

**Closest disciplinary antecedents (social science):**
- Davidson & Karell (2025, SMR) — measurement, prompting, simulation [priority read before drafting]
- Blanchard et al. (2025, Journal of Marketing) — most complete social science pipeline [priority read before drafting]
- Törnberg (2024) — text annotation best practices, prompt stability
- Jones (2025) — qualitative AI disclosure heuristic

**Contrast case:**
- Xu & Yang (2026, arXiv 2602.16733) — automated multi-agent pipeline for scaling replication; contrast with human-in-the-loop workflow

**Framing citations:**
- Grossmann et al. (2023, *Science*) — AI transforming social science; cautiously optimistic framing
- Korinek (2023, NBER) — use cases for economists; practical/descriptive; complementary to the epistemic framework argument

**Open science / pre-registration connection:**
- [see notes-explicit-reasoning.md]
- Nosek et al. (2015, *Science*) — open science
- Freese & Peterson (2017, ARS) — replication in sociology

**Journal policy:**
- Ganjavi et al. (2024) — publishers' author instructions
