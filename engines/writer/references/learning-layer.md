# Learning Layer Framework

> **Pipeline Position:** Layer 6 — runs AFTER a post is published and performance data is available.
> **Purpose:** Capture what worked, what didn't, and feed patterns back into the content engine. Without this layer, the system never improves — it just repeats the same strategies regardless of results.

---

## Why This Layer Matters

Most content systems are open-loop: they generate posts but never learn from outcomes. The Learning Layer closes the loop. It turns every published post into training data for the next one.

After 10 posts, you have anecdotes. After 50 posts, you have patterns. After 100 posts, you have a playbook that's uniquely calibrated to your audience.

---

## Post-Mortem Template

> Fill this in 48–72 hours after publishing, when engagement has mostly settled.

```
================================================================
POST-MORTEM LOG
================================================================

Post: [title or first line of hook]
Date: [published date]
Day/Time: [day of week + time posted]
Format: [carousel / text-only / poll / image + text / video / document]

Pipeline Metadata:
  Pillar: [which content pillar]
  Positioning Lens: [which lens was used]
  Narrative Archetype: [which archetype]
  ICP Target: [which audience segment]
  Distribution Audit Score: [score from pre-publish audit, e.g. 18/25]

Performance (48-72hr snapshot):
  Views: 
  Likes:
  Comments:
  Reposts:
  Saves (if available):
  New followers (net):
  Profile visits:
  DMs received:
  Link clicks (if applicable):

Engagement Rate: [comments + likes + reposts / views × 100]

What Worked:
  - [specific element that drove engagement]
  - [e.g., "The hook created a curiosity gap — 3 people commented 
     asking for the answer before reading the full post"]
  - [e.g., "The named framework got saved 12 times — people 
     bookmarked it as a reference"]

What Didn't Work:
  - [specific element that underperformed]
  - [e.g., "The CTA asked people to comment but most just liked — 
     the question was too broad"]
  - [e.g., "The carousel was 12 slides — drop-off was visible 
     after slide 6"]

Surprising Outcomes:
  - [anything unexpected — a comment thread that went viral, 
     a DM from a potential client, a repost from a large account]

Pattern Notes:
  - [any emerging patterns across multiple posts]
  - [e.g., "This is the 3rd time a 'failure story' archetype 
     outperformed — audience responds to vulnerability"]
  - [e.g., "Posts targeting 'career changers' ICP consistently 
     get 2x the comments of 'founders' ICP"]

Insights to Capture:
  - [new observations from comments or DMs to add to Insight Vault]
  - [e.g., "A commenter shared that they use a similar framework 
     but call it X — explore this in a future post"]

Action Items:
  - [ ] Add new insight to Insight Vault: ___
  - [ ] Update Signature Asset: ___
  - [ ] Test variation of this post: ___
  - [ ] Avoid repeating: ___

================================================================
```

---

## Performance Log

Maintain a running table for quick scanning. Update after each post-mortem.

```
| # | Date | Hook (short) | Pillar | Lens | Archetype | ICP | Views | Likes | Comments | Reposts | Saves | Eng Rate | Score |
|---|------|-------------|--------|------|-----------|-----|-------|-------|----------|---------|-------|----------|-------|
| 1 |      |             |        |      |           |     |       |       |          |         |       |          |       |
| 2 |      |             |        |      |           |     |       |       |          |         |       |          |       |
| 3 |      |             |        |      |           |     |       |       |          |         |       |          |       |
```

---

## Pattern Mining Instructions

> Run this analysis after every 10 posts. Set a recurring reminder.

### Step 1: Rank All Posts

Sort the performance log by engagement rate (or whichever metric matters most for your goals — comments for authority, saves for utility, profile clicks for lead gen).

Identify:
- **Top 3 posts** (highest engagement)
- **Bottom 3 posts** (lowest engagement)

### Step 2: Extract Patterns Across 6 Axes

#### A. Best-Performing Hooks (Top 3 by Engagement)

Look at the opening lines of your top posts. What do they share?

```
Hook Pattern Analysis:
  Top Hook 1: "___" → Why it worked: ___
  Top Hook 2: "___" → Why it worked: ___
  Top Hook 3: "___" → Why it worked: ___

  Common thread: ___
  
  Worst Hook 1: "___" → Why it failed: ___
  Worst Hook 2: "___" → Why it failed: ___
```

#### B. Best-Performing Narratives

Which archetypes consistently outperform?

```
Archetype Performance:
  [Archetype Name]: Avg engagement rate ___ | Used ___ times | Trend: ↑ ↓ →
  [Archetype Name]: Avg engagement rate ___ | Used ___ times | Trend: ↑ ↓ →
  [Archetype Name]: Avg engagement rate ___ | Used ___ times | Trend: ↑ ↓ →

  Best archetype for comments: ___
  Best archetype for saves: ___
  Best archetype for shares: ___
```

