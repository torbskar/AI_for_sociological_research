# Underlying motivation — needs to be explicit in framing

An underlying motivation has so far been left implicit but should be central to how the article is framed. The introduction needs a clear problem statement. Without it, the paper risks reading as enthusiasm for a new tool or toy rather than a methodological contribution to a real problem.

## The real problems the paper contributes to solving

**AI is already reshaping the scholarly landscape.** This is not speculative. Two things are simultaneously true:

1. There are serious worries about papermills, unethical use, fraudulent research, and generally bullshit-production from uncritical AI use.
2. AI is here to stay. It is being integrated into everything we do and is so easily available that it is naive to think researchers will not use it.

**The slippery slope is real, not hypothetical.** There is a continuous gradient from editing language → rewriting → generating → inferring with authorship. Everyone is struggling with where on this slope it remains acceptable. This connects directly to the forking-paths idea: unstructured AI use multiplies undocumented decision points.

**Declaration is not enough.** One of the main guardrails currently proposed against AI-papermills is declaration of AI use. This is naive. What is needed is real documentation and paper trails — transparency artefacts, not self-reports.

**Authorship itself is under real pressure.** This is not a philosophical puzzle to muse about; it is a practical issue researchers must handle now.

**AI makes shallow thinking look good.** Strong sycophancy tendencies reinforce the author's existing perceptions, and fluent output disguises thin reasoning. This is an epistemic hazard distinct from outright fraud.

