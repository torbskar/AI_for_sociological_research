# Query Authorship: A Framework for Systematic AI Use in Social Science

Torbjørn Skardhamar, Department of Sociology and human geography, University of Oslo

**Date:** 2026-04-25

---

## Abstract

The intellectual contribution in AI-assisted research is not in the text the AI produces but in the instructions that shaped it. Unsystematic use of AI is unaccountable, with a possible consequence of overflowing the scientific literature with noise. In contrast: systematic use of AI is embedded in explicit criteria, subject to human verification, and producing documented outputs. Both modes of AI use are currently treated as equal — but they are not. I introduce the concept of *query authorship*. Systematic AI authorship is a necessary condition for epistemic soundness, not a sufficient one: it makes errors visible and correctable rather than eliminating them. It instantiates the properties of open-science practice — externalising tacit commitments, producing verifiable artefacts, consistent with replication package norms. A documentation-based framework that operationalises this distinction is more epistemically honest than binary approaches and requires no new infrastructure.

---

## Introduction

The scholarly record is under documented pressure. Papermill operations — organisations that produce fabricated research for payment — have industrialised the generation of fraudulent work, and AI tools have made that production faster and cheaper. The Hindawi/Wiley retraction of more than eight thousand papers in 2022–23 is the clearest large-scale marker of what that pressure looks like (Retraction Watch, 2023): a major publisher publicly acknowledging that its editorial safeguards had been overwhelmed. AI-induced hallucinated citations contaminate the evidential record in a more dispersed way — citations function as data in social science disciplines, and fabricated references are not a nuisance but a direct integrity failure. Unstructured AI use also multiplies undocumented decision points across the research process, from language editing through substantive rewriting to generating conclusions with authorship attribution: the gradient is continuous and everyone in the field is struggling with where it remains acceptable. The question is not whether AI has entered research practice — it has, and researchers will use it — but whether the field has the right instruments to govern its use.

The dominant institutional response has been to require disclosure. Journals ask authors to declare whether AI tools were used; publishers issue guidelines specifying what must be reported. This is a reasonable first step, but it is insufficient as a primary safeguard on two independent grounds.

The first is scale. Declaration-based policy offers no resistance to industrial-scale fraud: papermill operations can produce plausible disclosures at volume. More tellingly, the response to enforcement-based detection has been the emergence of a counter-industry: services that, for a fee, strip textual patterns associated with AI generation from submitted manuscripts — not to improve the text but to evade detection. Disclosure policy has produced the perverse consequence that it drives AI use underground rather than making it transparent. Documentation policy, by contrast, cannot be evaded in the same way: its artefacts are generated during the work, not as statements made about it afterwards.

The second ground is mechanism. Declaration-based policy rests on a behavioural assumption: that requiring a declaration of intent produces the declared behaviour. That assumption had an unusually prominent empirical demonstration in a much-cited paper reporting that signing an honesty pledge at the top rather than the bottom of a form increases honest reporting. That paper was retracted in 2021 after apparent data fabrication was identified in a co-authored study; two further papers by the same lead author were retracted in 2023 (O'Grady, 2023). The specific mechanism that declaration-based AI policy would need to work — that requiring a declaration of compliance produces compliant behaviour — has lost its most-cited empirical demonstration, and that demonstration was itself fabricated. I do not cite this to impugn the disclosure tradition as a whole, but to make a precise point: the policy instrument most widely adopted has an empirical warrant that has been publicly undermined in precisely the field that generated it.

I want to acknowledge that journals and publishers responded to genuine problems rapidly and largely in good faith. The concerns motivating binary AI policies — undisclosed AI-generated text, AI-assisted fabrication at scale, questions about authorship and accountability — are real and serious. The argument here is about the instrument, not the intent. A binary approach — use or non-use, disclosed or not — misidentifies the epistemically relevant dimension. What matters is not whether AI was used but whether its use was *systematic*: embedded in explicit criteria, subject to human verification at each stage, and producing documented outputs. The structured/unstructured distinction is where the real epistemic leverage lies, and current policies leave it invisible.

This paper makes five connected moves. First, I develop the distinction between systematic and unsystematic AI authorship, arguing that the two differ not in average output quality but in epistemic standing: systematic use makes errors visible and correctable; unsystematic use does not. Second, I introduce the concept of *query authorship* — the argument that designing a search strategy, a screening rubric, or a review configuration encodes the researcher's intellectual commitments in a verifiable form, and that this constitutes the human contribution in AI-assisted research. Third, I describe a systematic workflow for sociology across the research pipeline, from literature search through drafting and review to documentation. Fourth, I argue that systematic AI authorship instantiates the epistemic properties of open-science practices — in particular, the function of pre-registration in forcing explicit commitment to decisions before outcomes are known. Fifth, I draw implications for journal policy, arguing that a documentation-based framework that asks researchers to show what they did is both more epistemically honest and more consistent with existing open-science infrastructure than binary policies.[^1] The concept of systematic AI authorship, as I develop it, maps directly onto established scholarly authorship standards — in particular, the ICMJE[^2] criteria (often called "Vancouver criteria") that define what it means to be an author rather than merely a contributor — a connection I develop towards the end of the section on epistemic properties.

The systematic approach is a spectrum rather than a binary. Degrees of systematic use exist, and how to implement it is up to the author and their theoretical, methodological, and epistemic commitments. The unsystematic approach is off this spectrum rather than at one end of it: the absence of explicit criteria and documentation is not a minimal version of systematic use but something categorically different, because errors cannot be detected and choices cannot be attributed.

The workflow described here is for text-heavy and empirical social science research; the focus is on the systematic use and documentation rather than the specifics of empirical analysis as such. Data collection and the handling of personal data are subject to additional constraints described in the section on empirical data and analysis.

The argument developed here is directed at sociology and adjacent social sciences where research questions and theoretical framings cannot be delegated to automated agents. The workflow generalises from the author's own research practice; the case for its broader applicability rests on its correspondence to methodological commitments — documentation norms, verification requirements, explicit criteria — that predate AI use. The workflow is demonstrated using Claude (Anthropic) as the AI tool, and some implementation details — in particular the project context file (CLAUDE.md), the context exclusion list (.claudeignore), and configured reviewer roles (skills) — use Claude-specific terminology throughout. Any AI system that supports persistent context, configurable roles, and session logging can implement the same workflow structure; the principles are not specific to Claude.

---

## AI in research

Large language models have been widely adopted across academic disciplines (Grossmann et al. 2023), and in sociology their uptake has outpaced the institutional frameworks for evaluating them. Korinek (2023) catalogues practical use cases for economists and social scientists; Feuerriegel et al. (2024) trace early adoption in information systems. The question of whether AI has entered research practice is settled; what remains contested is what kind of practice has emerged and what kind should be.

The dominant institutional response has been the reporting checklist — an instrument designed to improve transparency by specifying what authors must disclose about AI use after the research is done. These checklists have proliferated rapidly. Zrubka et al. (2023) systematically reviewed 24 such instruments and found that item counts range from 10 to 66, indicating that no consensus has emerged on what "full disclosure" even means. Among the most developed are PRISMA-trAIce (Holst et al., 2025) for systematic reviews, TITAN (Agha et al., 2025) for general academic purposes, and the clinical variants TRIPOD-LLM and CONSORT-AI. Publisher and journal guidance follows the same disclosure logic. Mondal et al. (2024) audited 20 major publishers and identified six converging themes across their AI policies — all centred on disclosure of AI use and attribution of responsibility, none on the epistemic structure of the research process itself. Ganjavi et al. (2024) extend this picture to the journal level, finding that 87% of top-ranked journals have issued AI guidelines while only 24% of large publishers have done so, and that in some cases individual journals contradict their own publisher's guidance — a fragmentation that leaves authors navigating requirements that vary not only across disciplines but within them. Goyanes (2025) documents similar variation in journal-level policies.

Social science has developed some pipeline-oriented guidance. Törnberg (2024) addresses text annotation best practices and prompt stability analysis; Davidson and Karell (2025) provide a framing for integrating generative AI into social science research across measurement, prompting, and simulation tasks. To my knowledge, Blanchard et al. (2025) offer the most complete practical pipeline in the social sciences — reproducible prompt templates and pre-registration materials, developed for marketing research. From NLP and data science, Zeng et al. (2025) demonstrate that systematic prompting designed for reproducibility also produces better results on average across a large sample of tasks — a suggestive finding for adjacent social science uses, though not directly transferable. To my knowledge, no sociology-specific guidance exists, as distinct from the broader social science literature.

### Checklists and declarations

The checklist approach addresses one genuine problem: it creates a record of AI use that did not previously exist, enabling readers to assess what was done. This is of course good practice. The limitation is that checklists are post-hoc instruments: they assume the research process was already sound and ask only that the author report on it. A researcher could complete every item on PRISMA-trAIce while having used AI in a wholly unverifiable way. The checklist captures the end state; it has nothing to say about how that end state was produced.

No established framework explicitly theorises the systematic/unsystematic distinction as the fundamental policy-relevant axis. Törnberg (2024) and Davidson and Karell (2025) both implicitly favour more systematic over less systematic AI use, but neither treats this distinction as the central policy question. To my knowledge, no existing work treats AI tool configuration — skill files, configured reviewer roles, system-level prompts — as an epistemic mechanism comparable to pre-registration or researcher-degrees-of-freedom disclosure. Neither am I aware of any work that discusses the transparency artefacts produced by systematic AI use (prompt templates, search logs, skill configurations) as components of a replication package, nor any sociology-specific workflow framework of this kind. It is worth noting that such a framework, encoding configuration and criteria, could itself be pre-registered — producing a public, timestamped commitment to the research design before data collection or analysis begins.

The one settled question in the policy literature is that AI cannot be an author — a position consistent with the ICMJE criteria, which require accountable, consenting persons (Ganjavi et al., 2024; Mondal et al., 2024). But the criteria themselves do more than rule out AI authorship: they specify what the human researcher must demonstrate to claim authorship in any research context — substantial intellectual contribution to conception or design, critical engagement with the content, final approval, and accountability for all aspects of the work. To my knowledge, no existing work has developed the ICMJE criteria into a positive framework for evaluating the human researcher's contribution in AI-assisted work — as distinct from applying them negatively to rule out AI authorship, which is widely done. That question is the one that matters for evaluating the epistemic standing of AI-assisted work, and it is the one current policies do not ask.

---

## The systematic/unsystematic distinction

Unsystematic AI authorship is characterised by prompting without explicit criteria and refining until an acceptable output is produced. In the worst case, the criteria are entirely implicit, outputs are accepted without verification, and no documentation is produced that would allow another researcher — or the same researcher at a later date — to audit what was done, let alone reproduce it. This is not primarily a matter of negligence; most researchers who use AI tools unsystematically are trying to do good work. The problem is structural: the conditions for verifiable good work with AI are absent.

The epistemic cost of this approach has been documented from several angles. Ludwig, Mullainathan and Rambachan (2024) show that seemingly innocuous choices — which model, which prompt formulation — can produce substantially different parameter estimates, and that these choices are rarely reported. Barrie et al. (2025) find that LLM performance variance is often unacceptably high even under controlled temperature settings; without logging, there is no way to know whether a given result would survive re-running. Kosch and Feger (2025) document a closely related failure they term PARKing — Prompt Adjustments to Reach Known Outcomes — in which researchers iteratively modify prompts until the model returns a desired result, producing outputs that resist replication because the prompt history is undocumented. Cheng et al. (2026) demonstrate something more troubling: sycophantic AI responses — outputs calibrated to confirm rather than challenge user priors — systematically reduce independent judgment and promote dependence. Asher et al. (2026) demonstrate this in a more precise empirical register: in 640 runs across four published political science datasets, LLMs prompted through a reframed "nuclear" instruction performed systematic specification searches — cycling through hundreds of analytical variants and selecting only significant results. Peters and Chin-Yee (2025) document a further directional failure: generalisation bias, the tendency of LLMs to broaden the scope of scientific conclusions beyond what the original data supports — a finding with particular force for literature-based research in which the AI summarises sources. The implication for research is that the failure mode in unsystematic AI use is not random but directional. The AI is not simply noisy; it tends to confirm rather than challenge, and to overstate rather than accurately report.

A useful characterisation of what these specific failure modes share is offered by Frankfurt's (2005) distinction between lying and bullshit: the liar aims to deceive and so must track the truth in order to subvert it, while the bullshitter is indifferent to whether what they say is true. Language models, considered as output-generating processes, are structurally closer to Frankfurt's bullshitter than to his liar — they optimise for plausible continuation, not for truth (Hicks et al., 2024). The point is not that researchers using AI tools are bullshitters; most are truth-seeking. The point is that unsystematic AI use leaves the researcher accepting outputs from a process that does not itself track truth. Systematic use is what converts a truth-indifferent generator into a truth-accountable workflow — by imposing at each stage the explicit criteria and human verification checkpoints that the underlying generator does not supply.

None of these problems are unique to AI. Undocumented manual coding, unreported variable transformations, and selective literature search are all unsystematic in the same sense — they produce results that cannot be evaluated because the process that produced them is invisible. What AI introduces is scale: the range of judgements that can be delegated, and therefore potentially hidden, has expanded enormously. In this sense, the systematic/unsystematic distinction is not a new principle; it is the application of an existing epistemic standard to a new tool.

The failure modes described above concern what the AI does to outputs. There is also a problem about what unsystematic AI use does to research thinking. The writing-as-thinking tradition documents that writing is epistemically valuable precisely because it forces deliberate semantics — the explicit structuring of logical relationships that tacit thought leaves implicit (Emig, 1977). Sommers (1981) frames the complement: revision is not polishing but recursive discovery — finding a structure is itself a strategy for finding meaning, and a writer who is handed a pre-given structure to polish is doing something categorically different from one who discovers structure through composition. Unsystematic AI use maps directly onto this failure: a prompt without explicit criteria, an output accepted without iteration — the AI does the structuring and the researcher accepts the result. The deliberate semantics that would force articulation of what the argument is and why the evidence supports it are bypassed. This is not a concern unique to AI; it is the longstanding concern about delegating cognitive work, now operating at scale.

### What systematic AI use looks like

Systematic AI authorship has three defining features. The first is explicit criteria: the instructions given to the AI specify what to do and on what grounds — not "screen this abstract for relevance" but "retain this abstract if it addresses AI use in empirical research practice; exclude if it addresses only AI as a research subject, AI ethics in general, or K-12 education; retain in case of doubt." The research question or purpose should be part of the persistent context so that each individual prompt is not interpreted in isolation. In practice, explicit criteria operate at multiple levels: a persistent project-level configuration that encodes the research question and scope, and individual prompt-level specifications for each task. AI tools implement this differently, but the principle is consistent across platforms.

The second is human verification: at each stage where the AI produces an output, there is a specified human checkpoint where the output is evaluated against the criteria before it passes to the next stage.

The third is documented outputs: prompt configurations, screening rubrics, skill files, and decision logs are retained as artefacts that allow the process to be reconstructed and evaluated.

These three features are implemented through a project-level configuration with associated file structure that supports progress across the full project — from initial design through execution to documentation. This project-level structure encodes the researcher's theoretical commitments, scope decisions, and evaluative standards. These choices belong to the researcher, not the AI, regardless of who executes them. The AI executes within the instructions; the researcher authors the instructions. Systematic use makes this authorship explicit and verifiable. Unsystematic use leaves it implicit, creating a false impression that outputs emerged from the AI rather than from the researcher's intellectual commitments working through it. To be precise: unsystematic use also involves intellectual choices; the point is not that systematic use uniquely creates the researcher's contribution but that it documents and verifies it. This is what the concept of *query authorship* captures.

Systematic AI authorship can be understood in functional terms as analogous to pre-registration. Pre-registration does not improve research by restricting it but by forcing explicit commitment to research design decisions before outcomes are known. Systematic AI use does the same: the criteria must be articulated before the tool is run, not constructed post hoc to justify what the AI returned. Kosch and Feger's (2025) PARKing — iterative prompt refinement until a desired result emerges — is precisely the failure mode that pre-specification forecloses, and the remedy they propose is the same: a contemporaneous record of what criteria were set and which attempts preceded the accepted output. The analogy holds in function. A relevant disanalogy is that pre-registration involves a public, timestamped commitment, while a systematic AI protocol is initially private. The disanalogy is genuine: systematic AI use does not provide the binding constraint, publicity, or guard against manipulation of pre-registration. First, the externalisation benefit — forcing articulation of tacit decisions — follows from the act of specification itself, regardless of whether it is public; second, the working logs that document iterative process address the cherry-picking risk that pre-registration's public commitment eliminates through publicity; third, there is no obstacle to pre-registering a systematic AI workflow where the research design permits it. 

When the analysis is complete, the artefacts — scripts, configurations, logs, screening decisions — are documented analogously to open-science materials for empirical analysis. The pipeline and workflow constitute a replication package: the "open code and data" of systematic AI use.

Within the systematic category, implementation ranges widely — from informal discipline in specifying criteria and logging outputs to full pre-registration of the workflow protocol. Partial compliance is better than none; the framework identifies the properties that systematic use must have without specifying a single required level of rigour. Pre-registration represents the far end of the spectrum for researchers who want the publicity and anti-manipulation guarantee it provides; informal systematic discipline is the minimal entry point.

### Why the distinction matters

Epistemically, the core consequence is simple: systematic use makes errors visible and correctable; unsystematic use does not. A miscalibrated screening rubric in a documented, reproducible workflow can be identified, challenged, and corrected by a reviewer. An undocumented prompt cannot.

The existing literature has converged on reporting checklists as the response to this problem, and I have already acknowledged what these instruments achieve. Their limitation is different from what critics of AI in research sometimes suggest. The concern is not that checklists enable researchers to hide bad practice behind a disclosure form — most researchers using these instruments are acting in good faith. (Neither would they prevent bad practice by motivated actors.) The concern is structural: checklists presuppose a prior question rather than answering it. They ask what was done; systematic use determines whether what was done is evaluable. These are different moments in the research process, and addressing one does not substitute for the other.

The systematic/unsystematic axis is also orthogonal to the use/non-use axis that current policy focuses on. A researcher using AI in a systematic and documented way may produce work that is more epistemically auditable than one who relies on undocumented, unreportable manual judgements — judgements about what is relevant, which sources are important, which arguments are coherent — that are equally invisible but have simply not attracted policy attention. The policy question is not, or should not be, whether AI was used, but whether what was done can be evaluated.

---

## A systematic workflow for sociology and social sciences

Established best practice already exists for empirical data analysis — sharing code and data, using version control, documenting variable transformations. These practices apply whether the work is AI-assisted or not, and systematic AI authorship extends rather than replaces them. The focus here is on the research and writing pipeline of a standard journal article — covering literature work, empirical analysis, and documentation. Systematic review has its own established protocols and is not addressed here.

A systematic workflow for this purpose has five stages: 1) literature search with screening and synthesis, 2) empirical data and analysis, 3) drafting, 4) review, and 5) documentation. At each stage the structure is the same: explicit input criteria determine what the AI is instructed to do; a configured AI tool executes within those criteria; a human verification checkpoint evaluates the output before it passes to the next stage; and a documented artefact records what was done. The transparency artefacts produced across all stages — boolean search strings, screening rubrics, skill configurations, prompt templates, search logs, source set compositions, analysis scripts, codebooks, review records — constitute the replication package. 

