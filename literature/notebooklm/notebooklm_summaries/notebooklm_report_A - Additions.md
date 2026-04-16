# NotebookLM Synthesis Report — Notebook A

## Theme: Structured and unstructured AI use in research practice

**Date:**
**Sources:** [N] PDFs, Theme A top 50
**Configuration:** `supplementary/example-notebooklm-configuration.md`

---

**STANDING INSTRUCTIONS — applies to all sections of this report:**

*This is a manual workflow. Submit each query (Q0, Q1, etc.) separately in
NotebookLM and paste the response into the corresponding section before
moving to the next query. Do not submit the whole document as a single prompt.*

*Citations:* Every substantive claim must be cited in the text immediately
after the sentence it supports, using author-year format, e.g. (Smith et al.,
2023). If multiple sources support a claim, cite all of them. Do not group
citations at the end of a paragraph.

*Source coverage:* All sources in this notebook must be considered when
answering each query. Sources that are not informative for a given section
should not simply be ignored — they must be listed in the "Sources not drawn
on" section at the end of the report, with a brief explanation of why they
did not contribute (e.g. not relevant to the theme, too general, overlaps
with a stronger source, does not address the question asked).

---

## 0. Source coverage check

*Q0 — submit this exact text to NotebookLM before any other query:*

> This notebook contains [N] sources. List ALL of them by title, one per line,
> numbered. For each, write one sentence on what it covers and whether it is
> relevant to AI use in academic research. Do not skip any source. If you
> cannot identify [N] distinct sources, say so explicitly and state how many
> you found.

