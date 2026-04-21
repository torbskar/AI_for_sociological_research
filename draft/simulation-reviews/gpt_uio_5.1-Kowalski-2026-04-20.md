# Comments on “Systematic AI Use in Sociological Research”

## 1. Two technically imprecise / gappy parts of the argument

### (1) The pre-registration analogy and the strength of “internal” timestamps

You lean heavily on the claim that systematic AI use partially substitutes for preregistration by externalising decisions and by using working logs + git timestamps as a check against post‑hoc reconstruction:

> “the working logs that document iterative process address the cherry-picking risk that pre-registration's public commitment eliminates through publicity” <ref: index={1} firstWord={1880} lastWord={1915}/>

and earlier:

> “The `.git/` repository's commit history does more than track changes: it timestamps every file modification, which means that session logs and author-input files can be independently verified as contemporaneous records rather than retrospective reconstructions. This is the same principle that makes pre-registration timestamps credible, applied to the working documentation of the research process.” <ref: index={1} firstWord={780} lastWord={830}/>

For a methods‑savvy reader, this is where the argument currently overreaches:

* Git timestamps are only as trustworthy as the *threat model* permits. A single researcher can:
  * fabricate logs late in the project and commit them in one burst;
  * rewrite history (e.g., `git rebase`, deleting earlier branches or logs);
  * commit from a machine with a manipulated system clock.
* Preregistration services add (i) external hosting, (ii) cryptographic checksums, and often (iii) embargo/visibility controls. A private git repo on a personal machine is not evidentially equivalent.

You do flag that preregistration involves “a public, timestamped commitment” and that this is a “relevant disanalogy” <ref: index={1} firstWord={640} lastWord={675}/>, but then slide back into language that suggests functional equivalence.

**What a demanding reader will want:**

1. An explicit *weak vs strong* claim:
   
   * Weak: “Local logs and version control make post‑hoc reconstruction *more difficult* and cherry‑picking *easier to detect* than in undocumented workflows.”
   * Strong (and currently implied): “They play the *same epistemic role* as preregistration timestamps.”

2. An explicit statement of limits, e.g.:
   
   * Logs and git history are excellent *process documentation*, but:
     * they are not tamper‑evident in the way third‑party preregistration is;
     * they should be treated as *complementary to*, not *substitutes for*, formal preregistration where that is possible.

3. A short paragraph recommending *minimal hardening* if you want to make the prereg analogy persuasive: for example,
   
   * periodic pushes to an external repository (OSF / institutional GitLab);
   * archiving log snapshots with DOIs at milestones;
   * explicit statement that reviewers can check that the submitted supplement matches an earlier archived version.

That would preserve your central “externalisation” argument but avoid the impression that you’re underplaying the difference between internal and third‑party timestamps.

---

### (2) The systematic/unsystematic distinction as a binary, and the missing threshold problem

Throughout, you present “systematic / unsystematic” as a clean dichotomy, parallel to but better than “use / non‑use.” For example:

> “Systematic AI authorship has four defining features. The first is explicit criteria… The second is human verification… The third is documented outputs…” <ref: index={1} firstWord={540} lastWord={585}/>

and:

> “Systematic AI authorship is a necessary condition for epistemic soundness in AI-assisted research, not a sufficient one.” <ref: index={1} firstWord={2680} lastWord={2720}/>

The problem: the very practices you describe are *graded*:

* Criteria can be more or less explicit, more or less theory‑laden, and more or less stable over time.
* Verification can be cursory (“skim and accept”) or rigorous (spot‑checks with explicit decision rationales).
* Documentation can range from a few saved prompts to a complete, reviewable log with scripts and skill files.

Your own examples implicitly acknowledge a continuum (e.g., that checklists are “post‑hoc instruments” yet still a step up from nothing <ref: index={1} firstWord={365} lastWord={410}/>), but the conceptual language doesn’t.

For a methodologist, this creates a gap between the normative distinction (“systematic vs unsystematic”) and any **operational** definition that an editor or reviewer could apply. Two concrete issues follow:

1. **Where is the cut‑point?**  
   At what point along the spectrum of “somewhat structured AI use” do you want journals to treat a workflow as “systematic” for policy purposes?
   
   * Is saving a few prompts and giving a paragraph in Methods enough?
   * Do you require reusable prompt templates and skill files?
   * Must there be stage‑specific logs with human decision rationales?

2. **How much variation is acceptable within “systematic”?**  
   You praise Zeng et al. for showing that reproducibility‑oriented prompting improves accuracy <ref: index={1} firstWord={2200} lastWord={2245}/>, but you don’t say how rough a workflow can be and still count as “systematic” in your sense.

**What would tighten this up:**

