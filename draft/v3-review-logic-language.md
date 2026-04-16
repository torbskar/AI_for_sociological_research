# Logic & Language Review — v3-draft.md

**Skills applied:** logic-language-reviewer + skardhamar-style  
**Date:** 2026-04-16  
**Draft reviewed:** `draft/v3-draft.md`  
**Previous review:** `draft/v2-review-logic-language.md` (score 3.5/5)

---

## Step 0: Paper type

**Discipline-reflective / programmatic** — unchanged. The argument chain runs: diagnosis (binary AI policies misidentify the epistemically relevant axis) → evidence for diagnosis → proposed alternative (systematic AI authorship + documentation-based policy framework) → justification → conclusion.

---

## Status of carry-forward issues from v2 review

| Issue | Status in v3 |
|---|---|
| NC1 — §1 scope paragraph (grammar, dangling construction, scope expansion) | **SUBSTANTIALLY FIXED** — all three specific errors corrected. Minor residuals: "focus" appears twice in the opening sentence; "system and protocols" (sentence 3) is vague. |
| prev 1.2 — §4→§5 inferential bridge missing | **ATTEMPTED BUT NOT FIXED** — three new sentences added at the end of §4.6 as a bridge, but they introduce subject-verb errors and a logically thin argument. See NC-v3-1. |
| prev 4.2 — Five moves (§1) vs. three arguments (§7) | **PARTIALLY FIXED** — the explicit "I have argued for three things" is gone from §7. The structural mismatch between five announced moves and the conclusion's coverage is partially resolved, but §7 does not return to the five moves in a systematic way. See NS-v3-4. |
| prev 4.1 — Peer reviewer competence not acknowledged in §6.3 | **NOT FIXED** — §6.3 still asserts "Reviewers or editor should be able to assess the configuration choices made are theoretically justified" without acknowledging that this requires competence most peer reviewers currently lack. |
| NA3 — "without an explicit criteria" (§5.4) | **NOT FIXED** — still reads "without an explicit criteria." |
| NS1 — §2.2 ICMJE gap claim missing "To my knowledge" | **FIXED** |
| NS2 — ICMJE pointer directs to "§5" not "§5.5" | **FIXED** — now reads "towards the end of §5" |
| NS3 — "I want to make a pointed but careful claim here" meta-announcement | **FIXED** — removed |
| NS4 — §5.5 para 2 "is a direct claim" awkward construction | **FIXED** — "query authorship maps directly" |
| NS5 — §4.6 sentence fragment "documented the _query-authorship_" | **FIXED** — removed |
| NA1 — §2.1 opening sentence (SV disagreement, "and transforming") | **FIXED** |
| NA2 — "or should be developed to" dangling preposition | **FIXED** |
| NA4 — Incomplete constructions in §5.4 | **FIXED** |
| NA5 — Non-parallel "high quality or eliminating errors" | **FIXED** |
| NA6 — Weak §4.6 opener | **FIXED** |
| prev 1.1 — §6.2 binary claim overstated | **FIXED** — "Probably the most common policy structure" adequately hedges |
| prev 1.3 — §4.1 scope not acknowledged | **FIXED** — scope note added to §4.1 |
| prev 5.3 — "errors visible and correctable" near-slogan | **NOT FULLY FIXED** — still appears in §3.3 and in §7 with identical phrasing |
| NC-new-1 — §2.2 "theorises" missing "that" | **RESOLVED** — "theorises the systematic/unsystematic distinction *as* the fundamental policy-relevant axis" is grammatically defensible (transitive "theorise" + "as"); no change required |
| NS-new-2 — §7 "through analysis of data" breaks em-dash list | **FIXED** |

**Net:** 14 issues fully resolved; 1 partially resolved; 4 not fixed (prev 1.2 attempted and new errors introduced; prev 4.2 partially; prev 4.1; NA3; prev 5.3).

---

## New issues — Critical

### NC-v3-1 — §4.6 bridge paragraph: subject-verb errors and logically thin argument

The three sentences added at the end of §4.6 to bridge to §5 introduce new problems:

> "While the artifacts produced by systematic AI authorship is documentation, these outputs also matter epistemically. A well-crafted AI workflow starts with a structured query and a setup that guides the project thereafter. An analogy is pre-registration of empirical studies, where the research question and procedure is made into an explicit study protocol."

**Subject-verb disagreement (sentence 1)**: "artifacts...is documentation" — plural subject requires "are." 

