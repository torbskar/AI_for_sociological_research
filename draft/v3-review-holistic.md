# Holistic review of v3-draft.md

**Date:** 2026-04-16
**Reviewer lenses applied:** `logic-language-reviewer` + `skardhamar-style` + full-manuscript reading for argument coherence, effectiveness for Sociological Science readership, and substantive content.
**Paper type:** Discipline-reflective / programmatic, with a substantial methodological-workflow core. Not empirical; not purely theoretical.

---

## 0. Does the overall argument hold?

**Yes, with one terminological fault-line and two load-bearing claims that need tightening.**

The paper's spine is coherent:

1. *Diagnosis* — current policies treat AI use as a binary (use/non-use, disclosed/not) and miss the epistemically relevant axis. Supported by Ganjavi, Mondal, Zrubka.
2. *Reconception* — the relevant axis is systematic/unsystematic AI authorship; the intellectual work is in the query, not the output.
3. *Mechanism* — a documented workflow implements the systematic side.
4. *Justification* — systematic AI authorship instantiates open-science properties (externalisation, artefacts) and, mapped onto ICMJE, strengthens rather than erodes the criteria.
5. *Prescription* — a documentation-based policy framework is feasible, requires no new infrastructure, and is more consistent with existing replication norms than the binary.

The five announced moves in §1 are delivered and returned to in §7. The ICMJE bridge (§2.2 → §5.5) is the paper's strongest structural move: it takes a settled negative claim (AI cannot be an author) and extracts from it a productive positive question (what must the human researcher demonstrate?). This is a genuine contribution rather than a relabelling.

The fault-line is terminological (see Priority 1 below). Two load-bearing claims require attention (Priority 2 and 3). Beyond that, the paper is close to submission-ready.

**Score: 4/5. Recommendation: Minor revisions.**

---

## Priority 1 — Critical. Fix before submission.

### 1.1 Terminological drift: *structured/unstructured* vs *systematic/unsystematic*

The paper uses two near-synonymous term pairs and switches between them without acknowledgement:

- **Title:** "Structured AI Use"
- **Abstract:** "used systematically"; "systematic AI authorship"
- **§1 move 1:** "systematic and unsystematic AI authorship"
- **§3 heading:** "The structured/unstructured distinction"
- **§3.1 heading:** "What unstructured AI use looks like"; body: "Unsystematic AI authorship is characterised by..."
- **§3.2 heading:** "What structured AI use looks like"; body: "Systematic AI authorship has four defining features"
- **§3.3 heading:** "Why the distinction matters"; body oscillates between "structured" and "systematic"
- **§§4–7:** predominantly "systematic AI authorship"

A reader can reconstruct that the two pairs mean the same thing, but the paper never says so, and the inconsistency will be flagged by any careful reviewer. Worse, "structured use" and "systematic AI authorship" are not obviously coextensive — "authorship" is a stronger claim than "use," and readers may wonder whether the author is drawing a subtle distinction and then failing to maintain it.

**Fix:** pick one pair and use it throughout. Recommendation — **systematic / unsystematic AI authorship** — for three reasons: (i) "authorship" is the concept that does the work in §5.5 and §7; (ii) "systematic" avoids the connotation of "merely structured" (i.e. having some format) without being epistemically committed; (iii) it is the pair used in the abstract and the conclusion, which are the most consequential framing positions. The title, §3 heading, §3.1 heading, and §3.2 heading then need to be changed. "Structured use" can survive as a lower-register descriptor in a handful of places but should not carry argumentative weight.

Alternative: if the author wants to retain "structured/unstructured" at the section-heading level because it reads more concretely, then add a sentence at the first use (§3, opening) stating the two pairs are used interchangeably and why — but this is the weaker option.

### 1.2 §1 move 1 and §5.4 sit in tension

§1 states that systematic and unsystematic use "differ not merely in transparency but in epistemic quality: systematic use makes errors visible and correctable; unsystematic use does not."

