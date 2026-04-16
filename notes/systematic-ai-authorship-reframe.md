# Systematic AI authorship — conceptual reframe

## Core reframe

The primary term going forward is **systematic AI authorship**, not "structured AI use". "Query authorship" may be retained as a sub-category or instance of this concept, but it should not carry the weight of the main argument.

The major claim: **systematic use of AI — including pipeline design, tool configuration, and workflow organisation — is de facto an authorship contribution**. The execution (what the AI actually produces) is not the most important thing. The intellectual structure built around it is. This inverts the intuition behind most current journal policy, which focuses on the generated text.

The subsequent sections/chapters discuss what systematic AI authorship can or should look like: documentation, pipelines, verification checkpoints, transparency artefacts. These are the practices that constitute authorship, not the prompts in isolation.

## The key contrast: systematic vs. unsystematic AI authorship

The relevant axis is **systematic vs. unsystematic**, not use vs. non-use, nor structured vs. unstructured (though the latter distinction survives as a description of practice).

- **Systematic AI authorship**: explicit criteria, documented decisions, built-in verification, reproducible outputs. Accountable and auditable.
- **Unsystematic AI authorship**: AI used without explicit criteria, outputs accepted without verification, no documentation. May produce excellent results, but is **unaccountable and unreliable** — there is no way to evaluate whether the output is sound.

The unsystematic/systematic distinction also explains where the binary permit/prohibit thinking in journal policy comes from: unsystematic AI authorship can produce bullshit at scale. The problems with p-hacking, HARKing, and related bad research practices are reinforced. Papermills and low-quality journals already polluted the scientific literature before AI; AI makes it dramatically easier to scale such bad science.

## Tighter link to open science

This reframe tightens the connection to open science practices. Systematic AI authorship *is* an open science practice — it produces transparency artefacts, requires pre-specification of criteria, and enables independent evaluation. The argument is not just that systematic use is better; it is that **open science practices become more important, not less, in an AI-saturated research environment**.

## Structural implication for the paper

A dedicated section or chapter on **pipelines and workflows** — how to organise a research project systematically using AI — is now warranted. This is currently folded into what was Section 4, but the framing shift may require giving it more prominence or restructuring the argument around it.

The chapter sequence might run: (1) the distinction → (2) what systematic authorship looks like in practice [pipelines, workflows] → (3) epistemic properties → (4) policy implications.

## Workflow and infrastructure notes (from this session)

- Global CLAUDE.md has been updated with new instructions.
- A `.gitignore` now excludes a `git-folder`, PDFs, and related large/copyright-sensitive files to prevent accidental republication of PDFs and to reduce token costs and GitHub storage. This is itself a structural change to the workflow and should be documented in the replication package.
- This kind of configuration decision — deliberate, documented, versioned — is an example of systematic AI authorship practice. Worth noting in the paper as an illustration.
