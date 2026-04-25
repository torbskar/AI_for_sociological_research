# Claude contribution: 2026-04-23

## research-project-setup skill created

**Skill architecture and content** — Initiated by author query

*Author query as intellectual contribution — specified that the skill should (a) cover CLAUDE.md subfolder splitting, skardhamar-style, naming conventions, and literature search setup; (b) include logging, especially with a new Claude-contribution file analogous to the author-input file; (c) treat queries as intellectual contributions in accordance with query-authorship; and (d) check existing state before asking targeted questions about gaps. This specification determined the skill's scope, structure, and the conceptual distinction between the three log file types.*

Proposed a plugin structure with SKILL.md, `references/`, and `examples/` directories following Claude Code's progressive disclosure design pattern. The `references/` directory carries the detail (log formats, contribution guide, pipeline, project structure templates) while SKILL.md stays lean (~1,800 words). This architecture means the skill loads efficiently on trigger and pulls detail as needed.

**Three-file logging system formalization** — Initiated by author query

*Author query as intellectual contribution — introduced the requirement for a Claude-contribution file paired with the existing author-input file, and specified that it should record decisions/reasoning and initiative attribution, treating queries as intellectual contributions consistent with query-authorship.*

Designed the initiative attribution taxonomy (Initiated by author query / Claude initiative) and the query-authorship annotation format. The annotation — `*Author query as intellectual contribution — [description]*` — provides a specific mechanism for documenting when the author's query was itself the intellectual contribution rather than merely an instruction. This operationalizes query-authorship within the transparency artefact system.

**`references/claude-contribution-guide.md`** — Claude initiative

Proposed a dedicated reference file explaining the purpose, scope, and practical writing guidance for claude-contribution files. The observation that a pattern of predominantly "Claude initiative" labels is diagnostic of under-structured use was not in the author's query — it follows from the structured/unstructured distinction and provides a self-auditing function for the logging system.

**Log-index four-column format** — Initiated by author query

Extended the existing two-column index to four columns, preserving all existing data with `—` in the Claude-contribution column for prior sessions. The decision to use `—` rather than leaving the cell empty was a minor execution choice to keep the table readable.

**Skill name selection** — Initiated by author query

Author chose `research-project-setup` from four options (also presented: `sociology-research-project`, `structured-ai-research`, `research-project-setup`). Claude generated the option set; the choice was the author's.
