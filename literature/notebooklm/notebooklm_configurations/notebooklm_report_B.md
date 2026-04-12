# NotebookLM Synthesis Report — Notebook B

## Theme: Explicit reasoning, pre-registration, open science, tacit knowledge

**Date:**
**Sources:** [N] PDFs, Theme B top 50
**Configuration:** `supplementary/example-notebooklm-configuration.md`

---

**STANDING INSTRUCTIONS — applies to all sections of this report:**

*This is a manual workflow. Submit each query (Q0, Q1, etc.) separately in
NotebookLM and paste the response into the corresponding section before
moving to the next query. Do not submit the whole document as a single prompt.*

*Citations:* Every substantive claim must be cited in the text immediately
after the sentence it supports, using author-year format, e.g. (Smith et al.,
2023). If multiple sources support a claim, cite all of them. Do not group
citations at the end of a paragraph.

*Source coverage:* All sources in this notebook must be considered when
answering each query. Sources that are not informative for a given section
should not simply be ignored — they must be listed in the "Sources not drawn
on" section at the end of the report, with a brief explanation of why they
did not contribute (e.g. not relevant to the theme, too general, overlaps
with a stronger source, does not address the question asked).

---

## 0. Source coverage check

*Q0 — submit this exact text to NotebookLM before any other query:*

> This notebook contains [N] sources. List ALL of them by title, one per line,
> numbered. For each, write one sentence on what it covers and whether it is
> relevant to open science, pre-registration, tacit knowledge, or the
> epistemology of research practice. Do not skip any source. If you cannot
> identify [N] distinct sources, say so explicitly and state how many you found.

