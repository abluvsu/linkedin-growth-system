# Authority Audit v2

This audit runs in Phase 4 (Quality), BEFORE any line-editing (humanizer pass, voice calibration, or formatting). A post that fails the Authority Audit should be restructured, not polished.

## Purpose

A LinkedIn post can be 100% human-sounding and still get zero engagement. Humanization removes AI signals. The Authority Audit ensures the post contains something worth reading.

The key shift from v1: harder rejection criteria and weighted scoring with forced justification. Pass/fail is replaced by a scoring system that prevents mediocre content from sneaking through.

---

## The 6 Authority Checks

Run these checks in order. Each check is binary: pass or reject.

---

### Check 1: Insight Test

**Question:** Could a smart person disagree with this?

**Pass:** The post takes a position that a reasonable, informed person might push back on. It has a genuine point of view.

**Reject:** The post states something everyone already agrees with.

Reject examples:
- "Networking matters"
- "AI is changing everything"
- "You should invest in yourself"
- "Communication skills are important"

These are true but they are not insights. An insight requires tension.

---

### Check 2: Originality Test

**Question:** Would 100 smart creators independently produce this insight?

**Pass:** The insight is specific enough to the author's experience, perspective, or analysis that it would be unlikely to emerge from a random sample of 100 creators writing about the same topic.

**Reject:** The insight is a common reframe that anyone following the topic would eventually articulate.

This is the test that separates creators from aggregators.

Reject examples:
- "Remote work isn't dead" (obvious contrarian take)
- "AI won't replace you, a person using AI will" (said by 10,000 people)
- "Stop chasing productivity, focus on outcomes" (generic wisdom)

Pass examples:
- "I ran CareerFlow against 47 resumes and the ones that got callbacks weren't the ones with the most keywords, they were the ones that named the hiring problem in the first paragraph" (specific, experience-based, hard to replicate)

---

### Check 3: Experience Test

**Question:** Could ChatGPT have written this without the author?

**Pass:** The post contains details, stories, numbers, or observations that could only come from someone who has lived this experience or done this specific work.

**Reject:** The post is composed entirely of ideas that could be assembled from publicly available information by any competent language model.

This check forces the Insight Vault to be used. Posts that fail this check are almost always missing a personal story, a specific number, or a named observation.

---

### Check 4: Evidence Test

**Question:** Is there at least one piece of supporting evidence?

**Evidence types (strongest to weakest):**
- Personal experience with specific details ("I ran this workflow on 47 resumes over 3 weeks")
- Named data points ("Feedly gained 3 million users in 14 days")
- Specific anecdotes ("A recruiter at [company] told me...")
- Observable patterns ("I have seen this happen in 4 out of 5 projects I reviewed")

**Reject:** The post uses only abstract claims, vague appeals to authority ("experts agree"), or unsupported generalizations.

**Remediation:** Add one concrete data point, one personal anecdote, or one specific example. If no evidence exists, the post is opinion. Ensure the insight is strong enough to stand without evidence, and flag it as opinion.

---

### Check 5: Memorability Test

**Question:** Can someone repeat this idea tomorrow?

**Pass:** The post has a named framework, a surprising statistic, a vivid image, or a one-line thesis that sticks. If you closed LinkedIn right now, you would remember one thing from this post in 2 hours.

**Reject:** The post has many decent points but no single anchor. It reads well but evaporates.

**Remediation:** Identify the single strongest line in the draft. Promote it. Build the post's structure so that line is impossible to miss (either the hook or the framework title). Consider creating a Signature Asset from it. See [../signature-assets.md](../signature-assets.md).

---

### Check 6: Save Test

**Question:** Would someone screenshot this?

**Pass:** The post contains a reusable framework, a checklist, a system, a contrarian reframe someone can apply to their own situation, or a story that changes how they think about a problem.

**Reject:** The post is interesting but not useful. It provokes a nod but not an action.

**Remediation:** Add a "Start here:" section or a named framework. Convert observation into system.

**Exception for Pillar 4 (Personal Stories):** The save test is relaxed. The post passes if it creates genuine emotional resonance instead of practical utility.

---

## Gate Decision

| Checks Passed | Meaning | Action |
|---------------|---------|--------|
| 6/6 | Strong post | Proceed to Content Scoring |
| 5/6 | Good post with one gap | Fix the failing check, then proceed |
| 4/6 | Mediocre post | Restructure before proceeding |
| 3/6 or fewer | Weak post | Return to Positioning Engine (Phase 1, Stage 3) |

---

## Content Scoring System

After passing the 6 checks, score the post. See [content-scoring.md](content-scoring.md) for the full scoring framework.

| Dimension | Weight | Guiding Question |
|-----------|--------|------------------|
| Insight Strength | 25 | Could a smart person disagree? Is this non-obvious? |
| Novelty | 20 | Have readers seen this 100 times? |
| Credibility | 20 | Is there a story, number, observation, or pattern? |
| Emotional Resonance | 15 | Does this make the reader feel something? |
| Clarity | 10 | Could a 15-year-old understand the core message? |
| Shareability | 10 | Would someone screenshot this or send it to a colleague? |

### Forced Justification Rule

**Every score MUST include a written rationale.** The model cannot assign a score without evidence. This prevents self-congratulatory scoring.

Example:
```
Novelty: 12/20
Rationale: Similar ideas appear in 3+ recent LinkedIn posts about AI hiring.
The framing around 'problem diagnosis vs keyword matching' adds slight
differentification but the core insight is not new.
```

### Thresholds

- **85+** = Proceed to Phase 4 (Humanizer Pass)
- **70-84** = Identify the weakest dimension, improve it, re-score, then proceed
- **<70** = Return to Phase 1, Stage 3 (Positioning Engine) and start over

---

## When to Skip the Authority Audit

- **Hiring announcements**: Informational, not persuasive. Skip.
- **Event announcements**: Same. Skip.
- **Simple reposts with commentary**: Apply a lighter version (Insight Test and Originality Test only).

## Integration with the Pipeline

The Authority Audit is Stage 7 in the pipeline (Phase 4: Quality). It runs after the draft is assembled (Phase 3) and before any voice or humanization work begins (Stages 8-10). This ordering is intentional: there is no point polishing a post that has nothing to say.
