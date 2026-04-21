# Comparison: Gemini deep research vs. current project setup
## Source: notes/google-gemini-onResearchStructure.md

The Gemini document is a Norwegian-language deep research report on how to use Claude Code professionally in social science research, drawing on IT infrastructure principles (Cookiecutter Data Science, Architecture Decision Records, Git workflows, GDPR hooks). It covers six main areas: folder structure, CLAUDE.md configuration, skills, MCP integrations, GDPR/privacy, and decision logging.

Overall verdict: the current project setup is ahead of most of the Gemini suggestions in several areas (decision logging, session protocol, skill configuration, author-input transparency), but there are genuine gaps — particularly around empirical data handling, ADR status tracking, citation verification, and GDPR hooks.

---

## What is already well covered in the current setup

**CLAUDE.md as project constitution** — fully implemented. Gemini describes this as a key innovation; we are already using it with more specificity than Gemini recommends.

**Decision logging** — fully implemented. The current log format (log files, author-input files, session summaries, log index) is more systematic than anything Gemini describes. The author-input file in particular is a transparency mechanism Gemini does not mention at all.

**Skills** — implemented: skardhamar-style (drafting), logic-language-reviewer (argument review), social-science-article-reviewer (discipline-specific review). Gemini recommends skills for qualitative coding and quantitative validation; these are complementary rather than overlapping.

**Notes system with lifecycle tracking** — implemented via notes/ and notes/used/. Gemini does not discuss this.

**Literature pipeline** — fully implemented and more sophisticated than anything Gemini describes (OpenAlex + Unpaywall + Elicit + NotebookLM, full audit trail, screening decisions documented).

**Replication package framing** — implemented. Gemini does not discuss the replication package as a transparency artefact, which is one of the paper's core arguments.

**Regular /clear usage** — implemented in session protocol. Gemini mentions it but only in passing under cost control.

---

## What is similar but implemented differently

**Decision logging format vs. ADR (Architecture Decision Records)**
Gemini recommends ADR files (from software engineering) stored in docs/adr/ with a lifecycle status field: Proposed → Accepted → Superseded → Rejected. The current log format records decisions as they happen but does not track their lifecycle — a decision made on April 5 cannot be easily marked as "Superseded" when it is changed later.

*Consideration*: The ADR status system adds something genuinely useful — especially for a paper arguing for accountability and traceability. A decision that was superseded should show up as such, not just be absent from later logs. This could be implemented lightly: add a status field to the log format, and when a decision is reversed, create a brief "closed" entry linking back to the original. Full ADR file-per-decision is probably too heavy for this project type.

**Folder structure**
Gemini follows Cookiecutter Data Science: data/raw, data/interim, data/processed, data/external, src/, notebooks/, reports/, docs/. The current structure is designed for a literature-based paper (literature/, notes/, draft/, scripts/, supplementary/) and does not accommodate empirical data. These are complementary structures for different research modes, not competing alternatives.

*Consideration*: If the paper is to include a section on systematic AI use in empirical research, the data/ subfolder hierarchy (raw → interim → processed → external) should be documented as the recommended structure for that mode. The immutable raw data principle (raw data is never edited, only read) is the key norm to articulate.

**Zotero integration**
Current setup uses a Python script (copy_pdfs_from_zotero.py) to copy PDFs from local Zotero storage. Gemini describes more sophisticated MCP integration: semantic search within the Zotero library, full-text interaction, BibTeX export from the terminal. The zotero-mcp and zotero-fulltext MCP servers exist and could replace the manual script.

*Consideration*: Worth exploring as an upgrade, but not urgent. The current pipeline (OpenAlex + Unpaywall + manual) is already well-documented and serves the paper's self-demonstrating function. A Zotero MCP would be a better fit for a future empirical project or for a researcher who manages literature primarily in Zotero rather than via search pipelines.

**Settings hierarchy**
Gemini describes three settings levels: global (~/.claude/settings.json), project (.claude/settings.json — shared via git), and local (.claude/settings.local.json — personal overrides not in git). The current setup uses only CLAUDE.md and does not explicitly document this hierarchy or the .gitignore convention for settings.local.json.

*Consideration*: Document the settings hierarchy in the paper's supplementary materials and file-structure template. The distinction between shared project config and local overrides is directly relevant to the paper's replication package argument.

---

## What is new and worth considering

**1. Citation verification skill**
Gemini describes a citation-verification skill that checks .bib files against CrossRef or OpenAlex to detect hallucinated references. This is directly relevant to the paper: one of the documented risks of unstructured AI use is hallucinated citations, and a verification skill is a concrete example of structured use preventing that failure mode.

*Recommendation*: Consider implementing a citation-verification skill for this project (to check the reference list before submission), and describe it in the paper as an example of a verification checkpoint. This would both serve a practical need and strengthen the argument with a concrete demonstration.

