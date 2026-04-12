# Legal Considerations: AI-Assisted Literature Analysis
## Project: Structured AI Use in Sociological Research
## Date: 2026-04-05
## Status: Provisional — requires confirmation from UiO library

---

## Summary

The legal situation for AI-assisted literature analysis differs by data source and type of use. The key finding is that the most restrictive terms apply to Scopus metadata exports, while full text analysis is covered by a combination of open licences, institutional agreements, and statutory TDM rights. Tool choice (Claude, NotebookLM, Ollama) does not affect the legal basis — the relevant questions are upstream of tool selection.

---

## 1. Scopus metadata exports

**Status: Grey zone — library consultation required**

Scopus's terms of service restrict using exported data to feed into AI systems for analysis. The legal basis is database rights (investment in compiling the database) and contract, not copyright on individual papers. This restriction is aimed primarily at commercial scraping and dataset creation, but is broad enough to cover computational analysis workflows.

**What does not resolve this:**
- Turning off Claude's training data opt-out — removes training risk but does not change contractual obligations to Scopus
- Using a local model (Ollama) — data stays on machine but the act of feeding exported data into AI analysis is still potentially non-compliant
- Any tool-level solution — the restriction is on data use, not data location or model training

**What may resolve this:**
- UiO's institutional Scopus agreement may include a research use clause covering computational analysis of exported metadata. Many institutional agreements now include this explicitly. **Confirm with UiO library.**

**Practical note:** The use case here — filtering a literature search for a research project — is what Scopus exists to support. The restriction is more plausibly aimed at commercial exploitation. But this needs formal confirmation rather than inference.

---

## 2. Full text from Unpaywall / open access routes

**Status: Clean — no further action needed**

Papers obtained via Unpaywall are either published under open licences (CC-BY and variants) or deposited as accepted manuscripts in institutional repositories. CC-BY explicitly permits computational analysis and text and data mining. This is the legally most solid portion of any corpus assembled this way.

---

## 3. Full text from publisher PDFs via UiO institutional access

**Status: Very likely permitted — confirm with UiO library**

When downloading PDFs through UiO's institutional access, the governing terms are the publisher's licence agreement with UiO, not Scopus's terms. These agreements vary by publisher but the trend is permissive:

- Major publishers (Elsevier, Springer, Wiley, Sage) now include text and data mining (TDM) clauses in institutional agreements. These typically permit computational analysis for non-commercial academic research purposes.
- Norwegian and European institutional contracts have moved in this direction following Plan S and the Norwegian Open Access policy framework.

**Statutory basis (EU/EEA):**
The EU Copyright Directive Article 4 (implemented in Norway via EØS) includes a statutory TDM exception for research organisations conducting scientific research. Key features:
- Applies to non-commercial research purposes
- Cannot be contracted away — exists independently of licence terms
- UiO as a research institution almost certainly qualifies
- Applies regardless of which AI tool is used for analysis

This statutory basis means that even where publisher licence terms are ambiguous, there is an independent legal foundation for full text analysis in an academic research context.

**Confirm with UiO library:** Which publishers have explicit TDM permissions in their UiO agreements, and whether the statutory TDM exception has been formally assessed for this type of workflow.

---

## 4. Tool choice: legal equivalence

The legal basis for analysis is the same regardless of tool:

| Tool | Training risk | Data location | Legal basis for analysis |
|------|--------------|---------------|--------------------------|
| Claude (training off) | None | Anthropic servers, not retained | Same as others |
| NotebookLM | None (Google policy) | Google servers, persists until deleted | Same as others |
| Ollama (local) | None | Local machine only | Same as others |

Tool choice affects data handling and privacy, not the legal basis for analysis. The relevant legal questions — licence terms, TDM rights, institutional agreements — are determined by the content source, not the analysis tool.

**One practical distinction:** NotebookLM is the only tool where uploaded content persists beyond the session. For published papers this is not material. For pre-publication manuscripts from other researchers, data handling terms would require separate consideration.

---

## 5. Questions for UiO library

1. Does UiO's institutional Scopus agreement include a clause permitting computational analysis of exported metadata for research purposes?
2. Which major publishers have explicit TDM permissions in their UiO licence agreements?
3. Has UiO formally assessed the scope of the EU/EEA statutory TDM exception (EU Copyright Directive Art. 4) for AI-assisted analysis workflows?
4. Is there a recommended procedure for documenting compliance when using full text analysis in a published research workflow?

---

## 6. Relevance for the paper

These legal considerations are directly relevant to the paper's argument in two ways.

First, the Scopus restriction illustrates a policy gap of the kind the paper discusses — institutional and publisher policies have not kept pace with structured, legitimate research uses of AI tools. The restriction is plausibly not aimed at this type of use but is broad enough to catch it.

Second, the statutory TDM exception and the trend toward explicit TDM clauses in institutional agreements show that the legal infrastructure for structured AI use is more permissive than most researchers assume. This supports the paper's argument that the relevant policy question is not whether to permit AI use but how to distinguish structured from unstructured use.

Both points belong in the paper — the first as an illustration of policy bluntness, the second as grounds for a more calibrated framework.

---

## Status tracking

| Issue | Status | Action |
|-------|--------|--------|
| Scopus metadata export terms | Unresolved | Contact UiO library |
| Unpaywall / OA full text | Resolved — permitted | None |
| Publisher full text via UiO | Likely permitted | Confirm TDM clauses with library |
| EU TDM statutory exception | Likely applies | Confirm with library |
| Tool choice legal equivalence | Resolved | None |
