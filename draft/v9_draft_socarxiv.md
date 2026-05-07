# Query Authorship: A Framework for Systematic AI Use in Social Science

Torbjørn Skardhamar, Department of Sociology and Human Geography, University of Oslo

**Date:** 2026-05-04

---

## Abstract

**Background:** The widespread adoption of large language models in social science research has created a transparency deficit. The methodologically relevant distinction is not between AI use and non-use but between systematic use and unsystematic use. The latter lacks explicit criteria, human verification, documented outputs, which leaves AI-assisted decisions unaccountable. 

**Epistemic Properties and Policy Implications:** Systematic AI use instantiates the function of pre-registration, externalising tacit decisions before outcomes are known. Existing replication package norms, extended to AI-assisted workflows, provide a sufficient policy framework — one that requires no new infrastructure.

**Workflow:** I describe a systematic workflow across five pipeline stages — literature search, empirical analysis, drafting, review, and documentation — each producing transparency artefacts (skill files, prompt templates, search logs) that constitute a documentation package.

**Conceptual Framework:** I introduce *query authorship*: the intellectual contribution lies in the instructions that shape AI outputs, not in the outputs themselves. Systematic AI authorship makes this contribution auditable; unsystematic use does not.

---

## Introduction

The scholarly record is under documented pressure. Papermill operations — organisations that produce fabricated research for payment — have industrialised the generation of fraudulent work, and AI tools have made that production faster and cheaper. The Hindawi/Wiley retraction of more than eight thousand papers in 2022–23 is the clearest large-scale marker of what that pressure looks like (Retraction Watch, 2023): a major publisher publicly acknowledging that its editorial safeguards had been overwhelmed. AI-induced hallucinated citations contaminate the evidential record in a more dispersed way — citations function as data in social science disciplines, and fabricated references are not a nuisance but a direct integrity failure. Unstructured AI use also multiplies undocumented decision points across the research process, from language editing through substantive rewriting to generating conclusions with authorship attribution: the gradient is continuous and everyone in the field is struggling with where it remains acceptable. The question is not whether AI has entered research practice — it has, and researchers will use it — but whether the field has the right instruments to govern its use.

The dominant institutional response has been to require disclosure. Journals ask authors to declare whether AI tools were used; publishers issue guidelines specifying what must be reported. This is a reasonable first step, but it is insufficient as a primary safeguard on two independent grounds.

The first is scale. Declaration-based policy offers no resistance to industrial-scale fraud: papermill operations can produce plausible disclosures at volume. More tellingly, the response to enforcement-based detection has been the emergence of a counter-industry: services that, for a fee, strip textual patterns associated with AI generation from submitted manuscripts — not to improve the text but to evade detection. Disclosure policy has produced the perverse consequence that it drives AI use underground rather than making it transparent. Documentation policy, by contrast, cannot be evaded in the same way: its artefacts are generated during the work, not as statements made about it afterwards.

