# Logic & Language Review — v1-draft.md

**Skill applied:** logic-language-reviewer + skardhamar-style (per skill instructions for author's own manuscript)  
**Date:** 2026-04-11  
**Draft reviewed:** `draft/v1-draft.md`  

---

## Step 0: Paper type

**Discipline-reflective / programmatic** — primary type. Diagnoses a state of affairs (binary AI policies, checklist dominance), proposes a corrective framework (structured/unstructured distinction + documentation requirement), and demonstrates the framework in practice. There is a substantial theoretical component (query authorship concept). Some elements of a theoretical paper also apply. The argument chain runs: diagnosis → evidence for diagnosis → proposed framework → justification for framework → conclusion.

---

## 1. Central Question ↔ Approach Alignment

**Overall verdict: Valid, with two specific problems.**

The central diagnosis is specific and evaluable: current journal policies treat AI use as binary (use/non-use; disclose or not), and this binary misidentifies the epistemically relevant dimension. The prescription (documentation-based framework) follows directly from the diagnosis. The general alignment is sound.

**Issue 1.1 — The universal claim is not established (Critical)**

§6.2 states: "Current policies treat AI use as a binary." This is a universal claim. The evidence cited (Mondal et al. 2024, Ganjavi et al. 2024) establishes that dominant or majority policies are binary — not that all are. The paper does not quote any policy text directly, nor survey the full population of policies. One counterexample would undermine the claim as stated.

*Fix*: Replace with "Most current policies treat AI use as a binary" or "Dominant policy frameworks..." throughout. Check whether the same universal appears elsewhere (§3.3 and §1 also carry versions of this claim) and apply the same correction.

**Issue 1.2 — The §4 → §5 inferential bridge is still missing (Critical)**

This was flagged in the pre-draft logic review of the outline (Issue 2) and remains unfixed. §4 ends with the documentation and replication package discussion. §5 opens with "The epistemic function of pre-registration is frequently misunderstood as restriction." The logical connection between "here is the workflow" and "here are the epistemic properties it instantiates" is not stated. A reader who has followed §4 does not yet know why they should care about what was just demonstrated.

*Fix*: Add a connective paragraph — or at minimum a connective sentence — at the opening of §5 that names the inferential step: "The workflow described above is not merely a practical procedure. I now identify the epistemic properties it instantiates — properties that connect structured AI use to the open-science practices sociology already recognises as normative." The exact wording should be in the Skardhamar register (direct, explicit, no throat-clearing), but the move must be present.

**Issue 1.3 — The demonstration's scope is not explicitly acknowledged as illustrative**

The paper demonstrates one researcher's structured workflow for one paper. §6's policy implication is that all AI-assisted research should be documented this way. The jump from one instance to a general prescription is not explicitly addressed. The paper could be challenged: perhaps this level of documentation is feasible for a methods paper but not for standard empirical work; perhaps it requires technical skills most sociologists lack.

*Fix*: One sentence in §4.1 acknowledging that the demonstration is illustrative: "The specific configurations used here are one instance; other structured workflows, adapted to different tasks, would produce different artefacts but the same formal properties — explicit criteria, human verification, documented outputs."

---

## 2. Conceptual Precision & Consistency

**Overall verdict: Good, with four minor issues.**

The key concepts — structured/unstructured, query authorship, transparency artefacts — are defined clearly and used consistently throughout.

**Issue 2.1 — "Documentation-based framework" is invoked but not defined (Minor)**

The phrase "documentation-based framework" appears in the abstract, the introduction, and §6.3 as the prescription, but the framework itself is never explicitly constituted. What exactly are its components? The paper describes what it would require in §6.3 (show that inclusion criteria were specified, verification checkpoints recorded, etc.) but doesn't assemble these into a named, bounded framework. A reader looking to adopt or evaluate the "framework" is left to reconstruct it from the discussion.

*Fix*: Either give the framework a brief explicit statement in §6.3 ("A documentation-based framework has three requirements: first... second... third...") or, if the paper deliberately leaves the framework open-textured, acknowledge this explicitly ("I do not specify this framework in full detail here; its core requirement is simply that the evaluative burden shift from whether AI was used to whether what was done is documentable").

**Issue 2.2 — "Epistemically sound" used in §5.4 without prior definition (Minor)**

"Epistemic soundness" is used as if defined, but the paper has been working with a functional definition (structured use = errors visible and correctable) without naming it as a definition of soundness. The functional formulation is better than the abstract label.

*Fix*: Replace "epistemic soundness" with the functional formulation: "the conditions under which errors are visible and correctable" on first use.

**Issue 2.3 — "Methodological tacit knowledge" is the author's formulation, not an established term (Minor)**

The paper distinguishes this from Polanyi's original sense (craft/perceptual skill) and the distinction is explicitly acknowledged. However, the term is introduced as if it has prior standing. This is a legitimate coinage; it should be signalled as such.

*Fix*: On first use: "what might be called *methodological* tacit knowledge — the scope commitments, theoretical priorities, and evaluative standards that..."  The phrase "what might be called" correctly flags it as a formulation rather than a citation.  (The draft already uses this phrasing at §5.1 — this is already correctly handled. ✓)

**Issue 2.4 — "Binary" used in two slightly different senses (Addressable)**

§1 uses "permit or prohibit" (the policy binary); §6.2 uses "used or not used, disclosed or not disclosed" (the epistemic binary). These overlap but are not identical — a policy could permit use while making the disclosure requirement substantive (approaching a graduated framework). The paper conflates them throughout. The epistemic binary (use/non-use) is the one that matters for the argument; the policy binary (permit/prohibit) is a consequence of it.

*Fix*: Clarify that the policy binary (permit/prohibit) reflects an underlying epistemic assumption (that use/non-use is the relevant axis), and that the paper's challenge is to the underlying assumption — not just to policy implementations.

---

## 3. Theoretical Fidelity Check

**Issue 3.1 — Registered reports analogy is inaccurate (Critical)**

§3.2 contains the following: "The public commitment arrives at submission, as it does in registered reports." This is incorrect. In registered reports, in-principle acceptance is granted before data collection, based on the registered design. The defining feature of registered reports — what distinguishes them from standard preregistration — is that the commitment to publication is made before the researcher has seen the results, structurally preventing outcome-based decision making. Committing "at submission" is the exact opposite: by submission, the researcher has seen all the results. The analogy therefore works against the point the paper is making.

*Fix*: Remove "as it does in registered reports." The analogical point — that the public commitment arrives when the replication package is deposited, not during the research — can stand without this specific comparison. The correct formulation would be something like: "The public commitment arrives when the replication package is deposited at submission — analogous to retrospective OSF registration or open-materials deposits, which achieve transparency through public archiving of process materials even when the commitment was not made prospectively."

Alternatively, the paper could keep the registered reports reference but reverse the direction: note that registered reports represent the strongest form of pre-commitment (before results), that structured AI use falls short of that ideal, but that retrospective deposit of process materials recovers some of the transparency benefit. This is a more honest framing and a stronger argument.

**Issue 3.2 — Polanyi is invoked but not cited**

§5.1 makes the Polanyi connection explicit in text: "The tacit knowledge at issue is not the kind Polanyi associated with expert craft skill." Polanyi is not in the references section. For a claim about what Polanyi's concept covers, the citation should be present.

*Fix*: Add Polanyi (1966, *The Tacit Dimension*) or Polanyi (1958, *Personal Knowledge*) to the references. The 1966 work is the more accessible source for the tacit/explicit distinction.

**Issue 3.3 — Pre-registration characterisation is accurate**

The paper's characterisation of pre-registration's epistemic function — "externalisation of decisions before outcomes are known" — is standard and correct. The disanalogy (public/private) is acknowledged and addressed. ✓

---

## 4. Logical Validity of the Argument Chain

**Diagnosis → Evidence: Plausible but not tight**

The claim that policies are binary is supported by secondary literature (audits of publisher guidelines) rather than by direct citation of policy text. This is workable for a methods paper, but the claim should be weakened from universal to dominant (see Issue 1.1).

**Prescription → Justification: One unaddressed challenge**

**Issue 4.1 — Peer reviewer competence is asserted, not argued (Significant)**

§6.3 states: "Reviewers should be able to assess whether inclusion criteria were specified before the search was run, whether human verification checkpoints are recorded at each stage..." This assumes that peer reviewers currently have the skills to evaluate AI workflow documentation. Most do not — evaluation of AI pipeline documentation requires understanding of what good documentation looks like, which is precisely the expertise the paper is trying to establish. The paper notes that reviewers of quantitative replication packages evaluate statistical code, but that analogy has limits: statistical code review is at least within the domain of quantitative methods training; AI workflow documentation review is not currently in any training standard for social science reviewers.

*Fix*: Acknowledge this: "Reviewers who currently evaluate statistical replication packages face an analogous challenge — the relevant skills are acquired rather than innate — and the same professional development logic applies to AI workflow review. The documentation-based framework creates the conditions for that learning; it does not presuppose that the skills exist already." This turns a weakness into a feature: the framework both enables evaluation and builds the evaluative capacity over time.

**Issue 4.2 — The five moves in §1 vs. the three arguments in §7 (Significant)**

The introduction promises five moves. The conclusion delivers three arguments. This creates structural dissonance for a careful reader who tracks the opening promise. The three arguments in §7 are not inconsistent with the five moves — they are a re-framing at a higher level of abstraction — but the asymmetry is noticeable.

*Fix*: Either restructure the conclusion to track the five moves explicitly ("I have demonstrated five things...") or revise the introduction to promise three arguments rather than five moves. The latter would require rewriting the second paragraph of §1, but the result would be cleaner. The five-move structure is slightly listy for the paper's argumentative register; three substantive claims may serve better.

---

## 5. Precision of Language

**Issue 5.1 — "Has no good answer" should be "the wrong question" (Addressable)**

§7: "The first question has no good answer in a world where AI tools are routinely used for drafting and editing." The question "did a human write this text?" is in principle answerable — it has become difficult to answer reliably, but it is not inherently unanswerable. The problem is that it is the *wrong* question, not that it lacks an answer.

*Suggested reformulation*: "The first question is the wrong question in a world where..."

**Issue 5.2 — "Is no longer whether but how" appears twice (Addressable)**

The phrase "the question is no longer whether but how" (§1) and "The question of whether... is settled" (§2.1) express the same idea in quick succession. The repetition makes it feel like a refrain rather than an argument.

*Fix*: Remove the formulation from §1 or vary it substantially in §2.1.

**Issue 5.3 — "Structured use makes errors visible and correctable" is used as a near-slogan (Addressable)**

This formulation, or a close variant, appears in §3.3, §5.4, and §7. The repetition is useful for emphasis but starts to feel mechanical. Vary the formulation in at least one instance: "what structured use achieves is not the elimination of error but its detectability" or "the diagnostic capacity that structured use provides."

**Issue 5.4 — "I cannot claim to have demonstrated" (Addressable)**

§5.3: "I cannot claim to have demonstrated this for sociology research specifically." In Skardhamar's register, this is slightly passive and over-hedged. He would more likely own the scope limitation in active voice: "I have not demonstrated this for sociology specifically."

**Issue 5.5 — "More credibly argued" in §1 (Minor)**

§1: "A paper arguing for reproducible AI-assisted research practice is more credibly argued if the research practice producing it is reproducible." "More credibly argued" is a rhetorical claim (more convincing to readers). The paper's actual point is stronger — it's a consistency claim, not a credibility one. Suggested: "A paper arguing for reproducible AI-assisted research practice is more consistently supported if the research practice producing it is reproducible."

---

## 6. Rhetorical Effectiveness

**Issue 6.1 — The reflexivity note appears twice and is better placed in §2.2 (Critical)**

The reflexivity note — the claim that this paper's own research practice is an instance of the structured workflow — appears in both §1 (third paragraph) and at the end of §2.2. The §1 placement is premature: the reader doesn't yet know what the workflow is, so the claim cannot be evaluated. The §2.2 placement is better: it follows immediately from the gap statement and can be understood in context.

*Fix*: Remove the reflexivity paragraph from §1. Retain and strengthen the §2.2 version. The §2.2 version currently says "I note this not to sidestep the reflexive problem but to illustrate it" — this defensive phrasing should be dropped. The point is strong; it should not be apologised for. Replace with: "I note this as an illustration: the same pipeline that locates the gap in the existing literature simultaneously occupies that gap."

**Issue 6.2 — §4 → §5 transition is abrupt**

Already flagged in Issue 1.2. The rhetorical consequence: the reader who has followed §4's detailed demonstration arrives at §5 wondering why §4 was included before the epistemic argument. The missing connective sentence is also a missing rhetorical signal.

**Issue 6.3 — The conclusion's three-arguments structure vs. five-moves introduction**

Already flagged in Issue 4.2. Rhetorical consequence: a careful reader who remembers the five-move promise may feel the conclusion is incomplete.

**Issue 6.4 — The conclusion punchline is strong ✓**

"Show us yours" — this is effective, specific, and directive. Not merely aspirational. The call to action is clear. ✓

**Issue 6.5 — "As a byproduct" appears twice (Minor)**

§4.5: "structured use produces replication-ready materials as a natural byproduct." §5.2: "Structured AI use satisfies these requirements naturally — as a byproduct of the workflow." The duplication is noticeable. Vary one: "as a consequence of the workflow" or "without additional overhead."

---

## 7. Internal Consistency

**Issue 7.1 — Introduction promises five moves; §6.2 uses the phrase "two problematic consequences that work in opposite directions"**

The paper's argument structure is internally consistent, but the two-consequences framing in §6.2 (penalises structured use; permissiveness of disclosure) could be telegraphed in the introduction. Currently it is not. Minor — not a logical inconsistency, but a structural connection the introduction could anticipate.

**Issue 7.2 — The scope limitation in §4.1 about Xu and Yang**

§4.1 explains that the workflow is not an automated agent pipeline "in the sense of Xu and Yang (2026)." This contrast is useful. It appears only once and is not referenced again. The paper might briefly return to this contrast when discussing limitations (§5.4) — a sentence acknowledging that for certain tasks (well-specified, repeatable, computational), automated pipelines may be preferable to the human-in-the-loop approach, and that the workflow presented here is not a claim that automation is always worse.

**Cheng et al. double-appearance: ✓**
§3.1 (sycophancy as failure mode) and §4.4 (adversarial configuration as structural response). Well-handled.

**Query authorship double-appearance: ✓**
§3.2 (defined) and §5.1 (fully developed). Well-structured.

**Pre-registration analogy double-appearance: ✓**
§3.2 (introduced with disanalogy) and §5.1 (developed; cross-references §3.2 explicitly). Well-handled.

---

## 8. Scope, Limitations & Honesty

**Issue 8.1 — Peer reviewer competence (already flagged as Issue 4.1)**

**Issue 8.2 — The Zeng et al. limitation is correctly handled ✓**

"I cannot claim to have demonstrated this for sociology research specifically" — scope limitation is stated at the right point, in the right register. ✓

**Issue 8.3 — The demonstration's single-instance scope needs explicit acknowledgment**

Already flagged as Issue 1.3. The paper demonstrates one workflow for one paper type. The policy prescription applies to all AI-assisted research. This gap should be acknowledged explicitly.

---

## 9. Conclusion, Take-Home Message & Punchline

**Issue 9.1 — Three arguments vs. five moves (flagged as Issue 4.2)**

**Issue 9.2 — The "future research" paragraph is well-positioned**

The final paragraph calls for "replication studies comparing structured and unstructured AI use across standard sociology research tasks." This is specific, not generic, and is followed by "It is not required to begin adopting the documentation framework" — which correctly frames the research agenda as supplementary to the present argument, not as a condition for acting on it. ✓

**Issue 9.3 — The conclusion introduces no new material ✓**

All claims in the conclusion track claims made earlier in the paper. ✓

---

## Skardhamar style check

**Hedging calibration:**
- "I argue" — used for defended positions throughout ✓
- "I suggest" — used for the Zeng et al. generalisation and speculative extension ✓
- "I cannot claim to have demonstrated" — slightly over-hedged; see Issue 5.4
- No instances of over-claiming or under-hedging beyond those flagged ✓

**Concessive moves:**
- §2.2 on checklists: "I do not want to dismiss this contribution" ✓
- §3.3 on checklists again: "I have already acknowledged what these instruments achieve" ✓
- §6.1 on journal policies: "largely sensible" ✓
- All required concessive moves present ✓

**Logical tracking:**
- "This is what query authorship amounts to" — effective explicit tracking ✓
- "This changes what academic integrity means" — effective ✓
- Weak: the §4 → §5 joint (see Issue 1.2 and Issue 6.2)
- "It then follows that..." — used appropriately ✓

**Topic sentences:**
- Most paragraphs open with substantive claims ✓
- §5.1 opens with "The epistemic function of pre-registration is frequently misunderstood as restriction" — this opens on the negative (what it is NOT), which is a legitimate move but could be inverted: open with the positive, then introduce the misunderstanding as a contrast. Minor.

**One stylistic cluster: inventory prose in §4.2**
The paragraph enumerating the two-route search procedure is necessary but reads more as methodology reporting than argument. This is appropriate given the section's function (demonstration), but the transition back to argumentative mode at the end of §4.2 ("This query formulation is an instance of query authorship") is slightly abrupt. A sentence bridging the descriptive and argumentative registers would help.

---

## Summary of issues by priority

### Critical — must be fixed before submission

| # | Issue | Location |
|---|-------|----------|
| 1.1 | "Current policies treat AI use as a binary" — universal claim not established | §6.2 and elsewhere |
| 1.2 | §4 → §5 inferential bridge is missing | Between §4.5 and §5.1 |
| 3.1 | Registered reports analogy is inaccurate | §3.2 |
| 6.1 | Reflexivity note duplicated; §1 version is premature; defensive language in §2.2 version | §1 (para 3) and §2.2 |

### Significant — should be addressed in revision

| # | Issue | Location |
|---|-------|----------|
| 1.3 | Demonstration is one instance; this should be explicitly acknowledged | §4.1 |
| 2.1 | "Documentation-based framework" is invoked but not constituted | §6.3 |
| 3.2 | Polanyi invoked in text but not cited | References |
| 4.1 | Peer reviewer competence not acknowledged | §6.3 |
| 4.2 | Five moves in §1 vs. three arguments in §7 — structural dissonance | §1 and §7 |

### Addressable in revision

| # | Issue | Location |
|---|-------|----------|
| 2.4 | "Binary" used in two slightly different senses | §1, §6.2 |
| 5.1 | "Has no good answer" → "the wrong question" | §7 |
| 5.2 | "Whether but how" phrase appears twice | §1 and §2.1 |
| 5.3 | "Errors visible and correctable" is near-slogan; vary formulation | §3.3, §5.4, §7 |
| 5.4 | "I cannot claim to have demonstrated" → active construction | §5.3 |
| 5.5 | "More credibly argued" → consistency claim, not credibility | §1 |
| 6.5 | "As a byproduct" appears twice | §4.5 and §5.2 |

---

## 10. Overall Assessment

**Score: 3.5 / 5 — Good with targeted revisions required**

The argument holds from diagnosis through prescription. The core conceptual contributions (structured/unstructured distinction, query authorship) are clearly developed and consistently applied. The concessive register is maintained throughout. The epistemic argument in §5 is the paper's strongest section. The conclusion is directive and specific.

The most consequential single error is the registered reports analogy (Issue 3.1) — it is factually wrong and currently works against the point being made. The missing §4 → §5 bridge (Issue 1.2) leaves the demonstration section feeling incomplete. The duplication of the reflexivity note (Issue 6.1) introduces a premature claim in the introduction that a reader cannot yet evaluate.

The universalising claim about binary policies (Issue 1.1) is correctable with two-word substitutions but should be applied consistently throughout.

**Recommendation: Revise — targeted fixes to the critical and significant issues above. No structural reconceptualisation required.**

---

*Review complete — 2026-04-11*
