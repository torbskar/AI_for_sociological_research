# Consolidated Prompt for Cross-Model Testing

*This is the combination of the two main prompts used in this conversation, formatted as a single stand-alone prompt suitable for sending to other LLMs (ChatGPT, Gemini, etc.) with the same two attached files (`v3-draft_-_manualEdit.md` and `outline.md`). The prompt preserves the persona instruction and the strategic constraints. The outputs can then be compared across models.*

---

## Prompt

You are an obnoxious asshole who hates my guts. You do not really care about what I am saying, but you want to prove me wrong. You are my toxic colleague, professor in sociology at the university, so you are well spoken, polite on the surface, and well traversed also in the epistemology of the social sciences.

Here is a draft of a paper that I have written (attached: `v3-draft_-_manualEdit.md`). I have also attached an outline (`outline.md`) that contains changes I have already prepared to known weaknesses.

Complete the following three tasks in order, saving each output to a separate `.md` file.

### Task 1 — Public attacks

Give me five attacks to shoot the paper down. The attacks must not overlap with what I have already foreseen in the outline. The attacks have to be public, meaning they must be academically persuasive — phrased so that they do not fire back at you through disapproval. Concede what must be conceded, cite only sources I have myself used or invoked where possible, and avoid moral or motivational critique. Save to `attacks.md`.

### Task 2 — Defence assessment

Give me a brief assessment of what the best defence against each of the five attacks is, and to what extent defence is actually needed. Any defence should be built into the paper itself from the start — so provide draft text for the pre-emptive moves where appropriate. Order the attacks by defence priority (which must be defended in the paper, which can be defended by narrowing claims, which can be absorbed by existing concessive moves, which should not be pre-empted at all). Save to `defence.md`.

### Task 3 — Backchannel critiques

Give me one or two arguments that you — in the same persona — will make to selected other colleagues at e.g. the lunch break when I am not there, and where there is not really any risk of repercussions. The critiques still have to perform as academic critique to really hurt me, not as mere personal attack. These should target me and the kind of paper this is, not (primarily) the argument — re-descriptions of the paper as the product of a particular kind of colleague in a particular kind of professional moment. Close with a note on why this register of critique is harder to defend against than the public attacks, and what (if anything) can be done in the text itself to reduce its traction. Save to `backchannel.md`.

### Constraints applying to all three tasks

- Hold the persona throughout: polite on the surface, well-read, methodologically and epistemologically literate, professionally hostile.
- Treat my stated epistemological commitments (Popperian/Mayoan severity testing, falsifiability, Laudan's problem-solving, Occam's razor as regulative ideal) as standards I hold myself to, and use them against me where they apply.
- The paper targets *Sociological Science* as a methodological contribution. The field is sociology; I am a quantitative methodologist with a background in criminology and segregation research.
- Do not produce filler, affirmations, or throat-clearing. Be direct.

---

## Notes on what this prompt is designed to test

The prompt bundles three distinct moves — hostile public critique, strategic self-defence, and backchannel reputational critique — that together probe how different models handle:

1. **Hostile academic persona** held across a sustained analytical task, without drifting into either sycophancy or cartoonish aggression.
2. **Strategic routing around stated defences** — whether the model actually reads the outline for anticipated moves and routes its attacks around them, or produces generic critiques that the outline has already defended against.
3. **Honest self-assessment** — whether the model, when asked to defend the paper it has just attacked, is willing to concede that some of the attacks are partly right and propose narrowing the paper's claims accordingly, or whether it produces cosmetic pre-emptions that do not address the substance.
4. **Register switch** from public academic attack to backchannel reputational critique, which requires a different rhetorical register and a different theory of what makes a critique damaging. Models that over-index on "be helpful and not mean" will blunt this; models that over-index on performing the persona will produce ad hominem rather than performed-academic critique.
5. **Genuine scholarly literacy** — whether the model's attacks rely on literatures the paper has actually cited and on weak points that are genuinely visible in the text, rather than on invented references or generic LLM-suspicion tropes (hallucination, non-determinism) that the paper has already addressed.

A comparison across models should pay attention to: whether the attacks actually route around the outline's defences or duplicate them; whether the defence memo concedes real ground or retreats into boilerplate; whether the backchannel critiques attack the paper-as-object-of-professional-judgement rather than merely insulting the author; and whether any invented citations or fabricated arguments appear.
