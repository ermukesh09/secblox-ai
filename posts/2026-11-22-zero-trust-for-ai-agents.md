---
title: Zero Trust for AI Agents: 6 Controls That Matter
description: Zero trust for AI agents: how to apply identity, least privilege, tool security, isolation, memory security and monitoring to agentic AI, mapped to SOC 2.
date: 2026-11-22
updated: 2026-11-22
tags: AI security, agentic AI, zero trust, AI governance
keyword: zero trust for ai agents
takeaways: Zero trust for AI agents means no agent is trusted by default: every action is tied to a known agent identity, scoped to the task, checked and logged.|AI agents interpret instructions, call tools, keep context and act with little human input, so they need controls designed for autonomy rather than for ordinary applications or users.|Six controls cover most of the risk: agent identity, least privilege, tool security, isolation, memory security and continuous monitoring, plus a tested way to stop an agent.|These principles apply to any agent stack — Claude, GPT, Gemini, open-source models or custom frameworks — and map directly to SOC 2, ISO 42001 and the NIST AI RMF.
draft: false
---

**Zero trust for AI agents means treating every agent as untrusted by default: each action is tied to a known agent identity, limited to the permissions the task needs, checked at every tool and data boundary, and logged so it can be reviewed or stopped.** AI agents can interpret instructions, access data, invoke tools, retain context and act with very little human intervention. That's a different risk profile from a normal application or a human user, and it needs zero trust applied as an architectural principle, not a checkbox.

## Why do AI agents need a zero trust approach?

Zero trust started as a network idea: stop trusting anything because of where it sits, and verify every request instead. NIST SP 800-207 describes it as an architecture built around identity, least privilege and continuous verification rather than a trusted internal network.

AI agents stretch that model in three ways:

- **They decide what to do next.** An ordinary application follows code paths you wrote. An agent chooses which tool to call and with what inputs, based on instructions and content it reads at run time.
- **They act on someone's behalf.** An agent might draft an email, change a ticket, query a database or run code, using credentials that belong to a person or a service.
- **They read untrusted content.** Web pages, documents, emails and tool outputs can all carry instructions. Prompt injection means a single poisoned input can redirect an agent that has real permissions.

