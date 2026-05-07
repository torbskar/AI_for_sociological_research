# Query Authorship: A Framework for Systematic AI Use in Social Science

Torbjørn Skardhamar, Department of Sociology and Human Geography, University of Oslo

**Date:** 2026-05-06

---

## Abstract

**Background:** The widespread adoption of large language models in social science research has created a specific authorship problem: when AI executes research tasks, the human researcher's intellectual contribution becomes opaque. Existing institutional responses — disclosure requirements, reporting checklists — address whether AI was used and whether it was disclosed; none address the epistemic structure of the process or the question of authorship.

**Conceptual Framework:** I argue that authorship in AI-assisted research requires documentable intellectual contribution at the level of the query — search criteria, screening rubrics, analytical specifications, and reviewer configurations. I call this *query authorship*. Drawing on the ICMJE authorship criteria, in particular criterion four's requirement of genuine accountability, I show that query authorship is what makes the human contribution demonstrable and satisfies the established standard for scholarly authorship.

**Workflow:** Systematic AI use — characterised by explicit criteria, human verification at each stage, and documented outputs — is the condition under which query authorship can be demonstrated. I describe a workflow across the research pipeline (literature search, empirical analysis, drafting, review, documentation) and the documentation package it generates.

**Policy Implications:** Because query authorship must be demonstrable to satisfy ICMJE criteria, the policy directive follows from the authorship argument rather than from a contested diagnosis of policy failure: journals should require documentation packages for AI-assisted work, modelled on existing replication-package norms, and ask not "did you use AI?" but "can you show what you did?"

---

## Introduction

Large language models can now produce plausible academic text across the full research pipeline — synthesising literature, generating interpretation, drafting arguments, reviewing manuscripts. Their adoption in social science research is rapid, widespread, and will not be reversed (Grossmann et al. 2023). This creates a specific problem for scholarship: when the text could have been generated, the question of what the human researcher contributed becomes genuinely open. That question is not primarily about fraud. It is about authorship — the conditions under which a researcher can claim the intellectual responsibility that authorship entails.

Existing institutional responses have converged on disclosure. Journals require authors to declare whether AI tools were used; publishers issue guidance specifying what must be reported. These requirements address a genuine concern in a reasonable way. The difficulty is that they do not address the authorship question. A disclosure that AI was used for literature review tells a reader almost nothing about whether the researcher made the intellectual contributions that authorship requires; the same disclosure is consistent with careful systematic work and with unverified acceptance of whatever the model produced. Reporting checklists for AI use — of which there are now more than twenty, with item counts ranging from ten to sixty-six (Zrubka et al. 2023; Holst et al. 2025; Agha et al. 2025; Mondal et al. 2025; Ganjavi et al. 2024) — share this limitation: they address what was used and whether it was disclosed; none address the epistemic structure of the process that produced the work.

Two practical weaknesses compound this structural limitation. Disclosure requirements that depend on author self-report are vulnerable exactly where the incentive to under-report is highest — when detection is unreliable and the consequences of disclosure are uncertain. More concretely, enforcement-oriented detection has already produced a counter-industry: services that strip AI-associated textual patterns from manuscripts before submission, driving AI use underground rather than making it transparent. Documentation policy cannot be evaded in the same way; its artefacts are generated during the work, not asserted about it afterwards.

This paper develops a different approach. I argue that what authorship requires when AI is involved is documentable intellectual contribution at the level of the query — the search criteria, screening rubrics, analytical specifications, and reviewer configurations that shape what the AI does. I call this *query authorship*. The conditions under which query authorship can be demonstrated are the conditions of *systematic use*: explicit criteria, human verification at each stage, and documented outputs. The policy implication follows directly: journals should not ask whether AI was used, but whether the researcher can demonstrate query authorship through a documentation package. No new principle is required — the extension of existing replication-package norms to AI-assisted workflows is the instrument, and journals that already require replication packages already have the infrastructure.

The argument proceeds in seven steps. I begin by developing the authorship problem — what AI does to the human contribution and why the question of what the researcher contributed becomes genuinely open. I then introduce the concept of query authorship and argue that it satisfies the established criteria for scholarly authorship. I develop systematic use as the condition under which query authorship can be demonstrated, and describe a practical workflow across the research pipeline. I argue that systematic use produces an epistemic dividend by externalising tacit knowledge in a form that is auditable and creditable. I describe the documentation package that systematic use generates and how it fits existing open-science infrastructure. I draw the policy implications. And I conclude by connecting the argument to the authorship question with which it began.

The argument is directed at text-heavy and empirical social science research. Systematic reviews have their own established protocols and are out of scope here.

---

## What AI does to authorship

### The authorship problem

The problem AI creates for scholarship is not primarily the problem of fraud, though fraud exists and matters. The deeper problem is authorship — what it means to claim intellectual responsibility for work that an AI system substantially executed.

This is a harder problem than it first appears. A researcher who uses AI to generate a first draft of a literature review, accepts that draft with light editing, and submits the result has produced something. The question is whether they have met the conditions for claiming the intellectual contribution that authorship entails. The text is theirs in the sense that they submitted it; it is less clear that it is theirs in the sense that they can answer for its every claim, trace every interpretive move, and explain why the synthesis emphasises what it does. When a researcher uses AI across multiple stages — search, synthesis, analysis, drafting, review — the accumulation of undocumented decisions makes the authorship question harder to answer still.

Importantly, this is not a question about intent. A researcher who used AI carelessly, without intending to deceive, may nonetheless be in a position where they cannot substantively defend the work they submitted. The authorship problem is structural, not motivational. It arises as soon as the conditions for genuine accountability are absent, regardless of whether the researcher would recognise them as absent.

### The bullshit warning

At scale, this structural problem has a specific shape. Large language models do not track truth. Frankfurt (2005) drew a distinction between lying and bullshit that is useful here: the liar aims to deceive and therefore must track the truth to subvert it, while the bullshitter is simply indifferent to whether what they say is true. Hicks, Humphries, and Slater (2024) apply this characterisation directly to LLMs: these systems optimise for plausible continuation, not for accuracy. They produce text that fits what would come next in a plausible academic argument, regardless of whether the underlying claim is well-supported. This is not a deficiency that will be fixed by improving the models; it is a structural feature of how they work.

