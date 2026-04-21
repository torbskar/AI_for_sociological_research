# Synthesis: Persona Reviews
**Date:** 2026-04-19 (updated 2026-04-21 with asshole-reviewer material)
**Models covered:** Claude (all 6 personas), Gemini (all 6 personas), ChatGPT (Personas 1–2 only — free tier limit reached), plus Persona 7: asshole-reviewer (public attacks + backchannel critiques + internal defence assessment)
**Protocol:** Act on objections raised by 2+ models independently; flag for judgment those raised by only one; note divergence as a signal of genuine ambiguity. The asshole-reviewer is a single-source voice but is deliberately adversarial and routes around existing defences — its attacks are treated as serious if not rebutted by existing concessions.

---

## By persona

### Persona 1: Delacroix (theoretical sociologist, anti-positivist) — Claude, Gemini, ChatGPT

**Convergent across all three models:**

- *Pre-registration analogy overextended.* All three flag it: logs are private, retrospective, and researcher-controlled; they do not function as binding constraints. Claude presses hardest on the "in principle" hedging in §5.1; Gemini calls it "hermeneutic suicide"; ChatGPT simply says the analogy is "private and retrospective" and should be weakened.
- *Query authorship asserted, not argued.* All three agree the concept is interesting but underdefended. Claude wants engagement with the philosophy of authorship; Gemini accuses it of reducing the researcher to a "prompt manager"; ChatGPT calls it "infrastructural authorship" and treats it as a promising but undeveloped line.
- *Scope limitation inadequate.* All three press this, though from slightly different angles. Claude argues that the pipeline model is implicit in the whole paper and that the categories used (literature search, synthesis) are not neutral; Gemini insists categorisation is theoretical work; ChatGPT says the normative implications extend beyond the declared domain.
- *Externalisation of tacit knowledge may distort inquiry.* All three raise it. The Polanyi/Bourdieu concern — that forcing tacit commitments into explicit criteria is not a neutral act but may destroy what it describes — is the shared underlying worry.

**Divergence (informative):** Claude is the sharpest on the logical structure of the pre-registration disanalogy and does not dismiss the paper overall. Gemini is angrier and more rhetorical; some of the Gemini critique reads as in-character performance rather than precision (e.g., "hermeneutic suicide," the Lacanian "Other" riff). ChatGPT is the most compact and least hostile. The convergence is real; the Gemini register should be discounted somewhat.

**Genuinely interesting acknowledgement (all three):** The adversarial configuration (§4.5) and query authorship concept are named as the strongest contributions even by the most resistant persona.

---

### Persona 2: Philosopher (writing-as-thinking) — Claude, Gemini, ChatGPT

**Convergent across all three models:**

- *The drafting stage is where the relocation claim is weakest.* All three argue — with different vocabulary — that writing is not the expression of a prior thought but sometimes the act by which the thought is formed. ChatGPT is sharpest: some commitments are "not yet formed until writing forces them into being." Claude distinguishes generative resistance from revision. Gemini frames it as the "recursive nature of drafting."
- *"Relocation" is not a neutral redistribution.* All three reject the claim that effort at specification is equivalent to effort at generation. ChatGPT explicitly says cognition is "non-modular and temporally extended"; Claude argues the two kinds of effort produce qualitatively different outputs; Gemini calls revision a "checker mindset" versus the "generative, synthetic mode" of drafting.
- *A caveat about the drafting stage is needed.* All three recommend one, with similar content: that delegating prose generation risks attenuating the cognitive function through which arguments are formed, not merely expressed.

**Divergence:** Gemini adds a long-term atrophy concern ("cognitive parasitism") that neither Claude nor ChatGPT raises — and that is probably too speculative for this paper. Claude's formulation is the most precise and the most intellectually fair: the concern is not about craft but about a specific class of cognitive events, and it is most serious for theoretical and methodological work where the paper is working something out rather than expressing something already worked out. The Gemini review also acknowledges — unusually for this persona — that the structured approach is a genuine improvement and that the adversarial configuration moves toward dialogue.

**Most useful specific contribution (Claude-philosopher):** The observation that this very paper may be an instance of work where the text partly constitutes the argument — making the relocation claim self-undermining if applied to the paper's own composition. This is a sharp and honest point that the caveat should acknowledge.

---

### Persona 3: Hartmann (applied microeconomist) — Claude, Gemini

