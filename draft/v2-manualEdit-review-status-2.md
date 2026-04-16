# Review status check (2nd pass) — v2-draft - manualEdit.md

**Date:** 2026-04-16  
**File reviewed:** `draft/v2-draft - manualEdit.md`  
**Previous status check:** `draft/v2-manualEdit-review-status.md`

---

## Items from previous status check: now fixed

- **NS1** (§2.2 gap claim hedging) — "To my knowledge, no existing work has applied..." ✓
- **NS3** (meta-announcement in §5.5 para 5) — paragraph now opens directly ✓
- **NS4** ("is a direct claim") — "query authorship maps directly" ✓
- **NS5** (§4.6 fragment) — removed; paragraph flows cleanly ✓
- **prev 1.1** (§6.2 binary claim overstated) — "Probably the most common policy structure" is a clear and sufficient hedge ✓
- **NA2** ("or should be developed to") — "what kind should be" ✓
- **NA4** (§5.4 incomplete constructions) — rewritten cleanly ✓
- **NA5** (non-parallel construction in §5.4) — "does not guarantee high quality or eliminate errors" ✓
- **NA6** (weak §4.6 opener) — "The documentation produced across all stages of the workflow..." ✓
- **§5.5 para 6** ("answers neither") — "Blanket disclosure answers neither question" ✓
- **New-1** (§2.2 broken sentence with dangling "which") — §2.2 now reads cleanly; the mid-sentence insertion is not present ✓
- **New-2 (partial)** — main grammar errors fixed: "systematic use" (not "uses"), "systematic reviews are a separate domain" (verb agreement), no misspelling; self-referential phrasing improved ✓
- **New-3** (stray period in Feuerriegel title) — gone ✓
- **References** — Goyanes, Cheng, Davidson & Karell entries now complete ✓; Feuerriegel year corrected to 2024 ✓; Mondal replaced with a different paper that matches in-text claim (2024, journal publishers) ✓; Zrubka preprint details added ✓; Barrie URL added ✓

---

## Items from previous status check: still open

**NS2 — ICMJE pointer: "towards the end of §5"**  
§1 now reads "a connection I develop towards the end of §5" — improved from the plain "§5," and the phrase "towards the end" is an accurate and sufficient pointer. This is adequate; specifying "§5.5" would be more precise but is optional.  
*Status: functionally resolved; precision improvement optional.*

**prev 1.2 — §4 → §5 inferential bridge**  
Three new sentences have been added at the opening of §5.1: "A well crafted AI workflow starts with a structured query and setup that guides the project thereafter. On the one hand, this could be pre-registered along with other parts of the protocol as suggested by open sciences guidelines. But there is also a structural similarity to pre-registration at a deeper level." These sentences introduce §5.1's pre-registration discussion but do not bridge from §4's workflow description — the §4.6 ending ("systematic AI authorship produces replication-ready materials as a natural byproduct of the workflow") is not picked up by this opening. The transition is somewhat better than before but the logical connection between the workflow section and the epistemic section remains implicit.  
*Status: partially addressed; the fundamental bridge remains missing.*

**prev 4.2 — Five moves (§1) vs. three arguments (§7)**  
Unchanged: §1 lists five moves; §7 opens "I have argued for three things."  
*Status: not fixed.*

**prev 4.1 — Peer reviewer competence (§6.3)**  
§6.3 still asserts "Reviewers can assess whether a structured process was appropriate" without acknowledging the competence requirement.  
*Status: not fixed.*

**NA3 — "without an explicit criteria"**  
§5.4 still: "The AI operating without an explicit criteria may perform equally well on average." Fix: "without explicit criteria" (drop "an").  
*Status: not fixed.*

**NA1 partial — "transforming the scientific practices"**  
§2.1: "Large language models have been widely adopted across academic disciplines, and transforming the scientific practices (Grossmann et al. 2023)." The "have" is now correct. The residual issues: "and transforming" is non-parallel to "have been widely adopted" (should be either "and are transforming" or, cleaner, drop "and" and write "have been widely adopted across academic disciplines, transforming scientific practice"); "the scientific practices" should be "scientific practice" (uncountable noun).  
*Status: partially fixed; two minor residual issues remain.*

**New-4 — Zrubka year discrepancy**  
Text still: "Zrubka et al. (2025) systematically reviewed 24 such instruments." Reference entry now dated 2023 (Research Square preprint, October 2023). The year in the text must be updated to "(2023)" to match the reference, or a published 2025 version must be located.  
*Status: not fixed — discrepancy persists.*

---

## New issues introduced in this edit

### Critical

**NC-new-1 — §2.2 gap paragraph: missing "that" creates ungrammatical sentence**  
The paragraph now opens: "Thus, there is no widely established framework explicitly theorises the systematic/unsystematic distinction as the fundamental policy-relevant axis."  
"Framework explicitly theorises" is ungrammatical: the relative clause requires "that": "Thus, there is no widely established framework **that** explicitly theorises..." This is the first sentence of the gap paragraph — a structurally prominent location.  
*Fix*: Insert "that" after "framework." While here: "Thus, there is no widely established framework that explicitly theorises" reads naturally, but "Thus" as a sentence opener can be cut; "No existing framework explicitly theorises" (the original phrasing) was cleaner.

### Significant

