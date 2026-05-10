# Trimming note: v11 → target ≤ 8,000 words

Current count: 9,557 words. Target: 8,000 or under. Gap: ~1,500 words.
Constraint: no paragraphs removed. All cuts are within paragraphs.

Estimated savings per section noted in brackets. Total realistic target: 1,200–1,500 words.

---

## Introduction [~150 words]

- "Their adoption in social science research is rapid, widespread, and will not be reversed (Grossmann et al. 2023)." Cut "and will not be reversed" — states the obvious, adds nothing argumentative.
- "These requirements address a genuine concern in a reasonable way." Cut entirely — throat-clearing before the concessive move; the move works without it.
- Counter-industry sentence: "More concretely, enforcement-oriented detection has already produced a counter-industry: services that strip AI-associated textual patterns from manuscripts before submission, driving AI use underground rather than making it transparent." Tighten to one clause, e.g., fold into the preceding sentence: "…where the incentive to under-report is highest — and enforcement-oriented detection has already produced services that strip AI-associated patterns before submission, driving use underground rather than making it transparent."
- Roadmap paragraph ("The argument proceeds in seven steps…"): currently ~130 words. Could compress to 70–80 by replacing the seven-step enumeration with two or three summary sentences. The enumeration is mechanical and the paper's structure is clear without it.
- "No new principle is required — the extension of existing replication-package norms to AI-assisted workflows is the instrument, and journals that already require replication packages already have the infrastructure." Two "already"s; cut the second clause here — it's stated again later and more forcefully.

---

## What AI does to authorship [~100 words]

- "This is a harder problem than it first appears." Cut — the paragraph that follows demonstrates it without announcement.
- Bullshit warning study list: each of the six studies (Kosch, Cheng, Peters, Ludwig, Barrie, Asher) gets its own sentence. Ludwig and Barrie make closely related points (prompt choice → variance, performance variance). Could compress to: "Ludwig, Mullainathan, and Rambachan (2024) and Barrie, Palmer, and Spirling (2025) demonstrate that seemingly innocuous choices — model, prompt formulation — produce substantially different estimates, with performance variance unacceptably high even under controlled conditions." Saves ~40 words.
- "The failure mode in unsystematic AI use is not random. It is directional: the tool confirms rather than challenges, and overstates rather than accurately reports." Merge: "The failure mode is not random but directional: the tool confirms rather than challenges, and overstates rather than accurately reports."
- ICMJE section: "The first three criteria raise important questions for AI-assisted research, which I take up in the next section. The fourth is the sharpest." The first sentence is redundant given the structure; cut it and lead with "The fourth criterion is the sharpest."

---

## Query authorship [~80 words]

- Abbott paragraph: "This is not a concession made for AI; it is a general claim about where the judgment that distinguishes research resides." This is implied by the paragraph context; cut.
- "Query authorship may appear strikingly novel. It is not." Merge: "Query authorship is not as novel as it may appear."
- Boundary condition, final sentence: "A query that meets none of these markers is generic task delegation; a query meeting all three constitutes query authorship in the relevant sense." This restates the three markers just given. Cut.

---

## Systematic use [~100 words]

- "Without all three features, query authorship cannot be demonstrated." paragraph: the three-sentence mechanical elaboration (criteria without verification produces…; verification without documentation produces…; documentation without explicit criteria produces…) is useful but slightly over-explained. The last sentence ("Documentation without explicit criteria produces artefacts that record what happened but not what was supposed to happen — and therefore cannot show that the process was sound, only that it occurred") is the weakest of the three. Consider cutting it and ending after the second.
- Literature search paragraph: the three-routes description runs long. "Each route catches what the others miss" — this sentence can be cut; it is implied.
- Review section: the synthesis protocol sentence at the end ("act on objections raised independently by two or more models; flag for individual judgement…") is a useful list but could be compressed from four clauses to three by merging the last two ("disregard sycophantic positive feedback" is the obvious corollary of adversarial configuration already described).
- Project folder structure: the explanation after the code block ("A configuration file at the project root encodes the research scope…") repeats points already made about the systematic/unsystematic distinction. The paragraph could lose one sentence — probably "A second specifies access controls — in particular, that `data/raw/` is excluded from the AI's context regardless of how the tool is used in a given session" since this was already stated in the empirical analysis paragraph.

---

## Externalising tacit knowledge [~150 words]