The structure presented here is a basic setup, and it could also be done differently.[^3]  How it was implemented specifically to this specific paper are in the supplementary materials and full details are available in a github repository[^4].

The three requirements — explicit criteria, human verification, and documented outputs — can be implemented with different tools and at varying levels of complexity. What follows is one minimal but complete implementation: sufficient to instantiate all three properties, and sufficient to demonstrate the replication package logic, without requiring specialised infrastructure. The specific tools (Claude Code, NotebookLM, ASReview, Elicit) are instances of a type, not the only instances; a researcher working with different platforms can implement the same structural logic using equivalent tools that serve the same functions. The workflow as described assumes agentic AI — a tool that reads files, maintains persistent context across sessions, and executes within a standing project configuration. Researchers working with chat-only interfaces (ChatGPT, Gemini, and similar) can implement the same principles, but the setup is more manual: project context must be pasted at the start of each session, outputs downloaded and filed by hand, and configuration maintained through discipline rather than automation. The core requirements — explicit criteria, human verification, documented outputs — do not change; the practical barrier to maintaining them consistently is meaningfully higher.

The basic project folder structure that supports this workflow is illustrated below. Empirical papers include the `data/` subdirectories; non-empirical papers do not.

```
project/
├── data/
│   ├── raw/                  ← original data
│   └── processed/            ← analysis-ready files
├── scripts/                  ← analysis code (R, Python, Stata)
├── outputs/                  ← tables and figures
├── literature/               ← search logs, source sets, syntheses
├── notes/                    ← working notes and argument sketches
├── draft/                    ← manuscript versions with full edit history
├── logs/                     ← session decision logs and author-input files
└── supplementary/            ← replication package materials
```

A few configuration files at the project root do structural work not visible in the folder tree. One encodes the project context — the research scope, argument, and key distinctions — so that every session starts with the same framing. Another specifies access controls: certain folders, in particular `data/raw/`, can be blocked from the AI's context entirely, providing a structural safeguard that raw data never enters the AI regardless of how the tool is used in a given session. A version-control repository timestamps every change to the project files, so that session logs and author-input files can be verified as contemporaneous records rather than retrospective reconstructions. The full configuration, including the specification for agentic AI tools, is detailed in Appendix A.

This is not an automated pipeline in the sense of Xu and Yang (2026), who demonstrate multi-agent systems capable of scaling well-defined computational tasks with minimal human input. That approach is effective where the research task is sufficiently specified that its execution can be delegated. Sociology research — formulating questions, selecting and interpreting evidence, constructing arguments — is typically not of that kind. The researcher is in the loop at every stage; the AI handles execution within explicitly defined criteria, and the researcher handles judgement — even if discussing options with the AI before deciding. The distinction matters for both epistemic and methodological reasons: it is precisely this division of labour that makes the workflow's outputs attributable to the researcher.

### Literature search and screening

The literature review can of course be done manually in a standard way, and whether to use AI in this specific stage is up to the author. A standard literature review in a journal article is not a systematic review. It is typically more selective, guided by the author's sense of what is relevant and frequently shaped by citation patterns rather than by systematic coverage. Systematic reviews have established protocols — PRISMA and its variants — that serve a different purpose and are not the target here. What systematic AI authorship offers for a standard article is something intermediate: a more thorough and more accountable search and screening process than is typically possible manually, without the full apparatus of a systematic review (Hart 2025, Gusenbauer & Gauster 2025). It will involve three basic stages: literature search, filtering based on metadata (title and abstract), and summarizing from fulltext.  