**2. Numbered sequential scripts**
Gemini recommends prefixing scripts with numbers to make execution order explicit: 01_clean.py, 02_screen.py, 03_score.py. The current scripts/ folder uses descriptive names (screen_candidates.py, screen_fulltexts.py, download_pdfs.R) but not sequential numbering.

*Recommendation*: Rename scripts with numeric prefixes. This is a small change that makes the pipeline more self-documenting and easier for a replication reader to follow. It is also consistent with the paper's argument about making research decisions explicit.

**3. Immutable raw data principle**
Gemini states that raw data must be treated as immutable: never edited manually or overwritten by scripts, with all transformations applied via versioned code. The current setup does not explicitly articulate this norm, though in practice the pipeline respects it.

*Recommendation*: Add this principle explicitly to the file-structure-template.md in supplementary/ and to the paper's section on empirical data. It is one of the clearest analogies from IT infrastructure to research practice and should be named.

**4. GDPR/PII hooks for empirical research**
Gemini describes PreToolUse hooks that run a local script to scan text for PII patterns (names, emails, identifiers) before it is sent to the cloud. This is relevant for any empirical project with participant data, and it is the kind of systematic, configured safeguard that characterises systematic AI authorship.

*Recommendation*: For the paper's empirical data section, document this as a concrete example of a systematic safeguard. Describe the hook mechanism (PreToolUse in settings.json), the principle (data never leaves the local machine unredacted), and the available tools (ScrubDuck, custom Python scripts). This does not require implementing it for the current project (which has no participant data) but should be described as the correct approach for projects that do.

**5. data-anonymizer and statistical-audit skills**
Gemini describes two skills relevant for empirical work: a data-anonymizer skill (identifies and masks PII in raw text) and a statistical-audit skill (reviews R/Python code for p-hacking, missing data handling, model specification errors). These are examples of AI-assisted methodological safeguards that directly instantiate systematic authorship.

*Recommendation*: Describe these as examples in the paper's empirical data section. The statistical-audit skill in particular is a direct counter to the p-hacking and replication crisis concerns raised in the reframe note — it shows how systematic AI use can reinforce rather than undermine research integrity.

**6. Cost control mechanisms**
Gemini describes CLI flags for budget management (--max-budget-usd, --max-turns, --effort) and prompt caching for repeated large documents. These are practical considerations not currently discussed in the project.

*Recommendation*: Low priority for this paper, but worth a brief mention in the file-structure-template or supplementary materials as part of the practical workflow guide. Token costs are a real constraint for researchers, especially outside well-funded institutions.

**7. ADR lifecycle statuses**
As noted above: Proposed / Accepted / Superseded / Rejected. Not currently implemented.

*Recommendation*: A light version of this — adding a brief "decision revised" note to the log whenever a prior decision is changed, with a link back to the original — would improve the audit trail without requiring a full ADR file-per-decision system. This is worth implementing in the logging instructions.

---

## For the empirical data section of the paper

If a section on empirical data handling is added, the following Gemini-sourced elements are the most useful to incorporate:

1. **Data folder hierarchy**: data/raw (immutable, read-only) → data/interim (intermediate transformations) → data/processed (analysis-ready) → data/external (third-party reference data). This is the standard Cookiecutter structure and is well-established in reproducible research practice.

2. **Immutable raw data norm**: articulate explicitly. All transformations via versioned, numbered scripts. Raw data never touched after download/receipt.

3. **GDPR hooks**: PreToolUse hook running a local PII scanner before any file is sent to the API. Describe the mechanism and recommend specific tools.

4. **Sequential numbered scripts**: 01_import, 02_clean, 03_anonymize, 04_analyse. Makes pipeline self-documenting and replication-ready.

5. **Statistical-audit skill**: configured skill that reviews analytical code for methodological errors. Describe as a verification checkpoint analogous to the logic-language-reviewer skill used in this paper.

6. **ADR for analytical decisions**: document decisions like exclusion criteria, variable coding, model specification in structured decision records. Directly analogous to the log files used in this project.

The key framing for the empirical section is that all of these practices are instances of systematic AI authorship: configured, documented, verifiable. The alternative — accepting AI-generated analyses without explicit criteria, verification checkpoints, or documented decisions — is unsystematic AI authorship, and produces exactly the kind of accountability problems the paper argues against.

---

## What Gemini misses entirely

- Author-input files (documenting the human intellectual contribution)
- Session-start protocol and /clear discipline as epistemic practice
- The structured/systematic vs. unstructured/unsystematic distinction as an analytical frame
- The replication package as transparency artefact (rather than just as technical reproduction)
- Query authorship / systematic authorship as a concept
- The journal policy implications

These are the paper's original contributions. The Gemini document is strong on technical infrastructure but does not theorise what systematic use means or why it matters epistemically. That gap is the paper's whole argument.
