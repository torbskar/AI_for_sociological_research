# Logic & Language Review — v2-draft.md

**Skill applied:** logic-language-reviewer + skardhamar-style  
**Date:** 2026-04-16  
**Draft reviewed:** `draft/v2-draft.md`  
**Previous review:** `draft/v1-manualEdit-review-logic-language.md`

---

## Step 0: Paper type

**Discipline-reflective / programmatic** — unchanged. Standard for this paper.

---

## Status of issues from the previous review

| Previous issue                                                    | Status in v2                                                                                                                                                                                    |
| ----------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| C1 — "Three" features, four listed (§3.2)                         | **FIXED** — now reads "four defining features"                                                                                                                                                  |
| C2 — Abstract over-length, tool-specific, informal                | **FIXED** — v1 abstract restored; clean, tool-agnostic, within 150 words                                                                                                                        |
| C3 — §4.4 narrative describes discarding structured workflow      | **FIXED** — process narrative removed; §4.4 (now §4.5) reads cleanly                                                                                                                            |
| [prev 1.1] — §6.2 binary claim stated as universal                | **NOT FIXED** — "dominant policy structure treats AI use as a binary" is the same phrasing; "dominant" adds some hedge but the claim is still not evidenced                                     |
| [prev 1.2] — §4 → §5 inferential bridge missing                   | **NOT FIXED** — §4.6 ends on the replication package; §5.1 opens on pre-registration with no connective sentence                                                                                |
| [prev 1.3] — Demonstration scope not acknowledged as illustrative | **PARTIALLY FIXED** — §4.3 now acknowledges "anticipatory guidance rather than demonstrated practice" for the empirical section; §4.1 overview still presents the workflow without a scope note |
| [prev 3.1] — Registered reports analogy inaccurate                | **FIXED** — §3.2 now reads "analogous to pre-registration" throughout; "registered reports" removed                                                                                             |
| [prev 6.1] — Reflexivity note duplicated; §2.2 version defensive  | **FIXED** — neither instance appears in v2                                                                                                                                                      |
| S1 — "I firmly believe" as warrant (§5.3)                         | **FIXED** — removed                                                                                                                                                                             |
| S2 — "AI-architecture" introduced and abandoned (§3.2)            | **FIXED** — removed                                                                                                                                                                             |
| S3 — Database licensing loosely integrated (§4.2)                 | **FIXED** — consolidated to one sentence                                                                                                                                                        |
| S4 — "In my opinion" weakens a defensible claim (§5.1)            | **FIXED** — removed                                                                                                                                                                             |
| S5 — CLAUDE.md tool-specific reference (§3.2)                     | **FIXED** — replaced with tool-agnostic formulation                                                                                                                                             |
| S6 — "I think not" register (§6.1)                                | **FIXED** — replaced with "I address both questions in turn"                                                                                                                                    |
| [prev 2.1] — "Documentation-based framework" not constituted      | **FIXED** — §6.3 now specifies what peer reviewers should assess                                                                                                                                |
| [prev 4.1] — Peer reviewer competence not acknowledged (§6.3)     | **NOT FIXED** — §6.3 states "reviewers can assess" without acknowledging that this requires competence most reviewers currently lack                                                            |
| [prev 4.2] — Five moves (§1) vs. three arguments (§7)             | **NOT FIXED** — §1 lists five moves; §7 opens "I have argued for three things"                                                                                                                  |
| [prev 5.1] — "Has no good answer" (§7)                            | **FIXED** — not present in v2                                                                                                                                                                   |
| [prev 5.2] — "Whether but how" appears twice                      | **FIXED** — appears once (§1); §2.1 now reads "whether AI has entered research practice"                                                                                                        |
| [prev 5.3] — "Errors visible and correctable" near-slogan         | **PARTIALLY FIXED** — reduced from three instances to two; §3.3 uses "visible and correctable"; §5.4 uses "visible and therefore addressable" (differentiated); not in §7                       |
| A1–A9 addressable issues                                          | **ALL FIXED**                                                                                                                                                                                   |

**Summary:** 14 of 18 tracked issues fully resolved; 2 partially resolved; 4 not fixed (prev 1.1, 1.2, 4.1, 4.2). All critical issues from the v1-manualEdit review that were attributed to the manual edit are fixed. The four unresolved issues are all carry-forwards from before the manual edit.

---

## New issues — Critical

### NC1 — §1 scope paragraph: multiple grammar and logic failures

The scope paragraph in §1 was rewritten and introduces several interacting problems:

> "The workflow described here is focused on text-heavy and empirical social science research, but the focus is on the systematic uses and documentation, not the specifics of empirical analysis as such. However, primary data collection and the handling of personal data require additional safeguards is discussed. Similarly, while I include a section on literature review, this is not a guide to AI for systematic reviews, which have their own established protocols, where AI can be efficient additions, especially if it can be documented it is done in a structured way. The argument developed here is directed at sociology and adjacent social sciences where research questions, theoretical framings, but extends to any discipline where interpretive moves cannot be delegated to automated agents."

