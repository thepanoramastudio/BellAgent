# Bell Agent — AI Customer Support System

## Project Overview

An AI-powered customer support system for a tech company, delivered via LINE Official Account, with a multi-tier agent hierarchy mirroring the human team structure.

---

## Service Requirements

| Item | Detail |
|---|---|
| **Service Channel** | LINE Official Account (LINE Messaging API) |
| **Knowledge Base** | NotebookLM (source docs exported → custom RAG) |
| **Ticket System** | Odoo 19 (Helpdesk module) |
| **Company Type** | Tech company |

---

## Core Rule

> **Every incoming LINE message must create an Odoo ticket immediately — regardless of whether it needs escalation or not.**

---

## Team & AI Hierarchy

```
Customer (LINE)
     │
     ▼ [TICKET CREATED IMMEDIATELY — every case]
     │
AI Agent (L1)
  ├── resolved → update ticket: closed
  └── needs escalation → AI Supervisor routes to...
          │
          ├── Human Agent (L1)      — general / non-technical
          ├── L2 Technical Support  — product issues, config, bugs
          └── L2 Developer          — code-level, API, integration bugs
                    │
               AI Manager (L3)
               monitors all tiers, reporting, alerts
```

---

## AI Role Breakdown

| AI Tier | Role | Tools |
|---|---|---|
| **AI Agent (L1)** | Answers all incoming cases, records every ticket | LINE API, Odoo (create ticket), RAG knowledge base |
| **AI Supervisor (L2)** | Classifies issue type, routes escalations to correct team | Odoo (update/assign ticket), team availability check |
| **AI Manager (L3)** | Monitors all tiers, generates reports, sends alerts | Odoo (read all tickets), LINE notify to managers |

> L2 Technical Support and L2 Developer are **human roles**. AI Supervisor routes to them; they perform the work. AI assistance at L2 (suggested solutions, similar past tickets) can be added in a later phase.

---

## Ticket Flow

```
Message arrives on LINE
     │
     ├── 1. Create Odoo ticket immediately (status: open, assigned: AI Agent)
     ├── 2. AI Agent queries knowledge base (RAG) and attempts resolution
     │
     ├── Resolved by AI?
     │     └── Update ticket: resolved_by=AI, status=closed
     │
     └── Not resolved?
           ├── AI Supervisor classifies issue type
           │     ├── General / Account / Billing  → Human Agent (L1)
           │     ├── Technical / Config / Bug      → L2 Technical Support
           │     └── Code / API / Integration      → L2 Developer
           └── Update ticket: reassigned to correct team, status=in-progress
```

---

## Issue Classification Rules (AI Supervisor)

| Keywords / Signals | Route To |
|---|---|
| "error", "crash", "API", "code", "integration", "bug in code" | L2 Developer |
| "not working", "wrong config", "setup", "feature broken" | L2 Technical Support |
| "billing", "account", "password", "general question" | Human Agent (L1) |
| Unclear / ambiguous | Human Agent (L1) as fallback |

---

## Odoo Ticket Schema

Replicated from current Jira ticket structure:

```
--- Core ---
- status                  : open | in-progress | resolved | closed | done
- priority                : 1-Critical | 2-High | 3-Medium | 4-Low
- issued_date_time        : timestamp (when message was received)
- description             : full customer message / issue description

--- POS / Channel Info ---
- channel                 : LINE channel name (e.g. Line@WePOS)
- project_name            : project the customer belongs to (e.g. CPF)
- shop_name               : customer's shop name
- customer_name           : customer's name
- contact_number          : customer's phone number
- device                  : device type (if applicable, else None)

--- Issue Classification ---
- category                : main category (e.g. Request, Incident, Bug)
- sub_category            : sub category (e.g. Payment Package Subscription)
- problem                 : problem type (if applicable)
- sub_problem             : sub problem (if applicable)

--- Routing & Action ---
- action_card             : L1 action | L2 action | L2-Tech action | L2-Dev action
- request_type            : General Request | Technical | Developer
- assignee                : assigned agent/team member
- reporter                : who created the ticket (AI or human)
- ref_ticket_no           : reference ticket number for linked/parent cases

--- Resolution ---
- resolution_for_cs       : FCR (First Call Resolution) | Escalated | Workaround | Pending
- resolved_by             : AI | Human-L1 | L2-Tech | L2-Dev

--- SLA ---
- sla_first_response      : target per priority — actual: first_response_at timestamp
- sla_time_to_escalate    : target per priority — actual: escalated_at timestamp
- sla_time_to_resolution  : target per priority — actual: resolved_at timestamp
- resolve_time            : duration in minutes (resolved_at - issued_date_time)

--- Tracking ---
- pos_sla                 : SLA tier applied to this ticket (if custom per project)
- worklog_timer           : time spent working on ticket (for reporting)
```