**Automated research systems are emerging.** Projects like APE (https://ape.socialcatalystlab.org/) are interesting evidence of AI capabilities, but also look like gigantic fishing expeditions — p-hacking at scale. This is another reason structured, documented use matters: unstructured automation at scale is exactly the wrong direction.

## Implication for the introduction

The intro must open with the problem, not with the tool. The reader should feel that something is already going wrong in scholarly practice and that the paper is offering a principled response — not that the author has discovered a cool way of working and wants to share.

Concessive move: acknowledge the genuine worries about AI in research *before* arguing that blanket restriction is the wrong response and that the structured/unstructured distinction is where the real leverage lies.

---

## Update 2026-04-21 — supporting grey literature from scholarly-publishing venues

Gemini summary of *The Scholarly Kitchen*, *Chronicle of Higher Education*, and *Nature* coverage in [literature/gemini - Scholarly AI Concerns_ Fraud, Authorship, Ethics.md](literature/gemini - Scholarly AI Concerns_ Fraud, Authorship, Ethics.md). Assessment: **this directly supports the framing and gives the introduction concrete anchors it currently lacks.** Several points are worth absorbing into the problem statement.

**Concrete anchors for the paper-mill concern.** The "five-alarm fire" characterisation and the Wiley/Hindawi retraction of 8,000+ papers give the papermill worry a specific, citeable event rather than leaving it as a generic concern. Use Hindawi as the reference case: it is the moment at which the scholarly-publishing industry publicly acknowledged that AI-scale fraud had overwhelmed traditional editorial safeguards. This is exactly the problem a documentation-based policy addresses, and framing the paper's contribution against Hindawi grounds the stakes without hand-waving.

**"Authorship is accountability, not just participation"** is a direct echo of the clarification we reached in the ICMJE thread (see synthesis N1 update): the paper's move is that human authorship under AI-assisted conditions *requires* substantive evidentiary support for criterion-4 accountability. The *Scholarly Kitchen*/Chronicle framing has already begun using this formulation; the paper is not introducing the principle but specifying what it requires in practice. Cite this as part of the problem statement — the field has named the accountability gap; the paper operationalises a response.

**The "Humanity Test"** (can the author defend every claim, trace every source, explain every nuance without AI help?) is a near-restatement of what the paper proposes as the *criterion* verification should satisfy. The paper's contribution is that documented workflow artefacts provide *structural conditions* under which the humanity test can be substantively passed — rather than leaving the test as an abstract expectation. Useful connection to the verification-quality caveat (revision D) and to the broader argument.

**"De-AI" services as a named phenomenon** is a significant gift to the paper. Authors paying to strip "AI signatures" from their text — not to improve the text but to evade detection — is the clearest possible evidence that disclosure-based policy creates perverse incentives and that detection-based enforcement drives the research process underground rather than making it transparent. This is the strongest available empirical case for the paper's core argument that *documentation, not declaration, is the right instrument*. Cite this in the framing: disclosure policy has already produced a counter-industry; documentation policy cannot be evaded in the same way because its artefacts are generated during the work, not about it.

**Task-based declarations and the "research assistant, not lead researcher" framing** both confirm the field-movement point in synthesis N4 — the field is already drifting toward tiered, task-specific approaches. The introduction can acknowledge this movement and position the paper's contribution as specifying *which axis* the tiering should be organised along, rather than claiming to invent tiered disclosure.

**"Hallucinated citations as misconduct"** (*Accountability in Research*) is a useful bridge to the social-science context: citations function as data in our disciplines, so AI-induced citation errors are not a nuisance but a direct contamination of the evidential record. This supports the paper's emphasis on literature-search and screening as the stages where structured AI use matters most.

### What this changes for the introduction

The problem statement now has specific names and events, not just generic concerns:
- Hindawi (the papermill watershed)
- "Authorship is accountability, not just participation" (the consensus principle)
- "De-AI" services (the perverse incentive of disclosure policy)
- The Humanity Test (the verification standard already being discussed)
- "Hallucinated citations as misconduct" (the relevance to social-science data)

These give the introduction five concrete handles for the concessive-first, problem-statement-first framing the original note called for. The paper is not a think-piece waving at AI anxiety in general; it is a methodological response to a set of named, documented problems the scholarly-publishing community has already identified.

### What this does not change

The grey literature summarised here is journalistic/editorial commentary, not peer-reviewed research. Use it for framing the problem and citing the field's self-understanding; do not rely on it for load-bearing theoretical claims. The peer-reviewed grounding (Pruschak & Hopp, Polanyi, Sibbald, Krippendorff when added, Collins when added) remains the argument's scholarly spine.

---

## Update 2026-04-21 — the Gino irony as evidence against declaration-based policy

Source: O'Grady (2023), "Honesty papers retracted for data 'discrepancies'," *Science* 381(6655), 255–256 — [literature/pdfs/pdfs_manualy_supplemented/science.adj8305.pdf](literature/pdfs/pdfs_manualy_supplemented/science.adj8305.pdf).

**The argument.** Francesca Gino, the Harvard Business School behavioural scientist whose programme of work established the empirical case that declarations of honesty produce honest behaviour, has had multiple papers retracted for fabricated data. The flagship finding — that signing a pledge at the *top* of a form rather than the bottom increases honest reporting (Shu, Mazar, Gino, Ariely, *PNAS* 2012) — was itself retracted in 2021 after Data Colada identified apparent fraud in a co-authored study; two further Gino papers were retracted in 2023 following a Harvard investigation. Michael Sanders (King's College London) reports that his team spent ~$250,000 running field trials built on the 2012 paper — including a collaboration with the Guatemalan tax authority — all of which failed to replicate.

Two things follow for the paper.

**1. The empirical foundation for disclosure-as-mechanism is not merely thin; it is contaminated.** Journal AI-disclosure policies, AI-use declarations in methods sections, and honesty-pledge compliance instruments all rely on the same underlying causal claim: that requiring a declaration of intent produces the declared behaviour. That claim had an unusually clear empirical showcase in the Shu/Mazar/Gino/Ariely result, and that showcase has collapsed. The field does not merely lack strong evidence that declarations produce compliance; it has direct evidence that the most-cited demonstration of the mechanism was fabricated. Declaration-based AI policy is not a cautious default with some empirical backing — it is a default with its leading empirical support retracted.

**2. The irony is sharp enough to use in the introduction without being a cheap shot.** The trust-in-research field's own flagship result on how to produce honest behaviour through a signature was produced dishonestly. This is exactly the structural failure the paper is arguing against in miniature: a checklist or declaration produces the appearance of compliance, while the actual work — including the work of honestly producing the evidence that declarations work — remains uninspected. A single paragraph in the introduction can use this as the most vivid available illustration of why documentation (inspectable artefacts generated during the work) is epistemically different in kind from disclosure (statements about the work made after it). The Gino case is not evidence that declarations *never* work; it is evidence that the mechanism on which declaration-based policy rests has not been established, was oversold, and was in its showcase case manufactured. Calibrated correctly, this is a powerful framing device.

**Connection to the documentation-vs-declaration argument.** The paper's core move — that AI policy should require documentation rather than declaration — already rested on a priori reasoning (artefacts produced during work are harder to fabricate than statements made after work) and on the papermill/Hindawi evidence. The Gino case adds a third, independent strand: the behavioural-science literature that would otherwise be the strongest empirical support for declaration-based policy has had its flagship finding retracted. Declaration is not merely a weaker instrument than documentation; it is one whose empirical warrant has been publicly undermined in precisely the field that generated it.

**How to use this in the paper.** One paragraph in the introduction, immediately after the Hindawi anchor, framing the problem at two levels: papermills demonstrate that disclosure-based policy is overwhelmed at scale by bad actors, and the Gino retractions demonstrate that the behavioural-science case for declaration-as-mechanism has collapsed even among good-faith researchers. Together these give the problem statement a concrete empirical shape: the field has reached for declaration-based instruments at a moment when their scale-limits and their mechanism-credibility have both been publicly discredited. The paper's contribution — a documentation-based alternative — is a direct response, not a speculative proposal.

**Calibration.** Do not present this as "behavioural economics is bunk" or use it to sneer at the disclosure tradition. The claim is narrower and more precise: the specific mechanism by which declarations are supposed to produce compliance has lost its most-cited empirical demonstration, which matters when that mechanism is being imported into research-integrity policy. State it once, cite O'Grady, and move on. The case makes itself.