The key principle is that AI makes extensive search and screening of large literatures inexpensive in terms of researcher time, though it costs computational resources. A realistic workflow combines three routes: automated keyword searches across an open bibliographic database, semantic searches that find papers regardless of their keyword choices, and targeted manual retrieval for specific high-priority items. Each route catches what the others miss, and together they produce coverage substantially better than any single approach. For accountability, standard keyword searches in databases like Scopus and WebOfScience is a good basis, and AI can speed up the screening using specialized tools like [ASReview](https://asreview.nl/). 

However, for the use of AI, open database APIs with explicit research-use permission are preferable to bulk export from subscription databases, whose institutional agreements vary and may not cover computational analysis. Boolean search strings are documented in advance as explicit inclusion/exclusion criteria — not constructed post hoc to cover what was found — and the full search log is archived. Candidate screening applies a configured keyword-based rubric with stated criteria; retain in case of doubt and exclude only on well-specified grounds. Full-text relevance scoring across themes is algorithmic and auditable. The semantic search route — using tools designed for semantic rather than keyword matching — recovers papers that use different terminology for the same concepts and covers preprints and working papers that keyword searches miss.

Source synthesis uses a grounded AI tool: queries are submitted to a notebook containing only the relevant-theme documents, and responses are grounded in and cited from those documents. Unlike a general-purpose chatbot, this produces inline citations the researcher can verify against the underlying sources. The synthesis query itself is an instance of query authorship: the intellectual work lies in specifying what the synthesis should produce, what distinctions matter, and what gaps should be identified.

The literature search for this paper followed these principles; the full implementation — search strings, hit counts, screening criteria, and synthesis queries — is documented in Appendix A.

### Empirical data and analysis

Primary empirical data introduces constraints that literature work does not face. Research data — whether administrative records, survey responses, or interview transcripts — is frequently subject to GDPR obligations, ethics committee conditions, or institutional data agreements that restrict where data can be stored, processed, and shared. These constraints interact directly with how AI tools can be used. The principle that governs this section is strict separation: the AI operates on the research context and on analysis scripts, not on the data itself. Correctly implemented, the AI never reads the raw data; it reads and helps write, review, and document the code that processes it. The paper's own production is literature-based and does not involve primary data; what follows is anticipatory guidance rather than demonstrated practice, grounded in the configurations and data structures that implement the separation principle.

The project folder structure for empirical work extends the template shown in the workflow overview with a `data/` hierarchy following the Cookiecutter Data Science standard: `data/raw/` for original data as received, `data/interim/` for intermediate files after cleaning or anonymisation, `data/processed/` for analysis-ready datasets, and `data/external/` for third-party reference data. The `data/raw/` folder is immutable: original data is a transparency artefact, not a working file, and must not be modified — not manually, not by scripts, not by AI — after receipt. This norm is encoded in the project's `CLAUDE.md` as an explicit rule, and `.claudeignore` excludes the folder from the AI's working context — keeping raw data out of what the AI attends to, though actual prevention of data reaching the API requires access-control configuration beyond context exclusion, as discussed below. The immutability norm is the data equivalent of the pre-registration norm: it prevents post-hoc manipulation of the starting conditions and ensures that replication can begin from the same starting point every time.

The AI's role in empirical analysis is to write, review, and document the analysis code — not to inspect the data directly. Transformation and analysis scripts are written by the AI to a specification the researcher authors: which variables to construct, which analytical strategy to apply, how edge cases should be handled. This is query authorship in the empirical register. The researcher's intellectual contribution is the specification; the AI's contribution is its implementation. For the workflow to remain verifiable by a researcher without deep programming expertise, that implementation must be legible. Practical requirements follow from this: scripts are numbered sequentially to make execution order explicit (`01_import.R`, `02_clean.R`, `03_anonymise.R`, `04_analyse.R`); each begins with a short header specifying inputs, outputs, and purpose; intermediate outputs are saved after each major transformation step so the researcher can inspect the data at each stage without re-running the full pipeline; and comments explain in plain language why each step is taken, not merely what it does.

For projects involving personal data, raw data must not be sent to a cloud AI API without screening. Claude Code implements this through a `PreToolUse` hook: a local Python script runs before any file read operation and scans the target file for personal data patterns; if personal identifiers are detected, the read is blocked before any data reaches the API. Available tools for this screening include Microsoft Presidio — open-source and configurable for Norwegian identifiers such as fødselsnummer and D-numbers — and custom regular expressions for jurisdiction-specific patterns. The three-zone model maps onto the folder hierarchy: `data/raw/` contains data with identifiers and is never sent to the API; `data/interim/` contains pseudonymised or anonymised data and can be used for AI-assisted cleaning and variable construction; `data/processed/` contains fully anonymised analysis-ready data and can be used without restriction. Under GDPR, sending personal data to a cloud processor requires a data processing agreement with the provider; the hook approach prevents raw personal data from leaving the local machine at the raw data stage, avoiding that requirement for the most sensitive part of the workflow.

The three configurations described — the immutability rule, the accessibility-oriented script specification, and the PII hook — are instances of systematic AI authorship at the empirical level. Each is a documented, enforceable constraint: not a norm that depends on individual researcher vigilance in any given session but a structural feature of the project that holds across sessions regardless of how the tool is used on a particular day. It is worth stating explicitly that for projects involving personal data, systematic AI authorship is not merely epistemically preferable but, in this form, the legally required approach: sending raw participant files to a cloud API without screening, running undocumented analyses, and accepting AI-transformed data without verification is unaccountable and potentially a GDPR violation. The transparency artefacts for empirical work — analysis scripts, codebooks, data management protocols, and PII hook configuration — are submitted as part of the replication package alongside the project-level configuration files.

### Drafting, reviewing and adversarial configuration

By the time the drafting stage begins, substantial work has already been done: the outline has been developed and iterated, the literature has been searched and synthesised, any empirical analysis has been conducted and its results interpreted, and the main argument has been articulated. The drafting workflow draws on all of this as context. A skill-configured style profile encodes explicit criteria for sentence rhythm, hedging calibration, paragraph structure, and rhetorical stance. The skill specification is detailed enough to be evaluable: a reviewer reading the draft alongside the skill file can assess whether the style criteria were met, disagree with specific criteria, and suggest revisions to the configuration. The intellectual contribution lies in the skill specification and the accumulated project context, not in the draft text itself. All prompts, configurations, and session logs are retained.

Drafts produced by a configured skill are inputs to human revision, not outputs for direct use. The researcher reads, revises, accepts, or rejects each section, exercising the judgement that makes the output theirs. The skill enforces a consistent standard; the researcher enforces a consistent argument. These are different functions, and both are necessary. 

The drafting stage is an opportunity to engage with writing as a mode of thinking, not only as a vehicle for expressing ideas already formed. Writing forces deliberate semantics — the explicit structuring of logical relationships that tacit thought can leave implicit — and revision is a recursive process of discovery rather than polishing: the writer finds meaning by finding a structure that fits it (Emig, 1977; Sommers, 1981; Prain & Hand, 2016; Quitadamo & Kurtz, 2007). This is the hermeneutic circle between drafting, reviewing, and revising: each pass changes not only the text but the writer's grasp of the argument.

The same mechanism operates in the specification work that systematic AI use requires. Writing a screening rubric, an inclusion criterion, or a skill configuration is not clerical work; it engages deliberate semantics directly — the researcher must articulate in explicit, structured form what would otherwise remain a tacit evaluative standard. Through the act of writing the specification, the researcher often discovers that their prior criterion was ambiguous or inconsistently held; revising it in response is exactly the recursive discovery Sommers describes. This is the cognitive work that query authorship captures, and it is why systematic AI use does not bypass the deliberate semantics of writing but relocates them to the specification layer, where they simultaneously serve the argument and generate verifiable artefacts.  

I suggest an AI-supported review-and-revise stage that consists of three components, each addressing a failure mode the others do not.

The first is colleague review — the primary external check. The manuscript is sent to colleagues for human expert feedback. AI-assisted review is supplementary to this, not a substitute for it. What the structured approach provides is a better-prepared manuscript before it reaches human reviewers: weaknesses that would otherwise appear in referee reports are identified and addressed earlier, and the author arrives at the colleague-review stage with a more defensible draft. 

The second is a structured AI-reviewer skill run in a fresh session. Discipline-specific reviewer skills check for internal consistency, unresolved inferential gaps, and framing errors — not whether the argument is compelling but whether it is coherent. These configurations produce legible, actionable feedback organised by type of issue rather than an impressionistic sense of quality. The fresh-session requirement is critical: reviewing in a session with full prior project context biases the AI toward consistency and coherence with previous exchanges rather than independent critical assessment. A model that has been part of developing an argument is not in the same epistemic position as one encountering it for the first time. Fresh-session design approximates the position of an external reviewer encountering the work cold — which is the relevant epistemic standard.

Adversarial configuration addresses the sycophancy problem documented by Cheng et al. (2026). The empirical warrant for building this into the skill configuration rather than into individual prompts is sharpened by Asher et al. (2026): their finding that safety guardrails remain sensitive to framing rather than intent — the same outcome achieved by a direct request can be obtained through a reframed one — means that session-level prompting offers weaker protection than structural configuration. By explicitly instructing the reviewer skill to be critical, raise objections, and play devil's advocate — and by building these instructions into the persistent skill configuration rather than into individual prompts — the workflow encodes a structural countermeasure against confirmation bias. This is a concrete illustration of the systematic/unsystematic distinction: the same AI tool, identically prompted for content, produces epistemically different review outputs depending on whether its review behaviour has been explicitly configured to resist confirmation bias. The researcher using a default-mode AI review is exposed to systematically affirming feedback; the researcher whose reviewer skill specifies severity testing is not. The difference is in the configuration, not the content.

The third component is cross-model persona review. The same configured reviewer prompts — for this project, six personas calibrated to likely critical positions (for this paper, I specified these as a theoretical sociologist, a philosopher of mind, an applied microeconomist, a computational political scientist, a regulatory committee perspective, and a developer perspective) — are run in fresh sessions across at least two models from different developers. Different models have different training data, tendencies, and likely blind spots; one model's confirmation may reflect that model's biases rather than the argument's strength. A concern raised independently by two or more models is substantially more credible than the same concern raised by only one. Divergence across models on the same question is also informative: it signals where the argument is genuinely ambiguous rather than merely weak in one model's register. This functions as the review equivalent of a robustness check — not because any single AI review is decisive, but because convergence across independent systems is stronger evidence of a real weakness than any single system's output. One concern with AI-reviews is that LLMs tend to be too polite. You could also include a persona that is directly hostile, a toxic colleague or that like. (For this article, this was done after a couple of revisions, which proved surprisingly fruitful).   

The synthesis protocol for cross-model review is itself a documented artefact: act on objections raised independently by two or more models; flag for individual judgement objections raised by only one model; note model divergence as a signal of genuine ambiguity; disregard sycophantic positive feedback. The persona prompts and synthesis file are part of the replication package. The persona calibration is itself an instance of query authorship: each persona encodes a specific epistemic position structurally likely to resist the paper's argument from a direction the author cannot fully anticipate. The intellectual work is in designing those constraints; the model's output is execution within them. This is different from asking "what are the weaknesses of this paper?" — a generic question that produces generic feedback.

### Documentation

The documentation produced across all stages serves two distinct functions, addressed through two tiers of artefacts. The first tier consists of working logs — daily session records of decisions made, and paired author-input files — which document the process as it happened, including decisions revised and refined along the way. These are analogous to a lab notebook: their evidential weight lies in their contemporaneous character and in their recording of iterative process rather than end-state outcomes. The second tier consists of the supplementary materials presented at submission — skill files, prompt templates, search scripts, screening logs — in the form in which another researcher would need them to reproduce or evaluate the workflow.

Both tiers are present in the replication package because they serve different functions. This mirrors how pre-registration works: the registered plan and the final methods section each provide evidence the other cannot — the plan documents the prior commitment, the methods section specifies what was actually done. Neither substitutes for the other. The logs provide process integrity evidence; the supplement provides replicability materials. He et al. (2026), developing an accountability framework for automated ML research, independently arrive at a minimum artefact set — an objective sheet, program boundaries, a discovery trace, a verification ledger, a provenance bundle, and a role map — that maps closely onto what the two-tier documentation system produces. The convergence from a different discipline on the same structural requirements is indicative: the documentation logic is not sociology-specific but reflects a general accountability demand as AI systems take on larger shares of research execution.

The author-input files — first-person prose records of what the author brought to each session — serve a function analogous to authorship declarations in co-authored work. They document the intellectual origin of the work: which ideas and framings originated with the researcher, which redirections and corrections the researcher made to AI outputs, and which decisions originated with the researcher rather than from AI elaboration. Systematic AI authorship with author-input logging enables the kind of CRediT-style attribution that the existing authorship literature has advocated for collaborative research: transparent specification of who did what, and why.

It is now common that social science journals require a replication package as a condition of publication, understood as statistical code and data sufficient to reproduce reported results. For a paper using a systematic AI workflow, the transparency artefacts — skill files, prompt templates, search scripts, screening logs — serve the equivalent function. This is not a workaround: systematic AI authorship produces replication-ready materials as a natural byproduct of the workflow. The full replication package for this paper is available at https://github.com/torbskar/structured-use-of-AI; Appendix A provides curated excerpts for readers who want a rapid introduction without navigating the full repository.

The documentation described in this section does more than satisfy replication requirements. A search script, screening rubric, and reviewer configuration that are specified before outcomes are known — and retained — can be examined, challenged, and credited in ways that undocumented equivalents cannot. This is not merely an administrative property; it is an epistemic one. Section 5 examines what that property amounts to and why it matters beyond compliance.

---

## Epistemic properties of systematic use

The epistemic function of pre-registration is frequently misunderstood as a restriction: the researcher commits in advance and is not permitted to deviate. The more accurate description is externalisation: the researcher is required to articulate decisions — about design, measurement, analysis — before outcomes are known, which makes those decisions visible, challengeable, and creditable. Pre-registration does not improve research only by constraining it; it improves research by making tacit commitments explicit.

Systematic AI use functions the same way. To direct the AI, the context must be specified: before a search string is executed, the researcher must specify which concepts are to be included and excluded, what constitutes relevance, and how edge cases should be resolved; before a screening rubric is run, the researcher must articulate what the inclusion criteria are and why; before an analysis script is written, the researcher must specify which variables operationalise the theoretical concepts, which estimator suits the data structure, and how edge cases in variable construction should be handled; before a review prompt is submitted, the researcher must specify what standards of argument and evidence the work should meet. None of these specifications are novel — every careful researcher has views on these questions. Systematic use of AI forces their externalisation rather than their implicit deployment.

The tacit knowledge at issue is not the kind associated with expert craft skill — motor and perceptual knowledge that resists verbal articulation, which Mitchell et al. (2022) term inherent tacit knowledge (Polanyi 1966, Collins 2001). It is closer to what Mitchell et al. call implicit tacit knowledge: the scope commitments, theoretical priorities, and evaluative standards that a practitioner could articulate if prompted but rarely does because stating them would feel redundant to anyone sharing the disciplinary frame. Systematic AI use makes this knowledge explicit by requiring it to be encoded in a query, a rubric, or a configuration. The researcher who has never written out an inclusion criterion is forced to write one; the researcher who has never specified what "relevant" means is forced to specify it. This is not merely a transparency benefit — it is also a quality check, since the act of writing the criterion sometimes reveals that the criterion is unclear or inconsistently applied.

A related problem is what Gelman and Loken (2014) call the garden of forking paths: the cumulative effect of small, locally reasonable decisions that, undocumented, become invisible in hindsight. A researcher using AI without explicit criteria makes dozens of small acceptance decisions — this framing, this summary, this emphasis — each unremarkable in the moment and seemingly inevitable in retrospect. This is not dishonesty; it is the ordinary tendency to narrativise post hoc, which documented criteria at each stage are designed to prevent.

This is what *query authorship* amounts to. The query is not just an instruction; it is an intellectual contribution — an encoding of the researcher's theoretical commitments in a form that can be examined, challenged, revised, and credited. A well-formed search string embeds a theory of what the relevant literature is and why; a well-formed screening rubric embeds a theory of inclusion that reflects the paper's scope commitments; a well-formed analytical specification embeds a theory of measurement and causal structure; a well-formed reviewer configuration embeds standards of evaluation that the researcher would endorse under scrutiny. The argument that AI-assisted research is not "really" research because the AI wrote the text misses the point: the intellectual work is to a large extent in the query, and the query is authored by the researcher.

The idea that intellectual authorship resides in specification rather than execution is not new to sociology or to methodology. Abbott (2004) argues that the core creative act in social science is the heuristic move — the "gambit of imagination" that frames a problem, selects an angle, and constrains what follows — and that execution is not where the intellectual work sits. Krippendorff makes the same point from a methodological direction: rigorous coding instructions are designed so that coders are interchangeable, meaning the executor's identity should not affect the outcome, and the analyst's intellectual contribution is formalised in what he calls the analytical construct — the computable model of how the text relates to the research question. Krippendorff already extends this logic to computer-aided text analysis, where algorithms replace human coders; LLM query authorship is the next step in that lineage, not a departure from it. What changes with LLMs is not the principle but the failure modes of the executor: sycophancy, generalisation bias, and non-determinism mean that the relationship between specification and output is less stable than it is for a trained coder or a deterministic algorithm, and it is precisely this instability that makes the documentation and verification requirements specific to systematic AI use rather than a restatement of prior practice.

The pre-registration analogy and its disanalogy were noted above. Syed (2024) argues that a persistent misconception treats pre-registration as appropriate only for confirmatory experimental research; the epistemic argument for externalising decisions in advance applies equally to secondary data analysis, qualitative work, and literature synthesis. The same holds for systematic AI authorship. The key point is that the externalisation function — which is the epistemic core of pre-registration's value — is fully present in systematic AI authorship regardless of whether the initial commitment is public. Systematic specification of criteria before running the AI produces the externalisation benefit even without a timestamp. In principle, the working logs that record iterative process — including when criteria were changed and why — address the cherry-picking risk that pre-registration's public commitment eliminates through publicity.

### Systematic use as open science practice

The transparency artefacts produced by systematic AI use — skill files, prompt templates, boolean search strings, screening logs — have the formal properties open-science infrastructure already requires for other research outputs. They are shareable, versionable, independently evaluable, and capable of being deposited in a repository. A reviewer who receives a replication package containing a search script, a screening rubric, and a skill file can assess whether the inclusion criteria were explicit before the search, whether human verification checkpoints are recorded, and whether the search strings and screening decisions are reproducible from the submitted materials. This is the same evaluation that reviewers of quantitative replication packages perform with statistical code and data.

The Momeni et al. (2025) checklist for computational reproducibility in social science, developed with over 180 social scientists, covers data documentation, source sharing, and methodological reporting. Systematic AI use satisfies these requirements naturally — as a byproduct of the workflow, not as an additional burden. Törnberg's (2024) point about prompt stability analysis makes the same connection from a different angle: testing whether minor prompt changes alter results is only possible if prompts are documented. Systematic use makes this possibility available by default.

Freese and Peterson (2017) identify sociology's engagement with open science norms as incomplete; Systematic AI use, applied across the research pipeline — literature selection, analytical decision-making, conceptual development, argument review — produces exactly the kind of decision documentation that Freese and Peterson identify as missing.

### The reliability finding and its limits

Zeng et al. (2025) find, across 1,032 tasks in data science, that reproducibility correlates positively with accuracy: prompting strategies designed for reproducibility also produce better results on average. If this finding generalises, systematic use is not merely a transparency mechanism but a quality mechanism — a discipline that produces better outputs, not just more auditable ones. I suggest this is plausible: the same reasoning that produces a clear and specific inclusion criterion probably produces a better-executed search than vague prompting, just as the same reasoning that produces a legible research design probably produces better data collection than an undocumented one. The evidence from adjacent fields is consistent with there being no trade-off between reproducibility and quality.

This has not been demonstrated for sociology research specifically. The Zeng et al. finding comes from data science tasks that differ in important ways from qualitative and interpretive research. The claim here is more limited: systematic AI authorship is a necessary condition for the kind of quality control that makes errors detectable, and the adjacent evidence does not support the common assumption that reproducibility requirements trade off against quality. Whether systematic AI authorship improves average output quality in sociology is an open empirical question worth addressing when systematic use becomes sufficiently common to permit comparison.

### What systematic use cannot guarantee

It is worth distinguishing three levels at which systematic use bears on epistemic accountability. The first is what documentation _certifies_: that the criteria governing AI use were specified before the tool was run, not constructed post hoc to justify what it returned. Publicly timestamped documentation — a pre-registered protocol, or a project pushed to a public repository at the outset — provides stronger evidence of temporal priority than private logs, which, however contemporaneous, remain researcher-controlled. A documented inclusion criterion is evaluable; an undocumented one is not. The second is what documentation _makes possible but does not certify_: independent evaluation of whether the AI's execution of those criteria was accurate. A miscalibrated screening rubric can be identified and corrected — but only if the rubric exists to examine. Documentation is a prerequisite for this evaluation, not a guarantee that the evaluation was passed; its quality depends on the domain expertise and critical orientation of the researcher doing the verification. The third is what _no documentation regime can fully resolve_: non-deterministic AI outputs and the effect of model-version change on those outputs.

Systematic use does not guarantee high quality or eliminate errors. Documentation can still be faked by dishonest researchers, just as before. Open science practices and systematic AI use increase the likelihood that faked documentation is detected, since the artefacts produced are evaluable rather than merely asserted. He et al. (2026) frame the underlying problem precisely: output-only reporting is epistemically lossy because it conceals exactly where scientific judgment entered — discarded branches, failed reruns, and weak evidence absorbed into a smooth narrative they term fabricated closure. Working logs that record iterative process, including unsuccessful attempts, are the structural safeguard: substantially harder to retroactively sanitise than end-state outputs, and their inclusion in the replication package is what makes the documented process auditable rather than merely asserted. A genuine limitation is that the session logs described in this paper are manually written, which means their contemporaneous character depends on researcher diligence and they do not capture the LLM's reasoning process before each action. Singh (2026) describes a more technically reliable standard for that function: automated logging of the model's reasoning trace before each tool call, with machine-generated identity metadata and tamper-resistant command records. That infrastructure is not yet standard in academic research tools, and the three-file manual system is the available approximation.

Systematic use does not eliminate LLM error either; but it makes errors more visible and correctable. Any misclassification will be visible in the documented outputs and correctable through the human verification checkpoint. It cannot be ruled out that AI operating without explicit criteria may perform equally well on average — the reliability finding discussed earlier suggests it is unlikely — but its errors are less visible. The systematic user can discover and correct; it is much harder for the unsystematic user.

Non-determinism remains a practical challenge, and AI-generated text will not be reproducible verbatim. The same prompt, run twice at the same temperature setting, will almost certainly produce different outputs, but a systematic approach should put limits on how different they will be. Ideally, the *substantive* points will be similar. The appropriate response is not to treat this as a defeater for systematic use but to incorporate it into the documentation protocol: log outputs alongside prompts, note when re-runs produce substantively different results, and treat AI output as input to human judgement rather than as a final product. This is already standard practice in quantitative research when working with stochastic estimators.

The documentation should include the model version string alongside prompt templates and screening logs: the same workflow run against a later model version may produce substantively different outputs, and without the version string the documented process cannot be reproduced under equivalent conditions. Git commit timestamps provide contemporaneous process evidence that is substantially harder to fabricate than no record, though they fall short of a pre-registration server timestamp; researchers who want stronger integrity guarantees can push to a remote repository at project outset or register the project on OSF.

Systematic AI authorship is a necessary condition for epistemic soundness in AI-assisted research, not a sufficient one. The criteria encoded in a query may be poorly theorised; the human verification may be superficial — its quality depends on the researcher's domain expertise and genuine critical orientation, which the framework creates conditions for but cannot guarantee; the skill configuration may encode biases the researcher has not examined. These are real risks. The point is that systematic use makes them visible and therefore addressable — which unsystematic use does not.

The argument here is not that all AI use must be systematic, any more than the case for replication packages implies that all analysis must be automated. Researchers will continue to work exploratorily, to think while writing, and to let the process develop their thinking. What systematic AI authorship provides is not a constraint on how one works but evidence of how one worked. The same logic governs open science practices more broadly: if a hypothesis was not pre-registered, one must assume some degree of forking paths was possible; if code is not available, one must assume the study is not independently replicable; if AI workflow artefacts are not available, one must assume the process was unsystematic. These inferences are not certain, but the absence of evidence forces a conservative prior. The choice to work without producing accountability artefacts is a legitimate one; so is the reader's inference from their absence.

One scope note applies to this paper's own self-demonstration: the claim that the supplementary material package constitutes a proof of concept holds for the literature-review component, where search criteria and screening rubrics were pre-specified; the paper's conceptual contribution developed hermeneutically through the writing process and is accommodated by the spectrum framing of systematic use rather than by its narrow definition.

### Authorship criteria and the accountability threshold

Scholarly authorship has an established standard. The ICMJE criteria specify four requirements, all of which must be met: 1) substantial contributions to the conception or design of the work, or to the acquisition, analysis, or interpretation of data; 2) drafting or revising the work critically for important intellectual content; 3) final approval of the version to be published; and 4) agreement to be accountable for all aspects of the work, including the investigation of questions relating to accuracy or integrity. These criteria define the line between authorship and acknowledged contribution, and they already address AI authorship — negatively and decisively. AI cannot hold legal standing, cannot consent, and cannot agree to be accountable in any meaningful sense. Criteria 3 and 4 exclude AI from authorship categorically, without requiring philosophical claims about creativity or consciousness. The journals that prohibit AI authorship are correct; the criteria simply confirm it.

