# Outline: Query Authorship and Systematic AI Use in the Social Sciences

**Status**: Working outline for v10 — derived from `draft/outline_v10_query_authorship.md` (2026-05-06 restructuring).
**Predecessor**: `outline_old.md` (v9 outline, archived 2026-05-06).
**Source draft for prose reuse**: `draft/v9_draft_socarxiv.md`.
**Review that motivated the reframe**: `draft/v9_draft_review.md`.

---

## Core argument (one sentence)

What authorship requires when AI is involved is documentable query authorship under systematic use; the policy implications follow from the authorship argument, not from a contested empirical diagnosis of policy failure.

---

## Framing note

The central reframe from v9: the paper is no longer a policy diagnosis (disclosure has failed) but an authorship argument (here is what authorship requires when AI is involved, and here is what follows). The Hindawi/bullshit material functions as a motivating warning, not as evidence. The policy directive is derived deductively from the authorship argument and the ICMJE criteria, not inductively from a contested empirical claim about policy failure.

---

## Material disposition

Three things from v9 are explicitly removed from the main argument:

- **Cut**: the honesty-pledge / Ariely retraction argument (v9 Introduction). The v9 review identified this as the paper's most exposed logical error — one retraction does not invalidate a behavioural hypothesis. Not reframable; remove entirely.
- **Moved to supplementary materials**: empirical-data-and-security section (v9 §4.3, including the three-zone data model, Presidio PII scanning, GDPR specifics). Implementation guidance, not argument. The argument's core principle (strict separation of AI from primary data) is preserved at one-sentence level in §3.3.
- **Compressed**: the checklist literature (v9 §2 "AI in research: existing literature"). Reduced to one sentence in the Introduction (situating existing institutional responses) and one paragraph in §6 (policy implications). The gap identified by v9 — no framework treats systematic/unsystematic as the policy axis — survives; the survey is condensed.

---

## Word-count allocation (SMR discipline preserved)