**Convergent across both models:**

- *Pre-registration analogy: bound it explicitly.* Both press the same gap: the analogy gives the externalisation benefit but not the anti-manipulation benefit. Claude is precise: git timestamps are "trivially malleable" and a researcher who reconstructs a plausible log after the fact leaves no distinguishable trace. Gemini: distinguish "intent documentation" from "inferential constraint." Both recommend reframing as **auditability**, not replication.
- *Documenting process does not verify output.* Both raise this as the central caveat the paper needs. The framework documents that criteria were prior and explicit; it does not certify that the AI's execution of those criteria was accurate. Documentation is a prerequisite for evaluation, not a certificate of validity.
- *Verification checkpoints are the weakest link.* Both push on this. Gemini explicitly recommends audit samples and inter-rater reliability between human and AI output. Claude asks: verifiable to whom, and how?

**Genuinely positive (both):** Both find the ICMJE reframing and the adversarial configuration to be the paper's strongest and most practically useful contributions. Gemini specifically names the PII hook and .claudeignore as immediately adoptable.

**Divergence:** Claude presses harder on the productivity-versus-documentation conflation — the quality argument is in a different evidential register from the documentation argument and the paper blurs this. Gemini adds a call for audit metrics and IRR scores that goes further than the paper needs to engage with.

---

### Persona 4: Kowalski (political scientist, methods pluralist) — Claude, Gemini

**Convergent across both models:**

- *Pre-registration: the social/institutional accountability mechanism is missing.* Both argue the pre-registration analogy works at the level of process design but not at the level of enforcement. Gemini: the social cost of visible deviation is what gives pre-registration its disciplinary force; a private git log lacks this. Claude: the researcher can run the AI many times, find a favourable output, and begin logging from that point; logs document what was retained, not the full decision landscape.
- *Git malleability.* Both flag it directly. Claude notes that OSF registration at project outset, or pushing to a remote at time of each commit, is the structural fix. Gemini suggests cryptographic hashing.
- *The binary framing creates problems.* Both argue the systematic/unsystematic distinction is presented as categorical when partial compliance is common and better than none. A graded account — or at least acknowledgement that the category is a spectrum — would make the framework more adoptable.

**Sharp new point (Claude-Kowalski only, worth flagging for judgment):** The Gelman-Loken forking-paths critique applies to the documentation process itself, not just to the research process. A researcher can be broadly systematic but produce a log that reflects the cleaned-up version rather than the actual process — not through dishonesty but through ordinary retrospective rationalisation. The paper invokes Gelman-Loken against unsystematic users but never turns the critique on its own proposed solution. This is a genuine gap.

**Underselling (Claude-Kowalski only):** The grounded synthesis design in §4.2 — submitting queries against the specific relevant-theme documents rather than a general-purpose chat — is the most distinctive practical contribution for readers who already use AI for coding and are considering extension to synthesis. The paper mentions it briefly and moves on.

**Disclosure standard (both):** Both press for a more concrete policy output. Claude proposes a draft attestation template; Gemini proposes a "Systematic AI Supplement (SAIS)" with four artefacts. The paper gives journals a direction but not an instrument.

---

### Persona 5: AI Committee — Claude, Gemini

**Convergent across both models:**

- *Systematic/unsystematic maps onto appropriate/inappropriate use; the analogy largely holds.* Both agree and develop the mapping well. The certification analogue in research = attributed competence; the paper's documentation framework addresses this.
- *Writing-as-thinking / cognitive depth concern.* Both raise it, though with different vocabulary. Gemini focuses on "serendipitous insights" from the struggle of manual composition; Claude focuses on metacognitive laziness — the condition in which a researcher believes they are exercising judgment while not being able to.
- *Verification quality underspecified.* Both press this. The framework creates conditions for good verification but does not specify what makes verification credible. The human verification checkpoint could be a checkbox or a genuine test; the paper does not distinguish.
- *Automation bias.* Both mention it: the tendency to trust automated suggestion even when exercising formal oversight. Configuring the AI to be critical helps on the AI side; it does not address the researcher's tendency to accept plausible-seeming critical outputs without substantive evaluation.

**Sharp point (Claude-AIcommittee only, flag for judgment):** The competence threshold problem — the paper is calibrated for experienced researchers with deep domain expertise, but does not say so. A junior researcher or a researcher using AI to extend into a subfield outside their core expertise is in a structurally different position, and the framework's protections are thinnest exactly where the risk is highest.

