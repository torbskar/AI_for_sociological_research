# Note: Logic & Language Review of Outline
## Date: 2026-04-10
## Source: logic-language-reviewer skill applied to outline.md

---

## Paper type

Discipline-reflective / programmatic — diagnoses a state of affairs (binary AI policies, checklist dominance), proposes a corrective framework (structured/unstructured distinction + documentation requirement), and demonstrates the framework in practice. Significant theoretical component (query authorship).

---

## Critical issues — resolve before drafting

### 1. "More productive" in the core argument is unsupported

The core argument claims the documentation framework is "both more honest *and more productive* than current journal policy." "More honest" is supported. "More productive" is either undefined or contradicted by §5.3, which explicitly hedges the reliability claim (Zeng et al. is from data science; the sociology claim cannot be demonstrated). The core argument cannot promise productivity while the body retreats to "I suggest."

**Fix**: Replace "more productive" with "more consistent with existing open-science infrastructure" or drop it. Suggested replacement for the core argument sentence: "...a documentation-based framework that recognises this distinction is both more epistemically honest and more consistent with existing open-science infrastructure than current journal policy."

### 2. The §4 → §5 inferential bridge is unspecified

§4 is explicitly "descriptive"; §5 is "the normative argument." The outline does not specify the logical link between them. Without it, the two sections will feel juxtaposed rather than connected. Readers will ask "so what?" after §4.

**Fix**: Add a transition note to the outline (and signal for the draft) that names the inferential step: "I have shown you what the workflow looks like; I now identify the epistemic properties it instantiates." This must be written explicitly in the draft's connecting paragraph, not left implicit.

### 3. Query authorship → policy implication is dangled, not developed

§5.1 states that query authorship "has implications for attribution and academic integrity beyond the AI context." §6 does not pick this up. The policy section addresses documentation requirements and replication packages but says nothing about attribution or authorship conventions.

**Fix**: Either develop the link in §6 (what does query authorship imply for authorship declarations, CRediT, or academic integrity policy?) or remove the claim from §5.1. Currently it opens a door the paper does not walk through.

### 4. §6.3 prescription is incomplete

The conservative framing is rhetorically effective. But the proposal — that reviewers assess whether the structured process was appropriate — does not specify what "appropriate" means or what reviewing a skill file or search log involves. The evaluative burden is shifted to peer review without explaining what peer review of an AI workflow actually looks like.

**Fix**: Add at least a gesture toward criteria — e.g., "reviewers should check whether inclusion criteria were explicit before the search, whether human verification checkpoints are recorded, and whether the search string and screening decisions are reproducible from the submitted materials." Without this, the proposal remains aspirational.

### 5. The conclusion (§7) is underpowered

Three of five bullets are recaps; one calls for future research; only the query authorship bullet adds something. The conclusion does not answer: what should a sociologist *do* differently after reading this? What should a journal editor *do* differently?

**Fix**: The final bullet should state a directive, not a research agenda. The punchline should be: sociologists who work this way are already doing open science; the infrastructure to recognise it exists. The call to action is to adopt the documentation-based policy framework now, not contingent on future validation. "Future validation" should at most be a subordinate clause, not the closing note.

---

## Significant issues — resolve before drafting

### 6. Pre-registration analogy has a known disanalogy

Pre-registration is a *public, timestamped commitment* before data collection. Structured AI use is a *private, logged protocol* before running the tool. The analogy holds in spirit but breaks on two points: (a) publicity vs. privacy of the commitment; (b) pre-registration structurally prevents cherry-picking by public commitment; structured AI use does not obviously prevent a researcher from revising queries after seeing outputs and logging only the final version.

**Fix**: Acknowledge the disanalogy in §5.1 and explain why it doesn't defeat the analogy. The response might be: the two-tier documentation structure (working logs + final supplement) addresses (b) — the logs record the iterative process, not just the end-state. For (a): the public commitment comes at submission, when the replication package is deposited. This is similar to how registered reports work post-hoc in some contexts. This argument needs to be made explicitly.

### 7. "No existing work..." claims are too absolute

§2.2 makes four consecutive "No existing work..." statements. These are empirically risky. Törnberg (2024), Davidson & Karell (2025), and Blanchard et al. (2025) all implicitly distinguish between more and less systematic AI use — they just don't theorise this distinction as *the* policy-relevant axis. One counterexample undermines the gap claim.

**Fix**: Replace each with "No existing framework *explicitly theorises* the structured/unstructured distinction as *the* fundamental policy-relevant axis" and equivalent careful formulations.

### 8. Tacit knowledge / Polanyi bridge is implicit

Polanyi's insight is about expert craft knowledge embedded in practice — motor and perceptual skill. The application here is about methodological decision criteria. These are not the same kind of tacit knowledge. The bridge must be made explicit in the draft: what specifically is tacit in unstructured AI use that structured use externalises? The answer the outline implies is: theoretical choices, scope commitments, evaluative standards. That answer needs to be stated, and the connection to Polanyi made through it, not assumed.

### 9. Checklist characterisation is inconsistent

§2.2 says checklists "have nothing to say about" process soundness — dismissive. §3.3 calls them "valuable; just insufficient" — concessive. The draft will inherit this inconsistency. Decide: concessive throughout (checklists address one real problem but not the one that matters most) or more critical (checklists presuppose what should be established). The concessive register is more defensible and less likely to antagonise checklist authors who might review the paper.

---

## Addressable issues — can be fixed during drafting

### 10. Self-reference error in §4 function note
"Descriptive — this is how it works, not why it is better (that comes in section 4)." Should be "section 5."

### 11. "The binary is wrong" is too combative
Replace with "the binary misidentifies the epistemically relevant dimension" or "the binary is the wrong cut."

### 12. "This is not a trade-off" overstates Zeng et al.
Zeng et al. shows correlation between reproducibility and accuracy in data science tasks. Replace with "this suggests it need not be a trade-off" or "the evidence from adjacent fields is consistent with there being no trade-off."

### 13. "Journals have no principled basis" will antagonise
Replace with "journals that already apply replication package requirements to quantitative work face a consistency challenge in treating AI workflow documentation differently."

### 14. Query authorship needs a one-clause definition in §1
The introduction lists it as a contribution but does not define it. Add a defining clause: "the concept of *query authorship* — the argument that formulating a search string or review configuration encodes the researcher's intellectual commitments in a verifiable form."

### 15. Structural question: §4 before §5?
The current order asks readers to follow a demonstration before they understand why the properties demonstrated matter. The alternative — epistemic argument (§5) before demonstration (§4) — would allow the workflow to serve as evidence for the epistemic claims rather than §5 explaining what §4 was doing. Worth deciding before drafting, not during.

### 16. §4.1 overview inconsistent with consolidated structure
The overview lists "NotebookLM source sets" as a standalone artefact, but source synthesis was folded into §4.2. The artefacts list in §4.1 should reflect this.

### 17. Query authorship creates vs. documents intellectual contribution
The current framing implies structured use uniquely *creates* the researcher's intellectual contribution. The more defensible claim is that it *documents and verifies* it — unstructured use also involves intellectual choices, they are simply invisible. Change framing accordingly throughout.

---

## Overall score: 3/5 — Major revisions to the outline needed before drafting begins

Issues 1–5 are architectural decisions that cannot be patched in revision. Issues 6–9 require additional argumentative content. Issues 10–17 are language and framing fixes that can be handled during drafting if the architectural issues are resolved first.
