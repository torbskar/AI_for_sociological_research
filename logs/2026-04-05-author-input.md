# Author input: Database strategy and legal considerations
## Date: 2026-04-05
## Previous session: 2026-04-04

The legal concern about Scopus was mine. I raised it as a practical obstacle after
working through the download workflow, not as an abstract ethical point. The specific
question -- whether Scopus's export restrictions apply regardless of where the model
runs -- came from me, and it was the right question to ask. The AI confirmed that tool
location (including local Ollama models) does not resolve the contractual restriction,
which I had suspected but needed to verify.

The question about Google Scholar scraping was also mine. I raised it as a potential
alternative route to metadata. The answer ruled it out, but asking the question led
directly to OpenAlex being identified as the clean solution. That chain -- Scopus
restricted, Google Scholar prohibited, therefore what is actually open? -- was my
reasoning, not a suggestion from the AI.

The decision to accept coverage loss and use OpenAlex rather than pursue the Scopus
legal question further was mine. The reasoning was that this is not a formal systematic
review, so perfect coverage is not required, and that the OpenAlex route is cleaner
both legally and procedurally. I made this call explicitly.

The instruction to write a separate .md file for Claude Code on the database strategy
was mine. The AI had not proposed separating operational instructions into their own
file; I recognised that the CLAUDE.md file should not accumulate tool-specific
procedural detail, and that a dedicated instructions file would be more useful for
Claude Code in practice.

The request to keep search terms in a separate file rather than hardcoded in the R
script was mine. This reflects a general principle I apply in my R work -- separating
configuration from execution -- but here it also serves the transparency goal of the
paper: the search terms are a documented methodological decision, not implementation
detail.

The request for a transparency note documenting my own input -- including the
questions that implied the core ideas -- was mine. I recognised that questions can
carry as much intellectual content as statements, and that a transparency record that
only documents explicit decisions would miss the reasoning that drove those decisions.

The argument about query authorship is mine. It emerged from reflecting on how the
session itself had unfolded: the Scopus legal question, the Google Scholar question,
the decision chain leading to OpenAlex -- all of these were intellectual moves I made
in query form, not in prose. The observation that a well-formed query encodes a
research question, a theoretical framing, and a judgment about what the literature is
missing -- and that this constitutes intellectual work regardless of who produces the
response -- is original to me. I wrote it up as a note (review_v10.md) because I
recognised it as the conceptual core of what the structured/unstructured distinction
is actually about, and because it needed to be captured before the framing was lost.

The specific example I used to illustrate the point -- the question about whether
legal restrictions apply regardless of model location -- was deliberate. It is a
question that encodes a distinction (data location vs. data use rights) that most
people conflate, and recognising that distinction was the intellectual move that
resolved the Scopus problem. The AI confirmed what I had already reasoned; it did not
originate the reasoning.

I noted in the draft of review_v10.md that this argument is likely the most novel
contribution the paper makes beyond the workflow itself. I stand by that assessment.

The decision to change the target journal to Sociological Science was mine. The
reasoning was mine: stronger journal, replicability focus consistent with the paper's
argument, no conservative AI policy, and openness to methodological contributions
without requiring a specific format. I also identified that the replication package
requirement — mandatory since April 2023 — is a structural fit with what this project
produces anyway. The transparency artefacts are the replication package. That
connection is not incidental; it is an argument for why this paper belongs in this
journal rather than a methods-specific outlet.

---

## Pipeline execution

The decision to build a keyword-based screener (`screen_candidates.py`) rather than
use Haiku sub-agents was mine, made after observing that sub-agents were failing on
Bash permissions regardless of auto-accept settings. I had expected the AI to handle
the screening autonomously; when that route hit a structural constraint I redirected
to scripting. This reflects the general pattern of the project: AI-assisted
automation is contingent on actual capability, not asserted capability, and the human
has to diagnose and reroute when the automation fails.

The decision to export 50 papers per subfolder rather than 50 in total was mine.
My reasoning was that the thematic structure of the search (six different query
blocks) reflects real variation in the literature, and collapsing to a single
globally-ranked 50 would likely over-represent the broad AI-in-research topic and
under-represent the more specific blocks (pre-registration, journal policy). I made
the call for balanced coverage over composite-score maximisation.

The instruction to write PIPELINE.md as a durable user guide — not just inline
documentation — was mine. The pipeline is complex enough that it needs a standalone
document, and I want to be able to reproduce or extend it without reconstructing the
steps from session logs. The format (step table, manual checkpoints marked with ✋,
expanded NotebookLM section) reflects how I actually work with this kind of document.

The decision to skip Step 6 (PDF renaming) and proceed directly to full-text
screening was mine. The rename step is cosmetic for the screening purpose; DOI-based
names do not impair relevance scoring. I preferred to keep the pipeline moving rather
than spend time on a step whose output would not affect the analysis.

The NotebookLM configuration and report templates were requested by me as structured
inputs to a manual analysis stage. The report templates with standing citation and
source-coverage instructions came from recognising that NotebookLM's default outputs
omit in-text citations and do not account for all sources. I specified both
requirements explicitly and they were encoded in the template headers. The decision
to mark Section 2 of Report C as the most important for the paper argument was mine —
it identifies the binary-versus-graduated policy distinction, which is the direct
empirical grounding for the paper's policy claim.
