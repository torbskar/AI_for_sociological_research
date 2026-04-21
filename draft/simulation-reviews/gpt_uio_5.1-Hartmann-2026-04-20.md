# Notes on “Systematic AI Use in Sociological Research”

*Professor David Hartmann – applied microeconomist’s comments*

## 1. Two arguments that need sharpening for economists

### 1.1 “Functional equivalence” to pre-registration / open science

The paper leans heavily on an analogy between systematic AI authorship and pre-registration / open science:

- Systematic AI use is described as “functionally analogous to pre-registration”: explicit criteria before running the AI, with logs and artefacts as a kind of design commitment <ref: index={3491948} firstWord={1} lastWord={70}/>.  
- Transparency artefacts (skill files, prompt templates, search scripts, logs) are said to constitute a replication package, the “open code and data” of AI use <ref: index={3491930} firstWord={60} lastWord={130}/>, and this is repeated when the folder structure and logs are presented as the “complete documentary record” of the research process <ref: index={3491952} firstWord={80} lastWord={170}/>.

From an economist’s standpoint, this analogy is doing too much work and needs sharper limits:

1. **Timing and publicity.**  
   Pre-registration in our world = public, timestamped, pre-outcome commitment. The paper acknowledges the disanalogy (protocol initially private; only optionally pre-registrable) and calls it “real but not fatal” <ref: index={3491948} firstWord={70} lastWord={160}/>. But the rhetoric still drifts back toward *equivalence in epistemic function*. I would separate more cleanly:
   
   - “Externalisation for my own discipline and memory,” versus  
   - “Public commitment that constrains ex post flexibility and is independently auditable as such.”
   
   The logs and git timestamps do give a **weak pre-registration-like property** (time-ordering) <ref: index={3491950} firstWord={1} lastWord={80}/>, but they are not equivalent to a pre-analysis plan on OSF.

2. **What is actually being pre-specified.**  
   In pre-analysis plans we usually pre-specify estimands, models, outcomes, key robustness checks. Here, what is specified are search strings, screening rubrics, skill configurations, reviewer criteria, and drafting styles <ref: index={3491932} firstWord={1} lastWord={90}/>, <ref: index={3491926} firstWord={1} lastWord={90}/>. That is much closer to *methods documentation* and *query design* than to pre-specification of hypotheses and estimands. It’s epistemically useful, but not the same object.

3. **Replication: process vs results.**  
   The paper equates the AI artefacts plus project structure with a replication package <ref: index={3491952} firstWord={1} lastWord={80}/>, <ref: index={3491930} firstWord={60} lastWord={130}/>. Yet it also notes that non-determinism means “AI-generated text will not be reproducible verbatim” and suggests focusing on similarity of “substantive points” instead <ref: index={3491935} firstWord={40} lastWord={120}/>.  
   In econometrics, we normally reserve “replicable” for something closer to *result reproducibility* (same numbers, up to tolerance), not just *pipeline reconstructability*.

To be credible to economists, I’d suggest:

- Explicitly distinguishing three things:
  1. **Process transparency** (we can see what was done);
  2. **Design commitment** (pre-specification that creates constraints);
  3. **Result reproducibility** (re-running yields essentially the same estimates/conclusions).
- Mapping systematic AI use primarily to (1), weakly to (2), and **not** to (3).  
- Softening the language from “functional analogue of pre-registration” to something like “inherits some pre-registration-like benefits (externalisation, time-ordering) without actually being pre-registration in the standard sense” <ref: index={3491948} firstWord={1} lastWord={90}/>, <ref: index={3491932} firstWord={90} lastWord={160}/>.

### 1.2 “Quality mechanism” and the use of Zeng et al.

The second place that feels overstated is the “quality mechanism” claim around Zeng et al. (2025):

