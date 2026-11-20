---
title: SOC 2 Readiness Assessment: What It Covers
description: What a SOC 2 readiness assessment covers, what you should get at the end, how long it takes and how to tell if your startup is ready for the audit.
date: 2026-11-19
tags: SOC 2, startups, readiness
keyword: soc 2 readiness assessment
takeaways: A SOC 2 readiness assessment compares your current controls against the Trust Services Criteria before the auditor does.|It should deliver a gap list, a prioritised remediation plan with owners, a scope recommendation, a target audit date and evidence guidance.|The assessment usually takes one to two weeks; remediation typically takes four to eight weeks.|It is optional, but skipping it is the most common reason first audits run late or come back with exceptions.
---

**A SOC 2 readiness assessment is a pre-audit review that compares your current security controls against the SOC 2 Trust Services Criteria, then tells you exactly what to fix before an auditor looks.** Done well, it turns "we need SOC 2" into a scoped, prioritised plan with a realistic audit date, so you don't pay for an audit you aren't ready to pass.

## Why do one before the audit

A CPA firm performs the SOC 2 audit itself and reports what it finds. It won't build your controls for you, and gaps found during fieldwork end up as exceptions in the report your customers read. A readiness assessment moves that discovery earlier, when fixing things is cheap and nothing is on the record.

It also answers the questions founders actually ask:

- Which Trust Services Criteria do we need? Most startups start with **Security** only.
- Type I or Type II first? See [SOC 2 Type I vs Type II](/blog/soc-2-type-1-vs-type-2/).
- What's in scope: which product, which cloud accounts, which people and vendors?
- How much work is left, and when can the audit realistically start?

## What a readiness assessment covers

| Area | What gets reviewed |
|---|---|
| Scope and system boundaries | Product, infrastructure, data flows, subprocessors |
| Governance | Security policies, roles, risk assessment, board or management oversight |
| Access control | SSO/MFA, joiner-mover-leaver process, privileged access, access reviews |
| Change management | Code review, CI/CD controls, separation of duties, deployment approvals |
| Infrastructure security | Cloud configuration, logging and monitoring, encryption, vulnerability management |
| Operations | Incident response, backups and restore testing, business continuity |
| People | Background checks, security training, onboarding and offboarding |
| Vendors | Vendor inventory, risk reviews, contracts with security terms |
| AI systems (if you build with AI) | Model and LLM vendors, data used in prompts, AI-specific risks and controls |

## What you should get at the end

A readiness assessment is only useful if it produces something you can act on. Expect:

1. **A gap list** — every control mapped to the criteria, marked in place, partial or missing
2. **A prioritised remediation plan** — what to fix first, who owns it, and how long it should take
3. **A scope recommendation** — criteria, systems and Type I or Type II
4. **A target audit date** — based on the real remaining work, not optimism
5. **Evidence guidance** — what the auditor will ask for and how to collect it continuously

If you only get a spreadsheet of findings with no plan or owners, you've paid for half the job.

## How long it takes

For a typical SaaS startup, the assessment itself takes **one to two weeks**: a few working sessions with engineering and leadership, plus a review of your cloud environment and documents. Remediation afterwards usually takes **four to eight weeks**, depending on how much exists already. See [how long SOC 2 takes](/blog/how-long-does-soc-2-take/) for the full timeline.

Want a quick first read? Try our free [SOC 2 readiness checklist](/soc-2-readiness-checklist/) — 15 questions with a score and your top gaps.

## Signs you're ready for the audit

- Policies are approved and people have actually acknowledged them
- MFA and SSO cover your production systems and key SaaS tools
- Access reviews, vulnerability scans and backup restore tests run on a schedule, with evidence
- You can show a risk assessment and a vendor review from the last 12 months
- Incident response is written down and has been tested at least once
- Evidence is collected continuously, not gathered the week before fieldwork

If several of these are missing, you aren't behind. That's what readiness is for.

## Readiness vs "just buying a compliance platform"

Compliance automation platforms help track controls and collect evidence, but they don't decide your scope, write policies that match how you really work, or fix your cloud configuration. Readiness is the thinking and implementation work that makes a platform worth paying for. A hands-on consultant can also help you pick tooling that fits your budget rather than the most expensive bundle.

## FAQ

### Is a SOC 2 readiness assessment required?

No. It's optional, but skipping it is the most common reason first audits run late or come back with exceptions.

### Can the same firm do the readiness assessment and the audit?

Independence rules generally prevent the CPA firm that audits you from also designing and implementing your controls. Many companies use a consultant for readiness and an independent CPA firm for the audit.

### Do AI startups need anything extra for SOC 2 readiness?

SOC 2 has no AI-specific criteria, but auditors and customers increasingly ask about LLM vendors, customer data in prompts and model changes. Cover them in your risk assessment and vendor reviews. See [our SOC 2 checklist for AI startups](/blog/soc-2-checklist-for-ai-startups/).

Next, see the [SOC 2 audit process](/blog/soc-2-audit-process/) and whether you need a [SOC 2 consultant vs a compliance platform](/blog/soc-2-consultant-vs-compliance-platform/). See how we run readiness on our [SOC 2 compliance page](/soc-2-compliance/), or [book a free scoping call](/contact/).
