# Critical Review: "Query Authorship: A Framework for Systematic AI Use in Social Science"

**Manuscript:** v9_draft_socarxiv.md (Draft, 2026-05-04)  
**Target journal:** *Sociological Methods & Research*  
**Review date:** 2026-05-06  
**Review type:** Peer review — logic, argumentation, and methodological fit

---

## Paper Type Classification

This is a **hybrid**: primarily a discipline-reflective/programmatic paper (diagnosing a governance failure in AI policy and prescribing a documentation-based alternative) with a methodological contribution (the systematic workflow) and a conceptual contribution (*query authorship*). The argument chain that matters is therefore: diagnosis → evidence for diagnosis → prescription → justification of prescription → conclusion. The methodological sections (workflow, documentation) serve as justification for the prescription, not as the paper's primary claim.

---

## 1. Central Question ↔ Approach Alignment

### Main diagnosis
The core claim is that the use/non-use binary is the wrong policy axis and that systematic/unsystematic is the epistemically relevant distinction. This is clearly stated and consistently maintained. The paper does not drift from it. So far, so good.

### Critical flaw: the diagnosis lacks independent evidentiary grounding

For a discipline-reflective paper, the diagnosis must be grounded in evidence *about the discipline*, not inferred from first principles. The paper argues that current disclosure-based policies are insufficient, but it does not demonstrate this empirically. The evidence marshalled is:

1. The Hindawi/Wiley retraction episode — this shows papermill fraud existed; it does not show that disclosure policy failed to reduce it, nor that documentation-based policy would have prevented it.
2. The honesty-pledge retraction story — vivid but structurally weak (see §3 below).
3. The claim that AI detection tools are unreliable — asserted without citation.
4. That disclosure requirements may bias against non-native English speakers — one sentence, one citation, no development.

None of this constitutes evidence that *disclosure requirements specifically have failed or are failing in their stated purpose*. The paper would need data on policy adoption vs. observed AI misuse rates, or evidence that systematic AI fraud has continued unabated after disclosure requirements were introduced, or documented cases where a documentation-based approach would have caught what disclosure missed. Without this, the diagnosis is essentially normative: disclosure is insufficient *by design* because it is post-hoc. That is a valid analytical point, but it does not constitute evidence that the policy *has failed* — only that it *could* fail. The paper repeatedly elides this distinction.

**Severity: major.** SMR reviewers will ask what the evidence base for the diagnosis is. "It is insufficient by design" is a philosophical claim, not a sociological diagnosis.

### Prescription ↔ diagnosis fit

The prescription — extend replication package norms to AI workflows — follows logically *if* you accept the diagnosis. The logic of the chain is sound. The question is whether the prior step (the diagnosis) is established with enough force.

---

## 2. Conceptual Precision & Consistency

### *Query authorship*: underspecified at the conceptual boundary

The concept is the paper's primary novel contribution and is developed with reasonable care. However, the boundary conditions are not fully specified. Two problems:

**Problem 1: What counts as a "query"?**  
The paper extends the concept from literal search strings (where it is most intuitive) to skill configurations, reviewer prompts, and screening rubrics. The extension is plausible, but the paper does not address how granular query authorship is. If a researcher tells Claude "review this for logical coherence," is that a query? If they say "be a hostile critic," is that? The paper implies yes, but the distinction between *substantive intellectual specification* and *generic task delegation* — which presumably separates meaningful query authorship from trivial AI use — is never drawn. The Abbott (2004) "heuristic move" analogy gestures at this but does not resolve it. Without a boundary condition, query authorship risks becoming so broad as to be trivially satisfied by any non-trivial AI interaction.

**Problem 2: Query authorship vs. existing concepts**  
The paper claims this is a novel contribution, but the concept is in obvious tension with related ideas that are not adequately distinguished: (a) Latour's inscription and the notion that instruments encode theories; (b) pre-registration, which the paper itself explicitly analogises; (c) Krippendorff's analytical construct, which the paper cites approvingly. The relationship to Krippendorff is particularly underdeveloped — if the concept is "the next step in that lineage," the reader is entitled to know what is new and what is extension. The paper gestures at this ("What changes with LLMs is not the principle but the failure modes") but this is too thin to constitute a genuine differentiation of the concept.