**Subject-verb disagreement (sentence 3)**: "the research question and procedure is made" — compound subject requires "are made."

**Vague claim (sentence 1)**: "these outputs also matter epistemically" — matter how? The sentence does not specify. This is not answered by sentences 2–3.

**Redundancy (sentence 2)**: "A well-crafted AI workflow starts with a structured query and a setup that guides the project thereafter" restates §§3–4's argument without advancing it. A bridge should do connective work, not recapitulate.

**Logical mismatch (sentence 3)**: The pre-registration analogy was already introduced and developed in §3.2 (including the disanalogy). Re-introducing it here as if for the first time ("An analogy is pre-registration...") creates a false impression of novelty and duplicates content.

**The bridge does not bridge**: The preceding §4.6 text ends with a strong formulation: "A replication package containing these materials is at once a transparency artefact and a proof of concept." The added sentences detour through a garbled pre-registration observation and then §5.1 opens on a different pre-registration point ("can, or perhaps even should, be included in pre-registrations"). The connective work is not done. 

What is needed is a sentence that draws out the *epistemic* implication of the documentation just described — not a new analogy, but a logical consequence: that the documentation produced makes the epistemic properties of the workflow available for evaluation, which is what §5 examines. Something along these lines: "The documentation produced across these stages is not merely a record — it makes the epistemic quality of the process available for evaluation in ways that undocumented research does not permit. Section 5 examines those epistemic properties directly." The three added sentences should be removed and replaced with a single connective sentence of this kind.

---

## New issues — Significant

### NS-v3-1 — §5.1 opening: misspelling, awkward hedging, and defective logical connector

> "The setup and configuration files can, or perhaps even should, be included in pre-registerations along with other parts of the protocol as suggested by open science guidelines. But there is also a structural similarity to pre-registration."

**Misspelling**: "pre-registerations" should be "pre-registrations."

**Hedging incoherence**: "can, or perhaps even should" — the "can" is redundant with "should"; the intended hedge is simply "perhaps should" or "should, perhaps." The comma-bracketed disjunction reads as clumsy.

**Defective "also"**: Sentence 2 says "there is *also* a structural similarity." For "also" to function, it must refer to a first thing of which structural similarity is the second. Sentence 1 is about including configs in pre-registration platforms — not about a first similarity. The connector is logically misplaced.

**Topic-sentence failure (skardhamar-style)**: The section is titled "Making tacit commitments explicit" and its thesis is externalisation. The opening sentence is a peripheral observation about pre-registration protocols. By style standards, the topic sentence should commit immediately to the section's main argument. The current opener delays and misdirects.

*Fix*: Remove sentence 1 or relocate it to §3.2 (where the pre-registration analogy and the public-vs-private disanalogy are discussed). Open §5.1 directly with the externalisation argument: "The epistemic function of pre-registration is frequently misunderstood as a restriction..." — which is the current second paragraph's opening and works well as the section's topic sentence.

### NS-v3-2 — §6.3: number mismatch and missing "that"

> "Reviewers or editor should be able to assess the configuration choices made are theoretically justified and accountable."

Two grammatical errors in one sentence:

**Number mismatch**: "Reviewers or editor" — "Reviewers" is plural; "editor" is singular. Should be "Reviewers or editors."

**Missing "that"**: "assess the configuration choices made are theoretically justified" — needs "that": "assess *that* the configuration choices made are theoretically justified."

*Fix*: "Reviewers and editors should be able to assess that the configuration choices made are theoretically justified and accountable."

Note: prev 4.1 (not acknowledging reviewer competence) also remains unaddressed in this sentence. The sentence should concede that this capacity requires familiarity with structured AI workflows that most current reviewers do not have, then argue that this is an acquirable competence as documentation norms develop — as it has been for statistical code review.

### NS-v3-3 — §7 para 1: weak interpolated sentence; spelling inconsistency

> "Systematic AI authorship has a workflow and pipeline from beginning to end, which produces artifacts that are accountable and transparent."

This sentence was inserted between "I have argued that..." and "Thus, systematic AI authorship has the properties of open-science practice." It introduces three problems:

**Redundancy**: "a workflow and pipeline from beginning to end" — a pipeline *is* a workflow from beginning to end; this is a near-tautology and adds nothing.

**Wrong predicate**: "artifacts that are accountable and transparent" — artefacts are not accountable; research *processes* and *researchers* are accountable. Artefacts support accountability; they do not possess it. "Produces artefacts that support accountability and transparency" would be accurate.