The practical consequences are documented across several studies. Kosch and Feger (2025) identify PARKing — Prompt Adjustments to Reach Known Outcomes — in which researchers iteratively modify prompts until the model returns a desired result; the outcome fits the researcher's prior expectations and the prompt history that produced it is undocumented. Cheng et al. (2026) show that sycophantic AI responses systematically reduce independent judgment: the model tends to confirm the user's existing perspective rather than challenge it. Peters and Chin-Yee (2025) document generalisation bias: LLMs broaden the scope of scientific conclusions beyond what the underlying evidence supports. Ludwig, Mullainathan, and Rambachan (2024) demonstrate that seemingly innocuous choices — which model, which prompt formulation — can produce substantially different parameter estimates. Barrie, Palmer, and Spirling (2025) find LLM performance variance unacceptably high even under controlled conditions. Asher et al. (2026) show that LLMs can execute systematic specification searches when prompted in certain ways. The failure mode in unsystematic AI use is not random. It is directional: the tool confirms rather than challenges, and overstates rather than accurately reports.

The Hindawi/Wiley retraction of more than eight thousand papers in 2022–23 is the sharpest large-scale illustration of what it looks like when this pattern operates at industrial scale (Retraction Watch 2023). This is not primarily evidence that current AI disclosure policies have failed — the Hindawi episode predates most such policy. It is a warning of what unchecked AI use could produce: the gap between plausible-looking text and genuine scholarship can be vast, and it can be invisible without structural safeguards. The question this paper addresses is how a researcher can demonstrate that their AI-assisted work is genuinely the product of a truth-seeking process rather than a truth-indifferent one.

### ICMJE criterion four as the accountability standard

Scholarly authorship has an established standard. The ICMJE criteria — developed for biomedical research but widely adopted across disciplines — require four things: substantial contribution to conception or design, or to acquisition, analysis, or interpretation of data; critical revision for important intellectual content; final approval of the version to be published; and accountability for all aspects of the work, including the ability to investigate questions about accuracy and integrity.

The ICMJE criteria are the de facto reference standard in empirical social science authorship research. In a survey of 2,222 social scientists, Pruschak and Hopp (2022) find that social scientists apply these criteria as their normative benchmark — if inconsistently, with honorary authorship affecting 43 percent of papers. Instructively, that study operationalised only the first three ICMJE criteria, excluding criterion four "for the sake of simplicity and comparability": the criterion social science has found most difficult to operationalise is, for AI-assisted research, the criterion that does the most work.

The first three criteria raise important questions for AI-assisted research, which I take up in the next section. The fourth is the sharpest. To be genuinely accountable, a researcher must be able to investigate questions about the accuracy and integrity of the work — to trace the analytical steps, explain the interpretive choices, and show that the process was conducted appropriately. This requires access to the process, not just access to the output.

Where AI executed the work and the researcher accepted the output without documentation, recall alone cannot satisfy criterion four. A researcher who cannot say which inclusion criteria governed a screening exercise, why a particular synthesis framing was selected, or how the review process produced the argument in the final manuscript — because none of these were documented — is not in a position to investigate questions about accuracy and integrity in any substantive sense. They may be honest, careful, and highly competent. But the structural conditions for genuine accountability are absent.

It then follows that this gives journal policy a more tractable question than "was AI used?". The tractable question is: can the researcher demonstrate that the authorship criteria are met? That question has a concrete answer — yes or no — and that answer can in principle be evidenced. What it requires is a documentation package that shows the process was conducted as claimed. Developing what that package consists of, and what conditions must hold for it to be produced, is the task of the sections that follow.

---

## Query authorship: the human contribution in AI-assisted research

### Where the intellectual work sits

I have argued that the authorship problem arises from the opacity of the human contribution when AI executes research tasks. To see where the human contribution actually lies, it helps to consider what makes AI-assisted research different from any other case in which the researcher delegates execution.

Abbott (2004) argues that the core creative act in social science is the heuristic move — the framing of a problem, the selection of an angle, the constraint of what follows — and that execution is not where the intellectual work sits. This is not a concession made for AI; it is a general claim about where the judgment that distinguishes research resides. The analyst who designs a coding scheme for a content analysis and trains a team of research assistants has made the intellectual contribution in the design; the coders execute within it. Krippendorff (2019) formalises this point: rigorous coding instructions are designed so that coders are interchangeable — the executor's identity should not affect the outcome — and the analyst's intellectual contribution is formalised in what he calls the analytical construct, the computable model of how the text relates to the research question. Krippendorff already extends this logic to computer-aided text analysis. Query authorship is the next step in that lineage, not a departure from it.

Query authorship may appear strikingly novel. It is not. The principle — that intellectual contribution resides in the specification, and that execution by an interchangeable agent does not diminish it — is well established. What is new is the executor and its particular failure modes, not the move itself. The same observation applies to the writing-as-thinking tradition (Emig 1977; Sommers 1981), which I develop more fully below: writing is epistemically valuable because it forces deliberate semantics, the explicit structuring of logical relationships that tacit thought leaves implicit. Query authorship does the same work at the specification layer. Designing a search criterion, a screening rubric, or a reviewer configuration is not clerical preparation for research; it is an instance of deliberate semantics — the researcher must articulate in explicit, structured form what would otherwise remain a tacit evaluative standard. In this respect, Krippendorff and the writing-as-thinking tradition converge. Query authorship names the convergence point in an LLM context.

What does change with LLMs is the instability of the executor. A trained coder following a well-specified rubric produces outcomes whose variance is bounded by the rubric's precision. An LLM operating on the same rubric introduces additional variance through sycophancy, generalisation bias, and non-determinism — the failure modes documented in the previous section. It is precisely this instability that makes the documentation and verification requirements specific to systematic AI use. The principle of specification-authored intellectual contribution is continuous with established practice; the operational requirements that protect it are LLM-specific.

### Query authorship satisfies the ICMJE criteria

Criterion four — genuine accountability — is the sharpest test, as I have argued. But query authorship also satisfies the prior three criteria in ways that are worth making explicit, because they give the concept its positive institutional traction.