The second ground is mechanism. Declaration-based policy rests on a behavioural assumption: that requiring a declaration of intent produces the declared behaviour. That assumption had an unusually prominent empirical demonstration in a much-cited paper reporting that signing an honesty pledge at the top rather than the bottom of a form increases honest reporting. That paper was retracted in 2021 after apparent data fabrication was identified in a co-authored study; two further papers by the same lead author were retracted in 2023 (O'Grady, 2023). The specific mechanism that declaration-based AI policy would need to work — that requiring a declaration of compliance produces compliant behaviour — has lost its most-cited empirical demonstration, and that demonstration was itself fabricated. I do not cite this to impugn the disclosure tradition as a whole, but to make a precise point: the policy instrument most widely adopted has an empirical warrant that has been publicly undermined in precisely the field that generated it.

Journals and publishers responded to genuine problems rapidly and largely in good faith. The concerns motivating binary AI policies — undisclosed AI-generated text, AI-assisted fabrication at scale, questions about authorship and accountability — are real and serious. The argument here is about the instrument, not the intent. A binary approach — use or non-use, disclosed or not — misidentifies the epistemically relevant dimension. What matters is not whether AI was used but whether its use was *systematic*: embedded in explicit criteria, subject to human verification at each stage, and producing documented outputs. The structured/unstructured distinction is where the real epistemic leverage lies, and current policies leave it invisible.

This paper makes five connected moves. First, I develop the distinction between systematic and unsystematic AI authorship, arguing that the two differ not in average output quality but in epistemic standing: systematic use makes errors visible and correctable; unsystematic use does not. Second, I introduce the concept of *query authorship* — the argument that designing a search strategy, a screening rubric, or a review configuration encodes the researcher's intellectual commitments in a verifiable form, and that this constitutes the human contribution in AI-assisted research. Third, I describe a systematic workflow for the social sciences across the research pipeline, from literature search through drafting and review to documentation. Fourth, I argue that systematic AI authorship instantiates the epistemic properties of open-science practices — in particular, the function of pre-registration in forcing explicit commitment to decisions before outcomes are known. Fifth, I draw implications for journal policy, arguing that a documentation-based framework that asks researchers to show what they did is both more epistemically honest and more consistent with existing open-science infrastructure than binary policies.[^1] The concept of systematic AI authorship maps directly onto established scholarly authorship standards — in particular, the ICMJE criteria[^2] — a connection I develop in the section on epistemic properties.

The systematic approach is a spectrum rather than a binary. Degrees of systematic use exist, and how to implement it is up to the author and their theoretical, methodological, and epistemic commitments. The unsystematic approach is off this spectrum rather than at one end of it: the absence of explicit criteria and documentation is not a minimal version of systematic use but something categorically different, because errors cannot be detected and choices cannot be attributed.

The workflow described here is for text-heavy and empirical social science research. The argument is directed at the social sciences, where research questions and theoretical framings cannot be delegated to automated agents. The workflow is demonstrated using Claude (Anthropic) as the AI tool, and some implementation details use Claude-specific terminology; any AI system that supports persistent context, configurable roles, and session logging can implement the same workflow structure.

---

## AI in research

Large language models have been widely adopted across academic disciplines (Grossmann et al., 2023), and in the social sciences their uptake has outpaced the institutional frameworks for evaluating them. Korinek (2023) catalogues practical use cases for economists and social scientists; Feuerriegel et al. (2024) trace early adoption in information systems. The question of whether AI has entered research practice is settled; what remains contested is what kind of practice has emerged and what kind should be.

The dominant institutional response has been the reporting checklist — an instrument designed to improve transparency by specifying what authors must disclose about AI use after the research is done. These checklists have proliferated rapidly. Zrubka et al. (2023) systematically reviewed 24 such instruments and found that item counts range from 10 to 66, indicating that no consensus has emerged on what "full disclosure" even means. Among the most developed are PRISMA-trAIce (Holst et al., 2025) for systematic reviews, TITAN (Agha et al., 2025) for general academic purposes, and the clinical variants TRIPOD-LLM and CONSORT-AI. Publisher and journal guidance follows the same disclosure logic. Mondal et al. (2024) audited 20 major publishers and identified six converging themes across their AI policies — all centred on disclosure of AI use and attribution of responsibility, none on the epistemic structure of the research process itself. Ganjavi et al. (2024) extend this picture to the journal level, finding that 87% of top-ranked journals have issued AI guidelines while only 24% of large publishers have done so, and that individual journals sometimes contradict their own publisher's guidance. Goyanes (2025) documents similar variation in journal-level policies.

Social science has developed some pipeline-oriented guidance. Törnberg (2024) addresses text annotation best practices and prompt stability analysis; Davidson and Karell (2025) provide a framing for integrating generative AI into social science research across measurement, prompting, and simulation tasks. Blanchard et al. (2025) offer the most complete practical pipeline in the social sciences — reproducible prompt templates and pre-registration materials, developed for marketing research. From NLP and data science, Zeng et al. (2025) demonstrate that systematic prompting designed for reproducibility also produces better results on average — a suggestive finding for adjacent social science uses, though not directly transferable. No social-science-specific guidance of this kind exists.

### Checklists and declarations

The checklist approach addresses one genuine problem: it creates a record of AI use that did not previously exist. The limitation is that checklists are post-hoc instruments: they assume the research process was already sound and ask only that the author report on it. A researcher could complete every item on PRISMA-trAIce while having used AI in a wholly unverifiable way. The checklist captures the end state; it has nothing to say about how that end state was produced.

No established framework explicitly theorises the systematic/unsystematic distinction as the fundamental policy-relevant axis. Törnberg (2024) and Davidson and Karell (2025) both implicitly favour more systematic over less systematic AI use, but neither treats this distinction as the central policy question. No existing work treats AI tool configuration — skill files, configured reviewer roles, system-level prompts — as an epistemic mechanism comparable to pre-registration or researcher-degrees-of-freedom disclosure. Neither does any existing work discuss the transparency artefacts produced by systematic AI use as components of a replication package, nor any social-science-specific workflow framework of this kind.

The one settled question in the policy literature is that AI cannot be an author — a position consistent with the ICMJE criteria, which require accountable, consenting persons (Ganjavi et al., 2024; Mondal et al., 2024). But the criteria themselves do more than rule out AI authorship: they specify what the human researcher must demonstrate to claim authorship in any research context. No existing work has developed the ICMJE criteria into a positive framework for evaluating the human researcher's contribution in AI-assisted work. That question is the one that matters for evaluating the epistemic standing of AI-assisted research, and it is the one current policies do not ask.

---

## The systematic/unsystematic distinction

Unsystematic AI authorship is characterised by prompting without explicit criteria and refining until an acceptable output is produced. The criteria are entirely implicit, outputs are accepted without verification, and no documentation is produced that would allow another researcher to audit what was done, let alone reproduce it. The problem is structural: the conditions for verifiable good work with AI are absent.

The epistemic cost of this approach has been documented from several angles. Ludwig, Mullainathan and Rambachan (2024) show that seemingly innocuous choices — which model, which prompt formulation — can produce substantially different parameter estimates, and that these choices are rarely reported. Barrie et al. (2025) find that LLM performance variance is often unacceptably high even under controlled temperature settings; without logging, there is no way to know whether a given result would survive re-running. Kosch and Feger (2025) document a closely related failure they term PARKing — Prompt Adjustments to Reach Known Outcomes — in which researchers iteratively modify prompts until the model returns a desired result, producing outputs that resist replication because the prompt history is undocumented. Cheng et al. (2026) demonstrate that sycophantic AI responses systematically reduce independent judgment and promote dependence. Asher et al. (2026) show that in 640 runs across four published political science datasets, LLMs can perform systematic specification searches — cycling through hundreds of analytical variants and returning significant results — when prompted in certain ways. Peters and Chin-Yee (2025) document generalisation bias: LLMs tend to broaden the scope of scientific conclusions beyond what the original data supports. The failure mode in unsystematic AI use is not random but directional: AI tends to confirm rather than challenge, and to overstate rather than accurately report.

A useful characterisation of what these failure modes share is offered by Frankfurt's (2005) distinction between lying and bullshit: the liar aims to deceive and must track the truth to subvert it, while the bullshitter is indifferent to whether what they say is true. Language models are structurally closer to Frankfurt's bullshitter — they optimise for plausible continuation, not for truth (Hicks et al., 2024). The point is not that researchers using AI are bullshitters; most are truth-seeking. The point is that unsystematic AI use leaves the researcher accepting outputs from a process that does not itself track truth. Systematic use converts a truth-indifferent generator into a truth-accountable workflow by imposing explicit criteria and human verification at each stage.

None of these problems are unique to AI. Undocumented manual coding, unreported variable transformations, and selective literature search are all unsystematic in the same sense. What AI introduces is scale: the range of judgements that can be delegated, and therefore potentially hidden, has expanded enormously. The systematic/unsystematic distinction is not a new principle; it is the application of an existing epistemic standard to a new tool.

There is also a problem about what unsystematic AI use does to research thinking. The writing-as-thinking tradition documents that writing is epistemically valuable precisely because it forces deliberate semantics — the explicit structuring of logical relationships that tacit thought leaves implicit (Emig, 1977). Sommers (1981) frames the complement: revision is not polishing but recursive discovery — finding a structure is itself a strategy for finding meaning, and a writer who is handed a pre-given structure to polish is doing something categorically different from one who discovers structure through composition. Unsystematic AI use maps directly onto this failure: a prompt without explicit criteria, an output accepted without iteration — the AI does the structuring and the researcher accepts the result. The deliberate semantics that would force articulation of what the argument is and why the evidence supports it are bypassed. This is not a concern unique to AI; it is the longstanding concern about delegating cognitive work, now operating at scale.

### What systematic AI use looks like

Systematic AI authorship has three defining features. The first is explicit criteria: the instructions given to the AI specify what to do and on what grounds — not "screen this abstract for relevance" but "retain this abstract if it addresses AI use in empirical research practice; exclude if it addresses only AI as a research subject, AI ethics in general, or K-12 education; retain in case of doubt." The research question or purpose should be part of the persistent context so that each individual prompt is not interpreted in isolation.

The second is human verification: at each stage where the AI produces an output, there is a specified human checkpoint where the output is evaluated against the criteria before it passes to the next stage.

The third is documented outputs: prompt configurations, screening rubrics, skill files, and decision logs are retained as artefacts that allow the process to be reconstructed and evaluated.

These three features are implemented through a project-level configuration with associated file structure that supports progress across the full project. This project-level structure encodes the researcher's theoretical commitments, scope decisions, and evaluative standards. The AI executes within the instructions; the researcher authors the instructions. Systematic use makes this authorship explicit and verifiable. This is what the concept of *query authorship* captures.

Systematic AI authorship is functionally analogous to pre-registration. Pre-registration does not improve research by restricting it but by forcing explicit commitment to research design decisions before outcomes are known. Systematic AI use does the same: the criteria must be articulated before the tool is run, not constructed post hoc to justify what the AI returned. Kosch and Feger's (2025) PARKing is precisely the failure mode that pre-specification forecloses. The analogy holds in function; a relevant disanalogy is that pre-registration involves a public, timestamped commitment, while a systematic AI protocol is initially private. The externalisation benefit, however, follows from the act of specification itself, regardless of whether it is public, and there is no obstacle to pre-registering a systematic AI workflow where the research design permits it.

### Why the distinction matters

Epistemically, the core consequence is simple: systematic use makes errors visible and correctable; unsystematic use does not. A miscalibrated screening rubric in a documented, reproducible workflow can be identified, challenged, and corrected by a reviewer. An undocumented prompt cannot.

The systematic/unsystematic axis is orthogonal to the use/non-use axis that current policy focuses on. A researcher using AI in a systematic and documented way may produce work that is more epistemically auditable than one who relies on undocumented, unreportable manual judgements — judgements about what is relevant, which sources are important, which arguments are coherent — that are equally invisible but have simply not attracted policy attention. The policy question is not, or should not be, whether AI was used, but whether what was done can be evaluated.

---

## A systematic workflow for the social sciences

Established best practice already exists for empirical data analysis — sharing code and data, using version control, documenting variable transformations. These practices apply whether the work is AI-assisted or not, and systematic AI authorship extends rather than replaces them. The focus here is on the research and writing pipeline of a standard journal article covering literature work, empirical analysis, and documentation. Systematic review has its own established protocols and is not addressed here.

A systematic workflow has five stages: 1) literature search with screening and synthesis, 2) empirical data and analysis, 3) drafting, 4) review, and 5) documentation. At each stage the structure is the same: explicit input criteria determine what the AI is instructed to do; a configured AI tool executes within those criteria; a human verification checkpoint evaluates the output before it passes to the next stage; and a documented artefact records what was done. The transparency artefacts produced across all stages — boolean search strings, screening rubrics, skill configurations, prompt templates, search logs, analysis scripts, review records — constitute the replication package.

