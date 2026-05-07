# CLAUDE.md — Project: Structured AI Use in Social Science Research

## Project overview

This paper argues for a principled distinction between *systematic* and *unsystematic* AI use in academic research, develops a practical workflow implementing systematic use across the full research process, and draws implications for journal policy. Target journal: ***Social Epistemology: A Journal of Knowledge, Culture and Policy***, published by Taylor & Francis (Routledge).

The paper is both descriptive (here is a workflow) and argumentative (systematic use is epistemically preferable to unsystematic use, and current journal policies do not make this distinction). It is framed as a **conceptual and argumentative contribution to the epistemology of research practice** — Social Epistemology publishes interdisciplinary philosophical and social-scientific work on the production, assessment, and validation of knowledge, which is precisely this paper's register. It is not a methods paper and should not be written as one.

## Core argument

1. The systematic/unsystematic distinction — not AI use versus non-use — is the epistemically relevant axis for policy.
2. Systematic AI use forces explicit articulation of tacit research decisions, functioning analogously to pre-registration.
3. This produces transparency artefacts (prompt templates, skill configurations, search logs) that are open-science compatible.
4. Current journal policies, even the more sophisticated tiered approaches, organise disclosure along the wrong axis — what was used and whether it was disclosed, rather than whether the process was epistemically sound.
5. A documentation-based framework, organised around the systematic/unsystematic distinction, is the appropriate instrument — and existing replication-package infrastructure already supports it.

## Key conceptual distinctions (use consistently throughout)

- **Systematic use**: tool configurations with explicit criteria, built-in human verification at each stage, documented outputs
- **Unsystematic use**: accepting AI outputs without explicit criteria, verification, or documentation
- **Query authorship**: the intellectual contribution in AI-assisted research resides in the query — search criteria, screening rubrics, analytical specifications, reviewer configurations — not in the generated text
- **Skills / reviewer skills**: configured AI personas with discipline-specific review criteria
- **Transparency artefacts**: prompt templates, skill files, search logs, session records — shareable as documentation package / replication materials

## Writing instructions

- Use the `skardhamar-style` skill for all prose drafting and review
- First-person, explicitly argumentative stance throughout
- Hedging hierarchy must be strictly observed (see style skill)
- No bullet points in running prose — use natural language enumeration
- Concessive moves required before any critique of journal policies or existing AI guidance
- Scope limitations stated at point of relevance, not batched
- Literature review in the paper itself must be **short and concise** — cite to support claims, do not survey. The extensive background work done here feeds the argument, not the prose.
- Frame consistently as a **conceptual and argumentative contribution to the epistemology of research practice**: the paper demonstrates a workflow, argues for its epistemic properties, and draws policy implications. The audience is philosophers, science studies researchers, and social epistemologists — not primarily methods specialists. The argument must be philosophically credible, not just practically useful.

## File structure

```
ai-sociology-paper/
├── CLAUDE.md                        ← this file (project-wide context)
├── logs/                            ← session logs, author-input records (see logs/CLAUDE.md)
├── literature/                      ← search results, PDFs, notes, pipeline guide (see literature/CLAUDE.md and PIPELINE.md)
├── notes/                           ← working notes; used/ for archived (see notes/CLAUDE.md)
├── draft/                           ← manuscript versions (see draft/CLAUDE.md)
├── outline.md                       ← working outline
├── scripts/                         ← R and Python search/processing utilities
├── supplementary/                   ← example skills, prompt templates, guides
└── dismissed_ideas/                 ← archived approaches with reasons
```

Folder-specific protocols (logging, draft versioning, notes archiving, literature tasks) are in `CLAUDE.md` files within each subfolder.

**Session-start protocol**: see `logs/CLAUDE.md`. Run it at the start of every session before any other work.

## Target journal requirements (*Social Epistemology*, Taylor & Francis)

Author instructions page: https://www.tandfonline.com/action/authorSubmission?show=instructions&journalCode=tsep20