**Sharp point (Claude-AIcommittee only, flag for judgment):** Thin-but-genuine documentation — a researcher who followed the workflow procedurally without the intellectual substance the framework is designed to certify. The paper acknowledges fabrication; it does not engage with this more common adjacent case.

---

### Persona 6: Developer — Claude, Gemini

**Convergent across both models:**

- *Model version pinning absent.* Both flag this as the most significant gap in the reproducibility argument. The same prompt against different model versions produces meaningfully different outputs; a replication package without a pinned model string reproduces the form of the workflow but not the conditions under which it produced the documented outputs. Both recommend explicit model version logging.
- *Reproducibility should be framed as auditability.* Convergent with Hartmann. AI workflows produce auditable process records; they do not produce reproducible outputs in the sense that re-running a script produces the same numbers.
- *.claudeignore and PII hook are the strongest parts.* Both identify these — structural data access control as a genuine technical contribution that goes beyond documented intention to enforced boundary.

**Divergence:** Claude presses the chat-interface/API-interface distinction — the whole configuration architecture depends on Claude Code semantics and is substantially different in a chat interface, and the paper does not say this. Gemini focuses more on context drift within a single long session ("lost in the middle" — criteria followed at the start, ignored after 40 minutes of accumulated context). Both are real problems; the chat/API distinction is more fundamental for this paper's claims.

**Gemini-developer's "clean room" protocol** — a fresh session for every major stage — is consistent with what the paper already recommends for the review stage; extending this norm to all stages would strengthen the reproducibility argument.

---

## Cross-persona convergence: what the synthesis protocol requires

### Act on — 4+ independent instances

**1. Pre-registration analogy needs reframing**
Raised by all five personas across all models. The planned revision (spectrum, more flexible framing, explicit acknowledgement that the framework can be combined with formal pre-registration but is not equivalent to it) directly addresses the core concern. What the paper also needs to add: a clear statement of what the framework *does* give (externalisation discipline, auditability, process legibility) versus what it does *not* give (binding constraint, publicity, anti-manipulation guarantee). The current "real but not fatal" treatment is insufficient.

**2. Documenting process ≠ verifying output**
Raised by Hartmann (both models), Kowalski (both models), and Delacroix (Claude). This is the most actionable single caveat. The paper should add a concise statement distinguishing: what documentation certifies (criteria were prior and explicit), what it makes possible but does not certify (output accuracy), and what remains genuinely unverifiable under any documentation regime (non-deterministic execution against possibly changed models).

**3. Writing-as-thinking / drafting stage caveat**
Raised by Philosopher (all three), AI Committee (both), Gemini-Delacroix. Add a caveat in §4.4 or §5.1 acknowledging that the relocation framing is most defensible for literature search, screening, and analytical tasks; it is most contested for drafting, where some arguments are formed through the act of composition rather than expressed from prior specification. One paragraph; honest but not capitulating.

**4. Verification quality**
Raised by AI Committee (both), Hartmann (both), Kowalski (Claude). Add a sentence or two noting that human verification is only as good as the human doing it; the framework creates conditions for credible verification but does not guarantee it; competence and genuine critical orientation matter.

### Act on — 2–3 instances

**5. Spectrum, not binary**
Kowalski (both), Delacroix (Gemini, ChatGPT). A brief acknowledgement that systematic/unsystematic is a spectrum; partial compliance is better than none; the framework is a direction, not a bright line.

**6. Model version as replication caveat**
Developer (both), Hartmann (Claude, implicit). Add a sentence to the replication package section noting that a complete documentation record includes the model version string alongside prompt templates, and acknowledging that outputs against a later model version may differ.

**7. Git timestamps are soft evidence**
Kowalski (both), Hartmann (Claude). Calibrate the claim: git commit history provides contemporaneous evidence that is substantially harder to fabricate than no record, but it is not equivalent to a pre-registration server timestamp. OSF registration at project outset would strengthen the integrity claim.

### Flag for judgment — raised by one model only

