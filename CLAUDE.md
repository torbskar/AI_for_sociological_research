# CLAUDE.md — Project: Structured AI Use in Sociological Research

## Project overview

This paper argues for a principled distinction between *structured* and *unstructured* AI use in academic research, develops a practical workflow implementing structured use across the full research process, and draws implications for journal policy. The target journal is **Sociological Science** (open access, Diamond OA).

The paper is both descriptive (here is a workflow) and softly normative (structured use is epistemically and ethically preferable to unstructured use, and current journal policies do not make this distinction). It must be framed as a **methodological contribution**, not a commentary — Sociological Science expects substantive sociological scholarship, not opinion pieces.

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

## Target journal requirements (Sociological Science)

- Diamond open access (no APC)
- **No word limit** — but brevity is explicitly valued and long literature reviews are discouraged. Keep the literature review section short and concise; the extensive background work feeds the argument, not the prose.
- Abstract: 150 words maximum
- All sociological scholarship types welcomed, including novel theoretical ideas without empirical results
- **Replication package mandatory** (since April 2023): must submit statistical code and data sufficient to reproduce reported results as condition of publication. For this paper, the transparency artefacts (prompt templates, skill files, R scripts, search logs) serve as the replication package — this is a strong fit and should be noted explicitly in the methods section.
- Qualitative work: data analysis methods must be documented; anonymity and consent disclosures required
- Quantitative work: substantive effect sizes over statistical significance; graphical displays preferred; control variable tables in appendices
- No explicit AI policy — consistent with the paper's argument that current policies are underdeveloped
- Follows COPE Code of Conduct; CrossCheck/iThenticate similarity screening applies
- Check current author guidelines and Manuscript Preparation page before submission

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
- Long literature review sections — Sociological Science explicitly discourages them
- Commentary or opinion-piece tone — must read as methodological scholarship
