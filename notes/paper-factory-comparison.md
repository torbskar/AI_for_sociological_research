# Paper Factory: comparison notes for draft incorporation

**Reference:** Engzell, Per, and Nathan Wilmers. "The Paper Factory." Working paper, May 5, 2026. https://doi.org/10.31235/osf.io/24xfq_v1

## What the Paper Factory is

A multi-agent workflow that automates the full production of quantitative social science papers from an initial prompt. Researchers codify their heuristics into "expert scaffolding" — explicit, executable instructions for specialised agents. Six parallel agents assemble candidate findings, each facing adversarial critic loops. Covers data prep, viability gating, analysis, robustness checks, writing, and auditing. Explicitly scoped to quantitative research on large-scale, population-representative data.

---

## Where the Paper Factory strengthens this paper's argument

**Expert scaffolding = forced externalisation of tacit knowledge — but only the articulable component.** The Paper Factory's core claim — that researchers must codify their "hidden curriculum" into explicit, executable scaffolding before the pipeline can run — is a more radical implementation of this paper's tacit-knowledge-externalisation argument, and useful as a limiting case. But it also exposes a foundational problem: complete externalisation is not realistic.

Using the Mitchell et al. distinction (already in this paper), expert scaffolding can capture *implicit* tacit knowledge — the articulable component that the researcher could spell out if pressed: inclusion criteria, methodological preferences, theoretical framings, quality checklists. It cannot capture *inherent* tacit knowledge — the genuinely ineffable component: a practitioner's sense of whether a finding is surprising or artifactual, whether a question is interesting or merely answerable, whether a synthesis has missed the point while satisfying every stated criterion. These resist articulation not because the researcher hasn't tried hard enough, but in principle. Better prompts reach an asymptote.

The failure mode when the pipeline runs on an incomplete specification is specific: the system produces output that is internally coherent and satisfies all stated criteria while violating criteria the researcher never articulated. The pipeline cannot flag its own incompleteness. The researcher may recognise that something is wrong without being able to say what — and must then either override the output on intuition (tacit judgment re-entering undocumented) or accept it because no specific objection can be formed. The second path is dangerous: confident, coherent, wrong in ways invisible to the specification. E&W frame this risk as a prompt-quality problem — better prompts will capture more of the curriculum. But if some component is inherent rather than implicit, this is wrong: it is a structural feature of automated pipelines that cannot be resolved by better scaffolding.

A second failure mode compounds this. When researchers attempt to codify their expertise, they simplify their own process to make it executable — producing the "greatest hits" version of their methodology. The codification is not a partial transcript of expertise; it is a caricature. Agents optimise for the explicit rules while the broader critical context that normally surrounds them is absent. The output hyper-conforms to the stated criteria while bypassing exactly the skeptical judgment that would usually qualify them. This is distinct from incomplete externalisation: the problem is not only that some tacit knowledge resists articulation, but that the act of codification itself introduces distortion.

A third failure mode is error propagation. If a misframing or hallucination enters the pipeline early — in literature mapping, in problem setup — it becomes foundational assumption for all subsequent agents. By the time the human reviews a finished, internally coherent document, they are epistemically worse-positioned to spot the foundational flaw than during turn-by-turn interaction. The document's internal coherence actively works against detection: everything hangs together because everything was built on the same error. This sharpens the human-verification argument: checkpoints are not only quality control at each stage but prevention of error compounding across stages.

**This clarifies why human verification at each stage is epistemically necessary, not merely conservative.** The verification checkpoint is not only a check against AI error; it is the structural mechanism by which inherent tacit knowledge enters the research process. A researcher reviewing a synthesis output applies knowledge they could not have fully specified in advance. Remove verification and you have not reduced oversight — you have severed the channel through which the ineffable component of expert judgment operates. This paper's framework preserves that channel; the Paper Factory at full automation closes it. Use this to sharpen the verification-asymmetry argument: the issue is not just that interpretive tasks are harder to check, but that the checking *is* the epistemic contribution.

