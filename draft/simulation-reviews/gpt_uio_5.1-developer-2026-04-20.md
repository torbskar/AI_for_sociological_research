# Technical feedback on the systematic AI workflow

## 1. Two weakest points against professional LLM-pipeline standards

From a software / LLM-systems perspective, the paper’s *conceptual* design is strong, but two implementation gaps would be serious weaknesses in a professional pipeline:

### 1.1. Model specification and configuration are under-defined and not treated as “first-class” artefacts

Throughout, the workflow talks about “using Claude” with project context, skills, and logs, but never treats the **model and its runtime configuration as a tracked dependency** in the same way code and data are tracked.

Concretely:

- **Model identity and versioning**  
  
  - “Claude” is described generically. In practice, different Claude models (and version updates of the same model) behave meaningfully differently.  
  - There is no requirement that each session, or each “production” run, logs:
    - exact model name (e.g. `claude-3.5-sonnet-2025-02-15` vs `claude-3-haiku-2025-01-10`)
    - provider-side model version changes over time.
  - In a real pipeline, this is analogous to not recording which R or Stata version you used.

- **Sampling settings omitted**  
  
  - Temperature, `top_p`, `top_k`, max tokens, and any nucleus-sampling / beam-search settings are not treated as configurable parameters or artefacts.
  - The paper notes non-determinism (§5.4) but does not propose a standard for:
    - which settings to use in “serious” runs,
    - how to distinguish “exploratory high-temperature” sessions from “low-variance” sessions for materials that end up in the paper.

- **Chat vs API / IDE modes blurred**  
  
  - The workflow is clearly written around an IDE/“Claude Code” style integration, but many researchers will use:
    - browser chat,
    - notebook-style grounded tools,
    - or direct API calls.
  - These modes often have different defaults and limits. Because the workflow doesn’t insist on logging *how* the model was accessed (chat vs IDE vs API) and with which settings, another researcher cannot reliably reproduce behaviour even if they use “Claude” on the same project files.

From an engineering standpoint, this is the single biggest reproducibility gap. You treat prompts, skills, and file structure as versioned artefacts (good), but treat the model itself as an opaque, stable tool (which it is not). In production systems, we routinely:

- pin the model and provider,
- pin or at least log all sampling parameters,
- and treat these as part of the “experiment configuration”.

Your workflow could be substantially strengthened by explicitly treating “model + configuration” as part of the replication package, on par with scripts and search strings.

---

### 1.2. Context-window and session-state management are not specified precisely enough

The paper does an excellent job of emphasising **project-level context** (`CLAUDE.md`, `.claudeignore`, `.claudedocs/`) and **session logs**, but it stops short of the level of precision you’d expect in a robust LLM pipeline about **what was actually in the context window at the time an output was generated**.

Two specific weaknesses:

- **No practical scheme to reconstruct the context window for a given “production” output**
  In tools like Claude Code or chat UIs, the effective context at generation time typically consists of:
  
  1. Global/system instructions,
  2. Project-level context files (like `CLAUDE.md`),
  3. Any loaded skill or role configuration,
  4. The visible conversation history up to that point,
  5. Any inlined files or retrieved snippets the tool auto-includes.
  
  The paper logs prompts and outputs, and describes the presence of context files, but does not describe any procedure to:
  
  - snapshot which files were actually pulled into the context window,
  - capture which skills (and which *version* of each skill) were active at the time,
  - differentiate exploratory conversational history from the “minimal prompt” needed to drive a specific result.
  
  In practice, this means that a future researcher can see the *inputs* (files, skills, prompts) and the *outputs*, but cannot reliably reconstruct the **exact call** that produced the output.

- **No versioning strategy for skills / configurations over time**
  You describe evolving skills and reviewer configurations but do not propose:
  
  - semantic versioning for skills (e.g. `reviewer_skill_v1.1`),
  - a mapping from each important output to the skill version used,
  - or a change log for key configuration files.
  
  In software terms, skills and `CLAUDE.md` are “configuration-as-code”. Without explicit versioning and an easy way to link an output to the configuration version, the system is closer to “configuration-as-a-moving-target”, which is precisely what you’re trying to avoid.

So the second weak point is not *conceptual* — you have the right building blocks — but **operational**: there is no concrete, reproducible way to say “here is the exact context state and configuration used when generating this artefact”. That’s the bar professional LLM pipelines aim for.

---

## 2. Are the transparency artefacts sufficient to reconstruct the workflow?

If I put on a developer hat and asked: “Can I re-run this project and get broadly comparable outputs?”, the answer is: **not yet**, though you are closer than most academic setups.

