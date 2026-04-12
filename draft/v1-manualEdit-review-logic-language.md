# Logic & Language Review — v1-draft - manualEdit.md

**Skill applied:** logic-language-reviewer + skardhamar-style  
**Date:** 2026-04-11  
**Draft reviewed:** `draft/v1-draft - manualEdit.md`  
**Previous review:** `draft/v1-review-logic-language.md`

---

## Step 0: Paper type

**Discipline-reflective / programmatic** — unchanged from previous review.

---

## Status of issues from the previous review

Before identifying new issues, I track which critical and significant issues from the v1 review were addressed in the manual edit.

| Previous issue | Status |
|---|---|
| 1.1 — "Current policies treat AI use as a binary" (universal claim) | **NOT FIXED** — §6.2 still reads identically |
| 1.2 — §4 → §5 inferential bridge missing | **NOT FIXED** — §5 still opens without a connective sentence |
| 1.3 — Demonstration scope not acknowledged as illustrative | **NOT FIXED** |
| 3.1 — Registered reports analogy inaccurate | **NOT FIXED** — §3.2 still reads "as it does in registered reports" |
| 3.2 — Polanyi not cited | **PARTIALLY FIXED** — now reads "Polanyi (REF)"; placeholder present |
| 4.1 — Peer reviewer competence not acknowledged | **NOT FIXED** |
| 4.2 — Five moves vs. three arguments (§1 vs. §7) | **NOT FIXED** |
| 6.1 — Reflexivity note duplicated; §2.2 version is defensive | **NOT FIXED** — both instances remain; §2.2 still reads "I note this not to sidestep the reflexive problem but to illustrate it" |
| 5.1 — "Has no good answer" (§7) | **NOT FIXED** |
| 5.2 — "Whether but how" appears twice | **NOT FIXED** |
| 2.1 — "Documentation-based framework" undefined | **NOT FIXED** |

All critical issues from the previous review are unaddressed.

---

## New issues introduced in the manual edit

The following problems were not present in v1 and have been introduced by the manual edits. They are grouped by severity.

---

### Critical — must be fixed

**C1 — "Three" defining features, but four are listed (§3.2)**

§3.2 opens: "Structured AI use has **three** main defining features." It then lists: (1) explicit criteria, (2) human verification, (3) documented outputs — and then immediately adds: "Fourth, there is a documented workflow or pipeline with associated folder structure to support the progress." The contradiction is direct and in close proximity. A reader encounters the number claim and the violation in the same section.

*Fix*: Either revise the count to four (and consolidate/justify the fourth feature clearly), or absorb the fourth point into one of the existing three. If kept as four, the concept note that follows ("We might refer to this kind of structure as the AI-architecture...") would also need tightening.

**C2 — Abstract is now over-length, registers below target, and violates the tool-agnostic principle**

The manually edited abstract runs approximately 175 words against Sociological Science's 150-word maximum. More substantively, it violates the paper's own stated tool-agnostic principle in the first sentence: "The introduction of agentic AI like Claude Code and Codex takes giant steps that our current evaluation frameworks struggle to keep up with." The outline explicitly states that "specific tool names (Claude, NotebookLM, ChatGPT) are illustrative and will date" and that the argument must be "tool-agnostic throughout." Naming Claude Code and Codex in the abstract is the most prominent possible violation of this.

The abstract also contains several register problems for a Sociological Science submission: "There are plenty of *checklists*" is informal; "something aka a reproducibility package" is too casual; the phrase "which can even be pre-registred" contains a misspelling and is syntactically incomplete.

*Fix*: Revert to the v1 abstract and apply targeted edits. The v1 abstract was 138 words, within limit, and correctly tool-agnostic. If the tool-agnostic principle is to be softened, that is an argument-level decision that should be made explicitly, not introduced silently in an edit.

**C3 — §4.4 narrative describes abandoning the structured workflow**