---

## System Architecture

```
Customer (LINE)
     │
     ▼
LINE Messaging API (Webhook)
     │
     ▼
Backend Server (Python / FastAPI)
     ├── AI Agent (L1)      ←── RAG (vector search over knowledge base docs)
     ├── AI Supervisor      ←── classification logic + Odoo assignment
     ├── AI Manager (L3)    ←── scheduled reporting + alerting
     └── Odoo 19 REST API   ←── create / update / query tickets
```

---

## Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | Python, FastAPI |
| **AI Model** | Claude API (claude-sonnet-4-6) |
| **Vector DB** | Supabase pgvector |
| **Knowledge Base** | Source docs exported from NotebookLM → embedded into vector DB |
| **Ticket System** | Odoo 19 (JSON-RPC / REST API) |
| **LINE Integration** | LINE Messaging API (webhook) |
| **Hosting** | Railway or Render (requires public HTTPS for LINE webhook) |

---

## Knowledge Base Strategy

NotebookLM has no public API. Approach:
- Use NotebookLM as an **authoring and review tool** only
- Export source documents → ingest into Supabase pgvector
- AI Agent queries vector DB at runtime (RAG pattern)
- Keep source docs in sync between NotebookLM and vector DB when updated

---

## Planned Development Phases

1. **Phase 1** — LINE webhook + Odoo ticket creation (every message)
2. **Phase 2** — AI Agent (L1) with RAG knowledge base
3. **Phase 3** — AI Supervisor with classification and routing
4. **Phase 4** — AI Manager reporting and alerting
5. **Phase 5** *(optional)* — AI assistance tools for L2 human teams

---

## SLA Targets by Priority

> Medium (3) is the baseline from current Jira config. Adjust Critical/High/Low to match your policy.

| Priority | First Response | Time to Escalate | Time to Resolution |
|---|---|---|---|
| **1 - Critical** | 5 min | 1 hour | 4 hours |
| **2 - High** | 5 min | 4 hours | 8 hours |
| **3 - Medium** | 5 min | 24 hours | 36 hours |
| **4 - Low** | 15 min | 48 hours | 72 hours |

### SLA Breach Behavior
- **First Response breached** → AI Manager alerts supervisor immediately
- **Time to Escalate breached** → auto-escalate ticket to next tier, notify team lead
- **Time to Resolution breached** → notify manager, flag ticket as SLA-breached in Odoo

### Priority Assignment Rules (AI Agent)
| Signal | Priority |
|---|---|
| System down, cannot operate, data loss | 1 - Critical |
| Major feature broken, affects multiple users | 2 - High |
| Single feature issue, workaround exists | 3 - Medium |
| General question, cosmetic issue, low urgency | 4 - Low |
| Not specified by customer | default: 3 - Medium |

---

## Agent Prompts

---

### AI Agent (L1) — System Prompt

```
You are Bell, an AI customer support agent for a tech company.
You communicate with customers via LINE Official Account in a friendly, professional tone.
You support both Thai and English — always reply in the same language the customer uses.

Your job on every incoming message:
1. Immediately create an Odoo support ticket with all available customer information.
2. Search the knowledge base for a relevant answer.
3. If you can resolve the issue confidently, reply to the customer and close the ticket.
4. If you cannot resolve it, do NOT guess. Tell the customer you are escalating and pass the case to the Supervisor.

When creating a ticket, collect and fill in:
- customer_name, contact_number, shop_name, project_name (ask if not provided)
- channel: the LINE channel this message came from
- description: the full customer message
- category & sub_category: classify based on the message
- priority: assign based on urgency signals (default: 3-Medium)
- action_card: L1 action
- reporter: AI

Priority assignment rules:
- System down / cannot operate / data loss → 1-Critical
- Major feature broken / affects multiple users → 2-High
- Single issue / workaround exists → 3-Medium
- General question / low urgency → 4-Low

Always be concise, empathetic, and solution-focused.
Never share internal ticket IDs, system errors, or technical details with the customer.
If escalating, say: "ขณะนี้กำลังส่งเรื่องให้ทีมผู้เชี่ยวชาญดูแลต่อครับ/ค่ะ กรุณารอสักครู่"
(English: "I'm escalating your case to our specialist team. Please wait a moment.")
```

**Tools available to AI Agent (L1):**
- `create_odoo_ticket` — create ticket on every incoming message
- `update_odoo_ticket` — update status, resolution, resolved_by
- `search_knowledge_base` — RAG query over support docs
- `reply_line_message` — send reply to customer on LINE
- `escalate_to_supervisor` — hand off case with full context

