---
title: SOC 2 Audit Checklist for AI Startups (2026)
description: A practical SOC 2 checklist for AI startups: scoping LLM vendors, prompt change management, RAG data isolation, policies, evidence and audit preparation.
date: 2026-11-14
tags: SOC 2, AI startups, checklist
updated: 2026-11-19
takeaways: AI startups need the standard SOC 2 foundations plus a short list of AI-specific controls.|Put AI features and model providers inside the SOC 2 system boundary and treat prompts like code: versioned, peer-reviewed and tested.|Isolate tenant data in vector stores and RAG retrieval, and get no-training or limited-retention terms from model providers.|Include LLM attack paths such as prompt injection in your annual penetration test.
---

**An AI startup's SOC 2 checklist is the standard SOC 2 foundation — scope, policies, access, change management, data protection, vendors and operations — plus AI-specific items: model providers in scope, prompts under change control, tenant-isolated RAG data and LLM-focused testing.** This checklist covers both, in the order most startups tackle them.

## 1. Scope

- Define the system boundary, including AI features and model providers
- Choose Trust Services Criteria (Security + only what customers require)
- Decide Type I first or straight to Type II

## 2. Governance & policies

- Information security policy and supporting policies
- AI acceptable use and AI development policy
- Annual risk assessment including AI risks
- Security awareness training for all staff

## 3. Access control

- SSO and MFA everywhere, including model-provider consoles
- Least-privilege access to production, prompts and model configuration
- Quarterly access reviews

## 4. Change management

- Code, infrastructure and **prompts** in version control with peer review
- Evaluation tests before model or prompt changes ship

## 5. Data protection

- Encryption at rest and in transit
- Tenant isolation in vector stores and RAG retrieval
- Contractual no-training / limited-retention terms with model providers

## 6. Vendor risk

- Vendor inventory with risk ratings, including AI providers
- Annual review of vendor SOC 2 reports

## 7. Operations

- Centralized logging, alerting and incident response runbooks (including AI incidents)
- Vulnerability management and annual penetration test including LLM attack paths
- Backups and a tested BCP/DR plan

## 8. Audit readiness

- Compliance automation platform connected to cloud, IdP, HR and code repos
- System description drafted, auditor selected

## FAQ

### Does SOC 2 have AI-specific requirements?

No. The Trust Services Criteria are technology-neutral, but they apply to every component that handles customer data — including LLM providers, vector stores and AI features. See [does SOC 2 cover AI and LLM vendors](/blog/does-soc-2-cover-ai-llm-vendors/).

### Do prompts need change management for SOC 2?

Treat production prompts and model configuration like code: version control, peer review and testing before release. A prompt change can alter system behaviour as much as a code change.

### How long does this checklist take to complete?

Readiness for a typical SaaS startup takes about 6–10 weeks. See [how long SOC 2 takes](/blog/how-long-does-soc-2-take/) for the full timeline.

Once the checklist is done, follow the [SOC 2 audit process](/blog/soc-2-audit-process/) and [choose a SOC 2 auditor](/blog/how-to-choose-a-soc-2-auditor/). Need help working through it? Start with a [SOC 2 readiness assessment](/blog/soc-2-readiness-assessment/), see [SOC 2 for AI companies](/soc-2-for-ai-companies/) or [book a call](/contact/).
