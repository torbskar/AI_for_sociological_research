# CLAUDE.md — Project: Structured AI Use in Sociological Research

## Project overview

This paper argues for a principled distinction between *structured* and *unstructured* AI use in academic research, develops a practical workflow implementing structured use across the full research process, and draws implications for journal policy. Target journal: ***Sociological Methods & Research* (SMR)**, published by SAGE.

The paper is both descriptive (here is a workflow) and softly normative (structured use is epistemically and ethically preferable to unstructured use, and current journal policies do not make this distinction). It must be framed as a **methodological contribution**, not a commentary — SMR publishes original research and methods contributions, not opinion pieces.

## Core argument

1. The structured/unstructured distinction — not AI use versus non-use — is the epistemically relevant axis for policy.
2. Structured AI use forces explicit articulation of tacit research decisions, functioning analogously to pre-registration.
3. This produces transparency artefacts (prompt templates, skill configurations, search logs) that are open-science compatible.
4. Current journal policies are blunt instruments that inadvertently penalise good practice.
5. A documentation-based policy framework is preferable to blanket restriction or blanket permission.

## Key conceptual distinctions (use consistently throughout)

- **Structured use**: tool configurations with explicit criteria, built-in human verification at each stage, documented outputs
- **Unstructured use**: accepting AI outputs without systematic verification or explicit criteria
- **Skills / reviewer skills**: configured AI personas with discipline-specific review criteria
- **Transparency artefacts**: prompt templates, skill files, search logs, NotebookLM source sets — shareable as supplementary materials

## Writing instructions

- Use the `skardhamar-style` skill for all prose drafting and review
- First-person, explicitly argumentative stance throughout
- Hedging hierarchy must be strictly observed (see style skill)
- No bullet points in running prose — use natural language enumeration
- Concessive moves required before any critique of journal policies or existing AI guidance
- Scope limitations stated at point of relevance, not batched
- Literature review in the paper itself must be **short and concise** — cite to support claims, do not survey. The extensive background work done here feeds the argument, not the prose.
- Frame consistently as a **methodological contribution**: the paper demonstrates a workflow, argues for its epistemic properties, and draws policy implications. It is not a think-piece or a commentary.

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

## Target journal requirements (*Sociological Methods & Research*, SAGE)

- **Subscription journal** with open access options (not Diamond OA); SAGE transformative agreements may apply
- **Word limit: 10,000 words**, including references and tables — a binding constraint; keep the draft tight
- **Abstract**: structured abstract required; exact word limit not confirmed — verify before submission
- Original research and methodological contributions; no empirical results required for methods papers
- **Open Science Policy** (applies to all manuscripts submitted after June 1, 2025): data, code, and materials must be openly accessible; authors must provide anonymised code and materials at submission for peer review; replication package in a trusted public repository required. For this paper, the transparency artefacts (prompt templates, skill files, R scripts, search logs) serve as the replication package — note explicitly in the methods section.
- **AI policy (SAGE)**: distinguishes *assistive* AI (grammar, language, structure — no disclosure required) from *generative* AI (content affecting methodology, analysis, results — must be disclosed in the methods or acknowledgements section). LLMs cannot be listed as authors. Undisclosed generative AI use can trigger rejection at any stage. This paper's structured AI use falls under the generative category and must be disclosed — the methods section is the natural location and a direct instantiation of the paper's argument.
- **Critique note**: SAGE's policy is more nuanced than a blanket ban but still does not distinguish structured from unstructured generative AI use — the paper's critique applies at this level, not at the assistive/generative level. The concessive move in §6 must acknowledge the SAGE policy's sophistication before pressing the argument.
- Double-blind peer review; submitted via ScholarOne Manuscripts (mc.manuscriptcentral.com/smr)
- Follows COPE Code of Conduct; iThenticate/CrossCheck similarity screening applies
- Verify current author guidelines and abstract format before submission

## What this paper is NOT

- Not a review paper cataloguing all AI tools
- Not a technical paper about how AI works
- Not a polemic against journal policies
- Not a claim that AI replaces expert judgment

## Key things to avoid in drafting

- Overstating the reliability of AI outputs
- Treating the workflow as universally applicable (scope it to sociology and adjacent fields)
- Making the journal policy critique the main event — it is an implication, not the thesis
- Generic "AI is changing everything" framing in the introduction
- Long literature review sections — SMR has a 10,000-word limit (including references); every word counts
- Commentary or opinion-piece tone — must read as methodological scholarship
