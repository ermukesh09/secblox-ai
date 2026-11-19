---
title: ISO 42001 vs NIST AI RMF: Which First?
description: ISO 42001 vs NIST AI RMF: certifiable standard vs voluntary framework, what each requires, where they overlap and which an AI startup should start with.
date: 2026-11-19
tags: ISO 42001, NIST AI RMF, AI governance
---

**ISO/IEC 42001 is a certifiable management system standard for AI; the NIST AI Risk Management Framework is a free, voluntary framework for managing AI risk.** NIST AI RMF tells you how to think about AI risk. ISO 42001 gives you a system an external auditor can certify. Most AI startups get the best result by using NIST AI RMF to build the risk practice, then formalising it into ISO 42001 when customers start asking for proof.

## The difference in one table

| | ISO/IEC 42001 | NIST AI RMF 1.0 |
|---|---|---|
| Type | International management system standard | Voluntary framework from the US NIST |
| Published | December 2023 | January 2023 |
| Certification | Yes, by an accredited certification body | No certification exists |
| Cost to access | Paid standard | Free |
| Structure | Management system clauses plus Annex A controls | Four functions: Govern, Map, Measure, Manage |
| Best for | Proving AI governance to customers and regulators | Building a practical AI risk process |
| Typical buyer signal | "Are you ISO 42001 certified?" | "How do you manage AI risk?" |

## What ISO 42001 requires

ISO 42001 follows the same management system structure as ISO 27001, so it will look familiar if you already have that. You define the scope of your AI management system, set an AI policy and objectives, run AI risk assessments and AI system impact assessments, choose controls from Annex A, and keep the system running with internal audits and management reviews. A certification body then audits you, and certificates are maintained with surveillance audits.

## What NIST AI RMF asks for

NIST AI RMF is organised into four functions:

- **Govern** — policies, accountability and a culture of AI risk management
- **Map** — understand the context, purpose and impact of each AI system
- **Measure** — assess and track risks such as bias, robustness, privacy and security
- **Manage** — prioritise and act on risks, and monitor them over time

NIST also publishes a Generative AI Profile that applies the framework to risks specific to LLMs and generative systems. For a deeper walkthrough, see [NIST AI RMF explained](/blog/nist-ai-rmf-explained/).

## Where they overlap

The two map closely. An AI inventory, risk assessments, impact assessments, defined roles, vendor and model oversight, and monitoring appear in both. Work done for NIST AI RMF is rarely wasted when you move to ISO 42001; you mainly add the management system layer (documented scope, objectives, internal audit, management review) and the evidence a certification body needs.

## Which should an AI startup start with?

**Start with NIST AI RMF if:**

- No customer has asked for an AI certification yet
- You need a working AI risk process quickly and cheaply
- You sell mainly to US customers who want to see "how you manage AI risk"

**Go straight to ISO 42001 if:**

- Enterprise or regulated customers are asking for a certificate in security reviews
- You sell into the EU or UK and want a recognised standard behind your AI governance
- You already run ISO 27001 and can extend the same management system

**Pair either with SOC 2.** SOC 2 remains the baseline security report US buyers expect. AI governance sits on top of it rather than replacing it. See [SOC 2 vs ISO 42001](/blog/soc-2-vs-iso-42001/).

## A practical path

1. Build an AI system inventory, including third-party models and AI features in your SaaS tools
2. Run a NIST AI RMF–style risk assessment on each system
3. Write an AI policy and an [AI acceptable use policy](/blog/ai-acceptable-use-policy/)
4. Put vendor and model oversight in place for LLM providers
5. When a customer or market requires it, formalise everything into an ISO 42001 management system and book certification

## FAQ

### Is NIST AI RMF mandatory?

No. It's voluntary, though some customers and public-sector buyers use it as their reference for AI risk management.

### Can you be "NIST AI RMF certified"?

No. There is no official certification. Be cautious of anyone selling one. You can, however, be assessed against it and show the results to customers.

### Does ISO 42001 help with the EU AI Act?

It helps you build the governance, risk management and documentation the Act expects, but certification does not by itself make you compliant. See [the EU AI Act for US SaaS companies](/blog/eu-ai-act-for-us-saas-companies/).

See our [AI governance](/ai-governance/) and [ISO 42001](/iso-42001/) services, or [book a free scoping call](/contact/).