The more interesting question — and the one current policies do not ask — is what the ICMJE criteria imply for the human researcher in AI-assisted work. On criterion 1, query authorship maps directly: designing a search strategy, specifying inclusion and exclusion criteria, formulating synthesis questions, specifying an analytical model and variable construction rules, and configuring a reviewer skill are all acts of conception and design in the relevant sense. They encode the researcher's theoretical commitments and scope decisions. The difference systematic use makes is not in whether these contributions exist — any careful researcher makes them — but in whether they are documented and verifiable. Systematic AI authorship produces the evidence that criterion 1 is met; unsystematic use produces no such evidence and, if outputs are accepted without criteria-driven judgement, may not meet the criterion substantively.

Criterion 2 requires not merely drafting but reviewing the work critically — exercising intellectual judgement on the content. Author-input files are a direct instantiation of this criterion: they document, session by session, what the researcher directed, redirected, and rejected, distinguishing critical engagement from passive acceptance. This form of documentation is typically unavailable in traditional research. Criterion 3 — final approval — is formally met by any researcher who submits a manuscript. What systematic use adds is that the approval is *informed*: the researcher can trace the process that produced the version they approved, rather than endorsing an opaque product.

Criterion 4 is where the argument becomes sharpest. To be genuinely accountable for the work — able to investigate questions about accuracy and integrity, to explain why decisions were made, to show that the process was sound — the researcher must have access to the process that produced the work. Systematic AI authorship is designed to produce exactly this access: search strings, screening decisions, synthesis queries, and review configurations are documented and retained. The researcher who can point to these materials can investigate questions about accuracy in a way that an undocumented researcher — whether using AI or not — cannot.

