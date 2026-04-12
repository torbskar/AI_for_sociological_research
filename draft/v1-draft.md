# Structured AI Use in Sociological Research

**Draft version:** v1  
**Date:** 2026-04-11  
**Status:** First full draft — all sections present; ready for review  
**Target:** Sociological Science — methodological contribution

---

## Abstract

The adoption of large language models in academic research has outpaced the development of frameworks for evaluating it. Current journal policies treat AI use as binary — permitted or prohibited, disclosed or not — but this framing misidentifies the epistemically relevant dimension. What matters is not whether AI was used but whether its use was structured: embedded in explicit criteria, subject to human verification, and producing documented outputs. I demonstrate a structured workflow for sociological research across the full research pipeline and argue that structured use instantiates the epistemic properties of open-science practice, particularly pre-registration's function of externalising tacit decisions. Central to the argument is the concept of query authorship: the intellectual contribution in AI-assisted research lies in the query — explicit criteria encoded in search strings, screening rubrics, and reviewer configurations — not in the generated text. I draw policy implications, arguing for a documentation-based framework that is both more epistemically honest and more consistent with existing open-science infrastructure than current binary approaches.

---

## 1. Introduction

The adoption of large language models in academic research has proceeded more quickly than the development of frameworks to evaluate it. Sociologists are using these tools — for literature review, coding, drafting, analysis — and the question is no longer whether but how. The institutional response has largely been binary: permit or prohibit, with disclosure requirements attached to the permissive end. This framing misidentifies the epistemically relevant dimension. What matters is not whether AI was used but whether its use was structured — embedded in explicit criteria, subject to human verification at each stage, and producing documented outputs.

This paper makes five connected moves. First, I develop the distinction between structured and unstructured AI use, arguing that the two differ not merely in transparency but in epistemic quality: structured use makes errors visible and correctable; unstructured use does not. Second, I introduce the concept of *query authorship* — the argument that formulating a search string, a screening rubric, or a review configuration encodes the researcher's intellectual commitments in a verifiable form, and that this constitutes the human contribution in AI-assisted research. Third, I demonstrate a structured workflow for sociology across the full research pipeline, from literature search through drafting and review to documentation. Fourth, I argue that structured AI use instantiates the epistemic properties of open-science practices — in particular, the function of pre-registration in forcing explicit commitment to decisions before outcomes are known. Fifth, I draw implications for journal policy, arguing that a documentation-based framework that asks researchers to show what they did is both more epistemically honest and more consistent with existing open-science infrastructure than policies that treat AI use as a binary.

The demonstration is itself an instance of the argument. The literature reviewed in this paper was identified through the documented pipeline described in §4: seven boolean search strings against the OpenAlex API, keyword-based abstract screening, full-text relevance scoring, and source synthesis via NotebookLM with queries grounded in uploaded sources. The scripts, search strings, screening decisions, and query logs are in the supplementary materials. A paper arguing for reproducible AI-assisted research practice is more credibly argued if the research practice producing it is reproducible.

A scope limitation, stated here rather than batched into a limitations section: the workflow demonstrated is for text-heavy, literature-based, and qualitative or mixed social science research. Quantitative primary data collection is not addressed in detail. The argument is scoped to sociology and adjacent social sciences where research questions, theoretical framings, and interpretive moves cannot be delegated to automated agents.

---

## 2. AI in research: the existing literature and the gap

### 2.1 What the literature covers

The rapid adoption of large language models across academic disciplines is by now well documented. Grossmann et al. (2023) identify AI as transforming scientific practice across fields; Korinek (2023) catalogues practical use cases for economists and social scientists; Feuerriegel et al. (2023) trace early adoption in information systems. The question of whether AI has entered research practice is settled. The question of what kind of practice it is entering has received less attention.

