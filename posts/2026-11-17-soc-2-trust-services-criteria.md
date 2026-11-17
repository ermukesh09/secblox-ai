---
title: SOC 2 Trust Services Criteria: Which Do You Need?
description: The five SOC 2 Trust Services Criteria explained — Security, Availability, Confidentiality, Processing Integrity, Privacy — and how to pick your scope.
date: 2026-11-17
tags: SOC 2, scoping
---

**Every SOC 2 report must include Security. The other four Trust Services Criteria — Availability, Confidentiality, Processing Integrity and Privacy — are optional, and you should add them only when customers or contracts ask for them.** Most SaaS startups get a strong first report with Security alone, or Security plus Availability and Confidentiality. Adding criteria nobody requested makes the audit longer and more expensive without winning more deals.

## The five criteria at a glance

| Criteria | What it proves | Required? | Usually added when… |
|---|---|---|---|
| **Security** | Systems are protected against unauthorised access | Always | — |
| **Availability** | Systems are available as committed (uptime, capacity, recovery) | Optional | You offer uptime SLAs or customers depend on you operationally |
| **Confidentiality** | Information designated confidential is protected | Optional | You handle customer IP, contracts, financial or other sensitive business data |
| **Processing Integrity** | Processing is complete, valid, accurate, timely and authorised | Optional | You process transactions, payments, payroll or calculations customers rely on |
| **Privacy** | Personal information is collected, used, retained and disposed of properly | Optional | Personal data handling is central to your service and customers ask about it specifically |

## Security: the Common Criteria

Security is covered by the Common Criteria, CC1 to CC9:

- **CC1** Control environment — governance, ethics, structure, HR
- **CC2** Communication and information
- **CC3** Risk assessment
- **CC4** Monitoring activities
- **CC5** Control activities
- **CC6** Logical and physical access
- **CC7** System operations — detection, monitoring, incident response
- **CC8** Change management
- **CC9** Risk mitigation — business disruption and vendor risk

Most of your SOC 2 effort lives here, whichever optional criteria you add.

## How to choose your scope

Ask three questions:

1. **What have customers actually asked for?** Check security questionnaires, contracts and lost-deal feedback.
2. **What have you promised?** Uptime SLAs point to Availability; confidentiality clauses point to Confidentiality.
3. **What does your product do?** Financial calculations or transactions point to Processing Integrity.

If the answer to all three is "nothing specific", start with **Security only**. You can add criteria in a later report.

## Common scoping mistakes

- **Adding Privacy by default.** It's the most demanding optional criterion. If you mainly need to show GDPR or UK GDPR alignment, that's often better handled separately.
- **Skipping Availability when you sell SLAs.** Buyers notice the gap.
- **Scoping every product.** Scope the product customers are buying; add others later.
- **Forgetting AI components.** If AI features process customer data, they're inside your system boundary whichever criteria you choose. See [Does SOC 2 cover AI vendors?](/blog/does-soc-2-cover-ai-llm-vendors/)

## A typical starting point

| Company type | Typical first scope |
|---|---|
| Early-stage B2B SaaS | Security |
| SaaS with uptime SLAs | Security + Availability |
| SaaS handling sensitive customer data | Security + Availability + Confidentiality |
| Fintech / payments / payroll | Add Processing Integrity |

## FAQ

### Can we add criteria later?

Yes. Many companies start with Security and add Availability or Confidentiality in their second or third report as customer demands grow.

### Does adding criteria change the timeline?

It adds controls to implement and evidence to collect, so expect more preparation work and a larger audit — but it doesn't change the length of the Type II observation window.

### Is Privacy the same as GDPR compliance?

No. The Privacy criterion is based on AICPA principles and overlaps with GDPR, but neither substitutes for the other.

Not sure which criteria to include? [Book a free scoping call](/contact/), read [how long SOC 2 takes](/blog/how-long-does-soc-2-take/), or see our [SOC 2 compliance service](/soc-2-compliance/).