- Zeng et al. find, in data-science tasks, that reproducibility-oriented prompting correlates with higher accuracy. The paper infers that *if* this generalises, systematic AI is “not merely a transparency mechanism but a quality mechanism” and suggests “no trade-off between reproducibility and quality” <ref: index={3491958} firstWord={1} lastWord={90}/>.  
- It then states that systematic AI authorship is “a necessary condition for the kind of quality control that makes errors detectable” <ref: index={3491958} firstWord={90} lastWord={170}/>.

You already acknowledge the limits:

- The finding is from data science, not sociology; tasks differ “in important ways from qualitative and interpretive research” and the quality claim for sociology is explicitly labelled an “open empirical question” <ref: index={3491958} firstWord={90} lastWord={180}/>.

But two points still look too strong for an economist:

1. **Domain transfer.**  
   Zeng’s setting has clear ground truth and well-specified tasks. The paper *assumes* that the cognitive discipline of explicit prompting generalises to literature synthesis and interpretive work, which is plausible but not shown. Right now it’s a hypothesis, not even a stylised fact.

2. **“Necessary condition” language.**  
   Claiming that systematic AI authorship is a *necessary* condition for error-detecting quality control sits awkwardly with the existence of high-quality, fully non-AI, code-and-data-documented research. A well-documented non-AI workflow with do-files and lab notebooks absolutely allows error detection; what your framework does is extend that logic to AI-assisted work and make some previously tacit choices explicit <ref: index={3491934} firstWord={60} lastWord={150}/>.

I would sharpen by:

- Downgrading from “necessary condition” to “sufficient (and highly desirable) condition for error-detectability in AI-assisted workflows, and often helpful even without AI” <ref: index={3491935} firstWord={120} lastWord={210}/>.  
- Separating clearly:
  - A **theoretical argument**: externalising criteria is a cognitive discipline that *should* improve quality on average;  
  - A **documented regularity** in one domain (Zeng);  
  - An **open empirical question** in sociology <ref: index={3491958} firstWord={1} lastWord={180}/>.  
- Being explicit about the counterfactual: what error-detection capabilities do the AI artefacts add over and above a traditional, well-kept lab notebook plus version control?

## 2. Caveat to add: what transparency artefacts guarantee vs merely document

You already say much of what’s needed, but I’d make one key caveat more explicit.

Current text:

- “Systematic use does not guarantee high quality or eliminate errors. Documentation can still be faked by dishonest researchers, just as before.” <ref: index={3491935} firstWord={1} lastWord={80}/>  
- Systematic use “makes errors more visible and correctable” but is “not a sufficient” condition for epistemic soundness; criteria can be “poorly theorised,” verification “superficial,” and configurations can encode bias <ref: index={3491935} firstWord={120} lastWord={220}/>.

What’s missing, especially for an economist, is a blunt statement that:

- **Documenting process does not verify correctness of outputs.**  
  It creates an *audit trail* but does not by itself validate the claims.

Concretely:

- The artefacts **guarantee** (if genuine):
  - A reconstructable record of what queries, criteria, and configurations were used;  
  - Time-ordering of decisions via logs and git commits <ref: index={3491950} firstWord={1} lastWord={80}/>.  
- They **do not guarantee**:
  - That search strategies were substantively adequate;  
  - That coding / screening rules were reasonable;  
  - That interpretations or causal arguments are correct.

Implications you could spell out in one short paragraph:

- The epistemic role of these artefacts is analogous to code and data: they enable *ex post* critique, reproduction, and sensitivity analysis, but they are **not** themselves evidence that the substantive conclusions are true <ref: index={3491932} firstWord={90} lastWord={170}/>.  
- Policies and norms should therefore treat them as **inputs to review and re-analysis**, not as warrant that “AI use is now safe.”

That explicit caveat would prevent misreading the framework as a certification of output quality rather than as an accountability mechanism.

## 3. Process documentation vs output verification

The paper mostly treats this distinction correctly, but implicitly.

Evidence you already provide:

- Systematic use “makes errors visible and correctable; unsystematic use does not” <ref: index={3491948} firstWord={150} lastWord={220}/>.  
- Non-determinism is acknowledged; outputs will not be textually reproducible, so you recommend logging outputs and prompt pairs and treating AI results as *inputs to human judgement* <ref: index={3491935} firstWord={40} lastWord={140}/>.  
- You explicitly distinguish:
  - Working logs and author-input files as first-tier, lab-notebook-like process documentation;  
  - Supplementary skill files, scripts, and logs as second-tier replication materials <ref: index={3491929} firstWord={40} lastWord={140}/>.

What’s missing for a hard-nosed reader is:

1. **A concise, explicit contrast.**  
   Something like a table or short subsection that says:
   
   - **Process transparency:** artefacts allow others to check whether criteria were set ex ante, whether logs are coherent with the narrative, and whether the described pipeline can be reconstructed (within stochastic limits) <ref: index={3491932} firstWord={90} lastWord={170}/>.  
   - **Output correctness:** still rests on substantive judgement about theory, identification, measurement, and interpretation; these cannot be mechanically guaranteed by the existence of a well-documented AI pipeline.

2. **Role of reviewers with these artefacts.**  
   You say reviewers can inspect criteria and logs to evaluate the systematic process <ref: index={3491955} firstWord={40} lastWord={150}/>, but it would help to make concrete:
   
   - Reviewers can re-run literature searches or syntheses with alternative criteria or prompts, analogous to robustness checks in regression <ref: index={3491950} firstWord={80} lastWord={170}/>.  
   - They can judge whether inclusion/exclusion criteria are substantively defensible and whether reviewer skills are appropriately adversarial, not merely present <ref: index={3491926} firstWord={80} lastWord={190}/>, <ref: index={3491934} firstWord={60} lastWord={150}/>.

Right now, the text makes it clear that process is documented, but it does not spell out *how far* that takes us toward verifying outputs, and what still depends on ordinary peer-review judgement. Making that boundary explicit would align the argument with existing practice in empirical economics.

## 4. What I would adopt in my own practice; productivity argument

### 4.1 Practices I’d adopt

Several parts of the workflow are readily transferable to applied micro and attractive:

1. **Project structure and context separation.**  
   The `project/` layout with `CLAUDE.md`, `.claudedocs/`, `.claudeignore`, git, and a clear data hierarchy is excellent:
   
   - Two-level configuration (global epistemic preferences in `.claudedocs/`, project-specific scope in `CLAUDE.md`) <ref: index={3491943} firstWord={1} lastWord={120}/>  
   - `.claudeignore` excluding `data/raw/`, credentials, and git metadata from AI context, giving a *structural guarantee* that raw data stay out of AI context <ref: index={3491943} firstWord={120} lastWord={210}/>  
   - Raw data as immutable transparency artefact, never modified, and excluded from both AI and version control <ref: index={3491931} firstWord={80} lastWord={170}/>, reinforced by the PreToolUse PII hook and three-zone model for personal data <ref: index={3491937} firstWord={120} lastWord={220}/>, <ref: index={3491933} firstWord={1} lastWord={110}/>.  
   
   This is exactly in line with how we already think about administrative data, and I would directly adopt this pattern.

2. **Author-input files and decision logs.**  
   The first-tier documentation — session logs plus first-person author-input files — is compelling:
   
   - Logs capture “decisions revised and refined along the way,” analogous to a lab notebook but richer, and author-input files record what the human actually contributed in each session <ref: index={3491929} firstWord={40} lastWord={140}/>, <ref: index={3491930} firstWord={1} lastWord={70}/>.  
   - Combined with git history, this yields contemporaneous, timestamped process evidence <ref: index={3491950} firstWord={1} lastWord={80}/>.
   
   For my own coding and drafting with AI, I’d adopt this: it turns my currently ad-hoc AI use into something auditable.

3. **Accessible, numbered scripts and intermediate outputs.**  
   For empirical work, the insistence on legible, sequentially numbered scripts with clear headers, comments, and saved intermediates is exactly what I’d want if I were relying on an AI to implement my code:
   
   - AI writes code to a human-authored specification; researcher remains responsible for the specification and for inspecting intermediates <ref: index={3491937} firstWord={40} lastWord={150}/>.  
   
   This is fully aligned with applied micro practice; the only novelty is taking AI seriously as a coding assistant while preserving verifiability.