---

### AI Supervisor — System Prompt

```
You are the Bell Supervisor, an AI routing agent for a tech company support system.
You receive escalated cases from the AI Agent (L1) that could not be resolved automatically.

Your job:
1. Read the full ticket context: customer message, category, priority, conversation history.
2. Classify the issue into one of three routing targets:
   - Human Agent (L1): general questions, account, billing, unclear issues
   - L2 Technical Support: product bugs, configuration issues, feature not working
   - L2 Developer: code-level bugs, API errors, integration failures, data issues
3. Assign the ticket to the correct team in Odoo.
4. Notify the assigned team via LINE or internal channel.
5. Send a holding message to the customer confirming their ticket number and expected response time.

Classification rules:
- Keywords: "error", "crash", "API", "code", "integration", "webhook", "database" → L2 Developer
- Keywords: "not working", "wrong config", "setup", "cannot access", "feature broken" → L2 Technical Support
- Keywords: "billing", "account", "password", "general", "how to" → Human Agent (L1)
- Ambiguous or unclear → Human Agent (L1) as fallback

SLA to communicate to customer (by priority):
- Critical: resolution within 4 hours
- High: resolution within 8 hours
- Medium: resolution within 36 hours
- Low: resolution within 72 hours

Always update the Odoo ticket:
- action_card: set to correct tier (L2-Tech action / L2-Dev action / L1 action)
- assignee: set to correct team
- status: in-progress
- request_type: Technical | Developer | General Request
```

**Tools available to AI Supervisor:**
- `read_odoo_ticket` — get full ticket details
- `update_odoo_ticket` — reassign, update action_card, status, request_type
- `notify_team` — send LINE/internal notification to assigned team
- `reply_line_message` — send ticket confirmation message to customer

---

### AI Manager (L3) — System Prompt

```
You are the Bell Manager, an AI operations monitor for a tech company support system.
You run on a scheduled basis and also respond to SLA breach alerts in real time.

Your responsibilities:

1. SLA Monitoring (real-time):
   - Watch all open tickets for SLA breach risk
   - First response breached → alert supervisor immediately
   - Time to escalate breached → auto-escalate + notify team lead
   - Time to resolution breached → notify manager, flag ticket as SLA-breached

2. Daily Report (scheduled — end of business day):
   - Total tickets created
   - Resolved by AI vs Human breakdown
   - Average resolve time per priority
   - SLA breach count and which tickets breached
   - Top 3 issue categories of the day
   - Knowledge base gaps (questions AI could not answer)

3. Knowledge Gap Detection:
   - Flag recurring questions that the AI Agent could not resolve
   - Report to manager as candidates for knowledge base updates

Always present reports in a clear, structured format.
Send daily reports to the manager via LINE notify.
Send real-time SLA alerts immediately when triggered.
```

**Tools available to AI Manager (L3):**
- `query_odoo_tickets` — read and filter all tickets
- `flag_sla_breach` — mark ticket as SLA-breached in Odoo
- `escalate_ticket` — force-escalate a ticket to next tier
- `send_line_notify` — push report/alert to manager LINE
- `generate_report` — compile daily or on-demand report

---

## Tool Definitions Summary

| Tool | Used By | Purpose |
|---|---|---|
| `create_odoo_ticket` | L1 Agent | Create ticket on every message |
| `update_odoo_ticket` | L1 Agent, Supervisor | Update status, assignee, resolution |
| `read_odoo_ticket` | Supervisor, Manager | Read full ticket details |
| `query_odoo_tickets` | Manager | Filter/aggregate tickets for reporting |
| `flag_sla_breach` | Manager | Mark ticket as SLA-breached |
| `escalate_ticket` | Manager | Force-escalate overdue ticket |
| `search_knowledge_base` | L1 Agent | RAG query over support docs |
| `reply_line_message` | L1 Agent, Supervisor | Send message to customer on LINE |
| `escalate_to_supervisor` | L1 Agent | Hand off unresolved case |
| `notify_team` | Supervisor | Notify assigned human team |
| `send_line_notify` | Manager | Push alert/report to manager |
| `generate_report` | Manager | Compile daily/on-demand report |

---

## Notes

- LINE reply tokens expire in 30 seconds — backend must respond quickly; use async processing
- Odoo 19 supports REST API via `/web/dataset/call_kw` and newer REST endpoints
- AI Agent must always create a ticket BEFORE attempting to answer — never skip ticket creation
- All agent prompts above are starting points — tune with real conversation examples after testing
