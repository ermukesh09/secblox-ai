---
title: EU AI Act for US SaaS Companies: What Applies Now
description: Does the EU AI Act apply to your US SaaS product? Who is in scope, what already applies, what the Digital Omnibus delayed, and what to do first.
date: 2026-11-17
tags: EU AI Act, AI governance, SaaS
updated: 2026-11-19
takeaways: The EU AI Act can apply to a US SaaS company with no EU office if its AI system or its output is used in the EU.|The heaviest high-risk obligations were delayed to 2 December 2027 by the Digital Omnibus.|Transparency obligations under Article 50 already apply and are enforceable.|Start with an AI inventory, a risk classification of each system and clear AI disclosures in your product.
---

**Short answer:** yes, the EU AI Act can apply to a US SaaS company — even with no EU office. If you place an AI system on the EU market, or the output of your AI system is used in the EU, you are likely in scope. The good news for most SaaS vendors: the heaviest "high-risk" obligations were pushed back to **2 December 2027**, but the **transparency rules already apply** and are enforceable today.

## Does the EU AI Act apply to a US company?

The Act follows the product, not the headquarters. It can apply to you if you are:

- a **provider** — you develop an AI system (or have one developed) and put it on the market under your name, including as a feature inside your SaaS product, and EU customers use it; or
- a **deployer** — you use an AI system in your own operations, and its output is used in the EU (for example, an AI screening tool used on EU job applicants).

Most AI-enabled SaaS companies are **providers** of their AI features and **deployers** of AI tools they use internally. The two roles carry different duties, so the first job is to work out which hat you wear for each system.

## What already applies (and what was delayed)

The Act phases in over several years, and the EU's **Digital Omnibus on AI** — in force since 27 July 2026 — moved some of the dates.

| Date | What applies |
|---|---|
| 2 Feb 2025 | Prohibited AI practices (e.g. manipulative techniques, social scoring) |
| 2 Aug 2025 | Obligations for general-purpose AI (GPAI) model providers |
| **2 Aug 2026** | **Article 50 transparency obligations**, plus penalties and enforcement |
| 2 Dec 2026 | End of the grace period for marking AI-generated content from GenAI systems already on the market before 2 Aug 2026; additional prohibited practices |
| **2 Dec 2027** | **High-risk obligations for stand-alone (Annex III) systems** — previously 2 Aug 2026 |
| 2 Aug 2028 | High-risk obligations for AI embedded in regulated products (Annex I) |

The delay to high-risk rules happened because harmonised technical standards and national authorities were not ready — not because the requirements were softened. Treat 2027 as preparation time, not a reprieve.

## The obligation most SaaS companies face today: transparency

Article 50 applies to everyday AI features, not just high-risk ones. In practice, check whether you:

1. **Let people interact with AI** — chatbots, AI assistants, AI agents. Users must be told they are dealing with an AI system unless it is obvious from context.
2. **Generate synthetic content** — text, images, audio or video. Providers must mark outputs in a machine-readable way so they can be detected as AI-generated.
3. **Use emotion recognition or biometric categorisation** — people exposed to it must be informed.
4. **Publish deepfakes or AI-generated text on matters of public interest** — deployers must disclose it.

Breaches of Article 50 can attract fines of up to €15 million or 3% of worldwide annual turnover, whichever is higher.

## Are you high-risk?

Probably not — but check. High-risk systems are those used in sensitive areas listed in Annex III, such as **employment and HR decisions, education, credit scoring and insurance, access to essential services, biometrics, critical infrastructure and law enforcement**. If your product screens candidates, scores creditworthiness or decides access to services, assume high-risk until proven otherwise and start planning for the 2027 date now: risk management, data governance, technical documentation, logging, human oversight, accuracy and robustness, and a conformity assessment.

## What to do first

1. **Build an AI inventory.** List every AI feature you ship and every AI tool you use internally, with owner, purpose, data used and the model provider behind it.
2. **Assign roles.** For each system, decide whether you are provider, deployer or both.
3. **Classify risk.** Prohibited, high-risk, transparency (Article 50) or minimal.
4. **Fix transparency now.** Add AI-interaction notices to chat and agent interfaces, and make sure generated content is marked.
5. **Review your model providers.** Confirm what they commit to on GPAI obligations, data use and retention.
6. **Document it.** Keep the inventory, classification and decisions somewhere an auditor or customer can follow.
7. **Connect it to your security program.** Access control, change management, logging and vendor risk you already run for SOC 2 cover a lot of the groundwork.

## How this fits with SOC 2 and ISO 42001

SOC 2 proves your security controls work; it does not address AI-specific legal obligations. The EU AI Act is law. **ISO/IEC 42001** is a certifiable management system that gives you a structured way to run AI governance — and evidence that you do. Many companies use 42001 as the operating model and map EU AI Act duties onto it. See our [AI governance service](/ai-governance/) and [ISO 42001 readiness](/iso-42001/).

## FAQ

### We only sell to US customers. Are we in scope?

If no EU customers use your AI features and no AI output from your systems is used in the EU, your exposure is low. Many US SaaS companies discover EU users through existing customers' subsidiaries, so check your customer and user base before concluding.

### Does using an API from a model provider make us a provider?

If you build that model into a product or feature you offer under your own name, you are generally the provider of that **AI system**, even though someone else built the underlying model. The model provider carries the separate GPAI obligations.

### Is this legal advice?

No. This is a practical overview. For your specific obligations, involve EU legal counsel — we help you build the inventory, controls and evidence they will ask for.

Related: [EU AI Act Article 50 transparency](/blog/eu-ai-act-article-50-transparency/) and [ISO 42001 vs NIST AI RMF](/blog/iso-42001-vs-nist-ai-rmf/). See our [AI governance service](/ai-governance/), or want a quick read on where you stand? [Book a free 30-minute scoping call](/contact/).