The basic project folder structure that supports this workflow is illustrated below. Empirical papers include the `data/` subdirectories; non-empirical papers do not.[^3]

```
project/
├── data/
│   ├── raw/                  ← original data
│   └── processed/            ← analysis-ready files
├── scripts/                  ← analysis code (R, Python, Stata)
├── outputs/                  ← tables and figures
├── literature/               ← search logs, source sets, syntheses
├── notes/                    ← working notes and argument sketches
├── draft/                    ← manuscript versions with full edit history
├── logs/                     ← session decision logs and author-input files
└── supplementary/            ← replication package materials
```

A few configuration files at the project root do structural work not visible in the folder tree. One encodes the project context — the research scope, argument, and key distinctions — so that every session starts with the same framing. Another specifies access controls: certain folders, in particular `data/raw/`, can be blocked from the AI's context entirely, providing a structural safeguard that raw data never enters the AI regardless of how the tool is used in a given session. A version-control repository timestamps every change to the project files, so that session logs and author-input files can be verified as contemporaneous records rather than retrospective reconstructions. The full configuration, including illustrative excerpts and tool-specific details, is in the supplementary materials.

This is not an automated pipeline in the sense of Xu and Yang (2026), who demonstrate multi-agent systems capable of scaling well-defined computational tasks with minimal human input. The researcher is in the loop at every stage; the AI handles execution within explicitly defined criteria, and the researcher handles judgement. The distinction matters for both epistemic and methodological reasons: it is precisely this division of labour that makes the workflow's outputs attributable to the researcher.

### Literature search and screening

A standard literature review in a journal article is typically more selective than a systematic review, guided by the author's sense of relevance and shaped by citation patterns. What systematic AI authorship offers is something intermediate: a more thorough and more accountable search and screening process than is typically possible manually, without the full apparatus of a systematic review (Hart, 2025; Gusenbauer & Gauster, 2025).

A realistic workflow combines three routes: automated keyword searches across an open bibliographic database, semantic searches that find papers regardless of keyword choices, and targeted manual retrieval for specific high-priority items. Each route catches what the others miss. Open database APIs with explicit research-use permission are preferable to bulk export from subscription databases, whose institutional agreements may not cover computational analysis. Boolean search strings are documented in advance as explicit inclusion/exclusion criteria — not constructed post hoc — and the full search log is archived. Source synthesis uses a grounded AI tool: queries are submitted to a notebook containing only the relevant-theme documents, and responses are cited from those documents. Unlike a general-purpose chatbot, this produces inline citations the researcher can verify. The synthesis query is itself an instance of query authorship: the intellectual work lies in specifying what the synthesis should produce, what distinctions matter, and what gaps should be identified.

Human verification operates at each stage: spot-checking excluded records for false negatives, reviewing missing PDFs, and cross-checking synthesis outputs against their cited sources independently. The full implementation for this paper — search strings, hit counts, screening criteria, and synthesis queries — is documented in the supplementary materials.

### Empirical data and analysis

The governing principle for primary empirical data is strict separation: the AI operates on the research context and on analysis scripts, not on the data itself. The project folder hierarchy implements this: `data/raw/` for original data as received is immutable after receipt — not modified manually, by scripts, or by AI — and is excluded from the AI's working context. The AI's role is to write, review, and document analysis code to a specification the researcher authors: which variables to construct, which analytical strategy to apply, how edge cases should be handled. This is query authorship in the empirical register — the researcher contributes the specification; the AI its implementation. For the implementation to remain verifiable by a researcher without deep programming expertise, scripts are numbered sequentially to make execution order explicit, and each begins with a header specifying inputs, outputs, and purpose.

