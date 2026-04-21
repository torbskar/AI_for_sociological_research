# Note: Review stage — full protocol and draft text for §4.5

**Source:** Author reflection (2026-04-17)

---

## The full review protocol (three components)

The review stage as actually practised has three components that §4.5 currently describes only partially.

**Component 1 — Colleague review.** The manuscript is sent to colleagues for external human expert feedback. This is the baseline and primary external check; AI-assisted review is supplementary to it, not a substitute. The paper should say this explicitly — both to be accurate about the workflow and to avoid the impression that AI review replaces human review.

**Component 2 — AI reviewer skill in fresh session (within Claude).** The structured reviewer skill is run in a fresh session with no prior project context. The fresh-session design is critical and currently unmentioned in the draft: running the review in a session that already has full project context biases the model toward consistency and coherence with previous exchanges rather than independent critical assessment. A reviewer who has been part of the discussion is not the same as a reviewer encountering the argument for the first time. Fresh session = no prior context = closer to the epistemic position of an actual external reviewer.

**Component 3 — Cross-model review using calibrated personas.** The same persona prompts (see `notes/review-prompts-personas.md`) are submitted in fresh sessions to at least two other models (ChatGPT, Gemini, potentially Mistral). The design rationale: different models have different training data, tendencies, and likely blind spots. One model's confirmation may be that model's bias; convergent critique across models is substantially more credible. Divergence across models on the same prompt is itself informative — it signals where the argument is genuinely ambiguous rather than merely weak in one model's framing.

The synthesis protocol from `review-prompts-personas.md`:
- Act on any objection raised independently by two or more models
- Flag for judgment any objection raised by only one model
- Note model divergence as a signal of genuine ambiguity
- Disregard sycophantic positive feedback; use critical outputs only

---

## What this adds to the paper's argument

The current §4.5 covers adversarial configuration within a session. The three-component protocol extends this in two directions the paper should describe:

**Fresh session as structural design.** Just as the pre-registration analogy is about commitment before outcomes are known, the fresh-session design is about assessment before context accumulates. A reviewer inside the project is not the same epistemic position as a reviewer outside it. The fresh-session requirement is a structural countermeasure against familiarity bias — the tendency of a model (or a colleague who has heard the argument evolve) to evaluate what the argument was trying to do rather than what it actually achieved.

**Cross-model review as structural countermeasure against model-specific bias.** The adversarial configuration in §4.5 addresses sycophancy within one model. Cross-model review addresses a different problem: that a single model may be systematically biased toward certain argumentative styles, theoretical traditions, or rhetorical conventions. Running the same persona prompts across Claude, ChatGPT, and Gemini exploits the variance between models to identify critique that is robust across training regimes. This is the review-stage equivalent of robustness checks in quantitative analysis: not because any one check is decisive, but because convergence across multiple independent tests is more credible than any single test alone.

**Persona calibration as query authorship.** The simulated reviewer prompts in `review-prompts-personas.md` are themselves a demonstration of query authorship: each persona encodes a specific epistemic position (anti-positivist theorist, philosopher of extended mind, credibility-revolution economist, computational political scientist) that is structurally likely to resist the paper's argument from a direction the author cannot fully anticipate. The prompt design is the intellectual work; the model's output is the execution within those constraints. This is distinct from asking "what are the weaknesses of this paper?" — a generic question that produces generic feedback.

---

## Proposed text for §4.5 (to be integrated with existing content)

The current §4.5 ends with the adversarial-configuration paragraph. Proposed addition after that paragraph:

---

The review stage as described so far addresses the sycophancy problem within a single session. Two structural extensions address further failure modes. The first is the fresh-session requirement: reviewer skills should be run in sessions with no prior project context, not in continuation of the working session. A model that has participated in developing an argument is not the same epistemic position as one encountering it for the first time; familiarity biases assessment toward evaluating intent rather than achievement. The fresh-session design approximates the epistemic position of an external reviewer.

The second is cross-model review. Submitting the same configured reviewer prompts to multiple AI systems — at minimum to two models from different developers — exploits variance in training regimes to identify critique that is robust across models. A concern raised by one model may reflect that model's tendencies; the same concern raised independently by two or more models is substantially more credible. Divergence across models on the same question is also informative: it signals where the argument is genuinely ambiguous rather than merely weak in one model's register. This functions as the review equivalent of a robustness check — not because any single AI review is decisive, but because convergent critique across independent systems is stronger evidence of a real weakness than any single system's output.

Colleague review remains the primary external check; AI-assisted review, whether within a single configured skill or across multiple models, is supplementary to it. What the structured approach provides is a well-prepared manuscript before it reaches human reviewers: weaknesses that would have appeared in referee reports are identified and addressed earlier in the process, and the author arrives at the colleague-review stage with a more defensible draft.

---

## What to do with `notes/review-prompts-personas.md`

The persona prompts file is itself a transparency artefact — it should be included in or referenced from the supplementary materials / replication package. It demonstrates query authorship at the review stage: the intellectual work is in calibrating the personas, not in whatever the model returns.

**Defer to:** next manual edit pass of §4.5.
