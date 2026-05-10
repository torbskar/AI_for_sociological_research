# Assessment: how far to defend human-in-the-loop against E&W

## Source material

Notes file `noteOnEandW_factory.md` contains three repetitions of the same "three fundamental failures" block plus a fourth block of more specific methodological critiques. Distinct ideas after deduplication:

**Core philosophical critiques:**
1. Tacit residue as opacity multiplier — uncodified biases automated into coherent artefacts the researcher can no longer detect
2. ICMJE criterion four failure — accountability requires contemporaneous intellectual engagement, not post-hoc audit of a resolution ledger
3. Epistemic exhaustion / noise machine — infinite cheap papers flood the literature with statistically significant coincidences; multiverse becomes a mask for forking paths rather than a robustness check

**More specific methodological critiques:**
4. Tautological trap — LLM "discovery" of causal shocks is high-dimensional retrieval from training data, not genuine discovery; the Popperian test is not severe
5. P-hacking the hypothesis — parallel agents iterate on the research question after observing data, which is specification search by another name
6. Status quo bias — "plausibility" filters suppress disruptive null results before they reach the viability gate
7. Logical vs. syntactic auditing — agents catch code errors but not causal reasoning failures (e.g., selection bias from a complex join)
8. Independence of parallel agents — agents sharing the same architecture and training produce hallucinated coherence rather than genuine adversarial independence
9. Shared training corpora across models — even cross-model validation (GPT-4 vs Claude) cannot triangulate to truth if models share training data (Common Crawl, digitised books, open-access journals); systematic biases in the corpus produce a "hallucination of consensus" that looks like robustness. This is a sharper claim than point 8: it undercuts not just within-model parallelism but E&W's cross-model validation strategy specifically.

---

## Assessment: the paper does not need to go further

V12 already covers the two arguments that matter most for the paper's own thesis: the tacit residue problem (grounded in Mitchell et al., which is theoretically stronger than asserting E&W are wrong) and the ICMJE criterion four consequence (in footnote 3, which is the right register for a concessive engagement with a contemporary preprint). The verification-architecture point — that the appropriate system varies with research type, and the authorship question applies regardless — is stated clearly in the text.

The additional critiques do not belong in this paper for three reasons:

**Scope mismatch.** The epistemic exhaustion and tautological trap arguments are sharp but specific to E&W's causal identification design. This paper is methods-neutral and should not anchor an argument to a critique of that specific approach.

**Empirical claims without citation.** Multiple comparisons, status quo bias, and agent independence are claims about how E&W's system performs in practice. They would need citation and import a level of specificity that turns E&W into an adversary rather than an interlocutor.

**Frame integrity.** The paper's frame is not *critique of the Paper Factory* but *here is a framework that answers the authorship question*. That framework is complete without going further. Going further risks making the paper look like a response to a preprint rather than a free-standing argument.

## One thing worth considering

Whether the ICMJE/authorship gap point should move one sentence from footnote 3 into the main text — specifically the observation that more automation makes criterion four *harder* to satisfy, not easier. But even this is optional: the footnote placement is appropriate for a preprint that appeared after the paper's main argument was developed.