§5.4 says: "The AI operating without explicit criteria may perform equally well on average, but its errors are less visible."

These can be reconciled — "epistemic quality" in §1 meaning the *evaluability* of the work, not its average accuracy — but the surface reading is a contradiction. A policy-adjacent reviewer will notice.

**Fix:** tighten §1 move 1. Replace "differ not merely in transparency but in epistemic quality" with "differ not in average output quality but in epistemic standing: systematic use makes errors visible and correctable; unsystematic use does not." This aligns §1 with §5.3 (no demonstrated quality difference) and §5.4 (visibility, not average accuracy, is the point).

### 1.3 The "eight stages" mismatch in §4.1

§4.1 announces: "A systematic workflow for this purpose has eight stages: literature search, candidate screening, full-text screening, source organisation and synthesis, empirical data and analysis, drafting, review, and documentation."

But the subsections of §4 are: 4.2 Literature search and screening (which collapses the first three announced stages), 4.3 Empirical data and analysis, 4.4 Drafting, 4.5 Review, 4.6 Documentation. That is five subsections covering the eight stages, with the first four stages all folded into §4.2.

The mismatch is not fatal — the stages are conceptual, the subsections are organisational — but it will prompt a reviewer to ask why the structure doesn't mirror the claim.

**Fix (lightest touch):** add one clause to the §4.1 sentence: "A systematic workflow for this purpose has eight stages — literature search, candidate screening, full-text screening, source organisation and synthesis, empirical data and analysis, drafting, review, and documentation — organised below into five subsections (the first four literature stages are treated together)."

### 1.4 §3.2's "four defining features" — the fourth overlaps with the others

The four features are listed as: explicit criteria, human verification, documented outputs, and "a documented workflow or pipeline with an associated file structure that supports progress across the full project."

The fourth is not a fourth feature of equal standing with the first three — it is a structural precondition that subsumes them. A file structure is the container; the first three are what fills it. Listing it as a co-ordinate item muddles the analytic structure and makes the §3.2 paragraph that follows ("This project-level structure...") read as if it were stepping back to a higher level, which it is.

**Fix:** restructure as three defining features (explicit criteria, human verification, documented outputs) plus a closing sentence — or paragraph — that says these three are implemented through a project-level configuration and file structure. This matches how the rest of the paper actually uses the concepts.

---

## Priority 2 — Important. Significantly strengthens the paper.

### 2.1 §1 second paragraph — scope and tool-disclosure both crowd into the same paragraph

The second paragraph of §1 now carries four jobs:

- announcing scope (text-heavy/empirical social science)
- flagging GDPR/empirical constraints → §4.3
- flagging literature-search coverage → §4.2
- tool disclosure (Claude, CLAUDE.md, .claudeignore, skills)

The "Similarly, while a section on literature search and review is included below, the main focus is on the system and protocols" sentence is the weakest link — "similarly" doesn't follow cleanly from the preceding data-constraints sentence, and the sentence itself is a slightly apologetic gesture that tells the reader the paper is about less than they might expect.

**Fix:** split into two paragraphs. First paragraph: scope (who this is for, what is covered, the empirical caveat pointing to §4.3). Second paragraph: tool disclosure. Drop or rewrite the "Similarly..." sentence — the literature-focus point is already implicit in §4.1's scope note and doesn't need advance warning.

### 2.2 §2.1 opener is generic

"Large language models have been widely adopted across academic disciplines, transforming scientific practice (Grossmann et al. 2023)."

This is the "AI is changing everything" opener that the project instructions warn against, and it underperforms the substantive observation that the paper actually has. The real opening should foreground the asymmetry: adoption has outpaced the frameworks to evaluate it.

**Fix:** Open §2.1 with a claim that does work, e.g. "AI tools are now widely used across academic disciplines (Grossmann et al. 2023), and in sociology their uptake has outpaced the institutional frameworks for evaluating them. Korinek (2023) catalogues practical use cases for economists and social scientists; Feuerriegel et al. (2024) trace early adoption in information systems. The question of whether AI has entered research practice is settled; what remains contested is what kind of practice has emerged and what kind should be."

