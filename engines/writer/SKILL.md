---
name: linkedin-writer
description: Write LinkedIn posts in the author's distinctive voice and style. Use when the user wants to draft a LinkedIn post, write a LinkedIn update, compose social content for LinkedIn, or convert rough notes/ideas/articles into a LinkedIn post. Accepts any input format: bullet points, rough notes, article summaries, or just a topic/thesis. Produces posts that match the author's contrarian, framework-driven, short-paragraph style while avoiding AI-generated writing patterns.
---

# LinkedIn Post Writer — Creator Operating System

Write LinkedIn posts that sound like the author, not like AI. Generate stronger ideas, package them into memorable narratives, then optimize for distribution.

## Integrated Systems

Three external skills feed this pipeline. Read their configurations before starting:

- **Copywriting** (persuasion mechanics): configured in [references/copywriting-config.md](references/copywriting-config.md)
- **Humanizer** (AI-pattern removal): configured in [references/humanizer-config.md](references/humanizer-config.md)
- **Hook Writer** (scroll-stop optimization): [../hook-writer/SKILL.md](../hook-writer/SKILL.md) and [references/hooks-framework.md](references/hooks-framework.md)
- **Lead Magnet Mode** (value/tease architecture): [references/lead-magnet-mode.md](references/lead-magnet-mode.md)
- **Authority Audit** (content quality gate): [references/authority-audit.md](references/authority-audit.md)

## Conflict Resolution Hierarchy

When rules from different systems conflict, the higher-priority layer wins:

```
Voice Rules (author's personal style)      ← highest priority
    ↓
Copywriting Rules (persuasion mechanics)
    ↓
Platform Rules (LinkedIn formatting)
    ↓
Humanizer Rules (AI-pattern removal)       ← lowest priority
```

## Content Pillars

Every post falls under one of 5 pillars. See [references/content-pillars.md](references/content-pillars.md) for full details, tone guidance, and example topics.

| # | Pillar | Mix |
|---|--------|-----|
| 1 | **AI Playbooks & Practical How-Tos** | ~30% |
| 2 | **AI Industry Takes & Contrarian POVs** | ~25% |
| 3 | **Career & Future of Work in AI Era** | ~20% |
| 4 | **Personal Stories & Behind-the-Scenes** | ~15% |
| 5 | **Educator/Builder POV on AI Tools** | ~10% |

## Input Handling

Accept any form of rough material:
- **Bullet points / notes**: Extract the core insight, find the contrarian angle.
- **Article / link summary**: Identify the author's unique take, not a summary.
- **Topic / thesis only**: Generate the supporting argument and framework from scratch.
- **Pillar selection only (no topic)**: Switch to **Idea Generation Mode** — generate 5-7 post ideas for the selected pillar, each with a hook sketch, core insight, and framework suggestion. See [references/content-pillars.md](references/content-pillars.md).
- **Mixed**: Combine elements as needed.

---

## Pipeline (6 Layers, 5 Phases)

The pipeline has 6 functional layers. Externally, present them as 5 phases (Strategy, Idea, Creation, Quality, Distribution). Internally, execute all stages. Do not skip stages.

---

### Layer 0: Insight Vault (Always Active)

Before starting any post, check the author's personal knowledge repository:

- **Insight Vault**: [insight-vault.md](insight-vault.md) — stories, observations, failures, lessons, frameworks, contrarian beliefs, data points.
- **Signature Assets**: [signature-assets.md](signature-assets.md) — reusable IP (named frameworks, lenses, laws, recurring metaphors).

If the Insight Vault contains material relevant to the current topic, use it. Posts built from the Vault are inherently more authentic than posts generated from scratch.

If the Vault is empty or has no relevant entries, proceed with the raw input. After the post is published, prompt the author to add new observations to the Vault.

---

### Phase 1: Strategy (Layer 1)

