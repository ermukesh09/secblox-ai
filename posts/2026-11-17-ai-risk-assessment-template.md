---
title: AI Risk Assessment Template (NIST AI RMF Aligned)
description: A practical AI risk assessment template aligned to the NIST AI RMF: what to capture, a scoring method, common AI risks and how to keep it current.
date: 2026-11-17
tags: AI governance, NIST AI RMF, risk assessment
updated: 2026-11-19
takeaways: An AI risk assessment records what an AI system does, what could go wrong, how likely and severe it is, and how you treat it.|This template follows the four NIST AI RMF functions: Govern, Map, Measure and Manage.|It takes about an hour per AI system and can be reused for SOC 2, ISO 42001 and customer questionnaires.|Review each assessment when the model, data or use case changes, and at least once a year.
---

**An AI risk assessment records what an AI system does, what could go wrong, how likely and severe that is, and what you're doing about it.** Below is a practical template aligned to the four NIST AI RMF functions — Govern, Map, Measure, Manage — that a SaaS company can complete in about an hour per system and reuse for SOC 2, ISO 42001 and customer questionnaires.

## Section 1: System profile (Govern + Map)

| Field | What to record |
|---|---|
| System name | e.g. "Support reply assistant" |
| Owner | Accountable person |
| Purpose | What business problem it solves |
| Your role | Developer, provider, deployer — or several |
| Users | Internal staff, customers, end users |
| Affected people | Who is impacted by outputs, even if they never use it |
| Model(s) and provider | Model, version, hosting |
| Data inputs | Types and sensitivity (customer data, personal data, confidential) |
| Outputs | What it produces and where outputs go |
| Autonomy | Suggests only, acts with approval, or acts automatically |
| Regulatory flags | EU AI Act category, sector rules, contractual commitments |

## Section 2: Risk identification (Map)

Assess each category and note specific scenarios:

| Category | Example risks |
|---|---|
| Security | Prompt injection, data exfiltration, over-privileged agents, API key abuse |
| Privacy | Personal data in prompts, logs or training; retention by providers |
| Accuracy / reliability | Hallucinations, outdated knowledge, drift after model updates |
| Fairness | Biased outcomes in decisions about people |
| Transparency | Users unaware they interact with AI; unmarked generated content |
| Safety / misuse | Harmful content, use outside intended purpose |
| Third-party | Provider outage, terms changes, sub-processors |
| Legal / contractual | EU AI Act obligations, customer contract terms, IP |

## Section 3: Scoring (Measure)

Use a simple 1–5 scale for **likelihood** and **impact**, then multiply:

| Score | Rating | Action |
|---|---|---|
| 15–25 | High | Treat before launch or immediately; leadership sign-off |
| 8–14 | Medium | Treatment plan with owner and date |
| 1–7 | Low | Accept or monitor |

Base likelihood on evidence where you can: test results, red-team findings, incident history, monitoring data.

## Section 4: Treatment (Manage)

For each medium or high risk record: the **control** (e.g. tenant-filtered retrieval, human approval, output filtering), the **owner**, the **due date**, the **residual risk** after treatment, and the **decision** — mitigate, transfer, avoid or accept (with who accepted it).

## Section 5: Monitoring and review (Manage)

- Metrics to watch (error rates, user complaints, flagged outputs, abuse attempts)
- Review triggers: model or provider change, new data types, new user groups, incidents
- Review date — at least annually

## Example: support reply assistant

| Risk | L | I | Score | Treatment |
|---|---|---|---|---|
| Reply includes another customer's data via retrieval | 2 | 5 | 10 | Permission-filtered retrieval; cross-tenant tests in CI |
| Inaccurate answer sent to customer | 3 | 3 | 9 | Agent reviews before sending; feedback loop |
| Prompt injection through ticket content | 3 | 3 | 9 | No tool access beyond drafting; output filtering |
| Provider retains ticket data | 2 | 3 | 6 | Zero-retention terms; vendor review |

## How it connects to SOC 2 and ISO 42001

Add AI systems to your existing SOC 2 risk register rather than keeping a separate one. For ISO 42001, extend this template with an **AI system impact assessment** covering effects on individuals and society. See [NIST AI RMF explained](/blog/nist-ai-rmf-explained/) and [ISO 42001 readiness](/iso-42001/).

## FAQ

### How many AI systems need an assessment?

Every system in your AI inventory, scaled to risk. An internal summarisation tool needs a short assessment; a customer-facing agent needs the full template.

### Who should complete it?

The system owner, with input from engineering, security and — for decisions about people — legal or HR.

### How often should it be updated?

At least annually, and whenever the model, provider, data or use changes materially.

Related: [NIST AI RMF explained](/blog/nist-ai-rmf-explained/) and [AI vendor risk assessment questions](/blog/ai-vendor-risk-assessment-questions/). Want help assessing your AI systems? [Book a free scoping call](/contact/) or see our [AI governance service](/ai-governance/).