The dominant institutional response has been the reporting checklist — an instrument designed to improve transparency by specifying what authors must disclose about AI use after the research is done. These checklists have proliferated rapidly. Zrubka et al. (2025) systematically reviewed 24 such instruments and found that item counts range from 10 to 66, indicating that no consensus has emerged on what "full disclosure" even means. Among the most developed are PRISMA-trAIce (Holst et al., 2025) for systematic reviews, TITAN (Agha et al., 2025) for general academic purposes, and the clinical variants TRIPOD-LLM and CONSORT-AI. Publisher and journal guidance follows the same disclosure logic. Mondal et al. (2024) audited 20 major publishers and identified six converging themes across their AI policies — all centred on disclosure of AI use and attribution of responsibility, none on the epistemic structure of the research process itself. Ganjavi et al. (2024) and Goyanes (2025) extend this picture to the journal level.

Social science has developed some pipeline-oriented guidance. Törnberg (2024) addresses text annotation best practices and prompt stability analysis; Davidson and Karell (2025) provide a framing for integrating generative AI into social science research across measurement, prompting, and simulation tasks. Blanchard et al. (2025) offer the most complete practical pipeline found in the social science literature — reproducible prompt templates and pre-registration materials, developed for marketing research. From NLP and data science, Zeng et al. (2025) demonstrate that structured prompting designed for reproducibility also produces better results on average across a large sample of tasks — a suggestive finding for adjacent social science uses, though not directly transferable. Sociology-specific guidance, as distinct from the broader social science literature, is absent.

### 2.2 The gap

The checklist approach addresses one genuine problem: it creates a record of AI use that did not previously exist, enabling readers to assess what was done. I do not want to dismiss this contribution. The limitation is that checklists are post-hoc instruments: they assume the research process was already sound and ask only that the author report on it. A researcher could complete every item on PRISMA-trAIce while having used AI in a wholly unverifiable way. The checklist captures the end state; it has nothing to say about how that end state was produced.

No existing framework explicitly theorises the structured/unstructured distinction as the fundamental policy-relevant axis. Törnberg (2024) and Davidson and Karell (2025) both implicitly favour more systematic over less systematic AI use, but neither treats this distinction as the central policy question. No existing framework treats AI tool configuration — skill files, configured reviewer roles, system-level prompts — as an epistemic mechanism comparable to pre-registration. No existing work discusses the transparency artefacts produced by structured AI use (prompt templates, search logs, skill configurations) as components of a replication package. And no sociology-specific workflow framework of any kind exists.

A brief methodological note: the literature reviewed in this section was identified through the structured pipeline described in §4 — OpenAlex API searches across seven boolean strings, keyword-based abstract screening, full-text relevance scoring, and NotebookLM-assisted theme synthesis grounded in uploaded sources. The search strings, screening decisions, and relevance scores are in the supplementary materials. This means the literature review is itself an instance of the practice the paper defends. I note this not to sidestep the reflexive problem but to illustrate it: the same pipeline that locates the gap in the existing literature simultaneously occupies that gap.

---

## 3. The structured/unstructured distinction

### 3.1 What unstructured AI use looks like

Unstructured AI use is not defined by negligence. Most researchers who use AI tools unstructuredly are trying to do good work; the problem is that the conditions for verifiable good work are absent. The essential features are: prompting without explicit criteria, accepting outputs without systematic verification, and producing no documentation that would allow another researcher — or the same researcher at a later date — to reproduce or audit what was done.

The epistemic cost of this approach has been documented from several angles. Ludwig, Mullainathan and Rambachan (2024) show that seemingly innocuous choices — which model, which prompt formulation — can produce substantially different parameter estimates, and that these choices are rarely reported. Barrie et al. find that LLM performance variance is often unacceptably high even under controlled temperature settings; without logging, there is no way to know whether a given result would survive re-running. Cheng et al. (2026) demonstrate something more troubling: sycophantic AI responses — outputs calibrated to confirm rather than challenge user priors — systematically reduce independent judgment and promote dependence. The implication for research is that the failure mode in unstructured AI use is not random but directional. The AI is not simply noisy; it tends to confirm rather than challenge.