**Spelling inconsistency**: "artifacts" (American) — the paper uses "artefacts" (British) throughout. This sentence also disrupts the logical flow: "I have argued... [statement of argument]. [Redundant summary sentence]. Thus, systematic AI authorship has the properties..." The pivot to "Thus" is undercut by the interposed sentence.

*Fix*: Remove the interpolated sentence. The paragraph reads better as: "I have argued that the systematic/unsystematic AI authorship distinction — not the use/non-use binary — is the epistemically relevant axis for evaluating and regulating AI-assisted research. Thus, systematic AI authorship has the properties of open-science practice..."

### NS-v3-4 — §1/§7 structural mapping: five moves announced, conclusion covers them unevenly

The five moves announced in §1 are:

1. Systematic/unsystematic distinction + epistemic quality (distinct not merely in transparency)
2. Query authorship concept
3. Systematic workflow for sociology across the research pipeline
4. Systematic AI authorship instantiates open-science properties, particularly the externalisation function of pre-registration
5. Journal policy implications + documentation-based framework

§7 covers moves 1, 2, 4, and 5, but move 3 — the workflow description — appears only as a single clause ("Systematic AI authorship has a workflow and pipeline from beginning to end"), which is too thin to constitute a conclusion to a full section (§4). A reader who read the introduction expecting the conclusion to return to what a systematic workflow delivers for sociology will find the conclusion silent on this. The §7 treatment of the five moves is uneven rather than structurally mismatched (the explicit numerical mismatch is resolved), but the unevenness is visible and worth correcting.

*Fix*: Add one sentence to §7 that retrieves move 3 specifically — what systematic AI authorship produces at the workflow level that a researcher can point to and submit. This can be brief. The fourth paragraph of §7 ("Sociologists who build explicit search criteria, maintain screening logs...") does this implicitly but does not connect it explicitly to the workflow section.

---

## New issues — Addressable

### NA-v3-1 — §3.1 Barrie et al.: year missing

> "Barrie et al. find that LLM performance variance is often unacceptably high..."

In-text citation gives no year. Reference entry confirms "(2025)." *Fix*: "Barrie et al. (2025) find that..."

### NA-v3-2 — §5.4 "the misclassification" — definite article presupposes unintroduced referent

> "The misclassification will be visible in the documented outputs and correctable through the human verification checkpoint."

"The misclassification" uses the definite article, presupposing a specific misclassification has been named. No specific misclassification was named in the preceding sentences — the paragraph speaks generically of "LLM error." *Fix*: "Any misclassification will be visible..." or "Such errors will be visible in the documented outputs..."

### NA-v3-3 — §5.1 "externalizing ideas" — imprecise term and spelling

> "Structured AI use functions the same way by externalizing ideas (whether time-stamped or not)."

**Imprecise term**: "externalizing ideas" — the section's thesis is externalisation of *tacit commitments* or *tacit decisions*. "Ideas" does not carry the epistemically specific meaning that the surrounding argument requires. The section heading says "Making tacit commitments explicit"; the body should use the same frame.

**Spelling**: "externalizing" (American) — should be "externalising" (British) for consistency with the rest of the paper.

**Parenthetical placement**: "(whether time-stamped or not)" is an odd qualifier after "externalizing ideas"; it is clearly responding to the pre-registration disanalogy (public timestamp), but the disanalogy was handled in §3.2. Reappearing here without explanation it reads as a floating caveat.

*Fix*: "Structured AI use functions the same way: to direct the AI, the context must be specified..." — removing the vague parenthetical and opening directly onto the specification requirement that follows.

### NA-v3-4 — §4.6 pre-registration analogy garbled

> "Both tiers are present in the replication package because they serve different functions. This mirrors how pre-registration works: the registered plan and the final methods section are both legitimate, and neither substitutes for the other."

"The registered plan and the final methods section are both legitimate" — the point of the analogy is not that both are legitimate but that both are *evidentially necessary for different reasons*. As written, the sentence defends against a criticism that neither tier is legitimate, which is not the concern. The analogy should convey that the pre-registration plan provides process integrity evidence, while the methods section provides replication materials — just as the logs (tier 1) and the supplementary materials (tier 2) serve different evidential functions.

*Fix*: "This mirrors how pre-registration works: the registered plan and the final methods section each provide evidence the other cannot — the plan documents the prior commitment, the methods section specifies what was actually done. Neither substitutes for the other, and both are in the replication package for that reason."