### 2.3 §2.2's central claim is strong and should be hedged more precisely

"To my knowledge, no existing work has applied these criteria to AI-assisted research in a way that asks whether the human researcher meets them."

This is essentially the paper's contribution claim. It is stated three times in the paper (§2.2, §5.5, §7) with slightly different wording. A committed critic could find counterexamples — some editorial commentary in medical journals has raised this, and the ICMJE itself has addressed AI authorship, though not in the direction the paper develops.

**Fix:** specify the scope of the claim more narrowly. "To my knowledge, no existing work has developed the ICMJE criteria into a positive framework for evaluating the human researcher's contribution in AI-assisted work — as distinct from applying them negatively to rule out AI authorship, which is widely done." This is both more defensible and more precise about the contribution.

### 2.4 §5.5 on "structural vs presumptive accountability" — load-bearing claim deserves more care

The claim that systematic AI authorship produces accountability that is "stronger than what traditional undocumented research provides" is consequential and somewhat provocative. It is hedged appropriately in the subsequent sentence ("a claim about the type and verifiability of accountability, not a claim that AI-assisted research is better research"), but the ordering matters: the stronger claim lands first and the hedge arrives second.

**Fix:** reverse the order. State the narrower claim first — the *type* of accountability is different — and then allow the comparative statement to follow as an implication. Something like: "The replication package and session logs constitute accountability that is structural rather than presumptive; in the specific sense that criterion 4 requires — the capacity to investigate — this is a different type of accountability than what recall-based reconstruction provides, and arguably a stronger one for the evidential purposes criterion 4 names. I am not claiming that AI-assisted research is better research..."

### 2.5 §4.6 → §5 bridge now works but leaves a residual seam at §4.6's opening

The rewritten bridge paragraph at the end of §4.6 is effective. But §4.6 itself still opens with "The documentation produced across all stages of the workflow is structured in two tiers" — a dense opening that pitches into content without orienting the reader. The section carries three threads (two-tier logs, CRediT attribution, replication package) and the bridge paragraph is now doing the work of synthesising them. Worth a second look: does §4.6 earn its place in §4, or would it work better as the first subsection of §5?

**Less invasive fix:** add an orienting sentence at the top of §4.6 that names the three threads before developing them. No structural change needed.

---

## Priority 3 — Minor. Precision and polish.

### 3.1 Abstract

- **[DONE]** "externalises tacit decisions" → "externalises tacit commitments" (matches §5.1's careful distinction between inherent and implicit tacit knowledge; "decisions" is looser than the paper's own usage).
- **[MANUAL]** The abstract does not mention the ICMJE bridge, which is arguably the paper's most distinctive move. Consider adding one clause: "and shows that the ICMJE authorship criteria, applied positively rather than merely negatively, give policy a more tractable question than whether AI was used." (Space permitting — the abstract is at ~175 words; SocSci cap is 150, so something else would have to come out.)

### 3.2 §3.1 last paragraph

"In this sense, the structured/unstructured distinction is not a new principle; it is the application of an existing epistemic standard to a new tool." Good closing move. **[DONE]** ~~But note the double-space before "is not a new principle" in the source.~~ Double space removed.

### 3.3 §5.2 — partial repetition with §4.6

"A reviewer who receives a replication package containing a search script, a screening rubric, and a skill file can assess whether the inclusion criteria were explicit before the search, whether human verification checkpoints are recorded, and whether the search strings and screening decisions are reproducible from the submitted materials. This is exactly what reviewers of quantitative replication packages do with statistical code and data."

This exact connection — workflow docs as the equivalent of statistical code for reviewer purposes — is made in §4.6, §5.2, and §6.3. It is a good connection; it does not need to be made three times at the same level of detail. Consider trimming §5.2's version to a clause that references §4.6 and moves on to the Momeni citation.