- **Gelman-Loken applied to documentation itself** (Kowalski-Claude) — the forking-paths critique applies to the logging process, not just the research process. Sharp and true, but engaging with it risks undermining confidence in the paper's own proposed solution. Consider a single honest sentence in limitations.
- **Competence threshold / junior researcher vulnerability** (Claude-AIcommittee) — a single sentence in scope limitations would address this without expanding the paper.
- **Chat interface vs Claude Code distinction** (Claude-developer) — technically correct but may be too narrow for a Sociological Science audience. A footnote acknowledging that the workflow as described requires Claude Code or equivalent rather than a chat interface would suffice.
- **Grounded synthesis undersold** (Kowalski-Claude) — an opportunity, not a problem. Could strengthen §4.2 with two additional sentences for readers already using AI for coding.
- **Thin-but-genuine documentation** (Claude-AIcommittee) — the researcher who follows the workflow procedurally without the intellectual substance. More concerning in practice than outright fabrication. Could be absorbed into the verification quality caveat.

---

## Suggested revision actions

Given the stated plan — adjust, sharpen, improve limitations and caveats, implement the pre-registration/spectrum reframing:

**A. Pre-registration reframing (§3.2 and §5.1)**
Replace the current "real but not fatal" treatment with a direct statement of what the framework offers and what it does not. Tie to the spectrum argument in `notes/preregistration-analogy-limits-and-spectrum.md`. Key addition: the framework does not provide the publicity and anti-manipulation guarantee of pre-registration, but it can be combined with formal pre-registration for researchers who want that guarantee, and it provides the externalisation discipline regardless. The spectrum point — that implementation ranges from informal discipline to full pre-registration — handles both the economist's critique (too weak) and the theorist's critique (too rigid).

**B. Documentation ≠ verification caveat (§5.4)**
A short paragraph distinguishing three tiers: what documentation certifies (criteria were prior and explicit); what it makes possible but does not certify (output accuracy); what remains unverifiable under any documentation regime (non-deterministic execution, model version change). Frame the whole as "auditability" rather than "replication." This is the single caveat that does most work with the widest range of sceptical readers.

**C. Writing-as-thinking caveat (§4.4 or §5.1)**
One paragraph acknowledging that the relocation claim is strongest for search, screening, and analytical tasks; most contested for drafting; and that researchers for whom the text partly constitutes the argument should treat the drafting stage as the one where the framework's assumptions are most likely to require individual adjustment. The paper need not concede the point — it should acknowledge the genuine uncertainty.

**D. Verification quality (§5.4 or §3.2)**
One or two sentences noting that human verification checkpoints are only as good as the researcher's domain expertise and critical orientation; the framework creates the conditions but does not guarantee the substance.

**E. Spectrum acknowledgement (§3.2)**
Two to three sentences noting that the systematic/unsystematic distinction is a spectrum; the framework defines the features of the systematic end without implying that partial compliance is without value. This also positions the pre-registration combination as the far end of the spectrum rather than a separate thing.

**F. Model version and git calibration (§5.4 or supplementary materials section)**
One sentence each: model version pinning as a required element of a complete replication package; git timestamps as soft but meaningful evidence that stops short of the pre-registration server standard, with OSF registration noted as the option for researchers who want stronger integrity guarantees.

---

## Persona 7: Asshole-reviewer — public attacks and backchannel critiques (added 2026-04-21)

This persona supplies a deliberately adversarial reading in two registers: five public attacks designed to survive contact with the defences already in the v3 outline, and two backchannel critiques (sociology-of-knowledge read; generational read) that target the author rather than the argument. A companion defence-assessment memo drafts pre-emptive textual moves for the attacks it judges damaging. The material is single-source but introduces several objections absent from the six-persona synthesis above, and some of them land.

### What is genuinely new (not covered by Personas 1–6)

**N1. ICMJE criterion 4 is institutional, not evidentiary (Attack 1).**
The ICMJE criteria commit the *named author* to answer for the work; criterion 4 is not a standard about what kind of record exists, but about who can be summoned. The v3 move that a contemporaneous paper trail is "arguably a stronger" form of accountability substitutes a process-property for a person-property. This is the single most fixable public weakness. The Hartmann and AI-committee personas pressed verification quality and auditability but did not touch this specific category distinction.

*Update 2026-04-21 — evidence from Elicit query on sociology authorship norms ([literature/Elicit_export/Elicit-authorship-ICMJE.md](literature/Elicit_export/Elicit-authorship-ICMJE.md)):*