None of these problems are unique to AI. Undocumented manual coding, unreported variable transformations, and selective literature search are all unstructured in the same sense — they produce results that cannot be evaluated because the process that produced them is invisible. What AI introduces is scale: the range of judgements that can be delegated, and therefore potentially hidden, has expanded enormously. The structured/unstructured distinction is not a new principle; it is the application of an existing epistemic standard to a new tool.

### 3.2 What structured AI use looks like

Structured AI use has three defining features. The first is explicit criteria: the instructions given to the AI specify what to do and on what grounds — not "screen this abstract for relevance" but "retain this abstract if it addresses AI use in empirical research practice; exclude if it addresses only AI as a research subject, AI ethics in general, or K-12 education; retain in case of doubt." The second is human verification: at each stage where the AI produces an output, there is a specified human checkpoint where the output is evaluated against the criteria before it is used. The third is documented outputs: prompt configurations, screening rubrics, skill files, and decision logs are retained as artefacts that allow the process to be reconstructed and evaluated.

The concept of *query authorship* follows from this. Formulating a search string, a screening rubric, or a review configuration is an intellectual act — it encodes the researcher's theoretical commitments, scope decisions, and evaluative standards. These choices belong to the researcher, not the AI. The AI executes within them; the researcher authors them. Structured use makes this authorship explicit and verifiable. Unstructured use leaves it implicit, creating a false impression that the outputs emerged from the AI rather than from the researcher's intellectual commitments working through it. To be clear: unstructured use also involves intellectual choices; the point is not that structured use uniquely creates the researcher's contribution but that it documents and verifies it.

Structured use is also analogous to pre-registration, with an important qualification. Pre-registration forces explicit commitment to research design decisions before data are collected. Structured AI use forces explicit articulation of criteria before the tool is run — which search terms, which inclusion rules, which coding standards. The analogy holds in function: both prevent the post-hoc construction of criteria to justify what was already found. The qualification is that pre-registration is a public, timestamped commitment, while a structured AI protocol is initially private. This disanalogy is real but not fatal. The working logs maintained throughout structured use record the iterative process rather than just its end state — including when criteria were changed and why — and these logs are submitted with the replication package. The public commitment arrives at submission, as it does in registered reports.

### 3.3 Why the distinction matters

Epistemically, the core consequence is simple: structured use makes errors visible and correctable; unstructured use does not. A miscalibrated screening rubric in a documented, reproducible workflow can be identified, challenged, and corrected by a reviewer. An undocumented prompt cannot.

The existing literature has converged on reporting checklists as the response to this problem, and I have already acknowledged what these instruments achieve. Their limitation is different from what critics of AI in research sometimes suggest. The concern is not that checklists enable researchers to hide bad practice behind a disclosure form — most researchers using these instruments are acting in good faith. The concern is structural: checklists presuppose a prior question rather than answering it. They ask what was done; structured use determines whether what was done is evaluable. These are different moments in the research process, and addressing one does not substitute for the other.

The structured/unstructured axis is also orthogonal to the use/non-use axis that current policy focuses on. A researcher using AI in a structured and documented way may produce work that is more epistemically auditable than one who relies on undocumented, unreportable manual judgements — judgements about which abstracts are relevant, which sources are important, which arguments are coherent — that are equally invisible but have simply not attracted policy attention. The policy question is not, or should not be, whether AI was used, but whether what was done can be evaluated.

---

## 4. A structured workflow for sociology

### 4.1 Overview

The workflow described here has seven stages: literature search, candidate screening, full-text screening, source organisation and synthesis, drafting, review, and documentation. At each stage the structure is the same: explicit input criteria determine what the AI is instructed to do; a configured AI tool executes within those criteria; a human verification checkpoint evaluates the output before it passes to the next stage; and a documented artefact records what was done. The transparency artefacts produced across all stages — boolean search strings, screening rubrics, skill configurations, prompt templates, search logs, source set compositions, review records — constitute the replication package.