For projects with personal data, the tool can be configured to screen files for personal identifiers before any read operation reaches the API — a structural safeguard rather than a per-session norm. A three-zone data model maps onto the folder hierarchy: raw data with identifiers is never sent to the API; pseudonymised data supports AI-assisted cleaning and variable construction; anonymised analysis-ready data is unrestricted. Under GDPR, this structural approach is the relevant minimum standard. The transparency artefacts for empirical work — analysis scripts, codebooks, and data management protocols — are submitted as part of the replication package. The paper's own production is literature-based and does not involve primary data; detailed implementation guidance for empirical projects is in the supplementary materials.

### Drafting, reviewing and adversarial configuration

By the time the drafting stage begins, the outline has been developed and iterated, the literature has been searched and synthesised, any empirical analysis has been conducted, and the main argument has been articulated. The drafting workflow draws on all of this as context. A skill-configured style profile encodes explicit criteria for sentence rhythm, hedging calibration, paragraph structure, and rhetorical stance. Drafts produced by a configured skill are inputs to human revision, not outputs for direct use — the researcher reads, revises, accepts, or rejects each section, exercising the judgement that makes the output theirs. All prompts, configurations, and session logs are retained.

The drafting stage is an opportunity to engage with writing as a mode of thinking, not only as a vehicle for expressing ideas already formed. Writing forces deliberate semantics — the explicit structuring of logical relationships that tacit thought can leave implicit — and revision is a recursive process of discovery rather than polishing: the writer finds meaning by finding a structure that fits it (Emig, 1977; Sommers, 1981). This is the hermeneutic circle between drafting, reviewing, and revising: each pass changes not only the text but the writer's grasp of the argument.

The same mechanism operates in the specification work that systematic AI use requires. Writing a screening rubric, an inclusion criterion, or a skill configuration is not clerical work; it engages deliberate semantics directly — the researcher must articulate in explicit, structured form what would otherwise remain a tacit evaluative standard. Through the act of writing the specification, the researcher often discovers that their prior criterion was ambiguous or inconsistently held; revising it in response is exactly the recursive discovery Sommers describes. This is the cognitive work that query authorship captures, and it is why systematic AI use does not bypass the deliberate semantics of writing but relocates them to the specification layer, where they simultaneously serve the argument and generate verifiable artefacts.

The review-and-revise stage has three components, each addressing a failure mode the others do not.

The first is colleague review — the primary external check. The manuscript is sent to colleagues for human expert feedback. AI-assisted review is supplementary to this, not a substitute. What the structured approach provides is a better-prepared manuscript before it reaches human reviewers: weaknesses that would otherwise appear in referee reports are identified and addressed earlier.

The second is a structured AI-reviewer skill run in a fresh session. Discipline-specific reviewer skills check for internal consistency, unresolved inferential gaps, and framing errors — not whether the argument is compelling but whether it is coherent. These configurations produce legible, actionable feedback organised by type of issue. The fresh-session requirement is critical: reviewing in a session with full prior project context biases the AI toward consistency with previous exchanges rather than independent critical assessment. Fresh-session design approximates the position of an external reviewer encountering the work cold — which is the relevant epistemic standard. Adversarial configuration addresses the sycophancy problem documented by Cheng et al. (2026): explicitly instructing the reviewer skill to be critical and raise objections, built into the persistent skill configuration, encodes a structural countermeasure against confirmation bias. A researcher whose reviewer skill specifies severity testing receives systematically different feedback from one using a default-mode AI review. The difference is in the configuration, not the content.

The third component is cross-model persona review. The same configured reviewer prompts — for this project, six personas calibrated to likely critical positions (for this paper, I specified these as a theoretical social scientist, a philosopher of mind, an applied microeconomist, a computational political scientist, a regulatory committee perspective, and a developer perspective) — are run in fresh sessions across at least two models from different developers. Different models have different training data, tendencies, and likely blind spots; one model's confirmation may reflect that model's biases rather than the argument's strength. A concern raised independently by two or more models is substantially more credible than the same concern raised by only one. Divergence across models on the same question is also informative: it signals where the argument is genuinely ambiguous rather than merely weak in one model's register. This functions as the review equivalent of a robustness check — not because any single AI review is decisive, but because convergence across independent systems is stronger evidence of a real weakness than any single system's output. One concern with AI-reviews is that LLMs tend to be too polite. You could also include a persona that is directly hostile, a toxic colleague or that like. (For this article, this was done after a couple of revisions, which proved surprisingly fruitful).

The synthesis protocol for cross-model review is itself a documented artefact: act on objections raised independently by two or more models; flag for individual judgement objections raised by only one model; note model divergence as a signal of genuine ambiguity; disregard sycophantic positive feedback. The persona prompts and synthesis file are part of the replication package. The persona calibration is itself an instance of query authorship: each persona encodes a specific epistemic position structurally likely to resist the paper's argument from a direction the author cannot fully anticipate. The intellectual work is in designing those constraints; the model's output is execution within them. This is different from asking "what are the weaknesses of this paper?" — a generic question that produces generic feedback.

### Documentation

The documentation produced across all stages serves two distinct functions through two tiers of artefacts. Working logs — daily session records of decisions made, paired with author-input files written in first-person prose — document the process as it happened, including decisions revised and refined along the way. These are analogous to a lab notebook: their evidential weight lies in their contemporaneous character and recording of iterative process. The supplementary materials at submission — skill files, prompt templates, search scripts, screening logs — present the end-state artefacts in reusable, accessible form.

Both tiers are present in the replication package because they serve different functions. The logs provide process integrity evidence; the supplement provides replicability materials. The author-input files document the intellectual origin of the work session by session: which ideas and framings originated with the researcher, which redirections and corrections the researcher made, enabling a CRediT-style account of who contributed what to the work.

It is now common that social science journals require a replication package as a condition of publication, understood as statistical code and data. For a paper using a systematic AI workflow, the transparency artefacts serve the equivalent function. The full replication package for this paper is available at https://github.com/torbskar/structured-use-of-AI; the supplementary materials provide curated excerpts for readers who want a rapid introduction without navigating the full repository.

---

## Epistemic properties of systematic use

The epistemic function of pre-registration is frequently misunderstood as a restriction. The more accurate description is externalisation: the researcher is required to articulate decisions — about design, measurement, analysis — before outcomes are known, which makes those decisions visible, challengeable, and creditable. Pre-registration does not improve research only by constraining it; it improves research by making tacit commitments explicit.