- **The paper's use of ICMJE as a reference point for sociology is empirically defensible.** Pruschak (2021) and Pruschak & Hopp (2022, n=2,222) find that social scientists adhere to ICMJE-style criteria in practice even without formal instruction, and Bebeau & Monson (2011) show broad agreement across psychology, sociology, and education codes of ethics. The ASA maintains explicit sanction authority. This partly softens the generational re-description (N7) *for this specific move*: invoking ICMJE for sociology is not a category error at the venue level; it is the de facto standard. The paper can strengthen the move by citing Pruschak & Hopp rather than treating ICMJE as a foreign import.
- **The literature unambiguously confirms Attack 1's reading of criterion 4.** The Elicit summary renders criterion 4 as "Agreement to be accountable for all aspects of the work — meaning the author can ensure that questions about accuracy or integrity are appropriately investigated and resolved." This is a commitment by a person, not a property of a record. The AI-authorship consensus since 2023 is grounded in exactly this: AI cannot be listed as author *because* it cannot satisfy criteria 3 and 4 — it cannot approve, cannot be accountable. The criterion is being actively used in the field as a personhood test, not as an evidentiary test. This makes the "arguably stronger" line more exposed, not less: any reviewer alert to the AI-authorship debate will read that line as collapsing the same distinction the AI-authorship consensus relies on to exclude AI.
- **CRediT is a better vehicle than the paper currently recognises.** The Elicit summary frames CRediT (14 contributor roles) as complementing ICMJE by making contribution patterns transparent without replacing the authorship threshold. This is directly relevant to N4 (tiered disclosure) and to revision action J: CRediT is an existing tiered contribution-documentation standard that the paper can position its workflow artefacts alongside, rather than arguing against a binary the field has already partly left behind. A researcher's CRediT attribution for "Conceptualization," "Methodology," "Writing — Original Draft" is exactly the kind of pre-specified-contribution claim the workflow artefacts support or fail to support. This gives revision action H (query-authorship genealogy) an additional, sociology-native precedent and gives revision action J a concrete existing instrument to build on.
- **Revised revision action G**: The draft text for §5.5 (in defence_assessment.md §Attack 1) now needs two small additions: (i) cite Pruschak & Hopp (2022) at the point where ICMJE is introduced, positioning it as the empirical norm in social science; (ii) note that the AI-authorship consensus rests on criterion 4 read as personhood-accountability, and that the paper's analogical use of criterion 4 is an *evidentiary supplement to* rather than a *substitute for* that personhood commitment — which is precisely why AI cannot be an author under the framework the paper proposes. This turns the demotion from a defensive move into a constructive one: the paper's framework gives journals a concrete instrument for evaluating whether the human authors' claimed criterion-1-and-2 contributions are substantively present, without disturbing the criterion-3-and-4 ground on which AI is excluded.
- **New revision action O — CRediT integration (§5.5 or §6.2).** Add one paragraph positioning the systematic-AI-use workflow artefacts as evidence supporting (or failing to support) specific CRediT role claims — particularly Conceptualization, Methodology, Formal Analysis, and Writing (Original Draft). This makes the policy recommendation concrete and ties it to an instrument large publishers already use.

*Further clarification 2026-04-21 — scope of the authorship argument.*

The paper does **not** argue about whether AI should be listed as an author. That question is settled: the post-2023 consensus is that AI cannot be an author precisely because it cannot satisfy criteria 3 and 4, and the paper does not contest this. What the paper addresses is the *human* authorship situation when AI executes substantial parts of the work (writing, searching, screening, drafting). The human remains the author and bears criterion-4 accountability; the framework's purpose is to produce the evidence that makes that accountability substantive rather than nominal.

This sharpens the response to the second Elicit bullet (criterion 4 as personhood-accountability) considerably:

