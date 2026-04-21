# Notes on Skardhamar (2026): Systematic AI Use in Sociological Research

**Reviewer:** David Hartmann  
**Date:** 2026-04-19  
**Format:** Identification of specific issues, not a full review

---

## 1. Two arguments requiring sharper specification

### 1.1 The pre-registration analogy is doing more work than it can bear

The paper claims that systematic AI authorship "instantiates the epistemic properties" of pre-registration, and the analogy recurs across sections 3.2, 5.1, and 5.3. The functional analogy — both force articulation of decisions before outcomes are known — is defensible as stated. The problem is that the paper extracts stronger claims from the analogy than the functional similarity warrants, without adequately accounting for the disanalogy it acknowledges but then moves past too quickly.

Pre-registration's epistemic value is inseparable from its publicity and its timestamp. The point is not just that the researcher committed to something; it is that the commitment was made verifiably prior to data observation, in a form accessible to anyone, and that deviations are visible as deviations. The paper acknowledges this (§3.2, §5.1) but then says the disanalogy is "real but not fatal" and moves on in roughly a sentence. That is not sufficient. The working log — the paper's proposed substitute for publicity — is contemporaneous in a much weaker sense. It is a private document on the researcher's machine, timestamped by git commit, produced by the researcher themselves, and not subject to independent verification of its own authenticity. Git timestamps are trivially malleable; a researcher who backdates a commit or reconstructs a plausible-looking log after the fact leaves no forensic trace distinguishable from a genuine contemporaneous log in normal usage. Pre-registration eliminates this problem structurally; the proposed workflow does not. The paper should either bound the analogy explicitly — "externalisation benefit only, not the integrity-against-manipulation benefit" — or explain how the log-plus-git-history mechanism actually replicates the anti-manipulation property that makes the pre-registration timestamp credible. Asserting the disanalogy is not fatal does not close it.

The related claim that "working logs... address the cherry-picking risk that pre-registration's public commitment eliminates through publicity" (§5.1) is simply not demonstrated. Pre-registration eliminates cherry-picking through an enforcement mechanism: the public commitment exists before the data, so deviation is observable. A private log addresses cherry-picking only if it is itself immune to post-hoc construction — which the paper does not establish. This claim needs either a stronger argument or significant hedging.

### 1.2 The productivity and quality argument is underdeveloped and partially unsupported

The paper cites Zeng et al. (2025) as suggestive evidence that systematic prompting improves output quality, not just auditability. The citation is appropriate, and the paper's hedging is largely correct (§5.3 notes the finding comes from data science tasks "that differ in important ways"). The problem is that the abstract promises the paper "shows" that systematic use has epistemic properties consistent with open-science practice — and the policy argument in section 6 repeatedly implies that systematic use is better research, not merely more auditable research. The closing paragraph of section 5.3 — "the act of externalising and specifying criteria is itself a cognitive discipline: it forces precision that vague prompting does not" — is presented as an argument for quality improvement. It may well be true. But it is a plausibility claim, not evidence, and the paper nowhere flags that the quality argument is in a different evidential register from the documentation argument. These two arguments — documentation improves auditability; systematic use improves output — need to be disentangled. The first is demonstrated by construction; the second is empirically open. Conflating them, even gently, gives the quality argument unearned credibility in a policy context.

The productivity case is less developed than the transparency case throughout the paper, despite being the one argument most likely to change practitioner behaviour. I would want to see either a more explicit acknowledgment that the quality case is unestablished, or a more developed treatment of the mechanisms — why we should expect quality to improve, what it would take to demonstrate it, and what the likely effect size is. The Zeng et al. finding (reproducibility correlates with accuracy across 1,032 data science tasks) is a single study in an adjacent field. It warrants a footnote, not a section.

---

## 2. The one caveat that should be added

**Documenting process does not verify output.**

The paper's central claim is that transparency artefacts — skill files, screening logs, prompt templates, author-input files — give reviewers the materials needed to evaluate AI-assisted research. This is correct as far as it goes. What it does not say, anywhere, is what these artefacts actually guarantee versus what they merely document.

Here is the gap: a complete replication package for a systematic AI workflow tells a reviewer exactly how the workflow was configured and what it was instructed to do. It does not tell the reviewer whether the outputs of that workflow were accurate. A beautifully documented screening rubric with explicit inclusion criteria and a complete log of every AI decision still cannot tell a reviewer whether the AI's classifications were correct — because, as the paper itself notes (§5.4), systematic use "does not eliminate LLM error." Documentation makes errors visible and correctable — but only if someone checks. The verification checkpoints in the workflow are performed by the researcher, not by an independent party. For a replication package of statistical code, a reviewer can re-run the code and verify the output. For a systematic AI workflow, a reviewer who re-runs the screening rubric against the same corpus will not necessarily get the same classifications, because the model is non-deterministic and the model version may have changed. 

