---
title: SOC 2 Checklist for AI Startups (2026)
description: A practical SOC 2 checklist for AI startups: scoping LLM vendors, prompt change management, RAG data isolation, policies, evidence and audit preparation.
date: 2026-11-14
tags: SOC 2, AI startups, checklist
---

This checklist covers the SOC 2 foundations every SaaS company needs, plus the AI-specific items auditors and buyers now ask about.

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

Need help working through it? [See SOC 2 for AI companies](/soc-2-for-ai-companies/) or [book a call](/contact/).
