---
title: Does SOC 2 Cover AI and LLM Vendors?
description: How SOC 2 treats model providers like OpenAI or Anthropic: subservice organizations, carve-out vs inclusive, vendor reviews and what auditors ask.
date: 2026-11-17
tags: SOC 2, AI vendors, LLM
updated: 2026-11-19
takeaways: Yes — if your product sends customer data to an AI or LLM provider, that provider is part of your SOC 2 scope.|SOC 2 has no AI-specific criteria, but the Trust Services Criteria apply to every component that processes customer data.|Most reports treat the model provider as a subservice organization using the carve-out method.|You must show how you selected, reviewed and monitor the provider, and describe it in your system description.
---

**Yes — if your product sends customer data to an AI or LLM provider, that provider sits inside your SOC 2 story.** SOC 2 has no AI-specific criteria, but the Trust Services Criteria apply to every component that processes customer data. In most reports the model provider is treated as a **subservice organization** using the **carve-out method**, and you must show how you selected, reviewed and monitor it.

## Is an LLM provider a vendor or a subservice organization?

It depends on what it does for your system:

- **Subservice organization** — it performs part of the service you deliver to customers and its controls matter to your commitments. A model API that processes customer prompts and returns results inside your product usually fits here.
- **Vendor** — it supports your business but isn't part of the system you describe, such as an AI writing assistant your marketing team uses.

When in doubt, ask: *if this provider failed or leaked data, would my customers' data or service be affected?* If yes, treat it as a subservice organization.

## Carve-out vs inclusive method

| Method | What it means | When it's used |
|---|---|---|
| **Carve-out** | Your report describes the provider's role but excludes its controls; you rely on its own assurance (e.g. its SOC 2 report) | Almost always for large model providers |
| **Inclusive** | The provider's controls are tested as part of your audit | Rare — requires the provider's cooperation |

With carve-out, your system description lists **complementary subservice organization controls (CSOCs)** — the controls you expect the provider to operate — and you must show you monitor them.

## What auditors and customers ask about AI providers

1. Which AI providers process customer data, and for what?
2. Have you reviewed their security reports (SOC 2, ISO 27001) and noted any exceptions?
3. Do their terms allow them to **train on your customers' data**? Is that switched off?
4. How long do they **retain** prompts and outputs? Can retention be reduced to zero?
5. Where is data processed (region / residency)?
6. Who in your company can access model consoles and API keys?
7. How are prompt and model changes reviewed before release?
8. How would you detect and respond to an AI-related incident?

## Controls to have in place

- **Vendor inventory** listing every AI provider, its data access and risk rating
- **Annual review** of each provider's security report, with follow-up on exceptions
- **Contract terms**: no training on customer data, limited retention, breach notification, sub-processor disclosure
- **Access control**: SSO/MFA on provider consoles, keys in a secrets manager, rotation, least privilege
- **Change management** for prompts, system instructions and model versions
- **Data minimisation**: send only what the feature needs; strip or mask sensitive fields
- **Monitoring**: usage, errors and anomalous volumes on AI API keys

## Don't forget the system description

Your SOC 2 system description should name AI providers as subservice organizations, explain what data flows to them, and state which controls you rely on them for. Buyers read this section closely — a clear description of AI data flows builds trust. See [SOC 2 for AI companies](/soc-2-for-ai-companies/).

## FAQ

### Do we need our model provider's SOC 2 report?

You need some independent assurance over their controls — usually their SOC 2 Type II report or ISO 27001 certificate. Review it, record the review and track any exceptions.

### What if an AI tool has no SOC 2 report?

Assess the risk. For low-risk internal use, a security questionnaire and contract review may be enough. For tools processing customer data, lack of assurance is a real risk — consider alternatives or compensating controls.

### Do internal AI tools need to be in our SOC 2 scope?

Only if they process in-scope data or support the system. Cover them with your AI acceptable use policy and vendor process either way. See our [AI acceptable use policy guide](/blog/ai-acceptable-use-policy/).

Use our [AI vendor risk assessment questions](/blog/ai-vendor-risk-assessment-questions/) for the review itself. Need help scoping AI vendors for your SOC 2? [Book a free scoping call](/contact/).