- The paper and the AI-authorship consensus are on the same side of the criterion-4 distinction. Both treat criterion 4 as a personhood commitment that AI cannot satisfy. The paper's contribution is downstream: *given* that the human is the accountable author, what does criterion 4 require of them when AI did much of the execution? The answer proposed is that the human must be in a position to answer for what the AI did — which requires the kind of documentation the framework produces.
- This means the "arguably stronger" line can be repaired without retreat. The framework does not claim to be a stronger form of ICMJE accountability; it claims to be what criterion 4 *substantively requires* for human authors of AI-assisted work. Memory-based reconstruction satisfies criterion 4 for traditional work because the human executed the work and can answer for it from recall. For AI-executed work, memory-based reconstruction cannot do the same epistemic job, because the human did not execute the work — so criterion 4 accountability requires an additional evidentiary support that was unnecessary before. The framework is not stronger than ICMJE; it is what ICMJE already requires in a situation the original drafters did not anticipate.
- Revision action G is therefore tighter than the first draft of the defence text suggested. The move is not "ICMJE is a motivating analogue" but "criterion 4 applies unchanged; the evidentiary conditions under which a human can substantively satisfy it differ once AI executes the work, and the framework specifies those conditions." This preserves the ICMJE move in §5.5 and §6 without the category-error exposure, and it is more accurate to what the paper actually contributes.
- The generational re-description (N7) also loses force for this specific move: the paper is not reinventing authorship theory; it is making a narrow claim about what an established criterion requires under conditions the criterion's drafters did not face. Cite Pruschak & Hopp for the empirical standard and the AI-authorship consensus for the criterion-4-as-personhood reading, and the argument is situated rather than freelance.

*Further literature input 2026-04-21 — Elicit query on tacit knowledge ([literature/Elicit_export/Elicit-Tacit-knowledge.md](literature/Elicit_export/Elicit-Tacit-knowledge.md)):*

**Assessment: substantially covers the Polanyian ground but leaves two named gaps.** The Elicit summary provides what revision action M required for the tacit-knowledge pillar — Polanyi (1958, 1966), the "we can know more than we can tell" formulation, the dwelling metaphor, Hadjimichael et al. (2023) on Polanyi in organisational theory and theory development, and the reflexivity literature (Corlett & Mavin 2017; Berger 2015; Folkes 2022; Sibbald et al. 2025; Trundle et al. 2025). This is enough to ground the paper's externalisation-of-tacit-commitments language in an identified tradition rather than leave it free-floating.

Two productive sharpenings from the summary the paper should absorb:

- **Sibbald et al.'s performance-vs-practice distinction is a direct gift to the argument.** A "shopping list" positionality statement — listing one's attributes to satisfy a formal requirement while doing no actual reflexive work — is the qualitative-methods equivalent of the disclosure-based AI policy the paper critiques. The paper can cite Sibbald to argue that the reflexivity literature has already recognised that declaration without substance is a failure mode, and that the systematic/unsystematic distinction applies the same structural insight to AI use. This strengthens both the AI-policy critique in §6 and the generational-read defence: the paper is participating in a known methodological conversation, not reinventing it.
- **Marques (2021) on the erasure of the subject in academic writing conventions** connects to the writing-as-thinking concern (Persona 2 / revision C) and to the query-authorship argument. The passive-voice/impersonal-construction convention performs a withdrawal of authorship; the paper's proposal is that AI-assisted work requires re-inserting the author evidentially. One-sentence connection, useful.

**Remaining gaps that this Elicit pass does not fill:**

- **Harry Collins is not covered.** Collins is the sociologist who most extensively developed Polanyi's ideas into an empirical programme — the sociology of scientific knowledge (SSK), the typology of relational/somatic/collective tacit knowledge (*Tacit and Explicit Knowledge*, 2010), the experimenter's regress, the studies of tacit skill transmission in laboratory science. For the generational re-description (N7) in its sharpest form, Polanyi alone is insufficient because the critique is that *sociology* has been thinking about tacit knowledge for decades. Citing Polanyi covers the philosophical ground; citing Collins covers the sociological extension and shows the paper is aware of the disciplinary conversation, not just the philosophical foundation. A targeted supplementary search for Collins (and possibly Collins & Evans on expertise) would close this gap — it is the single most load-bearing name for the generational critique that the current Elicit summary omits.
- **Krippendorff on content analysis is not covered here and was not expected to be.** That literature is a separate pillar required by revision action H (query-authorship genealogy in §5.1 / §3.2) and by Attack 2 on the novelty claim. Krippendorff (2019, *Content Analysis: An Introduction to Its Methodology*, 4th ed.) is the canonical reference; a targeted search against Krippendorff, PRISMA/Cochrane, and computational-content-analysis training-regime practice is still needed. The tacit-knowledge Elicit does not and should not supply it.
- **Qualitative-methods tradition on coder training and negotiated coding** is not directly covered. The reflexivity literature surfaced here addresses researcher standpoint; the coder-training literature addresses how interpretive decisions are documented and transferred across multiple analysts. These are adjacent but distinct. Saldaña's *Coding Manual for Qualitative Researchers* or Campbell et al. on inter-coder agreement would cover it. Lower priority than Collins and Krippendorff, but worth one citation if possible — it is the most direct precedent for the "query authorship = pre-specified rubric executed by a non-author" logic.