This is not an automated pipeline in the sense of Xu and Yang (2026), who demonstrate multi-agent systems capable of scaling well-defined computational tasks with minimal human input. That approach is effective where the research task is sufficiently specified that its execution can be delegated. Sociology research — formulating questions, selecting and interpreting evidence, constructing arguments — is not of that kind. The researcher is in the loop at every stage; the AI handles execution within explicitly defined criteria, and the researcher handles judgement. The distinction matters for both epistemic and methodological reasons: it is precisely this division of labour that makes the workflow's outputs attributable to the researcher.

### 4.2 Literature search and screening

The literature search for this paper was conducted via a two-route procedure. The primary route used the OpenAlex API, queried via R with seven boolean search strings documented in advance and archived in the supplementary materials. OpenAlex was chosen over licensed databases partly on legal grounds: institutional subscription agreements for bulk computational export vary and may not explicitly permit AI-assisted analysis, while OpenAlex's open API carries explicit research-use permission. The automated search returned 1,378 records after deduplication. Records were screened using a keyword-based exclusion script with explicit criteria — retain in case of doubt, exclude only for well-specified off-topic patterns — yielding 1,322 retained records at a 95.9% retention rate. Open-access PDFs were retrieved via Unpaywall for approximately 58% of retained records; full-text relevance scoring was applied across three themes. A secondary route used Elicit semantic searches and targeted manual retrieval to recover several papers that keyword searches missed. Both routes are documented in the supplementary materials.

Source synthesis used NotebookLM with queries submitted to notebooks containing only the relevant theme PDFs. The key design choice here is grounding: NotebookLM responds based on uploaded sources and cites them, in contrast to querying a general-purpose chatbot whose responses are ungrounded in any specific corpus and cannot be sourced. Each query was formulated to be explicit about what was being asked and why — what claims needed support, what distinctions mattered, what gaps should be named. This query formulation is an instance of query authorship: the intellectual work is in specifying what the synthesis should do, not merely in evaluating the text the AI produces.

Human verification at this stage takes two forms. First, the top-scored papers were read by the researcher independently of the NotebookLM synthesis, with discrepancies between the synthesis and the researcher's reading flagged and investigated. Second, synthesis responses were cross-checked against the uploaded sources using the inline citations NotebookLM provides — a feature that makes systematic misrepresentation of source content visible in a way that a general chatbot query does not.

### 4.3 Drafting

The drafting workflow uses a skill-configured AI persona — a style profile derived from close analysis of the author's prior published work, encoding explicit criteria for sentence rhythm, hedging calibration, paragraph structure, and rhetorical stance. The skill specification is detailed enough to be evaluable: a reviewer reading the draft alongside the skill file can assess whether the style criteria were met, disagree with specific criteria, and suggest revisions to the configuration. The intellectual contribution here lies in the skill specification, not in the draft text itself. All prompts, configurations, and session logs are retained.

A point worth making explicit: drafts produced by a configured skill are inputs to human revision, not outputs for direct use. The researcher who reads, revises, accepts, or rejects each paragraph is exercising the judgement that makes the output theirs. The skill enforces a consistent standard; the researcher enforces a consistent argument. These are different functions, and both are necessary.

### 4.4 Review and adversarial configuration

Structured review uses discipline-specific reviewer skills with explicit criteria. A social science article reviewer skill specifies what counts as a well-argued claim, a credible empirical warrant, a properly hedged conclusion. A logic and language reviewer skill checks for internal consistency, unresolved inferential gaps, and framing errors — not whether the argument is compelling but whether it is coherent. These configurations produce legible, actionable feedback organised by principle rather than an impressionistic sense of quality.