*(Replace [N] with the actual number of sources uploaded before submitting.
This forces NotebookLM to register the full source set. Later queries should
reference: "drawing on all [N] sources listed in Q0, including those not yet
cited in earlier sections.")*

1. **Large language models show human-like content biases in transmission chain experiments**: This source examines how ChatGPT-3 reflects human cultural transmission biases such as gender stereotypes, which is relevant to academic research as these biases can distort AI-generated text and summaries.
2. **How should the advancement of large language models affect the practice of science?**: This article presents multiple perspectives on LLMs potentially serving as scientific collaborators or assistants, highlighting their relevance for facilitating tasks like coding and drafting while warning about threats to research integrity.
3. **The Integration of Generative AI Tools in Academic Writing: Implications for Student Research**: This paper explores how generative AI can assist students with literature reviews, data analysis, and thesis organization, arguing that its responsible use is essential for modern academic training.
4. **Can Generative AI improve social science?**: This source argues that generative AI can enhance social science by simulating human behavior and automating text analysis, but it notes relevance to research caution due to opaque training processes and algorithmic bias.
5. **Do large language models have a legal duty to tell the truth?**: This research discusses "careless speech" in LLMs and is relevant to academic research because it examines how subtly incorrect AI outputs can cumulatively degrade shared social truths and scientific knowledge.
6. **Generalization bias in large language model summarization of scientific research**: This study demonstrates a strong bias in LLMs toward overgeneralizing scientific findings, making it highly relevant to researchers who must be wary of misinterpreting data when using AI for summarization.
7. **Investigating the replicability of the social and behavioural sciences**: This article details a massive replication effort that utilized LLMs to automatically identify and summarize the methods and theoretical frameworks of thousands of papers, demonstrating a practical application of AI in meta-scientific research.
8. **Prompts, Pearls, Imperfections: Comparing ChatGPT and a Human Researcher in Qualitative Data Analysis**: This source compares the ability of AI and humans to identify themes in qualitative transcripts, concluding that AI is relevant as a fast, augmentative research tool but lacks the necessary human reflexivity for deep analysis.

---

## 1. Landscape of positions

*Q1–3: What is the overall stance toward AI use in research — encouraging, discouraging, conditional? What reasons are given for caution? What benefits are identified and for which tasks? Draw on all sources from Q0.*

The overall stance toward AI use in research across the sources is **predominantly conditional**, characterized by a tension between its transformative potential and significant risks to scientific integrity. While some perspectives are **highly encouraging**, viewing AI as a "knowledgeable research assistant" or "collaborator", others are **strongly cautionary or discouraging**, arguing that AI generates "form without substance" and threatens the social nature of scientific expertise.

### **Reasons for Caution**

The sources identify several critical risks that necessitate human oversight:

* **Algorithmic and Human Biases:** LLMs tend to reproduce and magnify human cultural transmission biases, such as **gender stereotypes**, and exhibit a "common token bias" that favors majority views over minority or marginalized perspectives.
* **Generalization Bias:** A strong tendency in LLMs to **overgeneralize scientific findings**, broadening conclusions beyond what the original data supports, which can lead to large-scale misinterpretations of research.
* **"Careless Speech" and Hallucinations:** AI often produces "careless speech"—plausible and confident text that contains **factual inaccuracies, fabricated citations, or misleading references**.
* **Opacity and Reliability:** The "black box" nature of proprietary models makes it difficult to verify source data or ensure **reproducibility**, as model outputs can change over time without warning.
* **Lack of Accountability:** Because AI lacks intentionality and "personhood," it cannot be held accountable for scientific errors; the **legal and ethical responsibility** remains solely with the human researcher.

### **Identified Benefits and Tasks**

Despite these cautions, the sources identify substantial benefits for increasing the **scale, scope, and speed** of research:

* **Literature and Text Summarization:** AI is highly efficient at searching, identifying, and summarizing vast bodies of literature, which helps researchers manage "onerous" amounts of information.
* **Writing and Editing Assistance:** Tasks include **drafting introductions**, correcting grammar and syntax, translating academic articles for better comprehension, and aligning text with formatting standards like APA.
* **Data Analysis and Coding:** AI can automate **text analysis (coding)**, identify themes in qualitative transcripts, and organize complex datasets.
* **Scientific Discovery and Simulation:** Benefits include **generating new leads** for mathematicians, predicting protein structures, and creating "silicon samples" to simulate human behavior in social science experiments.
* **Meta-Scientific Research:** Large-scale efforts like the SCORE program utilized LLMs to automatically identify **theoretical frameworks and statistical methods** across thousands of abstracts to evaluate replicability.
* **Teaching and Training:** AI can serve as a "tutor" or "simulator" to help students practice interview probing techniques or understand complex academic concepts.

**Author notes:** *[Tensions, surprises, follow-up items.]*

---

## 2. Conditions and requirements

*Q4: Do any sources specify conditions for acceptable AI use — disclosure, verification, prompt documentation, human oversight, task restrictions?*

Yes, several sources specify explicit conditions and best practices for the acceptable use of AI in academic research. These conditions emphasize that **the human researcher must remain the central authority and moral agent** in the scientific process.

### **Disclosure and Transparency**

Sources emphasize that researchers have a duty to be open about how AI is integrated into their work:

* **Transparent Attribution:** Authors should **explicitly state which LLMs were used and for what purpose**, either within the method section or a dedicated statement.
* **Citing AI Content:** Any ideas or text generated by AI must be **properly cited** to avoid academic dishonesty.
* **Version and Time Reporting:** Because models change over time ("drift"), researchers should report the **exact version of the model and the date of analysis**.
* **Watermarking:** The EU AI Act includes requirements for **watermarking** AI-generated content and informing users when they are interacting with a chatbot.

### **Verification and Accuracy**

The sources treat verification as a non-negotiable prerequisite for AI use:

* **Fact-Checking:** Researchers must **verify all AI-generated outputs against original academic sources**. This is critical because LLMs are "incidental truth-tellers" and frequently fabricate citations.
* **Standardized Quality Criteria:** A "good practice" is to define **clear quality criteria and verification methods _before_ using LLMs** to ensure the time saved in generation isn't lost during the vetting process.
* **Conservative Technical Settings:** To mitigate "generalization bias" in scientific summaries, researchers should use **lower temperature settings** (ideally 0) to make outputs more deterministic and faithful to the source material.

### **Prompt Documentation**

Documenting the interaction between the human and the machine is recommended for reproducibility:

* **Public Release of Prompts:** In the spirit of open science, researchers should **publicly release their prompts and the corresponding LLM responses** as supplementary materials.

### **Human Oversight and Responsibility**

Human control is described as the primary safeguard against the degradation of research integrity:

* **Human-in-the-Loop:** Humans must guide the AI process, **correct errors**, and ultimately decide which ideas warrant pursuit.
* **Retention of Responsibility:** Authors retain **sole legal and ethical responsibility** for the entire content of their papers, including accuracy and precision; AI cannot be held accountable.
* **Reflexivity:** In qualitative research, humans must provide the **reflexivity and contextual understanding** (e.g., interpreting non-verbal cues) that AI cannot perform.

### **Task Restrictions**

Certain tasks are identified as inappropriate for AI or subject to strict limitations:

* **Authorship Exclusion:** There is a general consensus that **LLMs are not eligible for co-authorship** because they lack accountability and personhood.
* **Peer Review Prohibitions:** Using proprietary LLMs for peer review is often prohibited (e.g., by the NIH) because **manuscripts under review are confidential** and entering them into AI systems violates that trust.
* **Normative and Epistemic Limits:** Humans should reserve the right to **decide what problems are worth studying** and determine the "scientific roadmap," as these choices are based on human values and subjective points of view.
* **Sensitive Data:** Researchers are cautioned against **loading sensitive or non-anonymized datasets** into LLMs due to privacy concerns and the lack of ethical oversight by AI corporations.

**Author notes:** *[Which conditions recur? Which are isolated?]*

---

## 3. Structured and systematic use — including practical methods

*Q5a: Do sources distinguish ad hoc AI use from systematic, structured, or workflow-based approaches? Recommendations for how to use AI, not just whether?*

*Q5b: Do sources propose named methods or frameworks? For each, describe the steps in enough detail that an unfamiliar reader understands the procedure.*

*Q5c: Do any sources include templates, checklists, prompt templates, or worked examples? List and describe them.*

The sources distinguish between **ad hoc AI use** and **systematic, workflow-based approaches**, emphasizing that "working with LLMs is an iterative process" that requires more than "just booting up an LLM and copy-pasting its outputs". Instead of ad hoc interaction, sources recommend establishing **clear quality criteria and verification methods _before_ using LLMs**.

### **Q5a: Systematic vs. Ad Hoc AI Use**

The sources propose several structured approaches for integrating AI into academic work:

* **Human-in-the-Loop:** In computational fields, researchers are encouraged to use LLMs to speed up prototyping while a human guides the process, corrects errors, and decides which ideas warrant pursuit.
* **Context Isolation:** For qualitative analysis, researchers recommend using **separate conversations for independent tasks** to prevent the model from "learning" from previous prompts and biasing subsequent results.
* **The "Two-Lane" Approach:** This framework, implemented at the University of Sydney, separates academic tasks into **Lane 1** (traditional assessments where AI is restricted to ensure core knowledge acquisition) and **Lane 2** (where AI is embraced as a learning tool for brainstorming and refining ideas).
* **Scientific Reproducibility Standards:** To move beyond ad hoc usage, researchers should report the **exact model version and the date of analysis**, and utilize open-source models that can be run locally for full control over variables.

### **Q5b: Named Methods and Frameworks**

The sources describe several named frameworks for research and evaluation:

* **Transmission Chain Method:** Derived from psychology, this "laboratory version of the telephone game" involves passing a story iteratively through an LLM. The researcher prompts the LLM to summarize a text, then feeds the output back into the model with the same prompt for successive steps to track how content (such as gender stereotypes) is modified or retained over time.
* **Five-Step Framework Approach:** A leading method for thematic analysis in health research applied to AI. The steps include: **(1) Getting started** (identifying transcript context); **(2) Familiarization** (identifying broad attitudes); **(3) Identifying a thematic framework** (developing initial themes); **(4) Indexing** (matching key quotes to themes); and **(5) Mapping and interpretation** (analyzing patterns across themes).
* **Agent-Based Modeling (ABM) with LLMs:** A paradigm for simulating human societies. Researchers create a "facsimile of a social setting" and populate it with **silicon agents** given specific personalities and traits (e.g., a "gregarious pharmacist"). The agents are equipped with software infrastructure for **memories of past interactions**, allowing researchers to track emergent group properties like dates, parties, or gossip.
* **Three-Step Framework for Benchmarking Generalization Accuracy:** This systematic evaluation involves: **(1)** Prompting an LLM to summarize scientific texts; **(2)** Classifying both original and summary texts for three features (**generic, present tense, and action-guiding generalizations**); and **(3)** Comparing classifications to generate a quantifiable "overgeneralization score".

### **Q5c: Templates, Checklists, and Worked Examples**

Several sources provide practical tools for implementing these frameworks:

* **Thesis and Research Prompt Templates:** One source lists **10 specific prompts** to guide a student through every phase of a research project, from topic selection and literature reviews to statistical analysis and drawing conclusions.
* **The "AI Tutor" Prompt:** A comprehensive template that sets a persona ("upbeat, encouraging tutor") and instructs the AI to guide students using open-ended, leading questions rather than providing immediate answers.
* **Qualitative Analysis Examples:** One source includes a **worked qualitative codebook** for healthcare research and worked examples of applying abstract theoretical lenses, such as a **Marxist perspective** or a **socio-ecological model**, to interview data.
* **Research Checklists:** The sources mention the **STROBE checklist** for observational studies as a tool to guide exploratory AI analysis and recommend the **CrediT taxonomy** to code the specific nature of AI's contribution to a manuscript.
* **Generalization Transition Examples:** A table provides **worked examples of "algorithmic overgeneralizations,"** showing side-by-side how a specific narrower claim from a scientific abstract was transformed into a broader, unwarranted generalization by an LLM.

**Author notes:** *[(a) Explicit vs. implicit structured/unstructured distinction; (b) sources closest to paper's argument; (c) sources silent on this; (d) methods or templates usable as precedent.]*

---

## 4. Tool types and disciplinary variation

*Q6–7: Do sources differentiate tool types — conversational, specialised, agentic? Variation across disciplines? What is said about social science or sociology specifically?*

Sources differentiate between AI tools based on their scope and functionality, distinguishing between **general-purpose conversational agents**, **specialized scientific models**, and **agentic systems** capable of autonomous social simulation.

### **Differentiation of Tool Types**

* **Conversational and General-Purpose:** This category includes widely used models like **ChatGPT, Gemini (formerly Bard), Claude, and Bing (Copilot)**. These tools are characterized by their ability to generate human-like text, summarize articles, and participate in natural language conversations across a broad array of subjects. Some sources describe these as **"universal tools"** that remove the need for building task-specific software.
* **Specialized and Bespoke:** Sources highlight models designed for specific scientific domains, such as **Galactica** (for scientific knowledge discovery), **AlphaFold** (for protein structure prediction), and **formal proof verifiers**. Some contributors argue that the future of machine-aided science lies in an ensemble of these "bespoke" and lightweight models designed for high interpretability and efficiency in specific tasks rather than one-size-fits-all LLMs. Specialized AI add-ons are also appearing in qualitative software like **NVivo and MaxQDA**.
* **Agentic and Simulation Tools:** These tools go beyond text generation to perform as **"silicon agents"** in complex environments. This includes LLMs integrated into **agent-based modeling (ABM)** to simulate social processes, and models that play high-level strategy games like **Diplomacy** or **AlphaGo**.

### **Variation Across Disciplines**

The application and reception of AI vary significantly by field:

* **Computational and Natural Sciences:** Research focuses on **predictive technology**, such as automating code generation for math problems, rediscovering orbital mechanics, and advancing mathematics through proof-verifiers.
* **Medicine and Healthcare:** Studies emphasize the risks of **generalization bias** in clinical trial summaries and the use of AI for medical education and research synthesis in top-tier journals like _The Lancet_ and _NEJM_.
* **Education and Academic Writing:** Focuses on using AI as a **"learning partner" or "tutor"** to help students practice interview probing, refine research questions, and manage literature reviews.
* **Social and Behavioral Sciences:** AI is used for large-scale **meta-science**, such as automatically identifying theoretical frameworks and statistical methods across thousands of papers in business, economics, and psychology.

### **Specifics for Social Science and Sociology**

Sociology and related social sciences are identified as being at the center of "reverse engineering" the **"social sense"** of human behavior.

* **Silicon Samples:** Sociologists are exploring LLMs as **proxies for human participants** in public opinion surveys. "Silicon samples" can accurately impersonate demographic groups to pre-test survey questions or impute missing data, although they may exaggerate extreme attitudes.
* **Cultural Transmission:** Using **"transmission chain" experiments**, sociologists study how LLMs reflect human cultural evolution by tracking how content like **gender stereotypes** or **"gossip"** is retained or modified across iterations.
* **Agent-Based Modeling (ABM):** Sociology has a decades-old tradition of ABMs that is now being transformed by "generative agents". These agents are given traits (e.g., a "gregarious pharmacist") and **software-based memories**, allowing them to demonstrate emergent group properties like forming daily routines, planning parties, and spreading information about romantic relationships.
* **Social Science Text Analysis:** LLMs have proven highly effective at **automated content analysis**, coding the ideology of elected officials or the credibility of media sources with an accuracy that matches or exceeds crowd-workers.
* **Unique Risks:** Social scientists are warned about **algorithmic bias** favoring WEIRD (Western, Educated, Industrialized, Rich, Democratic) populations and the risk of **"careless speech"** that could cumulatively degrade shared social truths. To mitigate corporate opacity, social scientists are encouraged to build their own **open-source infrastructure** for behavioral research.

**Author notes:** *[Gaps for sociology.]*

---

## 5. Synthesis

*Q8: Emerging consensus on responsible AI use? Core principles across sources? Where do sources disagree?*

An emerging consensus across the sources suggests that the responsible use of AI in academic research requires a move toward **proactive integration** guided by shared values rather than mere prohibition. While perspectives range from enthusiastic to skeptical, there is a clear agreement that **the human researcher must remain the central moral and epistemic agent** in the scientific process.

### **Core Principles of Responsible AI Use**

The sources converge on several foundational principles for maintaining research integrity:

* **Transparency and Disclosure:** Researchers must **explicitly state which AI tools were used and for what purpose**. This includes documenting prompts and sharing AI responses as supplementary material to ensure openness.
* **Accountability:** Because AI lacks personhood and cannot be held responsible for errors, **authors retain sole legal and ethical responsibility** for every part of their work, including the accuracy of citations and data.
* **Verification and Rigorous Oversight:** Blind trust is discouraged; users must **verify all AI-generated content against original academic sources**. This is vital because LLMs often produce "careless speech"—plausible but factually incorrect information.
* **Fairness and Bias Mitigation:** Researchers have a duty to recognize that LLMs reflect **human cultural transmission biases**, such as gender stereotypes and Western-centric viewpoints. Responsible use involves adapting prompts to ensure **plurality and representativeness** of sources.
* **Open Science and Reproducibility:** There is a strong call for **open-source infrastructure** to ensure that models are secure, explainable, and robust against "drift" (unannounced changes by proprietary providers).
* **AI Literacy:** Universities should embed AI literacy into their curricula, teaching students to understand the **limitations and technical affordances** of these tools.

### **Areas of Disagreement**

Despite the consensus on values, sources disagree on the implementation and the fundamental nature of AI:

* **Collaborator vs. Tool:** Some scientists argue LLMs should be viewed as **"knowledgeable research assistants" or "collaborators"** who can facilitate complex cognitive work. Others strongly reject this as harmful **anthropomorphization**, insisting AI is merely a **"synthetic text-extruding machine"** that cannot learn from mistakes or participate in the social conversation of science.
* **The Bound of AI’s Proper Domain:** Contributors disagree on how much autonomy to grant AI. Some argue for **"firm and restrictive boundaries"** where humans alone decide which problems are worth studying (the normative aspect) and retain the goal of human understanding (the epistemic aspect). Others suggest that if an AI can fruitfully identify productive research directions, we should **take any help we can get**.
* **Technological Settings and Prompting Strategies:** Disagreement exists on the best technical methods for accuracy. While some recommend **systematic "step-by-step" prompts**, others found that explicitly asking for accuracy can actually **backfire**, increasing the likelihood of "algorithmic overgeneralization" due to an "ironic rebound" effect in the model’s processing.
* **Regulation vs. Principles:** While some advocate for **legal "truth duties"** requiring providers to align models with ground truth, others argue that **strict, preconceived norms are a losing battle** and that the scientific community should instead focus on training and shared values.

**Author notes:** *[What supports the paper argument; what is contested; what is absent.]*

---

## Key claims for the paper

| Claim                                                                                                                                                                 | Source(s)                     | Section in paper                           |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- | ------------------------------------------ |
| Large language models reproduce and magnify human cultural transmission biases, such as gender stereotypes, when summarizing narratives.                              | Acerbi & Stubbersfield (2023) | Significance; Discussion                   |
| LLMs can act as "knowledgeable research assistants" but threaten scientific integrity through fabricated information and a lack of accountability.                    | Binz et al. (2025)            | Background; Perspective 1; Conclusion      |
| Responsible integration of generative AI is essential for student training to prepare them for an AI-driven workforce while maintaining academic integrity.           | Rodafinos (2025)              | Abstract; Aligning curricula; Ethical use  |
| Generative AI can advance the scale, scope, and speed of social science through "silicon samples" and automated content analysis.                                     | Bail (2024)                   | Abstract; Opportunities for Social Science |
| "Careless speech" in LLMs creates unique long-term harms by degrading shared social truths and homogenizing scientific knowledge.                                     | Wachter et al. (2024)         | Abstract; Introduction; Careless speech    |
| Most prominent LLMs exhibit a strong "generalization bias," consistently broadening scientific conclusions beyond what is warranted by the original data.             | Peters & Chin-Yee (2025)      | Abstract; Discussion; Conclusion           |
| Large-scale meta-scientific efforts can utilize LLMs to identify theoretical frameworks and statistical methods across thousands of research papers.                  | Tyner et al. (2026)           | Methods; Extended Data Figs. 9-10          |
| AI-assisted qualitative analysis identifies descriptive themes that overlap with human researchers but lacks the reflexivity required for deep interpretive analysis. | Wachinger et al. (2024)       | Abstract; Results; Reflexivity             |

* * *

Gaps and follow-up
------------------

* There is a critical lack of published user studies that quantify the time and effort required for researchers to accurately fact-check LLM outputs under pressure.
* Comprehensive empirical data regarding the long-term impacts of AI integration on student learning outcomes and optimal educational strategies are still emerging.
* Future research must systematically investigate whether "accuracy prompts" (requesting model faithfulness) consistently trigger "ironic rebound" effects that actually increase inaccuracies.
* Deeper investigation is needed into the legal feasibility of a "truth duty" for AI providers to prevent the cumulative erosion of historical and scientific records.

* * *

Sources not drawn on
--------------------

All 8 sources provided in the notebook have been utilized in the previous responses and this final summary.

| Source | Reason not cited                                                                               |
| ------ | ---------------------------------------------------------------------------------------------- |
| None   | All sources were found to be highly relevant to AI use in research and were cited accordingly. |

References
----------

* Acerbi, A., & Stubbersfield, J. M. (2023). Large language models show human-like content biases in transmission chain experiments. PNAS. [10.1073/pnas.2313790120](https://doi.org/10.1073/pnas.2313790120).
* Binz, M., Alaniz, S., Roskies, A., Aczel, B., Bergstrom, C. T., Allen, C., Schad, D., Wulff, D., West, J. D., Zhang, Q., Shiffrin, R. M., Gershman, S. J., Popov, V., Bender, E. M., Marelli, M., Botvinick, M. M., Akata, Z., & Schulz, E. (2025). How should the advancement of large language models affect the practice of science? PNAS. [10.1073/pnas.2401227121](https://doi.org/10.1073/pnas.2401227121).
* Rodafinos, A. (2025). The Integration of Generative AI Tools in Academic Writing: Implications for Student Research. Social Education Research. [10.37256/ser.6220256517](https://doi.org/10.37256/ser.6220256517).
* Bail, C. A. (2024). Can Generative AI improve social science? PNAS. [10.1073/pnas.2314021121](https://doi.org/10.1073/pnas.2314021121).
* Wachter, S., Mittelstadt, B., & Russell, C. (2024). Do large language models have a legal duty to tell the truth? R. Soc. Open Sci. [10.1098/rsos.240197](https://doi.org/10.1098/rsos.240197).
* Peters, U., & Chin-Yee, B. (2025). Generalization bias in large language model summarization of scientific research. R. Soc. Open Sci. [10.1098/rsos.241776](https://doi.org/10.1098/rsos.241776).
* Tyner, A. H., Abatayo, A. L., Daley, M., Field, S., Fox, N., Haber, N. A., Hahn, K. M., Struhl, M. K., Mawhinney, B., Miske, O., Silverstein, P., Soderberg, C. K., Stankov, T., et al. (2026). Investigating the replicability of the social and behavioural sciences. Nature. [10.1038/s41586-025-10078-y](https://doi.org/10.1038/s41586-025-10078-y).
* Wachinger, J., Bärnighausen, K., Schäfer, L. N., Scott, K., & McMahon, S. A. (2024). Prompts, Pearls, Imperfections: Comparing ChatGPT and a Human Researcher in Qualitative Data Analysis. Qualitative Health Research. [10.1177/10497323241244669](https://doi.org/10.1177/10497323241244669).*

---

<!-- INSTRUCTIONS (remove before archiving)

Run Q0 first — forces NotebookLM to register all sources before thematic queries.
Cross-check Q0 list against citations in each section as you work.

Q1–3 and Q6–7 are combined queries: run separately, synthesise when pasting.
Q5 has three sub-queries: run all three, combine in Section 3.
If NotebookLM names a method (e.g. SELAR), follow up: "Describe exactly how
[method] works step by step." Paste follow-up into Section 3.

Add author-year citations and references as you paste — do not leave for later.
Run Q9 last. Complete Key claims table before closing.

-->
