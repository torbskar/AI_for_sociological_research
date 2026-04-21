# Four Attacks on "Systematic AI Use in Sociological Research" (Skardhamar, v3)

*Prepared for public academic consumption. Each attack is designed to be difficult to dismiss as bad faith, routes around the defences already prepared in the v3 outline, and concedes what must be conceded so that the critique cannot be neutralised by pointing to an unreciprocated concession.*

---

## Attack 1 — The ICMJE move is a category error

Skardhamar's sharpest claim — the move that gives §5.5 and the abstract their bite — is that the ICMJE criteria, "applied positively rather than merely negatively," give journal policy a more tractable question than whether AI was used. He goes further: the contemporaneous paper trail produced by a systematic workflow is, on criterion 4, "arguably a stronger" form of accountability "for the evidential purposes criterion 4 names" than the traditional researcher's recall-based reconstruction.

This is a category error, and it is not a small one.

The ICMJE criteria were drafted by and for medical journal editors. Criterion 4 — accountability for all aspects of the work — is not primarily evidentiary. It is *institutional*: the named author is the person who can be summoned by an editor, a research integrity officer, a funder, or a court, and who bears professional and, in some jurisdictions, legal consequences when the work is found wanting. The standard is that there *is* a person with standing to be held responsible, not that a document trail exists. A researcher with perfect recall who can answer any question put to them satisfies the criterion; a researcher with an exemplary git log who has moved to a different institution and declines to correspond does not.

Skardhamar collapses this distinction. He treats "accountability" as "the capacity to investigate" and then observes, correctly, that his artefacts support such investigation better than memory does. But the ICMJE document is explicit that the named author must *agree to be accountable* — a performative commitment by a person, not a property of a corpus. Converting the criterion into a property of the process, and then claiming the process-property version is "arguably stronger," is a rhetorical move that does not survive contact with the source document.

The consequence is not merely that the ICMJE framing oversells. It is that the entire policy scaffolding of §5.5 and §6 — the claim that documentation-based policy operationalises an already-accepted authorship standard — rests on a reading the criteria themselves do not support. The reader is being offered a continuity claim ("this requires no new principle") that is in fact a substitution of one accountability concept for another.

Skardhamar could recover by stating frankly that the ICMJE criteria are being used as a motivating analogue rather than as a normative source — but doing so deflates the paper's strongest-sounding move and reveals that the authorship argument is an exegesis of his own, not an application of an established standard. As written, the move is vulnerable to exactly this objection from any reviewer who has read the ICMJE document with care.

---

## Attack 2 — "Query authorship" names something that already has a name

The paper offers "query authorship" as its central conceptual contribution — the argument that the researcher's intellectual work lies in designing the query, the configuration, and the verification structure. Skardhamar is careful in §5.1 to ground this in the tacit-knowledge-to-explicit-criteria move, and in §2.2 he claims that no existing work treats configuration as "an epistemic mechanism comparable to pre-registration."

The difficulty is that the thing being named is not new. Pre-specified Boolean search strings with documented inclusion and exclusion criteria are the defining methodological feature of systematic review (Cochrane Handbook, 1994 onwards; PRISMA, 2009). Pre-specified coding rubrics with explicit category definitions and inter-coder reliability protocols are the defining feature of quantitative content analysis (Krippendorff 1980, revised 2019). Pre-specified classifier training regimes with documented labelling instructions are standard in computational text analysis. Pre-specified reviewer criteria are embedded in every journal's reviewer guidelines. In each case, the intellectual contribution is understood to lie in the specification rather than the execution, and the specification is understood to be a methodological artefact subject to external evaluation.

"Query authorship" is, in substance, the claim that these long-standing methodological commitments apply when the executor is an LLM rather than a research assistant, a coder, or a classifier trained on labelled data. This is a useful observation. It is not a new concept.

The paper's own citations partially betray this. Momeni et al. (2025) is a computational-reproducibility checklist for social science, developed with over 180 social scientists, that already covers what Skardhamar calls the artefacts of query authorship. Törnberg (2024) addresses prompt stability analysis in exactly the terms a computational content-analysis methodologist would recognise. Davidson and Karell (2025) frame measurement, prompting, and simulation in established social-science-methodological vocabulary. Skardhamar positions these as antecedents that "implicitly favour" systematic use without theorising it; an unsympathetic reading is that they already theorise it, in the vocabulary of their own methodological traditions, and the novelty claim survives only by declining to map his terminology onto theirs.

