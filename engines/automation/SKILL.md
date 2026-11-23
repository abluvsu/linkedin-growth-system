---
name: linkedin-automation
description: Automate LinkedIn marketing, lead generation, content publishing, and professional networking via MCP server workflows and Python scripts.
version: 1.0.0
---

# LinkedIn Automation Engine

Comprehensive engine for orchestrating LinkedIn content scheduling, B2B lead generation workflows, connection outreach sequences, and MCP-based automation scripts.

## System Architecture

```
engines/automation/
├── SKILL.md                         # Autonomous pipeline specification & templates
└── scripts/                         # Python MCP execution scripts
    ├── draft_outbound.py            # Searches people via MCP, creates approval queue
    ├── send_outbound.py             # Sends approved connection invites via MCP
    ├── draft_followup.py            # Follow-up drafter based on sent_log.csv
    └── send_followup.py             # Follow-up message sender
```

## Safety Thresholds & Human-in-the-Loop (HitL) Protocol

1. **Daily Volume Limits:**
   - Outbound Connection Invites: Max 20/day
   - Follow-up Direct Messages: Max 30/day
   - Comments / Engagements: Max 50/day
2. **Approval Queues:**
   - Automation scripts NEVER send blind messages without explicit human sign-off.
   - `draft_outbound.py` generates `outbound_queue.md`. The operator must review and check `[x]` before `send_outbound.py` transmits.
   - `draft_followup.py` generates `followup_queue.md` with inbox context for verification before `send_followup.py` transmits.
3. **Data Security & Privacy:**
   - Sent logs (`sent_log.csv`, `followup_log.csv`) and queue files with personal names/URLs are strictly excluded from Git tracking via `.gitignore`.

---

## Core Workflows

### 1. Content Pipeline
1. **Content Planning:** Topics, pillars, and weekly posting rhythm.
2. **Drafting:** Narrative, data case studies, carousels (PDF), and single-line bombs.
3. **Hook Optimization:** Calibration to mobile truncation points (<210 chars total, <75 chars/line).
4. **Publish & First-Hour Engagement:** Accelerating algorithmic dwell time by responding to comments within 60 minutes.

### 2. Lead Generation & Outreach Flow
```yaml
lead_gen_workflow:
  search:
    filters:
      - industry: "Healthcare / SaaS / Insurance / AI"
      - company_size: "11-50, 51-200"
      - title_contains: ["Founder", "CEO", "DSO Operator", "VP Engineering", "Head of Product", "VP Analytics"]
  qualify:
    criteria:
      - has_recent_activity: true
      - mutual_connections: "> 2"
  outreach:
    sequence:
      - action: connect
        message: connection_request (personalized reference to their post/company)
      - wait: 2_days
      - action: message
        template: pain_point_inquiry
      - wait: 4_days
      - action: follow_up
        template: value_add_asset (send framework / lead magnet free)
```

---

## Outbound Connection Templates

### A. Mutual Connection & Peer Operator
```text
Hi {{first_name}},
I noticed we're both connected to {{mutual}} and following the AI in healthcare space.
Really impressed by what you're building at {{company}}.
Would love to connect and follow your updates!
Best,
Ashutosh
```

### B. Shared Discussion / Post Insight
```text
Hi {{first_name}},
Came across your thoughts on {{topic}}—agreed on the point about {{key_insight}}.
I've been writing about operational automation and AI in regulated sectors, would love to stay connected here.
Best,
Ashutosh
```

### C. Engineering & AI Leader (ICICI Enterprise Credential)
```text
Hi {{first_name}},
I saw your company has been growing. I have been building production AI systems at ICICI Prudential for 4+ years, including a predictive model that cut a 7-day manual process to 15 minutes under full regulatory compliance. If your team is hiring for AI or engineering roles, I would love to connect.
Best,
Ashutosh
```

---

## Script Execution Guide

### 1. Staging Outbound Messages
Run the drafter script to query profiles matching your target criteria via the MCP server:
```powershell
python engines/automation/scripts/draft_outbound.py
```
This inspects candidate profiles and generates an approval queue. Review the queue and place an `[x]` next to approved candidates.

### 2. Transmitting Approved Connections
Execute the sender script:
```powershell
python engines/automation/scripts/send_outbound.py
```
This sends personalized invitations with notes and appends timestamped records to `sent_log.csv`.

### 3. Drafting Follow-ups (3+ Days Inactive)
```powershell
python engines/automation/scripts/draft_followup.py
```
Scans `sent_log.csv` for connections accepted 3+ days ago without recent replies, generates conversational context, and prepares `followup_queue.md`.

### 4. Sending Approved Follow-ups
```powershell
python engines/automation/scripts/send_followup.py
```
Transmits conversational follow-up messages to approved connections.

---

## Best Practices
1. **Consistency:** Post 3-5 times per week.
2. **Value First:** Give high-utility lead magnets without asking for payment.
3. **Engage Authentically:** 16-20+ word constructive comments on peer and prospect posts daily.
4. **Zero Fluff:** Strict focus on quantified business outcomes (time saved, revenue recovered, error rates reduced).