*(Replace [N] with the actual number of sources uploaded before submitting.
Later queries should reference: "drawing on all [N] sources listed in Q0,
including those not yet cited in earlier sections.")*

[Paste response. Cross-check: does the count match what you uploaded?]

---

## 1. Epistemic functions of pre-registration and open science

*Q1: What epistemic functions do sources attribute to pre-registration, open
science, and transparency practices — what problems are they argued to solve,
and how? Draw on all sources from Q0.*

The sources attribute several critical epistemic functions to pre-registration, open science, and transparency practices, primarily framing them as tools to ensure the **reliability, validity, and self-correcting nature of scientific knowledge** (Nosek et al., 2022; Skubera et al., 2025; Tyner et al., 2026). These practices are argued to solve systematic failures in the research ecosystem by restructuring incentives and making the research process visible to both experts and the public (Heesen & Bright, 2025; Skubera et al., 2025).

### 1. Limiting Analytical Flexibility and QRPs
A primary problem these practices solve is the prevalence of **Questionable Research Practices (QRPs)**, such as *p-hacking* and *HARKing* (hypothesizing after results are known), which exploit "researcher degrees of freedom" to find significant results (Nagy et al., 2025; Skubera et al., 2025). 
*   **Pre-registration:** By requiring researchers to time-stamp their hypotheses, methods, and analysis plans before data collection, pre-registration **demarcates confirmatory from exploratory analyses** (Syed, 2024). This makes undisclosed data-dependent decision-making more detectable and prevents the framing of post hoc discoveries as a priori predictions (Nagy et al., 2025; Syed, 2024).
*   **Transparency Checklists:** Using standardized reporting guidelines (e.g., JARS) and checklists ensures that critical methodological steps are not omitted, thereby reducing the "garden of forking paths" where researchers might otherwise choose only the most favorable results (Nagy et al., 2025).

### 2. Mitigating Publication Bias
Sources argue that the research ecosystem has historically rewarded **novelty over robustness**, leading to a "file drawer effect" where null results are rarely published (Heesen & Bright, 2025; Skubera et al., 2025).
*   **Registered Reports:** This publishing model integrates pre-registration by providing **peer review of study designs *before* data collection** (Skubera et al., 2025; Syed, 2024). This shifts the epistemic focus from the nature of the results to the rigor of the methodology, guaranteeing publication regardless of the outcome and thus directly countering publication bias (Skubera et al., 2025).
*   **Benefits for "Go-Between" Agents:** Transparency is particularly vital for non-experts—such as journalists and civil servants—who translate scientific findings into policy (Heesen & Bright, 2025). While sophisticated scientists might theoretically account for publication bias using Bayesian reasoning, **"go-between" agents require an unbiased publication record** to make accurate social and political decisions (Heesen & Bright, 2025).

### 3. Facilitating Error Detection and Verification
Transparency practices function to make research **Findable, Accessible, Interoperable, and Reusable (FAIR)**, which allows the scientific community to verify claims (Nagy et al., 2025; Skubera et al., 2025).
*   **Open Data and Code:** Sharing raw data and analytical code reduces "process reproducibility failures," allowing others to confirm that the reported results actually follow from the data (Nosek et al., 2022). 
*   **Integrity in the AI Era:** As generative AI increases the risk of **fraudulent, AI-generated research**, open science practices like transparent peer review and mandatory data sharing are argued to be the primary defense for maintaining scientific integrity (Lin, 2023).
*   **Robustness Reanalysis:** Transparency allows for "robustness checks," where independent teams test if a finding holds up under different analysis strategies using the same data (Nosek et al., 2022; Ozier, 2021). For example, the "Worm Wars" highlighted how data availability allowed epidemiologists to re-evaluate economic findings, uncovering how specific analytical choices—like sample weighting—affected the significance of results (Ozier, 2021).

### 4. Bounding Scientific Uncertainty
Transparency serves an important function in communicating the **tentativeness of scientific findings** to the public (Howell, 2020).
*   **Managing Expectations:** Openly reporting caveats and "hedging" language can actually **increase the perceived credibility** of scientists among non-experts, as it aligns with the public's expectation that science involves inherent uncertainty (Howell, 2020).
*   **Self-Correction:** Highlighting replication failures through open science initiatives (e.g., the SCORE program) is argued to be a sign of a **healthy, self-correcting discipline** rather than a sign of failure (Howell, 2020; Tyner et al., 2026). It reduces overconfidence in published claims by illustrating that "published" and "true" are not synonymous (Tyner et al., 2026).

### 5. Externalizing Tacit Knowledge
Beyond explicit data, transparency can serve to **externalize "tacit knowledge"**—the unspoken "know-how" required to translate research into real-world impact (Mitchell et al., 2022).
*   **Bridging the Gap:** By utilizing processes like **reflexivity and dialogical sense-making**, researchers can convert implicit tacit knowledge into explicit word or image formats, making it accessible to practitioners (Mitchell et al., 2022). This solves the problem of research impact being elusive due to the undervaluation of the background knowledge necessary to apply explicit findings in different contexts (Mitchell et al., 2022).

---

**Sources not drawn on:**
None. All 10 sources identified in Q0 were used to answer this query.

**Author notes:** *[Which problems recur? Which are specific to one field?
Note any claims that connect directly to structured AI use as an analogous practice.]*

---

## 2. Tacit knowledge in research

*Q2: How do sources treat tacit knowledge in research — as a problem, a
resource, or both? What role does making reasoning explicit play? Are there
accounts of what tacit knowledge consists of in practice?*

[Paste response.]

**Author notes:** *[Flag any sources that connect tacit knowledge to
reproducibility or to the documentation of research decisions.]*

---

## 3. Structured workflows and epistemic quality

*Q3a: Do sources draw connections between structured or documented research
workflows — specifying decisions in advance, recording criteria, building in
verification steps — and epistemic quality, research integrity, or validity?*

*Q3b: Do sources propose specific methods, protocols, or frameworks for making
research reasoning explicit? For each, describe the steps in enough detail
that an unfamiliar reader understands the procedure.*

*Q3c: Do any sources include templates, checklists, or worked examples for
structured research practice? List and describe them.*

[Paste response.]

**Author notes:** *[(a) Sources that make the analogy between structured
workflows and pre-registration explicitly; (b) sources where this connection
is implicit or can be inferred; (c) methods or templates usable as precedent
for the paper's argument.]*

---

## 4. Replication crisis and its lessons

*Q4: How do sources characterise the replication crisis — causes, scope,
proposed remedies? Which remedies involve making reasoning more explicit or
decisions more transparent?*

[Paste response.]

**Author notes:** *[Note whether sociology is discussed separately from
psychology or other fields where the crisis originated.]*

---

## 5. Synthesis

*Q5: Across sources, what is the core argument for why explicit, transparent,
and structured research practice is epistemically valuable? Where do sources
agree and where do they disagree?*

[Paste response.]

**Author notes:** *[What the literature supports for the pre-registration
analogy; what is contested; what is absent.]*

---

## Key claims for the paper

| Claim | Source(s) | Section in paper |
| ----- | --------- | ---------------- |
|       |           |                  |
|       |           |                  |
|       |           |                  |

---

## Gaps and follow-up

-
-

---

## Sources not drawn on

*Q6: Which sources were not cited in your previous responses, and why — not
relevant, too general, or overlapping with a stronger source?*

[Paste response, then supplement from Q0 list.]

| Source | Reason not cited |
| ------ | ---------------- |
|        |                  |
|        |                  |

---

## References

*Cited sources with full references from `literature/openalex_retained.csv`.
Format: Author(s) (Year). Title. Journal. DOI.*

---

<!-- INSTRUCTIONS (remove before archiving)

Run Q0 first. Cross-check Q0 list against citations in each section.
Q3 has three sub-queries: run all three, combine in Section 3.
If a method or framework is named, follow up: "Describe exactly how [method]
works step by step." Paste into Section 3.
Add citations and references as you paste. Run Q6 last.

-->
