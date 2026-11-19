---
title: Shadow AI: Find and Govern Unapproved AI Tools
description: Shadow AI explained for SaaS teams: where unapproved AI tools hide, how to discover them, and a practical way to govern them without banning AI.
date: 2026-11-17
tags: AI governance, shadow AI, SOC 2
updated: 2026-11-19
takeaways: Shadow AI is any AI tool staff use without security or IT review, such as browser extensions, meeting bots, personal chatbot accounts and AI features inside SaaS apps.|It is usually well-intentioned but sends company and customer data to places you haven't assessed.|The fix is not a ban: discover what is in use, offer a fast approval path and keep a short list of approved tools.|Shadow AI controls map to SOC 2 vendor management (CC9), logical access (CC6), monitoring (CC4) and incident response (CC7).
---

**Shadow AI is any AI tool your staff use without security or IT review — browser extensions, meeting bots, personal chatbot accounts, AI features switched on inside SaaS apps.** It's usually well-intentioned, but it sends company and customer data to places you haven't assessed. The fix isn't a ban; it's discovery, a fast approval path and a short list of approved tools people actually want to use.

## Why shadow AI is a real risk

- **Data leakage** — customer data, source code, contracts and credentials pasted into tools with unknown retention or training terms
- **Contract breaches** — customer agreements often restrict where their data can be processed
- **Audit gaps** — SOC 2 auditors and enterprise buyers increasingly ask how you control AI tool usage
- **Inaccurate output** — unreviewed AI content reaching customers or decisions
- **Over-privileged integrations** — AI apps granted broad OAuth access to email, drives or code

## Where shadow AI hides

| Place | Examples |
|---|---|
| Personal accounts | Staff using personal chatbot logins for work |
| Browser extensions | Writing assistants, summarisers, "chat with this page" tools |
| Meeting tools | AI note-takers joining calls automatically |
| SaaS features | AI assistants enabled inside CRM, docs, ticketing or design tools |
| OAuth-connected apps | AI tools granted access to email, calendars, drives or repositories |
| Developer tools | AI coding assistants, CLI tools, API keys on personal cards |

## How to discover it

1. **Review OAuth grants** in your identity provider and workspace admin consoles — look for AI apps with access to mail, files or code.
2. **Check browser extension inventories** through your device management tooling.
3. **Review SaaS admin settings** for AI features that are on by default.
4. **Check expenses and card statements** for AI subscriptions.
5. **Look at DNS or web proxy logs** for traffic to AI services, where you have that visibility.
6. **Ask people.** A short, blame-free survey ("which AI tools help you work?") often finds more than technical discovery, and tells you which tools to approve.

## How to govern it without killing productivity

### Approve good tools quickly

Pick a small set of approved AI tools with company accounts and enterprise data terms — no training on your data, limited retention, SSO. If people have a good approved option, most shadow use disappears.

### Make the request path fast

A simple form and a decision within days. Review data use, retention, training terms, security assurance and the access the tool needs. A slow process creates more shadow AI.

### Set clear data rules

Spell out which data classes can go into which tools — and that credentials, keys and restricted personal data never go into any AI tool. Our [AI acceptable use policy guide](/blog/ai-acceptable-use-policy/) has a ready-made table.

### Put technical guardrails where they matter

- Restrict OAuth consent so users can't grant AI apps broad access without approval
- Manage browser extensions on company devices
- Turn off AI features in SaaS apps until reviewed
- Apply data loss prevention to the highest-risk data where you can

### Train and keep reviewing

Include AI in onboarding and annual awareness training, and review the approved list quarterly — AI tools change fast.

## How this maps to SOC 2

| Shadow AI control | SOC 2 area |
|---|---|
| Approved AI tool list and request process | Vendor management (CC9) |
| OAuth and extension restrictions | Logical access (CC6) |
| AI acceptable use policy and training | Control environment, communication (CC1, CC2) |
| Discovery reviews | Monitoring (CC4) |
| AI data incidents in your playbook | Incident response (CC7) |

See [AI governance for SaaS startups](/blog/ai-governance-for-saas-startups/) for the wider program and [AI vendor risk assessment questions](/blog/ai-vendor-risk-assessment-questions/) for reviewing tools.

## FAQ

### Should we block public AI tools?

Restrict them for confidential data and give people an approved alternative. Blocking without an alternative pushes usage onto personal devices where you have no visibility.

### How often should we look for shadow AI?

Run discovery at least quarterly, and check OAuth grants and new SaaS AI features monthly if you can.

### Is a policy enough?

No. A policy sets expectations, but you need discovery, an approved tool list and a few technical controls to make it real — and auditors will look for evidence of all three.

Need help getting AI tool usage under control? [Book a free scoping call](/contact/) or see our [AI governance service](/ai-governance/).