Criterion one requires substantial contribution to conception or design, or to the acquisition, analysis, or interpretation of data. Designing a search strategy is an act of conception: it embeds a theory of what the relevant literature is and why. Specifying inclusion and exclusion criteria is an act of design: it formalises the scope commitments of the research question. Formulating synthesis questions is an act of interpretation: it encodes what the literature is expected to say about what. Configuring a reviewer skill with discipline-specific evaluative standards is an act of design in exactly the sense criterion one requires. These are not administrative tasks; they are the intellectual moves through which the research takes its shape.

Criterion two requires critical revision for important intellectual content. Author-input files — session-by-session records of what the researcher directed, redirected, and rejected — are a direct instantiation of this. They document, in contemporaneous first-person prose, which ideas and framings the researcher introduced, which AI outputs were modified or discarded and why, and which interpretive decisions were made by the researcher against the model's suggestions. This is critical revision in the precise sense the criterion requires: not passive acceptance of AI output but active intellectual engagement with it, documented as it happened.

Criterion four, as I have argued, requires the ability to investigate questions about accuracy and integrity. Documented queries are what make this possible. A researcher with a complete documentation package can trace the process that produced any claim in the manuscript, identify the criteria that governed any search or screening decision, and explain why any particular framing was retained or revised. That is what the criterion demands. Unsystematic use cannot provide this; systematic use does. This is not a claim to a stronger form of accountability than criterion four already requires; it is a claim about what criterion four requires in a situation its original drafters did not anticipate. Memory-based reconstruction satisfies criterion four for traditional research because the researcher executed the work and can answer for it from recall; where AI executed the work, recall alone cannot do the same epistemic job.

### Boundary condition

Not every AI interaction constitutes query authorship. The concept requires that the query encode substantive intellectual commitments, and this sets a boundary that it is important to make precise.

Three markers distinguish a query that constitutes query authorship from one that does not. The first is scope logic: the query specifies what counts as in-scope and what counts as out-of-scope, and on what grounds. "Retain this abstract if it addresses AI use in empirical research practice; exclude if it addresses only AI ethics in general" encodes a scope commitment. "Summarise these abstracts for me" does not. The second is evaluative grounds: the query encodes the criterion against which the output will be judged — what would make the output correct, useful, or defensible. Without this, there is nothing to verify against. The third is recognisability of failure: the query is explicit enough that the researcher can recognise when the output is wrong, not merely when it is unexpected. A query that meets none of these markers is generic task delegation; a query meeting all three constitutes query authorship in the relevant sense.

This is also the line between systematic and unsystematic use, which I take up in the next section. Unsystematic use is precisely use in which the query encodes no explicit criteria, so no verification is possible, no failure is recognisable, and no intellectual commitment can be attributed to the researcher. The boundary condition is not a high bar; it requires genuine specification, not exhaustive specification. But some genuine specification is required.

---

## Systematic use as the condition for query authorship

### Three defining features

Query authorship is a claim about where the intellectual work lies. For that claim to be demonstrable — which ICMJE criterion four requires — the process that produced the work must be recoverable. This is what systematic use provides.

Systematic AI authorship has three defining features. The first is explicit criteria: the instructions given to the AI specify what to do and on what grounds, and those criteria are articulated before the tool is run, not constructed after the fact to justify the output. The second is human verification: at each stage where the AI produces an output, there is a specified checkpoint at which the researcher evaluates the output against the criteria before it passes to the next stage. The third is documented outputs: prompt configurations, screening rubrics, skill files, and decision logs are retained as artefacts that allow the process to be reconstructed and evaluated.

Without all three features, query authorship cannot be demonstrated. Explicit criteria without verification produces documented intentions that may not have governed the actual process. Verification without documentation produces quality control that cannot be examined retrospectively. Documentation without explicit criteria produces artefacts that record what happened but not what was supposed to happen — and therefore cannot show that the process was sound, only that it occurred.

### The systematic/unsystematic axis

Unsystematic AI use is characterised by the absence of these conditions. The researcher prompts without explicit criteria, refines the output until it is acceptable, and documents nothing. The criteria are entirely implicit; outputs are accepted without verification; no record is produced that would allow another researcher to assess what was done. The problem is not that this approach produces poor results on average — it may not. The problem is structural: the conditions for verifiable good work are absent. Errors are invisible, and choices cannot be attributed.

The systematic/unsystematic axis is orthogonal to the use/non-use axis that most current policy focuses on. A researcher using AI systematically may produce work that is more epistemically auditable than one relying on undocumented manual judgements — undocumented decisions about what is relevant, which sources are important, which arguments are coherent — that are equally invisible but have not attracted policy attention. The epistemic question is not whether AI was used; it is whether what was done can be evaluated.

The systematic approach is a spectrum. At one end is informal discipline — explicit criteria, retained configurations, session logs, but without formal pre-registration. At the other end, the full project setup — skill files, search protocols, screening rubrics, analytical specifications — is deposited with a public registry before outcomes are generated, providing a timestamped public commitment that strengthens the evidential value of the artefacts. Systematic AI use is compatible with both ends of this range; the workflow infrastructure supports exploratory and pre-registered work in the same structure.

Unsystematic use is not at one end of this spectrum. It is off the spectrum entirely. The absence of explicit criteria and documentation is not a minimal version of systematic use; it is categorically different, because errors cannot be detected and choices cannot be attributed. There is no gradient between systematic and unsystematic; the distinction is qualitative. This matters for policy: partial systematic use — explicit criteria for some stages, not others — is better than none, and should be recognised as such.

### Systematic use across the research pipeline

A systematic workflow has five stages: literature search and screening; empirical data and analysis; drafting; review; and documentation. At each stage the structure is the same: explicit input criteria, configured AI execution, human verification checkpoint, documented artefact. The transparency artefacts produced across all stages — boolean search strings, screening rubrics, skill files, prompt templates, session logs, analysis scripts, review records — constitute the documentation package.