**Documentation of all forking paths.** An automated pipeline records every decision fork as a byproduct of how agents log instructions — automatically, completely, without risk of selective retention. On this specific property, the automated approach produces stronger artefacts than private session logs. Worth acknowledging as a genuine strength.

**"Observable, auditable, accountable."** Engzell and Wilmers use this language for what the workflow produces — maps directly onto the documentation package argument.

---

## Where this paper is right and the Paper Factory goes too far or past the point

**The authorship problem is unaddressed.** When the human role is reduced to providing an initial concept prompt and reviewing the output, does the researcher satisfy ICMJE criterion four? The Paper Factory does not ask this question. The authorship gap is *larger* in their case than in the manually-assisted case, not smaller. The ICMJE framing is a genuine contribution the Paper Factory lacks.

**Scope.** The primary demonstration in E&W is quantitative work on large-scale, population-representative data, and this is where their engineering claims are grounded. However, their *theoretical* framing — codifying research heuristics into executable scaffolding — is stated as domain-agnostic: any research task that can be decomposed into expert-led instructions is in principle automatable. E&W gesture at extensions to qualitative synthesis (coding rubrics applied at scale by a "Skeptic Agent"), theoretical mapping (Bourdieuian analysis, adversarial theory critics), and dissemination (policy translation agents). These extensions are aspirational rather than demonstrated; the paper does not show a working qualitative or theoretical factory, only sketches one.

The qualification matters because the scope argument in this paper cannot rest solely on E&W's demonstrated application. The more defensible claim is narrower: the verification asymmetry, not the scope restriction, is what distinguishes the two approaches. For tasks where correctness is externally checkable — a regression coefficient, a merge rate, a top-code — adversarial-agent verification can substitute for human review. For tasks where correctness depends on disciplinary interpretation — whether a passage instantiates institutional distrust, whether a theoretical framing is coherent — the agent has no independent standard against which to check, and the "Skeptic Agent" can only flag internal inconsistency, not substantive error. The authorship problem sharpens in exactly this domain: a factory that produces plausible-sounding thematic codes generates the bullshit problem at qualitative scale. E&W acknowledge the risk of "mediocrity at scale" — technically proficient but substantively empty papers — but treat it as a prompt-quality problem. This paper's framing is that it is an authorship problem: without a researcher who can recognise when the interpretation is wrong, criterion four cannot be satisfied regardless of how well the heuristic was codified.

**The verification asymmetry.** Adversarial-agent verification may work for well-specified quantitative procedures. For interpretive and conceptual work — where the researcher's disciplinary judgment is the primary epistemic instrument — agent-to-agent verification cannot substitute for the researcher recognising when an output is wrong. Human-verification-at-each-stage is not conservatism; it is calibrated to verification risk in a different problem space.

**Sycophancy at scale.** Multiple agents from the same or similar models may share systematic biases rather than provide genuinely independent perspectives. Cross-model persona review (this paper's approach) addresses model-level bias more directly than multi-instance parallelism from the same architecture.

**Engineering versus epistemic warrant.** The Paper Factory provides an engineering solution to research quality. This paper provides the epistemic warrant — the framework under which a reader can assess whether the accountability conditions for authorship are satisfied. The Paper Factory can generate auditable artefacts without providing an argument for why those artefacts should ground epistemic trust.

---

## Draft incorporation notes

- **Footnote 3 tension** (already flagged re Sant'Anna): the Paper Factory makes the explicit live counterargument. Consider lifting this from a note into brief in-text acknowledgment, resolved by scope: for well-specified quantitative tasks, automated pipelines produce strong artefacts; the authorship question remains unanswered by the architecture and requires this paper's framework regardless of automation level.

- **Tacit knowledge / externalisation section**: use "expert scaffolding" as a concrete practical illustration of forced externalisation. Engzell and Wilmers provide the practitioner-facing term for what this paper describes philosophically.

- **Does not threaten the argument**: the Paper Factory describes a limiting case that maximally instantiates the externalisation requirement while entirely skipping the epistemic question this paper answers. Frame as complementary, not competing.
