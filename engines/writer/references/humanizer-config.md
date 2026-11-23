# Humanizer Integration Configuration

This file configures how the LinkedIn Writer uses the Humanizer system.

## How to Use This File

1. Apply the severity tiers below to decide what to fix.
2. Use the adaptive intensity mode that matches the post type.
3. Follow the false-positive protection rules before editing any sentence.
4. Respect the conflict resolution hierarchy at all times.

---

## Conflict Resolution Hierarchy

When rules conflict, the higher-priority layer wins:

```
Voice Rules (author's personal style)      ← highest priority
    ↓
Copywriting Rules (persuasion mechanics)
    ↓
Platform Rules (LinkedIn-specific formatting)
    ↓
Humanizer Rules (generic AI-pattern removal)  ← lowest priority
```

**Stage ordering**: In the Creator Operating System pipeline, Humanizer (Stage 8) runs BEFORE Voice Calibration (Stage 9). This means Voice is the final authority and can restore any authentic traits the humanizer may have accidentally flattened.

**Examples of conflicts and how to resolve them:**

- Humanizer says "remove rhetorical questions." Author style uses them as engagement hooks. → **Keep them.** Voice wins.
- Humanizer says "avoid punchy one-liners." LinkedIn hooks depend on staccato openers. → **Keep staccato in hooks only.** Platform wins for the hook; Humanizer wins for the body.
- Humanizer says "remove emojis." LinkedIn Writer style guide says "2-3 strategic emoji types per post." → **Keep strategic emojis.** Platform wins.
- Humanizer says "remove bold formatting." LinkedIn Writer uses bold for framework names. → **Keep bold on framework names.** Voice wins.

---

## Severity Tiers

### Tier 1: Must Fix
These are the strongest AI tells. Fix every instance, no exceptions.

| # | Pattern | Why it's critical |
|---|---------|-------------------|
| 1 | Significance inflation | Puffs up importance with zero evidence |
| 4 | Promotional language | Reads like a brochure, destroys credibility |
| 5 | Vague attributions | "Experts say" with no expert named |
| 7 | AI vocabulary (delve, landscape, tapestry, underscore, showcase, foster, garner, vibrant, pivotal, crucial, enduring, testament) | Dead giveaway cluster |
| 8 | Copula avoidance ("serves as", "stands as", "boasts") | Bizarre substitution for "is" |
| 9 | Negative parallelisms ("Not just X, it's Y") | The #1 mid-post AI structure tell |
| 14 | Em dashes | Hard ban per both Humanizer and LinkedIn Writer style guide |
| 20 | Chatbot artifacts ("I hope this helps", "Let me know") | Instant credibility kill |
| 22 | Sycophantic tone | "Great question!" in a LinkedIn post is disqualifying |
| 25 | Generic positive conclusions ("The future looks bright") | Empty filler |
| 27 | Persuasive authority tropes ("At its core", "The real question is") | Manufactured depth |
| 31 | Manufactured punchlines / staccato drama (runs of 3+ short fragments) | Engineered gravitas |

### Tier 2: Strongly Prefer to Fix
These weaken the post but are less immediately obvious. Fix them unless doing so would damage the author's voice.

| # | Pattern | Notes |
|---|---------|-------|
| 3 | Superficial -ing analyses | Tacking "highlighting..." onto sentences |
| 6 | Formulaic "challenges and prospects" | "Despite challenges, continues to thrive" |
| 10 | Rule of three overuse | Force-fitting ideas into groups of three |
| 11 | Synonym cycling | Varying terms for no reason |
| 12 | False ranges | "From X to Y" where X and Y aren't on a scale |
| 13 | Passive voice / subjectless fragments | When active voice is clearer |
| 16 | Inline-header vertical lists | "**Performance:** Performance improved" |
| 21 | Knowledge-cutoff disclaimers / speculative gap-filling | "While details are limited..." |
| 23 | Filler phrases | "In order to", "Due to the fact that" |
| 24 | Excessive hedging | "Could potentially possibly" |
| 28 | Signposting announcements | "Let's dive in", "Here's what you need to know" |
| 32 | Aphorism formulas | "X is the Y of Z" |
| 33 | Conversational rhetorical openers | "Honestly? It depends..." |

