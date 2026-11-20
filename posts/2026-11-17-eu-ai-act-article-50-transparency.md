---
title: EU AI Act Article 50: Transparency for AI Features
description: What EU AI Act Article 50 requires for chatbots, AI-generated content, emotion recognition and deepfakes — who it applies to, dates, fines and steps.
date: 2026-11-17
tags: EU AI Act, AI governance, transparency
updated: 2026-11-19
keyword: eu ai act article 50
takeaways: Article 50 of the EU AI Act requires that people know when they are dealing with AI.|It has applied since 2 August 2026 to chatbots and AI assistants, AI-generated content, emotion recognition, biometric categorisation and deepfakes.|Unlike the high-risk rules, which were delayed to December 2027, Article 50 applies now to everyday AI features.|Breaches can be fined up to €15 million or 3% of worldwide annual turnover.
---

**Article 50 of the EU AI Act requires that people know when they are dealing with AI.** Since 2 August 2026 it has applied to chatbots and AI assistants, AI-generated content, emotion recognition and biometric categorisation, and deepfakes. Unlike the high-risk rules — delayed to December 2027 — Article 50 applies **now**, to everyday AI features, and breaches can be fined up to €15 million or 3% of worldwide annual turnover.

## The four transparency obligations

| Situation | Who must act | What's required |
|---|---|---|
| **People interact with an AI system** (chatbots, assistants, agents) | Provider | Design the system so people are told they're interacting with AI, unless obvious from context |
| **AI generates synthetic audio, image, video or text** | Provider | Mark outputs in a machine-readable format so they're detectable as AI-generated |
| **Emotion recognition or biometric categorisation** | Deployer | Inform the people exposed to it |
| **Deepfakes, or AI-generated text published to inform the public on matters of public interest** | Deployer | Disclose that the content is AI-generated or manipulated |

There is one transitional exception: generative AI systems already on the market before 2 August 2026 had until **2 December 2026** to meet the content-marking requirement.

## Does it apply to your SaaS product?

If EU users interact with your AI features, or AI-generated output from your product reaches people in the EU, assume yes. Article 50 isn't limited to high-risk systems — it covers ordinary features such as:

- an in-app AI assistant or support chatbot
- AI-drafted emails, documents or marketing copy
- AI-generated images or avatars
- voice agents

See [EU AI Act for US SaaS companies](/blog/eu-ai-act-for-us-saas-companies/) for scope and roles.

## Practical steps

1. **Inventory** every AI feature that interacts with people or generates content.
2. **Assign roles** — provider or deployer — for each.
3. **Add AI-interaction notices** at the start of chat and voice experiences ("You're chatting with an AI assistant"). Make them clear, not buried in terms.
4. **Mark generated content** — use machine-readable marking (metadata or watermarking) for generated media; check what your model provider supports.
5. **Label deepfakes and public-interest AI text** where you publish them.
6. **Inform people** before any emotion recognition or biometric categorisation.
7. **Document and evidence it** — screenshots, design decisions, test records. Regulators expect transparency to be built in before release, not added afterwards.
8. **Contract for it** — confirm your AI vendors support the marking and disclosure you need.

## Good AI disclosure looks like

- Shown **before or at the start** of the interaction
- In plain language, in the user's language
- Visible on every channel (web, mobile, voice)
- With a path to a human where it matters

## How it fits your wider program

Article 50 controls slot into an AI governance program alongside your AI inventory, policy and risk assessments — and into SOC 2 through change management (disclosures don't get removed in a redesign) and product documentation. See [AI governance for SaaS startups](/blog/ai-governance-for-saas-startups/).

## FAQ

### Is a line in our terms of service enough?

Generally no. The intent is that people are informed at the point of interaction, in a clear and distinguishable way.

### Does an AI disclosure hurt conversion?

Clear disclosure, done well, builds trust. Keep it short and friendly and offer a human route.

### Is this legal advice?

No. It's a practical overview; confirm your obligations with EU legal counsel. We help build the inventory, controls and evidence.

See our [AI governance service](/ai-governance/) and [the EU AI Act for US SaaS companies](/blog/eu-ai-act-for-us-saas-companies/). Need an Article 50 readiness check? [Book a free scoping call](/contact/).