**Grammar error**: "require additional safeguards is discussed" — auxiliary verb clash; the main verb ("require") and the passive construction ("is discussed") compete. Either "require additional safeguards, discussed in the supplementary materials" or "are discussed in the supplementary materials."

**Dangling construction**: "where research questions, theoretical framings, but extends to any discipline" — the list beginning "where research questions, theoretical framings," is never completed; the sentence pivots to "but extends" before the listed items receive a predicate.

**Circular phrasing**: "especially if it can be documented it is done in a structured way" — this restates the paper's thesis as an observation about systematic reviews, which is circular and underdeveloped. The point either needs a sentence of support or should be cut.

**Self-referential register**: "while I include a section on literature review" — breaks the methodological register; the paper should refer to what the workflow covers, not to what the author chose to include.

**Scope expansion without argument**: "but extends to any discipline where interpretive moves cannot be delegated to automated agents" — this significantly broadens the scope claim beyond "sociology and adjacent social sciences" without acknowledging the change or providing grounds for it. The original scope sentence was deliberately scoped; the expansion is consequential and needs justification or a hedge.

*Fix*: Rewrite this paragraph. A clean version would: (1) state the primary scope (text-heavy and literature-based sociology research), (2) note that empirical data and personal data handling receive separate treatment in §4.3 with distinct constraints, (3) note that systematic review is excluded as a separate domain with established protocols, (4) close with the disciplinary scope claim (sociology and adjacent social sciences), hedged if broader applicability is to be asserted. The original v1 scope paragraph achieved this in four sentences; the rewrite should return to that precision.

---

## New issues — Significant

### NS1 — §2.2 ICMJE gap claim lacks hedging

The new paragraph at the end of §2.2 includes: "No existing work has applied these criteria to AI-assisted research in a way that asks whether the human researcher meets them."

This is a gap claim of the same type as those in §2.2: "No existing framework explicitly theorises the systematic/unsystematic distinction... No existing work treats AI tool configuration... No existing work discusses the transparency artefacts..." All those claims use the same flat construction, and in this register the review accepts them as-is. However, they stand at the end of a paragraph prefaced by careful hedging in §2.1 ("To my knowledge"), and the convention in the paper is that gap claims carry implicit hedging. The ICMJE gap claim is more specific and harder to verify than the others — it is a claim about a relatively constrained body of work (authorship criteria in AI-assisted research). For consistency with §2.1's hedging practice and as a risk-reduction measure: prefix with "To my knowledge."

### NS2 — §1 ICMJE pointer directs to §5, not §5.5

The ICMJE forward reference at the end of the five-moves paragraph reads: "a connection I develop in §5."

The connection is developed specifically in §5.5; §§5.1–5.4 do not develop it. A reader following this pointer may read through §5 expecting to find the authorship criteria applied, and only encounter it at §5.5. More precisely: "a connection I develop in §5.5" — or, if a section pointer is not stylistically preferred, "a connection I develop toward the end of §5."

### NS3 — §5.5 para 5: meta-announcement breaks argumentative register

"I want to make a pointed but careful claim here."

This sentence announces what is about to be said rather than saying it. The paper's argumentative register elsewhere makes the claim directly and applies the hedging within the claim. "I want to make a pointed but careful claim" is both redundant (the hedging in the following sentence does the work) and inconsistent with the register established elsewhere. The sentence should be removed; the paragraph can open directly with "The standard model of research accountability presupposes that the researcher knows what they did..."

### NS4 — §5.5 para 2: "the query authorship argument is a direct claim" — awkward construction

"On criterion 1, the query authorship argument is a direct claim: designing a search strategy..."

"Is a direct claim" does not grammatically resolve: a claim *about* what? The intended meaning is that the query authorship concept maps directly onto criterion 1. *Fix*: "On criterion 1, query authorship maps directly: designing a search strategy, specifying inclusion and exclusion criteria, formulating synthesis questions, and configuring a reviewer skill are acts of conception and design in the relevant sense."

### NS5 — §4.6 sentence fragment disrupts the lab-notebook analogy

"It documents what the _author_ has added or instructed, documented the _query-authorship_."