### NA-v3-5 — §4.1 typographic: hyphen instead of em-dash

> "the researcher handles judgement - even if discussing options with the AI before deciding"

Hyphen used where an em-dash is required. *Fix*: "the researcher handles judgement — even if discussing options with the AI before deciding."

---

## Theoretical fidelity check

### ICMJE criteria (§5.5) — verified

The four criteria are confirmed against the current ICMJE recommendations:

1. Substantial contributions to the conception or design of the work, or to the acquisition, analysis, or interpretation of data  
2. Drafting the work or *reviewing it critically* for important intellectual content  
3. Final approval of the version to be published  
4. Agreement to be accountable for all aspects of the work in ensuring questions related to accuracy or integrity are appropriately investigated and resolved

The paper's characterisation is accurate in substance, with one precision point: ICMJE criterion 2 specifies "drafting the work or **reviewing** it critically" — the paper's §5.5 renders this as "drafting or **revising** the work critically." "Reviewing critically" (providing critical assessment, which may or may not result in textual changes) is not identical to "revising" (actually modifying the text). The distinction matters because a researcher who critically reads and redirects AI-produced drafts, but does not personally retype passages, satisfies the ICMJE's "reviewing critically" — a point the author-input file documentation is designed to establish. The paper's use of "revising" is slightly narrower than the ICMJE's "reviewing" and inadvertently implies a more restrictive standard. The criterion should be quoted or paraphrased as "reviewing critically," which also better maps to what author-input files document (critical assessment and redirection, not necessarily rewriting).

### Mitchell et al. (2022) tacit knowledge (§5.1) — no issue

The distinction between "inherent tacit knowledge" (motor and perceptual; resists verbal articulation) and "implicit tacit knowledge" (scope commitments and evaluative standards; could be articulated if prompted) is attributed to Mitchell et al. correctly and used precisely. No discrepancy.

### Freese & Peterson (2017) (§5.2) — characterisation plausible, author to verify

The paper attributes to Freese and Peterson a claim that "sociology's engagement with open science norms [is] incomplete" and that "documentation of qualitative and interpretive decisions" is "a persistent gap." This is a plausible reading of their argument for replication in sociology, but the specific emphasis on *qualitative and interpretive decisions* as a gap identified by Freese and Peterson (as opposed to a gap the paper identifies using their framework) should be verified against the source. The sentence structure implies it is Freese and Peterson's own diagnosis; if it is the author's inference from their argument, the attribution should be adjusted accordingly.

---

## Skardhamar-style net assessment

**Substantial improvements from v2 → v3:**

- The tool disclosure paragraph (T1) is well-executed: names Claude once, identifies the three Claude-specific terms, asserts the principle generalises. Clean register, no over-explanation.
- The four empirical additions to §§5.1–5.5 (L3–L6) are smoothly integrated. The extended query authorship definition in §5.1 ("A well-formed analytical specification embeds a theory of measurement and causal structure...") is the paper's best new formulation — it instantiates the concept precisely and advances the argument.
- The §7 additions (L8) that bring "document analytical decisions" and "record their iterative decision process" into the conclusion are well-placed and do not disrupt the paragraph's rhythm.

**Register concerns introduced in v2-manualEdit and carried into v3:**

The §4.6 bridge paragraph (NC-v3-1) and the §5.1 opening (NS-v3-1) both fall below the draft's established register. By skardhamar-style standards, both violate the topic-sentence-commits-immediately principle and both contain hedging that is either incoherent (the "can, or perhaps even should" construction) or misplaced (the "also" connector). These are the two most stylistically problematic passages in the draft.

**Remaining sloganeering instance (prev 5.3):**

"Makes errors visible and correctable" appears with identical phrasing in §3.3 ("visible and correctable") and §7 ("makes errors visible and correctable"). Two instances still cross the near-slogan threshold. The §3.3 instance is the natural location for the full formulation; §7 should vary it — "detectable and correctable," "visible and therefore addressable" (already used in §5.4 and preferable), or simply "correctable."

**Strong formulations to preserve:**

- §5.5 bridge to §6: "Binary prohibition addresses the easy question (AI cannot be an author) while leaving the harder one unasked. Blanket disclosure answers neither." — the paper's sharpest sentence.
- §6.2 "disadvantages honest actors while leaving dishonest ones undetected" — precise and apt.
- §7 para 4: "Journals should ask not 'did you use AI?' but 'show us your systematic process.'" — a clean punchline; the last clause "That is a tractable request, it requires no new infrastructure, and it is more epistemically useful than either blanket prohibition or blanket disclosure" delivers the concluding argument effectively.