**Updated status of revision action M.** Polanyi pillar: covered. Reflexivity pillar: covered with useful sharpening (Sibbald; Folkes; Marques). Collins pillar: still needed. Krippendorff pillar: still needed (routes via revision action H, not M). Coder-training pillar: optional but available.

**Net answer to the question: for tacit knowledge specifically, yes — this covers sufficient ground provided Collins is added.** The reflexivity literature supplied is an unexpected bonus that actively strengthens the paper's argument (via Sibbald's performance-vs-practice distinction) rather than merely discharging a literature-review obligation. The two remaining named gaps (Collins, Krippendorff) sit outside the tacit-knowledge query's natural scope and require their own targeted searches.

**N2. "Query authorship" has clear precedents in systematic review, content analysis, and computational text analysis (Attack 2).**
Cochrane/PRISMA on search specification; Krippendorff on coding rubrics; computational text-analysis training regimes. Each treats pre-specified criteria as the locus of intellectual contribution independent of who or what executes them. The paper's own cited antecedents (Momeni et al. 2025; Törnberg 2024; Davidson & Karell 2025) partially encode this logic already. The contribution survives as *extension to a new executor with distinctive failure modes*, but not as a new concept. Personas 1 and 4 touched the "asserted, not argued" objection but did not supply the genealogy.

**N3. Self-demonstration holds for the literature-review component only (Attack 3).**
The paper's central conceptual moves (systematic/unsystematic distinction, query-authorship concept, ICMJE reframing) were not pre-specified — they emerged during writing. By the paper's own definition of query authorship, the documented artefacts certify the literature-search component but not the conceptual contribution. This is sharper than Persona 2's writing-as-thinking caveat: it is an internal-consistency point, not a phenomenological one.

**N4. The "binary policy" target is already being abandoned by the field (Attack 4).**
GAIDeT is tiered; Jones (2025) is an explicit disclosure heuristic; Davidson & Karell (2025) specify tasks rather than AI-presence; Zrubka et al.'s checklist-count range (10–66) is evidence of tiering, not binarism. The paper's §6 attacks a version of the field that §2 partly concedes has moved on. The Kowalski persona's spectrum point was adjacent but did not engage the specific sources.

**N5. Venue fit and the replication-package move (Attack 5).**
*Sociological Science*'s replication requirement (April 2023) exists to support reproduction of reported estimates. This paper reports none. Using the requirement as leverage to argue journals "face a consistency challenge" in treating AI workflow documentation differently conflates reproducibility-of-estimates with auditability-of-process. The infrastructural-compatibility claim is defensible; the consistency claim is not. No other persona raised venue fit.

**N6. Backchannel — sociology-of-knowledge read.**
The paper is the author's own project folder re-presented as methodology. The self-demonstration concession ("systematic in infrastructure, hermeneutic in argument") invites the re-description that the infrastructure records rather than produces the work. This cannot be rebutted textually because it is about what kind of paper this is; partial defence is narrower contribution claims plus an explicit statement in the introduction that the paper generalises from a particular practice.

**N7. Backchannel — generational read.**
Polanyi, Collins on tacit knowledge, and Krippendorff are absent. The qualitative-methods tradition on coder training, negotiated coding, and documentation of interpretive decisions is absent. The concepts being proposed ("externalising tacit commitments," "query authorship") have been the received view in a neighbouring subfield for decades. Only defence: engage the literature in the text. A paper that has demonstrably read it cannot be dismissed as written by someone who has not.

### How these interact with Personas 1–6

- **N1 supersedes and sharpens** the verification/auditability convergence from Hartmann, Developer, and AI Committee. Their shared recommendation (reframe as auditability) now carries an additional requirement: stop treating ICMJE as a normative source.
- **N2 strengthens and narrows** the cross-persona press on query authorship (Delacroix, AI Committee). The fix is constructive: state the genealogy, narrow the contribution to extension + policy implication.
- **N3 does not replace** Persona 2's drafting-stage caveat; it adds an internal-consistency dimension that the Persona 2 caveat alone does not cover.
- **N4 extends** Kowalski's spectrum point from a property of the proposal to a description of the field.
- **N5 is orthogonal** to all six personas and is the only venue-level objection surfaced in the review set.
- **N6–N7 do not have textual refutations**; they set a literature-engagement requirement and an introduction-level framing requirement.