### The systematic/unsystematic binary is presented as a spectrum and a dichotomy simultaneously

The paper says: "The systematic approach is a spectrum rather than a binary. The unsystematic approach is off this spectrum rather than at one end of it." This move is logically coherent but rhetorically unstable. Throughout the paper, the language oscillates between a strong binary (systematic vs. unsystematic) and a spectrum. If the spectrum framing is correct, the paper needs to be clearer about where on that spectrum specific practices (e.g., using AI for grammar polishing with human review vs. using AI to draft a literature review) fall — and which practices cross the threshold into what the paper calls "unsystematic." Without that, the policy prescription (documentation requirements) cannot be specified: documented how much? By what standard?

---

## 3. Argumentative Structure

### The honesty-pledge story is a rhetorical trap

The extended discussion of the Ariely retraction is the paper's weakest argumentative moment and potentially its most damaging one. The logic is:

1. Declaration-based policy rests on the assumption that requiring a declaration produces compliant behaviour.
2. The most-cited empirical support for this mechanism has been retracted.
3. Therefore, the mechanism is undermined.

This does not follow. The retraction of one empirical study does not invalidate a behavioural hypothesis — it removes one piece of evidence, leaving the prior probability of the mechanism where it would be without that study. The paper even acknowledges this: "I do not cite this to impugn the disclosure tradition as a whole, but to make a precise point." But the precise point is not as precise as the paper claims: the retraction shows the cited study was fabricated, not that signing pledges has no effect on compliance. Other studies on honesty nudges exist; the paper does not engage with the literature it is implicitly dismissing. A reviewer will skewer this. Consider cutting it entirely or significantly repositioning it as a rhetorical observation rather than an empirical argument.

**Severity: major.** This is the paper's most prominent logical gap and will be the first thing a hostile reviewer picks up.

### The Frankfurt/bullshit analogy is interesting but asymmetric

The claim that LLMs are closer to Frankfurt's bullshitter than to a liar is well-sourced (Hicks et al., 2024) and adds useful texture. The problem is the asymmetry: the paper uses this to argue that unsystematic AI use leaves the researcher accepting outputs from a truth-indifferent process. This is true. But it does not follow that systematic use converts the tool into a truth-accountable one — it converts the *workflow* into an accountable one. The outputs are still generated by a truth-indifferent process; what changes is the verification layer. This distinction matters because it affects how strong a claim the paper can make about the epistemic improvement systematic use delivers. The paper occasionally overclaims on this point.

### The pre-registration analogy carries more weight than it can bear

The analogy is the paper's main epistemic justification for systematic AI authorship. But the paper itself notes the key disanalogy: pre-registration is *public* and *timestamped*, while the systematic AI protocol is initially private. The paper acknowledges this ("The externalisation benefit, however, follows from the act of specification itself, regardless of whether it is public") but does not adequately defend it. Public pre-registration eliminates cherry-picking *because* it is public and timestamped — a researcher cannot go back and change it after seeing results. Private documentation does not do this. Working logs can be reconstructed post-hoc; session logs can be selectively retained; the claimed contemporaneity of the record relies on author compliance, which is precisely what the paper argues we cannot rely on. This gap is acknowledged in the "what systematic use cannot guarantee" section, but the concession is buried and its implication for the pre-registration analogy is not drawn out. The analogy is useful but the paper oversells it.

**Severity: moderate.** This needs explicit, prominent acknowledgement — not a footnote-level concession.

---

## 4. Argument Chain

The chain runs well from the systematic/unsystematic distinction through the workflow description to the policy implication. The main structural weaknesses are:

**The epistemic properties section is too long relative to its contribution.** The Polanyi/tacit knowledge discussion and the Gelman-Loken forking paths discussion are both illuminating but both make the same point: undocumented decisions are invisible. This is the paper's core claim, already established. The repetition in this section diffuses argumentative force.