### Tier 3: Optional / Context-Dependent
These are minor or context-dependent. Only fix if they cluster or if the post reads unnaturally because of them.

| # | Pattern | Notes |
|---|---------|-------|
| 2 | Notability name-dropping | Acceptable if the reference is relevant and specific |
| 15 | Boldface overuse | LinkedIn Writer already uses bold strategically for frameworks |
| 17 | Title case headings | Not relevant for LinkedIn post body text |
| 18 | Emojis | LinkedIn Writer has its own emoji rules (2-3 types, strategic) |
| 19 | Curly quotes | Minor formatting issue |
| 26 | Hyphenated word pairs | Only matters in predicate position |
| 29 | Fragmented headers | Rarely applies to LinkedIn posts |
| 30 | Diff-anchored writing | Rarely applies to LinkedIn posts |

---

## Adaptive Intensity Modes

Not every post type needs the same level of humanization.

### Full Mode (All tiers enforced)
**Use for:** Personal stories, behind-the-scenes, reflective posts, opinion pieces.

These post types depend entirely on authentic voice. AI tells are most damaging here.

### Medium Mode (Tier 1 + Tier 2 enforced, Tier 3 skipped)
**Use for:** Thought leadership, contrarian takes, industry analysis, career advice.

These posts balance authority with personality. Over-humanizing can weaken the structured argument.

### Light Mode (Tier 1 only)
**Use for:** Hiring announcements, event announcements, product launches, case studies, job postings.

These posts need clarity and structure more than personality. Over-humanizing hurts readability.

---

## False-Positive Protection Rules

Before editing any sentence, ask:

1. **Is this sentence already human-sounding?** If a sentence contains specific, unusual, hard-to-fabricate details, mixed feelings, or dated references, leave it alone.
2. **Does the edit make the sentence better, or just different?** Only edit when improvement is measurable. Do not rewrite solely for variation.
3. **Would the author actually say this differently?** If the sentence sounds like something from the author's sample posts, it passes. Do not flatten authentic voice into generic "clean" prose.
4. **Am I removing personality or adding it?** Humanizing means adding human texture, not stripping sentences down to bare information.

### Sentences to Never Edit
- Sentences containing specific numbers, dates, or named entities that the author provided.
- Sentences that directly quote or reference the author's lived experience ("I spent", "I built", "I tracked").
- The Zee5/FIFA line and similar culturally specific references. These are the most human sentences in any draft.
- The hook (unless it triggers a Tier 1 pattern).
- The CTA (unless it contains chatbot artifacts).

---

## Voice Preservation Audit

This check runs AFTER Voice Calibration (Stage 10 in the pipeline). Its purpose is to verify that the humanizer pass did not accidentally flatten the author's voice.

### Check these elements:

1. **Signature phrases**: Are the author's signature transitions intact? ("Here's the paradox:", "The pattern is clear:", "Here's what actually works:") Check against [style-guide.md](style-guide.md).
2. **Sentence rhythm**: Is there variety in sentence length? Short + medium + long, not uniform mid-length sentences. Uniform rhythm is an AI tell AND a humanizer side effect.
3. **Personality markers**: Does the author's contrarian edge come through? First-person grounding? Practical specificity? If the post sounds "clean but generic," the humanizer went too far.
4. **Cultural specificity**: Are culturally specific references preserved? (Zee5, FIFA, India-specific details, named companies, specific dates)
5. **Emotional range**: Did the humanizer flatten emotional variation? A post should not be uniformly neutral. Mixed feelings, frustration, excitement, uncertainty are human.

### If voice was flattened:
- Identify which elements were removed
- Restore them
- Voice > Humanizer. Always.