- **Full title**: *Social Epistemology: A Journal of Knowledge, Culture and Policy*, Taylor & Francis (Routledge)
- **Scope**: Interdisciplinary forum for philosophical and social-scientific enquiry on the production, assessment, and validation of knowledge — both empirical and normative. Audience includes philosophers, sociologists, psychologists, cultural historians, science studies scholars, political theorists, and education researchers. The "Policy" in the subtitle means policy implications are within the journal's core remit, not peripheral.
- **Word limit**: 6,000–8,000 words, inclusive of tables, references, figure/table captions, and endnotes. Include a word count with submission.
- **Abstract**: Unstructured paragraph, 200 words maximum.
- **Keywords**: 3–4 keywords.
- **Language**: British English throughout (behaviour not behavior; -ise not -ize; etc.).
- **Manuscript structure**: title page; abstract; keywords; main text; acknowledgments; declaration of interest; references; appendices (if any). The journal's boilerplate lists a biomedical IMRaD structure, which does not apply to conceptual/argumentative pieces.
- **Style**: Single quotation marks; long quotations indented without marks; no semicolons where avoidable; em dashes used sparingly; active voice; gender-neutral language; do not address the reader directly. No serial comma requirement stated; use consistently.
- **Format**: Times New Roman 12pt, double-line spacing, margins ≥ 2.5cm. Figures submitted separately (TIFF/JPEG/PS, 300 dpi colour / 600 dpi grayscale / 1200 dpi line art).
- **Biographical note**: Up to 200 words per author.
- **Reference format**: Chicago author-date, 17th edition (2017). T&F style guide confirmed: journal articles as `Surname, Given. yyyy. "Article Title." *Journal Title* vol (issue): pp–pp. https://doi.org/DOI.`; books as `Surname, Given. yyyy. *Book Title*. City: Publisher.`; two-author entries use "and" before second author in both citations and reference list; no en-dash replacement for repeated author names; hanging indent throughout. DOIs for published journal articles will be added by T&F production — authors do not need to include them in manuscript submissions (though including them is harmless).
- **Peer review**: Anonymised blind review; initial editor screening.
- **Open access**: APC-based open access available; institutional T&F agreements may apply. Verify current APC.
- **Data sharing**: T&F Basic Data Sharing Policy — authors encouraged (not required) to deposit data and provide a Data Availability Statement. The transparency artefacts (prompt templates, skill files, search scripts, session logs) serve as the documentation package; depositing these in a recognised repository and citing the DOI satisfies this policy and is a direct instantiation of the paper's argument.
- **AI policy (Taylor & Francis)**: All generative AI use must be disclosed in the Methods or Acknowledgements section. Required disclosure elements: full tool name, version number, how it was used, reason for use. AI cannot be listed as author. Authors remain accountable for accuracy, validity, and integrity of AI-assisted content. T&F does not distinguish assistive from generative AI — all generative AI requires specific disclosure. This paper's systematic AI use must be disclosed; the methods section (documentation package description) is the natural location and a direct instantiation of the paper's argument.
- **Critique note**: T&F's policy requires disclosure and author accountability but does not distinguish systematic from unsystematic generative AI use — the paper's critique applies at this level. The concessive move in the policy section must acknowledge T&F's disclosure requirement as a genuine step before pressing the systematic/unsystematic argument.
- **Submission system**: Taylor & Francis online portal (ScholarOne); verify exact submission URL from IFA.
- Follows COPE Code of Conduct; similarity screening applies.

## What this paper is NOT

- Not a review paper cataloguing all AI tools
- Not a technical paper about how AI works
- Not a polemic against journal policies
- Not a claim that AI replaces expert judgment

## Key things to avoid in drafting

- Overstating the reliability of AI outputs
- Treating the workflow as universally applicable (scope it to the social sciences, not all academic disciplines)
- Making the journal policy critique the main event — it is an implication, not the thesis
- Generic "AI is changing everything" framing in the introduction
- Long literature review sections — the word limit is 6,000–8,000 words inclusive of references; every word counts
- Commentary or opinion-piece tone — must read as philosophically credible scholarship