This sentence has two problems. First, "It" (singular) follows "These are" (plural, referring to working logs) — the pronoun number shifts. Second, "documented the _query-authorship_" is a participial fragment that does not attach to anything. The sentence appears to be a draft note that was not completed. As written, it also states the wrong emphasis — the point of the analogy is the contemporaneous character of the logs, not their authorship documentation function (which is made in §4.6's next paragraph about author-input files).

*Fix*: Remove the fragment. The preceding sentence ("These are analogous to a lab notebook: their evidential weight lies in their contemporaneous character and in their recording of iterative process rather than end-state outcomes") is a complete and accurate statement; the next sentence can open directly with "The second tier consists of..."

---

## New issues — Addressable in revision

### NA1 — §2.1 opening sentence: subject-verb disagreement and syntactic breakage

"Large language models has been adopted to a large extent across academic disciplines and  transforming the scientific practices (Grossmann et al. 2023)."

Three errors: "models has" (plural subject, singular verb); "and  transforming" (double space; "and" should connect to a parallel verb: "and are transforming" or, more cleanly, the gerund can be dropped); "the scientific practices" (either "scientific practice" or "research practices"). *Fix*: "Large language models have been widely adopted across academic disciplines, transforming research practice (Grossmann et al., 2023)."

### NA2 — §2.1 "or should be developed to" — dangling preposition

"The question of whether AI has entered research practice is settled, but less attention is paid to what kind of practice has developed, or should be developed to."

"Developed to" hangs. *Fix*: "...but less attention is paid to what kind of practice has emerged, or should." Or: "...what kind of practice is developing, and what kind should be."

### NA3 — §5.4 "without an explicit criteria" — number error

"The AI operating without an explicit criteria may perform equally well on average..."

"Criteria" is plural; "an explicit criteria" is ungrammatical. *Fix*: "The AI operating without explicit criteria" (drop "an").

### NA4 — §5.4 paragraph 1: incomplete and vague constructions

"Open Science practices will, however, restrict such possibilities, and make it easier to detect, and systematic use of AI will support that."

"Make it easier to detect" has no object — detect what? Documentation faking? Individual violations? "Systematic use of AI will support that" is similarly underspecified. Both incomplete constructions appear in the paper's least argued paragraph. *Fix*: Either complete both constructions with their objects (detect misconduct; support detection and correction) or rewrite for directness: "Open science practices and systematic AI use increase the likelihood that faked documentation is detected, since the artefacts produced are evaluable rather than merely asserted."

### NA5 — §5.4 non-parallel construction in opening claim

"What structured use cannot guarantee is high quality or eliminating errors."

"High quality" is a noun phrase; "eliminating errors" is a gerund phrase. They are not parallel. *Fix*: "What structured use cannot guarantee is high quality or error-free outputs" — or simply: "Structured use does not guarantee high quality or eliminate errors."

### NA6 — §4.6 "A major point in structured use of AI is documentation" — weak opening

This sentence is vague and low-register as a section opener. *Fix*: "Documentation is the central output of the structured workflow — it is what distinguishes systematic from unsystematic AI authorship at the point of submission" or, more economically, begin with the two-tier structure directly.

---

## Reference accuracy issues (require author verification, not logic-language fixes)

These are not logic or language issues but discrepancies identified in review that affect the accuracy of citations:

**Mondal et al.**: Cited in §2.1 and §2.2 as "(2024)" and as "audited 20 major publishers." The reference entry confirms the paper was published in 2025 and studied 162 STM publishers. The in-text citation may refer to a different paper (a 2024 source with 20 publishers), or the details are incorrect. Author must verify whether the in-text claim and citation details are consistent. If the confirmed Mondal et al. (2025) paper is the intended citation, both the year and the count in the text must be updated.

**Feuerriegel et al.**: Cited in §2.1 as "(2023)." The reference entry states publication in *BISE* 2024, with preprint 2023. Author to decide which year to use and update in-text citation to match.

**Three titles unconfirmed**: Cheng et al. (2026), Davidson & Karell (2025), and Holst et al. (2025) reference entries carry "[Title to be confirmed]." These should be resolved before submission.

---

## Skardhamar style: net assessment of v2 changes

**Improvements carried from v1 manual edits — now clean:**

- Register is substantially improved throughout; the informal insertions from v1-manualEdit are gone
- Hedging hierarchy is correctly observed in §§3–6
- "Whether but how" corrected to one instance
- §3.1, §5.1, §5.3, §5.4 read cleanly in the correct argumentative register

**New additions (§§2.2, 5.5) — mostly strong:**

- §2.2 ICMJE paragraph is cleanly argued and well-placed; sets up §5.5 correctly
- §5.5 is substantially well-argued; the careful claim in para 5 is appropriately hedged and the "structural vs. presumptive accountability" distinction is the paper's strongest new move
- The bridge paragraph (§5.5 para 6) earns its place: "Binary prohibition addresses the easy question (AI cannot be an author) while leaving the harder one unasked. Blanket disclosure answers neither" — this is the sharpest formulation in the section, and one of the paper's best sentences. The referent of "neither" (neither the easy question about AI authorship nor the question of human researcher accountability) is clear from context, though a revision could make it explicit: "neither question."

**Remaining register concerns:**

- NC1 (§1 scope paragraph) introduces the most significant register problems in the draft — the self-referential "while I include a section" and the dangling construction create a poor impression at a high-visibility location
- NS3 ("I want to make a pointed but careful claim here") is the only hedging anomaly in the new material
- The §4.6 fragment (NS5) is an editing artefact that reads as unfinished

---

## Summary of all open issues

### Critical

| #          | Issue                                                                                       | Location              |
| ---------- | ------------------------------------------------------------------------------------------- | --------------------- |
| NC1        | §1 scope paragraph: grammar errors, dangling construction, scope expansion without argument | §1 para 3             |
| [prev 1.2] | §4 → §5 inferential bridge missing                                                          | Between §4.6 and §5.1 |

### Significant

| #          | Issue                                                                           | Location    |
| ---------- | ------------------------------------------------------------------------------- | ----------- |
| NS1        | §2.2 ICMJE gap claim lacks "To my knowledge"                                    | §2.2        |
| NS2        | ICMJE forward reference directs to §5, not §5.5                                 | §1          |
| NS3        | "I want to make a pointed but careful claim here" — meta-announcement           | §5.5 para 5 |
| NS4        | "The query authorship argument is a direct claim" — grammatically awkward       | §5.5 para 2 |
| NS5        | §4.6 sentence fragment: "documented the _query-authorship_"                     | §4.6        |
| [prev 1.1] | §6.2 binary claim may be overstated; "dominant" hedges but evidence thin        | §6.2        |
| [prev 4.1] | Peer reviewer competence to evaluate AI workflow documentation not acknowledged | §6.3        |
| [prev 4.2] | Five moves (§1) vs. three arguments (§7): structural mismatch                   | §1 and §7   |

### Addressable

| #          | Issue                                                                                | Location      |
| ---------- | ------------------------------------------------------------------------------------ | ------------- |
| NA1        | §2.1 opening sentence: "models has", "and  transforming", "the scientific practices" | §2.1          |
| NA2        | "or should be developed to" — dangling preposition                                   | §2.1          |
| NA3        | "without an explicit criteria" — number error                                        | §5.4          |
| NA4        | "make it easier to detect" and "will support that" — incomplete constructions        | §5.4          |
| NA5        | Non-parallel "high quality or eliminating errors"                                    | §5.4          |
| NA6        | "A major point in structured use of AI is documentation" — weak opener               | §4.6          |
| [prev 1.3] | Scope not acknowledged as illustrative in §4.1 overview                              | §4.1          |
| [prev 5.3] | "Errors visible and correctable" at two proximity instances                          | §3.3 and §5.4 |

### Reference accuracy (author verification required)

| Issue                                                                                | Location   |
| ------------------------------------------------------------------------------------ | ---------- |
| Mondal et al.: year 2024 vs. confirmed 2025; "20 major publishers" vs. confirmed 162 | §2.1, §2.2 |
| Feuerriegel et al.: in-text 2023 vs. published 2024                                  | §2.1       |
| Cheng, Davidson & Karell, Holst: titles unconfirmed in reference list                | References |

---

## Overall assessment

**Score: 3.5 / 5 — moderate revisions required**

v2 represents a substantial improvement over v1-manualEdit. Almost all issues identified in the previous review have been resolved — including all three prior critical issues and all nine addressable issues. The new material (§4.3 empirical data, §5.5 authorship criteria) is generally well-argued and well-integrated, with §5.5 producing several of the draft's strongest formulations.

The score is held back by one new critical issue (the §1 scope paragraph), four persistent unresolved issues — two of which (§4→§5 bridge, five vs. three argument count) affect the paper's structural coherence — and a cluster of minor new issues that need clearing up before submission.

**Recommendation: Targeted revision. The §1 scope paragraph requires a full rewrite — this is the most visible failure and the one that most urgently needs attention. The §4→§5 bridge and the five-vs-three structural mismatch have been unresolved across all three review cycles and should be addressed in the same revision pass. The significant and addressable issues can be handled in one pass thereafter.**

Priority sequence:

1. Rewrite §1 scope paragraph (NC1)
2. Add §4 → §5 connective sentence (prev 1.2)
3. Reconcile five moves (§1) with three arguments (§7) — either consolidate §1 to three or expand §7 (prev 4.2)
4. Resolve NS3 (remove meta-announcement) and NS5 (remove fragment) — quick edits
5. Update §1 ICMJE pointer to "§5.5" (NS2)
6. Add "To my knowledge" to §2.2 ICMJE gap claim (NS1)
7. Fix addressable issues in one pass
8. Author: verify Mondal and Feuerriegel citations; confirm three unresolved titles

---

*Review complete — 2026-04-16*
