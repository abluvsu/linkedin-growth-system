# Content Scoring System

Every post receives a weighted score across 6 dimensions before publishing. No pass/fail — the score identifies exactly where a post is strong and where it needs work.

---

## Scoring Dimensions

| Dimension | Weight | What It Measures |
|---|---|---|
| Insight Strength | /25 | Could a smart, experienced person disagree with this? Is the core idea non-obvious? Does it go beyond restating common knowledge? |
| Novelty | /20 | Has the reader seen this idea, framing, or argument before? Would this feel fresh in a feed full of similar content? |
| Credibility | /20 | Is the claim supported by a specific story, number, observation, or pattern? Could the author prove this in a conversation? |
| Emotional Resonance | /15 | Does the post make the reader feel something — recognition, discomfort, relief, urgency, curiosity? Is the emotion earned or manufactured? |
| Clarity | /10 | Could a smart 15-year-old understand the core message on first read? Is the structure clean? Are there unnecessary detours? |
| Shareability | /10 | Would someone screenshot this, send it to a colleague, or tag someone in the comments? Does it contain a portable insight? |

**Total: /100**

---

## Thresholds

| Score Range | Action |
|---|---|
| **85–100** | **Publish.** The post is strong across dimensions. Minor polish only. |
| **70–84** | **Improve.** Identify the weakest dimension. Revise specifically to raise that dimension's score. Re-score after revision. |
| **Below 70** | **Rewrite.** The post has a structural problem. Return to the Positioning Engine and select a stronger angle before redrafting. |

### Threshold Rules

1. No post publishes below 85 without an explicit override and documented reason.
2. A post scoring below 70 does not get "improved" — it gets restarted. Polishing a weak angle is wasted effort.
3. If a post scores 85+ overall but has any single dimension below 50% of its weight (e.g., Novelty below 10/20), flag that dimension for review. A high total with a critical weakness can still underperform.

---

## Forced Justification Protocol

**Every score MUST include a written rationale.** A number without evidence is not a score — it is a guess.

### Format

```
[Dimension]: [Score]/[Weight]
Rationale: [2-3 sentences explaining the score with specific reference to the post content.]
```

### Rules

1. The rationale must reference specific words, phrases, or structural choices in the post.
2. "This is good" or "This could be better" are not rationales. State *what* is good or *what* is weak and *why*.
3. If you cannot write a rationale, you cannot assign the score. Re-read the post.

---

## Scored Example

### Sample Post

> I've reviewed 200+ resumes this year for mid-level product roles. The single biggest mistake isn't typos or bad formatting — it's leading with responsibilities instead of outcomes. "Managed a team of 5" tells me nothing. "Reduced onboarding time by 40% by redesigning the first-week workflow for a team of 5" tells me everything. The irony is that the people doing the best work are often the worst at describing it, because they're so close to the work that the outcome feels obvious to them. It's not obvious to me. I'm reading 30 resumes in a sitting. You have 6 seconds to make me care. Lead with the number. Lead with the change. Lead with what's different because you were there.

---

### Scorecard

```
Insight Strength: 18/25
Rationale: The distinction between responsibilities and outcomes is known
among career coaches but genuinely under-practiced by candidates. The
secondary insight — that high performers under-describe their impact
because the outcome feels obvious to them — adds a layer most resume
advice skips. A smart recruiter might agree rather than disagree, which
limits the score slightly. The idea is non-obvious to the target reader
(job seekers) even if familiar to hiring professionals.

Novelty: 13/20
Rationale: "Lead with outcomes, not responsibilities" has appeared in
resume advice for years. The framing around "the people doing the best
work are the worst at describing it" adds freshness, and the specific
stat (200+ resumes, 6-second read time) gives it texture. However, the
core advice is not new. The execution elevates familiar material but
does not introduce a genuinely new concept.

Credibility: 19/20
Rationale: The post opens with a specific, verifiable claim (200+
resumes reviewed this year for mid-level product roles). The bad
example ("Managed a team of 5") and good example ("Reduced onboarding
time by 40%...") are concrete and realistic. The detail about reading
30 resumes in a sitting and the 6-second attention window adds
operational credibility. The only reason this isn't 20/20 is the
absence of a named outcome — what happened when a candidate did lead
with outcomes? A result would close the loop.

Emotional Resonance: 13/15
Rationale: Job seekers reading this will feel immediate recognition
("I do that") followed by urgency ("I need to fix my resume"). The
line about high performers being bad at self-description provides
relief — it reframes a weakness as a natural consequence of being
close to the work, not a personal failing. The emotion is earned
through specificity, not hype.

Clarity: 9/10
Rationale: The core message is immediately clear: lead with outcomes.
The structure moves from observation (200 resumes) to problem
(responsibilities vs outcomes) to insight (why good people do this)
to action (lead with the number). A 15-year-old could follow the
argument. Minor deduction: the final three imperative sentences
("Lead with the number. Lead with the change. Lead with what's
different because you were there.") are stylistically strong but the
third one is slightly less concrete than the first two.

Shareability: 8/10
Rationale: The resume before/after comparison is highly screenshot-
able. Job seekers will tag friends or send this in group chats. The
"6 seconds" stat is portable — easy to remember and repeat. Slight
limitation: the post is most shareable within job-seeking circles;
it's less likely to cross over to founders or operators who don't
review resumes regularly.
```

### Total: 80/100

### Verdict: **Improve**

**Weakest Dimension:** Novelty (13/20)

**Recommended Fix:** Replace the familiar "outcomes over responsibilities" frame with a more specific, less-seen angle. For example, focus the post entirely on the secondary insight — why high performers under-describe their impact — and build the resume advice as the application, not the headline. This inverts the structure and makes the novelty the lead instead of the support.

**Re-score after revision.** If Novelty rises to 16+ and other dimensions hold, the post crosses the 85 threshold.