What you’re providing / planning to provide:

- Project structure and key configuration files (`CLAUDE.md`, `.claudedocs/`, `.claudeignore`).
- Skill files for drafting and reviewing.
- Search scripts, boolean queries, screening rubrics.
- Session logs (prompts + outputs).
- Git history for files and logs.

These are genuinely valuable, and in a lot of social science work they’d already be “above average”. The remaining blockers for a developer trying to reproduce the workflow:

### 2.1. Missing infrastructure metadata

To rebuild the environment, we would also need:

- **Exact model and provider** for each substantive step.
- **Exact sampling configuration** for those steps:
  - temperature,
  - `top_p` / `top_k`,
  - max output tokens,
  - any special decoding settings (e.g. “JSON mode”, max latency, etc.).
- **Interface/mode**:
  - whether each step was run in:
    - chat UI,
    - local IDE integration,
    - or direct API call with a given wrapper/library.
- **Tool version information**:
  - version of the IDE integration or local assistant,
  - any local pre- or post-processing scripts (e.g. the PII hook).

Without that, I can approximate your workflow, but I cannot be confident that differences in output are due to methodological choices rather than to “I accidentally used a different model variant at a higher temperature”.

A lightweight solution that wouldn’t require you to become a developer: a simple “run log” CSV/markdown table where, for each *important* AI-assisted step, you record:

- date,
- task (e.g. “screen first 200 abstracts”),
- entry point (chat / IDE / grounded notebook),
- model name,
- temperature and `top_p`,
- skill configuration file and version.

This is the kind of thing a developer would often wire up automatically; a researcher can do it manually with modest overhead.

---

### 2.2. Context state and file snapshot gaps

For replication, you’d also want:

- A clear statement of **how to export logs** from whatever interface you’re using (e.g. “download conversation transcript as JSON”) and how those logs are linked to project files and git commits.

- A simple convention like:
  
  - “When an AI interaction contributes text or decisions that end up in the paper, we:
    1. Move the relevant exchange and its output into a dedicated `logs/production/` file,
    2. Note which files were open/visible or referenced,
    3. Commit that log and the skill/config versions together.”

- For grounded / retrieval-augmented use (e.g. grounded literature synthesis), a way to reconstruct **the exact source set**:
  
  - which PDFs or notes were loaded into the tool,
  - which filters or collections applied at the time of the query.

You already keep search logs and “source sets”, but for a developer to reproduce a grounded run, they’d want an index: “this synthesis prompt was run on these N documents (or this folder / corpus snapshot)”.

---

### 2.3. Non-determinism and lack of “frozen runs”

You do acknowledge that verbatim reproduction is impossible, but you don’t define any protocol that tells a future user:

- which runs are considered **authoritative** (as in: these outputs were taken seriously enough to feed into the paper),
- and how those runs should be “frozen”:
  - e.g. low temperature,
  - shorter context window,
  - minimal prompt history.

Professionally, we often distinguish:

- **Exploratory runs** (high temperature, chatty context, ad hoc prompts),
- **Evaluation / production runs** (fixed prompts, low temperature, minimal context, logged as “experiments”).

Your workflow recognises the conceptual distinction (exploration vs systematic use) but not yet the *operational* step where a researcher says: “this interaction is now part of the paper, so I re-ran it under controlled conditions and saved that run”. Without that, replication is more art than science.

---

## 3. Where the approach aligns well with professional practice, and how to make that clearer

There are several areas where your workflow is very close to “best practice” from an LLM/pipeline perspective:

### 3.1. Configuration-as-code and environment separation

- **Project root with a dedicated configuration file (`CLAUDE.md`)**  
  This is exactly what developers mean by configuration-as-code: the environment the model operates in is expressed in plain text, in the repo, under version control.

- **Two-level configuration (global `.claudedocs/` + project `CLAUDE.md`)**  
  This maps very neatly onto common patterns:
  
  - global defaults (“my general stance on hedging, epistemology, etc.”),
  - project overrides (scope, research question, specific definitions).

- **`.claudeignore` vs `.gitignore` vs `data/` hierarchy**  
  This is basically:
  
  - data governance and PII safety baked into the file layout,
  - AI-context boundaries treated as first-class constraints.

In developer terms, you are using a simplified version of the patterns used in serious ML production: environment segregation, clear data tiers, and configuration files in source control.

You could make this resemblance explicit for social science readers with language like:

- “We treat these configuration files like analysis scripts: they live in the project directory, are versioned with the rest of the materials, and changes to them are part of what a replication package exposes.”