### 3.4 §7 second sentence

"Thus, systematic AI authorship has the properties of open-science practice..."

"Thus" does not track here — the sentence that follows is not an inference from the first; it is a separate summary. **[DONE]** Replaced "Thus," with "Further,".

### 3.5 §7 final sentence is anticlimactic

"It is not required to begin adopting the documentation framework."

The conclusion's final paragraph retreats from the argumentative ground the preceding paragraph established. Consider ending on the stronger of the two claims and letting the empirical-question gesture sit in the middle, not at the end. Something like: "Whether systematic AI authorship also improves average output quality in sociology is an open empirical question worth formal testing. But the case for adopting the documentation framework does not wait on that finding: the epistemic and policy arguments developed here stand on their own, and the infrastructure to implement them already exists."

### 3.6 §4.5 first paragraph

"The author's manual review remains the primary evaluative act, but it can be supported at this stage by AI-assisted review using discipline-specific reviewer skills." Sentence is good. Followed by "A structured reviewer skill with explicit criteria checks for internal consistency, unresolved inferential gaps, and framing errors — not whether the argument is compelling but whether it is coherent." The em-dash clarification is doing good work; keep. **[DONE]** "organised by principle" → "organised by type of issue". **[DONE]** §6.2 "problematic" → "divergent".

### 3.7 Document footer

**[DONE]** "Draft v2 complete — 2026-04-16" → "Draft v3 complete — 2026-04-16".

### 3.8 References — formatting still inconsistent

Mondal (line 279), Holst (273–274 — split across two lines, malformed indentation), Goyanes (271 — italics instruction and date placement inconsistent with surrounding entries), Zrubka (287 — preprint formatting stub). These are house-style issues that matter at submission but can be left until the reference list is finalised with the outstanding items from `logs/2026-04-16.md` (Blanchard, Goyanes title confirmation, etc.).

### 3.9 Agha et al. (2025)

Cited in §2.1 as TITAN; not in reference list. Already flagged in the open-questions log — noting here for completeness.

---

## On communicative effectiveness for *Sociological Science*

The paper is framed correctly as a methodological contribution. The concessive moves toward the checklist literature (§2.1, §3.3, §6.1) read as intellectually generous rather than strategic, which is the right register. The literature review is appropriately brief and cite-to-support rather than survey-style, as the journal's guidance prefers.

Two observations about audience:

**The target reader is a working sociologist who is sceptical but open.** Such a reader is likely to accept the systematic/unsystematic distinction as reasonable, to raise an eyebrow at the "stronger accountability" claim (§5.5), and to want concrete evidence that the proposed policy framework is workable by reviewers who do not yet have the competence (§6.3). The statistical-code-review analogy in §6.3 is the right move for this reader, but it is developed in two sentences. Consider whether a slightly fuller comparison — what statistical code review looked like in 2010, what it looks like now, what the parallel curve might look like for AI workflow review — would land better. This is not a critical fix; the reviewer can see the analogy work. It is a suggestion for where the paper's punch could be harder.

**The paper's style is consistent with the Skardhamar voice.** Hedging is calibrated. First person is used freely. Concessive moves are present before each critical passage. Transitions are simple ("However," "In contrast," "A related question is"). The signposting in §1 ("five connected moves") is returned to in §7. Logical tracking is explicit ("It is not merely... it is also..."). The one voice deviation I would flag is in §6.2's final sentence of the first paragraph — "with two problematic consequences that work in opposite directions" — where "problematic" is a register outlier; the paper uses it nowhere else, and "opposed" or "divergent" would fit better.

---

## Internal consistency check

Claims checked across sections:

- **Systematic = structured:** not explicitly equated anywhere. Priority 1.1.
- **Quality vs visibility:** §1 and §5.4 sit in tension. Priority 1.2.
- **"To my knowledge no work has..." claim:** stated in §2.2, §5.5, §7 with variants; scope needs tightening. Priority 2.3.
- **ICMJE paraphrase of criterion 2:** fixed in v3 — "reviewing the work critically" now matches source. Good.
- **Five moves in §1 ↔ §7 structure:** returned to. Good.
- **Three configurations in §4.3 ↔ documentation tiers in §4.6:** consistent.
- **Pre-registration analogy treatment:** §3.2 (raised, disanalogy addressed), §5.1 (treated further with Syed), §4.6 (analogous structure). Consistent; no drift.
- **"Query authorship":** introduced §1 → developed §3.2, §5.1 → returned to in §5.5 (criterion 1), §6.2, §7. Consistent.
- **"Transparency artefacts":** stable list across §3.2, §4.6, §5.2, §6.3, §7. Good.

---

## Prioritised action list

**Fix before submission:**
1. Choose one term pair (systematic/unsystematic) and apply throughout (title, §3 headings, §3.1–3.2 bodies, footer).
2. Reconcile §1 move 1 with §5.4.
3. Fix the eight-stages/five-subsections mismatch in §4.1.
4. Restructure §3.2 — three features plus a closing sentence on file structure, not four co-ordinate features.

**Strongly recommended:**
5. Split §1 paragraph 2 into scope and tool-disclosure paragraphs; rewrite the "Similarly..." sentence.
6. Rewrite §2.1 opener to open on the asymmetry rather than on "AI is transforming science."
7. Narrow the "to my knowledge no work has applied ICMJE positively" claim in §2.2.
8. Reorder §5.5's accountability paragraph so the narrower claim lands first.

**Polish:**
9. Abstract: ~~tacit decisions → tacit commitments~~ **[DONE]**; consider adding an ICMJE clause. **[MANUAL]**
10. Trim §5.2's replication-package-equivalence sentence (repetition with §4.6 and §6.3). **[MANUAL]**
11. ~~Replace "Thus" in §7 sentence 2~~ **[DONE]**; rework §7's final sentence for a stronger landing. **[MANUAL]**
12. ~~§6.2 "problematic" → "divergent"~~ **[DONE]**; ~~§4.5 "organised by principle" → "organised by type of issue"~~ **[DONE]**.
13. ~~Fix document footer to v3.~~ **[DONE]**
14. Normalise reference formatting (Holst, Mondal, Goyanes, Zrubka). **[MANUAL]**

---

## Summary of changes made in this pass

The following six mechanical edits were applied directly to `v3-draft.md`:

- Abstract: "tacit decisions" → "tacit commitments"
- §3.1 closing paragraph: double space removed before "is not a new principle"
- §4.5: "organised by principle" → "organised by type of issue"
- §6.2: "problematic consequences" → "divergent consequences"
- §7 sentence 2: "Thus," → "Further,"
- Footer: "Draft v2 complete" → "Draft v3 complete"

All items marked **[MANUAL]** above remain for the author to apply, as they involve argumentative framing, structural choices, or house-style decisions.

**Already carried, not in scope for this review:**
- Freese & Peterson attribution (notes/freese-peterson-attribution.md)
- Outstanding reference stubs (logs/2026-04-16.md open questions)
- Agha et al. (2025) reference entry

---

## Overall assessment

The argument holds. The concepts do the work they claim to do. The structure is coherent from the five moves announced in §1 through their return in §7. The ICMJE bridge is the paper's distinctive move and it lands. The policy prescription is conservative in the right sense: it frames itself as an extension of existing replication-package infrastructure rather than as a new regime, which is the right register for *Sociological Science*.

What the paper needs, in descending order of importance: terminological consistency (Priority 1.1); reconciliation of two claims that sit in apparent tension (Priority 1.2); one small structural fix to §3.2 and §4.1 (1.3, 1.4); and targeted rewrites in the introduction and the accountability paragraph of §5.5 (Priority 2). The rest is polish.

**Score: 4/5. Recommendation: Minor revisions.**