*Literature search and screening.* A systematic literature workflow combines three routes: automated keyword searches across an open bibliographic database, semantic searches that retrieve papers regardless of keyword choices, and targeted manual retrieval for specific high-priority items. Each route catches what the others miss. Boolean search strings are documented in advance as explicit inclusion and exclusion criteria — not constructed post hoc — and the full search log is archived. Source synthesis uses a grounded AI tool: queries are submitted to a notebook containing only the relevant documents, and responses are cited from those documents. Unlike a general-purpose chatbot, this produces inline citations the researcher can verify; the synthesis query itself is an instance of query authorship. Human verification operates at each stage: spot-checking excluded records for false negatives, cross-checking synthesis outputs against their cited sources. Open bibliographic database APIs with explicit research-use permission are preferable to bulk export from subscription databases, whose institutional agreements may not cover computational analysis.

*Drafting and review.* A skill-configured style profile encodes explicit criteria for sentence rhythm, hedging calibration, paragraph structure, and rhetorical stance. Drafts are inputs to human revision, not outputs for direct use; the researcher reads, revises, accepts, or rejects each passage, exercising the judgement that makes the output theirs.

The review stage has three components, each addressing a failure mode the others do not. The first is colleague review — the primary external check. AI-assisted review is supplementary to this, not a substitute; what the structured approach provides is a better-prepared manuscript before it reaches human reviewers, weaknesses identified and addressed earlier. The second is a structured AI-reviewer skill run in a fresh session. The fresh-session requirement is critical: reviewing in a session with full prior project context biases the AI toward consistency with previous exchanges rather than independent critical assessment. Fresh-session design approximates the epistemic position of an external reviewer encountering the work cold. Adversarial configuration addresses the sycophancy problem directly: explicitly instructing the reviewer skill to be critical and raise objections, built into the persistent skill configuration, encodes a structural countermeasure against the confirmation bias that Cheng et al. (2026) document. The third component is cross-model persona review. Configured reviewer prompts — personas calibrated to specific likely critical positions — are run in fresh sessions across at least two models from different developers. A concern raised independently by two or more models is substantially more credible than one raised by only one; divergence across models on the same point signals genuine argumentative ambiguity rather than one model's tendency. The synthesis protocol for cross-model review is itself a documented artefact: act on objections raised independently by two or more models; flag for individual judgement objections raised by only one; note divergence as a signal of ambiguity; disregard sycophantic positive feedback.

*Empirical data and analysis.* The governing principle for primary empirical data is strict separation: the AI operates on the research context and on analysis scripts, not on the data itself. Raw data is immutable and excluded from the AI's working context entirely. The AI's role is to write, review, and document analysis code to a specification the researcher authors. Three zones govern what can and cannot reach the API: raw data with identifiers never does; pseudonymised data supports AI-assisted cleaning; anonymised analysis-ready data is unrestricted. The transparency artefacts for empirical work — analysis scripts, codebooks, data management protocols — are submitted as part of the documentation package. Detailed implementation guidance is in the supplementary materials.

### Project folder structure as epistemic infrastructure

The documentation artefacts produced across all stages must be findable, structured, and interpretable to be epistemically useful. A pile of artefacts with no structure is not meaningfully different from no artefacts: a reviewer who cannot locate the search log, or who cannot tell which prompt configuration corresponds to which draft version, cannot assess whether the process was sound. The structure is part of the epistemic argument.

A systematic workflow is supported by a project folder structure that makes the documentation package navigable and auditable:

```
project/
├── data/raw/             ← original data; immutable; excluded from AI context
├── data/processed/       ← analysis-ready files
├── scripts/              ← analysis code (R, Python, Stata)
├── outputs/              ← tables and figures
├── literature/           ← search logs, source sets, syntheses
├── notes/                ← working notes and argument sketches
├── draft/                ← manuscript versions with full edit history
├── logs/                 ← session decision logs and author-input files
└── supplementary/        ← documentation package materials
```

A configuration file at the project root encodes the research scope and key distinctions persistently, so every session starts with the same framing. A second specifies access controls — in particular, that `data/raw/` is excluded from the AI's context regardless of how the tool is used in a given session. A version-control repository timestamps every change, so session logs and author-input files can be verified as contemporaneous records rather than retrospective reconstructions. Together these structural elements are not organisational convenience; they are what makes the accountability claim in the documentation package auditable in practice.

---

## Externalising tacit knowledge: the epistemic dividend

### Systematic use forces externalisation

To direct the AI, the context must be specified. Before a search string is executed, the researcher must specify which concepts are in scope and which are not, and what constitutes relevance. Before a screening rubric is run, the researcher must articulate the inclusion criteria and the grounds for borderline cases. Before an analysis script is written, the researcher must specify which variables operationalise the theoretical concepts and which estimator fits the data structure. Before a reviewer configuration is submitted, the researcher must specify what standards of argument and evidence the work should meet. None of these specifications are novel — every careful researcher has views on all of these questions. What systematic AI use does is force their externalisation rather than their implicit, undocumented deployment.

The tacit knowledge at issue is not the kind associated with expert craft — motor and perceptual knowledge that resists verbal articulation, which Mitchell et al. (2022) term inherent tacit knowledge (Polanyi 1966; Collins 2001). It is closer to what Mitchell et al. call implicit tacit knowledge: the scope commitments, theoretical priorities, and evaluative standards that a practitioner could articulate if prompted but rarely does, because the opportunity to articulate them rarely arises. Systematic use creates that opportunity structurally, at every stage.

A related problem is what Gelman and Loken (2014) call the garden of forking paths: the cumulative effect of small, locally reasonable decisions that, undocumented, become invisible in hindsight. A researcher using AI without explicit criteria makes dozens of small acceptance decisions — this framing, this summary, this emphasis — each unremarkable in the moment and apparently inevitable in retrospect. Documented criteria at each stage prevent this post-hoc rationalisation, not by eliminating the decisions but by recording them at the time they were made.

### The pre-registration parallel

Systematic AI use instantiates the function of pre-registration: the criteria must be articulated before the tool is run, not constructed post hoc to justify what the tool returned. Pre-registration does not improve research only by constraining it; it improves research by making tacit commitments explicit and challengeable before outcomes are known. Systematic AI use does the same. Kosch and Feger's (2025) PARKing is precisely the failure mode that pre-specification forecloses: if the criteria are fixed before the tool is run, iterating prompts until the model returns a preferred result is not possible within the constraints of the workflow.

