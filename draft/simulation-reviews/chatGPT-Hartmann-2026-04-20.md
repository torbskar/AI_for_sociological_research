Alright — this is a useful paper, and most of the instincts are right. The issues are about over-claiming and about sliding between \*documentation\*, \*commitment\*, and \*verification\* as if they were the same thing. They’re not. That’s where you’ll get pushback from economists.



I’ll go point by point, keeping it tight.



\---



\## 1. Two arguments that need sharpening



\### (A) The pre-registration analogy is doing too much work



You repeatedly claim that systematic AI use “functions like pre-registration” because it forces ex ante specification of criteria.



That’s directionally right, but as stated it won’t survive contact with anyone who actually works with pre-analysis plans.



\*\*Problem:\*\*

Pre-registration buys you \*commitment under observability\*. Your workflow buys you \*articulation under potential observability\*. Those are not equivalent.



\* Pre-registration constrains researcher degrees of freedom because:



&#x20; \* it is \*\*timestamped\*\*

&#x20; \* it is \*\*public or at least escrowed\*\*

&#x20; \* deviations are \*\*detectable ex post\*\*

\* Your workflow:



&#x20; \* can be written \*after seeing outputs\*

&#x20; \* can be iteratively revised without binding record (unless you lean heavily on version control, which you don’t fully formalize)

&#x20; \* does not prevent \*selective retention of runs\*



You acknowledge the disanalogy, but then walk it back too quickly (“not fatal”). That’s exactly where an economist will stop you.



\*\*What needs sharpening:\*\*



\* Be explicit: this is \*\*not a commitment device\*\* in the pre-registration sense.

\* At best, it is:



&#x20; \* a \*structured lab notebook\*

&#x20; \* potentially a \*weak commitment device\* \*\*if\*\* versioning + timestamps are enforced and disclosed



If you want the analogy to hold, you need a condition like:



> “The analogy to pre-registration holds only when configuration files and logs are version-controlled, time-stamped, and made available in full.”



Otherwise, you’re overstating.



\---



\### (B) “Systematic use produces verifiable artefacts” — imprecise



You repeatedly claim that systematic AI use produces \*verifiable\* artefacts and \*replication packages analogous to code and data\*.



That’s too strong.



\*\*Problem:\*\*

In empirical work, replication packages allow a third party to:



\* re-run the code

\* recover the same estimand (modulo randomness)



Your artefacts allow a third party to:



\* inspect what was \*intended\*

\* sometimes re-run prompts

\* but \*\*not recover the same output\*\*, nor guarantee the same selection path



So the analogy to replication packages is only partial.



More importantly:



\* A screening rubric being explicit does \*\*not\*\* mean the resulting literature set is reproducible

\* A prompt log does \*\*not\*\* mean the same text would be generated

\* A workflow does \*\*not\*\* mean the same decisions would be made at verification checkpoints



\*\*What needs sharpening:\*\*

You need to separate:



\* \*\*process transparency\*\*

\* \*\*computational reproducibility\*\*

\* \*\*decision reproducibility\*\*



Right now they’re blurred.



A cleaner claim would be:



> “These artefacts make the process \*auditable\*, not \*reproducible\* in the strict computational sense.”



Without that, economists will read this as casually equating logs with identification.



\---



\## 2. The missing caveat: documenting process ≠ verifying output



This is the single most important thing you need to add, and it’s currently underdeveloped.



You come close in §5.4, but you don’t state the implication clearly enough.



\*\*Core issue:\*\*

Documenting the process does \*\*not\*\* verify the output.



\* A fully documented workflow can still:



&#x20; \* encode biased inclusion criteria

&#x20; \* systematically misclassify

&#x20; \* produce incorrect summaries

&#x20; \* converge on the wrong conclusion



What documentation guarantees:



\* You can \*\*see how the result was produced\*\*



What it does \*not\* guarantee:



\* That the result is \*\*correct\*\*

\* That the process is \*\*valid\*\*

\* That conclusions are \*\*robust\*\*



\*\*What follows (and needs to be said explicitly):\*\*



\* Evaluation must shift from:



&#x20; \* “Can I reproduce this?”