No need to say “configuration-as-code” if that feels too technical; describing them as “scripts for how we talk to the AI” already conveys the point.

---

### 3.2. Strong data-governance and access-control design

Your separation of:

- `data/raw/` (immutable, never AI-readable, excluded by `.claudeignore`),
- `data/interim/` and `data/processed/` (increasingly safe for AI-assisted coding),

plus the pre-tool hook for PII detection, is very close to what you’d see in a well-run data engineering setup.

For reproducibility and policy arguments, you might emphasise that:

- This is not just “we promise not to show the AI raw data” but:
  - implemented as a **structural constraint** (folder layout + ignore rules + pre-flight checks),
  - auditable by looking at the replication package and seeing that the raw folder is ignored and the hook is in place.

That helps reviewers see that they’re not relying on researcher self-restraint, but on verifiable guardrails.

---

### 3.3. Adversarial reviewer configuration and explicit error-mitigation

The “adversarial” reviewer skill that encodes:

- “be critical”,
- “raise objections”,
- “avoid sycophancy”,

and bakes that into a reusable configuration rather than one-off prompts, is exactly the sort of “guardrail configuration” we would introduce in commercial settings to manage known failure modes.

A suggestion for making this connection clearer without jargon:

- Spell out that these reviewer skills are:
  - **re-usable checklists** the AI follows,
  - targeted at specific known weaknesses of LLMs (over-agreement, over-generalisation),
  - and that they can be inspected and criticised as part of peer review.

That maps neatly to existing ideas in social science about checklists and coding rubrics, just applied to AI behaviour.

---

### 3.4. Two-tier documentation (working logs vs clean supplement)

The distinction between:

- working logs (lab-notebook analogue),
- and clean supplementary materials,

is very close to how professional ML teams treat:

- experiment tracking metadata,
- vs published experiment summaries.

It’s worth highlighting that you’re not asking reviewers to wade through raw logs, but you’re preserving them as an audit trail. That matches good engineering practice and supports your argument that accountability is structured, not just asserted.

---

## 4. One concrete recommendation that fits your workflow

A practical addition, drawn directly from agentic LLM workflows, that you could adopt *without* turning researchers into developers is:

### Introduce “protocolised runs” for key AI-assisted steps

The idea is to distinguish formally between:

- **Exploratory use** (brainstorming, trying out rubrics, drafting in a messy way),
- and **protocolised runs** (a controlled, logged interaction that is part of the scientific record).

You already make this distinction conceptually; the missing step is a simple, repeatable practice to operationalise it.

A minimal version researchers could implement with their existing tools:

1. **When a prompt/configuration becomes important, freeze it into a “protocol sheet”**
   
   - Create a simple markdown or spreadsheet entry with columns like:
     
     - date,
     - task (“screen 500 abstracts”, “generate initial literature synthesis for Section 2.1”),
     - file(s) involved (e.g. `literature/ai_policy.bib`, `notes/outline_v2.md`),
     - skill or system configuration file and its version label,
     - intended model (name),
     - intended temperature and `top_p`.
   
   - Copy the exact prompt(s) you intend to use into this record.

2. **Re-run the interaction in a “clean” session**
   
   - Start a fresh session (no cluttered prior conversation),
   - load only the relevant project context and skills,
   - apply the recorded settings (model, temperature),
   - run the prompt(s) from the protocol sheet,
   - save the full exchange (prompt + output) as a separate log file under `logs/production/`.

3. **Commit protocol + log together**
   
   - Commit the protocol entry, the skill/configuration file (if changed), and the production log in a single git commit,
   - option­ally tag that commit (e.g. `v3_lit_synthesis_protocol1`).

From a researcher’s point of view, this is just:

- “When I decide a particular interaction matters, I:
  - write down exactly what I’m asking and how,
  - re-run it once under clean conditions,
  - and put that run and its settings into the replication materials.”

From a developer’s perspective, this gives you something very close to an **experiment run record**. It doesn’t eliminate non-determinism, but it:

- fixes the prompt,
- fixes the configuration,
- keeps the context small and inspectable,
- and creates a clear link in your repo between “this run” and “this part of the paper”.

It aligns perfectly with your existing emphasis on query authorship and systematic vs unsystematic use, and it’s implementable with nothing more than your current tools plus a little discipline.

---

In summary, your workflow is unusually close to professional practice for an academic setup. The main things missing are:

- explicitly treating **model choice and sampling configuration** as documented dependencies, and
- adding a lightweight procedure for **protocolised, reproducible runs** with clearly logged context state.

Both could be added with minimal technical overhead but would materially strengthen your claims about reproducibility and control.


