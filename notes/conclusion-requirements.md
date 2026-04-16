# Conclusion requirements — what must be present in the final conclusion
## Working draft: draft/v1-draft - manualEdit.md, §7 (lines 214–225)

This note is a checklist for the next drafting pass on the conclusion. Five points constitute the paper's original contributions and must appear explicitly. Cross-references to where each point is argued in the body are provided so the conclusion can close those arguments rather than introduce them.

---

## Checklist

### 1. Systematic/unsystematic AI authorship as the analytical frame

**Status in current draft:** MISSING. The current conclusion uses "structured/unstructured" throughout. The reframe to "systematic/unsystematic AI authorship" (captured in `notes/systematic-ai-authorship-reframe.md`) has not yet been applied to the conclusion.

**What needs to change:** Replace or supplement "structured/unstructured distinction" with "systematic/unsystematic AI authorship" as the overarching frame. The axis is not just about method (structured vs. unstructured) but about authorship accountability — systematic AI authorship is de facto intellectual contribution; unsystematic AI authorship is unaccountable and potentially unreliable.

**Where argued in body:** §3 (the distinction); §3.3 (why it matters); connection to p-hacking and papermill risks needs to be in body before conclusion can close it — currently only in `notes/systematic-ai-authorship-reframe.md`, not yet in draft.

---

### 2. Query authorship / systematic authorship as a concept

**Status in current draft:** PARTLY PRESENT. Query authorship is named and explained in the current conclusion (paragraph 2, lines 218). The framing is good: "not the generated text but the intellectual commitments encoded in the query." However, the term "systematic authorship" as the overarching concept is absent.

**What needs to change:** Either rename "query authorship" to "systematic AI authorship" or explicitly nest "query authorship" as the mechanism within the broader "systematic authorship" concept. The conclusion should make clear that query authorship is *how* systematic authorship is enacted, not a synonym for it.

**Where argued in body:** §3.2 (what structured use looks like); §5.1 (pre-registration analogy and query authorship); §6.2 (why binary policies miss this).

---

### 3. Author-input files and session protocol as transparency artefacts

**Status in current draft:** MISSING. The current conclusion mentions "a replication package is available at GitHub" (line 220) but does not name author-input files or session summaries as transparency mechanisms. These are novel artefacts demonstrated in this paper's own production and are part of what makes this a self-demonstrating paper.

**What needs to change:** The conclusion should explicitly name author-input files (contemporaneous record of the human intellectual contribution, session by session) and the session protocol (/clear discipline, context management) as components of the replication package. These are the mechanisms that document the human/AI division of labour in real time — they are what allows a reader to distinguish AI-generated content from author-directed content.

**Where argued in body:** §4.5 (documentation and replication package — check whether author-input files are described there; if not, add before revising conclusion). The conclusion can then close: "including, in this paper, session-by-session author-input logs that document the human intellectual contribution at each stage."

---

### 4. Journal policy directive — the question that should be asked

**Status in current draft:** PARTLY PRESENT. The final paragraph of the conclusion (line 222) contains the right move: "not 'did you use AI?' but 'here is what a structured process looks like — show us yours.'" This is good. However, it is framed as a possibility rather than a directive, and it does not specify what "showing" involves operationally.

**What needs to change:** Sharpen to a directive. The conclusion should state clearly what journals should ask for: a documented process showing (a) that criteria were explicit before outputs were generated, (b) that verification checkpoints existed, and (c) that the process is reproducible from the supplementary materials. This is not a new standard — it is the application of existing replication package norms to AI-assisted workflows.

**Where argued in body:** §6.3 (documentation-based alternative). The conclusion should close §6.3's argument, not reopen it.

---

### 5. The paper as self-demonstration

**Status in current draft:** PARTLY PRESENT. Line 220 states "This article is an example of structured use of AI, and a replication package is available at GitHub." This is correct but thin. It does not connect the self-demonstrating function to the argument's force: the paper's own production *is* an instance of the practice being argued for, which means the argument is not merely normative but demonstrated.

**What needs to change:** Make the self-demonstrating point more explicit and connect it to the replication package. The conclusion should state: (a) this paper was produced via the documented pipeline; (b) the supplementary materials — including search scripts, skill configurations, screening logs, and author-input files — constitute the replication package; (c) this means the argument is not just a proposal but a proof of concept. A reader can evaluate the process, not just the product.

**Where argued in body:** §4.5 (documentation and replication package — the strongest place to develop this); §5.2 (structured use as open science practice). The conclusion closes both.

---

## Structural note for the drafting pass

The current conclusion has four paragraphs:
1. Three-claim recap (structured/unstructured, open science, policy failure)
2. Query authorship development
3. Self-demonstration + replication package
4. Empirical open question (Zeng et al.)

**Suggested restructuring:**
1. Systematic/unsystematic AI authorship as the frame — closes the conceptual argument
2. Query authorship as the mechanism — closes §5.1 and §3.2
3. Transparency artefacts (author-input files, session protocol, replication package) — closes §4.5
4. Policy directive — closes §6.3
5. Self-demonstration — closes the whole paper
6. The empirical open question can remain as the final sentence but should be *after* the directive, not instead of it

The current conclusion ends on a call for replication studies (paragraph 4). This is too weak as a closing move — it makes the argument sound provisional. The directive should be the final substantive claim; the replication call can be a coda.

---

## Things NOT to add to the conclusion
- New arguments not in the body
- Technical detail about the pipeline
- Extensive literature citations (the conclusion should close, not reopen)
- Hedges that undermine the directive — scope limitations belong in the body (§4.1 already handles scope)