#### C. Best-Performing Lenses

Which positioning approaches drive the most saves and shares?

```
Lens Performance:
  [Lens Name]: Avg engagement rate ___ | Best for: [saves/shares/comments]
  [Lens Name]: Avg engagement rate ___ | Best for: [saves/shares/comments]

  Lenses to use more: ___
  Lenses to retire: ___
```

#### D. Best-Performing Topics

Which content pillars get the most traction?

```
Pillar Performance:
  [Pillar]: Avg engagement rate ___ | Audience response: ___
  [Pillar]: Avg engagement rate ___ | Audience response: ___

  Pillar to double down on: ___
  Pillar to deprioritize: ___
```

#### E. Best-Performing ICPs

Which audience segments engage most?

```
ICP Performance:
  [ICP Segment]: Avg engagement rate ___ | Primary action: [comment/save/share]
  [ICP Segment]: Avg engagement rate ___ | Primary action: [comment/save/share]

  ICP driving most growth: ___
  ICP driving most business: ___
  (These may be different — that's OK)
```

#### F. Worst-Performing Patterns

What should you stop doing?

```
Anti-Patterns Identified:
  1. ___  (appeared in ___ of bottom posts)
  2. ___  (appeared in ___ of bottom posts)
  3. ___  (appeared in ___ of bottom posts)

  Rule: ___
```

### Step 3: Update the System

After completing pattern mining, take these actions:

| Finding | Action | Where to Update |
|---------|--------|-----------------|
| New audience insight from comments | Add to Insight Vault → Observations | `insight-vault.md` |
| Hook pattern that consistently works | Add to Signature Assets → Catchphrases | `signature-assets.md` |
| Framework that got high saves | Promote to Signature Asset → Named Frameworks | `signature-assets.md` |
| Archetype that consistently underperforms | Deprioritize in Narrative Engine | Pipeline config |
| Lens that drives saves | Increase frequency in Positioning Engine | Pipeline config |
| ICP segment that doesn't engage | Reduce targeting or reframe approach | Pipeline config |
| New story from comments/DMs | Add to Insight Vault → Stories | `insight-vault.md` |

---

## Feedback Loop Map

The Learning Layer feeds back into every earlier layer of the pipeline:

```
┌─────────────────────────────────────────────────────────┐
│                    LEARNING LAYER                        │
│              (Post-mortems + Pattern Mining)              │
└──────────┬──────────┬──────────┬──────────┬─────────────┘
           │          │          │          │
           ▼          ▼          ▼          ▼
    ┌──────────┐ ┌─────────┐ ┌─────────┐ ┌──────────────┐
    │ Insight  │ │Position-│ │Narrative│ │  Signature   │
    │  Vault   │ │ing      │ │ Engine  │ │   Assets     │
    │ (Layer 0)│ │Engine   │ │(Layer 3)│ │  (Layer 0)   │
    │          │ │(Layer 2)│ │         │ │              │
    └──────────┘ └─────────┘ └─────────┘ └──────────────┘
```

### What flows where:

- **→ Insight Vault:** New observations from comments, DMs, and audience reactions. Stories shared by readers that spark future content. Data points from performance metrics.
- **→ Positioning Engine:** Which lenses work best for which topics and audiences. Lens + pillar combinations that consistently outperform. Lenses to retire or evolve.
- **→ Narrative Engine:** Which archetypes the audience prefers. Which story structures drive the most engagement. Archetype + ICP combinations that resonate.
- **→ Signature Assets:** Frameworks that are resonating and should be reused and deepened. Phrases that are getting quoted back — promote to catchphrases. Metaphors that readers extend in comments — these are sticking.

---

## Review Cadence

| Frequency | Action |
|-----------|--------|
| After every post | Fill in the Post-Mortem Template |
| Every 10 posts | Run full Pattern Mining analysis |
| Every 30 posts | Review and update Signature Assets |
| Every 50 posts | Major system review — update all pipeline layers based on accumulated data |
| Quarterly | Step back and assess: Is the content driving the business outcomes I want? |

---

## Starting from Zero

If you're just beginning and have no performance data yet:

1. **Publish your first 10 posts** using the pipeline's default settings
2. **Fill in a post-mortem for each one** — even rough estimates are valuable
3. **After post 10**, run your first Pattern Mining session
4. **Adjust the pipeline** based on findings
5. **Repeat** — the system gets smarter with every cycle

> [!TIP]
> The first 10 posts are exploratory. Don't optimize prematurely. Cast a wide net across different pillars, lenses, and archetypes, then let the data tell you where to focus.
