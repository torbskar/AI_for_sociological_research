# Outline: Systematic AI Authorship in Sociological Research

**Status**: Working outline — updated 2026-04-21  
**Last updated**: 2026-04-21  
**Target**: Sociological Science — methodological contribution

---

## Core argument (one sentence)

The epistemically relevant distinction is not between AI use and non-use but between *systematic* and *unsystematic* AI authorship, and a documentation-based framework that recognises this distinction is more epistemically honest and more consistent with existing open-science infrastructure than current journal policy.

---

## Note on durability

The argument must be tool-agnostic throughout. The structured/unstructured distinction and the query authorship concept are durable; specific tool names (Claude, NotebookLM, ChatGPT) are illustrative and will date. I might have to specify that agentic models have the edge for how to implement such structure in practice, as purely chat-based approaches are more limited. This is both a rhetorical and a substantive point: the paper argues for a principle, not a specific platform. Nevertheless, I am using Claude Code, and some parts of the structure is platform dependent, so some references to tool names will be included. I assume e.g. Codex have similar functionality, and future agentic models probably will as well. 

---

## 1. Introduction

**Function**: Establish the problem; state the paper's move; no long literature review. Open with the problem, not the tool. The reader must feel that something is already going wrong before the paper's contribution is introduced.

**Opening — problem statement, not enthusiasm for a new tool:**

- Two things are simultaneously true: there are serious and documented worries about AI-assisted fraud, papermills, and bullshit production from uncritical AI use; and AI tools are so embedded and accessible that it is naive to think researchers will not use them. The question is not whether but how the field governs this.
- The papermill problem is not speculative. The Hindawi/Wiley retraction of 8,000+ papers (2022–23) is the watershed: the moment the scholarly-publishing industry publicly acknowledged that AI-scale fraud had overwhelmed traditional editorial safeguards. This is the concrete problem a documentation-based policy is designed to address. Use Hindawi as the reference anchor — it gives the stakes a specific, citeable event.
- Unstructured AI use multiplies undocumented decision points — the slippery slope (language editing → rewriting → generating → inferring with authorship attribution) is continuous and real. Everyone in the field is struggling with where it remains acceptable. This connects directly to the forking-paths problem: unstructured AI use is an unmarked proliferation of researcher degrees of freedom.
- AI makes shallow thinking look good. Sycophancy tendencies reinforce the author's existing perceptions; fluent output disguises thin reasoning. This is an epistemic hazard distinct from outright fraud — and distinct from the reliability problem (§3.1, §4.5). Introduce it here as part of the problem; the mechanism argument follows later.
- Automated research systems (e.g. APE, socialcatalystlab.org) are emerging — interesting evidence of AI capabilities, but also gigantic fishing expeditions: p-hacking at scale. Unstructured automation at scale is exactly the wrong direction; structured, documented use is the right one.

**Why the current response fails — two independent grounds:**