Anthropic has published a guide, [Zero Trust for AI Agents](https://claude.com/resources/guides/zero-trust-for-ai-agents), that frames this as a security framework for deploying autonomous agents in the enterprise, covering identity, access control and monitoring, with a phased implementation workflow. The principles below are our practical reading of what matters most for SaaS and AI companies, whichever model or framework they build on.

## What are the six zero trust controls for AI agents?

| Control | The question it answers | What good looks like |
|---|---|---|
| 1. Agent identity | Which agent is acting, on whose behalf, under what authority? | A unique identity per agent, linked to the user or service it acts for |
| 2. Least privilege | What is this agent allowed to do for this task? | Narrow, task-scoped, short-lived permissions — nothing broad by default |
| 3. Tool security | Which tools and APIs can it reach, and are they safe? | An approved tool list, validated inputs and outputs, and each integration treated as part of the trust boundary |
| 4. Isolation | How far can a mistake or attack spread? | Sandboxed execution, separate environments and limits on network and data reach |
| 5. Memory security | What does the agent remember, and can that be poisoned? | Scoped, reviewable memory with retention limits and no secrets stored in context |
| 6. Continuous monitoring | Can we see what it did, and stop it quickly? | Logs of prompts, decisions, tool calls and data access, alerts, and a tested kill switch |

## 1. How do you give an AI agent an identity?

An agent should never act under a shared service account or a borrowed human session with full rights. Give each agent its own identity — a workload identity, service principal or IAM role — and record whose request it's serving.

That gives you three things you can't get otherwise: accountability (which agent did this?), delegation limits (it can only do what the requesting user could do, and often less) and revocation (you can disable one agent without touching anything else). Where agents call other agents, pass the original requester's identity along the chain rather than letting each hop escalate.

## 2. How do you apply least privilege to agents?

Scope permissions to the task, not to everything the agent might ever need. In practice:

- **Separate read from write.** Most agents need to read far more than they need to change.
- **Use short-lived credentials** issued for a session or task, not long-lived API keys in configuration.
- **Gate high-impact actions** — payments, deletions, sending external messages, production changes — behind human approval.
- **Set limits** on volume, cost and rate, so a looping or hijacked agent can't do unlimited damage.

The OWASP Top 10 for LLM Applications calls the failure mode here excessive agency: giving a model more functionality, permissions or autonomy than its job requires. Least privilege is the direct fix.

## 3. How do you secure the tools an agent uses?

Every tool, API, plugin and connected system an agent can call is part of its trust boundary. If the agent can reach it, an attacker who controls the agent's input may be able to reach it too.

Keep an approved list of tools for each agent and review new ones like any other third-party integration. Validate what goes into a tool and what comes back, because tool output is untrusted content that may contain instructions. Prefer narrow tools ("look up this customer's plan") over general ones ("run any SQL"). And give each tool its own credentials, so one compromised integration doesn't expose the rest. Our guide to [prompt injection controls for SOC 2](/blog/prompt-injection-controls-soc-2/) covers the input side in more detail.

## 4. How do you isolate AI agents?

Isolation limits the blast radius when an agent does something unintended — or something malicious after reading a poisoned input. Run code-executing agents in sandboxes without access to production credentials. Keep development, testing and production agents in separate environments and accounts. Restrict outbound network access to the destinations the task needs, which also blocks the simplest data exfiltration routes.

The same cloud patterns apply as for any workload: separate accounts, private networking and guardrail policies. See our [cloud security architecture guide](/blog/cloud-security-architecture/) for the AWS version.

## 5. Why is agent memory a security risk?

Persistent context lets agents carry knowledge between sessions, which is useful — and risky. Memory can be poisoned: a malicious instruction saved once may influence every later session. It can also retain data longer than your policies allow, or leak one user's information into another user's session.

Treat agent memory as a data store with owners and rules. Scope it per user or tenant, set retention limits, keep secrets and credentials out of it entirely, and make it reviewable so suspicious entries can be found and removed. If you're subject to GDPR or customer contracts, memory belongs in your data map and deletion process.

## 6. What should you monitor, and how do you stop an agent?

You can't trust what you can't see. Log the prompt or task, the agent's decisions, every tool call with its inputs and outputs, data accessed and actions taken — tied to the agent identity and the requesting user. Alert on unusual patterns: a sudden spike in tool calls, access to data outside the normal scope, or repeated failed actions.

Then make sure you can act fast. Every agent deployment needs a tested way to revoke its credentials, pause its execution and roll back what it changed. The real question for most organisations isn't whether they can deploy agents, but how quickly they can cut an agent's privileges when something goes wrong.

## How does zero trust for AI agents map to SOC 2 and ISO 42001?

These controls aren't extra work on top of compliance — they're how compliance applies to agents:

- **SOC 2 logical access (CC6)** — agent identities, least privilege and access reviews that include agents, not just people.
- **SOC 2 monitoring (CC7)** — agent activity logs, alerting and incident response for agent misuse.
- **SOC 2 change management (CC8)** — review and approval of new tools, prompts and agent capabilities.
- **ISO/IEC 42001** — AI risk assessment, defined responsibilities and operational controls for AI systems.
- **NIST AI RMF** — the Govern, Map, Measure and Manage functions give a structure for agent risk decisions.

For the governance side, see [AI governance for SaaS startups](/blog/ai-governance-for-saas-startups/) and how to handle unapproved agent use in [shadow AI governance](/blog/shadow-ai-governance/).

## In practice

When we review agent deployments, the most common gap is identity: agents running under one broad service account or an engineer's own credentials, which makes least privilege and an audit trail almost impossible. The second is tool sprawl — integrations added during a proof of concept and never reviewed. Fixing those two usually means giving each agent its own scoped identity, cutting its tool list down to what the task needs, and logging every tool call. It's a design decision best made before agents reach production, not after the first incident.

## FAQ

### What is zero trust for AI agents?

It's applying zero trust principles — verify explicitly, use least privilege and assume breach — to autonomous AI agents. Every agent has its own identity, gets only the permissions its task needs, is checked at each tool and data boundary, and is monitored so its actions can be reviewed or stopped.

### Does this only apply to Claude-based agents?

No. The principles apply to agents built on any model or framework, including Claude, GPT, Gemini, open-source models and custom agent frameworks. The controls sit around the agent — identity, permissions, tools, isolation, memory and monitoring — not inside the model.

### Should AI agents need human approval for actions?

For high-impact actions, yes: payments, deleting data, sending messages outside the company and changing production systems. Low-risk, reversible actions can run automatically within tight limits. Decide the threshold per agent and write it down.

### How do we test whether our agent controls work?

Include agents in your penetration testing and red-team exercises: try prompt injection through every input the agent reads, attempt privilege escalation through its tools, and confirm your kill switch actually revokes access. See our [penetration testing service](/services/penetration-testing/).

Related: [AI governance services](/ai-governance/) and [prompt injection controls for SOC 2](/blog/prompt-injection-controls-soc-2/). Want a review of your agent architecture? [Book a free scoping call](/contact/).