However, the analogy is one of function, not of form, and it is important to say so directly. Pre-registration's strongest epistemic property — the anti-manipulation guarantee — derives from public commitment: a protocol deposited with a registry before outcomes are generated cannot be altered without detection, because the timestamp is held by a third party. Private documentation does not provide this guarantee. Working logs can in principle be selectively retained; session records can be reconstructed to present a cleaned-up version of a messier process. The externalisation benefit — forcing explicit commitment to criteria before outcomes are known — survives in private documentation. The anti-manipulation benefit does not. If the distinction matters for the paper's evidentiary claims, it should be stated rather than elided.

This is not a fatal objection to the framework; it is a reason to seek the stronger form where possible. A timestamped documentation package pushed to a public repository at the outset — before data is collected, before searches are run, before analysis begins — provides evidence that the criteria preceded the outputs. Several artefacts that systematic use produces are natural candidates for formal pre-registration alongside a standard protocol: search strings, screening rubrics, and analytical specifications can be deposited with OSF or an equivalent registry before the work they govern is performed. This upgrades the framework's epistemic standing from externalisation to the stronger guarantee. Where this is impractical, the case for the framework rests on the externalisation function and the contemporaneous character of the working logs. Syed (2024) makes the related point that the epistemic argument for externalising decisions in advance applies equally to qualitative research and secondary data analysis, not only to confirmatory experimental work. The same applies here.

### Writing as thinking

The writing-as-thinking tradition provides a parallel perspective on what systematic use does and why it matters. Emig (1977) argues that writing is epistemically valuable because it forces deliberate semantics — the explicit structuring of logical relationships that tacit thought leaves implicit. Sommers (1981) frames the complement: revision is recursive discovery, not polishing. The writer finds meaning by finding a structure that fits it, and the structure of an argument is often discovered through the act of writing it rather than expressed from a prior specification. A researcher who is handed a pre-given structure to polish is doing something categorically different from one who discovers structure through composition.

Unsystematic AI use maps onto the failure Sommers describes: the AI does the structuring, and the researcher accepts the result. The deliberate semantics that would force articulation of what the argument is, and why the evidence supports it, are bypassed. The text may be fluent and coherent; it is not necessarily the researcher's.

Systematic AI use does not bypass this process — it relocates deliberate semantics to the specification layer. Writing a screening rubric, an inclusion criterion, or a reviewer configuration is not clerical work; it forces the researcher to articulate in explicit, structured form what would otherwise remain tacit. Through the act of writing the specification, the researcher often discovers that their prior criterion was ambiguous or inconsistently held; revising it in response is exactly the recursive discovery Sommers describes. This is the cognitive work that query authorship captures, and it is why systematic AI use does not bypass the deliberate semantics of writing but relocates them to the specification layer, where they simultaneously serve the argument and generate verifiable artefacts. Query authorship and writing-as-thinking are the same intellectual move applied at different sites — the specification and the manuscript paragraph — and in both cases the epistemic value lies in the externalisation of tacit structure into explicit form. Systematic use extends the hermeneutic circle; it does not replace it.

---

## The documentation package, open science infrastructure, and accountability

### What the documentation package is

Systematic use produces artefacts at each stage: boolean search strings, screening logs, skill files, prompt templates, session decision logs, author-input records, analysis scripts, codebooks. Together these constitute a documentation package. It is important to be precise about what this package is and what it is not.

It is not a replication package in the sense familiar from quantitative social science — the collection of code and data sufficient to reproduce a study's results. LLM outputs are not strictly reproducible: the same prompt, the same configuration, run against a later model version, may produce substantially different outputs. Non-determinism and silent model updates mean that bit-for-bit reproducibility of AI-assisted text is not a realistic standard.

What the documentation package certifies is something different and more important for the authorship question: that the criteria governing AI use were specified before the tool was run, and that the process was conducted as described. It provides the evidence from which a reader, reviewer, or editor can assess whether the researcher exercised the intellectual judgement that ICMJE criterion four demands. The documentation package must include the model version string alongside prompt templates and screening logs; without it, the documented process cannot be reproduced under even nominally equivalent conditions.

### The burden of evidence and the timestamp

In the absence of a documentation package, we must assume unsystematic use. This is not a punitive presumption. It is the same conservative prior that governs other open-science norms: if statistical code is not available, the study is assumed not independently replicable; if AI workflow artefacts are not available, the process is assumed unsystematic. The prior is symmetric across mechanisms. The choice to work without producing accountability artefacts is legitimate; so is the reader's inference from their absence.

A timestamped documentation package — pushed to a public repository at the outset of the project — is the strongest form of this evidence. It proves that the criteria preceded the outputs, which directly answers the question that the bullshit problem poses: is this demonstrably a truth-seeking process or not? Presence of a contemporaneously timestamped package licenses the inference of a truth-seeking process; absence licenses the inference of an unsystematic one. This is the connection between the opening warning and the policy prescription: the warning identifies what is at stake when the inference cannot be made; the documentation package is the instrument that makes it possible to make it.

Working logs that record the iterative texture of the process — including unsuccessful attempts, revised criteria, and decisions reversed — are substantially harder to retroactively sanitise than end-state outputs. This is part of their evidential weight. A clean supplementary file presenting the workflow as it was intended does not answer the accountability question in the way that contemporaneous logs presenting it as it actually unfolded do.

### Two tiers of artefacts

The documentation package has two tiers that serve distinct functions. Working logs — daily session records of decisions made, paired with author-input files written in first-person prose — are analogous to a lab notebook. Their evidential weight lies in their contemporaneous character and their recording of the iterative process, including what was tried and abandoned. The supplementary materials at submission — skill files, prompt templates, search scripts, screening logs — present the end-state artefacts in reusable, accessible form. Both are part of the package because they serve different purposes: the logs provide process integrity evidence; the supplement provides the materials needed to evaluate and, where appropriate, adapt the workflow.

Author-input files serve a specific function within the logs: they document the intellectual origin of the work session by session, recording which ideas and framings the researcher introduced, which redirections and corrections the researcher made, and which AI outputs were revised or rejected. This enables a CRediT-style account of who contributed what — evidence for ICMJE criterion two that goes beyond the formal declaration required of co-authors to include the researcher's own intellectual contributions as distinct from the AI's execution.