This matters because the paper's claim to methodological contribution — the reason *Sociological Science* would publish it as a methods piece rather than as an editorial — rests on the conceptual novelty of query authorship. If "query authorship" is a rebranding of pre-specified method applied to a new executor, the paper is an application, not a contribution, and the appropriate venue is a disciplinary commentary, not a methods journal. The paper's own scholarship, in other words, generates the strongest available defeater for its novelty claim. A reviewer does not need to dig for this; it is visible in §2 and §5.

---

## Attack 3 — The self-demonstration fails on its own terms

Skardhamar acknowledges in §5.4 and the outline's introduction that the paper's own composition was "systematic in infrastructure and more hermeneutic in argument development." He frames this as consistent with §3.4's spectrum argument: a single project sits at different points at different stages, and the infrastructure supports hermeneutic stages as well as pre-specifiable ones. This is a reasonable move against the weak version of the self-demonstration objection.

It does not address the sharp version.

The paper's central theoretical contribution — the systematic/unsystematic distinction, the query-authorship concept, the ICMJE reframing, the documentation-not-verification hierarchy — is not an empirical finding reached through a pipeline. It is a conceptual claim. But the paper's own framework argues that *the researcher's contribution is the pre-specified query*. If the central conceptual moves of this paper were not pre-specified — and Skardhamar concedes they were not — then by his own framework, the documented artefacts (search logs, screening rubrics, reviewer skills) do not constitute query authorship *for the conceptual contributions*. They constitute query authorship for the literature-review component, which is a subordinate part of the paper.

The self-demonstration claim is therefore not merely weakened by the concession; it is inverted. The paper demonstrates the workflow for the one component where the workflow is already well-understood in the existing literature (systematic literature search) and does not demonstrate it for the components the paper actually claims as novel (the conceptual framework). The replication package contains evidence for the least-contested element of the paper and no evidence for the most-contested ones.

Skardhamar's spectrum argument (§3.4) is designed to absorb this. His line is that hermeneutic development is legitimate and the infrastructure supports it. But the infrastructure supporting hermeneutic development is not what the framework licenses as *query authorship*. The framework's specific claim — criterion 1 of ICMJE, conception and design — requires that the intellectual commitments be encoded in a verifiable artefact. Session logs that record iterative argument development are a different kind of artefact: they document the hermeneutic process but do not encode prior commitments the AI then executed. Calling both "systematic infrastructure" blurs a distinction the paper elsewhere insists on.

The upshot, in public: the paper's self-demonstration argument is that its own production exemplifies the framework. The honest version of that claim is narrower — that its literature search component exemplifies the framework, while its conceptual development exemplifies hermeneutic work supported by logging infrastructure. These are not the same, and the paper's own distinction between systematic and unsystematic use makes them not the same. A framework that treats logged hermeneutic work as a form of query authorship has weakened "query authorship" to the point where the term no longer discriminates — which returns to Attack 2.

---

## Attack 4 — The "binary policies" target is a straw man the paper itself dismantles

The policy argument in §6 turns on the claim that current journal and publisher policy is structurally binary: permit/prohibit combined with disclose/not-disclose, with the systematic/unsystematic distinction invisible across the board. This is the problem Skardhamar's documentation-based alternative is framed as solving.

But the paper's own literature survey in §6.1 and §6.3 undermines the binary characterisation. GAIDeT — cited approvingly — is a *tiered* taxonomy: it offers a structured vocabulary for documenting which tasks were delegated and at what level of oversight. Jones (2025) is explicitly a "novel heuristic for disclosing uses of AI" — not a binary. Davidson and Karell (2025) specify what was done rather than whether AI was involved. Zrubka et al.'s (2023) finding that checklist item counts range from 10 to 66 is not evidence of binary policy; it is evidence that the field has already moved to graded, multi-item disclosure, and the disagreement is about *which* items, not whether granularity is desirable.

What Skardhamar's own §2 documents is a field in rapid, uncoordinated, multi-instrument movement toward graded disclosure. What §6 then argues against is a simplified version of that field in which disclosure is treated as a single yes/no item. The gap between these two characterisations is the gap the paper's novelty claim depends on, and a hostile reader will notice that it opens.

This matters for two reasons. First, it makes the policy recommendation considerably less novel than advertised: if GAIDeT and Jones are already moving in the direction Skardhamar proposes, his contribution is an argument for *why* that direction is correct and a specific operationalisation (replication package extension) — useful, but incremental. Second, and more damaging, it undercuts the specific claim that the field is structurally stuck on a binary that only his framework can break. The field is not stuck; it is converging, messily, toward tiered approaches. Skardhamar is one voice in that convergence, not its author.