### Updated revision actions (supersedes earlier list where marked)

**G. ICMJE demotion (§5.5 and abstract) — SUPERSEDES earlier treatment.**
Remove "arguably stronger." Reframe ICMJE from normative source to motivating analogue. Documentation is an *evidentiary supplement* to criterion 4, not a substitute for the accountable-commitment the criterion names. Draft text available in `asshole-reviewer/defence_assessment.md` §Attack 1.

**H. Query-authorship genealogy paragraph (§5.1 or §3.2) — NEW.**
Insert a paragraph acknowledging Cochrane/PRISMA, Krippendorff, and the computational content-analysis tradition as precedents. Restate the contribution as *extension to an executor with distinctive failure modes (sycophancy, generalisation bias, non-determinism) plus a specific policy implication*. Draft text available in defence_assessment.md §Attack 2. This also discharges part of N7 (generational read), provided Krippendorff is cited substantively.

**I. Self-demonstration scope sentence (§5.4) — NEW, single sentence.**
Append: the self-demonstration claim holds for the literature-review component, not for the conceptual contribution, which developed hermeneutically and is accommodated by the §3.4 spectrum rather than by the narrow definition of query authorship. Draft text in defence_assessment.md §Attack 3.

**J. Field-state acknowledgement (§6.1–6.2) — NEW, supersedes earlier E where it conflicts.**
Open §6.2 by acknowledging that the field is already moving toward tiered disclosure (GAIDeT, Jones 2025, Davidson & Karell 2025). Narrow the contribution: the paper proposes *which axis* tiering should be organised along, not that tiering should replace binarism. Draft text in defence_assessment.md §Attack 4.

**K. Venue-fit footnote in §1 — NEW.**
A single footnote or sentence acknowledging that the replication package accompanying this paper consists of workflow artefacts, not analytical code and data, and that the paper is offered to *Sociological Science* as a methodological contribution whose audience the journal's quantitative-transparency commitment attracts. Draft text in defence_assessment.md §Attack 5.

**L. §6.3 consistency-argument repair — NEW, supersedes the "consistency challenge" phrasing.**
Replace the "consistency challenge" claim with an infrastructural-compatibility claim: journals that already require replication packages have the infrastructure (deposition, review, editorial workflow) that documentation-based AI policy would use. Concede that reproducibility-of-estimates and auditability-of-process are distinct purposes. Draft text in defence_assessment.md §Attack 5.

**M. Literature engagement with tacit-knowledge and content-analysis traditions — NEW, structural.**
Cite Polanyi on tacit knowledge (at minimum once, at the point where externalisation of tacit commitments is introduced); cite Krippendorff on content analysis (tied to H above); consider Collins on tacit knowledge for the §4.2–§4.4 discussion of configuration. Without this, the paper is exposed to the generational re-description in ways textual pre-emption of individual attacks cannot fix.

**N. Introduction-level provenance acknowledgement — NEW, one sentence.**
State explicitly that the workflow described generalises from a particular practice (the author's) and that the defence of the generalisation is the workflow's correspondence to methodological commitments that predate AI use. This removes the element of concealment that the sociology-of-knowledge re-description relies on.

### What not to pre-empt

Per the defence assessment memo: do not pre-empt the motivational version of any attack ("query authorship is marketing"; "this is a hobbyhorse"); do not expand the venue-fit defence beyond the single footnote; do not over-concede on ICMJE once the category distinction is acknowledged. The analogical ICMJE version is sufficient to carry §5.5 and §6.3.

### Overall assessment

The six-persona synthesis produced six revision actions (A–F) that were about tightening caveats and acknowledging limits. The asshole-reviewer material adds eight more (G–N) that are about *narrowing the novelty claims and engaging a neighbouring literature the paper has not read*. Taken together, the paper after these revisions claims less than the v3 draft and defends what it claims more securely. None of the asshole-reviewer attacks require reconceiving the argument. The paper that survives them is the paper the v3 outline was already trying to write, with the over-claiming removed.

The single highest-priority additions are: G (ICMJE demotion), H (query-authorship genealogy), K (venue-fit footnote), and M (literature engagement). G and K are the public-attack equivalents; H and M together neutralise the generational re-description and strengthen the contribution at the same time.
