# v10 Defence Gap Assessment

**Date:** 2026-05-07
**Against:** `draft/simulation-reviews/synthesis-personas-reviews.md` and `draft/simulation-reviews/asshole-reviewer/four_attacks.md`

---

## What v10 has right

**Pre-registration reframing (Synthesis A — all 5 personas).** Solid. The section explicitly says the analogy is "one of function, not of form" and directly states that private documentation cannot provide the anti-manipulation guarantee. The distinction between what the framework gives (externalisation, auditability) and what it does not give (public anti-manipulation guarantee) is now in the text.

**Documenting ≠ verifying (Synthesis B — widest convergence).** The "What systematic use cannot guarantee" section cleanly distinguishes three tiers: what documentation *certifies*, what it *makes possible but does not certify*, and what *no regime can resolve*. This is exactly what the synthesis called for.

**Spectrum (Synthesis E, Kowalski/Delacroix).** Present and sharp: "Unsystematic use is not at one end of this spectrum. It is off the spectrum entirely." And: "partial systematic use... is better than none."

**Verification quality (Synthesis D, AI Committee/Hartmann).** The competence-threshold sentence is in place: "for a researcher extending into a subfield outside their existing expertise, the framework's protections are thinnest exactly where the verification risk is highest."

**Model version string (Synthesis F, Developer).** One sentence, in the right place: "The documentation package must include the model version string alongside prompt templates."

**Self-demonstration (N3).** The conclusion handles the sharp version correctly: it names the spectrum rather than asserting full self-demonstration, and "The conceptual moves... developed through the writing rather than from a pre-specified plan. This is what the spectrum framing predicts" is an honest and defensible move.

**Query authorship genealogy (N2 / Synthesis H).** Krippendorff is cited substantively and the "strikingly novel / it is not" sentence is now in the text: "Query authorship may appear strikingly novel. It is not. The principle... is well established. What is new is the executor and its particular failure modes." Defuses the sharpest version of Attack 2.

**Venue fit (N5).** Moot — the paper targets SMR, not Sociological Science.

**"Arguably stronger" language.** Removed. The argument is now that documentation is what makes criterion 4 satisfiable under AI-execution conditions — the correct and defensible framing.

---

## Gaps — act on before submission

### Gap 1 — ICMJE still runs as a normative source, not a motivating analogue (N1, sharpest attack)

The abstract says query authorship "satisfies the established standard for scholarly authorship." The body says it "satisfies the prior three criteria." The synthesis and defence assessment both say ICMJE should be a *motivating analogue*, not the normative framework the paper applies; the paper's actual claim is that criterion 4 *applies unchanged* but its evidentiary conditions differ once AI executes the work. The "satisfies the ICMJE criteria" language reads as treating ICMJE as the normative source for a non-biomedical context.

**What to add:** At criterion 4's first introduction, one sentence positioning ICMJE as the widely adopted evidentiary standard across social science, citing Pruschak & Hopp (2022, n=2,222), and framing the paper's use of criterion 4 as applying an established requirement to a situation the original drafters did not anticipate. Pruschak & Hopp is entirely absent from the references — a meaningful omission given the audience.

### Gap 2 — Polanyi and Collins absent (N7 / Synthesis M — generational re-description)

Mitchell et al. (2022) covers the concept of implicit tacit knowledge, but it is an organisational research paper. Polanyi (1958/1966) is the philosophical source the paper implicitly draws on, and Collins (*Tacit and Explicit Knowledge*, 2010) is the sociological extension — the name a senior sociological reviewer will look for and not find. The synthesis called Collins "the single most load-bearing name for the generational critique." Without it, the externalisation-of-tacit-commitments argument appears invented without awareness of a thirty-year sociological programme. One citation each, tied to the point where externalisation is first introduced, is sufficient.

### Gap 3 — Writing-as-thinking: the drafting caveat is missing (Synthesis C — 3+ personas)

The writing section argues that systematic use "relocates deliberate semantics to the specification layer" — the positive claim. But 3+ model agreement found that the relocation claim is *most contested for drafting*, where some arguments are formed through composition rather than expressed from prior specification. The v10 text asserts the relocation rather than acknowledging genuine uncertainty at the drafting stage. One paragraph noting that the relocation framing is most defensible for search, screening, and analytical tasks, and most contested at the drafting stage where iterative composition does epistemic work not reducible to prior specification, is the concessive move that gives the argument more room, not less.

### Gap 4 — GAIDeT and Jones (2025) absent from the policy section (N4 / Synthesis J)

The policy section acknowledges partial progress through SocArXiv and checklist proliferation, but does not name GAIDeT or Jones (2025) as tiered approaches. Attack 4's strongest form relies on those specific sources. Without naming and engaging them, the paper looks like it has not read the instruments that most directly anticipate its argument. The correct move: acknowledge these as moves in the right direction, then name the specific contribution as arguing for *which axis* tiering should be organised along. A defensible, narrower claim that cannot be dismissed as straw-manning a binary the field has already partly left behind.

### Gap 5 — Gelman-Loken not turned on the documentation process itself (Synthesis, flag for judgment)

The paper invokes Gelman and Loken (2014) against unsystematic users but does not acknowledge that the forking-paths critique applies to the logging process itself — a researcher can be broadly systematic but produce logs reflecting the cleaned-up version rather than the actual process, through ordinary retrospective rationalisation rather than dishonesty. The "What systematic use cannot guarantee" section addresses fabrication but not this subtler, more common case. One honest sentence acknowledging that working logs can reflect selected rather than complete process records, and that contemporaneous logging practice is the partial structural response, closes this.

### Gap 6 — Introduction-level provenance acknowledgement thin (N6 / Synthesis N)

The conclusion says the paper "was systematic in infrastructure and more hermeneutic in argument development" but does not explicitly state that the workflow described generalises from a particular practice (the author's) and that the defence of the generalisation is the workflow's correspondence to established methodological commitments. This is the move that neutralises the sociology-of-knowledge backchannel. One sentence in the introduction is enough; the point is to remove the element of concealment.

---

## Priority ranking

| Priority | Gap | Effort |
|---|---|---|
| 1 | Pruschak & Hopp + ICMJE-as-analogue sharpening (N1) | Low — 1–2 sentences + reference |
| 2 | Collins citation on tacit knowledge (N7/M) | Low — 1 citation at existing sentence |
| 3 | GAIDeT / Jones in policy section (N4/J) | Low — 2–3 sentences in §6 |
| 4 | Drafting-stage caveat in writing-as-thinking (Synthesis C) | Medium — 1 paragraph |
| 5 | Gelman-Loken on documentation process (flag for judgment) | Low — 1 sentence |
| 6 | Provenance acknowledgement in introduction (N6/N) | Low — 1 sentence |

The v10 draft is substantially stronger than the v3 the simulation reviews assessed. The core structural objections (pre-registration overreach, documenting ≠ verifying, verification quality, spectrum vs binary) are all handled. What remains are four citation gaps (Pruschak & Hopp, Collins, Polanyi directly, GAIDeT/Jones) and two passage-level concessions (drafting caveat, Gelman-Loken on documentation). None require reconceiving the argument.