Systematic AI use functions the same way. To direct the AI, the context must be specified: before a search string is executed, the researcher must specify which concepts are to be included and excluded and what constitutes relevance; before a screening rubric is run, the researcher must articulate what the inclusion criteria are; before an analysis script is written, the researcher must specify which variables operationalise the theoretical concepts and which estimator suits the data structure; before a review prompt is submitted, the researcher must specify what standards of argument and evidence the work should meet. None of these specifications are novel — every careful researcher has views on these questions. Systematic use of AI forces their externalisation rather than their implicit deployment.

The tacit knowledge at issue is not the kind associated with expert craft skill — motor and perceptual knowledge that resists verbal articulation. It is closer to what Mitchell et al. (2022) call implicit tacit knowledge: the scope commitments, theoretical priorities, and evaluative standards that a practitioner could articulate if prompted but rarely does. Systematic AI use makes this knowledge explicit by requiring it to be encoded in a query, a rubric, or a configuration.

A related problem is what Gelman and Loken (2014) call the garden of forking paths: the cumulative effect of small, locally reasonable decisions that, undocumented, become invisible in hindsight. A researcher using AI without explicit criteria makes dozens of small acceptance decisions — this framing, this summary, this emphasis — each unremarkable in the moment and seemingly inevitable in retrospect. Documented criteria at each stage are designed to prevent this post-hoc rationalisation.

This is what *query authorship* amounts to. The query is not just an instruction; it is an intellectual contribution — an encoding of the researcher's theoretical commitments in a form that can be examined, challenged, revised, and credited. A well-formed search string embeds a theory of what the relevant literature is and why; a well-formed screening rubric embeds a theory of inclusion that reflects the paper's scope commitments; a well-formed analytical specification embeds a theory of measurement and causal structure; a well-formed reviewer configuration embeds standards of evaluation that the researcher would endorse under scrutiny. The argument that AI-assisted research is not "really" research because the AI wrote the text misses the point: the intellectual work is to a large extent in the query, and the query is authored by the researcher.

The idea that intellectual authorship resides in specification rather than execution is not new to social science or to methodology. Abbott (2004) argues that the core creative act in social science is the heuristic move — the "gambit of imagination" that frames a problem, selects an angle, and constrains what follows — and that execution is not where the intellectual work sits. Krippendorff makes the same point from a methodological direction: rigorous coding instructions are designed so that coders are interchangeable, meaning the executor's identity should not affect the outcome, and the analyst's intellectual contribution is formalised in what he calls the analytical construct — the computable model of how the text relates to the research question. Krippendorff already extends this logic to computer-aided text analysis; LLM query authorship is the next step in that lineage, not a departure from it. What changes with LLMs is not the principle but the failure modes of the executor: sycophancy, generalisation bias, and non-determinism mean that the relationship between specification and output is less stable than for a trained coder or a deterministic algorithm, and it is precisely this instability that makes the documentation and verification requirements specific to systematic AI use.

The pre-registration analogy and its disanalogy were noted above. Syed (2024) argues that a persistent misconception treats pre-registration as appropriate only for confirmatory experimental research; the epistemic argument for externalising decisions in advance applies equally to secondary data analysis, qualitative work, and literature synthesis. The same holds for systematic AI authorship. The key point is that the externalisation function is fully present in systematic AI authorship regardless of whether the initial commitment is public. In principle, the working logs that record iterative process — including when criteria were changed and why — address the cherry-picking risk that pre-registration's public commitment eliminates through publicity.

### Systematic use as open science practice

The transparency artefacts produced by systematic AI use — skill files, prompt templates, boolean search strings, screening logs — have the formal properties open-science infrastructure already requires for other research outputs. They are shareable, versionable, independently evaluable, and capable of being deposited in a repository. A reviewer who receives a replication package containing a search script, a screening rubric, and a skill file can assess whether the inclusion criteria were explicit before the search and whether the screening decisions are reproducible from the submitted materials. This is the same evaluation that reviewers of quantitative replication packages perform with statistical code and data.

The Momeni et al. (2025) checklist for computational reproducibility in social science, developed with over 180 social scientists, covers data documentation, source sharing, and methodological reporting. Systematic AI use satisfies these requirements naturally — as a byproduct of the workflow, not as an additional burden. Törnberg's (2024) point about prompt stability analysis makes the same connection: testing whether minor prompt changes alter results is only possible if prompts are documented. Systematic use makes this possibility available by default.

Freese and Peterson (2017) identify social science's engagement with open science norms as incomplete. Systematic AI use applied across the research pipeline — literature selection, analytical decision-making, conceptual development, argument review — produces exactly the kind of decision documentation that Freese and Peterson identify as missing.

### The reliability finding and its limits

Zeng et al. (2025) find, across 1,032 tasks in data science, that reproducibility correlates positively with accuracy: prompting strategies designed for reproducibility also produce better results on average. If this finding generalises, systematic use is not merely a transparency mechanism but a quality mechanism. I suggest this is plausible: the same reasoning that produces a clear and specific inclusion criterion probably produces a better-executed search than vague prompting. The evidence from adjacent fields does not support the common assumption that reproducibility requirements trade off against quality.

This has not been demonstrated for social science research specifically. The claim here is more limited: systematic AI authorship is a necessary condition for the kind of quality control that makes errors detectable, and the adjacent evidence does not support the assumption of a trade-off.

### What systematic use cannot guarantee

It is worth distinguishing three levels at which systematic use bears on epistemic accountability. The first is what documentation *certifies*: that the criteria governing AI use were specified before the tool was run. Publicly timestamped documentation — a pre-registered protocol, or a project pushed to a public repository at the outset — provides stronger evidence than private logs, which remain researcher-controlled. The second is what documentation *makes possible but does not certify*: independent evaluation of whether the AI's execution of those criteria was accurate. Documentation is a prerequisite for this evaluation, not a guarantee that it was passed; its quality depends on the domain expertise of the researcher doing the verification. The third is what *no documentation regime can fully resolve*: non-deterministic AI outputs and the effect of model-version change.

Systematic use does not guarantee quality or eliminate errors. Documentation can be faked, as with any research record; what systematic documentation provides is evaluable artefacts rather than mere assertion, which makes fabrication more detectable. Working logs that record iterative process — including unsuccessful attempts — are substantially harder to retroactively sanitise than end-state outputs. The documentation should include the model version string alongside prompt templates and screening logs: the same workflow run against a later model version may produce substantially different outputs, and without the version string the documented process cannot be reproduced under equivalent conditions. More technically reliable logging infrastructure exists (Singh, 2026) but is not yet standard in academic research tools.