The standard model of research accountability presupposes that the researcher knows what they did — can recall, reconstruct, or explain their process if questioned. This presumptive accountability is rarely documented and typically unavailable for independent investigation except through the researcher's own testimony. Systematic AI authorship, by producing a contemporaneous written record of decisions as they were made, does not rely on recall or reconstruction. The replication package and session logs constitute accountability that is structural rather than presumptive. This is not a claim to a stronger form of accountability than criterion 4 already requires; it is a claim about what criterion 4 requires in a situation its original drafters did not anticipate. Memory-based reconstruction satisfies criterion 4 for traditional research because the researcher executed the work and can answer for it from recall; where AI executed the work, the researcher did not, and recall alone cannot do the same epistemic job. The documentation framework provides the evidentiary supplement that makes criterion-4 accountability substantive rather than nominal. I am not claiming that AI-assisted research is better research than traditional undocumented research; the claim is about the evidentiary conditions under which accountability can be substantively exercised in each case. A well-executed traditional study with tacit but sound judgements is epistemically excellent; systematic AI authorship makes the soundness of those judgements demonstrable rather than presumed.

The ICMJE criteria give policy a more tractable question than "was AI used?" Given that researchers are already obligated to meet these criteria for any work they claim as their own, the relevant evaluative question for AI-assisted research is whether the process permits the researcher to demonstrate that authorship criteria are met — not whether AI appears in the acknowledgements. A documentation-based policy framework asks exactly this. Binary prohibition addresses the easy question (AI cannot be an author) while leaving the harder one unasked. Blanket disclosure answers neither question.

---

## Implications for journal policy

### What most common policies do

The response of journal editors and publishers to AI tools has been rapid and, in the context of genuine uncertainty, largely sensible. Journals needed to respond to real concerns: AI-generated text submitted as original work, undisclosed AI use in peer review, fabricated references and citations. One concern is that AI-generated texts might appear as good work, while in reality being of low actual quality. Papermills and questionable research practices were a concern before AI too, and AI makes it easier to produce bad research at scale. The policies developed in response — mandatory disclosure, prohibition of AI authorship, editorial screening for AI-generated content — address these concerns directly (Mondal et al., 2024; Ganjavi et al., 2024; Goyanes et al., 2025; da Veiga, 2025). The field has moved from silence to active guidance in under two years, which is fast for any institutional domain.

The guidance has converged on six themes across major publishers: requiring disclosure of AI use, prohibiting AI authorship, placing responsibility on corresponding authors, requesting transparency about what AI was used for, urging caution with AI-generated content, and specifying that human oversight is required (Mondal et al., 2024). These are reasonable minimum standards. The question I address here is not whether they are sensible but whether they are sufficient — and whether the binary structure they largely share is the right instrument for the problem.

### The problem with binary policies

A common policy structure is to rely on disclosure of whether AI was used or not. This has perhaps never been quite satisfactory, and a tiered disclosure has begun to emerge, by demanding task-specific disclosure (Jones 2025, Davidson & Karell 2025). Thus, the field might be moving in the direction of more specified documentation. SocArXiv's 2026 AI policy is a concrete illustration of this partial move and of its remaining gap. The policy states directly that "we are getting overrun with machine-generated slop, some of which is manipulative or fraudulent and some of which is very low quality," while acknowledging at the same time that "some real researchers are using LLMs and other automation tools to help do research" (SocArXiv, 2026). The permitted-use list distinguishes by task — literature searching and idea organisation with human verification are explicitly allowed; verbatim AI text generation and unreviewed outputs are not. This is meaningfully closer to the framework developed here than a binary disclosure requirement. Yet the systematic/unsystematic axis remains invisible: a researcher with a documented, criterion-governed literature search and one who accepted unverified outputs from an unconfigured chatbot both pass on the acceptable side of the same distinction. The policy asks what AI was used *for* but not whether that use was verifiable or criterion-governed. The paper's argument is not against disclosure, but that the systematic/unsystematic distinction is the axis along which more specified documentation should be organised, a distinction current policies leave invisible, with two divergent consequences.

The first is the inadvertent penalisation of systematic use. A researcher who built a documented, reproducible screening protocol with explicit inclusion criteria, logged outputs, and human verification checkpoints is treated, under current policies, identically to one who asked a general-purpose chatbot to summarise their references and accepted the output without review. Both used AI; both must disclose. The disclosure requirement captures nothing about the epistemic difference between the two cases.

The second is the permissiveness of disclosure as a standard. A statement that "AI was used to assist with analysis" gives readers no actionable information about whether the use was epistemically sound. Blanket permission with disclosure is not the same as permission for systematic use; it is permission for any use accompanied by a statement that AI was involved. The incentive structure this creates does not favour systematic use. The reflexivity literature has already named this failure mode in an adjacent context: a positionality statement that satisfies a formal requirement without informing the analysis is a performance rather than a practice (Sibbald et al., 2025). A disclosure that reports AI use without specifying the epistemic structure of that use has the same property. 

The query authorship argument has a direct implication here. If the intellectual contribution in AI-assisted research also lies in the query — the search string, the screening rubric, the reviewer configuration — then the relevant policy question is not "did you use AI?" but "can you show what intellectual commitments you encoded in the tool?" A disclosure requirement that asks only whether AI was used is not asking the right question.

Two practical complications compound this structural problem. First, restrictive binary policies face an inherent enforceability gap: AI detection tools are not sufficiently reliable to identify undisclosed AI use (Ganjavi et al., 2024), which means prohibitions function largely on author compliance rather than institutional verification — an enforcement mechanism that disadvantages honest actors while leaving dishonest ones undetected. Second, mandatory disclosure requirements may introduce systematic bias against non-native English speakers who use AI for linguistic polishing, since disclosure flags the use of AI assistance to reviewers in contexts where it would be invisible in polished prose from a native speaker (Ganjavi et al., 2024). Documentation-based policy handles both complications more cleanly, by directing evaluative attention to the intellectual content of the process rather than to whether any AI was used.

### A documentation-based alternative

I argue for a documentation-based framework as an alternative to the binary. The conservative framing of this argument is important: it requires no new principle and no new infrastructure. Journals that already require replication packages for quantitative work have already accepted the underlying logic: that research claims should be accompanied by the materials needed to verify how the analysis was conducted. For a study using regression, those materials are code and data. For a study using a systematic AI workflow, they are skill files, prompt templates, search scripts, screening logs, and — for empirical studies — analysis scripts and codebooks. This paper's replication package, available at the project repository and excerpted in Appendix A, illustrates what such a package looks like in practice. Journals that already require replication packages have the infrastructure — deposition workflows, editorial review procedures, and author guidance — that a documentation-based AI policy would use. Reproducibility of reported estimates and auditability of research process are distinct purposes, but the institutional machinery already exists for both.

In practice, this means that peer review of AI-assisted work should be able to evaluate the quality of the systematic process rather than simply its existence. Reviewers and editors should be able to assess that the configuration choices are theoretically justified and accountable. This requires familiarity with systematic AI workflows that most current reviewers do not have — but so did statistical code review before replication packages became standard, and that competence is now widely expected. Documentation norms create the incentive to acquire it. Davidson and Karell (2025) and Jones (2025) move in this direction, developing disclosure frameworks that specify what was done rather than merely whether AI was involved. The Generative AI Delegation Taxonomy (GAIDeT) represents a similar move toward tiered governance: it provides a structured vocabulary for documenting exactly which tasks — substantive or routine — were delegated to AI, and at what level of human oversight (Ganjavi et al., 2024). The documentation-based framework formalises and extends this emerging direction and connects it to the existing open-science infrastructure.