The adversarial configuration addresses the sycophancy problem documented by Cheng et al. (2026). By explicitly instructing the reviewer skill to be critical, raise objections, and play devil's advocate — and by building these instructions into the persistent skill configuration rather than into individual prompts — the workflow encodes a structural countermeasure against confirmation bias. This is a concrete illustration of the structured/unstructured distinction: the same AI tool, identically prompted for content, produces epistemically different review outputs depending on whether its review behaviour has been explicitly configured to resist confirmation bias. The researcher using a default-mode AI review is exposed to systematically affirming feedback; the researcher whose reviewer skill specifies severity testing is not. The difference is in the configuration, not the content.

### 4.5 Documentation and replication package

The documentation produced across all stages of the workflow is structured in two tiers. The first tier consists of working logs — daily session records and paired author-input files — which document the process as it happened, including decisions revised and refined along the way. These are analogous to a lab notebook: their evidential weight lies in their contemporaneous character and in their recording of iterative process rather than end-state outcomes. The second tier consists of the supplementary materials presented at submission — skill files, prompt templates, search scripts, screening logs — in the form in which another researcher would need them to reproduce or evaluate the workflow.

Both tiers are present in the replication package because they serve different functions. The logs provide process integrity evidence; the supplement provides replicability materials. This mirrors how pre-registration works: the registered plan and the final methods section are both legitimate, and neither substitutes for the other.

The author-input files — first-person prose records of what the author brought to each session — serve a function analogous to authorship declarations in co-authored work. They document the intellectual origin of the work: which ideas and framings originated with the researcher, which redirections and corrections the researcher made to AI outputs, and which decisions originated with the researcher rather than from AI elaboration. More generally, structured AI use with author-input logging enables the kind of CRediT-style attribution that the existing authorship literature has advocated for collaborative research: transparent specification of who did what, and why.

Sociological Science requires a replication package as a condition of publication, understood as statistical code and data sufficient to reproduce reported results. For a paper using a structured AI workflow, the transparency artefacts — skill files, prompt templates, R scripts, search logs — serve the equivalent function. This is not a workaround but a demonstration of the argument: structured use produces replication-ready materials as a natural byproduct.

---

## 5. Epistemic properties of structured use

### 5.1 The pre-registration analogy and query authorship

The epistemic function of pre-registration is frequently misunderstood as restriction: the researcher commits in advance and is not permitted to deviate. The more accurate description is externalisation: the researcher is required to articulate decisions — about design, measurement, analysis — before outcomes are known, which makes those decisions visible, challengeable, and creditable. Pre-registration does not improve research by constraining it; it improves research by making tacit commitments explicit.

Structured AI use functions the same way. Before a search string is executed, the researcher must specify which concepts are to be included and excluded, what constitutes relevance, and how edge cases should be resolved. Before a screening rubric is run, the researcher must articulate what the inclusion criteria are and why. Before a review prompt is submitted, the researcher must specify what standards of argument and evidence the work should meet. None of these specifications are novel — every careful researcher has views on these questions. What structured use forces is their externalisation rather than their implicit deployment.

The tacit knowledge at issue is not the kind Polanyi associated with expert craft skill — motor and perceptual knowledge that resists verbal articulation. It is closer to what might be called methodological tacit knowledge: the scope commitments, theoretical priorities, and evaluative standards that shape every research decision but are rarely stated because stating them would feel redundant to a practitioner who takes them for granted. Structured AI use makes this knowledge explicit by requiring it to be encoded in a query, a rubric, or a configuration. The researcher who has never written out an inclusion criterion is forced to write one; the researcher who has never specified what "relevant" means is forced to specify it. This is not merely a transparency benefit — it is also a quality check, since the act of writing the criterion sometimes reveals that the criterion is unclear or inconsistently applied.

This is what query authorship amounts to. The query is not just an instruction; it is an intellectual contribution — an encoding of the researcher's theoretical commitments in a form that can be examined, challenged, revised, and credited. A well-formed search string embeds a theory of what the relevant literature is and why; a well-formed screening rubric embeds a theory of inclusion that reflects the paper's scope commitments; a well-formed reviewer configuration embeds standards of evaluation that the researcher would endorse under scrutiny. The argument that AI-assisted research is not "really" research because the AI wrote the text misses the point: the intellectual work is in the query, and the query is authored by the researcher.

