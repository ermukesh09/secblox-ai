---
title: SOC 2 Audit Process: What Happens, Step by Step
description: The SOC 2 audit process step by step: scoping, readiness, the observation window, fieldwork, exceptions and the final report, and how to prepare.
date: 2026-11-20
updated: 2026-11-20
tags: SOC 2, audit, startups
keyword: soc 2 audit process
takeaways: The SOC 2 audit process runs from scoping and readiness through an observation window (Type II), auditor fieldwork, a draft report and the final report.|A Type I tests control design at one date; a Type II tests whether controls operated over a period, usually 3–12 months.|During fieldwork the auditor uses inquiry, observation, inspection and sampling, so evidence must exist for the whole period.|The final report contains the auditor's opinion, management's assertion, the system description and the tested controls with any exceptions.
draft: false
---

**The SOC 2 audit process has six stages: choose an auditor and agree scope, get ready, run the observation window (for Type II), go through fieldwork, review the draft report, and receive the final report.** Only a licensed CPA firm can perform the audit, but most of the work — and most of the risk — sits with your team before the auditor arrives. Knowing what happens at each stage is the easiest way to avoid delays and exceptions.

## What are the stages of a SOC 2 audit?

| Stage | What happens | Typical owner |
|---|---|---|
| 1. Scoping and engagement | Agree criteria, systems, report type and dates; sign the engagement letter | Leadership + auditor |
| 2. Readiness | Find and fix gaps; write policies; set up evidence collection | Your team (often with a consultant) |
| 3. Observation window (Type II) | Controls operate and generate evidence for 3–12 months | Your team |
| 4. Fieldwork | Auditor tests controls through walkthroughs and samples | Auditor + your control owners |
| 5. Draft report | You review findings, the system description and any exceptions | Management + auditor |
| 6. Final report | The auditor issues the signed report you share with customers | Auditor |

## Stage 1: How is the audit scoped?

You and the audit firm agree which Trust Services Criteria are in scope (most startups start with Security only), which systems and locations are included, whether it's a Type I or Type II, and the period being tested. Scope drives both cost and effort, so decide it deliberately. See [which criteria you need](/blog/soc-2-trust-services-criteria/) and [Type I vs Type II](/blog/soc-2-type-1-vs-type-2/).

## Stage 2: What happens during readiness?

Readiness is where controls get designed and implemented: access management, change management, logging, backups, vendor reviews, incident response and policies. It isn't formally part of the audit, but skipping it is the most common reason first audits slip or end with exceptions. Start with a [SOC 2 readiness assessment](/blog/soc-2-readiness-assessment/).

## Stage 3: What is the observation window?

For a Type II, the auditor tests whether controls operated consistently over a defined period, usually 3–12 months. Every recurring control — quarterly access reviews, vulnerability scans, backup restore tests, onboarding and offboarding — must produce evidence across the whole window. A Type I has no window; it tests design at a single date.

## Stage 4: What happens during fieldwork?

The auditor tests your controls using four methods:

- **Inquiry** — interviewing control owners about how things work
- **Observation** — watching a process happen, such as a deployment or access change
- **Inspection** — reviewing documents, configurations, tickets and logs
- **Sampling** — selecting items from the period (for example new hires or production changes) and checking each one followed the control

Expect a request list of evidence items and several walkthrough calls. Fast, organised responses shorten fieldwork considerably.

## Stage 5: How are exceptions handled?

If a sampled item didn't follow the control — say, a leaver whose access was removed late — the auditor records an exception. Exceptions don't automatically mean a failed report; the auditor considers how significant they are. Management can add a written response explaining the cause and the fix, which appears in the report. Isolated exceptions are common; widespread ones can lead to a qualified opinion.

## Stage 6: What is in the final SOC 2 report?

A SOC 2 report typically contains:

1. **The auditor's opinion** on whether controls were suitably designed (and, for Type II, operated effectively)
2. **Management's assertion** about the system and controls
3. **The system description** — your services, infrastructure, people, processes and data
4. **Controls, tests and results**, including any exceptions
5. **Other information** (optional), such as management responses

Most customers read the opinion first, then the exceptions.

## How long does the SOC 2 audit process take?

Readiness typically takes 6–10 weeks for a SaaS startup. A Type II then needs its observation window plus a few weeks for fieldwork and reporting. See [how long SOC 2 takes](/blog/how-long-does-soc-2-take/) and [what it costs](/blog/soc-2-cost-for-startups/).

## In practice

The part of the audit process teams most often underestimate is the system description. It has to describe your real services, infrastructure, data flows and subservice providers accurately — and auditors test against it. The second is evidence gaps across the window: one missed quarterly access review shows up in sampling months later. Writing the description early and putting recurring controls on a calendar from day one avoids both.

## FAQ

### Who performs a SOC 2 audit?

A licensed CPA firm. Consultants and compliance platforms can help you prepare, but only an independent CPA firm can examine your controls and issue the report.

### Can you fail a SOC 2 audit?

There's no pass/fail grade. The auditor issues an opinion: unqualified (clean), qualified, adverse, or a disclaimer. Exceptions are listed in the report and can affect the opinion if they're significant.

### What is a bridge letter?

A letter from management covering the gap between the end of your last SOC 2 period and today, so customers have assurance until the next report is issued.

### Does the auditor need access to our systems?

Usually auditors review screenshots, exports, tickets and walkthroughs rather than taking direct access. Some may ask for read-only access or observe live during a call.

Related: [how to choose a SOC 2 auditor](/blog/how-to-choose-a-soc-2-auditor/). See our [SOC 2 compliance and audit readiness service](/soc-2-compliance/) or [book a free scoping call](/contact/).
