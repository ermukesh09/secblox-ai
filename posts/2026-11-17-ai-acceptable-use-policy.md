---
title: AI Acceptable Use Policy: What to Include (2026)
description: What a practical AI acceptable use policy should cover: approved tools, data rules, human review, prohibited uses, AI agents, training and enforcement.
date: 2026-11-17
tags: AI governance, AI policy, SOC 2
---

**An AI acceptable use policy tells your team which AI tools they may use, what data they may put into them, and what must be reviewed by a human before it is used.** It is usually the first AI policy a company needs, because staff are already using AI tools — approved or not. A good one is short, specific and enforceable, and it fits neatly into your existing SOC 2 policy set.

## Why you need one now

- **Data leakage:** staff paste customer data, source code or contracts into public AI tools.
- **Shadow AI:** browser extensions, meeting bots and AI features inside SaaS apps appear without review.
- **Customer questions:** security questionnaires increasingly ask whether you have an AI usage policy and how it is enforced.
- **Accountability:** when AI output is wrong, someone needs to have been responsible for checking it.

## What to include

### 1. Purpose and scope

Who it applies to (employees, contractors), and what counts as AI: chat assistants, coding assistants, AI features inside SaaS tools, browser extensions, meeting recorders and AI agents.

### 2. Approved tools

Keep a list of **approved AI tools** and the accounts to use them with (company accounts with enterprise data terms, not personal ones). New tools go through a simple request and review — security, privacy and vendor terms — before use.

### 3. Data rules

The heart of the policy. Map it to your data classification:

| Data class | Approved enterprise AI tools | Public / personal AI tools |
|---|---|---|
| Public | Allowed | Allowed |
| Internal | Allowed | Not allowed |
| Confidential (customer data, contracts, financials) | Allowed only where approved for that data | Never |
| Restricted (credentials, keys, regulated personal data) | Never | Never |

Make it explicit: **never paste secrets, API keys, passwords or customer personal data into an AI tool** unless that tool is specifically approved for it.

### 4. Human review

AI output must be reviewed by a competent person before it is:

- sent to a customer,
- merged into production code,
- used in a decision about a person (hiring, performance, access), or
- published externally.

The person who uses the output owns it.

### 5. Prohibited uses

For example: making automated decisions about individuals without human review; generating misleading content or impersonating people; bypassing security controls; uploading data you don't have the right to share; using AI to process data in ways customers haven't agreed to.

### 6. AI agents and automation

If staff use AI agents that can act (send email, change systems, run code), require: least-privilege access, approval for high-impact actions, logging, and an owner for each agent.

### 7. Transparency

Where customers interact with AI on your behalf — chatbots, AI-written replies — tell them. In the EU, telling people they are interacting with AI is now a legal requirement in many cases.

### 8. Intellectual property and confidentiality

Respect licences and third-party rights in inputs; check outputs before reusing them; keep confidential information confidential regardless of the tool.

### 9. Training and awareness

Include AI in onboarding and annual security awareness training. Short, practical examples work better than long rules.

### 10. Monitoring and enforcement

State that AI tool usage may be monitored, how violations are handled, and how to report incidents — such as accidentally pasting sensitive data — quickly and without blame.

### 11. Ownership and review

Name the policy owner and review it at least annually, or when you adopt significant new AI tools.

## How it supports SOC 2

An AI acceptable use policy plugs straight into existing SOC 2 controls: it extends your **acceptable use and data classification policies**, feeds **vendor management** (approved tools), is covered by **security awareness training**, and gives your auditor clear evidence that AI risk is governed. It is also a building block for [ISO 42001](/iso-42001/) and the [NIST AI RMF](/blog/nist-ai-rmf-explained/) "Govern" function.

## Common mistakes

- **Banning AI outright** — staff use it anyway, just unmanaged. Approve good tools instead.
- **No data rules** — "use AI responsibly" is not enforceable; data-class rules are.
- **No tool list** — people can't comply with a policy that doesn't say what's approved.
- **Set and forget** — AI tools change monthly; review the approved list quarterly.

## FAQ

### How long should an AI acceptable use policy be?

Two to four pages is enough for most companies. Put detail (the approved tool list) in an appendix that can be updated without re-approving the whole policy.

### Should we block public AI tools?

Block or restrict them for confidential data, and provide an approved alternative. Blocking without an alternative drives shadow AI.

### Is this the same as an AI governance policy?

No. Acceptable use covers how **staff** use AI. A broader AI governance or AI development policy covers how your **company builds and runs** AI systems. Most companies need both. See [AI governance for SaaS startups](/blog/ai-governance-for-saas-startups/).

Want a ready-to-adopt AI policy set aligned to SOC 2 and ISO 42001? [Book a free scoping call](/contact/).