* Add an explicit subsection (either in §3.2 or §6.3) that:
  
  * states that “systematic” is a *threshold concept* rather than a natural kind;
  
  * gives a minimal operationalisation, e.g.:
    
    > “For the purposes of journal policy, we can say that AI use is *systematic* when:  
    > (i) there is a written, date‑stamped configuration or protocol *before* execution for each major stage (search, screening, analysis, drafting, review);  
    > (ii) there is at least one documented human‑verification checkpoint per stage; and  
    > (iii) the protocol and logs are archived and shared as part of the replication package.”

* Explicitly recognise “partially systematic” cases, and say something like:
  
  > “Reviewers may reasonably treat workflows that meet (i) and (ii) for some stages but not others as *partially systematic*, and should make that judgment explicit in reviews.”

This would reassure technically sophisticated readers that the distinction can be actionably applied, not just used rhetorically.

---

## 2. Does the paper address the post‑hoc documentation problem?

You do more than most here, which is a major strength:

* You emphasise **contemporaneous logs** and “author‑input files” as lab‑notebook analogues <ref: index={1} firstWord={1530} lastWord={1600}/>.
* You tie them to **version control timestamps** and argue that this makes retrospective fabrication harder <ref: index={1} firstWord={780} lastWord={830}/>.

However, from a research‑integrity standpoint the treatment is still incomplete on two fronts:

1. **Explicit adversarial scenario.**  
   You briefly note that “documentation can still be faked by dishonest researchers” <ref: index={1} firstWord={2520} lastWord={2550}/>, but:
   
   * You do not spell out *how* logs could be fabricated late in the process (e.g., generate synthetic “iterative” logs from a nearly final draft and commit them all at once).
   * You do not distinguish between:
     * “good faith but sloppy” (which logging strongly discourages), and
     * “deliberate reconstruction” (which logging only partially constrains).

2. **Missing guidance on *verification* of the logs.**  
   You’re close but not quite there. A technical reader will ask:
   
   * What stops an author from curating away “messy” branches and only depositing a cleaned‑up commit history?
   * How is a reviewer to know whether the logs truly reflect the working process?

### What the paper should add

I’d encourage a short, forthright paragraph in §5.4 or §6.3 that:

* Acknowledges that **internal project documentation is not tamper‑proof**, and therefore:
  
  * “should be viewed as *stronger evidence* than ex post narrative methods sections, but weaker than third‑party preregistration.”

* Recommends concrete *mitigations*:
  
  1. **Automated / append‑only logging where possible.**  
     E.g.:
     
     * Use tools that automatically export session logs to an append‑only file on close of each AI session.
     * Avoid manual “curation” of logs before archiving.
  
  2. **Periodic external archiving.**  
     
     * Push the repo (or at least the `logs/` and configuration files) to an external service at major milestones.
     * For long projects, consider depositing interim snapshots with DOIs (OSF, institutional repository).
  
  3. **Explicit reporting standard in the paper.**  
     A sentence in Methods like:
     
     > “We used git for version control and archived an unedited copy of our logs and configuration files at OSF (DOI: …) before submitting the manuscript.”

With that, you’d have a clear, honest story: systematic AI workflows *substantially reduce* the scope for post‑hoc reconstruction and *improve* the auditability of the process, but they are not cryptographically secure; for that, preregistration and external archiving remain gold standards.

---

## 3. Where the paper undersells itself to heavy AI users

The place I think you undersell your contribution to already‑heavy AI users is in §4.3 on empirical data and the “PII hook” / separation of zones:

> “The three configurations described — the immutability rule, the accessibility-oriented script specification, and the PII hook — are instances of systematic AI authorship at the empirical level… it is worth stating explicitly that for projects involving personal data, systematic AI authorship is not merely epistemically preferable but, in this form, the legally required approach…” <ref: index={1} firstWord={1325} lastWord={1390}/>

Many social scientists who already use AI extensively for coding are in exactly this situation:

* They want to use AI for **analysis scripts** but are terrified of **GDPR / IRB** consequences and institutional IT rules.
* They currently get informal advice like “just don’t upload data,” which leaves them with no principled way to structure projects.

You’ve actually given them:

* A **design pattern** for safely separating raw / interim / processed data and configuring AI so that:
  * raw data *never* leaves the machine;
  * AI helps only with scripts and anonymised derivatives;
  * there is a defensible story for data protection officers.

But you present this as “anticipatory guidance” and almost as a side‑case to a literature‑only paper.

**How to make the contribution clearer for this audience:**

* In the Introduction or Conclusion, draw out a short, explicit claim:
  
  > “For researchers who already rely on AI for coding, the data‑separation architecture in §4.3 is not merely a nicety but a way to *unlock* AI assistance for empirical work while staying within GDPR / IRB constraints. It turns ‘don’t upload data’ into an auditable project‑level design that institutions can evaluate and endorse.”