### What systematic use cannot guarantee

Three levels of epistemic claim about systematic use should be kept distinct.

The first is what the documentation package *certifies*: that criteria were specified before the tool was run, and that the process is legible to an outside reader. This is the primary claim, and it is what makes the accountability requirement in ICMJE criterion four satisfiable.

The second is what documentation *makes possible but does not certify*: whether the AI's execution of those criteria was accurate. This depends on the human verification checkpoints embedded in the workflow and on the competence of the researcher doing the verification. The framework is calibrated for researchers with deep domain expertise who can recognise when an AI output is wrong; for a researcher extending into a subfield outside their existing expertise, the framework's protections are thinnest exactly where the verification risk is highest. This is a genuine scope condition, not a defeater.

The third is what *no documentation regime can fully resolve*: non-deterministic AI outputs and silent model-weight changes within a nominally identical version string. The appropriate response to non-determinism is to log outputs alongside prompts and note when re-runs produce substantively different results. Documentation can be faked, as with any research record; what systematic documentation provides is evaluable artefacts rather than mere assertion, which makes fabrication more detectable. It does not make fabrication impossible.

The argument here is not that all AI use must be systematic, any more than the case for replication packages implies that all analysis must be automated. Researchers will continue to work exploratorily, to think while writing, and to let the process develop their thinking. What systematic AI authorship provides is not a constraint on how one works but evidence of how one worked. The same logic governs open science practices more broadly: if a hypothesis was not pre-registered, one must assume some degree of forking paths was possible; if code is not available, one must assume the study is not independently replicable; if AI workflow artefacts are not available, one must assume the process was unsystematic. These inferences are not certain, but the absence of evidence forces a conservative prior. The choice to work without producing accountability artefacts is a legitimate one; so is the reader's inference from their absence.

### Open science infrastructure

The transparency artefacts that systematic use produces have the formal properties open-science infrastructure already expects: they are shareable, versionable, depositable, and independently evaluable. A reviewer who receives a documentation package can assess whether the inclusion criteria were explicit before the search was run and whether the screening decisions are reproducible from the submitted materials. This is the same evaluation that reviewers of quantitative replication packages perform with statistical code and data. The cognitive and institutional infrastructure for this kind of review already exists in journals that require replication packages.

The Momeni et al. (2025) checklist for computational reproducibility in social science — developed with more than 180 social scientists — covers data documentation, source sharing, and methodological reporting. Systematic AI use satisfies these requirements naturally, as a byproduct of the workflow rather than as an additional compliance burden. Törnberg (2024) makes a related point about prompt stability analysis: testing whether minor prompt changes alter results is only possible if prompts are documented. Systematic use makes this possibility available by default; unsystematic use forecloses it. Freese and Peterson (2017) identify social science's engagement with open-science norms as incomplete; systematic AI use applied across the research pipeline produces exactly the kind of decision documentation whose absence they identify.

Zeng et al. (2025) find, across more than a thousand tasks in data science, that reproducibility correlates positively with accuracy — prompting strategies designed for reproducibility also produce better average results. If this generalises, systematic use is not merely a transparency mechanism but a quality mechanism. I suggest the logic is plausible: the same discipline that produces a precise inclusion criterion probably produces a better-executed search than vague prompting. This has not been demonstrated for social science specifically, and I present it as a hypothesis consistent with adjacent evidence rather than an established claim.

### Journals requiring replication packages already have the infrastructure

Journals that already require replication packages as a condition of publication have the deposition workflows, editorial review procedures, and author guidance that a documentation-based AI policy would use. Extending these norms to AI-assisted workflows requires no new principle. For a quantitative study, the replication package contains statistical code and data. For a study using a systematic AI workflow, it contains skill files, prompt templates, search scripts, and screening logs. The logic is identical; the content differs. Journals that have already accepted that logic have no principled basis for treating AI workflow documentation differently.

Peer review of AI-assisted work should be able to evaluate not just the existence of a documentation package but the quality of the systematic process it records — whether the configuration choices are theoretically justified, whether the verification procedures were appropriate, whether the scope decisions are consistent with the research question. This requires familiarity with systematic AI workflows that most current reviewers lack. It is worth noting that the same was true of statistical code review before replication packages became standard: the competence developed alongside the requirement.

---

## Policy implications

AI use in research is widespread (Grossmann et al. 2023), and how systematic it is remains largely unknown. In the absence of documentation artefacts, the conservative prior is that it is unsystematic; the same prior that applies to missing code or missing data applies here. This is the policy context.

Journals and publishers responded to the emergence of AI-assisted research rapidly and largely in good faith. The convergence on disclosure requirements — requiring authors to declare what AI was used and for what tasks — reflects a genuine attempt to address real concerns about accountability and attribution. Existing instruments have moved the field from silence to active guidance. The concession matters; the argument is about the instrument, not the intent. Tiered disclosure has begun to emerge as a more refined response: Jones (2025) proposes an explicit heuristic for disclosing AI use by task type, and Davidson and Karell (2025) develop an integration framework that specifies what AI did rather than merely whether it was used. These approaches represent genuine progress beyond binary permit-or-prohibit requirements. The systematic/unsystematic distinction proposed here is a further step along the same axis: the argument is for which principle should organise the tiering, and for a documentation package as its instrument.

The difficulty is that disclosure requirements, however sophisticated, do not distinguish systematic from unsystematic use. A researcher who built a documented, reproducible literature-search protocol with explicit criteria and human verification at each stage, and one who accepted unverified chatbot outputs without criteria or documentation, face the same disclosure requirement. Disclosure captures what was used and whether it was admitted; it does not capture the epistemic structure of the process. A disclosure that names AI use without specifying the epistemic structure of that use is a performance rather than a practice (Sibbald et al. 2025). Reporting checklists share this limitation. Zrubka et al. (2023), Holst et al. (2025), Agha et al. (2025), Mondal et al. (2025), and Ganjavi et al. (2024) have developed and assessed a range of these instruments; they address what was done and whether it was disclosed, not whether the process was epistemically sound.