#### Stage 1: Topic Selection
- **Ask format preference**: "Single draft or 2-3 variations?" (unless user already specified)
- **Ask content pillar**: "Which pillar does this fall under?" — present the 5 pillars as options. Skip if the pillar is obvious from the input, or if the user already specified it. If the user picks a pillar with no topic, switch to Idea Generation Mode instead of drafting.
- **Determine post type** for adaptive humanizer intensity later: Story/Personal (Full), Thought Leadership/Contrarian/Career (Medium), Announcement/Hiring/Event (Light). See [references/humanizer-config.md](references/humanizer-config.md).
- **Lead Magnet Mode Detection**: Scan the user input/topic for explicit keywords: *freebie, template, cheat sheet, ebook, guide, checklist, resource, giveaway, pdf, download*. Confirm the user is the author/provider of the resource, not just discussing someone else's tool. If true, set `Lead_Magnet_Mode = ACTIVE` and output a system log line: `[SYSTEM: Lead Magnet Mode Activated]`.

#### Stage 2: Audience Definition (ICP)
Define the target reader before writing a single word. See [references/icp-engine.md](references/icp-engine.md).

- **Identify the ICP**: Founder, PM, Operator, Job Seeker, Consultant, or Mid-career professional. Who scrolls past this post and stops?
- **Define the desired reaction** (Think / Feel / Do):
  - **Think**: What new belief should the reader form?
  - **Feel**: What emotion should they experience? (urgency, validation, curiosity, relief)
  - **Do**: What action should they take? (follow, comment, save, share, click profile, DM)

#### Stage 3: Positioning Engine
Transform the topic into a strong angle. See [references/positioning-engine.md](references/positioning-engine.md).

Apply the Lens Selection Matrix to pick the best lens for this content type, then run the topic through it:

| Lens | Core Question |
|------|---------------|
| **Contrarian** | What does everyone believe? Why is it incomplete? |
| **Pattern Break** | What trend am I seeing repeatedly? |
| **Founder Lens** | What would only someone in my position know? |
| **Second-Order Effect** | What happens next? |
| **Hidden Cost** | What is nobody measuring? |

The topic must escalate from weak to exceptional:
- **Weak**: "AI is changing careers."
- **Good**: "AI is replacing junior analysts."
- **Exceptional**: "AI isn't replacing analysts. It's replacing analysts who confuse reporting with thinking."

Every post must pass at least one lens. If the topic cannot produce a strong angle through any lens, pick a different topic.

---

### Phase 2: Idea Development (Layer 2)

#### Stage 4: Insight Extraction
- **Check the Insight Vault first**: Does [insight-vault.md](insight-vault.md) have a relevant observation, story, failure, or data point? Use it.
- **Identify the core insight**: What is the one contrarian or non-obvious point?
- **Find the angle**: How does this challenge conventional thinking? What do most people get wrong?
- **Benefit-frame the insight** (copywriting): Frame as what changes for the reader, not what the product does. See [references/copywriting-config.md](references/copywriting-config.md).
- **Name the framework** (if applicable): Distill the insight into a memorable, titled framework (3-5 items). Check [signature-assets.md](signature-assets.md) — can an existing signature asset be referenced or extended?

#### Stage 5: Narrative Selection
Choose one narrative archetype for this post. See [references/narrative-engine.md](references/narrative-engine.md).

| Archetype | Story Arc |
|-----------|-----------|
| **Transformation** | Old belief → Discovery → New belief |
| **Observation** | Saw something → Pattern emerged → Lesson |
| **Contrarian** | Popular belief → Challenge → Evidence → New framing |
| **Failure** | Mistake → Consequence → Learning |
| **Prediction** | Trend → Implication → Action |

Select the archetype that best fits the insight and the content pillar. Do not default to the same archetype every time. Check [references/learning-layer.md](references/learning-layer.md) for which archetypes have performed best.

---

### Phase 3: Creation (Layer 3)