The manually added paragraph at the end of §4.4 reads: "In practice, after the first draft by AI, I ran the reviewer-skill to support my own assessment. However, there were so much to work on, and it I decided to discard the review and do an unaided manual assessment first." This contains a grammatical error ("it I decided") and, more consequentially, describes discarding the structured review output and proceeding without it — in the section where the paper argues for the epistemic value of structured review. A reader sceptical of the workflow will note the contradiction. The narrative of the iterative process that follows ("some adjustments are AI-assisted, some are not") is honest but belongs in a reflexive note or the documentation section, not in the section arguing for the epistemic value of adversarial configuration.

*Fix*: Move the process narrative to §4.5 (Documentation) or a brief reflexive footnote. §4.4 should remain focused on what the adversarial configuration achieves and why, not on the author's decision to bypass it in the first round.

---

### Significant — should be addressed

**S1 — "I firmly believe" as an evidential warrant (§5.3)**

§5.3 now contains: "However, I firmly believe that externalizing ideas and making them explicit and precise sharpens the mind, and that should — all else equal — lead to better quality analysis." This is a belief claim, not an argument. It is presented as if it provides warrant for a quality claim that the paper has just correctly hedged as an open empirical question. "Firmly believe" is particularly problematic because it substitutes conviction for evidence — the opposite of the hedging hierarchy the paper elsewhere observes. The sentence should either be cut (the paragraph already ends correctly with "an open empirical question") or replaced with an actual argument, such as a connection to the existing literature on externalisation and cognitive quality (there is relevant literature in cognitive psychology on writing and thinking that could be cited briefly).

**S2 — "AI-architecture" introduced and abandoned (§3.2)**

§3.2 introduces: "We might refer to this kind of structure as the *AI-architecture* of a given project." The term is not defined, not previously used, and does not appear again in the paper. Introducing a term that is neither defined nor developed creates an expectation the paper does not fulfil. Either develop the concept — it could be useful for describing the CLAUDE.md / project-level context / prompt-level hierarchy — or remove it.

**S3 — §4.2 database licensing discussion is loosely integrated**

The manual edit expands §4.2 with three paragraphs on database licensing. These paragraphs are informally written, introduce material at a different level of abstraction than the rest of the section, and do not integrate cleanly with the OpenAlex rationale that follows. The original §4.2 handled this in one sentence. The new version says: "There are legal obstacles to this approach... If you are licensed to such use, that one should do so" — this is inconsistently registered ("that one should do so" is awkward) and adds a recommendation without explaining what "that" refers to. The paragraph structure is:
1. Standard approach uses Scopus/WoS (reasonable point)
2. Legal obstacles exist (reasonable point)
3. "If you are licensed, you should" (what does this mean?)
4. There is specialized software (incomplete reference)
5. One can do more than one kind of search (true but vague)

*Fix*: Consolidate to two sentences: name the licensing issue and explain the OpenAlex choice as the solution adopted here. The level of detail on ASReview and general AI tools can be cut — it's a different paper.

**S4 — "In my opinion" weakens a defensible scholarly claim (§5.1)**

§5.1 now reads: "In my opinion, and in particular for the social sciences, the more appropriate description is externalisation." The characterisation of pre-registration as externalisation is a defensible, arguable position — not merely an opinion. Flagging it as personal opinion invites readers to dismiss it as subjective. The paper should argue for this characterisation, not merely hold it. Remove "In my opinion" and replace with the argument: "The more accurate description is externalisation: pre-registration does not improve research by constraining deviation but by forcing articulation of decisions before outcomes are known."

**S5 — §3.2 CLAUDE.md reference is tool-specific**

§3.2 now includes: "For example, in Claude, the project-level CLAUDE.md file would serve this purpose, but the root-folder CLAUDE.md file can also include relevant context information." This is directly tool-specific — naming a Claude-specific configuration file as an exemplar in the conceptual section. The outline's tool-agnostic requirement applies here. The general point (that context should be specified at multiple levels: root, project, prompt) is sound and worth making, but it should be made in tool-agnostic language.

*Suggested reformulation*: "In practice, explicit context operates at multiple levels: a persistent project-level configuration encoding the research question and scope, and individual prompt-level specifications for each task. AI tools implement this in different ways, but the principle is consistent across platforms."