The pre-registration analogy has a known limitation, which I noted in §3.2 and will not repeat in full. What I add here is this: the externalisation function, which is the epistemic core of pre-registration's value, is fully present in structured AI use regardless of whether the commitment is initially public. The benefit follows from the act of articulation itself. The working logs that record iterative process — including when criteria were changed and why — address the cherry-picking risk that pre-registration's public commitment eliminates through publicity; the public commitment then arrives at submission, as it does in registered reports.

### 5.2 Structured use as open science practice

The transparency artefacts produced by structured AI use — skill files, prompt templates, boolean search strings, screening logs — have the formal properties open-science infrastructure already requires for other research outputs. They are shareable, versionable, independently evaluable, and capable of being deposited in a repository. A reviewer who receives a replication package containing a search script, a screening rubric, and a skill file can assess whether the inclusion criteria were explicit before the search, whether human verification checkpoints are recorded, and whether the search strings and screening decisions are reproducible from the submitted materials. This is exactly what reviewers of quantitative replication packages do with statistical code and data.

The Momeni et al. (2025) checklist for computational reproducibility in social science, developed with over 180 social scientists, covers data documentation, source sharing, and methodological reporting. Structured AI use satisfies these requirements naturally — as a byproduct of the workflow, not as an additional burden. Törnberg's (2024) point about prompt stability analysis makes the same connection from a different angle: testing whether minor prompt changes alter results is only possible if prompts are documented. Structured use makes this possibility available by default.

Freese and Peterson (2017) identify sociology's engagement with open science norms as incomplete and point to the documentation of qualitative and interpretive decisions as a persistent gap. Structured AI use, applied to the qualitative and interpretive stages of sociological research — literature selection, conceptual development, argument review — produces exactly the kind of decision documentation that Freese and Peterson identify as missing.

### 5.3 The reliability finding and its limits

Zeng et al. (2025) find, across 1,032 tasks in data science, that reproducibility correlates positively with accuracy: prompting strategies designed for reproducibility also produce better results on average. If this finding generalises, structured use is not merely a transparency mechanism but a quality mechanism — a discipline that produces better outputs, not just more auditable ones. I suggest this is plausible: the same reasoning that produces a clear and specific inclusion criterion probably produces a better-executed search than vague prompting, just as the same reasoning that produces a legible research design probably produces better data collection than an undocumented one. The evidence from adjacent fields is consistent with there being no trade-off between reproducibility and quality.

I cannot claim to have demonstrated this for sociology research specifically. The Zeng et al. finding comes from data science tasks that differ in important ways from qualitative and interpretive research. The claim I make here is more limited: structured use is a necessary condition for the kind of quality control that makes errors detectable, and the adjacent evidence does not support the common assumption that reproducibility requirements trade off against quality. Whether structured use also improves average output quality in sociology is an open empirical question worth addressing in future work.

### 5.4 What structured use cannot guarantee

Structured use does not eliminate LLM error; it makes errors visible and correctable. The AI operating within an explicit screening rubric may still systematically misclassify certain types of abstract — but the misclassification will be visible in the documented outputs and correctable through the human verification checkpoint. The AI operating without an explicit rubric may perform equally well on average, but its errors are invisible. The structured user can discover and correct; the unstructured user cannot.

Non-determinism remains a practical challenge. The same prompt, run twice at the same temperature setting, may produce different outputs. The appropriate response is not to treat this as a defeater for structured use but to incorporate it into the documentation protocol: log outputs alongside prompts, note when re-runs produce substantively different results, and treat AI output as input to human judgement rather than as a final product. This is already standard practice in quantitative research when working with stochastic estimators.

Structured use is a necessary condition for epistemic soundness in AI-assisted research, not a sufficient one. The criteria encoded in a query may be poorly theorised; the human verification may be superficial; the skill configuration may encode biases the researcher has not examined. These are real risks. The point is that structured use makes them visible and therefore addressable, in a way that unstructured use does not.