Non-determinism is a practical challenge. The appropriate response is to log outputs alongside prompts, note when re-runs produce substantively different results, and treat AI output as input to human judgement rather than as a final product.

The argument here is not that all AI use must be systematic, any more than the case for replication packages implies that all analysis must be automated. Researchers will continue to work exploratorily, to think while writing, and to let the process develop their thinking. What systematic AI authorship provides is not a constraint on how one works but evidence of how one worked. The same logic governs open science practices more broadly: if a hypothesis was not pre-registered, one must assume some degree of forking paths was possible; if code is not available, one must assume the study is not independently replicable; if AI workflow artefacts are not available, one must assume the process was unsystematic. These inferences are not certain, but the absence of evidence forces a conservative prior. The choice to work without producing accountability artefacts is a legitimate one; so is the reader's inference from their absence.

One scope note applies to this paper's own composition: it was systematic in infrastructure and more hermeneutic in argument development — as the spectrum framing predicts. The systematic elements (session logs, reviewer skills, documented literature search) did real epistemic work; the conceptual moves developed through the writing rather than from a pre-specified plan. Acknowledging this is not a concession; it is the demonstration that the framework's value does not depend on pre-registered rigidity.

### Authorship criteria and the accountability threshold

Scholarly authorship has an established standard. The ICMJE criteria require substantial intellectual contribution to conception or design; critical revision for intellectual content; final approval; and accountability for all aspects of the work. AI is excluded decisively — it cannot consent and cannot be held accountable. The settled question is that AI cannot be an author.

The more interesting question is what the criteria require of the human researcher in AI-assisted work. On criterion 1, query authorship maps directly: designing a search strategy, specifying inclusion and exclusion criteria, formulating synthesis questions, and configuring a reviewer skill are all acts of conception and design in the relevant sense. The difference systematic use makes is not in whether these contributions exist but in whether they are documented and verifiable. Systematic AI authorship produces the evidence that criterion 1 is met; unsystematic use produces no such evidence.

Criterion 2 requires drafting or reviewing the work critically. Author-input files are a direct instantiation: they document, session by session, what the researcher directed, redirected, and rejected. Criterion 3 — final approval — is formally met by any researcher who submits. What systematic use adds is that the approval is *informed*: the researcher can trace the process that produced the version they approved. These two criteria, considered together, distinguish genuine intellectual engagement from passive acceptance of AI output.

Criterion 4 is where the argument becomes sharpest. To be genuinely accountable for the work — able to investigate questions about accuracy and integrity, to explain why decisions were made, to show that the process was sound — the researcher must have access to the process that produced the work. Systematic AI authorship is designed to produce exactly this access. The standard model of research accountability presupposes that the researcher knows what they did and can recall or reconstruct it if questioned. Where AI executed the work, recall alone cannot do the same epistemic job. The documentation framework provides the evidentiary supplement that makes criterion-4 accountability substantive rather than nominal.

The ICMJE criteria give policy a more tractable question than "was AI used?" Given that researchers are already obligated to meet these criteria for any work they claim as their own, the relevant evaluative question for AI-assisted research is whether the process permits the researcher to demonstrate that authorship criteria are met. A documentation-based framework asks exactly this. Binary prohibition addresses the easy question while leaving the harder one unasked.

---

## Implications for journal policy

### What most common policies do

The response of journal editors and publishers to AI tools has been rapid and, in the context of genuine uncertainty, largely sensible. The policies developed in response to real concerns — AI-generated text submitted as original work, fabricated references, authorship questions — address these concerns directly (Mondal et al., 2024; Ganjavi et al., 2024; Goyanes, 2025; da Veiga, 2025). The field has moved from silence to active guidance in under two years, which is fast for any institutional domain.

The guidance has converged on six themes across major publishers: requiring disclosure of AI use, prohibiting AI authorship, placing responsibility on corresponding authors, requesting transparency about what AI was used for, urging caution with AI-generated content, and specifying that human oversight is required (Mondal et al., 2024). These are reasonable minimum standards. The question I address here is not whether they are sensible but whether they are sufficient.

### The problem with binary policies

A common policy structure is to rely on disclosure of whether AI was used or not. This has perhaps never been quite satisfactory, and tiered disclosure has begun to emerge, demanding task-specific disclosure (Jones, 2025; Davidson & Karell, 2025). SocArXiv's 2026 AI policy is a concrete illustration of this partial move and of its remaining gap. The policy states directly that "we are getting overrun with machine-generated slop, some of which is manipulative or fraudulent," while acknowledging that "some real researchers are using LLMs and other automation tools to help do research" (SocArXiv, 2026). The permitted-use list distinguishes by task — literature searching and idea organisation with human verification are explicitly allowed; verbatim AI text generation and unreviewed outputs are not. This is meaningfully closer to the framework developed here than a binary disclosure requirement. Yet the systematic/unsystematic axis remains invisible: a researcher with a documented, criterion-governed literature search and one who accepted unverified outputs from an unconfigured chatbot both pass on the acceptable side of the same distinction.

The first consequence is the inadvertent penalisation of systematic use. A researcher who built a documented, reproducible screening protocol with explicit inclusion criteria, logged outputs, and human verification checkpoints is treated identically to one who asked a general-purpose chatbot to summarise their references and accepted the output without review. Both used AI; both must disclose. The disclosure requirement captures nothing about the epistemic difference between the two cases.

The second is the permissiveness of disclosure as a standard. A statement that "AI was used to assist with analysis" gives readers no actionable information about whether the use was epistemically sound. A disclosure that names AI use without specifying the epistemic structure of that use is a performance rather than a practice (Sibbald et al., 2025). The incentive structure this creates does not favour systematic use.

Two practical complications compound this structural problem. Restrictive binary policies face an inherent enforceability gap: AI detection tools are not sufficiently reliable to identify undisclosed AI use, meaning prohibitions function largely on author compliance rather than institutional verification — an enforcement mechanism that disadvantages honest actors while leaving dishonest ones undetected. Disclosure requirements may also introduce systematic bias against non-native English speakers who use AI for linguistic polishing (Ganjavi et al., 2024).

### A documentation-based alternative

