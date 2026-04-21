# Developer review: "Systematic AI Use in Sociological Research"

**Reviewer role:** Senior software developer / LLM systems architect  
**Date:** 2026-04-19  
**Draft reviewed:** v3, 2026-04-16

---

## Prefatory note

I am not the target audience for this paper, and I know it. What follows is what I would tell a researcher colleague who had showed me their setup: where the workflow resembles good professional practice, where it does not hold up against what we actually know about LLM deployment, and one concrete thing they are missing. I am not commenting on the sociological argument, the policy case, or the authorship theory. Those are not my domain.

---

## 1. The two weakest points in the described workflow

### 1.1 Model versioning is mentioned once and then structurally absent

The paper notes in §5.4 that "the same prompt, run twice at the same temperature setting, will almost certainly produce different outputs," which is correct. But it draws the wrong operational conclusion from this — it frames non-determinism as a documentation problem (log the outputs, note differences) rather than as a versioning problem.

Here is the professional-practice gap: a prompt template in a replication package tells me nothing about what model it was run against. Claude is not one thing. `claude-opus-4`, `claude-sonnet-4-5`, `claude-haiku-4-5` are meaningfully different models with different capability profiles, different instruction-following behaviour, and different tendencies on exactly the properties this paper cares about — sycophancy resistance, factual accuracy, adherence to complex rubrics. More importantly, these models are updated without changing their names, or retired and replaced. A skill file submitted as supplementary material in 2026 will not produce comparable outputs in 2028 against whatever model the API routes to by default. This is not a hypothetical concern; it is the lived experience of anyone who has maintained production LLM pipelines.

The paper's supplementary materials, as described, do not include model version pinning. The replication package can contain a beautiful screening rubric and still be unreproducible in any meaningful sense if the model it was designed against is no longer available or has been silently updated. In professional deployment, we pin model versions in configuration — not in prose notes, but as a mandatory field in every API call. A `CLAUDE.md` that does not include a `model:` field is incomplete by the standards of any production deployment.

This is the single biggest gap between what the paper claims about reproducibility and what the underlying setup actually delivers. The transparency artefacts are real, but they reproduce the *form* of the workflow without the conditions under which it produced the documented outputs. That is a meaningful distinction, and the paper should address it directly rather than treating non-determinism as merely a logging problem.

**What the paper should do:** Add model version pinning — including full model string, not just model family — as a required field in the project configuration (`CLAUDE.md`), in the session logs, and in the supplementary materials. Acknowledge that outputs produced against a pinned model string cannot be guaranteed to reproduce against a later model, even if the prompt is identical. This is honest and does not undermine the reproducibility argument — it just positions it correctly.

---

### 1.2 The chat interface / API distinction is unresolved and its implications are not addressed

The paper operates almost entirely in a Claude Code environment — a terminal-based agentic interface — but never explicitly addresses the difference between that environment and the chat interface (claude.ai) that most social science researchers will actually use. This distinction matters more than the paper acknowledges, for three reasons that bear directly on its reproducibility and transparency claims.

**Context management.** In a chat interface, context is managed implicitly by the interface: messages scroll out of the context window without notice, the user has no reliable visibility into what the model is currently attending to, and there is no programmatic way to verify that the project context file (`CLAUDE.md`) is active in any given session. In Claude Code, context is loaded explicitly and its state is inspectable. The paper's entire configuration architecture — the two-level CLAUDE.md setup, the `.claudedocs/` instructions, the `.claudeignore` exclusions — depends on Claude Code semantics. A researcher who reads this paper and attempts to implement the workflow in the chat interface gets something that looks similar but behaves differently in ways that are not visible from the outside.

**Temperature and sampling settings.** The chat interface exposes no controls over temperature, top-p, or sampling parameters. The API does. This matters for the paper's reproducibility argument: two researchers running the same prompt against the same model version at different sampling temperatures will get different outputs, and there is no way to document or replicate the sampling conditions from a chat-interface session. The paper's §5.4 discussion of non-determinism implicitly assumes these settings are stable, but they are only stable if they are explicitly set — which requires API access.

**Session logging.** The paper places significant evidential weight on session logs and author-input files as contemporaneous records. In Claude Code, session state is written to `.claude/` and can be excluded from version control while still being locally archived. In a chat interface, session history is held by Anthropic's servers, export formats are limited, and the researcher does not have structural guarantees about retention or format stability. A researcher maintaining a session log from chat-interface exports has something different — less structured, less reliable — than what the paper describes.

None of this means the workflow only works in Claude Code. But the paper should say clearly: *this workflow, as described, requires Claude Code or equivalent API access, not a chat interface.* It should also note that the reproducibility properties it claims are contingent on that environment, not on the transparency artefacts alone. A researcher implementing the screening rubric and skill files via a chat interface is doing something systematically less reproducible than what the paper describes, without necessarily knowing it.

---

## 2. Would the transparency artefacts be sufficient to reconstruct the workflow?

