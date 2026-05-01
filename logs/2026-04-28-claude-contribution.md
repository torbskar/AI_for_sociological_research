# Claude contribution: 2026-04-28

## Literature assessment — Initiated by author query

*Author query as intellectual contribution — asked for an assessment of two specific files against the current draft, structured as impact assessment before implementation approval. The sequencing (plan before edits) was author-specified.*

Produced a ranked assessment of five Elicit sources by impact on the draft: Kosch & Feger (2025) and Asher et al. (2026) as high-impact (directly supporting existing arguments); He et al. (2026) as medium-high (independent convergence from ML/AI); Singh (2026) and Elsevier (2025) as low/negligible (engineering blog; publisher promotional material). Issued a reliability caveat on `AI_PHacking_Summary_Report_2026.md` as likely AI-generated — recommended not citing its references until independently verified.

Identified specific insertion points in v6 for each high/medium-impact source: section, paragraph, and function (new evidence, independent corroboration, contrast case, named concept). Mapped Asher et al. to adversarial configuration; Kosch & Feger to pre-registration analogy and systematic/unsystematic section; He et al. to documentation and "cannot guarantee" sections.

## v7 insertions — Initiated by author query

Executed six targeted insertions and added four references. No structural changes; all additions supplement existing arguments rather than opening new ones. Adjusted "second directional failure" to "further directional failure" to avoid inaccuracy after inserting Asher et al. between Cheng et al. and Peters & Chin-Yee.

## Logging reliability assessment — Initiated by author query

*Author query as intellectual contribution — the framing "is the logging in these sources more sophisticated or reliable than what I propose?" directed the comparison toward an honest evaluation rather than a source inventory. The author anticipated the answer might require a concession and asked specifically.*

Produced the distinction that the two approaches serve different functions: Singh's automated telemetry is more reliable for machine-behavior accountability (captures reasoning trace before each tool call; machine-generated; tamper-resistant); the paper's author-input files capture human intellectual contribution, which automated logging does not cover. Framed this as complementary rather than competing, but identified the manual log's dependence on researcher diligence as a genuine limitation worth stating. Recommended adding both the "epistemically lossy" He et al. formulation and the Singh concession to "What systematic use cannot guarantee."

## SocArXiv policy note — Initiated by author query

Fetched https://socopen.org/ai-policy/, extracted full policy structure (acceptable/prohibited uses, stated goal, detection approach), and identified the "slop" quote as field-specific urgency evidence. Created `notes/socarxiv-ai-policy.md` with full reference, key quote, policy structure, and notes on relevance — including the observation that the policy implicitly recognises task-based distinctions (acceptable-use list with "human verification" clause) while leaving the systematic/unsystematic axis unaddressed.