The conservative framing of this argument is important: it requires no new principle and no new infrastructure. Journals that already require replication packages for quantitative work have already accepted the underlying logic — that research claims should be accompanied by the materials needed to verify how the analysis was conducted. For a study using regression, those materials are code and data. For a study using a systematic AI workflow, they are skill files, prompt templates, search scripts, and screening logs. This paper's replication package, available at the project repository and excerpted in the supplementary materials, illustrates what such a package looks like in practice. Journals that already require replication packages have the infrastructure — deposition workflows, editorial review procedures, and author guidance — that a documentation-based AI policy would use.

In practice, this means that peer review of AI-assisted work should be able to evaluate the quality of the systematic process rather than simply its existence. Reviewers and editors should be able to assess whether the configuration choices are theoretically justified and accountable. This requires familiarity with systematic AI workflows that most current reviewers do not have — but so did statistical code review before replication packages became standard, and that competence is now widely expected. Documentation norms create the incentive to acquire it. Davidson and Karell (2025) and Jones (2025) move in this direction, developing disclosure frameworks that specify what was done rather than merely whether AI was involved. The documentation-based framework developed here formalises and extends this emerging direction, connecting it to existing open-science infrastructure.

This approach shifts the evaluative burden to peer review, where it belongs. Reviewers can assess whether a systematic process was appropriate; they cannot currently assess whether an undocumented one was. Blanket restriction avoids the problem by eliminating the behaviour; documentation-based policy addresses it by making the behaviour evaluable.

---

## Conclusion

I have argued that the systematic/unsystematic AI authorship distinction — not the use/non-use binary — is the epistemically relevant axis for evaluating and governing AI-assisted research. The distinction is not merely terminological. Systematic AI authorship is de facto an authorship contribution in its own right: the intellectual work lies in designing the query, the workflow, and the verification structure, not in the generated text. Unsystematic use is unaccountable not because it is careless but because the conditions for verifiability are absent. A binary policy that asks "did you use AI?" is answering the wrong question.

The concept of *query authorship* identifies the mechanism. The researcher's intellectual contribution in AI-assisted work lies in the criteria, configuration, and verification design — the search string that encodes a theory of relevance, the screening rubric that encodes scope commitments, the reviewer configuration that encodes evaluative standards. These commitments are authored by the researcher, not generated by the AI. Systematic use makes them explicit and verifiable; unsystematic use leaves them tacit and unauditable.

The transparency artefacts produced by systematic AI authorship — skill files, prompt templates, search scripts, screening logs, and session-by-session author-input records — have the formal properties that open-science infrastructure already requires for other research outputs. Author-input files document the human intellectual origin of the work at each stage: which framings, arguments, and redirections originated with the researcher, and which with the AI. This is a function analogous to authorship declarations in co-authored work and is directly relevant to ICMJE criterion 4 — that the researcher be genuinely accountable for all aspects of the work. The replication package for this paper serves that function: the documentation itself is the demonstration.

The policy directive follows. Journals should not ask "did you use AI?" — a question that is unenforceable, that treats systematic and unsystematic use identically, and that addresses the easy question while leaving the harder one unasked. The right question is: show us your systematic process. Operationally, this means extending existing replication package norms to AI-assisted workflows. Journals that already require replication packages for quantitative work already have the infrastructure to require the equivalent for AI-assisted work. No new principle and no new infrastructure is needed.

The workflow described in the preceding sections is both argument and demonstration. The replication package — project configuration files, search scripts, skill files, persona review prompts, and session-by-session author-input logs — is available at https://github.com/torbskar/structured-use-of-AI, with curated excerpts in the supplementary materials. A reader can examine the systematic process, not merely read the account of it. Social scientists who build explicit search criteria, maintain screening logs, document analytical decisions, configure review tools against known failure modes, and record their iterative decision process are already doing open science. The gap is not in the infrastructure but in the policy framework that decides what counts as meeting the standard.

---

## Acknowledgements

I am grateful for valuable comments from Lars-Erik Kjekshus, Alexi Gugushvili, Johan Fredrik Rye, and Torkild H. Lyngstad for the almost daily discussions on AI.

---

## References

Abbott, A. (2004). *Methods of Discovery: Heuristics for the Social Sciences*. New York: W. W. Norton & Company.

Agha RA, Mathew G, Rashid R, Kerwan A, Al-Jabir A, Sohrabi C, Franchi T, Nicola M, Agha M, TITAN Group (2025). Transparency In The reporting of Artificial INtelligence — the TITAN guideline. *Premier Journal of Science*, 10, 100082.

Asher, S., Malzahn, J., Paschal, E., Persano, J., Myers, A. C. W., & Hall, A. B. (2026). Sycophancy and statistical analysis in large language models. Working paper. https://andrewbenjaminhall.com/asher_et_al_LLM_sycophancy.pdf

Barrie, C., Palmer, A., & Spirling, A. (2025). Replication for language models: problems, principles, and best practice for political science. Working paper. https://arthurspirling.org/documents/BarriePalmerSpirling_TrustMeBro.pdf

Blanchard, S. J., Duani, N., Garvey, A. M., Netzer, O., & Oh, T. T. (2025). New Tools, New Rules: A Practical Guide to Effective and Responsible Generative AI Use for Surveys and Experiments in Research. *Journal of Marketing*, 89(6), 119–139.

Cheng, M., Jurafsky, D., et al. (2026). Sycophantic AI decreases prosocial intentions and promotes dependence. *Science*, 391, eaec8352.

Collins, H. M. (2001). Tacit Knowledge, Trust and the Q of Sapphire. *Social Studies of Science*, 31(1), 71–85.

Davidson, T., & Karell, D. (2025). Integrating Generative Artificial Intelligence into Social Science Research: Measurement, Prompting, and Simulation. *Sociological Methods & Research*, 54(3), 775–793.

Emig, J. (1977). Writing as a mode of learning. *College Composition and Communication*, 28(2), 122–128.

Feuerriegel, S., et al. (2024). Generative AI. *Business & Information Systems Engineering*, 66(1), 111–126.

Frankfurt, H. G. (2005). *On bullshit*. Princeton University Press.

Freese, J., & Peterson, D. (2017). Replication in social science. *Annual Review of Sociology*, 43, 147–165.

Ganjavi, C., Eppler, M. B., Pekcan, A., Biedermann, B., Abreu, A., Collins, G. S., Gill, I. S., & Cacciamani, G. E. (2024). Publishers' and journals' instructions to authors on use of generative artificial intelligence in academic and scientific publishing: bibliometric analysis. *BMJ*, 384.