---

## 6. Implications for journal policy

### 6.1 What current policies do

The response of journal editors and publishers to AI tools has been rapid and, in the context of genuine uncertainty, largely sensible. Journals needed to respond to real concerns: AI-generated text submitted as original work, undisclosed AI use in peer review, fabricated references and citations. The policies developed in response — mandatory disclosure, prohibition of AI authorship, editorial screening for AI-generated content — address these concerns directly (Mondal et al., 2024; Ganjavi et al., 2024). The field has moved from silence to active guidance in under two years, which is fast for any institutional domain.

The guidance has converged on six themes across major publishers: requiring disclosure of AI use, prohibiting AI authorship, placing responsibility on corresponding authors, requesting transparency about what AI was used for, urging caution with AI-generated content, and specifying that human oversight is required (Mondal et al., 2024). These are reasonable minimum standards. The question I address here is not whether they are sensible but whether they are sufficient — and whether the binary structure they share is the right instrument for the problem.

### 6.2 The problem with binary policies

Current policies treat AI use as a binary: used or not used, disclosed or not disclosed. This structure leaves the structured/unstructured distinction invisible, with two problematic consequences that work in opposite directions.

The first is the inadvertent penalisation of structured use. A researcher who built a documented, reproducible screening protocol with explicit inclusion criteria, logged outputs, and human verification checkpoints is treated, under current policies, identically to one who asked a general-purpose chatbot to summarise their references and accepted the output without review. Both used AI; both must disclose. The disclosure requirement captures nothing about the epistemic difference between the two cases.

The second is the permissiveness of disclosure as a standard. A statement that "AI was used to assist with analysis" gives readers no actionable information about whether the use was epistemically sound. Blanket permission with disclosure is not the same as permission for structured use; it is permission for any use accompanied by a statement that AI was involved. The incentive structure this creates does not favour structured use.

The query authorship argument has a direct implication here. If the intellectual contribution in AI-assisted research lies in the query — the search string, the screening rubric, the reviewer configuration — then the relevant policy question is not "did you use AI?" but "can you show what intellectual commitments you encoded in the tool?" A disclosure requirement that asks only whether AI was used is not asking the right question.

### 6.3 A documentation-based alternative

I argue for a documentation-based framework as an alternative to the binary. The conservative framing of this argument is important: it requires no new principle and no new infrastructure. Journals that already require replication packages for quantitative work — including Sociological Science, whose replication package requirement has been mandatory since April 2023 — have already accepted the underlying logic: that research claims should be accompanied by the materials needed to verify how the analysis was conducted. For a study using regression, those materials are code and data. For a study using a structured AI workflow, they are skill files, prompt templates, search scripts, and screening logs. Journals that apply the replication package norm to quantitative work face a consistency challenge in treating AI workflow documentation differently.

In practice, this means that peer review of AI-assisted work should evaluate the quality of the structured process rather than simply its existence. Reviewers should be able to assess whether inclusion criteria were specified before the search was run, whether human verification checkpoints are recorded at each stage, whether the search strings and screening decisions can be reproduced from the submitted materials, and whether the configuration choices made — which criteria, which thresholds, which review standards — are theoretically justified. Davidson and Karell (2025) and Jones (2025) move in this direction, developing disclosure frameworks that specify what was done rather than merely whether AI was involved. The documentation-based framework formalises this move and connects it to the existing open-science infrastructure.

This approach shifts the evaluative burden to peer review, where it belongs. Reviewers can assess whether a structured process was appropriate; they cannot currently assess whether an undocumented one was. Blanket restriction avoids the problem by eliminating the behaviour; documentation-based policy addresses it by making the behaviour evaluable. These are different kinds of solutions, and the second is more consistent with how academic knowledge validation normally works.

---

## 7. Conclusion

