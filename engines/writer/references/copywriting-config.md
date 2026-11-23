# Copywriting Integration Configuration

This file configures how the LinkedIn Writer uses the Copywriting skill.

## Purpose

The linkedin-writer has voice calibration (author style) and AI-pattern removal (humanizer). Copywriting fills the third gap: **persuasion mechanics**. Every sentence in a LinkedIn post must earn its place by being clear, benefit-oriented, and specific.

## Conflict Resolution

Copywriting principles sit between Voice Rules and Humanizer Rules in the hierarchy:

```
Voice Rules (author's personal style)      ← highest priority
    ↓
Copywriting Rules (persuasion mechanics)
    ↓
Platform Rules (LinkedIn formatting)
    ↓
Humanizer Rules (AI-pattern removal)       ← lowest priority
```

**Conflicts and resolutions:**

- Copywriting says "remove exclamation points." Author style never uses them either. → No conflict. Both agree.
- Copywriting says "use rhetorical questions to engage." Humanizer says "avoid conversational rhetorical openers." → **Copywriting wins for hooks and CTAs.** Humanizer wins for body paragraphs. Rhetorical questions in the hook or as a closing CTA are a proven LinkedIn engagement mechanic. Mid-post rhetorical questions that sound like AI filler should be cut.
- Copywriting says "be direct, don't bury value in qualifications." Author style uses some setup before the payoff. → **Voice wins.** The author's 3-step hook formula (lean-in → scroll-stop → snapback) deliberately delays the payoff. That's a voice choice, not a clarity failure.
- Copywriting says "use analogies." Humanizer says "avoid aphorism formulas." → **Copywriting wins IF the analogy adds clarity.** "Like autocomplete for boring code" is a useful analogy. "Symmetry is the language of trust" is an aphorism formula. The test: does it make a concrete concept clearer, or does it make a vague concept sound deep?

---

## How Copywriting Maps to Pipeline Stages

### Stage 4: Insight Extraction → Benefit Framing

Before naming the insight, run it through the **Benefits Over Features** filter:

| Feature framing (weak) | Benefit framing (strong) |
|------------------------|--------------------------|
| "7 LLM stages process your resume" | "Your resume gets rewritten around the problem the company is hiring to solve" |
| "Skill gap analysis against the JD" | "You know exactly what you are missing before you apply" |
| "Chat interface for edits" | "Correcting a detail takes 30 seconds, not a full restart" |
| "5 models running concurrently" | "100+ users at the same time, probably faster than streaming the FIFA match on Zee5" |

The insight should be framed as: **what changes for the reader**, not what the product does.

### Stage 6: Draft Creation → Headline Formulas + Structure

**Hook construction** should layer copywriting formulas on top of the 3-step hook formula:

Headline formula options (adapted for LinkedIn hooks):
- "{Achieve outcome} without {pain point}" → "Get through to hiring managers without keyword-stuffing your resume"
- "Never {unpleasant event} again" → "Never rewrite your resume from scratch again"
- "{Question highlighting main pain point}" → "Why does every resume tool optimize for the filter instead of the job?"

**One Idea Per Paragraph**: Each paragraph advances exactly one argument. If a paragraph makes two points, split it.

**CTA construction** should follow the copywriting CTA formula:
- Weak: "Comment below" / "Let me know"
- Strong: [Action Verb] + [What They Get] + [Qualifier]
- LinkedIn adaptation: "Comment 'access code' and I will DM you one" ← already follows this pattern (action + what they get)

### Stage 9: Voice Calibration → Writing Style Rules

Apply the 6 copywriting style rules as a checklist during voice calibration:

1. **Simple over complex**: "Use" not "utilize." "Help" not "facilitate." "Fix" not "remediate."
2. **Specific over vague**: Kill "streamline," "optimize," "innovative," "cutting-edge." Replace with what specifically happens.
3. **Active over passive**: "CareerFlow reads the JD" not "The JD is read by CareerFlow."
4. **Confident over qualified**: Remove "almost," "very," "really," "just," "actually" (unless "actually" is used as a contrarian marker, which is an author voice choice).
5. **Show over tell**: "The rewrites read like a different person wrote them" > "The rewrites are significantly better."
6. **Honest over sensational**: Never fabricate statistics, testimonials, or outcomes. If you don't have a number, don't invent one.

### Stage 11: LinkedIn Platform + Distribution Audit → Persuasion Quality Check

After the existing platform checks, add a **Copywriting Quality Check**:

- [ ] Every paragraph advances exactly one argument
- [ ] No sentences are trying to do too much (split if needed)
- [ ] No passive voice constructions remain (unless intentional for rhythm)
- [ ] Zero exclamation points
- [ ] Zero marketing buzzwords without substance ("innovative," "cutting-edge," "revolutionary")
- [ ] Every feature mentioned is paired with its benefit or outcome
- [ ] CTA follows [Action Verb] + [What They Get] pattern
- [ ] Jargon is either explained or replaced with plain language

---

## LinkedIn-Specific Adaptations

The copywriting skill is designed for web pages. These adaptations make it work for LinkedIn posts:

| Web Copywriting | LinkedIn Adaptation |
|-----------------|---------------------|
| Above the fold = hero section | Above the fold = first 2-3 lines before "see more" |
| Primary CTA = button | Primary CTA = comment prompt or engagement question |
| Social proof = logos, stats | Social proof = specific numbers, named experiences |
| How It Works = 3-4 steps | How It Works = named stages or framework items |
| Objection handling = FAQ section | Objection handling = preemptive line in the body ("I am not monetizing this") |
| Risk reversal = guarantee | Risk reversal = "free, unlimited, for life" or "no cost, I want feedback" |
