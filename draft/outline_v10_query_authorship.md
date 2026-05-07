# Outline: Query Authorship and Systematic AI Use in Social Science

*Working outline for v10 — developed from review and restructuring session, 2026-05-06*
*Source draft: v9_draft_socarxiv.md*

---

## Framing note

The central reframe from v9: the paper is no longer primarily a policy diagnosis (disclosure requirements have failed) but an authorship argument (here is what authorship requires when AI is involved, and here is what follows from that). The policy implications are derived from the authorship argument, not from a contested empirical diagnosis of policy failure. The Hindawi/bullshit material functions as a motivating warning, not as evidence of policy failure.

---

## Introduction

- AI can produce large volumes of plausible text at low cost; its adoption in research is widespread and will not be reversed
- This creates a specific problem: the human contribution to the research product becomes opaque — not only to readers but potentially to reviewers, editors, and the researchers themselves
- Existing institutional responses have converged on disclosure requirements and reporting checklists; none address the epistemic structure of the research process itself [one sentence situating the checklist literature — Zrubka et al., PRISMA-trAIce, TITAN, Mondal et al., Ganjavi et al.]
- The argument proceeds in [N] steps: [explicit roadmap, in the style of v9's five-move structure, updated to match new outline]
- Scope: the argument is directed at social science research involving text-heavy and empirical work; systematic review has its own established protocols

---

## 1. What AI does to authorship

### 1.1 The authorship problem
- AI can generate plausible academic text across the full research pipeline — literature synthesis, analytical interpretation, drafting, review
- When the text is AI-generated, the question of what the human researcher contributed becomes genuinely open
- This is not primarily a fraud problem; it is an authorship problem — the conditions for claiming authorship may not be met even where no deception is intended

### 1.2 The bullshit warning
- At scale, AI-assisted work risks being indistinguishable from fabrication — not because researchers intend to deceive, but because a truth-indifferent generator leaves no trace of whether a truth-seeking process occurred
- Frankfurt (2005) / Hicks et al. (2024): LLMs optimise for plausible continuation, not for truth — structurally closer to Frankfurt's bullshitter than to a liar
- The Hindawi/Wiley episode (8,000+ retractions, 2022–23): what industrial-scale plausible-text production looks like when it reaches the scholarly record — the warning of what unchecked AI use could produce
- The failure mode in unsystematic AI use is directional, not random: sycophancy, generalisation bias, PARKing (Cheng et al. 2026; Peters & Chin-Yee 2025; Kosch & Feger 2025; Asher et al. 2026; Barrie et al. 2025; Ludwig et al. 2024) — the tool confirms rather than challenges, overstates rather than accurately reports
- The question the paper addresses: how can a researcher demonstrate that their AI-assisted work is genuinely the product of a truth-seeking process?

### 1.3 ICMJE criterion 4 as the accountability standard
- Scholarly authorship has an established standard; the ICMJE criteria require substantial intellectual contribution to conception or design; critical revision; final approval; and accountability for all aspects of the work
- Criterion 4 is the sharpest: to be genuinely accountable, the researcher must be able to investigate questions about accuracy and integrity, explain why decisions were made, and show that the process was sound
- Where AI executed the work, recall alone cannot do this epistemic job — the researcher who accepted AI outputs without documentation cannot satisfy criterion 4 in any substantive sense
- This gives policy a more tractable question than "was AI used?": can the researcher demonstrate that authorship criteria are met?

---

## 2. Query authorship: the human contribution in AI-assisted research

### 2.1 Where the intellectual work sits
- The intellectual contribution in AI-assisted work lies in the query: the search criteria, screening rubrics, analytical specifications, reviewer configurations — the instructions that shape what the AI does
- Abbott (2004): the core creative act in social science is the heuristic move — the framing of a problem, the selection of an angle, the constraint of what follows; execution is not where the intellectual work sits
- Krippendorff (2019): rigorous coding instructions are designed so that coders are interchangeable — the analyst's contribution is formalised in the analytical construct. LLM query authorship is the next step in that lineage, not a departure from it
- What changes with LLMs is not the principle but the failure modes of the executor: sycophancy, generalisation bias, non-determinism — which is precisely why documentation and verification requirements are specific to systematic AI use

### 2.2 Query authorship satisfies the ICMJE criteria
- Criterion 1 (conception and design): designing a search strategy, specifying inclusion and exclusion criteria, formulating synthesis questions, configuring a reviewer skill are acts of conception and design in the relevant sense
- Criterion 2 (critical revision): author-input files document session by session what the researcher directed, redirected, and rejected — this is critical revision of the work, not passive acceptance of AI output
- Criterion 4 (accountability): documented queries are what make genuine accountability possible — the researcher can trace the process that produced the version they approved and stand behind it

### 2.3 Boundary condition
- The query must encode substantive intellectual commitments to constitute authorship in the relevant sense
- The distinction is between substantive intellectual specification and generic task delegation: "retain this abstract if it addresses AI use in empirical research practice; exclude if it addresses only AI ethics in general" is query authorship; "summarise these abstracts for me" is not
- This is also the line between systematic and unsystematic use — the topic of the next section

---

## 3. Systematic use as the condition for query authorship

### 3.1 Three defining features
- Systematic AI authorship has three defining features:
  - **Explicit criteria**: the instructions specify what to do and on what grounds, before the tool is run
  - **Human verification**: at each stage where the AI produces an output, there is a specified human checkpoint where the output is evaluated against the criteria before it passes to the next stage
  - **Documented outputs**: prompt configurations, screening rubrics, skill files, and decision logs are retained as artefacts that allow the process to be reconstructed and evaluated
- Without all three, query authorship cannot be demonstrated — the criteria that would show the researcher shaped the work are absent or unverifiable

### 3.2 The systematic/unsystematic axis
- Unsystematic AI authorship: prompting without explicit criteria, refining until an acceptable output is produced, no documentation — the conditions for verifiable good work with AI are structurally absent
- The systematic/unsystematic axis is orthogonal to the use/non-use axis that current policy focuses on — a researcher using AI systematically may produce more epistemically auditable work than one relying on undocumented manual judgements
- The systematic approach is a spectrum; the unsystematic approach is off the spectrum — the absence of explicit criteria and documentation is not a minimal version of systematic use but something categorically different, because errors cannot be detected and choices cannot be attributed

### 3.3 Systematic use across the research pipeline
- A systematic workflow has five stages: literature search and screening; empirical data and analysis; drafting; review; documentation
- At each stage the structure is the same: explicit input criteria → configured AI execution → human verification checkpoint → documented artefact

**Literature search and screening**
- Boolean search strings documented in advance as explicit inclusion/exclusion criteria — not constructed post hoc
- Three routes combined: automated keyword searches, semantic searches, targeted manual retrieval — each catching what the others miss
- Source synthesis using a grounded AI tool (queries submitted to a notebook of relevant documents only, not a general-purpose chatbot) — produces inline citations the researcher can verify
- Human verification: spot-checking excluded records for false negatives, cross-checking synthesis outputs against cited sources
- Open bibliographic database APIs with explicit research-use permission preferable to bulk export from subscription databases (institutional agreements may not cover computational analysis)

**Drafting and review**
- Skill-configured style profile encodes explicit criteria for sentence rhythm, hedging calibration, paragraph structure — drafts are inputs to human revision, not outputs for direct use
- Review-and-revise stage: three components addressing failure modes the others do not — (1) colleague review as primary external check; (2) structured AI-reviewer skill in a fresh session (fresh-session requirement critical: prevents context bias, approximates external reviewer position); (3) cross-model persona review run across at least two models from different developers — convergence across models is stronger evidence of a real weakness than any single system's output; divergence signals genuine ambiguity
- Adversarial configuration addresses the sycophancy problem: explicitly instructing the reviewer skill to be critical, built into the persistent skill configuration, encodes a structural countermeasure against confirmation bias (Cheng et al. 2026)
- Synthesis protocol for cross-model review is itself a documented artefact: act on objections raised by two or more models; flag for individual judgement objections raised by only one; note divergence as signal of genuine ambiguity; disregard sycophantic positive feedback

**Empirical data and analysis** *(compressed; detail in supplementary materials)*
- Governing principle: strict separation — AI operates on research context and analysis scripts, not on primary data
- Three-zone data model: raw data with identifiers never sent to API; pseudonymised data supports AI-assisted cleaning and variable construction; anonymised analysis-ready data unrestricted
- Analysis scripts written to a researcher-authored specification; numbered sequentially; each with a header specifying inputs, outputs, and purpose

### 3.4 Project folder structure as epistemic infrastructure
- A structured project folder is not merely organisational housekeeping — it is what makes the documentation package auditable in practice
- A pile of artefacts with no structure is not meaningfully different from no artefacts: the structure is part of the epistemic argument

```
project/
├── data/
│   ├── raw/                  ← original data; immutable; excluded from AI context
│   └── processed/            ← analysis-ready files
├── scripts/                  ← analysis code (R, Python, Stata)
├── outputs/                  ← tables and figures
├── literature/               ← search logs, source sets, syntheses
├── notes/                    ← working notes and argument sketches
├── draft/                    ← manuscript versions with full edit history
├── logs/                     ← session decision logs and author-input files
└── supplementary/            ← documentation package materials
```

- Configuration files at the project root: one encodes research scope and key distinctions (persistent context for every session); one specifies access controls (data/raw/ excluded from AI context by default)
- Version-control repository timestamps every change — session logs and author-input files can be verified as contemporaneous records rather than retrospective reconstructions

---

## 4. Externalising tacit knowledge: the epistemic dividend

### 4.1 Systematic use forces externalisation
- To direct the AI, the context must be specified: before a search string is executed, before a screening rubric is run, before an analysis script is written — the researcher must articulate decisions that would otherwise remain tacit
- The tacit knowledge at issue is what Mitchell et al. (2022) call implicit tacit knowledge: scope commitments, theoretical priorities, evaluative standards that a practitioner could articulate if prompted but rarely does
- Writing a screening rubric, an inclusion criterion, or a skill configuration is not clerical work — it forces deliberate semantics, the explicit structuring of logical relationships that tacit thought leaves implicit (Emig 1977)
- Sommers (1981): revision is recursive discovery, not polishing — the researcher often discovers through the act of writing the specification that their prior criterion was ambiguous or inconsistently held. This is the cognitive work query authorship captures

### 4.2 The pre-registration parallel
- Systematic AI use instantiates the function of pre-registration: the criteria must be articulated before the tool is run, not constructed post hoc to justify what the AI returned
- Pre-registration does not improve research only by restricting it but by making tacit commitments explicit and challengeable before outcomes are known — systematic AI use does the same
- Kosch and Feger's (2025) PARKing (Prompt Adjustments to Reach Known Outcomes) is precisely the failure mode that pre-specification forecloses
- Gelman and Loken (2014) garden of forking paths: documented criteria at each stage prevent post-hoc rationalisation of AI-accepted outputs
- Syed (2024): the epistemic argument for externalising decisions in advance applies equally to secondary data analysis, qualitative work, and literature synthesis — not only confirmatory experimental research
- Pre-registration of the systematic workflow: where the research design permits, the systematic AI protocol can be pre-registered alongside a standard pre-registration — a public timestamp that strengthens the evidential value of the artefacts. Several artefacts (search strings, screening rubrics, analytical specifications) are natural candidates for pre-registration

### 4.3 Writing as thinking
- The writing-as-thinking tradition (Emig 1977; Sommers 1981): writing is epistemically valuable because it forces deliberate semantics — explicit structuring of logical relationships that tacit thought leaves implicit
- Unsystematic AI use maps directly onto the failure Sommers describes: the AI does the structuring and the researcher accepts the result, bypassing the deliberate semantics that would force articulation of what the argument is and why the evidence supports it
- Systematic AI use does not bypass this cognitive process — it relocates deliberate semantics to the specification layer, where they simultaneously serve the argument and generate verifiable artefacts

---

## 5. The documentation package, open science infrastructure, and accountability

### 5.1 What the documentation package is
- Systematic use produces artefacts across the research pipeline: boolean search strings, screening logs, skill files, prompt templates, session decision logs, author-input records
- These constitute a **documentation package** — not a replication package, because LLM outputs are not strictly reproducible (non-determinism; model-version change): the same workflow run against a later model version may produce substantially different outputs
- What the documentation package certifies: that the criteria governing AI use were specified before the tool was run, and that the process was conducted as described
- The documentation should include the model version string alongside prompt templates and screening logs — without the version string the documented process cannot be reproduced under equivalent conditions

### 5.2 The burden of evidence and the timestamp
- In the absence of a documentation package, we must assume unsystematic use — the burden of evidence runs in one direction
- This is not a punitive inference; it is the same conservative prior that governs other open science norms: if code is not available, the study is assumed not independently replicable; if AI workflow artefacts are not available, the process is assumed unsystematic
- A timestamped documentation package — pushed to a public repository at the outset — is the strongest form: it proves the criteria preceded the outputs, directly answers the bullshit question (this is demonstrably a truth-seeking process), and provides evidence analogous to pre-registration's epistemic function
- Working logs that record iterative process — including unsuccessful attempts and revised criteria — are substantially harder to retroactively sanitise than end-state outputs; the contemporaneous character is part of their evidential weight

### 5.3 Two tiers of artefacts
- **Working logs**: daily session records of decisions made, paired with author-input files written in first-person prose — analogous to a lab notebook; evidential weight lies in contemporaneous character and recording of iterative process
- **Supplementary materials**: skill files, prompt templates, search scripts, screening logs — end-state artefacts in reusable, accessible form
- Author-input files document session by session what the researcher directed, redirected, and rejected — enabling a CRediT-style account of human contribution (ICMJE criterion 2); what ideas and framings originated with the researcher; which redirections and corrections the researcher made

### 5.4 What systematic use cannot guarantee
- Documentation can be faked, as with any research record; what systematic documentation provides is evaluable artefacts rather than mere assertion — fabrication is more detectable
- Non-determinism is a practical challenge: the appropriate response is to log outputs alongside prompts, note when re-runs produce substantively different results, and treat AI output as input to human judgement rather than as a final product
- The documentation package does not guarantee quality or eliminate errors; it is a necessary condition for the kind of quality control that makes errors detectable

### 5.5 Open science infrastructure
- The transparency artefacts produced by systematic AI use have the formal properties open science infrastructure already requires: shareable, versionable, depositable, independently evaluable
- A reviewer who receives a documentation package can assess whether the inclusion criteria were explicit before the search and whether the screening decisions are reproducible from the submitted materials — the same evaluation that reviewers of quantitative replication packages perform with statistical code and data
- Momeni et al. (2025) checklist for computational reproducibility in social science: systematic AI use satisfies these requirements naturally — as a byproduct of the workflow, not as an additional burden
- Freese and Peterson (2017): social science's engagement with open science norms is incomplete; systematic AI use applied across the research pipeline produces exactly the kind of decision documentation identified as missing
- Törnberg (2024): prompt stability analysis — testing whether minor prompt changes alter results — is only possible if prompts are documented; systematic use makes this possibility available by default
- Zeng et al. (2025): across 1,032 tasks in data science, reproducibility correlates positively with accuracy — systematic use is not merely a transparency mechanism but plausibly a quality mechanism; this has not been demonstrated for social science specifically, but the adjacent evidence does not support the assumption of a trade-off

### 5.6 Journals requiring replication packages already have the infrastructure
- Journals that already require replication packages have the deposition workflows, editorial review procedures, and author guidance that a documentation-based AI policy would use
- Extension to AI workflows requires no new principle and no new infrastructure
- Peer review of AI-assisted work should be able to evaluate the quality of the systematic process, not simply its existence — whether the configuration choices are theoretically justified and accountable; this requires familiarity that most current reviewers lack, but so did statistical code review before replication packages became standard

---

## 6. Policy implications

- AI use is widespread (Grossmann et al. 2023); how systematic it is, is unknown — and in the absence of artefacts, must be assumed unsystematic
- The right question for journals is not "did you use AI?" but "can you show your systematic process?"
- **Require documentation packages** as a condition of publication for AI-assisted work, modelled on existing replication package norms
- The documentation burden scales with the complexity of AI use: minimal AI use (grammar polishing with human review) generates minimal artefacts; the requirement does not disadvantage researchers who use AI lightly and transparently
- Binary disclosure requirements treat systematic and unsystematic use identically and give readers no actionable information about epistemic quality [brief note on existing checklist literature: Zrubka et al., PRISMA-trAIce, TITAN, Mondal et al., Ganjavi et al. — these instruments address what was used and whether it was disclosed; none address the epistemic structure of the process that produced the work]
- SocArXiv (2026) as a concrete illustration of a partial move in the right direction: distinguishes by task but leaves the systematic/unsystematic axis invisible — a researcher with a documented criterion-governed literature search and one who accepted unverified chatbot outputs both pass on the acceptable side of the same distinction
- Restrictive binary policies face an inherent enforceability gap: AI detection tools are not sufficiently reliable, meaning prohibitions function largely on author compliance — an enforcement mechanism that disadvantages honest actors while leaving dishonest ones undetected
- The policy directive follows from the authorship argument, not from a contested diagnosis of policy failure: if researchers are already obligated to meet ICMJE authorship criteria, they are already obligated to be able to demonstrate what the documentation package certifies

---

## 7. Conclusion

- Systematic AI use and query authorship together constitute a genuinely defensible research practice: the human is demonstrably the author, the process is accountable, and the artefacts are evaluable
- I have argued that [explicit "I have argued" sequencing recapping the chain: authorship problem → query authorship → systematic use as condition → epistemic dividend of externalisation → documentation package → policy]
- The timestamped documentation package closes the bullshit question: absence of artefacts licenses the inference of unsystematic use; presence of artefacts licenses the inference of a truth-seeking process
- The policy directive follows from the authorship argument: journals should not ask "did you use AI?" — a question that is unenforceable and answers the wrong question — but "show us your systematic process"
- No new principle and no new infrastructure is needed: the extension of existing replication package norms to AI-assisted workflows is the policy instrument, and journals that already require replication packages already have the infrastructure to implement it
- Scope note on this paper's own composition [as in v9]: systematic in infrastructure and more hermeneutic in argument development — the conceptual moves developed through the writing rather than from a pre-specified plan; acknowledging this is not a concession but a demonstration that the framework's value does not depend on pre-registered rigidity

---

## Materials note

- Empirical data and security section from v9: moved to supplementary materials; the argument does not depend on it and the detail is implementation guidance rather than argument
- Replication package / documentation package for this paper: https://github.com/torbskar/structured-use-of-AI

---

---

# Session log: Restructuring conversation, 2026-05-06

## Purpose of this log

This log records the decisions made in a restructuring conversation between Torbjørn Skardhamar and Claude (Sonnet 4.6, claude.ai) on 2026-05-06. The conversation produced the outline above. The log is intended for use in a future session as a handoff document — providing enough context to continue the work without re-litigating decisions already made.

**Note on session design**: Using a fresh Claude session for this restructuring conversation was a conscious methodological decision by Torbjørn. The review of v9 (also conducted in a fresh session) identified structural weaknesses in the paper's argumentative architecture. A fresh session for the restructuring work approximates the position of an external reader encountering the argument without prior context bias — consistent with the paper's own argument about the epistemic value of fresh-session review. The decisions recorded here are therefore themselves an instance of the systematic workflow the paper describes.

---

## Starting point

**Source manuscript**: v9_draft_socarxiv.md (2026-05-04)  
**Target journal at time of review**: *Sociological Methods & Research* (Torbjørn subsequently decided to set journal targeting aside and reconsider after restructuring)

**Review finding that triggered the restructuring**: The v9 structure opened with a policy diagnosis (disclosure requirements are insufficient) and then introduced the conceptual framework (systematic/unsystematic, query authorship) as the basis for a prescription. The diagnosis was under-evidenced: the paper argued current policies had *failed* but supplied only analytical arguments about why they *could* fail. The paper's strongest and most novel contribution — the ICMJE criterion 4 analysis — was buried late in a long section.

---

## Key decisions

### 1. Reframe as an authorship argument, not a policy diagnosis

**Decision**: The paper's central move is now: *here is what authorship requires when AI is involved* → *here is what that implies for research practice* → *here is what that implies for policy*. The policy implications are derived from the authorship argument, not from a contested empirical diagnosis of policy failure.

**Rationale**: The argumentative chain becomes deductive rather than diagnostic, which avoids the evidentiary problem with the diagnosis and better matches the paper's actual intellectual contribution.

### 2. Hindawi/bullshit material repositioned as a warning, not as evidence

**Decision**: The Hindawi/Wiley retraction episode and the Frankfurt/bullshit argument function as a motivating warning — what unchecked AI use could produce at scale — not as evidence that current disclosure policies have failed.

**Rationale**: The review identified the honesty-pledge argument (in v9) as the paper's most exposed logical flaw. Repositioning these materials as a warning sidesteps that flaw while retaining the rhetorical force.

### 3. ICMJE criterion 4 analysis promoted

**Decision**: The ICMJE analysis — particularly criterion 4 (genuine accountability) — is foregrounded as the paper's sharpest original contribution. It anchors section 1 (as the institutional standard that makes the authorship problem precise) and section 2 (as what query authorship satisfies). It was buried in v9; it now drives the argument.

### 4. Query authorship as the organising concept

**Decision**: Query authorship is the paper's primary conceptual contribution and is introduced in section 2, after the authorship problem is established. The boundary condition — the query must encode substantive intellectual commitments, not just generic task delegation — is made explicit.

**Rationale**: In v9, query authorship was introduced alongside several other moves and did not clearly drive the argument. In the reframed version, it is the concept from which systematic use, the documentation package, and the policy implications all follow.

### 5. Systematic use as the condition for query authorship (section 3), including the workflow

**Decision**: The workflow section from v9 is folded into section 3 (systematic use), not treated as a standalone section. The folder structure and project configuration are presented as part of the epistemic argument — a structured documentation package is auditable; a pile of artefacts is not.

**Rationale**: Torbjørn's explicit decision: "You do not only need each artifact, but you need to put them somewhere to work. A pile in the top folder would be a mess and harder to audit. So this belongs to §3." The workflow section may be compressed relative to v9.

### 6. Pre-registration mentioned in two places

**Decision**: Pre-registration appears (a) in section 4 (externalising tacit knowledge), as the epistemic parallel — systematic AI use instantiates the function of pre-registration by forcing commitment before outcomes are known; and (b) in section 3 (systematic workflow), as a practical option — several artefacts (search strings, screening rubrics, analytical specifications) are natural candidates for pre-registration alongside a standard protocol. A timestamped documentation package (pushed to a public repository at the outset) is the strongest form and provides evidence analogous to pre-registration's epistemic function.

### 7. The timestamp and the bullshit question

**Decision**: The timestamp logic is central to section 5 (documentation package). In the absence of artefacts, we must assume unsystematic use. A timestamped documentation package proves the criteria preceded the outputs, directly answers the bullshit question, and provides the evidentiary analogue of pre-registration. This binds the opening warning (bullshit production) to the closing policy prescription (require documentation packages).

**Torbjørn's formulation**: "Do we know it is real science or could it be bullshit? That should not be an open question."

### 8. Sections 5 and 6 combined

**Decision**: The documentation package (what it is, what it certifies) and the open science infrastructure (how it fits existing norms) are combined into one section (section 5), moving from one to the other. They are closely related and gain from being read as a continuous argument rather than as separate sections.

### 9. Checklist literature compressed

**Decision**: The checklist literature (Zrubka, PRISMA-trAIce, TITAN, Mondal et al., Ganjavi et al.) is compressed to (a) one sentence in the introduction situating existing institutional responses, and (b) a short paragraph in section 7 (policy implications). It establishes the policy context but does not drive the argument in the reframed version.

### 10. Empirical data and security section moved to supplementary materials

**Decision**: The empirical data/security section from v9 is moved to supplementary materials. It is implementation guidance rather than argument, and the paper's argument does not depend on it in the reframed version.

**Torbjørn's assessment**: "The section on empirical data and security might no longer be as relevant."

### 11. Journal targeting deferred

**Decision**: Journal targeting (SMR vs. *Sociological Science* vs. other) is set aside during the restructuring. Torbjørn will reconsider once the reframed structure is clearer.

---

## Open questions carried forward

- **ICMJE analysis position**: Confirmed as opening anchor of section 1 and closing payoff of section 2 — both placements are used in the outline above.
- **Documentation burden objection**: Addressed in section 7 — the burden scales with complexity of AI use; minimal use generates minimal artefacts.
- **Sections 5 and 6 boundary**: Confirmed combined; the infrastructure point is the closing move within the combined section.

---

## What can be reused from v9

Most of v9's prose can be reused; the reframing is structural, not wholesale. Sections requiring the most rewriting are the introduction (new problem motivation) and the conclusion (updated to follow the authorship argument chain). The workflow material, the open science discussion, the Frankfurt/bullshit passage, the Kosch/Feger PARKing material, the Emig/Sommers writing-as-thinking passage, and the ICMJE analysis can all be carried forward with repositioning and modest revision.