Short answer: sufficient to reconstruct the *structure* of the workflow, not sufficient to reproduce *comparable outputs*.

What is present and genuinely useful:
- Skill files and prompt templates as described would give a developer enough to understand what criteria were applied and in what sequence. This is substantively better than nothing and better than most published AI-assisted research to date.
- The folder structure and configuration architecture (`CLAUDE.md`, `.claudeignore`, `.claudedocs/`) are professionally recognisable and implementable.
- The session logs and author-input files, if maintained as described, would provide an unusually detailed process record.

What is missing for a developer trying to reproduce comparable outputs:

1. **Model version string.** As discussed above. Without pinning, the replication package is a workflow specification, not a reproducibility guarantee.

2. **Temperature and sampling parameters.** Not mentioned anywhere in the paper. In Claude Code, these are either default (which is fine but should be stated) or configurable, but the paper gives no guidance on what settings were used.

3. **Context window state at generation time.** The paper cannot solve this problem — no one can, fully — but it should acknowledge it. Long sessions in Claude Code accumulate context that is invisible in the output artefacts: earlier exchanges, loaded files, tool call results. Two researchers starting from the same skill file and prompt template but with different session histories will have different effective contexts. The paper's session log structure partially addresses this (it records what was in the session), but the relationship between the session log and the model's actual context window at generation time is not the same thing.

4. **Interface specification.** As discussed: the paper should specify that the workflow requires Claude Code or API access and document which interface was used for which stages of the work it describes.

5. **Tool use configuration.** Claude Code supports tool use (file read, bash execution, web search). The paper's workflow likely uses some of these. The replication package should specify which tools were enabled and which were not, since tool availability affects what the model does even with identical prompts.

A developer receiving the supplementary materials as described could implement a recognisably similar workflow. They could not verify that their outputs are comparable to the original without the above information. For the paper's reproducibility argument, this gap matters.

---

## 3. Where the paper most closely resembles good professional practice

The strongest part of the workflow, from a professional standpoint, is the two-level configuration architecture: global instructions in `.claudedocs/` that travel across projects, and project-specific context in the local `CLAUDE.md`. This is exactly how we think about configuration management in production LLM deployments — separating stable system-level constraints from task-specific context, making both explicit and version-controlled. The insight that a project-level context file can function as a persistent framing mechanism that eliminates prompt-by-prompt re-specification is correct and well-implemented. Most researchers using AI tools have not thought about this at all; it genuinely distinguishes systematic from unsystematic use.

The `.claudeignore` mechanism as a structural data-access control — not a norm but an enforced boundary — is also professionally sound. The `PreToolUse` hook for PII screening is, frankly, more sophisticated than what most small development teams implement. These are not cosmetic features; they are the difference between a documented intention and a structural guarantee.

The two-tier documentation structure (working logs as process record, supplementary materials as replication package) maps onto a distinction we care about in professional contexts: the difference between audit trail and specification document. Most researchers conflate these or produce neither; having both, with distinct functions, is the right design.

**How the paper could make this resemblance more explicit:** The paper could note — briefly, without technical language — that the configuration architecture it describes is structurally analogous to how software teams manage environment configuration across projects: a shared base configuration that travels with the developer, and project-specific overrides. The analogy is not perfect but it is close enough that readers familiar with any kind of software project setup (R project structure, `.Rprofile`, `.Renviron`) will recognise the logic. This framing would strengthen the reproducibility argument without requiring new technical content.

---

## 4. One concrete recommendation from agentic LLM experience

**Use a lockfile or manifest for your AI sessions, the way dependency managers use lockfiles for software.**

In software development, a `package.json` specifies what you *want*; a `package-lock.json` records exactly what you *got* — specific versions, specific resolved dependencies, the exact state of the environment at build time. The distinction matters because "I wanted lodash ^4.0" and "I got lodash 4.17.21" are different pieces of information, and the second is what you need for reproducibility.

The paper's session logs do the equivalent of `package.json`: they document what was specified, what criteria were applied, what the researcher intended. What is missing is the equivalent of `package-lock.json`: a generated artefact, produced automatically at the end of each session, that records the actual model string used, the context window size at generation, the tool calls made and their results, and the sampling parameters in effect. In Claude Code, enough of this information is available to construct such a record automatically — the `.claude/` session state contains much of it.

The practical implementation does not require the researcher to become a developer. It requires one setup step: a short end-of-session script (five to ten lines of shell or Python) that reads the Claude Code session state and writes a structured summary — model version, session duration, files loaded, tools used — to a `session-manifest.json` in the logs directory. This file gets committed to git, which timestamps it. The researcher runs it at the end of each working session the same way they would commit their notes.

The benefit for the paper's argument is direct: it converts the session log from a researcher-authored narrative record into a combination of narrative record *plus* system-generated manifest, where the manifest provides the kind of environmental provenance that narrative records cannot. This is the closest thing available to the "context window state at generation time" that is otherwise unrecoverable — not perfect, but substantially better than nothing, and genuinely achievable without API expertise.

---

*End of review*