* In §4.3, add a sentence that signals to this audience:
  
  > “If you are already using AI as a coding assistant, this architecture is what allows you to extend that practice to sensitive empirical projects without sending raw data to any external provider.”

That makes it obvious that following your workflow doesn’t just make their current practice more transparent; it *enables* new, compliant uses they currently avoid.

---

## 4. What a concrete, actionable disclosure standard would look like — and how far the paper goes

You are very close to a usable standard, but it’s currently implicit and scattered across §§3–6. A journal editor who likes your argument would still have to reverse‑engineer it.

### A concrete, actionable standard (sketched)

You have all the ingredients; I’d encourage pulling them together (perhaps as a table in §6). Something like:

#### A. In the **manuscript**

1. **Methods: AI workflow overview**
   Include a short, structured paragraph answering:
   
   * *Stages*: For which stages was AI used? (e.g., search, screening, analysis‑code drafting, text‑drafting, review).
   * *Role*: For each stage, was AI use:
     * (a) merely clerical (formatting, deduplication),
     * (b) substantive but under explicit criteria + human verification (systematic),
     * (c) exploratory / unsystematic?
   * *Human checkpoints*: How and where did the human author verify or override AI output?
   
   Example sentence:
   
   > “We used an AI assistant systematically for (a) literature search and screening, (b) drafting analysis scripts, and (c) structured review. For each stage, we specified written criteria before running the AI, logged all prompts and outputs, and manually verified outputs against those criteria.”

2. **Data and privacy statement (if empirical)**
   
   * Explicitly state whether **raw data** was ever sent to an external AI service and how this was prevented (or why it was permitted).
   * Mention the three‑zone model (raw / interim / processed) if applicable.
   
   Example:
   
   > “Raw data (including personal identifiers) never entered any AI context. We used AI only to assist with writing and reviewing analysis code and documentation.”

3. **Authorship and accountability**
   
   * Explicitly link to query authorship:
     
     > “We treat configuration design (search strings, screening rubrics, analysis specifications, reviewer prompts) as part of our intellectual contribution, and we retain all such materials in the replication package.”

#### B. In the **supplement / replication package**

Require, at minimum:

1. **Configuration artefacts**
   
   * Project‑level configuration file(s) (e.g. `CLAUDE.md` equivalent).
   * Skill files / reviewer prompts.
   * Prompt templates used for each major stage (search, screening, synthesis, drafting, review).

2. **Logs**
   
   * Session logs or at least stage‑level logs, in an unedited form.
   * Author‑input files where you distinguish what is yours vs AI elaboration.

3. **Provenance & timing**
   
   * A short README stating:
     * when the log bundle was frozen (e.g., “before submission”);
     * where the full history can be inspected (e.g., OSF / Git repository).

4. **Task‑level delegation summary (GAIDeT‑style)**
   
   * A one‑page table listing, for each research task:
     * AI involvement (none / advisory / execution under criteria / freeform generation);
     * human oversight level;
     * link to relevant artefacts.

This could be framed explicitly as a *minimal disclosure standard for systematic AI use*, with journals free to demand more.

### How far the paper currently goes

You already provide most of the raw material:

* A project structure and artefact list in §4.1–4.6 <ref: index={1} firstWord={690} lastWord={940}/>, including logs, skill files, and search scripts.
* A clear normative claim that documentation should be part of the replication package <ref: index={1} firstWord={1550} lastWord={1615}/>, <ref: index={1} firstWord={1710} lastWord={1765}/>.
* Integration with ICMJE criteria in §5.5 that naturally underwrites disclosure about query authorship <ref: index={1} firstWord={2760} lastWord={2850}/>.

But you stop short of:

* Assembling these into a **canonical, 1–2 page standard** that an editor could paste into “Instructions for Authors.”
* Writing anything that looks like a **checklist** or minimum acceptance bar.

At the moment, the paper:

* **Does**: articulate principles, give a worked workflow, and argue for documentation‑based policy.
* **Does not yet**: specify a *concrete minimum package* that would allow a journal to say, “This is what systematic AI disclosure must include.”

My recommendation:

* Add a brief subsection to §6 (e.g. “6.4 A minimum disclosure standard for systematic AI use”) that:
  
  * Lists the **in‑paper** items (Methods paragraph, privacy statement, authorship statement).
  * Lists the **supplementary artefacts** required.
  * Explicitly notes that this is **compatible with existing replication‑package expectations** and does not require new infrastructure.

That would directly answer the “what should we ask for?” question that editors and reviewers will have after reading the paper, and would make your argument actionable without further interpretation.

---


