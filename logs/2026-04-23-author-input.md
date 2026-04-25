# Author input: 2026-04-23

The request today was entirely mine. I asked for a new skill based on the existing empirical-article-writer skill but extended and refined for the infrastructure used in this project. The specification was detailed and deliberate: I named the specific elements I wanted covered (subfolder CLAUDE.md files, skardhamar-style, naming conventions, literature search setup including scripts and search strings), flagged the logging procedure as of particular importance, and introduced the core requirement for a Claude-contribution log paired with the author-input log.

The conceptual framing for the Claude-contribution file was mine. I specified that it should treat queries as intellectual contributions in accordance with the query-authorship idea developed in the paper itself. This is a direct application of the paper's core argument to its own production infrastructure — the transparency artefact system should document not only what was produced but what the author contributed through their queries and configurations.

I also specified the skill's behavioral logic: it should check what is already present before asking questions, ask specifically about what is missing, and offer the choice of fixing immediately or leaving as a TODO. This reflects my preference for working interactively with what exists rather than re-scaffolding from scratch.

I approved the skill name `research-project-setup` after reviewing the options. The choice was mine on the basis that the name should emphasise the scaffolding function and remain general enough to apply to any structured AI-assisted social science research project, not only to this paper.