Body target ~7,800 words; references ~1,200 words; total ~9,000 (≈500 words headroom under SMR's 10,000-word ceiling).

| Section | Target words |
|---|---|
| Introduction | 700 |
| §1 What AI does to authorship | 1,100 |
| §2 Query authorship | 900 |
| §3 Systematic use as condition for query authorship | 1,800 |
| §4 Externalising tacit knowledge | 900 |
| §5 Documentation package + open science infrastructure | 1,400 |
| §6 Policy implications | 600 |
| §7 Conclusion | 400 |
| **Body total** | **7,800** |
| References | ~1,200 |
| **Grand total** | **~9,000** |

§3 is the largest section because it absorbs v9's standalone workflow section, but compressed substantially relative to v9's ~3,500 workflow words.

---

## Introduction

**Function**: Establish the authorship problem; preview the chain. Open with the fact of AI uptake, not with policy failure. The reader should feel the authorship question is genuinely open before the paper's contribution is introduced.

- AI can produce large volumes of plausible academic text at low cost; its adoption in research is widespread (cite Grossmann et al. 2023) and will not be reversed.
- This creates a specific problem for scholarship: the human contribution to the research product becomes opaque — not only to readers and reviewers but potentially to the researchers themselves.
- Existing institutional responses have converged on disclosure requirements and reporting checklists; none address the epistemic structure of the research process itself. *(One sentence situating the checklist literature: Zrubka et al., PRISMA-trAIce, TITAN, Mondal et al., Ganjavi et al.)*
- The argument proceeds in seven steps: (1) what AI does to authorship; (2) query authorship as the locus of the human contribution; (3) systematic use as the condition under which query authorship can be demonstrated; (4) the epistemic dividend of externalising tacit knowledge; (5) the documentation package and how it fits open-science infrastructure; (6) policy implications; (7) conclusion.
- **Scope**: text-heavy and empirical social science research. Systematic reviews have their own established protocols (PRISMA etc.) and are out of scope.

**Word-count target**: 700.

**Material status**:
- *Reusable v9 prose*: opening problem statement (v9 Introduction, paragraphs on AI uptake and undocumented decision points); scope limitation paragraph (v9 Introduction, end). Roadmap structure modelled on v9's five-move signpost.
- *Notes/literature available*: `notes/used/socarxiv-ai-policy.md` (background on field-specific policy progress); literature notes on checklist instruments in `literature/automated_literature_searches/`.
- *Needs new writing or stronger argument*: the reframe — opening as authorship problem rather than policy diagnosis; new seven-step roadmap; one-sentence checklist situator (compressed from v9 §2). The Hindawi/honesty-pledge material is **out** of the introduction (Hindawi moves to §1.2 as warning; honesty-pledge cut).

---

## §1 What AI does to authorship

### §1.1 The authorship problem

- AI can generate plausible academic text across the full research pipeline — literature synthesis, analytical interpretation, drafting, review.
- When the text is AI-generated, the question of what the human researcher contributed becomes genuinely open.
- This is not primarily a fraud problem; it is an authorship problem — the conditions for claiming authorship may not be met even where no deception is intended.

**Material status**:
- *Reusable v9 prose*: "multiple undocumented decision points" framing (v9 Introduction, p. 1); "authorship is accountability, not just participation" (v9 Introduction, p. 3) — repurposed.
- *Notes/literature available*: `notes/used/review_v10.md`; `notes/Sociological Framing for AI Authorship.md` (Latour inscription framing — optional).
- *Needs new writing or stronger argument*: the explicit framing that the problem is *authorship*, not fraud. This is the new entry point and replaces v9's policy-failure framing.

### §1.2 The bullshit warning

- At scale, AI-assisted work risks being indistinguishable from fabrication — not because researchers intend to deceive, but because a truth-indifferent generator leaves no trace of whether a truth-seeking process occurred.
- Frankfurt (2005) / Hicks et al. (2024): LLMs optimise for plausible continuation, not for truth — structurally closer to Frankfurt's bullshitter than to a liar.
- The Hindawi/Wiley episode (8,000+ retractions, 2022–23) is invoked here as **the warning of what unchecked AI use could produce**, not as evidence that current policies have failed.
- The failure mode in unsystematic AI use is directional, not random: sycophancy, generalisation bias, PARKing (Cheng et al. 2026; Peters & Chin-Yee 2025; Kosch & Feger 2025; Asher et al. 2026; Barrie et al. 2025; Ludwig et al. 2024) — the tool confirms rather than challenges, overstates rather than accurately reports.
- The closing question of this subsection: how can a researcher demonstrate that their AI-assisted work is genuinely the product of a truth-seeking process? This sets up §1.3.

**Material status**:
- *Reusable v9 prose*: Frankfurt/Hicks paragraph (v9 §3.1, p. 14); Hindawi paragraph (v9 Introduction, p. 2 — repositioned from evidence to warning); directional failure modes paragraph and citations (v9 §3.1, pp. 13–14).
- *Notes/literature available*: `notes/hindawi_reference_needed.md` (citation flag); `notes/AI_PHacking_Summary_Report_2026.md`; literature notes on Cheng et al., Peters & Chin-Yee, Kosch & Feger, Asher et al., Barrie et al., Ludwig et al.
- *Needs new writing or stronger argument*: the **repositioning** of Hindawi from evidence-of-policy-failure to warning-of-what-unchecked-use-produces. Closing question that sets up ICMJE in §1.3. *Reference verification pending*: 8,000+ Hindawi figure (Retraction Watch).

### §1.3 ICMJE criterion 4 as the accountability standard

- Scholarly authorship has an established standard. The ICMJE criteria require substantial intellectual contribution to conception or design; critical revision; final approval; and accountability for all aspects of the work.
- Criterion 4 is the sharpest: to be genuinely accountable, the researcher must be able to investigate questions about accuracy and integrity, explain why decisions were made, and show the process was sound.
- Where AI executed the work, recall alone cannot do this epistemic job — a researcher who accepted AI outputs without documentation cannot satisfy criterion 4 in any substantive sense.
- This gives policy a more tractable question than "was AI used?": can the researcher demonstrate that authorship criteria are met?

**Material status**:
- *Reusable v9 prose*: full ICMJE analysis (v9 §5.5, pp. 40–41) — the criterion 4 paragraphs in particular; "genuine accountability... ability to investigate questions about accuracy and integrity, explain decisions" passage (v9, p. 41).
- *Notes/literature available*: ICMJE Recommendations (latest revision); `notes/used/review_v10.md` for the accountability-not-participation framing.
- *Needs new writing or stronger argument*: **promotion** of ICMJE criterion 4 from buried late-section material to the closing anchor of §1. This is the reframe's sharpest move and the v9 review's clearest steer. Frame as institutional standard that makes the authorship problem tractable; sets up §2.

**§1 word-count target**: 1,100.

---

## §2 Query authorship: the human contribution in AI-assisted research

### §2.1 Where the intellectual work sits

- The intellectual contribution in AI-assisted work lies in the query: search criteria, screening rubrics, analytical specifications, reviewer configurations — the instructions that shape what the AI does.
- Abbott (2004): the core creative act in social science is the heuristic move — the framing of a problem, the selection of an angle, the constraint of what follows; execution is not where the intellectual work sits.
- **Query authorship is an expansion of Krippendorff (2019), not a departure from it.** Rigorous coding instructions are designed so that coders are interchangeable; the analyst's contribution is formalised in the analytical construct. Query authorship applies the same move to a different executor — an LLM rather than a trained human coder. The intellectual move (specification authored by the researcher; execution within those constraints) is the established one; what is new is the executor and its failure modes, not the principle.
- Query authorship may appear novel only because LLMs are novel. The same intellectual move shows up across several traditions that long predate it. The writing-as-thinking tradition (Emig 1977; Sommers 1981; developed in §4) is the closest parallel: writing forces deliberate semantics — the externalisation of tacit logical structure into explicit form. Query authorship does the same work, with the specification rather than the manuscript paragraph as the site at which deliberate semantics happens. Krippendorff and writing-as-thinking converge here from different angles; query authorship is the convergence point in an LLM context, not a new conceptual species.
- What does change with LLMs is the executor's failure modes: sycophancy, generalisation bias, non-determinism — which is why documentation and verification requirements are specific to systematic AI use. The principle is continuous; the operational requirements are LLM-specific.

**Material status**:
- *Reusable v9 prose*: Abbott "heuristic move" paragraph (v9 §5.1, p. 37); Krippendorff "analytical construct" paragraph (v9 §5.1, p. 37); query authorship core formulation (v9 §3.2, p. 14).
- *Notes/literature available*: `notes/used/notebooklm-Abbott_heuristic.md` (mechanism mapped); `notes/used/notebooklm-Krippendorff_coding.md` ("next step in that lineage" supported); `notes/used/writing-as-thinking-sources.md` (Emig/Sommers — supports the convergence claim).
- *Needs new writing or stronger argument*: explicit framing of query authorship as **expansion of Krippendorff and convergence with writing-as-thinking**, not as a novel conceptual species. The novelty is the LLM context; the intellectual move is established. This dissolves the v9 review's pressure to "differentiate from antecedents" by accepting continuity rather than asserting newness, and threads forward to §4.1/§4.3 where the writing-as-thinking strand does its own work.

### §2.2 Query authorship satisfies the ICMJE criteria

- **Criterion 1 (conception and design)**: designing a search strategy, specifying inclusion/exclusion criteria, formulating synthesis questions, configuring a reviewer skill are acts of conception and design in the relevant sense.
- **Criterion 2 (critical revision)**: author-input files document, session by session, what the researcher directed, redirected, and rejected — this is critical revision of the work, not passive acceptance of AI output.
- **Criterion 4 (accountability)**: documented queries are what make genuine accountability possible — the researcher can trace the process that produced the version they approved and stand behind it.

**Material status**:
- *Reusable v9 prose*: full criterion-by-criterion mapping (v9 §5.5, pp. 40–41).
- *Notes/literature available*: ICMJE; `notes/used/review_v10.md`.
- *Needs new writing or stronger argument*: this is the closing payoff for the §1 setup — query authorship is what allows a researcher in AI-assisted work to satisfy the criteria a hostile reviewer would press. Promote from v9's buried late-paragraph treatment to a numbered subsection here.

### §2.3 Boundary condition

The query must encode substantive intellectual commitments to constitute authorship in the relevant sense. Three operational markers distinguish query authorship from generic task delegation:

1. **Scope/inclusion logic**: the query specifies what counts as in-scope and what counts as out-of-scope, on what grounds. Example (in): "Retain if the abstract addresses AI use in empirical research practice; exclude if it addresses only AI ethics in general." Example (out): "Summarise these abstracts for me."
2. **Evaluative grounds**: the query encodes the criterion against which the output will be judged — what would make the output correct, useful, or defensible. Without this, verification has nothing to check against.
3. **Specification of positive vs. negative outputs**: the query is explicit enough that the researcher can recognise when the output is wrong, not just when it is unexpected. Without this, errors are detectable only by accident.

A query meeting all three markers constitutes query authorship; a query meeting none is generic delegation. Most real queries will meet some markers more strongly than others; this is the line between systematic and unsystematic use, and is taken up in §3.

**Material status**:
- *Reusable v9 prose*: query authorship core formulation (v9 §3.2, p. 14; v9 §5.1, p. 37) — supplies the concept; the operational markers are new.
- *Notes/literature available*: `notes/used/review_v10.md`; logical-language reviewer skill (in `supplementary/`) as illustration of an evaluatively-grounded query.
- *Needs new writing or stronger argument*: the **three operational markers** are new in v10 and respond directly to the v9 review's request that the query authorship boundary be operationalised. Without these, the concept risks being trivially satisfied by any non-trivial AI interaction. With them, it has policy-instrument traction.

**§2 word-count target**: 900.

---

## §3 Systematic use as the condition for query authorship

### §3.1 Three defining features

Systematic AI authorship has three defining features:

- **Explicit criteria**: the instructions specify what to do and on what grounds, before the tool is run.
- **Human verification**: at each stage where the AI produces an output, a specified human checkpoint evaluates the output against the criteria before it passes to the next stage.
- **Documented outputs**: prompt configurations, screening rubrics, skill files, and decision logs are retained as artefacts that allow the process to be reconstructed and evaluated.

Without all three, query authorship cannot be demonstrated — the criteria that would show the researcher shaped the work are absent or unverifiable.

**Material status**:
- *Reusable v9 prose*: three-features definition (v9 §3.2, pp. 14–15).
- *Needs new writing or stronger argument*: the necessity claim — *all three* are required, not just any one — is sharper in v10 than in v9. State explicitly.

### §3.2 The systematic/unsystematic axis

- **Unsystematic use**: prompting without explicit criteria, refining until an acceptable output is produced, no documentation — the conditions for verifiable good work with AI are structurally absent.
- The systematic/unsystematic axis is **orthogonal** to the use/non-use axis that current policy focuses on — a researcher using AI systematically may produce more epistemically auditable work than one relying on undocumented manual judgements.
- The systematic approach is a **spectrum**; the unsystematic approach is **off the spectrum** — the absence of explicit criteria and documentation is not a minimal version of systematic use but something categorically different, because errors cannot be detected and choices cannot be attributed.

**Material status**:
- *Reusable v9 prose*: orthogonality paragraph (v9 §3.3, p. 15); spectrum-vs-categorical-departure passage (v9 §3.4, pp. 15–16, compress).
- *Needs new writing or stronger argument*: tighten v9's lengthy spectrum discussion to the essential axis-orthogonality claim and the spectrum-vs-off-spectrum distinction. The v9 review noted oscillation between spectrum and binary framings; resolve here by stating both as a single coherent claim.

### §3.3 Systematic use across the research pipeline

A systematic workflow has five stages: literature search and screening; empirical data and analysis; drafting; review; documentation. At each stage the structure is the same: explicit input criteria → configured AI execution → human verification checkpoint → documented artefact.

**Literature search and screening**
- Boolean search strings documented in advance as explicit inclusion/exclusion criteria — not constructed post hoc.
- Three routes combined: automated keyword searches, semantic searches, targeted manual retrieval — each catching what the others miss.
- Source synthesis using a grounded AI tool (queries submitted to a notebook of relevant documents only, not a general-purpose chatbot) — produces inline citations the researcher can verify.
- Human verification: spot-checking excluded records for false negatives, cross-checking synthesis outputs against cited sources.
- Open bibliographic database APIs with explicit research-use permission preferable to bulk export from subscription databases.

**Drafting and review**
- Skill-configured style profile encodes explicit criteria for sentence rhythm, hedging calibration, paragraph structure — drafts are inputs to human revision, not outputs for direct use.
- Review-and-revise stage with three components: (1) colleague review as primary external check; (2) structured AI-reviewer skill in a fresh session — fresh-session requirement critical, prevents context bias, approximates external reviewer position; (3) cross-model persona review run across at least two models from different developers — convergence across models is stronger evidence of a real weakness than any single system's output; divergence signals genuine ambiguity.
- Adversarial configuration addresses the sycophancy problem: explicitly instructing the reviewer skill to be critical, built into the persistent skill configuration, encodes a structural countermeasure against confirmation bias (Cheng et al. 2026).
- Synthesis protocol for cross-model review is itself a documented artefact: act on objections raised by two or more models; flag for individual judgement objections raised by only one; note divergence as signal of genuine ambiguity; disregard sycophantic positive feedback.

**Empirical data and analysis** *(compressed; full detail in supplementary materials)*
- Governing principle: strict separation — AI operates on research context and analysis scripts, not on primary data.
- Three-zone data model in one sentence: raw data with identifiers never sent to API; pseudonymised data supports AI-assisted cleaning; anonymised analysis-ready data unrestricted.
- Analysis scripts written to a researcher-authored specification; numbered sequentially; each with a header specifying inputs, outputs, and purpose.
- Detail on PII scanning, GDPR specifics, three-zone enforcement: supplementary materials.

**Material status**:
- *Reusable v9 prose*: literature-search/screening paragraphs (v9 §4.2, pp. 20–21); drafting/review three-component structure (v9 §4.4–4.5, pp. 22–25); empirical-data principle paragraph (v9 §4.3, p. 22, kept; remainder moved to supplementary).
- *Notes/literature available*: `supplementary/boolean-search-guide.md`; `supplementary/file-structure-template.md`; `supplementary/review-prompts-personas.md`; `supplementary/asshole-reviewer-prompt.md`.
- *Needs new writing or stronger argument*: substantial compression of v9 §4 to fit ~1,200 words within §3.3 (down from v9's ~3,500). Empirical-data paragraph reduced to one sentence of principle plus a pointer; rest moves to supplementary. Three-component review and cross-model persona review keep their argumentative weight; procedural detail is compressed.

### §3.4 Project folder structure as epistemic infrastructure

- A structured project folder is not merely organisational housekeeping — it is what makes the documentation package auditable in practice.
- A pile of artefacts with no structure is not meaningfully different from no artefacts: the structure is part of the epistemic argument.
- Folder layout (kept short — full detail in `supplementary/file-structure-template.md`):
  ```
  project/
  ├── data/raw/             ← original data; immutable; excluded from AI context
  ├── data/processed/       ← analysis-ready files
  ├── scripts/              ← analysis code
  ├── outputs/              ← tables and figures
  ├── literature/           ← search logs, source sets, syntheses
  ├── notes/                ← working notes
  ├── draft/                ← manuscript versions with edit history
  ├── logs/                 ← session logs and author-input files
  └── supplementary/        ← documentation package materials
  ```
- Configuration files at the project root: one encodes research scope and key distinctions (persistent context for every session); one specifies access controls (`data/raw/` excluded from AI context by default).
- Version-control repository timestamps every change — session logs and author-input files can be verified as contemporaneous records rather than retrospective reconstructions.

**Material status**:
- *Reusable v9 prose*: folder-structure description (v9 §4.1, pp. 21–22); configuration-files paragraph (v9 §4.1).
- *Notes/literature available*: `supplementary/file-structure-template.md`.
- *Needs new writing or stronger argument*: the **framing** of folder structure as part of the epistemic argument (not as a separate organisational concern). v9 presented this descriptively; v10 presents it as load-bearing for the auditability claim.

**§3 word-count target**: 1,800.

---

## §4 Externalising tacit knowledge: the epistemic dividend

### §4.1 Systematic use forces externalisation

- To direct the AI, the context must be specified: before a search string is executed, before a screening rubric is run, before an analysis script is written — the researcher must articulate decisions that would otherwise remain tacit.
- The tacit knowledge at issue is what Mitchell et al. (2022) call *implicit tacit knowledge*: scope commitments, theoretical priorities, evaluative standards that a practitioner could articulate if prompted but rarely does.
- Writing a screening rubric, an inclusion criterion, or a skill configuration is not clerical work — it forces deliberate semantics, the explicit structuring of logical relationships that tacit thought leaves implicit (Emig 1977).
- Sommers (1981): revision is recursive discovery, not polishing — the researcher often discovers through the act of writing the specification that their prior criterion was ambiguous or inconsistently held. This is the cognitive work query authorship captures.

**Material status**:
- *Reusable v9 prose*: Mitchell et al. tacit-knowledge paragraph (v9 §5.1, p. 36); Emig/Sommers writing-as-thinking material (v9 §3.1, p. 14, and §4.4, p. 23).
- *Notes/literature available*: `notes/used/writing-as-thinking-sources.md` (full mechanism synthesis — manuscript-ready).
- *Needs new writing or stronger argument*: promotion of the externalisation logic from v9's epistemic-properties section to a load-bearing position here. Sharpen the claim: writing the specification *is* where the cognitive work happens, not a clerical antecedent to it.

### §4.2 The pre-registration parallel

- Systematic AI use instantiates the *function* of pre-registration: the criteria must be articulated before the tool is run, not constructed post hoc to justify what the AI returned.
- **Concession in main flow** (responding to v9 review): pre-registration's *form* — public, timestamped, deposited with a third-party registry — is what provides the anti-manipulation guarantee. Private documentation does not provide this; logs can in principle be reconstructed, session records selectively retained. The framework's externalisation function survives privately, but the anti-manipulation function does not.
- This means the pre-registration analogy is a parallel of *function*, not of *form*. The framework gives externalisation discipline, auditability, and process legibility; it does not, on its own, give the binding public commitment that pre-registration's strongest form provides.
- The strongest form of the framework — a timestamped documentation package pushed to a public repository at the outset — closes the gap (taken up in §5.2). For most projects this is the appropriate upgrade path; for projects where it is impractical, the framework still provides genuine externalisation.
- Kosch and Feger's (2025) *PARKing* (Prompt Adjustments to Reach Known Outcomes) is precisely the failure mode that pre-specification forecloses; Gelman and Loken (2014) *garden of forking paths* is the underlying rationale: documented criteria at each stage prevent post-hoc rationalisation.
- Syed (2024): the epistemic argument for externalising decisions in advance applies equally to secondary data analysis, qualitative work, and literature synthesis — not only confirmatory experimental research.
- Pre-registration as a *practical option* within the framework: several artefacts (search strings, screening rubrics, analytical specifications) are natural candidates for pre-registration alongside a standard protocol. Where the design permits, the systematic AI protocol can be registered with OSF or equivalent — a public timestamp that strengthens the evidential value of the artefacts.

**Material status**:
- *Reusable v9 prose*: pre-registration analogy structure (v9 §5.1, p. 35); private/public concession (v9 §5.1, p. 35 — currently buried; promote here); PARKing paragraph (v9 §3.1, p. 14); Gelman-Loken (v9 §5.1, p. 37); Syed (v9 §5.1, p. 36).
- *Notes/literature available*: `notes/used/preregistration-analogy-limits-and-spectrum.md` (concession material, ready).
- *Needs new writing or stronger argument*: **foreground the private/public disanalogy in main flow**, not as a buried scope note. The v9 review identified this as the moderate-severity issue most likely to recur in v10 review if not addressed structurally. Open with the analogy, hand the concession in main text, close by tying forward to §5.2's timestamp logic.

### §4.3 Writing as thinking

- The writing-as-thinking tradition (Emig 1977; Sommers 1981): writing is epistemically valuable because it forces deliberate semantics — explicit structuring of logical relationships that tacit thought leaves implicit.
- Unsystematic AI use maps directly onto the failure Sommers describes: the AI does the structuring and the researcher accepts the result, bypassing the deliberate semantics that would force articulation of what the argument is and why the evidence supports it.
- Systematic AI use does not bypass this cognitive process — it relocates deliberate semantics to the specification layer, where they simultaneously serve the argument and generate verifiable artefacts.
- Connection back to §2.1: query authorship and writing-as-thinking are the *same intellectual move* — externalisation of tacit logical structure into explicit form — applied at different sites (the specification; the manuscript paragraph). The recursive discovery Sommers describes happens in both. Systematic use extends, rather than replaces, the hermeneutic circle.

**Material status**:
- *Reusable v9 prose*: writing-as-thinking paragraph and Sommers/Emig material (v9 §3.1, p. 14; v9 §4.4, p. 23).
- *Notes/literature available*: `notes/used/writing-as-thinking-sources.md` (full source synthesis).
- *Needs new writing or stronger argument*: the **bridging claim** that specification-writing and text-writing are both instances of deliberate semantics. v9 split this point across §3.1 and §4.4; v10 brings it into one place where it does most argumentative work.

**§4 word-count target**: 900.

---

## §5 The documentation package, open science infrastructure, and accountability

*Sections 5.1–5.6 below combine v9's §5 (epistemic properties) and §6 (open science) into one continuous argument, per restructuring decision.*

### §5.1 What the documentation package is

- Systematic use produces artefacts across the research pipeline: boolean search strings, screening logs, skill files, prompt templates, session decision logs, author-input records.
- These constitute a **documentation package** — *not* a replication package, because LLM outputs are not strictly reproducible (non-determinism; model-version change). The same workflow run against a later model version may produce substantially different outputs.
- What the documentation package certifies: that the criteria governing AI use were specified before the tool was run, and that the process was conducted as described.
- The package must include the model version string alongside prompt templates and screening logs — without the version string the documented process cannot be reproduced under equivalent conditions.

**Material status**:
- *Reusable v9 prose*: two-tier structure description (v9 §4.6, p. 26–27); model-version paragraph (v9 §4.6, p. 26).
- *Notes/literature available*: `notes/used/replication-package-policy-argument.md`; `notes/used/supplement-vs-logs.md`.
- *Needs new writing or stronger argument*: explicit **terminological distinction** documentation package vs. replication package. v9 used "replication package" loosely; v10 must hold the distinction tightly because the auditability-not-replication claim depends on it.

### §5.2 The burden of evidence and the timestamp

- In the absence of a documentation package, we must assume unsystematic use — the burden of evidence runs in one direction.
- **This is not a punitive presumption**; it is the same conservative prior that governs other open science norms: if code is not available, the study is assumed not independently replicable; if AI workflow artefacts are not available, the process is assumed unsystematic. The prior is symmetric across mechanisms, not anti-AI.
- A timestamped documentation package — pushed to a public repository at the outset — is the strongest form: it proves the criteria preceded the outputs, directly answers the bullshit question (this is demonstrably a truth-seeking process), and provides evidence analogous to pre-registration's epistemic function.
- Working logs that record iterative process — including unsuccessful attempts and revised criteria — are substantially harder to retroactively sanitise than end-state outputs; the contemporaneous character is part of their evidential weight.

**Material status**:
- *Reusable v9 prose*: forking-paths/post-hoc-rationalisation passage (v9 §5.4, p. 40); two-tier evidential weight passage (v9 §4.6, p. 27).
- *Notes/literature available*: `notes/used/preregistration-analogy-limits-and-spectrum.md`; `notes/used/replication-package-policy-argument.md`.
- *Needs new writing or stronger argument*: **conservative-prior justification** elevated to its own sentence (responding to plan Step 3 third item). Without it, "absence of artefacts licenses inference of unsystematic use" reads as punitive; with it, the claim is symmetric with established open-science norms. The timestamp logic is also new emphasis in v10 — binding the opening warning (bullshit) to the closing policy prescription (require documentation packages).

### §5.3 Two tiers of artefacts

- **Working logs**: daily session records of decisions made, paired with author-input files written in first-person prose — analogous to a lab notebook; evidential weight lies in contemporaneous character and recording of iterative process.
- **Supplementary materials**: skill files, prompt templates, search scripts, screening logs — end-state artefacts in reusable, accessible form.
- Author-input files document, session by session, what the researcher directed, redirected, and rejected — enabling a CRediT-style account of human contribution (ICMJE criterion 2): which ideas and framings originated with the researcher; which redirections and corrections the researcher made.

**Material status**:
- *Reusable v9 prose*: two-tier structure (v9 §4.6, p. 27).
- *Notes/literature available*: `notes/used/supplement-vs-logs.md`; `supplementary/logging-system-guide.md`.
- *Needs new writing or stronger argument*: minor — the CRediT-style framing of author-input files belongs here rather than scattered as in v9.

### §5.4 What systematic use cannot guarantee

- Documentation can be faked, as with any research record; what systematic documentation provides is *evaluable* artefacts rather than mere assertion — fabrication is more detectable.
- Non-determinism is a practical challenge: the appropriate response is to log outputs alongside prompts, note when re-runs produce substantively different results, and treat AI output as input to human judgement rather than as a final product.
- The documentation package does not guarantee quality or eliminate errors; it is a **necessary condition** for the kind of quality control that makes errors detectable.
- *Verifier competence* is a scope condition: the framework is calibrated for researchers with deep domain expertise who can recognise when AI output is wrong; for a researcher extending into a new subfield, the framework's protections are thinnest where verification risk is highest. State at point of relevance, not gloss.

**Material status**:
- *Reusable v9 prose*: documentation-can-be-faked passage (v9 §5.4, p. 39); non-determinism paragraph (v9 §5.4, p. 39); competence-threshold passage (v9 §5.4, p. 39).
- *Needs new writing or stronger argument*: substantial compression. v9's §5.4 ran ~500 words; target here is ~250.

### §5.5 Open science infrastructure

- The transparency artefacts produced by systematic AI use have the formal properties open-science infrastructure already requires: shareable, versionable, depositable, independently evaluable.
- A reviewer who receives a documentation package can assess whether the inclusion criteria were explicit before the search and whether the screening decisions are reproducible from the submitted materials — the same evaluation that reviewers of quantitative replication packages perform.
- Momeni et al. (2025) checklist for computational reproducibility in social science: systematic AI use satisfies these requirements naturally — as a byproduct of the workflow, not as an additional burden.
- Freese and Peterson (2017): social science's engagement with open-science norms is incomplete; systematic AI use applied across the research pipeline produces exactly the kind of decision documentation identified as missing. *(Verify attribution: confirm whether F&P explicitly name qualitative-decision documentation as a gap, or whether this is author inference.)*
- Törnberg (2024): prompt stability analysis — testing whether minor prompt changes alter results — is only possible if prompts are documented; systematic use makes this possibility available by default.
- Zeng et al. (2025): across 1,032 tasks in data science, reproducibility correlates positively with accuracy — systematic use is not merely a transparency mechanism but plausibly a quality mechanism. *Hedge*: this has not been demonstrated for social science specifically; the adjacent evidence does not support the assumption of a trade-off.

**Material status**:
- *Reusable v9 prose*: Momeni paragraph (v9 §5.2, p. 38); Freese-Peterson paragraph (v9 §5.2, p. 38); Törnberg paragraph (v9 §5.2, p. 38); Zeng et al. paragraph with hedge (v9 §5.3, p. 38).
- *Notes/literature available*: `notes/freese-peterson-attribution.md` (verification flag).
- *Needs new writing or stronger argument*: integration into the documentation-package narrative (v9 had this as a separate §5.2). *Reference verification pending*: Freese & Peterson (2017) attribution.

### §5.6 Journals requiring replication packages already have the infrastructure

- Journals that already require replication packages have the deposition workflows, editorial review procedures, and author guidance that a documentation-based AI policy would use.
- Extension to AI workflows requires no new principle and no new infrastructure.
- Peer review of AI-assisted work should be able to evaluate the *quality* of the systematic process, not simply its existence — whether the configuration choices are theoretically justified and accountable. This requires familiarity that most current reviewers lack — but so did statistical-code review before replication packages became standard.

**Material status**:
- *Reusable v9 prose*: replication-package extension passage (v9 §6.3, pp. 49–50); peer-review-shift passage (v9 §6.3, p. 50).
- *Notes/literature available*: `notes/used/replication-package-policy-argument.md`.
- *Needs new writing or stronger argument*: framing the reviewer-competence gap as solvable by precedent (statistical code review) rather than as a defeating objection.

**§5 word-count target**: 1,400.

---

## §6 Policy implications

- AI use is widespread (Grossmann et al. 2023); how systematic it is, is unknown — and in the absence of artefacts, must be assumed unsystematic.
- The right question for journals is not "did you use AI?" but "can you show your systematic process?"
- **Require documentation packages** as a condition of publication for AI-assisted work, modelled on existing replication-package norms.
- The documentation burden scales with the complexity of AI use: minimal AI use (grammar polishing with human review) generates minimal artefacts. The requirement does not disadvantage researchers who use AI lightly and transparently.
- Binary disclosure requirements treat systematic and unsystematic use identically and give readers no actionable information about epistemic quality. *(Brief paragraph on existing checklist literature: Zrubka et al., PRISMA-trAIce, TITAN, Mondal et al., Ganjavi et al. — these instruments address what was used and whether it was disclosed; none address the epistemic structure of the process that produced the work.)*
- SocArXiv (2026) as a concrete illustration of a partial move in the right direction: distinguishes by task but leaves the systematic/unsystematic axis invisible — a researcher with a documented criterion-governed literature search and one who accepted unverified chatbot outputs both pass on the acceptable side of the same distinction.
- Restrictive binary policies face an inherent enforceability gap: AI detection tools are not sufficiently reliable, meaning prohibitions function largely on author compliance — an enforcement mechanism that disadvantages honest actors while leaving dishonest ones undetected.
- The policy directive follows from the authorship argument, not from a contested diagnosis of policy failure: if researchers are already obligated to meet ICMJE authorship criteria, they are already obligated to be able to demonstrate what the documentation package certifies.

**Material status**:
- *Reusable v9 prose*: concessive move on journal good faith (v9 §6.1, p. 48); binary-policy critique (v9 §6.2, pp. 48–49); SocArXiv paragraph (v9 §6.2, p. 49); enforcement-gap paragraph (v9 §6.2, p. 49); documentation-based alternative (v9 §6.3, pp. 49–50).
- *Notes/literature available*: `notes/used/socarxiv-ai-policy.md`; `notes/used/replication-package-policy-argument.md`.
- *Needs new writing or stronger argument*: the **deductive framing** — policy directive follows from authorship argument, not from contested empirical diagnosis. This is the v10 reframe's payoff for the §6 architecture; explicit closing sentence required. Compress checklist literature to one paragraph.

**§6 word-count target**: 600.

---

## §7 Conclusion

- Systematic AI use and query authorship together constitute a genuinely defensible research practice: the human is demonstrably the author, the process is accountable, and the artefacts are evaluable.
- "I have argued that ..." sequencing recapping the chain: authorship problem → query authorship → systematic use as condition → epistemic dividend of externalisation → documentation package → policy.
- The timestamped documentation package closes the bullshit question: absence of artefacts licenses the inference of unsystematic use; presence of artefacts licenses the inference of a truth-seeking process.
- The policy directive follows from the authorship argument: journals should not ask "did you use AI?" — a question that is unenforceable and answers the wrong question — but "show us your systematic process."
- No new principle and no new infrastructure is needed: the extension of existing replication-package norms to AI-assisted workflows is the policy instrument, and journals that already require replication packages already have the infrastructure to implement it.
- *Scope note on this paper's own composition*: systematic in infrastructure and more hermeneutic in argument development — the conceptual moves developed through the writing rather than from a pre-specified plan. Acknowledging this is not a concession but a demonstration that the framework's value does not depend on pre-registered rigidity.

**Material status**:
- *Reusable v9 prose*: five closing points and self-demonstration scope note (v9 §7, p. 52, and v9 §5.4 self-demonstration paragraph, p. 40).
- *Notes/literature available*: `notes/used/exploratory-work-caveat.md`; `notes/conclusion-requirements.md`.
- *Needs new writing or stronger argument*: explicit "I have argued that ..." chain matching the v10 architecture (replaces v9's chain). Timestamp logic as the closing rhetorical move binding §1.2's bullshit warning to the policy directive.

**§7 word-count target**: 400.

---

## Materials note (for paper's end)

- Empirical-data-and-security section from v9: moved to supplementary materials; the argument does not depend on it and the detail is implementation guidance rather than argument.
- Documentation package for this paper: `https://github.com/torbskar/structured-use-of-AI` (anonymise for double-blind submission).

---

## Open questions for drafting

These are flagged here so they are not re-litigated mid-draft:

- **Reference verifications pending** (carried from logs):
  - Hindawi/Wiley 8,000+ figure — confirm Retraction Watch (2023) source.
  - Freese & Peterson (2017) — confirm whether attribution claim about qualitative-decision documentation is explicit in source or author inference.
  - Sommers (1981) bibliographic page numbers.
  - Massimo et al. (2024) `openalexR` author names.
  - Barrie et al. (2025) author names; Cheng et al. (2026) DOI live status.
- **Journal targeting deferred**: SMR vs. *Sociological Science* vs. other — reconsider once v10 prose stabilises. Word-count discipline (~9,000 total) preserved in the meantime so SMR remains an option.
- **Self-demonstration scope note position**: planned for §7 closing (as in v9). Confirm at drafting time that this remains the right location once the reframed argument is on the page.
- **Honesty-pledge cut confirmed**: do not reintroduce. The Ariely material and the O'Grady (2023) citation come out of references unless they are used elsewhere.
- **Empirical data section anchor**: confirm at drafting time exactly how brief the §3.3 empirical-data paragraph should be (currently planned: one sentence of principle plus pointer to supplementary).
