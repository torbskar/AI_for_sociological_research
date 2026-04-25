# Claude Contribution Guide

## Purpose

The `YYYY-MM-DD-claude-contribution.md` file is the transparency record of what Claude contributed intellectually to a session. It is the counterpart to the author-input file, and together they document the human-AI division of intellectual labour in a form suitable for disclosure, peer review, and — where relevant — authorship attribution under CRediT criteria.

The file exists because "AI-assisted" is not a description — it is a placeholder. The contribution file makes the description concrete: what did the AI actually contribute, and did that contribution originate from the author's direction or from the AI's own elaboration?

---

## The two records the file must contain

### 1. Decisions and reasoning

For each substantive intellectual contribution Claude made, record:
- What was proposed or decided
- The reasoning, *only* when non-obvious or when the rejected alternative matters

Omit reasoning for straightforward execution. Do not narrate the process — record the intellectual output.

**Correct:**
> **Spectrum framing for the pre-registration analogy** — Initiated by author query
>
> Proposed replacing the binary pre-registration/not framing with a spectrum argument: implementation ranges from informal discipline (fluid end) to full pre-registration (strict end); both benefit from structured approach. The spectrum argument resolves the economist critique (requires strict pre-specification) and the theorist critique (pre-registration is incompatible with exploratory work) simultaneously, without requiring separate responses to each.

**Incorrect:**
> Claude wrote a section about the pre-registration analogy and explained that it could be framed as a spectrum. The author found this useful.

The first records the intellectual content; the second narrates the session.

---

### 2. Initiative attribution

Every substantive contribution carries one of two labels:

**Initiated by author query**: The author's query or prompt drove the intellectual move. Claude executed on the author's direction. The author specified what to do, what angle to take, what criteria to apply, or what problem to solve.

**Claude initiative**: Claude introduced a framing, argument, connection, or approach that was not present in the author's query. The author's query created the occasion, but Claude supplied the content.

Use "Claude initiative" accurately and sparingly. In a well-run structured session, most contributions should be "Initiated by author query" — that is what structured use means. A pattern of predominantly "Claude initiative" labels is a signal that the session was less structured than intended.

---

## Query-authorship annotation

The most important function of the claude-contribution file is to document query-authorship: the intellectual contribution embedded in the author's queries themselves.

A query is not merely an instruction. When an author asks Claude to "frame the pre-registration analogy as a spectrum", that framing is the intellectual contribution — not the paragraph Claude writes. When an author specifies exclusion criteria for a literature screen, those criteria are the intellectual contribution — not the Python script. When an author identifies that a section has a logical gap, that diagnosis is the intellectual contribution — not the revision.

Annotate these with:

> *Author query as intellectual contribution — [what the query contributed]*

### When to annotate

Annotate when the author's query:

- **Introduces a new framing or argument**: The query itself names or identifies an intellectual move that was not previously on the table.
- **Specifies evaluation criteria**: The query defines what counts as adequate, relevant, or well-argued — not just what to produce.
- **Diagnoses a problem**: The query identifies that something is wrong or missing in the current draft or argument.
- **Redirects work based on the author's own reasoning**: The query changes direction because the author has reached a conclusion, not because Claude suggested it.
- **Configures a tool or skill**: The author's specification of review criteria, search terms, or skill parameters is itself the intellectual contribution.

### When not to annotate

Do not annotate when the author's query is:
- A request for a well-defined task with no original intellectual content ("write the abstract", "check the log index")
- A confirmation or procedural exchange
- A response to a Claude initiative rather than an independent framing

### Example annotation

> **Hermeneutic dimension of reviewer personas** — Initiated by author query
>
> *Author query as intellectual contribution — identified the reviewer persona procedure as a hermeneutic tool (letting the text speak back reflexively), not merely a quality-control step. This reframing was not present in the prior session's discussion and reorients how the procedure is described in §4.*
>
> On author's framing, proposed language for §4 that distinguishes the epistemic function of reviewer personas (surface assumptions, expose blind spots) from their quality-assurance function (catch errors, improve clarity). The two functions are different in kind, and the distinction warrants separate treatment in the section.

---

## What the file is not

The claude-contribution file is not:
- A summary of what was produced (that goes in the decision log)
- A session narrative
- A list of tools used or files written
- An account of everything Claude did (only what was intellectually substantive)

It is also not a statement of Claude's authorship. The file documents contributions; authorship is the author's determination, based on the full record.

---

## Practical writing guidance

Write the file at the end of the session, after the decision log and the author-input file are complete. The decision log tells you what was decided; the author-input file tells you what the author brought; the claude-contribution file records the intellectual work on Claude's side.

Work through the decision log section by section. For each decision:
1. Was Claude's contribution substantive enough to warrant a record? (If not, omit.)
2. What was the contribution? (State it concisely, with non-obvious reasoning if any.)
3. Did it originate from the author's query or from Claude's initiative? (Label it.)
4. Was the author's query itself the intellectual contribution? (Annotate if so.)

A well-written claude-contribution file for a typical session is 300–600 words. A longer file usually means too much is being recorded (routine steps are being included) or the reasoning is being over-explained. A shorter file — for a substantive session — usually means the reasoning is being under-specified.