#### Stage 6: Draft Creation
- **Draft the post body**: Start directly with the narrative. Do NOT write the hook yet. The hook will be generated in Stage 11 after the body is finalized.
- **Draft using the selected narrative archetype**: Follow the story arc beats from Stage 5, not a generic Hook → Problem → Framework → Action → CTA structure. The archetype IS the structure.
- **One idea per paragraph** (copywriting): Each paragraph advances exactly one argument. If a paragraph makes two points, split it.
- **Apply copywriting style rules during drafting**: Simple over complex. Specific over vague. Active over passive. Confident over qualified. Show over tell. Honest over sensational.
- **Pair every feature with its benefit**: "Runs a skill gap analysis" → "Runs a skill gap analysis so you know exactly what you are missing before you apply."
- **Draft the CTA**:
  - `IF Lead_Magnet_Mode == ACTIVE`:
    1. Halt standard CTA generation.
    2. Read `references/lead-magnet-mode.md` -> Section 2 & 3.
    3. Cross-reference the draft's Hook with the Landing Page Promise to ensure zero narrative disconnect.
    4. Append the structurally compliant CTA based on the asset type (Condition A, B, or C).
  - `ELSE`: Draft the CTA using the standard copywriting CTA formula: [Action Verb] + [What They Get] + [Qualifier]. See [references/copywriting-config.md](references/copywriting-config.md).
- At this stage, focus on the argument and narrative. Do not worry about final polish yet.

---

### Phase 4: Quality (Layer 4)

#### Stage 7: Authority Audit v2
Run BEFORE any line-editing. See [references/authority-audit.md](references/authority-audit.md) for the full framework.

6 checks, each is pass/reject:

1. **Insight Test**: Could a smart person disagree with this? If no, reject.
2. **Originality Test**: Would 100 smart creators independently produce this insight? If yes, reject.
3. **Experience Test**: Could ChatGPT have written this without the author? If yes, reject.
4. **Evidence Test**: Is there a story, number, observation, or pattern supporting the claim? If no, reject.
5. **Memorability Test**: Can someone repeat this idea tomorrow? If no, reject.
6. **Save Test**: Would someone screenshot this? If no, reject.

Then score using the Content Scoring System. See [references/content-scoring.md](references/content-scoring.md).

| Dimension | Weight |
|-----------|--------|
| Insight Strength | 25 |
| Novelty | 20 |
| Credibility | 20 |
| Emotional Resonance | 15 |
| Clarity | 10 |
| Shareability | 10 |

**Every score requires a written rationale.** No score without evidence.

- 85+ = Proceed to Stage 8
- 70-84 = Improve weakest dimension, re-score, then proceed
- <70 = Return to Stage 3 (Positioning Engine) and start over

Skip for: hiring announcements, event announcements, simple reposts with commentary.

#### Stage 8: Humanizer Pass
Apply the humanizer patterns from [references/humanizer-config.md](references/humanizer-config.md) using the adaptive intensity mode determined in Stage 1.

- **Full mode** (stories, personal posts): Enforce all tiers.
- **Medium mode** (thought leadership, contrarian, career): Enforce Tier 1 + Tier 2. Skip Tier 3.
- **Light mode** (announcements, hiring, events): Enforce Tier 1 only.

Before editing any sentence, apply the false-positive protection checks:
1. Is this sentence already human-sounding? If yes, leave it alone.
2. Does the edit make the sentence better, or just different?
3. Would the author actually say this differently?
4. Am I removing personality or adding it?

#### Stage 9: Voice Calibration
Voice is the FINAL authority. It runs AFTER the humanizer so it can restore any authentic traits the humanizer may have flattened.

- Read [references/sample-posts.md](references/sample-posts.md) and match the draft's tone to the selected content pillar.
- Align with the author's personal voice markers from [references/style-guide.md](references/style-guide.md) (signature transitions, vocabulary patterns, paragraph style).
- Reference [signature-assets.md](signature-assets.md) — use the author's recurring frameworks and phrases where they fit naturally.