- Opening enumeration (before a search string… before a screening rubric… before an analysis script… before a reviewer configuration…): four instances is one too many. The analysis script instance ("the researcher must specify which variables operationalise the theoretical concepts and which estimator fits the data structure") is the most specialised to quantitative work and sits awkwardly in a methods-neutral paper. Cut it and replace with a closing generalisation.
- Pre-registration parallel: the Syed (2024) sentence at the end of the second paragraph ("Syed (2024) makes the related point that the epistemic argument for externalising decisions in advance applies equally to qualitative research and secondary data analysis, not only to confirmatory experimental work. The same applies here.") — "The same applies here" is redundant. Cut that final sentence.
- Writing-as-thinking: the final three sentences make one point. Trim to two: "This is the cognitive work that query authorship captures. Query authorship and writing-as-thinking are the same intellectual move at different sites — the specification and the manuscript paragraph — and in both cases the epistemic value lies in the externalisation of tacit structure into explicit form. Systematic use extends the hermeneutic circle; it does not replace it." Removes the middle sentence of the current three.

---

## Documentation package [~150 words]

- "What systematic use cannot guarantee" closing paragraph: "The argument here is not that all AI use must be systematic, any more than the case for replication packages implies that all analysis must be automated." — this is a fine opening for the paragraph. But the paragraph then runs to five sentences that partly duplicate the "burden of evidence" section two paragraphs earlier. The last three sentences (from "The same logic governs open science practices more broadly…") repeat the conservative-prior argument already made. Cut those three sentences; end the paragraph after "evidence of how one worked."
- Zeng et al. hedging: three sentences for one speculative point. Compress to: "Zeng et al. (2025) find that reproducibility correlates positively with accuracy across more than a thousand data-science tasks — suggesting, though not establishing for social science specifically, that systematic use may be a quality mechanism as well as a transparency one."
- Open science / journals paragraph ("Journals that already require replication packages…"): second paragraph is the strongest; first paragraph slightly repeats the policy section. Could trim one sentence.

---

## Policy implications [~80 words]

- "The concession matters; the argument is about the instrument, not the intent." Cut — this meta-comment is unnecessary; the concessive move speaks for itself.
- Sibbald et al. sentence: "A disclosure that names AI use without specifying the epistemic structure of that use is a performance rather than a practice (Sibbald et al. 2025)." The Sibbald paper is about positionality in qualitative research, not AI disclosure — the analogy is loose. Consider cutting this citation and sentence, or replacing with a simpler formulation without the citation.
- Reporting checklists sentence: "Zrubka et al. (2023), Holst et al. (2025), Agha et al. (2025), Mondal et al. (2025), and Ganjavi et al. (2024) have developed and assessed a range of these instruments; they address what was done and whether it was disclosed, not whether the process was epistemically sound." This point was already made in the introduction. Could cut or fold into a single clause appended to the previous sentence.

---

## Conclusion [~80 words]

- First paragraph is a long recapitulation (~180 words). The final sentence ("The policy directive follows: require documentation packages for AI-assisted work, ask not whether AI was used but whether the process can be shown.") repeats the policy section almost verbatim. Cut it from the conclusion; the paragraph ends more strongly on the documentation package sentence.
- Second paragraph is tight and strong — keep as is.
- Scope note: keep as is.

---

## Summary of largest single savings

| Location | Cut | Estimated saving |
|---|---|---|
| Intro roadmap paragraph | Compress from 7-step list to 2–3 sentences | ~60 words |
| Guarantee section closing paragraph | Cut last 3 sentences (duplicate of burden-of-evidence section) | ~100 words |
| Bullshit warning citations | Compress Ludwig + Barrie to one sentence | ~40 words |
| Writing-as-thinking | Cut middle sentence of three-sentence conclusion | ~35 words |
| Zeng hedging | Compress to one sentence | ~50 words |
| Policy checklists citation list | Fold into preceding sentence or cut | ~45 words |
| Conclusion first paragraph final sentence | Cut | ~30 words |
| Various small trims throughout | As noted above | ~300 words |
| **Total** | | **~660–750 words** |

This brings the count to approximately 8,800–8,900. A further pass tightening individual sentences throughout (cutting redundant qualifiers, merging short adjacent sentences, cutting "it is important to note that"-style throat-clearing) should yield the remaining 800–900 words. No argument is lost in any of these cuts.
