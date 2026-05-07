# Author input: 2026-05-07

## Gap assessment and v10 edits

The gap assessment emerged from a request I made at the end of the previous session — I asked for an evaluation of v10 against the simulation reviews and the asshole-reviewer attacks. The framework for what counts as a gap was mine: I wanted to know which of the adversarial criticisms the draft had not yet addressed, not just a general quality review. The six gaps identified (Pruschak & Hopp absence, Collins/Polanyi absence, drafting-stage caveat, GAIDeT/Jones absence, Gelman–Loken on documentation itself, provenance acknowledgement) were all things I could either confirm from my own reading or was prepared to accept as plausible given the paper's argument.

The edits themselves were directed in the gap assessment document. I did not review each edit in detail before accepting — the gap assessment established the rationale, and I treated the implementation as following from that. The Sant'Anna footnote flag is a case where I wanted a note added but was uncertain whether the URL I had in mind was final; the author flag in the draft records that.

## Journal change to Social Epistemology

The decision to move from SMR (set 2026-05-02, then deferred 2026-05-06) to Social Epistemology was mine. After the structural reframe to an authorship argument rather than a methods contribution, the paper no longer fit a quantitative methods journal. Social Epistemology was the venue I had in mind: it is the right disciplinary register — philosophical and argumentative, with a policy dimension — and the paper's register had moved in that direction. I did not need to be persuaded of this; I initiated the change after deciding the reframe was complete enough to settle the venue question.

Confirming the IFA requirements required the author instructions page, which was returning 403. I pasted the text directly into the session. The key details I wanted confirmed were the word limit (I suspected it would be tighter than SMR's 10,000) and the abstract format (I had been assuming unstructured but wanted confirmation). Both were as expected. The 6,000–8,000 word ceiling (inclusive of references) is tighter than I had worked to; it establishes that the draft needs to come down.

## Reference format

I provided the style guide PDF (tf_chicagoad.pdf) after noticing that the CLAUDE.md had a placeholder reference to Chicago 18th edition. The 17th edition was confirmed as correct from the PDF. I asked for the full reference list to be reformatted and for British English and other formalities to be checked at the same time — this was a combined instruction that I did not break into separate steps.

The bibliography construction from the upload folders was a specific initiative I took based on noticing that several reference entries in the draft were incomplete (no pages, no full author lists, no DOIs). The approach — using rename_mappings.json and openalex_retained.csv as the primary data source rather than re-reading PDFs — was Claude's suggestion, and it was sensible. I specified that the scope should be the upload_theme_*/ folders only, not the full literature corpus. The output (literature/chicago_references.md) is something I expect to use as the authoritative bibliography going forward.

The two flags that remain unresolved — Mitchell et al. and Kosch and Feger — are author-side verifications. The Mitchell discrepancy is particularly important: there appear to be two different papers that look similar, and only I can identify which one I intended to cite. I will resolve this before submission.
