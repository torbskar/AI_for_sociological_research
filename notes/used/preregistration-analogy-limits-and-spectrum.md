# Note: Pre-registration analogy — limits, flexibility, and the spectrum argument

**Source:** Author reflection (2026-04-19)

---

## The analogy does not fully work — and that is not a weakness

The pre-registration analogy is productive but imprecise. Pre-registration in the economist
or credibility-revolution sense is a binding commitment made before data are seen: it
forecloses certain decisions in advance. The structured AI workflow described in the paper
is not that. It is a discipline of explicitness — forcing articulation of criteria, goals,
and verification steps — but it does not bind the researcher to conclusions before inquiry
begins, and it does not prevent revision as the work develops.

This is a genuine disanalogy. It should be acknowledged, not papered over.

## But the framework is more flexible — and can accommodate pre-registration

The more important point is that the framework described is *compatible* with pre-registration
and can be made even more so. It is quite possible to include the full project setup —
skill configurations, prompt templates, search protocols, the CLAUDE.md specification — as
part of a formal pre-registration. This would give the economist-style critic exactly what
they want: a time-stamped, publicly committed specification of the workflow before results
are generated. The paper probably gestures at this but should make it explicit.

So the response to the "not really pre-registration" objection is not to defend the analogy
but to note that the structured approach sits on a spectrum that *includes* full
pre-registration at one end — and that the framework is designed to make that end of the
spectrum possible, not to replace it.

## The spectrum argument — and the opposite critique

This framing also handles the opposite objection: that structure is too limiting on free
thought, on writing-as-thinking, on the hermeneutic and exploratory character of qualitative
and interpretive research.

The answer is that there is a spectrum, and the structured approach benefits both ends of it.

At the strict end: the full setup can be pre-registered, outputs timestamped via git,
criteria fixed in advance. The economist gets what they want.

At the fluid end: even an exploratory, iterative, hermeneutic workflow benefits from
structure, because LLMs respond to what is put into them. No researcher is a blank slate.
Whatever the researcher brings to the interaction — their theoretical commitments, their
sense of what matters, their accumulated judgment about the material — shapes what the
model produces. Making that explicit, even loosely, is better than leaving it implicit and
invisible. The researcher who refuses to specify anything is not getting purer output; they
are getting output shaped by the model's priors rather than their own.

The decisive move, then, is *how* the structure is implemented. Implemented strictly, it
approximates pre-registration. Implemented loosely, it still externalises and disciplines
the researcher's own thinking without foreclosing it. Both are genuine gains over
unstructured use.

## The reviewer persona as a hermeneutic tool

The reviewer procedures and persona prompts are not only an epistemic check on the output.
They are also a way of letting the text speak back to the researcher — a reflexive,
hermeneutic move in which the researcher's own argument is returned to them from an alien
vantage point. If the researcher genuinely engages with what the configured persona
surfaces — if they do not simply dismiss the objection or accept a sycophantic softening
of it — the process functions as a form of rigorous self-interrogation.

This is the point at which sycophancy becomes a threat not only to the reliability of
the output but to the researcher's own thinking. A model that tells you what you want to
hear does not sharpen your mind; it insulates it. The adversarial configuration requirement
and the fresh-session design are defences against this — they are designed to make the
model's output harder to absorb uncritically.

## What the paper should say more explicitly

1. The pre-registration analogy is productive but imprecise: the structured approach
   disciplines rather than forecloses, and sits on a spectrum that includes full
   pre-registration at one end.
2. The full project setup can be included in a formal pre-registration — this should be
   stated explicitly, not left as an implication.
3. The spectrum argument handles both critiques: the economist who wants stricter binding
   and the theorist who wants freer inquiry. Both benefit; how much binding is appropriate
   is a methodological choice the framework does not make for the researcher.
4. The reviewer persona procedure has a hermeneutic dimension that the paper may
   understate: it is not only an error-detection mechanism but a means of disciplined
   reflexivity — letting the text speak back, if the researcher is willing to listen.

## Placement

- The pre-registration limit and spectrum argument: §3.2 (why the distinction matters)
  or §5.1 (where the pre-registration analogy is developed). Needs to coordinate with
  the exploratory-work caveat (notes/exploratory-work-caveat.md).
- The hermeneutic/reflexive dimension of reviewer personas: §4.5, as an additional
  framing of what the review stage does beyond error-detection. Connects to the
  philosopher of mind persona concern about writing-as-thinking.
- The sycophancy-as-threat-to-thinking formulation: could strengthen the sycophancy
  discussion in §3.1 or §4.5 — currently framed as a reliability problem; this
  reframes it as a cognitive problem for the researcher, which is a stronger claim.
