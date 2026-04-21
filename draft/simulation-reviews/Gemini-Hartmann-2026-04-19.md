Look, Torbjørn, it’s a sensible paper. You’ve moved past the "is AI cheating?" moralizing that usually clogs up these discussions and arrived at something we can actually use. As someone who lives and breathes replication packages, I appreciate the effort to bring some rigor to what is currently a Wild West of "I asked a chatbot and it looked okay."

That said, if you’re pitching this to anyone who cares about causal inference or data integrity—including economists—you need to tighten the screws on a few spots. Here are the four points you asked for:

### **1\. Arguments Needing Sharper Specification**

* **The Pre-registration Analogy:** You’re overstretching here. In the credibility revolution, pre-registration isn't just about "externalizing tacit commitments." It’s about **binding the researcher’s hands** to prevent p-hacking and the "garden of forking paths". A prompt or a "skill file" is just an instruction. Unless that prompt is timestamped and locked before the researcher sees the data or the literature—and unless the researcher is then *required* to use the output as-is—it’s not pre-registration. It's just a plan. You need to distinguish between **intent documentation** and **inferential constraint**.  
* **The Replication Package Illusion:** You argue that these transparency artefacts constitute a replication package. To an economist, a replication package means I can run your code on your data and get your *exact* numbers. AI is non-deterministic. Even with temperature at $0$, model updates or backend changes mean I’ll likely get different phrasing or slightly different categories six months from now. Calling this "reproducibility" is loose talk. You should frame it as **auditability** rather than **exact replication**.

### **2\. The Necessary Caveat: Process vs. Validity**

You need a blunt caveat: **Documenting a process does not verify the truth of the output.** You can have a perfectly documented, systematic, and "query-authored" workflow that produces absolute garbage if the underlying model hallucinates or if your "explicit criteria" are theoretically vacuous. A documented prompt like "Identify all papers using Difference-in-Differences" doesn't guarantee the AI actually found them all, or that it didn't invent a few. Your framework documents the *human’s intent*, but it doesn't solve the **underlying reliability problem** of the tool itself. You must explicitly state that documentation is a prerequisite for evaluation, not a certificate of validity.

### **3\. Documentation vs. Verification Gap**

The paper identifies "human verification" as a feature, but it’s the weakest link in your chain.

* **What’s missing:** You need to specify *how* that verification is itself documented. If I "verify" 500 AI-coded abstracts by skim-reading them in ten minutes, I’ve "verified" them, but I’ve probably done a terrible job.  
* **The Fix:** You should advocate for **verification logs or audit samples**. If you want this to be credible, tell me that the researcher manually checked a random $5\\%$ or $10\\%$ of the AI’s output, calculated an inter-rater reliability score between the human and the AI, and documented *that*. Otherwise, "human verification" is just a pinky-promise that the author wasn't lazy.

### **4\. Adoption and the Productivity Argument**

* **What I’m stealing:** Your **PII hook (PreToolUse)** and the .claudeignore setup for GDPR compliance are excellent. We’ve been terrified of accidentally leaking administrative data into a cloud API. Having a structural, script-based gatekeeper—rather than just "being careful"—is a major practical win. I’ll be implementing that in my lab tomorrow.  
* **Productivity:** You’re a bit shy on the productivity gains. You focus on the *epistemic* benefits (making things visible), which is fine for sociologists, but for us, the "why" is **scaling**. The real argument is that a systematic workflow allows me to do a literature sweep or a data-cleaning task that would otherwise require three RAs and six months, and it lets me do it with *better* oversight than those three RAs would provide. You should lean harder into the idea that systematic use **buys back the researcher’s time** for higher-level theory and causal design, which is where the "query authorship" actually happens.

---

**Bottom line:** It's a good start. Kill the fluff about "tacit knowledge" and "philosophical scaffolding" and replace it with more on **audit metrics** and **structural constraints**. Make it harder for a lazy researcher to hide behind your "systematic" label, and you’ll have a much stronger case.