**S6 — §6.1 ends with "I think not" (register)**

The paragraph in §6.1 assessing current policy closes: "The question I address here is not whether they are sensible but whether they are sufficient — and whether the binary structure they share is the right instrument for the problem. I think not." "I think not" as a standalone sentence is too casual, too curt, and inconsistent with the concessive register the section has been maintaining. It also breaks the sequencing: the paper should not conclude the concessive move with a dismissal. The paragraph should either end with the question and let §6.2 provide the answer, or close with a more measured formulation.

*Suggested reformulation*: "I address both questions in turn" — and let §6.2 provide the negative answer with its full argument.

---

### Addressable in revision

**A1 — §3.1 colloquial register**
"characterized by how most of us will use AI on an everyday basis: prompt and refine until satisfactory answer" — "satisfactory answer" should be "a satisfactory answer"; "most of us" shifts to a different first-person register than the rest of the paper. Revise to "characterised by prompting without explicit criteria and refining until an acceptable output is produced" or similar.

**A2 — §2.1 "As far as I am aware of" (unidiomatic)**
"As far as I am aware of, sociology-specific guidance... is absent." The correct idiom is "As far as I am aware" (without "of"). Replace with "To my knowledge" (already used correctly earlier in the same paragraph: "To my knowledge, Blanchard et al. offer...").

**A3 — §5.1 "In principle you can work along such lines without timestamp as well"**
This is syntactically loose. If the point about non-public commitment is already made in §3.2, it may not be needed here. If retained: "In principle, structured AI use without a public timestamp still achieves the externalisation benefit, even if it cannot be independently verified as pre-commitment."

**A4 — §5.3 "I cannot claim to have demonstrated"**
Still present from previous review. Revise to active: "I have not demonstrated this for sociology specifically."

**A5 — §6.1 "Papermills and questionable research practices was a concern"**
Subject-verb disagreement. "Papermills and questionable research practices *were* a concern also before AI."

**A6 — §4.3 "which I am particularly satisfied with"**
This personal evaluation appears in the middle of a description of a scholarly method. It is not wrong but it is informal and breaks the argumentative register. Consider cutting or replacing with a structural claim: "a style profile that encodes explicit criteria for..."

**A7 — §5.4 "I make no claim to solve all AI-related challenges for social sciences"**
Over-hedging. The section title ("What structured use cannot guarantee") already frames the scope. The disclaimer adds nothing.

**A8 — §4.5 "The registered plan and the final methods section are both legitimate"**
The manual edit removed the explicit pre-registration reference from this sentence: the original read "This mirrors how pre-registration works: the registered plan and the final methods section are both legitimate." The revision drops "This mirrors how pre-registration works:" — weakening the running analogy that connects §4 to §5. Restore the framing sentence.

**A9 — §7 new paragraph wording**
"something aka a reproducibility package" — "something aka" is too informal. Replace with: "a replication package, available at GitHub [URL]." The sentence "I have avoided putting emphasis on the specific tools I have been using, as the AI landscape is changing so fast" is defensively framed. Replace with the positive claim: "The structured/unstructured distinction is tool-agnostic; the workflow documented here is designed to be adapted to whatever AI infrastructure the researcher works with."

---

## Skardhamar style: net assessment of manual edits

The manual edits introduce a cluster of register inconsistencies that diverge from the established style:

**Problematic hedging patterns introduced:**
- "In my opinion" (§5.1) — undercuts the argumentative register
- "I firmly believe" (§5.3) — substitutes conviction for argument
- "As far as I am aware of" (§2.1) — unidiomatic
- "I make no claim to solve all AI-related challenges" (§5.4) — over-hedging

**Colloquial register introduced:**
- "plenty of checklists" (abstract)
- "prompt and refine until satisfactory answer" (§3.1)
- "something aka a reproducibility package" (abstract/§7)
- "the AI landscape is changing so fast" (§7)
- "I think not" (§6.1)