**The ICMJE analysis is the paper's strongest underplayed contribution.** The mapping of systematic AI authorship onto ICMJE criterion 4 (genuine accountability) is genuinely novel and precise. It gives policy a tractable, already-institutionalised standard rather than requiring a new framework. It is developed in about three paragraphs at the end of the epistemic properties section and then mentioned in the conclusion. Given that SMR readers will include methodologists interested in exactly this kind of operationalised standard, this should be foregrounded much more prominently — potentially as a standalone section.

**The workflow section is too long for the argument it carries.** It functions as a demonstration ("this is how you would do it") more than as an argument ("this is why the epistemic properties follow"). For SMR, a methods journal, workflow detail is not unwelcome, but the section reads like implementation guidance rather than methodological argument. Either substantially cut it (pointing to the supplementary materials, which do the implementation work) or restructure it to foreground the epistemic properties at each stage, not the procedural steps.

---

## 5. Precision of Language

Several passages use language that is either stronger than what is established or softer than what is meant:

- **"The scholarly record is under documented pressure"** (Introduction, first sentence) — "documented" is doing too much work. Documented by whom, with what evidence? The Hindawi/Wiley case is then offered, but one case ≠ documented pressure. Either supply more evidence or soften to "under growing pressure."

- **"Disclosure policy has produced the perverse consequence that it drives AI use underground"** — causal claim without causal evidence. Consider: "may drive AI use underground" or "creates incentives to drive…"

- **"The failure mode in unsystematic AI use is not random but directional"** — this is a strong and important claim, and the citations (Peters & Chin-Yee, Cheng et al., Asher et al.) support it. Good — keep as is.

- **"Systematic use makes this knowledge explicit by requiring it to be encoded in a query, a rubric, or a configuration"** — precise and well-supported. Good.

- **"A disclosure that names AI use without specifying the epistemic structure of that use is a performance rather than a practice"** — the Sibbald et al. (2025) citation is from qualitative health research methodology on positionality and reflexivity. This is a thin warrant for an analogy used in a policy argument. Either develop the analogy (performance vs. practice is a rich distinction, but it needs the reader to see why Sibbald applies here) or drop the citation and assert the distinction directly.

- In the conclusion: **"Social scientists who build explicit search criteria… are already doing open science"** — this is a claim the paper has been building toward, but "already doing" implies that the practices exist at non-trivial scale. The paper has not established this empirically. Soften: "who would build…" or "in building X, a researcher would be…"

---

## 6. Rhetorical Effectiveness

**The introduction is effective on problem motivation but slightly overloaded.** The Hindawi/Wiley episode, the counter-industry for AI-stripping, and the honesty-pledge retraction are three separate arguments for policy inadequacy, and they arrive in rapid sequence before the paper's own positive framework is introduced. A reader encountering this for the first time may struggle to track which argument is doing what work. Consider a brief orientation sentence after the three-paragraph problem statement, signposting what is coming.

**The five-move structure announced at the end of the introduction is a strength.** It is clear, it is met, and reviewers will appreciate the roadmap. Keep it.

**The workflow section's subfootnote 3 on Sant'Anna's 28-skill implementation** is a smart move: it signals that the paper's proposal is minimalist by design, not by ignorance. But the footnote form buries it. Consider a brief inline sentence acknowledging that more elaborate implementations exist, with the footnote as the reference.

**The "adversarial configuration" and "toxic colleague" aside** in the review-and-revise section is jarring in register. The parenthetical ("you could also include a persona that is directly hostile, a toxic colleague or that like") is conversational in a way that breaks the paper's otherwise measured tone. Either cut the informal aside or develop it properly: adversarial simulation is a real methodological point worth one structured sentence.

---

## 7. Internal Consistency