SocArXiv's (2026) AI policy is a concrete illustration of partial progress. It distinguishes AI use by task type — which is an improvement over binary permit-or-prohibit approaches — but leaves the systematic/unsystematic axis invisible. Under SocArXiv's framework, a researcher with a fully documented criterion-governed literature search and one who accepted unverified chatbot summaries both pass on the acceptable side of the same distinction, provided both disclose.

Restrictive binary policies face a different problem: enforceability. AI detection tools are not sufficiently reliable to function as an enforcement mechanism. This means prohibitions operate largely on author compliance — an enforcement mechanism that disadvantages honest actors who disclose while leaving dishonest ones undetected. The perverse consequence is a policy that burdens the transparent and enables the opaque.

The policy directive I develop here follows from the authorship argument, not from a contested empirical diagnosis of policy failure. If researchers are already obligated to satisfy ICMJE authorship criteria — and they are — they are already obligated to be able to demonstrate what a documentation package certifies. The question journals should ask is therefore not "did you use AI?" but "can you show what you did?". Specifically: require a documentation package as a condition of publication for AI-assisted work, modelled on existing replication-package norms. The burden should scale with the complexity of use: minimal AI involvement generates minimal artefacts and imposes minimal requirements. But where AI use was consequential for the research design, analysis, or argument, the documentation package should be a submission requirement, not an optional supplement.

This shifts the evaluative burden to peer review, where it belongs. A reviewer who can examine a documentation package can assess whether the systematic process was appropriate — whether the configuration choices are theoretically justified, whether the verification procedures were adequate, whether the scope decisions are consistent with the research question. A reviewer who receives only a disclosure statement cannot make this assessment. The documentation package is what makes substantive review of AI-assisted work possible.

---

## Conclusion

I have argued the following. AI-assisted research creates a structural authorship problem: the human contribution becomes opaque, and without documentation, genuine accountability — in the sense ICMJE criterion four requires — is impossible. The locus of the human intellectual contribution in AI-assisted research is the query: search criteria, screening rubrics, analytical specifications, reviewer configurations. This is query authorship, and it is an established intellectual move, continuous with the specification-authored contribution that Krippendorff formalises for content analysis and that the writing-as-thinking tradition identifies at the level of deliberate semantics. What is new is the executor and its failure modes, not the principle. Systematic use — explicit criteria, human verification at each stage, documented outputs — is the condition under which query authorship can be demonstrated. It produces an epistemic dividend by externalising tacit knowledge before outcomes are known, instantiating the function of pre-registration without requiring its form. The documentation package it generates fits open-science infrastructure because it has the same formal properties — shareable, versionable, independently evaluable — that open science already requires of other research outputs. The policy directive follows: require documentation packages for AI-assisted work, ask not whether AI was used but whether the process can be shown.

The timestamped documentation package closes the question that the bullshit problem poses. In the absence of artefacts, we must assume unsystematic use — a truth-indifferent process whose outputs are indistinguishable from genuine scholarship without structural safeguards. In the presence of a contemporaneously timestamped package, we can infer a truth-seeking process: the criteria preceded the outputs; the work was verified; the researcher can account for it. No new principle is required. The extension of existing replication-package norms to AI-assisted workflows is the instrument. Journals that already require replication packages already have the infrastructure.

One scope note on this paper's own composition: it was systematic in infrastructure and more hermeneutic in argument development. The session logs, author-input files, reviewer skills, and documented literature-search pipeline were in place throughout and did real epistemic work. The conceptual moves — the authorship-first reframe, the query-authorship boundary condition, the foregrounded pre-registration concession — developed through the writing rather than from a pre-specified plan. This is what the spectrum framing predicts, and acknowledging it is not a concession. It is the demonstration that the framework's value does not depend on pre-registered rigidity.

---

## References

Abbott, Andrew. 2004. *Methods of Discovery: Heuristics for the Social Sciences*. New York: W. W. Norton & Company.

Agha, Riaz A., Ginimol Mathew, Rasha Rashid, Ahmed Kerwan, Ahmed Al-Jabir, Catrin Sohrabi, Thomas Franchi, Maria Nicola, Maliha Agha and TITAN Group. 2025. "Transparency in the Reporting of Artificial Intelligence — the TITAN Guideline." *Premier Journal of Science* 10: 100082.

Asher, Samuel, Jessica Persano, Janet Malzahn, Andrew C. W. Myers, Elliot Paschal, Andrew B. Hall. 2026. "Do Claude Code and Codex P-Hack? Sycophancy and Statistical Analysis in Large Language Models." Working paper. https://andrewbenjaminhall.com/asher_et_al_LLM_sycophancy.pdf

Barrie, Christopher, Alexis Palmer, and Arthur Spirling. 2025. "Replication for Language Models: Problems, Principles, and Best Practice for Political Science." Working paper. https://arthurspirling.org/documents/BarriePalmerSpirling_TrustMeBro.pdf

Cheng, Myra, Cinoo Lee, Pranav Khadpe, Sunny Yu, Dyllan Han, and Dan Jurafsky. 2026. "Sycophantic AI Decreases Prosocial Intentions and Promotes Dependence." *Science* 391 (1348): eaec8352. https://doi.org/10.1126/science.aec8352.

Collins, H. M. 2001. "Tacit Knowledge, Trust and the Q of Sapphire." *Social Studies of Science* 31 (1): 71–85.

Davidson, Tracy, and Daniel Karell. 2025. "Integrating Generative Artificial Intelligence into Social Science Research: Measurement, Prompting, and Simulation." *Sociological Methods & Research* 54 (3): 775–793.

Emig, Janet. 1977. "Writing as a Mode of Learning." *College Composition and Communication* 28 (2): 122–128.

Frankfurt, Harry G. 2005. *On Bullshit*. Princeton, NJ: Princeton University Press.

Freese, Jeremy, and David Peterson. 2017. "Replication in Social Science." *Annual Review of Sociology* 43: 147–165.

Ganjavi, Conner, Michael B. Eppler, Asli Pekcan, Brett Biedermann, Andre Abreu, Gary S. Collins, Inderbir S. Gill, and Giovanni E. Cacciamani. 2024. "Publishers' and Journals' Instructions to Authors on Use of Generative Artificial Intelligence in Academic and Scientific Publishing: Bibliometric Analysis." *BMJ* 384: e077192. https://doi.org/10.1136/bmj-2023-077192.