4. **Structured drafting and reviewer skills.**  
   
   - Drafting skills: explicit style and structure criteria, with the intellectual contribution located in the skill and context, and drafts treated only as inputs to human revision <ref: index={3491926} firstWord={1} lastWord={80}/>.  
   - Reviewer skills configured to be adversarial, explicitly countering sycophancy <ref: index={3491926} firstWord={80} lastWord={190}/>.  
   
   I would use this as an internal pre-submission review tool, especially for checking coherence and catching gaps.

5. **Replication package that includes AI artefacts.**  
   Treating skill files, prompt templates, search scripts, screening logs, and AI-related configs as part of the replication package, alongside code and data, makes perfect sense <ref: index={3491930} firstWord={60} lastWord={140}/>, <ref: index={3491952} firstWord={1} lastWord={90}/>, <ref: index={3491933} firstWord={110} lastWord={200}/>.

Overall: I’m not resistant to the workflow; most of it I would happily adopt where I use AI.

### 4.2 Is the productivity argument adequately developed?

The **epistemic** and **policy** arguments are well developed; the productivity story is thinner.

You do note:

- AI makes extensive search and screening of large literatures inexpensive in researcher time, enabling more thorough and accountable non-systematic-review articles <ref: index={3491950} firstWord={80} lastWord={210}/>, <ref: index={3491944} firstWord={1} lastWord={90}/>.  
- Systematic AI use satisfies reproducibility checklists “as a byproduct of the workflow, not as an additional burden” <ref: index={3491932} firstWord={120} lastWord={210}/>.  
- Zeng et al. suggest no trade-off between reproducibility and output quality, which you tentatively connect to potential quality (and implicitly productivity) gains <ref: index={3491958} firstWord={1} lastWord={90}/>.

But relative to what an economist would expect, the productivity case is underdeveloped:

- No rough quantification of setup cost vs per-project savings (e.g., hours to configure skills and project structure vs time saved on literature triage, drafting, or robustness checks).  
- No explicit treatment of where the bottlenecks move: you implicitly assume that making criteria explicit and logging everything doesn’t meaningfully slow people down, which may or may not be true.  
- Zeng is used for a reliability/quality point, not to say anything about **throughput** (more tasks completed, more robustness checks run, broader literature coverage per unit of time).

What I’d add to satisfy a productivity-minded reader:

1. **A simple cost–benefit sketch.**  
   Even a qualitative model: fixed cost of adopting the workflow (learning, templates, initial skill set-up) versus marginal savings in standard tasks (screening 500 abstracts, drafting first-pass sections, iterating robustness checks). Back-of-the-envelope numbers from your own experience would be welcome.

2. **Identification of main gains.**  
   Spell out explicitly where you expect the big payoffs:
   
   - Literature search and synthesis, given your grounded-notebook approach <ref: index={3491944} firstWord={1} lastWord={110}/>;  
   - Drafting and stylistic consistency <ref: index={3491926} firstWord={1} lastWord={80}/>;  
   - Possibly documentation itself: replication package and authorship evidence produced “for free” once the system is in place <ref: index={3491929} firstWord={40} lastWord={140}/>, <ref: index={3491952} firstWord={1} lastWord={90}/>.

3. **Acknowledge potential overhead.**  
   Explicitly recognise that for small or one-off projects, the overhead may dominate the benefits, and that the system shines when researchers do many projects or handle large literatures. That would make the recommendation more credible.

At present, I’m convinced this is a **transparency and accountability upgrade** and plausibly a **quality discipline**; I’m inclined to think it’s a productivity win for heavy users of AI, but the paper doesn’t really make that case analytically. Adding even a modest, economist-style cost–benefit narrative would strengthen the appeal substantially.