---

## Summary of all open issues

### Critical

| # | Issue | Location |
|---|---|---|
| NC-v3-1 | §4.6 bridge paragraph: SV errors, vague claim, redundancy; bridge does not bridge | §4.6 final paragraph |

### Significant

| # | Issue | Location |
|---|---|---|
| NS-v3-1 | §5.1 opener: "pre-registerations" misspelling; "can, or perhaps even should" hedging; defective "also" connector; topic-sentence failure | §5.1 para 1 |
| NS-v3-2 | §6.3: "Reviewers or editor" (number); "assess the configuration choices made are" (missing "that") | §6.3 para 2 |
| NS-v3-3 | §7 para 1: interpolated sentence — tautologous, wrong predicate, spelling inconsistency | §7 para 1 |
| NS-v3-4 | §1/§7 structural mapping: five moves announced; §7 covers move 3 (workflow) only in passing | §1 and §7 |
| [prev 4.1] | §6.3 does not acknowledge reviewer competence gap | §6.3 |

### Addressable

| # | Issue | Location |
|---|---|---|
| NA-v3-1 | Barrie et al.: year missing from in-text citation | §3.1 |
| NA-v3-2 | "The misclassification" — presupposes unintroduced referent | §5.4 |
| NA-v3-3 | "externalizing ideas" — imprecise, American spelling, parenthetical awkward | §5.1 |
| NA-v3-4 | §4.6 pre-registration analogy garbled ("both legitimate") | §4.6 |
| NA-v3-5 | Hyphen instead of em-dash in §4.1 | §4.1 |
| NA3 | "without an explicit criteria" — number error | §5.4 |
| [prev 5.3] | "errors visible and correctable" — second instance in §7 should be varied | §3.3 / §7 |

### Theoretical fidelity (author verification)

| Issue | Location |
|---|---|
| ICMJE criterion 2: paper says "revising"; ICMJE says "reviewing it critically" — paraphrase should be adjusted | §5.5 |
| Freese & Peterson (2017): "documentation of qualitative and interpretive decisions as a persistent gap" — verify whether this is their diagnosis or the author's inference | §5.2 |

---

## Overall assessment

**Score: 4 / 5 — Good, minor to moderate revisions**

v3 represents a substantial advance. Fourteen issues from the v2 review are fully resolved, and several of the new substantive additions (the empirical parallel in query authorship, the analytical specification language in §5.1, the tool disclosure in §1) are executed well. The draft is close to submission quality.

The score is limited by one new critical issue (the §4.6 bridge paragraph, which attempts to fix a persistent problem but introduces grammar errors and logical thinness), two persistent structural issues (reviewer competence in §6.3; systematic mapping of §1 moves in §7), and a cluster of addressable new errors introduced in v2-manualEdit. None of the issues are intractable. The §4.6 bridge is the most urgent: the three added sentences should be replaced with a single connective sentence drawing the epistemic implication of the documentation described, which is what §5 then examines.

**Recommendation: Minor to moderate revisions. All required changes are local and can be addressed in a single editing pass. No structural reconceptualisation is needed.**

**Priority sequence:**

1. Replace §4.6 bridge paragraph with a single connective sentence (NC-v3-1) — this also closes prev 1.2
2. Remove §7 para 1 interpolated sentence; correct "artefacts" spelling (NS-v3-3)
3. Fix §5.1 opener: remove or relocate sentence 1; open on the externalisation argument; fix "also" connector (NS-v3-1)
4. Fix §6.3: "Reviewers and editors"; add "that"; add acknowledgement of reviewer competence gap (NS-v3-2 + prev 4.1)
5. Add brief retrieval of move 3 to §7 (NS-v3-4)
6. Fix ICMJE criterion 2 paraphrase from "revising" to "reviewing critically" (Theoretical fidelity)
7. Address all addressable issues in one pass: Barrie et al. year (NA-v3-1); "the misclassification" (NA-v3-2); "externalizing ideas" (NA-v3-3); pre-reg analogy (NA-v3-4); em-dash (NA-v3-5); "explicit criteria" (NA3); §7 sloganeering (prev 5.3)
8. Author: verify Freese & Peterson attribution (§5.2)

---

*Review complete — 2026-04-16*