The paper mentions non-determinism (§5.4) but treats it as a documentation challenge ("log outputs alongside prompts, note when re-runs produce substantively different results") rather than as a limitation on what the transparency artefacts can guarantee. The honest framing is this: systematic AI documentation guarantees that the researcher's *criteria* were explicit and prior; it does not guarantee that the AI's *execution* of those criteria was accurate, and independent verification of that execution is substantially harder than for statistical code. The paper should state this explicitly, note what follows — reviewers must either re-run and compare, or accept that they are evaluating process design rather than output verification — and adjust the strength of the epistemological claims accordingly.

---

## 3. Does the paper adequately address the process/output distinction?

Not fully. Section 5.4 is the closest engagement: "systematic use does not guarantee high quality or eliminate errors... any misclassification will be visible in the documented outputs and correctable through the human verification checkpoint." This is the right structure but it stops short of the important question, which is: *verifiable to whom, and how?*

The phrase "visible in the documented outputs" glosses over a significant difficulty. The documented output is the researcher's record of what the AI produced. An independent reviewer can see what the researcher recorded, but cannot easily verify that the record is complete or that the classification decisions were correct without re-running the workflow — and re-running may not reproduce the same results. The analogy to quantitative replication packages breaks down here. With code and data, a reviewer who re-runs the script gets the same numbers (setting aside stochastic estimators, which the paper correctly notes as parallel). With a documented AI workflow, a reviewer who re-runs the rubric gets *different* outputs from what was recorded, because the model is non-deterministic. This means the reviewer is evaluating the criteria design rather than verifying the output. That is valuable, but it is a different kind of verification than what replication packages normally provide, and the paper should say so.

What would need to be added: a brief section — a few paragraphs, not a new section — that distinguishes (a) what documentation verifies (that criteria were prior, explicit, and consistent with the paper's claims), (b) what documentation makes possible but does not verify (that outputs were accurate and complete), and (c) what remains genuinely unverifiable under any documentation regime (whether the AI's non-deterministic execution of correct criteria produced the same results as a different run would have). The paper's contribution is strongest on (a); it is weakest on acknowledging the limits at (c).

---

## 4. What the paper gets right, and whether I would adopt it

The core argument is sound and I find it practically useful. The systematic/unsystematic distinction is the right axis. Binary disclosure policies are genuinely inadequate, and the paper's diagnosis of why — they capture end-state, not process; they inadvertently treat epistemically accountable and unaccountable practice identically — is clear and correct. The ICMJE reframing is a good move: it shifts the policy question from the unanswerable ("was AI used?") to the answerable ("can the researcher demonstrate that authorship criteria are met?"), and it does so using an instrument journals already accept.

The adversarial configuration recommendation (§4.5) is the single most practically useful recommendation in the paper. Explicitly configuring a reviewer tool to be critical, to play devil's advocate, to raise objections — and encoding this in a persistent skill rather than trusting individual prompts — directly addresses the sycophancy failure documented by Cheng et al. I would implement this immediately and would have implemented it earlier if someone had stated it this clearly. The sycophancy problem is real and underappreciated, and framing it as a configuration problem rather than a model limitation is the right frame.

The `CLAUDE.md` project context file and the `.claudeignore` separation structure (§4.1, §4.3) are practically sound. Structurally preventing raw data from entering AI context rather than relying on researcher vigilance per session is the right engineering approach. I would adopt this.

On the productivity argument: the paper is correct that the case for systematic use does not depend on demonstrating quality improvements (final paragraph of §5.3, final paragraph of §7). It should say this earlier and more clearly. The documentation case stands on its own; pulling in the Zeng et al. quality argument without adequate hedging weakens the main argument by inviting the objection that the quality evidence is thin — which it is — when the stronger and better-supported case is about auditability, not output quality.

One practical note: the paper is written for sociologists who need convincing. For economists already operating in the replication package norm, the transparency argument is almost trivially obvious and the policy argument follows quickly. The value added is the specific implementation architecture (project folder structure, configuration layers, PII hook design, author-input files) and the ICMJE framing. Those are genuinely useful and I had not seen them stated this concretely.

---

*These are identification notes only, not a full review.*