This approach shifts the evaluative burden to peer review, where it belongs. Reviewers can assess whether a systematic process was appropriate; they cannot currently assess whether an undocumented one was. Blanket restriction avoids the problem by eliminating the behaviour; documentation-based policy addresses it by making the behaviour evaluable. These are different kinds of solutions, and the second is more consistent with how academic knowledge validation normally works.

---

## Conclusion

I have argued that the systematic/unsystematic AI authorship distinction — not the use/non-use binary — is the epistemically relevant axis for evaluating and governing AI-assisted research. The distinction is not merely terminological. Systematic AI authorship is de facto an authorship contribution in its own right: the intellectual work lies in designing the query, the workflow, and the verification structure, not in the generated text. Unsystematic use, by contrast, is unaccountable not because it is careless but because the conditions for verifiability are absent. A binary policy that asks "did you use AI?" is answering the wrong question.

The concept of *query authorship* identifies the mechanism. The researcher's intellectual contribution in AI-assisted work lies in the criteria, configuration, and verification design — the search string that encodes a theory of relevance, the screening rubric that encodes scope commitments, the reviewer configuration that encodes evaluative standards. These commitments are authored by the researcher, not generated by the AI. Systematic use makes them explicit and verifiable; unsystematic use leaves them tacit and unauditable. The argument that AI-assisted research is not "really" research because the AI wrote the text misses this: the query is where the intellectual work sits, and it is attributable.

The transparency artefacts produced by systematic AI authorship — skill files, prompt templates, search scripts, screening logs, and session-by-session author-input records — have the formal properties that open-science infrastructure already requires for other research outputs. They are shareable, versionable, and independently evaluable. Author-input files, in particular, document the human intellectual origin of the work at each stage: which framings, arguments, and redirections originated with the researcher, and which with the AI. This is a function analogous to authorship declarations in co-authored work — a form of documentation typically unavailable in traditional research and directly relevant to the ICMJE criterion 4 requirement that the researcher be genuinely accountable for all aspects of the work. The replication package for a paper using this workflow is simultaneously a transparency artefact and a proof of concept: the documentation itself is the demonstration, and the replication package and Appendix A for this paper serve that function.

The policy directive follows from this. Journals should not ask "did you use AI?" — a question that is unenforceable, that treats systematic and unsystematic use identically, and that addresses the easy question (AI cannot be an author) while leaving the harder one (can the researcher demonstrate that authorship criteria are met?) unasked. The right question is: show us your systematic process. Operationally, this means extending existing replication package norms to AI-assisted workflows. For a study using regression, the replication package contains code and data. For a study using a systematic AI workflow, it contains skill files, prompt templates, search scripts, and screening logs. Journals that already require the former already have the infrastructure to require the latter. No new principle and no new infrastructure is needed.