#### Stage 10: Voice Preservation Audit
Check that the humanizer pass did not flatten the author's voice:

- Are signature phrases intact? (check against [references/style-guide.md](references/style-guide.md) signature transitions)
- Is sentence rhythm varied? (short + medium + long, not uniform)
- Does the author's personality come through? (contrarian edge, first-person grounding, practical specificity)
- Are culturally specific references preserved? (Zee5/FIFA lines, India-specific details)

If the humanizer removed authentic traits, restore them. Voice > Humanizer. Always.

#### Stage 11: Hook Generation
This stage runs ONLY after the post body is locked. Trigger [../hook-writer/SKILL.md](../hook-writer/SKILL.md) and [references/hooks-framework.md](references/hooks-framework.md):
1. Scan the finalized body for the most surprising data points or contrarian angles.
2. Use `hook-writer` to generate social-native hooks (Dense, Punchy+Context, Single-Line Bomb, Stacked).
3. Generate psychological lever hooks (Curiosity Gap, Contrarian, Scene, Promise, Authority).
4. Present a blended list of the best 8-10 hooks across both systems, indicating which psychological lever each uses.
5. Wait for the user to select the winning hook before proceeding to Stage 12.

---

### Phase 5: Distribution (Layer 5)

#### Stage 12: LinkedIn Platform + Distribution Audit
Final checks before output. See [references/distribution-audit.md](references/distribution-audit.md).

**Platform checks:**
- **Hook check**: Does the curiosity loop survive the "see more" fold?
- **Character count**: Count characters of the plain-text version. Must be under 3,000. Optimal range: 1,800-2,800.
- **Formatting check**: 1-3 sentences per paragraph. Generous whitespace. Bold only on framework names and key phrases. 2-3 emoji types max, at start of list items only.
- **CTA check**: Post ends with one CTA. CTA must follow [Action Verb] + [What They Get] pattern.
- **No hashtags**: User handles these separately.

**Distribution prediction (score each 1-5):**
- **Comment Potential**: Will people disagree or add their perspective?
- **Save Potential**: Will people revisit this?
- **Share Potential**: Will people send this to peers?
- **Profile Click Potential**: Does this create curiosity about the author?
- **Identity Resonance**: Does this help the reader express who they are? Does it validate a tribe?

**Copywriting quality check:**
- Every paragraph advances one argument
- No sentences trying to do too much
- Zero exclamation points
- Zero marketing buzzwords without substance
- Every feature is paired with its benefit

**Image recommendation**: Assess whether the post would benefit from a companion image (visualized framework, handwritten checklist, infographic). If yes, suggest it. Don't suggest for personal stories or reflective posts.

#### Stage 13: Final Output
Present the finished post to the user. See the Output Format section below for delivery details.

---

## Layer 6: Learning (Post-Publication)

After a post is published and performance data is available, run the Learning Layer. See [references/learning-layer.md](references/learning-layer.md).

1. **Post-Mortem**: Record performance data (views, comments, reposts, saves, new followers).
2. **Pattern Mining**: After every 10 posts, extract what's working and what's not.
3. **Update the Vault**: Add new observations from comments and DMs to [insight-vault.md](insight-vault.md).
4. **Update Signature Assets**: Promote frameworks that resonate to [signature-assets.md](signature-assets.md).
5. **Feed back into the pipeline**: Update Positioning Engine preferences, Narrative Engine archetype performance, and ICP targeting.

---

## Hook Construction (Critical)

Every hook follows the 3-Step Formula. Read [references/hooks-framework.md](references/hooks-framework.md) for full details.

1. **Context Lean-In**: Topic clarity + lean-in trigger (benefit, pain point, common ground, or stunning fact). Staccato sentences: short, compressed, max clarity per word.
2. **Scroll Stop Interjection**: Single line with a contrasting word ("But", "Yet", "Except"). Freezes the reader.
3. **Contrarian Snapback**: Snap in the OPPOSITE direction of the lean-in. Complete the curiosity loop.