Gelman, Andrew, and Eric Loken. 2014. "The Statistical Crisis in Science." *American Scientist* 102 (6): 460–465.

Grossmann, Igor, Matthew Feinberg, Dawn C. Parker, Nichola A. Christakis, Philip E. Tetlock, and William A. Cunningham. 2023. "AI and the Transformation of Social Science Research." *Science* 380 (6650): 1108–1109.

Hicks, Michael Townsen, James Humphries, and Joe Slater. 2024. "ChatGPT Is Bullshit." *Ethics and Information Technology* 26 (2): 38.

Holst, Dirk, Keno Moenck, Julian Koch, Ole Schmedemann, and Thorsten Schüppstuhl. 2025. "Transparent Reporting of AI in Systematic Literature Reviews: Development of the PRISMA-trAIce Checklist." *JMIR AI* 4: e80247.

Jones, Kyle M. L. 2025. "Generative AI in Qualitative Research and Related Transparency Problems: A Novel Heuristic for Disclosing Uses of AI." *International Journal of Qualitative Methods* 24.

Kosch, Thomas, and Sebastian Feger. 2025. "Prompt-Hacking: The New p-Hacking?" arXiv preprint. [[2504.14571] Prompt-Hacking: The New p-Hacking?](https://arxiv.org/abs/2504.14571)  

Krippendorff, Klaus 2019. *Content Analysis: An Introduction to Its Methodology*. 4th ed. Thousand Oaks, CA: SAGE Publications.

Ludwig, Jens, Sendhil Mullainathan, and Ashesh Rambachan. 2024. "Large Language Models: An Applied Econometric Framework." arXiv preprint https://arxiv.org/abs/2412.07031

Mitchell, Vincent-Wayne, William S. Harvey Geoffrey Wood. 2022. "Where Does All the 'Know How' Go? The Role of Tacit Knowledge in Research Impact." *Higher Education Research & Development* 41 (5): 1664–1678. 

Momeni, Fakhri, Muhammad Taimoor Khan, Johannes Kiesel, and Tony Ross-Hellauer. 2025. "Checklists for Computational Reproducibility in Social Sciences: Insights from Literature and Survey Evaluation." In *Proceedings of the 3rd ACM Conference on Reproducibility and Replicability (ACM REP '25)*, 179–191.

Mondal, Himel, Sheikat Mondal, and Joshil Kumar Behera. 2025. "Artificial Intelligence in Academic Writing: Insights from Journal Publishers' Guidelines." *Perspectives in Clinical Research* 16 (1): 56–57. 

Peters, Uwe, and Benjamin Chin-Yee. 2025. "Generalization Bias in Large Language Model Summarization of Scientific Research." *Royal Society Open Science* 12: 241776. https://doi.org/10.1098/rsos.241776.

Polanyi, Michael. 1966. *The Tacit Dimension*. Chicago: University of Chicago Press.

Pruschak, Gernot, and Christian Hopp. 2022. "And the credit goes to … - Ghost and honorary authorship among social scientists." *PLoS ONE* 17(5): e0267312.

Retraction Watch. 2023. "Hindawi Reveals Process for Retracting More Than 8,000 Paper Mill Articles." December 19, 2023. https://retractionwatch.com/2023/12/19/hindawi-reveals-process-for-retracting-more-than-8000-paper-mill-articles/.

Sibbald, Kaitlin R., Shanon K. Phelan, Brenda L. Beagan, and Tara M. Pride. 2025. "Positioning Positionality and Reflecting on Reflexivity: Moving from Performance to Practice." *Qualitative Health Research*, onlineFirst, doi:[10.1177/10497323241309230](https://doi-org.ezproxy.uio.no/10.1177/10497323241309230)

SocArXiv. 2026. "AI Policy." Center for Open Science. March 8, 2026. https://socopen.org/ai-policy/.

Sommers, Nancy. 1981. "Intentions and Revisions." *Journal of Basic Writing* 3 (3): 41–49.

Syed, Moin. 2024. "Three Persistent Myths about Open Science." *Journal of Trial and Error* 4 (2): 32–45. https://doi.org/10.36850/mr11.

Törnberg, Petter. 2024. "Best Practices for Text Annotation with Large Language Models." *Sociologica* 18 (2): 67–85.

Zeng, Qiuhai, Claire Jin, Xinyue Wang, Yuhan Zheng and Qunhua Li. 2025. "AIRepr: An Analyst-Inspector Framework for Evaluating Reproducibility of LLMs in Data Science." In *Findings of the Association for Computational Linguistics: EMNLP 2025*. 

Zrubka, Zsombor, Levente Kovács, Hossein Motahari Nezhad, János Czere, László Gulácsi, Márta Péntek 2023. "Artificial Intelligence in Medicine: A Systematic Review of Guidelines on Reporting and Interpreting Studies." Preprint. 

---

## Notes

[^1]: The documentation burden scales with the complexity of AI use. Minimal use — grammar polishing, vocabulary suggestions, light restructuring — generates minimal artefacts and imposes minimal requirements. The framework does not disadvantage researchers who use AI lightly and transparently.

[^2]: International Committee of Medical Journal Editors

[^3]: More elaborate practitioner implementations of the same structured approach exist. Sant'Anna (n.d.) describes a Claude Code research workflow featuring twenty-eight configured reviewer skills, fourteen specialised agents, automated quality gates, and AEA replication standards compliance, framed explicitly as a "ceiling, not floor" with documented entry points for new adopters (https://psantanna.com/claude-code-my-workflow/workflow-guide.html). The workflow described in this paper is intentionally minimal. [**Author flag**: Sant'Anna's multi-agent design involves a degree of automation — agents executing sequentially with minimal human intervention between stages — that may sit in tension with this paper's emphasis on human verification at each stage. The artefacts are documented, but the human-in-the-loop principle is differently implemented. Review before submission and decide whether to cite, qualify, or drop.], *Recommendations for the Conduct, Reporting, Editing, and Publication of Scholarly Work in Medical Journals*, updated annually. Available at icmje.org.