The workflow described in the preceding sections is both argument and demonstration. The replication package for this paper — the project configuration files, search scripts, skill files, persona review prompts, and session-by-session author-input logs — is available in full at the project repository (https://github.com/torbskar/structured-use-of-AI), with curated excerpts in Appendix A. A reader can examine the systematic process, not merely read the account of it. Sociologists who build explicit search criteria, maintain screening logs, document analytical decisions, configure review tools against known failure modes, and record their iterative decision process are already doing open science. The gap is not in the infrastructure but in the policy framework that decides what counts as meeting the standard.

Whether systematic AI authorship also improves average output quality in sociology is an open empirical question — the Zeng et al. (2025) finding from data science suggests it is worth testing formally. But the case for adopting the documentation framework does not wait on that finding: the epistemic and policy arguments developed here stand on their own, and the infrastructure to implement them already exists.

--- 

## Acknowledgements

I am grateful for valuable comments on drafts of this article from my collages Lars-Erik Kjekshus, Alexi Gugushvili and Johan Fredrik Rye, and the almost daily discussions on AI with Torkild H. Lyngstad.  

---

## References

Abbott, A. (2004). _Methods of Discovery: Heuristics for the Social Sciences_. New York: W. W. Norton & Company.

Agha RA, Mathew G, Rashid R, Kerwan A, Al-Jabir A, Sohrabi C, Franchi T, Nicola M, Agha M, TITAN Group (2025). Transparency In The reporting of Artificial INtelligence — the TITAN guideline. *Premier Journal of Science*, 10, 100082. https://doi.org/10.70389/PJS.100082

Asher, S., Malzahn, J., Paschal, E., Persano, J., Myers, A. C. W., & Hall, A. B. (2026). Sycophancy and statistical analysis in large language models. Working paper. https://andrewbenjaminhall.com/asher_et_al_LLM_sycophancy.pdf

Barrie, C., Palmer, A., & Spirling, A. (2025). Replication for language models: problems, principles, and best practice for political science. Working paper. https://arthurspirling.org/documents/BarriePalmerSpirling_TrustMeBro.pdf

Blanchard, S. J., Duani, N., Garvey, A. M., Netzer, O., & Oh, T. T. (2025). New Tools, New Rules: A Practical Guide to Effective and Responsible Generative AI Use for Surveys and Experiments in Research. Journal of Marketing, 89(6), 119-139. https://doi.org/10.1177/00222429251349882 

Cheng, M., Jurafsky, D., et al. (2026). Sycophantic AI decreases prosocial intentions and promotes dependence. *Science*, *391*, eaec8352. https://doi.org/10.1126/science.aec8352

Collins, H. M. (2001). Tacit Knowledge, Trust and the Q of Sapphire. _Social Studies of Science_, _31_(1), 71-85. https://doi.org/10.1177/0306312010310010 

Davidson, T., & Karell, D. (2025). Integrating Generative Artificial Intelligence into Social Science Research: Measurement, Prompting, and Simulation. *Sociological Methods & Research*, *54*(3), 775–793. https://doi.org/10.1177/00491241251339184

Emig, J. (1977). Writing as a mode of learning. *College Composition and Communication*, *28*(2), 122–128. https://doi.org/10.58680/ccc197716382

Feuerriegel, S., et al. (2024). Generative AI. *Business & Information Systems Engineering*, *66*(1), 111–126. https://doi.org/10.1007/s12599-023-00834-7

Frankfurt, H. G. (2005). *On bullshit*. Princeton University Press.

Freese, J., & Peterson, D. (2017). Replication in social science. *Annual Review of Sociology*, 43, 147–165.

Ganjavi, C., Eppler, M. B., Pekcan, A., Biedermann, B., Abreu, A., Collins, G. S., Gill, I. S., & Cacciamani, G. E. (2024). Publishers' and journals' instructions to authors on use of generative artificial intelligence in academic and scientific publishing: bibliometric analysis. *BMJ*, 384. https://doi.org/10.1136/bmj-2023-077192

Gelman, A., & Loken, E. (2014). The statistical crisis in science. *American Scientist*, *102*(6), 460–465. https://doi.org/10.1511/2014.111.460

Goyanes, M., Lopezosa, C., & Piñeiro-Naval, V. (2025). The use of artificial intelligence (AI) in research: a review of author guidelines in leading journals across eight social science disciplines. *Scientometrics*, *130*, 3725–3741. https://doi.org/10.1007/s11192-025-05377-0

Grossmann, I., Feinberg, M., Parker, D. C., Christakis, N. A., Tetlock, P. E., & Cunningham, W. A. (2023). AI and the transformation of social science research. *Science*, *380*(6650), 1108–1109. https://doi.org/10.1126/science.adi1778

Gusenbauer, M., & Gauster, S. P. (2025). How to search for literature in systematic reviews and meta-analyses: A comprehensive step-by-step guide. _Technological Forecasting & Social Change_, _212_, 123833-. https://doi.org/10.1016/j.techfore.2024.123833

Hart, C. (2025). _Doing a literature review: releasing the research imagination_ (3rd edition). Sage. 

He, C., Zhou, X., Wang, D., Xu, H., Liu, W., & Miao, C. (2026). The AutoResearch moment: From experimenter to research director. Preprints.org. https://doi.org/10.20944/preprints202603.1329.v1

Hicks, M. T., Humphries, J., & Slater, J. (2024). ChatGPT is bullshit. *Ethics and Information Technology*, *26*(2), 38. https://doi.org/10.1007/s10676-024-09775-5

Holst, D., Moenck, K., Koch, J., Schmedemann, O., & Schüppstuhl, T. (2025). Transparent Reporting of AI in Systematic Literature Reviews: Development of the PRISMA-trAIce Checklist. *JMIR AI*, 4, e80247. https://doi.org/10.2196/80247

Jones, K. M. L. (2025). Generative AI in qualitative research and related transparency problems: a novel heuristic for disclosing uses of AI. *International Journal of Qualitative Methods*, *24*. https://doi.org/10.1177/16094069251404329

Korinek, A. (2023). Language models and cognitive automation for economic research. NBER Working Paper 30957. https://doi.org/10.3386/w30957

Kosch, T., & Feger, S. (2025). Prompt-hacking: The new p-hacking? ACM Reference Format, 1(1), 1–5. https://doi.org/10.1145/3744911

Krippendorff, K. (2019). _Content analysis: An introduction to its methodology_ (4th ed.). SAGE Publications. https://doi.org/10.4135/9781071878781

Ludwig, J., Mullainathan, S., & Rambachan, A. (2024). Large language models: an applied econometric framework. arXiv preprint 2412.07031.

Massimo A, Le Trang, Corrado C, Alessandra B, June C (2024). “openalexR: An R-Tool for Collecting Bibliometric Data from OpenAlex.” _The R Journal_, **15**, 167-180. ISSN 2073-4859, [doi:10.32614/RJ-2023-089](https://doi.org/10.32614/RJ-2023-089).

Mitchell, R. L. C., Holton, P., Chandola, T., Payne, J., Abell, J., & Ward, J. (2022). Where does all the 'know how' go? The role of tacit knowledge in research impact. *Higher Education Research & Development*, *42*(2). https://doi.org/10.1080/07294360.2021.1937066

Mondal, H., Mondal, S., & Behera, J. K. (2025). Artificial intelligence in academic writing: Insights from journal publishers' guidelines. *Perspectives in Clinical Research*, *16*(1), 56–57. https://doi.org/10.4103/picr.picr_67_24

Momeni, F., Khan, M. T., Kiesel, J., & Ross-Hellauer, T. (2025). Checklists for computational reproducibility in social sciences: insights from literature and survey evaluation. In *Proceedings of the 3rd ACM Conference on Reproducibility and Replicability (ACM REP '25)* (pp. 179–191). https://doi.org/10.1145/3736731.3746161

O'Grady, C. (2023). Honesty papers retracted for data 'discrepancies.' *Science*, *381*(6655), 255–256. https://doi.org/10.1126/science.adj8305

Peters, U., & Chin-Yee, B. (2025). Generalization bias in large language model summarization of scientific research. *Royal Society Open Science*. https://doi.org/10.1098/rsos.241776

Prain, V., & Hand, B. (2016). Coming to Know More Through and From Writing. _Educational Researcher_, _45_(7), 430-434. https://doi.org/10.3102/0013189X16672642

Polanyi M. (1966) _The Tacit Dimension_. Chicago: University of Chicago Press 

Quitadamo, I. J., & Kurtz, M. J. (2007). Learning to improve: Using writing to increase critical thinking performance in general education biology. *CBE—Life Sciences Education*, *6*(2), 140–154. https://doi.org/10.1187/cbe.06-11-0203

Retraction Watch. (2023, December 19). *Hindawi reveals process for retracting more than 8,000 paper mill articles*. https://retractionwatch.com/2023/12/19/hindawi-reveals-process-for-retracting-more-than-8000-paper-mill-articles/

Sibbald KR, Phelan SK, Beagan BL, Pride TM. Positioning Positionality and Reflecting on Reflexivity: Moving From Performance to Practice. _Qualitative Health Research_. 2025;0(0). doi:[10.1177/10497323241309230](https://doi.org/10.1177/10497323241309230)

Singh, K. (2026, February 25). Auditing and logging AI agent activity: A guide for engineers. LoginRadius Engineering Blog. https://www.loginradius.com/blog/engineering/auditing-and-logging-ai-agent-activity

SocArXiv. (2026, March 8). *AI policy*. Center for Open Science. https://socopen.org/ai-policy/

Sommers, N. (1981). Intentions and revisions. *Journal of Basic Writing*, *3*(3), 41–49. https://doi.org/10.37514/JBW-J.1981.3.3.05

Syed, M. (2024). Three persistent myths about open science. *Journal of Trial and Error*, *4*(2). https://journal.trialanderror.org/pub/three-persistent-myths/release/2

Törnberg, P. (2024). Best practices for text annotation with large language models. *Sociologica*, *18*(2), 67–85. https://doi.org/10.6092/issn.1971-8853/19461

da Veiga, A. (2025). Ethical guidelines for the use of generative artificial intelligence and artificial intelligence-assisted tools in scholarly publishing: a thematic analysis. *Science Editing*, *12*(1), 28–34. https://doi.org/10.6087/kcse.352

Xu, Y., & Yang, X. (2026). Scaling reproducibility: an AI-assisted workflow for large-scale replication and reanalysis. arXiv preprint 2602.16733.

Zeng, J., et al. (2025). AIRepr: an analyst-inspector framework for evaluating reproducibility of LLMs in data science. In *Findings of the Association for Computational Linguistics: EMNLP 2025*. https://aclanthology.org/2025.findings-emnlp.539/

Zrubka, Z., Kovács, L., Motahari Nezhad, H., et al. (2023). Artificial Intelligence in Medicine: A Systematic Review of Guidelines on Reporting and Interpreting Studies. Preprint. https://doi.org/10.21203/rs.3.rs-3430896/v1

---

*Draft v7 complete — 2026-04-28*



ewpage

# Appendix: Supplementary Materials — Illustrative Extracts

The extracts below are illustrative samples from the project's transparency artefacts. They are not exhaustive: the complete replication package — all R and Python scripts, skill configuration files, search logs, session decision records, and NotebookLM prompt templates — is available at https://github.com/torbskar/structured-use-of-AI. Together these materials constitute the transparency artefacts described in the paper: documented, shareable records of the choices made at each stage of the workflow. The extracts are presented in workflow order, from project configuration through literature search, AI tool configuration, synthesis protocol, and session logging.

---

## A. Project configuration

*Source: `CLAUDE.md` (project root)*

The root `CLAUDE.md` file functions as the project's standing instruction set — the document the AI assistant reads at the start of every session. It encodes the paper's epistemic commitments in operational terms, functioning analogously to a pre-registration document in that it fixes the framing, conceptual distinctions, and criteria before any analytic work begins. The following two sections are reproduced in full.

```
## Core argument

1. The structured/unstructured distinction — not AI use versus non-use — is the
   epistemically relevant axis for policy.
2. Structured AI use forces explicit articulation of tacit research decisions,
   functioning analogously to pre-registration.
3. This produces transparency artefacts (prompt templates, skill configurations,
   search logs) that are open-science compatible.
4. Current journal policies are blunt instruments that inadvertently penalise
   good practice.
5. A documentation-based policy framework is preferable to blanket restriction
   or blanket permission.

## Key conceptual distinctions (use consistently throughout)

- Structured use: tool configurations with explicit criteria, built-in human
  verification at each stage, documented outputs
- Unstructured use: accepting AI outputs without systematic verification or
  explicit criteria
- Skills / reviewer skills: configured AI personas with discipline-specific
  review criteria
- Transparency artefacts: prompt templates, skill files, search logs,
  NotebookLM source sets — shareable as supplementary materials
```

---

## B. Literature search pipeline

*Source: `literature/PIPELINE.md`*

The pipeline runs from OpenAlex database query to NotebookLM synthesis export across eight steps. The overview table below shows the full sequence; the two detailed extracts that follow show the human checkpoint at Step 4 and the thematic scoring criteria at Step 7. Human checkpoints (marked *[H]*) are built into the pipeline design: the workflow halts for manual review before proceeding, ensuring that automated decisions are subject to human verification.

### Overview

Full file paths are as documented in `literature/PIPELINE.md` in the project repository.

| Step | Script / action                          | Output                       |
| ---- | ---------------------------------------- | ---------------------------- |
| 1    | `search_openalex.R`                      | `combined_results.csv`       |
| 2    | `filter_results.py --extract`            | `filter_candidates.json`     |
| 3    | `screen_candidates.py`                   | `filter_decisions.json`      |
| 4    | `filter_results.py --apply`              | `openalex_retained.csv`      |
| 4    | *[H]* Spot-check excluded                | —                            |
| 5    | `download_pdfs.R`                        | `pdfs/[A–G]/`                |
| 5    | *[H]* Review missing PDFs                | —                            |
| 6    | `rename_pdfs.py --extract/--apply`       | renamed PDFs                 |
| 7    | `screen_fulltexts.py`                    | `fulltext_scores.csv`        |
| 7b   | `populate_upload_folders.py`             | `notebooklm/upload_[a/b/c]/` |
| 7b   | *[H]* Upload theme folders to NotebookLM | —                            |
| 7c   | *[H]* Write search summary report        | `search_summary_report.md`   |
| 8    | `export_notebooklm.py`                   | `notebooklm_export/`         |
| 8    | *[H]* Review composite export            | —                            |

### Step 4 — Apply filter decisions (human checkpoint)

```
Preview first:
    python scripts/filter_results.py --apply --dry-run

If reasonable, execute:
    python scripts/filter_results.py --apply

Outputs:
- literature/automated_literature_searches/openalex_retained.csv
- literature/automated_literature_searches/openalex_excluded.csv
- literature/automated_literature_searches/filter_tidying/filter_report.md

Human checkpoint: Spot-check ~30 records from openalex_excluded.csv for false
negatives before proceeding. If false negatives found, edit filter_decisions.json
and re-run --apply.
```

### Step 7 — Full-text relevance screening

Scores each PDF against three themes using weighted keyword matching on strategic page samples (first 3 pages + middle 2 pages + last 2 pages).

**Themes:**

| Theme | Description                                                         |
| ----- | ------------------------------------------------------------------- |
| A     | Structured / systematic AI use in research practice                 |
| B     | Explicit reasoning, pre-registration, open science, tacit knowledge |
| C     | Journal and publication policy on AI                                |

**Parameters:**

| Parameter   | Default           | Notes                |
| ----------- | ----------------- | -------------------- |
| `--top-n`   | 75                | Papers per theme CSV |
| `--pdf-dir` | `literature/pdfs` | Source PDF directory |

What to check: Open `fulltext_report.md` for an overview. Then open each theme CSV — the `hits_[a/b/c]` column shows which terms triggered the score, which helps identify false positives (high-scoring papers that are not actually relevant).

### Implementation for this paper

Three keyword searches were conducted using pre-specified boolean strings in OpenAlex via the `openalexR` package in R (Massimo et al., 2024), covering three topics: A) "Structured AI use in research practice"; B) "Explicit reasoning, pre-registration, open science"; and C) "Journal and publication policy on AI". This yielded 1,479 hits, of which 1,407 were retained after first screening of titles and abstracts. 1,205 full-text articles were successfully downloaded and screened. Full-text screening produced a ranked shortlist; the top-scored articles were loaded into NotebookLM for grounded synthesis (topic A: 48, topic B: 49, topic C: 46). Articles not retrievable by automation: the ten highest-ranked titles within each topic were manually located and added to the notebooks. A structured synthesis for each topic was exported from NotebookLM. A parallel semantic search using Elicit.com produced topic-level reports retained alongside the NotebookLM synthesis outputs as drafting materials.

Human verification took two forms: the top-scored papers were read independently of the AI synthesis, with discrepancies flagged and investigated; and synthesis outputs were cross-checked against the cited sources. All search strings, screening criteria, relevance scores, and synthesis queries are available in the project repository.

---

## C. Skill configuration

*Source: `supplementary/skills/lit-search/SKILL.md`*

A skill is a configuration file that encodes a workflow as an executable, repeatable set of instructions for the AI assistant. The extract below shows the frontmatter and first four steps of the literature search skill. The frontmatter specifies the trigger phrases that activate the skill and provides a description used by the assistant to recognise when the skill applies; the steps encode each stage of the pipeline with explicit decision rules and human checkpoints. Reviewer skills follow the same structure, substituting discipline-specific review criteria for search-step logic; the full reviewer skill configuration is available in the replication package.

```yaml
---
name: lit-search
description: >
  Run a structured literature search and screening pipeline for any research
  project. Use this skill whenever the user says /lit-search, "run the
  literature search", "start the search", "run the OpenAlex search", "execute
  the lit search", or wants to retrieve and filter academic literature. Runs
  search_openalex.R to query OpenAlex, screen_candidates.py for keyword-based
  abstract screening, download_pdfs.R to fetch open-access PDFs organised by
  search letter, screen_fulltexts.py for full-text scoring, and
  export_notebooklm.py for NotebookLM upload preparation. Human checkpoints
  after filtering and after download. All outputs go to literature/ in the
  project root. Run all scripts from the project root directory (not from
  scripts/).
---
```

```
## Step 1: Run OpenAlex search

    Rscript scripts/search_openalex.R

Output: literature/automated_literature_searches/combined_results.csv
Check the summary at the end of output: total records, records with abstracts,
records with OA URLs.

## Step 2: Prepare filter candidates

    python scripts/filter_results.py --extract

Output: literature/automated_literature_searches/filter_tidying/filter_candidates.json
Note the number of candidates printed to screen.

## Step 3: Abstract screening

    python scripts/screen_candidates.py

Applies keyword-based exclusion rules to all records and writes a decision for
each. RETAIN when in doubt — full-text screening (Step 7) handles precision.

Exclusion criteria — EXCLUDE if the title/abstract clearly indicates:
1. NLP/text processing as primary focus
2. School or K-12 context (unless about higher education or research practice)
3. AI affecting a non-research outcome (business productivity, HR, clinical
   diagnosis, etc.)
4. Big data/digitisation frame unrelated to research practice
5. Prediction or forecasting as primary purpose (ML as applied method)
6. Pedagogical effectiveness (AI improving student learning outcomes)

## Step 4: Apply filter decisions

Preview first:
    python scripts/filter_results.py --apply --dry-run

Human checkpoint: Spot-check ~30 records from openalex_excluded.csv for false
negatives before proceeding.
```

---

## D. NotebookLM synthesis protocol

*Source: `literature/notebooklm/notebooklm_summaries/notebooklm_report_B.md`*

The NotebookLM synthesis reports follow a structured query protocol. Standing instructions appear at the top of each report and apply to all subsequent queries; they specify citation requirements and impose a mandatory source-coverage check before synthesis begins. The Q0 query is submitted first in every notebook — it forces the AI to enumerate all uploaded sources and assess their relevance before any synthesis query is answered. This establishes which sources are available and confirms that none are silently ignored. The first six entries from the Q0 response in Notebook B (Theme: explicit reasoning, pre-registration, open science, tacit knowledge) are reproduced below.

### Standing instructions

```
STANDING INSTRUCTIONS — applies to all sections of this report:

This is a manual workflow. Submit each query (Q0, Q1, etc.) separately in
NotebookLM and paste the response into the corresponding section before
moving to the next query. Do not submit the whole document as a single prompt.

Citations: Every substantive claim must be cited in the text immediately after
the sentence it supports, using author-year format, e.g. (Smith et al., 2023).
If multiple sources support a claim, cite all of them. Do not group citations
at the end of a paragraph.

Source coverage: All sources in this notebook must be considered when answering
each query. Sources that are not informative for a given section should not
simply be ignored — they must be listed in the "Sources not drawn on" section
at the end of the report, with a brief explanation of why they did not
contribute (e.g. not relevant to the theme, too general, overlaps with a
stronger source, does not address the question asked).
```

### Q0 source-coverage check (query and excerpt from response)

```
Q0 — submit this exact text to NotebookLM before any other query:

> This notebook contains [N] sources. List ALL of them by title, one per line,
> numbered. For each, write one sentence on what it covers and whether it is
> relevant to open science, pre-registration, tacit knowledge, or the
> epistemology of research practice. Do not skip any source. If you cannot
> identify [N] distinct sources, say so explicitly and state how many you found.
>
> (Replace [N] with the actual number of sources uploaded before submitting.
> Later queries should reference: "drawing on all [N] sources listed in Q0,
> including those not yet cited in earlier sections.")

[Response excerpt — Notebook B, 46 sources confirmed:]

I have identified 46 distinct sources in this notebook. I could not identify a
47th distinct source based on the headers and metadata provided. The following
list identifies each source, summarizes its coverage, and specifies its
relevance to open science, pre-registration, tacit knowledge, or research
epistemology.

1. Cole et al. (2023): This source investigates enablers and barriers to
   reproducibility in qualitative research, focusing on the epistemological
   misalignment between open science practices and constructivist research
   paradigms.
2. Adjovi (2025): This bibliometric analysis tracks the worldwide production
   of research on ethics, providing a broad context for the sociological study
   of research integrity and responsibility in various disciplines.
3. Administrator (2024): This report audits current practices in human
   neuroscience, identifying how pre-registration and open science can guard
   against questionable practices like p-hacking and HARKing.
4. Van den Akker et al. (2023): This study assesses the practical value of
   pre-registration in psychology by comparing registered studies with
   equivalent non-registered ones to measure reporting consistency.
5. Al-Hoorie & Hiver (2021): This introduction to metascience in applied
   linguistics defines open science as transparency across the entire research
   process, covering open methods, reporting, and evaluation.
6. Torka et al. (2023): This paper addresses the low adoption rates of open
   science practices in management and organizational psychology, advocating
   for reform against publication bias and novelty-seeking.

[... 40 further entries ...]
```

---

## E. Session logs — three-file system

*Sources: `logs/CLAUDE.md`; `logs/2026-04-04-author-input.md`; `logs/2026-04-23-claude-contribution.md`*

Every session produces three log files: a decision log recording what was decided and the reasoning behind non-obvious choices; an author-input file recording the intellectual contributions of the human author in first-person prose; and a claude-contribution file recording the AI's intellectual contributions with initiative attribution. The protocol is specified in `logs/CLAUDE.md`; the two excerpt sections that follow show example entries from the first and last logged sessions.

### E1. Log format specification (from `logs/CLAUDE.md`)

```
Author-input file

Every session log must be accompanied by a paired YYYY-MM-DD-author-input.md
file. This file documents what the author brought to the session — ideas,
framings, arguments, redirections, and pushbacks — in first-person prose,
written as a contemporaneous record.

Purpose: To document the intellectual origin of the work. The decision log
records what was decided; the author-input file records who originated what.
This is essential for transparency about the human-AI division of labour and
defends against the criticism that the work is AI-generated rather than
AI-assisted.

Claude-contribution file

Every session log must also be accompanied by a YYYY-MM-DD-claude-contribution.md
file. This is the counterpart to the author-input file: it documents what Claude
contributed intellectually to the session, written in neutral third-person
academic register by Claude at the end of the session.

Purpose: To complete the transparency record of the human-AI division of
intellectual labour. The author-input file records the author's contributions;
this file records Claude's. Together they allow a full account of who originated
what — essential for query-authorship transparency and for any CRediT-style
disclosure.

What to include:
- Decisions Claude proposed and the reasoning behind them (only when non-obvious)
- Initiative attribution for each substantive contribution:
  "Initiated by author query" or "Claude initiative"
- Query-authorship annotations when the author's query itself was an intellectual
  contribution — a framing, criteria specification, diagnostic question, or
  structural insight: "Author query as intellectual contribution — [description]"
```

### E2. Author-input example (2026-04-04)

```
The core idea for this paper is mine. I had been working with structured AI
workflows in my own research for some time — building reviewer skills,
configuring tools for specific disciplinary standards, running the UiO guest
lecture on AI tools for sociology master's students — and I recognised that
what I was doing was methodologically distinct from the casual AI use that
journals were responding to with restrictive policies. The paper idea came from
that gap: sociology lacked a workflow paper written from inside the discipline
that could both describe what structured use looks like and make an argument
for why it matters.

[...]

A note on attribution that applies across this project: when I ask for advice
on a course of action, it is typically because I already have an idea and am
testing it before committing. The asking is itself an intellectual act — I have
identified the question, named the candidate solution, and am seeking an
assessment. The decision that follows is mine. This pattern is different from
the AI proposing something unprompted that I then adopt.
```

### E3. Claude-contribution example (2026-04-23)

```
## research-project-setup skill created

Skill architecture and content — Initiated by author query

*Author query as intellectual contribution — specified that the skill should
(a) cover CLAUDE.md subfolder splitting, skardhamar-style, naming conventions,
and literature search setup; (b) include logging, especially with a new
Claude-contribution file analogous to the author-input file; (c) treat queries
as intellectual contributions in accordance with query-authorship; and (d) check
existing state before asking targeted questions about gaps. This specification
determined the skill's scope, structure, and the conceptual distinction between
the three log file types.*

Proposed a plugin structure with SKILL.md, references/, and examples/ directories
following Claude Code's progressive disclosure design pattern. The references/
directory carries the detail (log formats, contribution guide, pipeline, project
structure templates) while SKILL.md stays lean (~1,800 words). This architecture
means the skill loads efficiently on trigger and pulls detail as needed.

## Three-file logging system formalization — Initiated by author query

*Author query as intellectual contribution — introduced the requirement for a
Claude-contribution file paired with the existing author-input file, and specified
that it should record decisions/reasoning and initiative attribution, treating
queries as intellectual contributions consistent with query-authorship.*

Designed the initiative attribution taxonomy (Initiated by author query / Claude
initiative) and the query-authorship annotation format. The annotation —
"Author query as intellectual contribution — [description]" — provides a specific
mechanism for documenting when the author's query was itself the intellectual
contribution rather than merely an instruction. This operationalizes
query-authorship within the transparency artefact system.
```

---

## G. Session metadata record

*Source: `logs/version-log.md` + `scripts/log_session_meta.sh`*

At the start of each session, a shell script logs the tool version and model identifier to a running version log. This record serves the same function as reporting a software version in a quantitative study: it specifies the conditions under which the documented outputs were produced. The AI model version is treated like a laboratory reagent or a specific release of Stata or R — a change in version is a change in the instrument, and outputs produced under different versions may differ. The following entry is representative; new entries are appended only when the version or model changes from the previous session.

```
## 2026-04-20 13:14

- Claude Code: 2.1.97 (Claude Code)
- Model:       default (see CLI version)
- Git commit:  3e85f13811c19c7dc1f2a67c71785d214445a8f9 (master)
```

The git commit hash links each version record to the exact state of all configuration files, scripts, and drafts at the time the session ran, providing an independent timestamp that is substantially harder to fabricate than a manually written date. The version log is included in the replication package alongside the session decision logs and author-input files.

---

## H. Full project folder structure

*Source: project root (agentic AI configuration)*

The simplified folder tree in the paper's workflow section shows only the content folders. The full structure below adds the configuration files used in an agentic AI setup (Claude Code). Subfolder context files are omitted here; they follow the same pattern as the root file and are available in the project repository.

```
project/
├── CLAUDE.md         ← project context; loaded automatically at session start
├── .claudedocs/      ← persistent cross-project instructions (style, epistemological commitments)
├── .claudeignore     ← paths excluded from AI context (data/raw/, credentials, git metadata)
├── .gitignore        ← paths excluded from version control (bulk PDFs, local AI state)
├── .git/             ← version control; commit history timestamps all file changes
├── data/
│   ├── raw/          ← original data; never AI-readable; immutable after receipt
│   └── processed/    ← analysis-ready files; script-generated only
├── scripts/          ← analysis code (R, Python, Stata)
├── outputs/          ← tables and figures; reproducible from scripts
├── literature/       ← search logs, source sets, syntheses
├── notes/            ← working notes and argument sketches
├── draft/            ← manuscript versions with full edit history
├── logs/             ← session decision logs and author-input files
└── supplementary/    ← replication package materials
```

Researchers using chat-only interfaces implement the same functions manually: the project context is pasted at session start rather than loaded automatically; access controls are maintained by folder discipline rather than enforced by the tool; and version control requires an explicit commit step rather than automatic tracking. The full agentic configuration, including `.claudeignore` specifications and the session-start protocol, is documented in the project repository at https://github.com/torbskar/structured-use-of-AI.

---

## F. Log index

*Source: `logs/log-index.md`*

The log index maintains a running table linking each session date to a one-line summary of key decisions. Each date has three associated files: a decision log, an author-input file, and a claude-contribution file, all named by date. Three rows are reproduced below; the full index covers all sessions from project initiation through final drafting.

| Date       | Key decisions                                                                                                                                                                                                        |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2026-04-04 | Paper type; target journal; core distinction; file structure; logging convention; three-stage screening protocol; lit-screen skill; string A screened (309→211)                                                      |
| 2026-04-05 | OpenAlex replaces Scopus/WoS; query authorship argument developed; target journal set to *Sociological Science*; full pipeline run (1,133 records → 300 exported); PIPELINE.md written; NotebookLM templates written |
| 2026-04-23 | research-project-setup skill created; logging system extended with claude-contribution file; log-index updated to four columns                                                                                       |

[^1]: The replication package for this paper consists of workflow artefacts — skill files, prompt templates, search scripts, screening logs, and author-input files — rather than statistical code and data. This is submitted as a methodological contribution to a journal whose mandatory replication package requirement (introduced April 2023) is itself an instance of the documentation norm the paper argues for.

[^2]: [ICMJE | Recommendations | Defining the Role of Authors and Contributors](https://www.icmje.org/recommendations/browse/roles-and-responsibilities/defining-the-role-of-authors-and-contributors.html)

[^3]: More elaborate practitioner implementations of the same structured approach exist. Sant'Anna (n.d.) describes a Claude Code research workflow featuring twenty-eight configured reviewer skills, fourteen specialised agents, automated quality gates, and AEA replication standards compliance, framed explicitly as a "ceiling, not floor" with documented entry points for new adopters (https://psantanna.com/claude-code-my-workflow/workflow-guide.html). The workflow described in this paper is intentionally minimal: the epistemic properties at issue — explicit criteria, human verification, and documented outputs — are present at any level of tooling complexity.

[^4]: https://github.com/torbskar/structured-use-of-AI