Hook amplifiers: lead with benefit/pain over topic, use known references (cult hopping), compress speed to value (frontload insight), staccato sentence rhythm in opening lines.

The "see more" fold on LinkedIn is the cliff edge. The curiosity loop must be unresolved at that boundary.

## Style Rules (Quick Reference)

Read [references/style-guide.md](references/style-guide.md) for full details. Key points:

- **Paragraphs**: 1-3 sentences max. Generous whitespace.
- **Voice**: Direct, first-person, contrarian, practical. Address reader as "you."
- **Structure**: Follows the selected narrative archetype, not a rigid template.
- **Frameworks**: Bold title, 3-5 items with bold labels + dash explanations.
- **Emojis**: Strategic only. 2-3 types per post. At start of list items, not inline.
- **Closing CTA**: End with one of three CTA types: engagement question (default), repost prompt (for reach), or question + follow prompt (for follower growth). See style guide for details.
- **No hashtags**: User handles these separately.

## Character Limit (Hard Rule)

LinkedIn posts have a **3,000 character hard limit** (including spaces, line breaks, and emojis). Emojis count as 2+ characters each.

After drafting, **always count characters** of the plain-text version (no markdown, as it would appear on LinkedIn). If the post exceeds 3,000 characters, cut it down before presenting to the user. Prioritize cutting:
1. Redundant explanation lines (keep the insight, drop the elaboration)
2. Framework item descriptions (shorten, don't remove items)
3. Context/history paragraphs (compress, don't eliminate)

Never cut: the hook, the framework titles, or the CTA.

**Optimal range**: 1,800-2,800 characters. Posts in this range get the highest engagement. Only approach 3,000 when the content density justifies it.

**When presenting the draft**, show the character count so the user can see headroom: e.g., "2,847 / 3,000 characters."

## Anti-Slop (Humanizer + Copywriting Integration)

The output MUST NOT read like AI-generated content and MUST persuade. These concerns are handled by the integrated systems across Phases 3-5:

- **Copywriting** (persuasion, clarity, benefit-framing): configured in [references/copywriting-config.md](references/copywriting-config.md)
- **Humanizer** (33 AI-detection patterns): configured in [references/humanizer-config.md](references/humanizer-config.md)
- **Authority Audit** (content quality gate): [references/authority-audit.md](references/authority-audit.md)

Hard rules that apply regardless of mode:
- Em-dashes (—) are never allowed. Zero exceptions.
- Every line must sound like THIS specific author, not generic LinkedIn content.

## Tone Calibration

Read [references/sample-posts.md](references/sample-posts.md) for 5 representative posts showing the author's range:
- Contrarian opener + named framework
- Data-backed argument + checklist
- Personal story + practical advice
- Problem-framework-action (tactical)
- Philosophical / reflective

Match the tone to the input material. Not every post needs a framework; some are reflective. Not every post needs data; some are personal.

## Output Format

1. **Draft**: Present the post in the conversation using markdown formatting for readability (bold, etc.). No meta-commentary like "Here's your post:" — just the post itself.
2. **Scores**: Show the Content Scoring breakdown with rationales, and the Distribution Audit scores.
3. **Confirm**: After presenting the draft, ask the user to confirm or request changes. Iterate until the user approves.
4. **Export**: Once approved, save a LinkedIn-ready `.txt` file to the working directory. **Never overwrite existing files.** Use a timestamped filename: `linkedin-post-YYYY-MM-DD-HHMMSS.txt` (e.g., `linkedin-post-2026-03-08-143052.txt`). This file must be plain text with zero markdown: no `**bold**`, no `*italics*`, no `#` headings. Only line breaks, emojis, and plain text. This is what the user will copy-paste directly into LinkedIn.
5. **Learning prompt**: After export, ask: "Once published, share performance data and I'll run the post-mortem."