&#x20;   to

&#x20; \* “Do I agree with the decision rules and how they were applied?”



That is a \*much harder\* burden on reviewers.



A clean caveat would look like:



> “Systematic documentation verifies the \*traceability\* of outputs, not their \*validity\*. The epistemic burden shifts from reproducing results to evaluating the adequacy of the decision rules that generated them.”



Right now, you imply this. You don’t state it.



\---



\## 3. Does the paper adequately distinguish process vs output?



\*\*Short answer: not quite.\*\*



You gesture at the distinction, but you repeatedly slide between:



\* “makes errors visible”

\* “makes work verifiable”

\* “supports replication”



Those are different claims.



What’s missing is a clean separation of three layers:



1\. \*\*Process documentation\*\*



&#x20;  \* prompts, criteria, logs

2\. \*\*Process auditability\*\*



&#x20;  \* can a third party evaluate those choices?

3\. \*\*Output validation\*\*



&#x20;  \* are the results actually correct?



Your paper is strong on (1), decent on (2), and too optimistic on (3).



\*\*What needs to be added:\*\*



You need a paragraph that explicitly says:



\* Auditability ≠ correctness

\* Transparency ≠ identification

\* Logged decisions ≠ unbiased decisions



And then say what would be required to get closer to output validation:



\* re-running workflows with perturbations (robustness)

\* alternative prompt specifications

\* human re-coding subsamples

\* sensitivity to model choice



In other words: bring in the equivalent of \*\*robustness checks\*\*. Right now, that layer is missing.



\---



\## 4. What the paper gets right (and I would adopt)



There’s a lot here I’d actually use.



\### (A) Treating prompts/configuration as first-class research objects



This is the strongest idea in the paper.



The move from:



\* “AI generated text”

&#x20; to

\* “the researcher authored the decision rules”



is exactly right, and it maps cleanly to how we think about:



\* code as the object of scrutiny

\* not just tables



I’d absolutely adopt:



\* storing prompts/configs alongside code

\* treating them as part of the replication package (with the caveats above)



\---



\### (B) Separation of AI from raw data via scripts



This is just good practice.



Your “AI touches code, not data” rule is:



\* legally sensible

\* methodologically clean

\* very easy to integrate into existing workflows



No objections there.



\---



\### (C) Adversarial reviewer configuration



This is underrated and actually useful.



Economists already try to:



\* stress-test specifications

\* look for failure modes



Encoding that into AI workflows is a natural extension.



I’d use that — especially for:



\* robustness brainstorming

\* spec variation

\* falsification ideas



\---



\### (D) The core policy critique (binary disclosure is useless)



This is correct.



“AI was used” is about as informative as:



\* “Stata was used”



Your push toward:



\* “show me the workflow”

&#x20; is aligned with how empirical work is already evaluated.



No issue there.



\---



\## 5. Is the productivity argument adequately developed?



Not really — it’s the weakest part.



You rely heavily on the idea (via Zeng et al.) that:



\* systematic prompting → better outcomes



But:



\* that evidence is from data science tasks

\* not from messy social science workflows

\* and definitely not from literature synthesis or argument construction



Right now, the productivity claim is:



\* plausible

\* but speculative



\*\*What’s missing:\*\*



You need at least one of:



\* a concrete example (time saved, coverage increased, error detected)

\* or a clearer decomposition of where gains come from:



&#x20; \* search breadth

&#x20; \* consistency of criteria

&#x20; \* reduced cognitive load



Otherwise, an economist reads this as:



> “This sounds efficient, but where’s the evidence?”



\---



\## Bottom line



\* The workflow is sensible and in many places better than current practice.

\* The paper’s problem is not direction — it’s \*\*over-claiming equivalence\*\*.



Tighten three things and it becomes much more credible:



1\. \*\*Downgrade the pre-registration analogy\*\* (or condition it on timestamped disclosure)

2\. \*\*Replace “verifiable” with “auditable” throughout\*\*

3\. \*\*Explicitly state that process transparency does not validate outputs\*\*



Do that, and the paper reads less like a manifesto and more like something economists will actually take seriously — and use.



