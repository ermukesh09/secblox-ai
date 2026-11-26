---
title: AI Vendor Risk Assessment: 25 Questions to Ask
description: 25 practical questions for assessing AI vendors and model providers: data use, training, retention, security, model behaviour, compliance and exit.
date: 2026-11-17
tags: AI governance, vendor risk, SOC 2
updated: 2026-11-26
keyword: ai vendor risk assessment questions
takeaways: Standard security questionnaires miss most AI-specific risks.|Ask AI vendors how they use your data, whether they train on it, how they protect it, how their models behave and what happens in an incident.|Use the 25 questions for model providers, AI features inside SaaS tools and AI startups you buy from.|Red flags include training on customer data by default with no contractual opt-out, and vague answers on retention or sub-processors.
---

**Before you let an AI vendor touch your data, ask how it uses that data, how it protects it, how its models behave, and what happens when something goes wrong.** Standard security questionnaires miss most AI-specific risks. These 25 questions fill the gap — use them for model providers, AI features inside SaaS tools, and AI startups you buy from.

## Data use and training

1. Is our data — prompts, files, outputs — used to train or improve your models? Can that be turned off contractually?
2. How long are prompts and outputs retained, and can retention be reduced or set to zero?
3. Who at your company can access our data, and under what circumstances (e.g. abuse monitoring)?
4. Where is our data processed and stored? Can we choose the region?
5. Which sub-processors, including other model providers, receive our data?

## Security

6. What independent assurance do you have (SOC 2 Type II, ISO 27001, ISO 42001)? Can we see the report?
7. How is our data isolated from other customers' data — including in caches, embeddings and retrieval indexes?
8. Do you support SSO, MFA and role-based access for your console?
9. How are API keys issued, scoped, rotated and revoked?
10. Is data encrypted in transit and at rest? Who manages the keys?
11. Do you run security testing on AI-specific threats such as prompt injection, data exfiltration and jailbreaks?

## Model behaviour and quality

12. Which underlying models do you use, and how will we be told when they change?
13. How do you evaluate accuracy, safety and bias before releasing model changes?
14. What controls limit harmful, misleading or off-policy outputs?
15. Can we configure guardrails, content filters or system instructions?
16. If your product takes actions (an AI agent), what permissions does it need and can high-impact actions require human approval?

## Transparency and compliance

17. Do you document intended use, limitations and known risks for your AI features?
18. How do you support customer obligations under the EU AI Act (e.g. transparency, marking AI-generated content)?
19. Do you have an AI governance program or policy? Who owns it?
20. How do you handle data subject requests that involve AI-processed data?

## Incidents and continuity

21. How will you notify us of security incidents or AI-related incidents (e.g. data exposure via model output), and how fast?
22. What logs can we access to investigate misuse or incidents?
23. What are your uptime commitments and fallback options if the model service is unavailable?

## Contract and exit

24. What contractual commitments back your answers (DPA, no-training clause, retention, liability)?
25. If we leave, how is our data — including fine-tuned models, embeddings and logs — returned or deleted, and can you confirm it?

## How to use the answers

Rate each vendor by **data sensitivity × criticality**. A meeting-notes tool with internal data needs a light review; a model API processing customer data inside your product needs the full set, contract terms and annual re-review. Record results in your vendor risk register — the same one you use for SOC 2 — so auditors see a single process. See [Does SOC 2 cover AI vendors?](/blog/does-soc-2-cover-ai-llm-vendors/).

## Red flags

- Training on customer data by default with no contractual opt-out
- No independent security assurance and no willingness to share details
- No notice of model changes
- Vague answers on retention or sub-processors
- Agents that need broad, standing access with no approval step

## FAQ

### Should we send all 25 questions to every vendor?

No. Tier your vendors. Use the full list for high-risk vendors and a short subset (data use, retention, assurance, incidents) for low-risk tools.

### How often should AI vendors be reassessed?

At least annually, and whenever the vendor changes models, terms or sub-processors, or you expand what data you send.

### Do AI vendors need to be in our SOC 2 scope?

If they process customer data or support your product, yes. See [does SOC 2 cover AI and LLM vendors](/blog/does-soc-2-cover-ai-llm-vendors/).

Related: [shadow AI governance](/blog/shadow-ai-governance/), the [AI risk assessment template](/blog/ai-risk-assessment-template/) and what an [AI security assessment](/blog/ai-security-assessment/) covers. Want an AI vendor risk process that fits your SOC 2 program? [Book a free scoping call](/contact/) or see our [AI governance service](/ai-governance/).