**NS-new-1 — §5.1 new opening sentences: register and logic issues**  
The three new sentences added at the top of §5.1 introduce several problems:  
- "A well crafted AI workflow" — "well crafted" should be hyphenated ("well-crafted") as a compound modifier before a noun  
- "as suggested by open sciences guidelines" — "open sciences" should be "open science" (no 's')  
- "On the one hand, this could be pre-registered... But there is also a structural similarity to pre-registration at a deeper level" — the "on the one hand / but there is also" construction implies a contrast that doesn't materialise: the two things (formal pre-registration and structural similarity to pre-registration) are not in tension; they are additive. The framing creates a false expectation of opposition.  
- "at a deeper level" — vague; the rest of §5.1 explains what this deeper level is, so the phrase is unnecessary  

The more fundamental issue: these sentences introduce §5.1's content but do not bridge from §4. The §4.6 ending is about the replication package; §5 is about epistemic properties. A connecting sentence should name this shift (e.g., "Having described what systematic AI authorship produces, I now examine why those outputs matter epistemically").

**NS-new-2 — §7 "through analysis of data" breaks the em-dash list**  
§7: "...the intellectual commitments encoded in the query — the literature search criteria, the screening standards, the configuration design, the verification structure, through analysis of data —"  
The list contains four noun phrases followed by a prepositional phrase ("through analysis of data"), which is a different grammatical type and doesn't fit the enumeration. The intent is to broaden the query authorship claim to include empirical analysis — a defensible expansion — but the execution is syntactically incorrect and the phrase "through analysis of data" is too vague to carry that weight.  
*Fix*: Either add "and empirical analysis decisions" as a fifth noun phrase in the list, or handle the expansion in a separate sentence after the em-dash clause.

### Addressable

**NA-new-1 — §1 scope paragraph: two residual issues**  
After the previous fixes, two problems remain:  
- "while a section on literature search and review is included below, the main focus is on the system and protocols, **while** e.g. systematic reviews are a separate domain not discussed further here" — two "while" clauses in succession; "e.g." is informal for this register (use "such as" or restructure)  
- "The handling of data and personal data is treated with distinct constraints" — "data and personal data" is redundant (personal data is a subset); "is treated with distinct constraints" is vague. *Fix*: "Data collection and the handling of personal data are subject to additional constraints described in §4.3."

**NA-new-2 — Holst reference: inconsistent formatting**  
Current entry:  
> Holst D, Moenck K, Koch J, Schmedemann O, Schüppstuhl T  
> Transparent Reporting of AI in Systematic Literature Reviews: Development of the PRISMA-trAIce Checklist JMIR AI 2025;4:e80247 https://ai.jmir.org/2025/1/e80247  

Problems: no periods after initials; journal-year-volume-article format instead of comma-separated; split across two lines; URL without doi: prefix. *Fix* to match the APA-style used throughout:  
> Holst, D., Moenck, K., Koch, J., Schmedemann, O., & Schüppstuhl, T. (2025). Transparent reporting of AI in systematic literature reviews: Development of the PRISMA-trAIce checklist. *JMIR AI*, *4*, e80247. https://ai.jmir.org/2025/1/e80247

**NA-new-3 — Mondal reference: affiliation numbers in author names and inconsistent style**  
Current entry:  
> Mondal, Himel; Mondal, Shaikat**1**; Behera, Joshil Kumar**2**. Artificial intelligence in academic writing...  

Superscript affiliation numbers (1, 2) are artefacts from a database export and should be removed. Semicolons between authors should be commas; "p 56-57" should be "56–57" (en dash). Format to match APA style used throughout:  
> Mondal, H., Mondal, S., & Behera, J. K. (2024). Artificial intelligence in academic writing: Insights from journal publishers' guidelines. *Perspectives in Clinical Research*, *16*(1), 56–57. https://doi.org/10.4103/picr.picr_67_24

---

## Persistent issues (pre-dating this edit, not yet addressed)

- **prev 4.1** — Peer reviewer competence (§6.3): "reviewers can assess" without noting that this requires training or familiarity currently absent
- **prev 4.2** — Five moves vs. three arguments: §1 and §7 still describe the paper's contribution differently
- **§4.1 folder tree**: comment "loaded automatically by Claude Code" names Claude Code specifically — tool-specific in a section meant to be tool-agnostic; been present since v1

---

## Net assessment

Good progress again: approximately fourteen items resolved in this pass, building on the previous round. The draft is now mostly clean in §§3–6. The remaining work is concentrated in three areas: (1) a single grammar error in §2.2 that needs a one-word fix; (2) the conclusion (§7) needs a list item corrected; and (3) the §5.1 opening sentences need light revision and the §4→§5 bridge needs a proper connective sentence. The structural mismatches (five moves vs. three arguments; peer reviewer competence) remain from earlier review cycles.

**Priority for next pass:**  
1. Fix "thus, there is no widely established framework explicitly theorises" — insert "that" (NC-new-1)  
2. Fix "through analysis of data" in §7 em-dash list (NS-new-2)  
3. Revise §5.1 opening sentences: hyphenate "well-crafted," fix "open science," and add a proper §4→§5 bridge sentence (NS-new-1 / prev 1.2)  
4. Fix Zrubka year: (2025) in text vs. (2023) in reference (New-4)  
5. Clean Holst and Mondal reference formatting (NA-new-2, NA-new-3)  
6. Remaining addressable items (NA3, NA1 partial, NA-new-1)

---

*Status check complete — 2026-04-16*
