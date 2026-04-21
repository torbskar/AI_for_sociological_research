# Note: Output verification and scope of argument

## Date: 2026-04-19

## For: Section on structured AI use / transparency claims / conclusion

---

## 1. Documentation of process is not verification of output

This needs to be stated explicitly in the paper. It may seem obvious to the author
but will not be obvious to all readers, and leaving it implicit invites the objection
that the transparency artefacts are a documentation ritual rather than a genuine
epistemic safeguard.

The argument to make:

The transparency artefacts produced by structured AI use — prompt templates, skill
configurations, session logs, inclusion criteria — document *intent and process*.
They show what the researcher decided to do, in what order, and on what basis.
They do not verify that the AI output accurately represented the literature, that
the inclusion criteria were applied consistently by the model, or that the reviewer
skill caught every problem it was supposed to catch. This is an honest limitation
and should be stated as one.

However, two things follow that prevent this from being a fatal concession. First,
documentation of process is more than researchers currently provide, which is
typically nothing. The transparency artefacts raise the floor of accountability
without claiming to deliver certainty. Second, structured use builds human
verification steps into the workflow at each stage — the researcher checks AI
summaries against source documents, evaluates whether inclusions are appropriate,
revises prose that does not reflect the intended argument. These verification steps
are themselves part of the structured approach and should be described as such in
the methods section.

The honest formulation is therefore: structured AI use documents process and
requires verification at each stage; it does not make verification unnecessary.
Unstructured use typically does neither.

---

## 2. This is one approach — other approaches remain valid, but carry different risks

The paper argues for one specific way of using AI in sociological research. It does
not argue that this is the only legitimate approach, and it does not prohibit or
dismiss other approaches. This scope limitation needs to be stated early and
returned to in the conclusion.

However, the scope limitation is not merely a politeness gesture. It carries a
substantive implication that should also be stated: researchers who use AI in less
structured ways are not doing something wrong in principle, but they should be aware
that unstructured use is more susceptible to a specific set of risks that structured
use is designed to mitigate.

The key risk is model bias. AI models are trained on large corpora that reflect the
theoretical, methodological, and disciplinary biases of their training data. These
biases are not random noise — they are systematic tendencies that will shape outputs
in consistent directions. A model trained predominantly on Anglo-American positivist
social science will tend to frame research questions in those terms, emphasise certain
kinds of evidence, and marginalise other traditions, unless the researcher explicitly
configures it otherwise.

In structured use, this risk is partially mitigated by several mechanisms: explicit
inclusion criteria that the researcher sets independently of the model, reviewer
skills configured to specific disciplinary standards rather than generic ones,
human verification steps that check AI outputs against source material, and
documented reasoning that makes the researcher's own framing visible and therefore
criticisable.

In unstructured use, none of these mitigations are in place. The model's tendencies
operate unchecked, and the researcher may not notice — precisely because the output
is fluent and confident. This is not a reason to prohibit unstructured use, but it
is a reason to be explicit about the risk. Researchers using AI in other ways should
ask: what are the systematic biases of the model I am using, and am I doing anything
to check for their influence on my output?

The paper's contribution is to show that structured use provides a framework for
answering that question. Other approaches are not ruled out — but they face that
question whether they acknowledge it or not.

---

## Drafting note

These two points belong in different places in the paper. The verification point
belongs in the section describing the workflow and transparency artefacts — it
should be a brief, honest acknowledgment of what the artefacts do and do not
guarantee, immediately after describing what they are.

The scope and model bias point belongs in the section making the structured/
unstructured distinction, as a clarification of what the distinction does and does
not imply. It should not read as defensive but as a genuine contribution: naming
the risk that unstructured use runs, and explaining why structured use reduces it,
strengthens the normative argument without requiring the paper to condemn other
practices.

---

## 3. The post-hoc documentation problem

This is a genuine methodological problem and the paper needs to address it directly.

The problem: transparency artefacts — session logs, prompt templates, inclusion
criteria, author-input files — only provide meaningful accountability if they were
produced contemporaneously with the work, not reconstructed after the fact to make
the process look tidier than it was. A researcher could in principle complete an
AI-assisted literature review, observe the output, decide retrospectively what the
"inclusion criteria" were, and write them up as if they had been specified in advance.
This would be a form of post-hoc rationalisation that the documentation system does
not automatically prevent.

This is structurally similar to the problem pre-registration solves in experimental
research: without a timestamp that predates data collection, a "pre-registered"
hypothesis could have been written after the researcher saw the results. The solution
in experimental research — submission to a registry before data collection — works
because the registry timestamp is independently verifiable. The question for AI-assisted
research workflows is whether an analogous mechanism exists or can be constructed.

**What this project does that partially addresses the problem**

The session logs and author-input files in this project are produced in real time
within timestamped conversations, and the file creation timestamps are independently
verifiable. The workflow is version-controlled in the sense that files are created
sequentially and the log index records when decisions were made. This does not make
post-hoc reconstruction impossible, but it makes it detectable — a retrospectively
constructed log would show file creation dates that cluster unnaturally rather than
tracking the actual research process.

More importantly, the author-input files are written as contemporaneous records of
what the author brought to each session, not summaries produced at the end. That
practice is the key mechanism: the point is not just that files exist, but that
they are produced at the time of the work.

**What the paper should say**

Three things, stated explicitly:

First, the value of transparency artefacts depends on when they are produced.
Artefacts produced contemporaneously with the work provide accountability;
artefacts reconstructed after the fact do not. The paper should recommend that
researchers treat log and documentation files as real-time records, not end-of-project
summaries.

Second, version control and timestamping are not optional features of the workflow
but epistemic requirements. Storing project files in a version-controlled repository
— Git, OSF, or similar — provides independently verifiable timestamps that make
post-hoc reconstruction detectable. This should be stated as a recommendation, not
left implicit.

Third, the paper should acknowledge honestly that no documentation system eliminates
the possibility of post-hoc rationalisation. The claim is not that structured use
makes dishonesty impossible, but that it makes the research process more transparent
and post-hoc reconstruction more detectable than unstructured use, which leaves no
trail at all. This is the same claim made for pre-registration: it does not prevent
all forms of researcher degrees of freedom, but it raises the cost of undisclosed
flexibility and makes certain forms of it visible.

**Drafting placement**

This point belongs in the transparency artefacts section, immediately after the
verification limitation acknowledged in section 1 above. The three limitations —
artefacts document intent not output, documentation does not eliminate post-hoc
risk, and neither limitation is fatal — should be presented together as an honest
accounting of what the framework delivers and does not deliver. Grouping them shows
intellectual honesty rather than burying each one separately where it might be missed.