One substantive inconsistency: the paper argues that systematic AI use forces externalisation of tacit decisions *before outcomes are known* (the pre-registration analogy). It then acknowledges, in the concluding scope note, that "the conceptual moves developed through the writing rather than from a pre-specified plan." This is honest and valuable, but it introduces a tension: if the paper's own argument was developed hermeneutically rather than pre-specified, then systematic AI use as practised here did *not* fully instantiate the pre-registration function for the most important parts of the work (the conceptual contribution). The paper frames this as a feature ("the framework's value does not depend on pre-registered rigidity"), but the argument for the pre-registration analogy is that externalisation *before outcomes are known* is what provides the epistemic guarantee. If key conceptual moves were not pre-specified, that guarantee is not fully present, and the paper should be clearer about which epistemic function it is and is not claiming to have instantiated. The current framing is too breezy about this.

---

## 8. Fit for *Sociological Methods & Research*

SMR publishes methodological contributions with a strong emphasis on:
- Statistical and computational methods
- Measurement and operationalisation
- Data collection and research design

The paper fits SMR's scope — it is a methodological argument about research practice, and Davidson & Karell (2025) are in SMR, which is a direct foothold in the right conversation. However, reviewers at SMR will expect:

1. **More rigorous engagement with the evidence base for the diagnosis.** SMR reviewers are quantitatively sophisticated and will not accept "insufficient by design" as a substitute for evidence that current policies have failed in measurable ways.

2. **Operationalisation of the core concepts.** Query authorship, systematic use, and the documentation threshold all need sharper operationalisation than the paper currently provides. What distinguishes a query that counts as intellectual authorship from one that does not? The concept needs a boundary condition, not just a characterisation.

3. **The workflow section needs either substantial compression or reframing as a methodological demonstration.** As currently written, it is more practical guide than methodological argument. For SMR, the epistemic argument should drive the presentation of the workflow, not vice versa.

4. **The reference to Zeng et al. (2025)** on reproducibility correlating with accuracy is used to suggest systematic use is a quality mechanism, not just a transparency mechanism. SMR reviewers will note that this is a data science study and the paper appropriately hedges the transfer to social science. The hedge is sufficient; the point is useful.

---

## 9. Production Issues

- **Reference entry for openalexR** (Massimo A et al., 2024) is flagged in-text as needing verification. Fix before submission.
- **Sommers (1981)** is cited as *Journal of Basic Writing* 3(3), 41–49 — verify against actual publication details; the bibliographic information looks slightly off (standard citation for Sommers's revision piece has different page numbers in some editions).
- **The Mondal et al. reference** appears twice under slightly different author strings (Mondal et al. 2025 in text vs. 2024 in one early in-text citation — check consistency).
- The final line of the workflow for adversarial review contains an unfinished sentence fragment: "or that like" — clearly a draft residue, clean up.

---

## 10. Overall Assessment

**Score: 3 / 5 (Acceptable — Major Revisions Required)**

**Recommendation: Major Revisions**

The paper makes a genuine conceptual contribution (*query authorship*) and a policy argument (extend replication package norms) that are coherent, well-motivated, and directly relevant to an active methodological debate. The ICMJE criterion 4 analysis is the strongest and most novel moment. The workflow demonstration is thorough and credible.

The critical weaknesses are:

1. **The diagnosis is under-evidenced.** The paper argues that current policies have failed, but supplies no systematic evidence of failure — only analytical argument about why they *could* fail. For a discipline-reflective paper in a methods journal, this is a major gap.

2. **The honesty-pledge argument is the most visible logical error** and will be the first thing hostile reviewers attack. Cut or substantially reframe.

3. **The pre-registration analogy is oversold** relative to the private/public disanalogy the paper itself acknowledges. This needs to be foregrounded and its implications addressed honestly.

4. **Query authorship needs a boundary condition.** Without one, the concept is under-specified as a policy instrument.

5. **The ICMJE analysis should be promoted to a standalone section** and foregrounded as the paper's sharpest original contribution.

The paper is clearly written, its argument is largely coherent, and the topic is timely. With targeted revision on the diagnosis, the honesty-pledge section, and the pre-registration analogy, it is submittable to SMR. Without those revisions, a sophisticated reviewer will find the core argument's evidentiary base insufficient.

---

*Review produced under systematic workflow — fresh-session, adversarial configuration.*