- The dominant guardrail is declaration: journals require disclosure, publishers ask for attestations of AI use. This treats disclosure as sufficient. It is not — on two independent grounds.
- *Scale failure*: Hindawi-style papermill operations produce plausible disclosures at volume. Declaration-based policy offers no resistance at scale. "De-AI" services — authors paying to strip AI signatures from text to evade detection — demonstrate the perverse consequence: enforcement-based disclosure policy drives research underground rather than making it transparent. Documentation policy cannot be evaded in the same way, because its artefacts are generated during the work, not as post-hoc statements about it.
- *Mechanism failure*: The behavioural-science case that requiring a declaration produces compliant behaviour has its flagship empirical demonstration retracted. Shu, Mazar, Gino, and Ariely (PNAS 2012) — that signing an honesty pledge at the top of a form increases honest reporting — was retracted in 2021 after Data Colada identified apparent fraud in a co-authored study; two further Gino papers were retracted in 2023 (O'Grady 2023). The Gino case is the sharpest available illustration of what the paper is arguing in miniature: the appearance of compliance through a declaration, while the actual work remains uninspected. Use this in one paragraph immediately after Hindawi — not as "behavioural economics is bunk" but as a precise, calibrated point: the specific mechanism on which declaration-based AI policy rests has lost its most-cited empirical demonstration. State once, cite O'Grady, move on.
- [Concessive move]: Journals responded rapidly and in good faith. Binary disclosure requirements were a reasonable first response in conditions of uncertainty. The paper's critique is of the instrument, not the intent.

**The paper's move:**

- The binary (AI use / no AI use) misidentifies the epistemically relevant dimension. What matters is not whether AI was used but whether it was used *systematically* — embedded in explicit criteria, human verification at each stage, documented outputs. This is where the real leverage lies.
- Hallucinated citations as misconduct (Accountability in Research): citations function as data in social science disciplines, so AI-induced citation errors are direct contamination of the evidential record, not a nuisance. Supports the argument that the literature-search and screening stages are where structured use matters most; grounds the stakes for the sociological reader.
- "Authorship is accountability, not just participation" is already being used in the field (Scholarly Kitchen / Chronicle). The paper is not introducing this principle; it is specifying what it requires in practice — what artefacts, produced how, make the accountability claim substantive rather than nominal. The "Humanity Test" (can the author defend every claim, trace every source, explain every nuance without AI help?) is the criterion; the paper's contribution is that documented workflow artefacts provide the structural conditions under which the test can be substantively passed.
- The field is already drifting toward tiered, task-specific disclosure frameworks. The paper's contribution is to specify *which axis* the tiering should be organised along — not task type (writing vs. analysis vs. search) but process structure (systematic vs. unsystematic).
- This paper: (1) develops the distinction between systematic and unsystematic AI authorship; (2) introduces the concept of *query authorship* — the intellectual contribution embedded in well-formed queries, configurations, and workflow design; (3) describes a systematic workflow for sociology across the full research pipeline; (4) argues that systematic AI authorship instantiates the epistemic properties of open-science practices; (5) draws implications for journal policy.
- The systematic approach is a spectrum — degrees of systematic. How to implement it is up to the author and their theoretical, methodological, and epistemic commitments. The unsystematic approach is *off* this spectrum, not at one end of it.
- Frame: methodological contribution. The paper demonstrates a workflow and argues for its epistemic properties — it is not a think-piece. The specific workflow and folder structure described are an example; others should adopt something analogous.
- **Self-demonstration, honestly stated**: this paper's own composition sits on the spectrum it describes — systematic in infrastructure (session logs, author-input files, reviewer skills, a documented literature search pipeline) and more hermeneutic in argument development. The systematic elements did genuine epistemic work; the conceptual moves developed during the writing not only from a pre-specified plan. A fuller treatment follows in §5.4. This acknowledgement is part of the argument: the framework's value is not contingent on pre-registered rigidity.

**Scope limitation** (stated here, not batched): The workflow described is for text-heavy, literature-based, and quantitative, qualitative, and mixed social science research. Systematic reviews have their own established guidance; what is described here is appropriate for standard journal articles. Empirical data (both quantitative and qualitative) data collection and GDPR considerations require additional safeguards addressed in the supplementary materials. The argument is scoped to sociology and adjacent social sciences.

---

## 2. AI in research: the existing literature and the gap

**Function**: Brief literature grounding — not a survey. Maps what exists, names the gap, and positions the paper's contribution. Keep short; Sociological Science discourages long literature reviews.

**Note**: The literature in this section was identified using the systematic pipeline described in §4. The search strings, screening decisions, and relevance scores are documented in the supplementary materials. No self-referential commentary on this in the text — the documentation itself serves as the demonstration.

### 2.1 What the existing literature covers

- Rapid AI adoption in research is well-documented and cross-disciplinary — Grossmann et al. (2023, *Science*), Korinek (2023, NBER), Feuerriegel et al. (2023): social science, economics, information systems all engaged early. The question is no longer whether but how.
- The dominant institutional response has been **reporting checklists**: post-hoc disclosure instruments telling authors what to report after the research is done. Numerous variants — PRISMA-trAIce (Holst et al., 2025, systematic reviews), TITAN (Agha et al., 2025, general purpose), TRIPOD-LLM, CONSORT-AI, MI-CLAIM-GEN, and others. Zrubka et al. (2025) systematically reviewed 24 such checklists: item counts range from 10 to 66, indicating no consensus even on what "full disclosure" means.
- Publisher and journal guidance follows the same logic: Mondal et al. (2024) audited 20 major publishers; Ganjavi et al. (2024) and Goyanes (2025) map journal-level author guidelines. Six themes recur across all audits — all centred on disclosure and attribution, none on the epistemic structure of the process.
- **Social science pipeline work** exists but is partial: Törnberg (2024) on text annotation best practices and prompt stability; Davidson & Karell (2025, *SMR*) on integrating generative AI into social science research (measurement, prompting, simulation); Blanchard et al. (2025, *Journal of Marketing*) — the most complete pipeline found, with reproducible templates and pre-registration materials. Lin (2025) for psychology; DataDreamer (Patel et al., 2024) and Zeng et al. (2025, AIRepr) from NLP/data science.

### 2.2 The gap

- The checklist literature addresses accountability after the fact. It implicitly assumes the research process is already sound — it has nothing to say about whether it was. A researcher could complete every item on PRISMA-trAIce while having used AI in a wholly unstructured, unverifiable way.
- No existing framework treats the **structured/unstructured distinction** as the fundamental policy-relevant axis.
- No sociology-specific workflow framework exists. Davidson & Karell (2025) is the closest — but it is a special-issue framing piece, not a workflow guide. Blanchard et al. is the most practical pipeline, but in marketing.
- No existing work treats AI tool configuration (skill files, configured reviewer roles, system-level prompts) as an epistemic mechanism comparable to pre-registration or researcher-degrees-of-freedom disclosure.
- No existing work discusses transparency artefacts (prompt templates, search logs, skill configurations) as components of a replication package.
- **Summary**: The field has checklists in abundance and structured process thinking almost nowhere. The most actionable pipeline works are in clinical research and ML/NLP. Social science equivalents are partial. Sociology-specific work is absent.

---

## 3. Systematic and unsystematic AI authorship

**Function**: The paper's conceptual contribution. Must be crisp — not a literature review. Primary terms: *systematic AI authorship* (the overarching concept) and *unsystematic AI authorship* (the contrast). "Structured/unstructured" survives as a description of practice but is not the primary frame.

### 3.1 What unsystematic AI use looks like

- Prompting without explicit criteria; accepting outputs without systematic verification; no documentation of process
- The problem is not that AI is unreliable but that without explicit criteria, errors are invisible and unrepeatable
- Ludwig, Mullainathan & Rambachan (2024): "seemingly innocuous choices (which model, which prompt) can produce dramatically different parameter estimates" — unstructured use makes this variance invisible
- Barrie et al.: "the observed variance in performance is often unacceptably high" even with temperature control — without logging, you cannot know whether your results would survive re-running
- Cheng et al. (2026, *Science*): sycophantic AI responses reduce independent judgment and promote dependence. The failure mode is directional — AI outputs tend to confirm rather than challenge user priors — but it is more than a reliability problem. A model that softens its critique to the researcher's expectations does not only produce biased outputs; it **insulates the researcher's thinking**. Unstructured use therefore exposes the researcher to a cognitive threat, not merely a data-quality threat. [First appearance; cognitive-threat framing returns in §4.5 as the motivation for adversarial configuration and fresh-session design.]

### 3.2 What systematic AI use looks like

- Tool configurations with explicit criteria built in (reviewer skills with discipline-specific standards)
- Human verification checkpoints at each stage — verification is part of the protocol, not an afterthought
- Documented outputs: prompt templates, skill configurations, search logs, screening decisions
- *Query authorship*: Configuration of the project and its structure. This includes literature search/review where formulating a search string, screening rubric, or review prompt is an intellectual act — it encodes theoretical choices, scope commitments, and evaluation standards. These choices belong to the researcher, not the AI. Systematic use makes them explicit and verifiable; unstructured use leaves them tacit and unauditable. [First appearance — see §5.1 for full development]
- Analogy to pre-registration: structured use forces explicit articulation of tacit decisions *before* results are known — which search terms? which inclusion criteria? which coding rules? what theoretical framwork? and so on. 

### 3.3 Why the distinction matters

- Epistemically: systematic use makes errors visible and correctable; unsystematic use does not
- Zeng et al. (2025, AIRepr): systematic prompting designed for reproducibility *also produces better results* — not just more transparent ones. This is not a trade-off. [Note: this finding comes from data science tasks; the claim for sociology is suggestive, not demonstrated — hedge accordingly in §5.3]
- The existing literature has converged on reporting checklists (PRISMA-trAIce, TITAN, TRIPOD-LLM, etc.) — instruments for disclosing AI use after the fact. These assume the underlying process was sound. Systematic use addresses the prior question: building soundness in. [Concessive: checklists are valuable; they are just insufficient.]
- The systematic/unsystematic axis is orthogonal to the use/non-use axis. A paper using AI in a systematic way may be more epistemically sound than one not using AI at all but relying on undocumented, unverifiable manual judgements.
- The query authorship concept travels beyond the immediate AI context: it connects to existing debates about transparency in qualitative research (what counts as a decision? who made it?) and to the open-science argument for researcher degrees of freedom disclosure.

### 3.4 Systematic use as a spectrum, not a binary

- The systematic/unsystematic axis is a **spectrum**, not a categorical split. The framework defines the features of the systematic end — explicit criteria, configured tools, documented verification, retained artefacts — without implying that partial compliance is without value. A researcher who documents some stages and not others is in a better epistemic position than one who documents none. The framework is a direction, not a bright line.
- The spectrum runs from **informal discipline** at one end (explicit criteria, retained configurations, session logs, but without pre-specification of outcomes) to **full formal pre-registration** at the other (project setup, skill files, search protocols, and CLAUDE.md registered with a trusted third party — OSF or equivalent — before outcomes are generated). The framework is compatible with both ends: the same infrastructure supports an exploratory, hermeneutic project and a pre-registered one; the difference is how much is fixed in advance.
- This gradient handles two otherwise-opposed critiques. The economist-style critic who wants binding constraints can pre-register the full setup. The theoretically-oriented critic who resists foreclosing inquiry retains the exploratory use of the same infrastructure. Neither has to choose between "rigour" and "hermeneutic openness"; they choose where on the spectrum to sit.
- **Unsystematic use is off the spectrum, not at one end of it.** The absence of explicit criteria and documentation is not a minimal version of systematic use; it is categorically different, because errors cannot be detected and choices cannot be attributed. This preserves the normative bite of the distinction while granting the gradient within systematic use.
- Cross-reference forward to §5.1 for the pre-registration analogy reframing.

---

## 4. A systematic workflow for sociology

**Function**: Shows what systematic AI authorship looks like in practice across the research pipeline. Descriptive — this is how it works, not why it is better (that comes in §5). Frame as a general workflow, not as a description of what this paper did. Details go to supplementary materials; text stays at the level of principle. No self-referential commentary.

### 4.1 Overview of the workflow

- Five stages: literature search with screning and synthesis → empirical data and analysis (both with AI and manually) → drafting (both with AI and manually) → review (both with AI and humans) → documentation.
- At each stage: explicit input criteria, configured AI tool, human verification checkpoint, documented output
- Transparency artefacts produced at each stage: boolean search strings, screening rubrics, skill configurations, prompt templates, search logs, NotebookLM source sets, analysis scripts and outputs, codebooks, review records
- Each stage can have their own level of systematic approach, their own configuration files etc. 
- [Scope note here, briefly]: This is not an automated pipeline that delegates decisions to agents. Xu & Yang (2026) demonstrate that type — effective for scaling well-defined computational tasks. The workflow here keeps the researcher in the loop at every stage; AI handles execution within explicitly defined criteria, the researcher handles judgement. The distinction matters for sociology, where research questions, theoretical framings, and interpretive moves cannot be delegated.

### 4.2 Literature search and screening

**Function**: Describe the principle of systematic literature searching using AI tools. Frame as one possible approach, but a more standard approach is possible or combined with other tools as well. Frame as a general workflow applicable to standard journal articles — not a systematic review, not self-referential description of this paper's own search. Scope note: systematic reviews have their own established protocols (PRISMA etc.) and this section does not replace them. Details go to supplementary materials.

**Key principle**: AI makes extensive search and screening of large literature cheap in terms of time (though it costs tokens). This should be presented as one component of a search strategy, supplemented by standard database searches and semantic searches (e.g. Elicit). The researcher's intellectual contribution is in specifying the search criteria, inclusion/exclusion logic, and synthesis questions — the execution is delegated.

- Boolean search strategy with explicit inclusion/exclusion criteria documented in advance — analogous to a systematic review protocol but applied at the scale of a standard article literature review
- Open database API (e.g. OpenAlex) searched via script — reproducible, logged, shareable. Licensing note: bulk export from subscription databases (Scopus, Web of Science) may not be permitted under institutional agreements; open APIs with explicit research-use permission avoid this issue. [One sentence — signals awareness; not a detailed discussion]
- Standard searches and semantic searches (e.g. Elicit) as complements — catches papers keyword search misses; covers preprints and working papers
- Candidate screening via configured keyword-based rubric with explicit criteria
- Full-text relevance scoring across themes — algorithmic, auditable
- Source synthesis via grounded AI tool (queries submitted to notebooks containing only the relevant PDFs) — contrast with general-purpose chatbot (unverifiable, no source accountability); query formulation is itself query authorship
- Human verification at each stage: top-scored papers read independently; synthesis outputs cross-checked against sources
- All outputs documented in supplementary materials (search strings, screening decisions, relevance scores, synthesis queries)

### 4.3 Empirical data and analysis

**Function**: Describes the governing principle and workflow for empirical projects with primary data. Scope: explicitly for quantitative and qualitative work with primary data; the paper's own production is literature-based and this section is anticipatory guidance rather than demonstrated practice. I may be mentioned that this article is not empirical and thus do not contain artifacts and workflows that cover this  section, so only the principle is discussed. 

**Key principle**: Strict separation — the AI operates on the research context and on analysis scripts, not on the data itself.

- Data folder hierarchy: Cookiecutter standard (`data/raw/` → `data/interim/` → `data/processed/` → `data/external/`); `data/raw/` is immutable — original data is a transparency artefact, never modified after receipt; enforced via `CLAUDE.md` rule and `.claudeignore`
- AI-assisted analysis scripts: numbered sequentially (`01_import.R`, `02_clean.R`, etc.), with plain-language comments; researcher authors the specification (variable definitions, analytical strategy, edge-case rules); AI implements; legibility is a design requirement so the researcher can verify the specification was correctly implemented
- GDPR/PII: `PreToolUse` hook runs a local PII scanner (Microsoft Presidio or custom Norwegian-identifier regex) before any file read operation — structural guarantee that raw personal data cannot be sent to the API; three-zone model: raw (never to API) / pseudonymised (AI-assisted cleaning) / anonymised (unrestricted use)
- Human verification: intermediate outputs saved after each major transformation step; researcher inspects data at each stage without re-running the full pipeline
- Transparency artefacts: analysis scripts, codebooks, data management protocols, PII hook configuration
- For projects with personal data: systematic AI authorship is not merely epistemically preferable — it is the legally required approach under GDPR

### 4.4 Drafting

- Skill-configured AI persona (skardhamar-style) with explicit style criteria — forces articulation of what the target voice is, not just "make it sound like me"
- Drafts are inputs to human revision, not outputs for direct use
- All prompts and skill configurations retained as artefacts
- **Writing-as-thinking caveat**: the relocation claim — AI handles execution within explicitly defined criteria, the researcher handles judgement — is strongest for search, screening, and analytical tasks where the specification can genuinely precede the execution. It is **most contested for drafting**, where some arguments are formed through the act of composition rather than expressed from prior specification. Researchers for whom the text partly constitutes the argument should treat drafting as the stage where the framework's assumptions most often require individual adjustment: more iterative use of the AI as a sparring partner, less delegation of whole passages, and more willingness to treat a draft as a thinking-tool rather than a candidate output. The systematic infrastructure — session logs, reviewer skills, author-input files — still supports hermeneutic drafting; it does not replace it. This is an honest acknowledgement, not a concession: the spectrum argument in §3.4 predicts exactly this sort of stage-specific variation in how pre-specifiable the work is.
- After initial draft, one moves to the reviewer phase described in §4.5, and we start with what is currently described as component 2. The review provides a list of things to be fixed, and a decision is made by the author. There might be manual adjustments to the draft as well, and perhaps changes to the outline, or there might be need to check additional literature or digg into some new perspective. Revise and then repeat the review and revision. Repeat if necessary. When reasonabley satisified, move to colleague review (component 1) and make new revision. Repeat component 2 if necessary. Then move on to component 3, and revise again. 

### 4.5 Review and adversarial configuration

The review stage has three components. They are cumulative — each addresses a failure mode the previous one does not.

**Component 1 — Colleague review (primary).** The manuscript is sent to colleagues for external human expert feedback. This is the baseline and primary external check; AI-assisted review is supplementary to it, not a substitute. The paper must say this explicitly — both to be accurate about the workflow and to avoid the impression that AI review replaces human review. What structured AI review provides is a well-prepared manuscript *before* it reaches human reviewers: weaknesses that would appear in referee reports are identified and addressed earlier, and the author arrives at the colleague-review stage with a more defensible draft.

**Component 2 — Structured reviewer skill in a fresh session.**

- Discipline-specific reviewer skills (social science article reviewer, logic-language reviewer, qualitative theory reviewer)
- Each skill has explicit review criteria built in — not "does this seem good?" but "does this meet these specific standards?"
- Structured review produces legible, actionable feedback — not a vague sense of quality
- **Fresh-session requirement**: reviewer skills must be run in sessions with no prior project context, not in continuation of the working session. A model that has participated in developing an argument is not in the same epistemic position as one encountering it for the first time; familiarity biases assessment toward evaluating intent rather than achievement. Fresh session = no accumulated context = closer to the epistemic position of an actual external reviewer. This is a structural design choice analogous to the pre-registration logic: assessment before context accumulates.
- Tool configuration can counteract known failure modes: explicitly instructing the AI to be critical, raise objections, and play devil's advocate addresses the sycophancy problem (Cheng et al. 2026). The user-level configuration documents epistemological commitments (severity testing, falsifiability, researcher degrees of freedom) — making them explicit rather than tacit, and encoding them as a permanent constraint on the tool's review behaviour.
- **Hermeneutic dimension of the reviewer persona**: the persona is not only an error-detection instrument. It is a reflexive move that lets the text speak back to the author from an alien vantage point — a form of disciplined self-interrogation in which the researcher's own argument is returned to them through a configured other. This is what makes structured review compatible with hermeneutic work (see §4.4): the reviewer skill does not presume a fixed prior argument; it produces critique that the researcher then engages with.

**Component 3 — Cross-model persona review.**

- **Cross-model persona review as documented procedure**: a set of reviewer personas — for this project, six (Delacroix, theoretical sociologist; Philosopher of mind; Hartmann, applied microeconomist; Kowalski, political scientist; Norwegian AI committee; Developer) — run in fresh sessions across multiple models (Claude, ChatGPT, Gemini). Each persona's prompt is documented; outputs are saved as markdown. The persona prompts and synthesis file are part of the replication package. At the and, run a new persona only once using Claude (presumably best suited for this task); the obnoxious asshole reviewer. Then revise. 
- **Rationale**: adversarial configuration (Component 2) addresses sycophancy within one model. Cross-model review addresses a different problem: a single model may be systematically biased toward certain argumentative styles, theoretical traditions, or rhetorical conventions. Running the same persona prompts across models from different developers exploits variance in training regimes to identify critique that is robust across models. A concern raised by one model may reflect that model's tendencies; the same concern raised independently by two or more models is substantially more credible. Model divergence on the same question is also informative — it signals genuine argumentative ambiguity. This is the review-stage equivalent of a robustness check.
- **Synthesis protocol**: act on any objection raised independently by two or more models; flag for judgement any objection raised by only one model; note model divergence as a signal of genuine ambiguity; disregard sycophantic positive feedback, use critical outputs only.
- **Persona calibration as query authorship**: each persona encodes a specific epistemic position structurally likely to resist the paper's argument from a direction the author cannot fully anticipate. The prompt design is the intellectual work; the model's output is execution within those constraints. This is distinct from asking "what are the weaknesses of this paper?" — a generic question that produces generic feedback.
- **Sycophancy as a threat to the researcher's thinking** (carried forward from §3.1): adversarial configuration and fresh-session design are defences not only against biased outputs but against the cognitive insulation a confirming model produces. A model that tells the researcher what they want to hear dulls rather than sharpens the researcher's thinking. [Second substantive appearance of Cheng et al.: first in §3.1 framing the problem; here as the mechanism structured use counters.]
- This is a concrete example of the structured/unstructured distinction: the same tool, identically prompted for content, produces epistemically different outputs depending on whether its review behaviour has been explicitly configured.

### 4.6 Documentation and replication package

- **Version tracking**: Run `bash scripts/log_session_meta.sh` at each session start. Appends to `logs/version-log.md` only when the Claude Code CLI version or configured model changes. Captures: CLI version, model identifier, git commit hash. This creates an audit trail of exactly which tool versions were used across the project's lifetime — essential for reproducibility given that AI tools update silently. Note the limitation: version logging documents the observable identifiers but cannot capture internal model weight changes within a version (that would require a locally deployed, pinned model). This limitation should be stated at point of relevance.
- All transparency artefacts compiled as supplementary material
- Include logging of which model is used, version pinning
- Sociological Science's mandatory replication package requirement: prompt templates, skill files, R scripts, search logs serve as the replication package — strong fit. The supplementary materials for a non-empirical methods paper are themselves a demonstration of the argument: structured use produces replication-ready materials as a natural byproduct. This is not additional overhead.
- **Two-tier documentation structure**: Working logs (daily session logs + author-input files) and final supplementary materials serve distinct functions. The logs document the process as it happened — iterative, with decisions revised and refined — and carry the evidentiary weight for process integrity, analogous to a lab notebook. The supplement presents the end-state artefacts in reusable, accessible form: what another researcher would need to adopt or verify the workflow. Both are present in the replication package; the paper should be explicit that they serve different purposes. [This mirrors how pre-registration works: the registered plan and the final methods section are both legitimate and neither substitutes for the other]
- **Author-input logs and authorship transparency**: The author-input files document what the author brought to each session — ideas, framings, redirections, pushbacks — in first-person prose. These serve a function analogous to authorship declarations in co-authored work: they document the human intellectual origin of the work and the human-AI division of labour. For this paper specifically, demonstrating this practice is the point. More generally, structured AI use with author-input logging enables transparent CRediT-style declarations of what was done by whom.

---

## 5. Epistemic properties of structured use

**Function**: The normative argument. Why structured use is epistemically preferable. Short, pointed, grounded in existing open-science literature.



### 5.1 The pre-registration analogy and query authorship

- The pre-registration analogy is productive but imprecise, and the honest way to use it is to state clearly what the framework gives, what it does not give on its own, and what it is compatible with.
- **What structured AI use gives**: externalisation discipline (tacit criteria are forced into explicit form), auditability (the record is there to be examined), and process legibility (a reader can follow what was done). These are genuine epistemic gains that parallel pre-registration's effect of making prior reasoning visible.
- **What structured AI use does not give on its own**: publicity, binding constraint, and the anti-manipulation guarantee that comes from a time-stamped commitment deposited with a trusted third party. A private log is not a public pre-registration, and git timestamps — while substantially harder to fabricate than recollection — fall short of the registration-server standard.
- **What it is compatible with**: the full setup (project configuration, skill files, search protocols, CLAUDE.md, prompt templates) can be deposited with OSF or an equivalent registry **before outcomes are generated**. The framework produces exactly the artefacts a formal pre-registration would require, so for researchers who want the stronger guarantee, the upgrade path is mechanical rather than conceptual. This is the far-systematic end of the spectrum introduced in §3.4.
- The decisive reframing: the primary epistemic claim is about **auditability**, not replication. AI workflows produce auditable process records; they do not produce bit-for-bit reproducible outputs (same prompt, different run, potentially different text). Positioning the framework as an auditability regime, with pre-registration as an optional upgrade, handles both the economist critique (too weak) and the theorist critique (too rigid).
- Note that pre-registration does not improve research only by restricting it — it improves research by forcing explicit commitment to decisions before outcomes are known. Structured AI use does this same externalising work whether or not a formal registration is attached.
- **Query authorship** is the conceptual heart of this: the configuration of the project, with research question, theoretical approach, how to do literature review (can be automated or autmented using AI), the automated reviewer processes, is an intellectual act that encodes the researcher's theoretical choices, scope commitments, and evaluative standards. The AI executes; the researcher authors. Making these choices explicit — in the query, the configuration, the documented protocol — externalises tacit knowledge in exactly the way pre-registration externalises research design choices. Unstructured use leaves this authorship invisible, creating a false impression that outputs emerged from the AI rather than from the researcher's intellectual commitments working through the AI.
- Literature on epistemic value of making reasoning explicit (notes-explicit-reasoning.md): tacit knowledge problem; externalisable criteria are verifiable criteria.
- The query authorship framing has implications for attribution and academic integrity beyond the AI context: it clarifies that the relevant intellectual contribution in AI-assisted research is the quality of the query, not the novelty of the output text.

### 5.2 Structured use as open science practice

- Transparency artefacts are shareable, versionable, and independently evaluable
- The Momeni et al. (2025) checklists for computational reproducibility in social science — developed with 180+ social scientists — cover data documentation, source sharing, methodological reporting; structured AI use satisfies these naturally
- Törnberg (2024) on prompt stability analysis: testing whether minor prompt changes alter results is only possible if prompts are documented — structured use makes this possible by default

### 5.3 The reliability finding — and its limits

- Zeng et al. (2025): reproducibility correlates with accuracy across 1,032 tasks — the discipline of structured prompting improves outputs, not just transparency. This is suggestive: structured use is not merely a transparency requirement but a mechanism for quality.
- **Scope limitation (stated here)**: The Zeng et al. finding comes from data science tasks; the paper cannot claim to have demonstrated the same for sociology research. The claim is that the logic is plausible and the adjacent evidence is consistent with it. This should be framed as "I suggest" rather than "I argue" — a hypothesis for future empirical validation, analogous to how Zeng et al. (2025) tested this formally in their domain.
- What this section can claim without overreach: structured use is a necessary condition for the kind of quality control that makes errors detectable; whether it also improves average output quality in sociology is an open empirical question.

### 5.4 What structured use cannot guarantee

- Structured use does not eliminate LLM error; it makes errors visible and correctable. It is a necessary condition for epistemic soundness, not a sufficient one. Non-determinism remains — same prompt, different output across runs; mitigation is to log outputs alongside prompts and to treat AI output as input to human judgement rather than as a final product.

**Documentation is not verification.** There are three tiers to keep distinct. (i) What documentation *certifies*: that criteria were prior and explicit, that configurations were retained, that the process is legible to an outside reader. (ii) What documentation *makes possible but does not certify*: the accuracy of the AI's execution of those criteria — this still depends on the human verification checkpoints embedded at each stage. (iii) What remains *unverifiable under any documentation regime*: non-deterministic execution, and internal model weight drift within a nominally identical model version (the version-log script captures observable identifiers, not weights). Framing the framework as auditability rather than replication makes this distinction honest rather than evasive.

**Verification quality depends on the verifier.** Human verification checkpoints are only as good as the researcher doing them. The framework creates the conditions for credible verification — intermediate outputs, legible scripts, traceable criteria — but cannot guarantee the substance. Two related thin-versus-thick worries follow. The **competence threshold**: the framework is calibrated for researchers with deep domain expertise who can recognise when an AI output is wrong. A junior researcher, or a researcher extending into a subfield outside their expertise, is in a structurally different position — the framework's protections are thinnest where the verification risk is highest, and this should be stated as a scope condition rather than glossed. The **thin-but-genuine documentation** case: a researcher who follows the workflow procedurally while the intellectual substance the framework is designed to certify is absent. This is more common in practice than outright fabrication and is not fully addressable by any disclosure regime.

**Git timestamps and model versions — calibrated claims.** Git commit history provides contemporaneous evidence that is substantially harder to fabricate than recollection, but it is soft evidence compared to a pre-registration server timestamp. OSF registration at project outset, or pushing to a remote at each commit, is the structural upgrade for researchers who want a stronger integrity guarantee. Model version pinning is a necessary element of a complete replication package — the `logs/version-log.md` record captures CLI version and configured model identifier — but outputs against a later model version may differ even with identical prompts, because weights change silently within a version string. The practical import: the framework moves from "trust the author's recollection" to "examine the author's process," which is a categorical improvement — but it does not move to "re-run the author's computation and get the same result."

**Self-demonstration — honestly stated.** This paper's own composition was systematic in infrastructure and more hermeneutic in argument development. The session logs, author-input files, reviewer skills, and literature-search pipeline were in place and did real epistemic work throughout. The conceptual moves — the spectrum reframing, the sycophancy-as-cognitive-threat formulation, the documentation-versus-verification distinction — developed during the writing rather than from a pre-specified plan. This is what the spectrum argument predicts (see §3.4 and §4.4): a single project sits at different points on the spectrum at different stages, and the systematic infrastructure supports hermeneutic stages as well as pre-specifiable ones. Acknowledging this is not an admission that weakens the paper; it is the demonstration that the framework's value does not depend on pre-registered rigidity. One further honest note: the Gelman-Loken forking-paths critique applies to the documentation process itself — a researcher can produce a log that reflects the cleaned-up version of the process rather than its full texture, not through dishonesty but through ordinary retrospective rationalisation. Structured use reduces but does not eliminate this.

### 5.5 Authorship criteria and the accountability threshold

**Function**: Connects the systematic use argument to established authorship standards (ICMJE/Vancouver criteria). Applies the criteria positively — as a framework for evaluating the human researcher's contribution in AI-assisted work — rather than merely negatively to exclude AI authorship (which is widely done and not in dispute).

- ICMJE criteria: four requirements — substantial contribution to conception/design; critical revision for intellectual content; final approval; accountability for all aspects. AI is excluded by criteria 3 and 4 (cannot consent, cannot be held accountable). This is settled and not the interesting question.
- The interesting question: what the criteria imply *for the researcher*. Criterion 1: query authorship maps directly — designing search strategy, screening rubric, analytical specification, reviewer configuration are all acts of conception and design. Systematic use produces the evidence that criterion 1 is met; unsystematic use does not.
- Criterion 2: author-input files are a direct instantiation — they document, session by session, what the researcher directed, redirected, and rejected. Criterion 3: final approval is *informed* under systematic use — the researcher can trace the process that produced the version they approved.
- Criterion 4 is sharpest: genuine accountability — ability to investigate questions about accuracy and integrity — requires access to the process. Systematic use produces this access structurally; undocumented use relies on recall and reconstruction. This is a different type of accountability, not merely a more transparent version of the same thing.
- Policy implication: the ICMJE criteria give journal policy a more tractable question than "was AI used?" — namely, whether the researcher can demonstrate that authorship criteria are met. A documentation-based framework operationalises this; binary prohibition addresses the easy question while leaving the harder one unasked.

---

## 6. Implications for journal policy

**Function**: Application of the argument. Critical but concessive. Not the main event — an implication.

### 6.1 What current policies do

- [Concessive]: Journals responded rapidly and in good faith to genuine concerns about AI-generated content and undisclosed use
- Cross-sectional audit (Mondal et al., 2024) of 20 major publishers: six converging themes. The field has moved from silence to active guidance. Goyanes (2025) and da Veiga (2025) extend this picture to the journal level.
- But the guidance is binary: permit or prohibit. No policy distinguishes structured from unstructured use.
- Ganjavi et al. (2024): publishers' instructions focus on disclosure of AI use, not on the epistemic quality of that use

### 6.2 The problem with binary policies

- Blanket restriction penalises structured use — the researcher who built a documented, reproducible screening protocol is treated the same as one who asked ChatGPT to summarise their references
- Blanket permission with disclosure does not incentivise structured use — disclosure of "I used GPT-4 to assist with analysis" gives readers no information about whether the use was epistemically sound
- Both responses leave the structured/unstructured distinction invisible
- [Tone note throughout §5]: The critique must stay constructive — the target is the framework, not the good faith of editors or publishers. The goal is to propose a better instrument, not to impugn the existing ones.

### 6.3 A documentation-based alternative

- The relevant policy question is not "did you use AI?" but "can you show what you did?"
- **The conservative framing**: Extending existing replication package norms to AI-assisted workflows requires no new principle and no new infrastructure — only an expanded understanding of what "the materials needed to reproduce the analysis" includes. For a study using regression, that means code and data. For a study using a structured AI workflow, that means skill files, prompt templates, search scripts, and screening logs. Journals that already require replication packages for quantitative work (Sociological Science since April 2023) have accepted the underlying logic; they have no principled basis for treating AI workflow documentation differently. This makes the policy recommendation conservative rather than radical.
- Jones (2025, qualitative) and Davidson & Karell (2025, SMR) move in this direction — disclosure frameworks that specify *what* was done, not just *whether*
- This shifts the evaluative burden to peer review, where it belongs: reviewers can assess whether the structured process was appropriate, not just whether AI was used

---

## 7. Conclusion

Five points must be present; see `notes/conclusion-requirements.md` for detail.

1. **Systematic/unsystematic AI authorship as the analytical frame** — not use/non-use, not structured/unstructured as the primary frame. The central claim: systematic AI use is de facto an authorship contribution; the execution is not the most important element.

2. **Query authorship as the mechanism** — intellectual contribution lies in the criteria, configuration, and verification design. This is citable, auditable, and open-science compatible.

3. **Author-input files and session protocol as transparency artefacts** — novel mechanisms that document the human intellectual origin of the work, session by session. Part of the replication package. No self-referential framing ("this paper did X") — just name the artefacts and their function.

4. **Journal policy directive** — the question journals should ask: not "did you use AI?" but "show us your systematic process." Operationalised through existing replication package norms; no new principle required.

5. **The workflow as demonstration** — the supplementary materials (not this paper's prose) serve as the proof of concept. The paper makes the argument; the documentation enacts it.

**Structural note**: Conclude on the policy directive, not on the empirical replication call. The Zeng et al. open question is a coda, not the closing move.

---

## Supplementary materials (replication package)

Sociological Science requires a replication package as a condition of publication (mandatory since April 2023), normally understood as statistical code and data. For this paper, the transparency artefacts of the structured workflow serve the equivalent function — and the paper should say so explicitly in the methods section. This is not a workaround but a demonstration of the argument: structured use produces replication-ready materials as a natural byproduct.

**Two-tier structure**: The package contains both working logs (process integrity evidence) and final artefacts (replicability evidence). These serve distinct functions and should be clearly labelled as such in the package documentation.

The package must include the actual files used, not illustrative examples:

- **Skill files** (actual versions in use): `skardhamar-style`, all reviewer skills used during drafting and review
- **`CLAUDE.md`** — project-level configuration including adversarial/critical engagement instructions
- **Main user-level `CLAUDE.md`** — system-level tool configuration including epistemological commitments (relevant to the query authorship and sycophancy arguments)
- **`scripts/log_session_meta.sh`** — version tracking script; `logs/version-log.md` — audit trail of CLI and model versions used across the project
- **`scripts/search_openalex.R`, `scripts/download_pdfs.R`, `scripts/screen_candidates.py`** — executed search and screening pipeline with parameters used
- **`literature/automated_literature_searches/boolean-searches.md`** — executed search strings, result counts, screening decisions
- **Screening outputs** — `literature/automated_literature_searches/fulltext_scores.csv` and `filter_tidying/rename_log.csv`, documenting inclusion/exclusion basis
- **`logs/`** — daily session logs and author-input files (process integrity record)
- **`supplementary/file-structure-template.md`** — project structure for reuse
- **`supplementary/boolean-search-guide.md`** — search strategy documentation
- **`supplementary/persona-review-prompts.md`** — the six persona prompt templates (Delacroix, Philosopher, Hartmann, Kowalski, AI committee, Developer) and the synthesis protocol used for cross-model review, derived from `notes/review-prompts-personas.md`
- **`draft/simulation-reviews/`** — collected persona-review outputs across Claude, ChatGPT, and Gemini, plus the synthesis file; serves as process-integrity evidence that the documented review procedure was executed

**Note before submission**: Copy installed skill files from AppData into `supplementary/` — do not rely on installed copies being stable.

---

## Key literature (to be cited; keep in-text citations minimal)

**Problem statement anchors (introduction):**

- Hindawi/Wiley retractions (2022–23) — 8,000+ papers; the watershed event for AI-scale fraud overwhelming editorial safeguards
- O'Grady, C. (2023). "Honesty papers retracted for data 'discrepancies'." *Science*, 381(6655), 255–256 — Gino retractions; the mechanism failure of declaration-based policy; one paragraph in the introduction
- "De-AI" services (grey literature) — perverse incentive evidence; the strongest available empirical case that disclosure policy creates evasion rather than transparency
- APE automated research system (ape.socialcatalystlab.org) — p-hacking at scale; evidence for why unstructured automation is the wrong direction

**The gap — checklists vs. pipelines:**

- Mondal et al. (2024) — publisher guidelines audit
- Zrubka et al. (2025) — systematic review of 24 AI reporting guidelines (10–66 items)
- Holst et al. / PRISMA-trAIce (2025) — most formalized checklist, systematic reviews only
- Goyanes (2025) — journal-level author guidelines survey [check: does it document binary permit/prohibit structure?]
- da Veiga (2025) — thematic analysis of AI ethics guidelines for scholarly publishing

**Epistemic cost of unstructured use:**

- Ludwig, Mullainathan & Rambachan (2024) — prompt choice affects parameter estimates
- Barrie et al. — LLM variance "unacceptably high" without versioning
- Zeng et al. (2025, AIRepr) — reproducibility correlates with accuracy [from data science; generalise cautiously]
- Cheng et al. (2026, *Science*) — sycophantic AI reduces independent judgment; empirical grounding for adversarial configuration

**Closest disciplinary antecedents (social science):**

- Davidson & Karell (2025, SMR) — measurement, prompting, simulation [priority read before drafting]
- Blanchard et al. (2025, Journal of Marketing) — most complete social science pipeline [priority read before drafting]
- Törnberg (2024) — text annotation best practices, prompt stability
- Jones (2025) — qualitative AI disclosure heuristic

**Contrast case:**

- Xu & Yang (2026, arXiv 2602.16733) — automated multi-agent pipeline for scaling replication; contrast with human-in-the-loop workflow

**Framing citations:**

- Grossmann et al. (2023, *Science*) — AI transforming social science; cautiously optimistic framing
- Korinek (2023, NBER) — use cases for economists; practical/descriptive; complementary to the epistemic framework argument

**Open science / pre-registration connection:**

- [see notes-explicit-reasoning.md]
- Nosek et al. (2015, *Science*) — open science
- Freese & Peterson (2017, ARS) — replication in sociology

**Journal policy:**

- Ganjavi et al. (2024) — publishers' author instructions