Skardhamar could answer this by reframing the contribution explicitly as "I propose the particular axis — systematic/unsystematic — along which the emerging tiered approaches should be organised, and I show that replication-package infrastructure operationalises it." That is a defensible, narrower claim. It is not the claim the paper as drafted makes. The gap between the two is where a reviewer will plant the flag.

---

## Attack 5 — The venue is wrong, and the replication-package move gives the game away

*Sociological Science* publishes quantitative sociology: empirical papers with data, hypotheses, and estimated quantities that other researchers can in principle re-estimate. The journal's mandatory replication package requirement, introduced in April 2023, exists to support that specific function — reviewers and readers should be able to reproduce the reported numbers from the deposited code and data. The requirement is a quality-control instrument tuned to a particular kind of contribution.

Skardhamar's paper is not that kind of contribution. It is a methodological-cum-programmatic essay with no primary data, no estimated quantities, no hypothesis tested against observation, and nothing for a third party to replicate in the sense the journal's replication requirement intends. The "replication package" he proposes to deposit consists of skill files, prompt templates, search scripts, screening logs, and author-input files. These are illustrative artefacts demonstrating a workflow. They are not the materials needed to reproduce a reported result, because the paper reports no result.

This matters in two ways, and both are visible on a close reading.

First, the fit with the journal. A methods piece at *Sociological Science* is defensible when it introduces a technique that quantitative sociologists will use on their own data — a new estimator, a new identification strategy, a new measurement instrument. The present paper introduces a documentation practice. The audience it most directly addresses is editorial and institutional, not analytical: journal editors designing AI policy, graduate programmes designing training. This is a fit for *The American Sociologist*, *Sociological Methods & Research*, or a policy-oriented venue. It is a stretch for *Sociological Science*, and the stretch is visible in §6, which is addressed to journal editors rather than to empirical researchers.

Second, and more damaging, the use Skardhamar makes of the replication requirement in §6.3 is rhetorical. He argues that journals already requiring replication packages "have accepted the underlying logic" and therefore "face a consistency challenge in treating AI workflow documentation differently." This is presented as a conservative extension. Read carefully, it is a category conflation. The replication package requirement accepts the logic that *quantitative claims should be accompanied by the code and data needed to reproduce them*. It does not accept the more general logic that any research output should be accompanied by documentation of its production process. Extending from the first to the second is a substantive policy move, not a consistency requirement. Packaging it as the latter is the kind of move that reviewers who have served on journal editorial boards will recognise immediately, because they have seen it before.

The self-demonstration claim compounds this. The paper argues that its own replication package is a proof of concept — the documentation itself is the demonstration. But the replication package *Sociological Science* requires is a proof of reproducibility for a specific reported result. A paper whose replication package demonstrates a workflow rather than supporting the reproduction of a result is using the requirement for a different purpose than the one the journal adopted it for. This is a legitimate critique available to any editor or reviewer who asks what, exactly, the replication package is for.

Skardhamar could recover by targeting a venue whose methodological remit covers practice rather than estimation, at which point the replication-package argument becomes a suggestion for that venue's editorial practice rather than a leverage point against *Sociological Science* specifically. As submitted to *Sociological Science*, the paper invites a desk-rejection on fit grounds that reviewers will not even need to articulate carefully — editors at quantitative journals know their remit, and this paper is adjacent to it rather than within it.

---

## Note on deployability

Attacks 1 and 2 are the ones I would lead with in writing. Each relies only on sources Skardhamar has himself cited or invoked (the ICMJE document; Momeni, Törnberg, Davidson & Karell) and neither can be rebutted by pointing to existing concessions in §3.4, §4.4, §5.4 or §6.2. Attack 3 is the most technically satisfying but requires the reader to hold the framework's internal distinctions in mind — it plays well in seminar, less well on a first read. Attack 4 is the most damaging to the paper's policy contribution but the easiest for Skardhamar to absorb through a reframing that costs him little. Attack 5 is the one that does its work before the paper is read on the merits — it is a desk-level objection, and the fact that Skardhamar has targeted the paper at *Sociological Science* rather than at a methods-oriented or policy-oriented venue means it operates at exactly the stage where the paper is most vulnerable. Use accordingly.