Gelman, A., & Loken, E. (2014). The statistical crisis in science. *American Scientist*, 102(6), 460–465.

Goyanes, M., Lopezosa, C., & Piñeiro-Naval, V. (2025). The use of artificial intelligence (AI) in research: a review of author guidelines in leading journals across eight social science disciplines. *Scientometrics*, 130, 3725–3741.

Grossmann, I., Feinberg, M., Parker, D. C., Christakis, N. A., Tetlock, P. E., & Cunningham, W. A. (2023). AI and the transformation of social science research. *Science*, 380(6650), 1108–1109.

Gusenbauer, M., & Gauster, S. P. (2025). How to search for literature in systematic reviews and meta-analyses: A comprehensive step-by-step guide. *Technological Forecasting & Social Change*, 212, 123833.

Hart, C. (2025). *Doing a literature review: releasing the research imagination* (3rd edition). Sage.

He, C., Zhou, X., Wang, D., Xu, H., Liu, W., & Miao, C. (2026). The AutoResearch moment: From experimenter to research director. Preprints.org.

Hicks, M. T., Humphries, J., & Slater, J. (2024). ChatGPT is bullshit. *Ethics and Information Technology*, 26(2), 38.

Holst, D., Moenck, K., Koch, J., Schmedemann, O., & Schüppstuhl, T. (2025). Transparent Reporting of AI in Systematic Literature Reviews: Development of the PRISMA-trAIce Checklist. *JMIR AI*, 4, e80247.

Jones, K. M. L. (2025). Generative AI in qualitative research and related transparency problems: a novel heuristic for disclosing uses of AI. *International Journal of Qualitative Methods*, 24.

Korinek, A. (2023). Language models and cognitive automation for economic research. NBER Working Paper 30957.

Kosch, T., & Feger, S. (2025). Prompt-hacking: The new p-hacking? *ACM Reference Format*, 1(1), 1–5.

Krippendorff, K. (2019). *Content analysis: An introduction to its methodology* (4th ed.). SAGE Publications.

Ludwig, J., Mullainathan, S., & Rambachan, A. (2024). Large language models: an applied econometric framework. arXiv preprint 2412.07031.

Massimo A, Le Trang, Corrado C, Alessandra B, June C (2024). openalexR: An R-Tool for Collecting Bibliometric Data from OpenAlex. *The R Journal*, 15, 167–180. [*Note: verify author names before submission*]

Mitchell, R. L. C., Holton, P., Chandola, T., Payne, J., Abell, J., & Ward, J. (2022). Where does all the 'know how' go? The role of tacit knowledge in research impact. *Higher Education Research & Development*, 42(2).

Mondal, H., Mondal, S., & Behera, J. K. (2025). Artificial intelligence in academic writing: Insights from journal publishers' guidelines. *Perspectives in Clinical Research*, 16(1), 56–57.

Momeni, F., Khan, M. T., Kiesel, J., & Ross-Hellauer, T. (2025). Checklists for computational reproducibility in social sciences: insights from literature and survey evaluation. In *Proceedings of the 3rd ACM Conference on Reproducibility and Replicability (ACM REP '25)* (pp. 179–191).

O'Grady, C. (2023). Honesty papers retracted for data 'discrepancies.' *Science*, 381(6655), 255–256.

Peters, U., & Chin-Yee, B. (2025). Generalization bias in large language model summarization of scientific research. *Royal Society Open Science*.

Polanyi, M. (1966). *The Tacit Dimension*. Chicago: University of Chicago Press.

Retraction Watch. (2023, December 19). *Hindawi reveals process for retracting more than 8,000 paper mill articles*. https://retractionwatch.com/2023/12/19/hindawi-reveals-process-for-retracting-more-than-8000-paper-mill-articles/

Sibbald, K. R., Phelan, S. K., Beagan, B. L., & Pride, T. M. (2025). Positioning Positionality and Reflecting on Reflexivity: Moving From Performance to Practice. *Qualitative Health Research*, 0(0).

Singh, K. (2026, February 25). Auditing and logging AI agent activity: A guide for engineers. LoginRadius Engineering Blog. https://www.loginradius.com/blog/engineering/auditing-and-logging-ai-agent-activity

SocArXiv. (2026, March 8). *AI policy*. Center for Open Science. https://socopen.org/ai-policy/

Sommers, N. (1981). Intentions and revisions. *Journal of Basic Writing*, 3(3), 41–49.

Syed, M. (2024). Three persistent myths about open science. *Journal of Trial and Error*, 4(2).

Törnberg, P. (2024). Best practices for text annotation with large language models. *Sociologica*, 18(2), 67–85.

da Veiga, A. (2025). Ethical guidelines for the use of generative artificial intelligence and artificial intelligence-assisted tools in scholarly publishing: a thematic analysis. *Science Editing*, 12(1), 28–34.

Xu, Y., & Yang, X. (2026). Scaling reproducibility: an AI-assisted workflow for large-scale replication and reanalysis. arXiv preprint 2602.16733.

Zeng, J., et al. (2025). AIRepr: an analyst-inspector framework for evaluating reproducibility of LLMs in data science. In *Findings of the Association for Computational Linguistics: EMNLP 2025*.

Zrubka, Z., Kovács, L., Motahari Nezhad, H., et al. (2023). Artificial Intelligence in Medicine: A Systematic Review of Guidelines on Reporting and Interpreting Studies. Preprint.

---

---

*Draft v9 — 2026-05-04*

[^1]: The replication package for this paper consists of workflow artefacts — skill files, prompt templates, search scripts, screening logs, and author-input files — rather than statistical code and data. This is submitted as a methodological contribution to a journal whose open science policy (requiring openly accessible code and materials for all manuscripts submitted from June 2025) is itself an instance of the documentation norm the paper argues for.

[^2]: [ICMJE | Recommendations | Defining the Role of Authors and Contributors](https://www.icmje.org/recommendations/browse/roles-and-responsibilities/defining-the-role-of-authors-and-contributors.html)

[^3]: More elaborate practitioner implementations of the same structured approach exist. Sant'Anna (n.d.) describes a Claude Code research workflow featuring twenty-eight configured reviewer skills, fourteen specialised agents, automated quality gates, and AEA replication standards compliance, framed explicitly as a "ceiling, not floor" with documented entry points for new adopters (https://psantanna.com/claude-code-my-workflow/workflow-guide.html). The workflow described in this paper is intentionally minimal: the epistemic properties at issue — explicit criteria, human verification, and documented outputs — are present at any level of tooling complexity.