I have argued for three things. First, that the structured/unstructured distinction — not the use/non-use binary — is the epistemically relevant axis for evaluating AI-assisted research. Second, that structured AI use has the properties of open-science practice: it forces explicit articulation of tacit decisions, produces documented artefacts that can be independently evaluated, and makes errors visible and correctable. Third, that current journal policy — whatever its other merits — fails to recognise this distinction, inadvertently treating epistemically sound practice identically to epistemically unsound practice.

The concept of query authorship is central to all three. If the researcher's intellectual contribution in AI-assisted work is not the generated text but the intellectual commitments encoded in the query — the search criteria, the screening standards, the evaluative configuration — then documentation of those commitments is both possible and sufficient to attribute the work appropriately. This changes what academic integrity means in the context of AI use: not "did a human write this text?" but "can we verify what intellectual commitments shaped this output?" The first question has no good answer in a world where AI tools are routinely used for drafting and editing. The second is answerable, auditable, and consistent with the methods-disclosure norms sociology already applies to its quantitative and qualitative work.

Sociologists who build explicit search criteria, maintain screening logs, configure review tools against known failure modes, and document their iterative decision process are already doing open science. The infrastructure to recognise this already exists — replication packages, preregistration servers, open data repositories, ORCID and CRediT attribution standards. The gap is not in the infrastructure but in the policy framework that decides what counts as meeting the standard. Extending documentation norms to AI-assisted workflows requires journals to ask a different question of authors: not "did you use AI?" but "here is what a structured process looks like — show us yours." That is a tractable request, and it is more useful than either blanket prohibition or blanket disclosure.

The open empirical question is whether structured AI use also improves average output quality in sociology research — the Zeng et al. (2025) finding from data science suggests this is worth testing formally. I suggest this as the next methodological priority for the field: replication studies comparing structured and unstructured AI use across standard sociology research tasks, designed to test the quality hypothesis rigorously. That work will strengthen the argument made here. It is not required to begin adopting the documentation framework.

---

## References

*To be completed from `literature/openalex_retained.csv` and manual retrieval list before submission.*

Barrie, C., et al. — [full reference needed; LLM performance variance]  
Blanchard, S. J., et al. (2025). — [full reference needed; Journal of Marketing pipeline]  
Cheng, M., et al. (2026). — [full reference needed; sycophancy, *Science*]  
Davidson, T., & Karell, D. (2025). — [full reference needed; *Sociological Methods & Research*]  
Feuerriegel, S., et al. (2023). — [full reference needed; early AI adoption in information systems]  
Freese, J., & Peterson, D. (2017). Replication in social science. *Annual Review of Sociology*, 43, 147–165.  
Ganjavi, C., et al. (2024). Publishers' and journals' instructions to authors on use of generative artificial intelligence in academic and scientific publishing: bibliometric analysis.  
Goyanes, M. (2025). — [full reference needed; journal-level author guidelines survey]  
Grossmann, I., et al. (2023). — [full reference needed; *Science*, AI transforming research]  
Holst, C., et al. (2025). PRISMA-trAIce. — [full reference needed]  
Jones, P. (2025). — [full reference needed; qualitative AI disclosure heuristic]  
Korinek, A. (2023). — [full reference needed; NBER working paper, LLMs for economists]  
Ludwig, J., Mullainathan, S., & Rambachan, A. (2024). — [full reference needed; prompt choice and parameter estimates]  
Mondal, H., et al. (2024). — [full reference needed; publisher guidelines audit, 20 publishers]  
Momeni, F., et al. (2025). — [full reference needed; computational reproducibility checklist, social science]  
Törnberg, P. (2024). — [full reference needed; text annotation, prompt stability]  
Xu, Y., & Yang, X. (2026). — [full reference needed; arXiv 2602.16733, multi-agent replication pipeline]  
Zeng, J., et al. (2025). — [full reference needed; AIRepr, reproducibility correlates with accuracy]  
Zrubka, M., et al. (2025). — [full reference needed; systematic review of 24 AI reporting guidelines]  

---

*Draft v1 complete — 2026-04-11*