**Positive additions from manual edits:**
- The explicit tool-agnostic signal in §7 is in the right spirit (execution needs polish)
- The broadening of §4 framing (sociological article as distinct from systematic review) is appropriate
- The "To my knowledge" hedges on gap claims in §2.1 and §2.2 are more measured than the original
- The honest description of iterative process in §4.4 is epistemically appropriate, even if misplaced structurally

---

## Summary of all open issues

### Critical

| # | Issue | Location |
|---|---|---|
| C1 | "Three" features, four listed | §3.2 |
| C2 | Abstract: over-length, tool-specific, informal register | Abstract |
| C3 | §4.4 narrative describes discarding the structured workflow | §4.4 |
| [prev 1.1] | "Current policies treat AI use as a binary" — universal | §6.2 |
| [prev 1.2] | §4 → §5 inferential bridge missing | Between §4.5 and §5.1 |
| [prev 3.1] | Registered reports analogy inaccurate | §3.2 |
| [prev 6.1] | Reflexivity note duplicated; §2.2 version defensive | §1 and §2.2 |

### Significant

| # | Issue | Location |
|---|---|---|
| S1 | "I firmly believe" as warrant | §5.3 |
| S2 | "AI-architecture" introduced and abandoned | §3.2 |
| S3 | Database licensing discussion loosely integrated | §4.2 |
| S4 | "In my opinion" weakens a defensible claim | §5.1 |
| S5 | CLAUDE.md reference is tool-specific | §3.2 |
| S6 | "I think not" — wrong register | §6.1 |
| [prev 1.3] | Demonstration scope: one instance, not acknowledged | §4.1 |
| [prev 2.1] | "Documentation-based framework" not constituted | §6.3 |
| [prev 4.1] | Peer reviewer competence not acknowledged | §6.3 |
| [prev 4.2] | Five moves (§1) vs. three arguments (§7) | §1 and §7 |

### Addressable

| # | Issue | Location |
|---|---|---|
| A1 | §3.1 colloquial register | §3.1 |
| A2 | "As far as I am aware of" — unidiomatic | §2.1 |
| A3 | Loose syntax in pre-registration analogy note | §5.1 |
| A4 | "I cannot claim to have demonstrated" → active | §5.3 |
| A5 | Subject-verb: "Papermills... was" | §6.1 |
| A6 | "which I am particularly satisfied with" | §4.3 |
| A7 | "I make no claim to solve..." — over-hedging | §5.4 |
| A8 | Pre-registration framing sentence removed from §4.5 | §4.5 |
| A9 | §7 new paragraph wording and tool-agnostic framing | §7 |
| [prev 5.1] | "Has no good answer" → "the wrong question" | §7 |
| [prev 5.2] | "Whether but how" appears twice | §1 and §2.1 |
| [prev 5.3] | "Errors visible and correctable" near-slogan | §3.3, §5.4, §7 |

---

## 10. Overall Assessment

**Score: 3 / 5 — major revisions required**

The manually edited version is roughly equivalent to the v1 original in overall quality, with the balance tipping slightly lower due to new errors introduced. Several edits represent genuine improvements: the gap claims in §2.2 are more carefully hedged; the framing of the literature review section is somewhat broader; the conclusion adds a useful replication package pointer. These are real gains.

Against these, the manual edit introduced three new critical-severity problems (abstract length/register/tool-naming; the "three vs. four" counting error; the structural problem in §4.4), five new significant problems, and a cluster of register inconsistencies that work against the Skardhamar style. None of the critical issues from the previous review were addressed.

**Recommendation: Revise — work through the critical issues in order before proceeding to the significant and addressable items.**

Priority sequence for the next revision pass:
1. Revert the abstract to v1 and apply targeted edits (tool-agnostic, within 150 words)
2. Fix the registered reports analogy in §3.2
3. Add the §4 → §5 connective sentence
4. Resolve "three vs. four" in §3.2
5. Relocate or remove the §4.4 process narrative
6. Remove reflexivity note from §1; de-hedge the §2.2 version
7. Address significant issues in one further pass

---

*Review complete — 2026-04-11*
