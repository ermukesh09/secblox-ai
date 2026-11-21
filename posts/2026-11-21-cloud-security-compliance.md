---
title: Cloud Security Compliance for SaaS Companies
description: Cloud security compliance for SaaS companies: how AWS, Azure and GCP controls map to SOC 2, ISO 27001 and GDPR, what you own, and how to keep evidence current.
date: 2026-11-21
updated: 2026-11-21
tags: cloud security, compliance, SOC 2, GDPR
keyword: cloud security compliance
takeaways: Cloud security compliance means proving that your cloud environment meets the security requirements of frameworks such as SOC 2, ISO 27001 and GDPR, not just configuring it well.|Under the shared responsibility model, your cloud provider's certifications cover their infrastructure, but not how you configure accounts, identities and data.|Most SOC 2 security controls for a cloud-native SaaS company are implemented in the cloud console: access, logging, encryption, change management and backups.|One well-designed set of cloud controls can satisfy SOC 2, ISO 27001 and GDPR security requirements at the same time if you map them once.
draft: false
---

**Cloud security compliance is the work of configuring your cloud environment to meet a framework's security requirements — SOC 2, ISO 27001, GDPR and others — and being able to prove it with evidence.** For a SaaS company, most of those requirements are implemented in AWS, Azure or Google Cloud, so your cloud setup and your compliance programme are largely the same project. Map your cloud controls once, and the same controls can support several frameworks.

## What is cloud security compliance?

Cloud security is about reducing risk: closing exposed services, limiting access and detecting attacks. Cloud compliance is about demonstrating that specific requirements are met, to an auditor, a regulator or a customer's security team. The two overlap heavily, but they're not identical. A well-secured environment with no documentation, no review records and no evidence will still struggle in an audit. A compliant-looking environment with policies on paper but loose real-world configuration will fail a serious security review.

Good cloud security compliance joins the two: controls that genuinely work, plus a reliable trail showing they've worked over time.

## Who is responsible for what in the cloud?

The shared responsibility model is the starting point for every cloud compliance conversation. Your provider is responsible for security *of* the cloud — data centres, hardware, the hypervisor and the core network. You're responsible for security *in* the cloud — identities, configurations, network rules, encryption choices, your applications and your data.

This matters for compliance because of a common misunderstanding: "AWS is SOC 2 compliant, so we are too." Your provider's SOC 2 report and ISO certificates cover only their side. Your auditor will treat the provider as a subservice organisation, review its report, and then test your controls for everything you're responsible for. How much falls on you depends on the services you use: with virtual machines you own the operating system and patching; with managed databases and serverless functions, more shifts to the provider.

## Which frameworks apply to SaaS cloud environments?

| Framework | Who asks for it | What it expects in the cloud |
|---|---|---|
| SOC 2 | US enterprise customers | Access control, monitoring, change management, encryption, backups and incident response, tested over a period |
| ISO 27001 | UK, EU and global customers | An information security management system, with Annex A controls including information security for the use of cloud services |
| GDPR | Anyone processing EU personal data | Appropriate technical and organisational security measures (Article 32), processor agreements and controls on international transfers |
| CSA Cloud Controls Matrix | Cloud-focused security reviews | A cloud-specific control framework with mappings to ISO 27001, SOC 2 criteria and other standards |
| HIPAA, PCI DSS | Health data, card data | Sector-specific safeguards that build on the same cloud foundations |

Most early-stage SaaS companies start with SOC 2 for US customers, add ISO 27001 as they sell internationally, and handle GDPR alongside both. Our comparison of [SOC 2 vs ISO 27001](/blog/soc-2-vs-iso-27001/) explains how to sequence the first two.

## How do cloud controls map to SOC 2?

SOC 2 is built on the AICPA Trust Services Criteria. For a cloud-native company, most of the common criteria are met — or missed — in your cloud accounts:

| SOC 2 area | Cloud controls that satisfy it | Evidence an auditor will ask for |
|---|---|---|
| Logical access (CC6) | SSO through the provider's identity service, MFA for everyone, least-privilege roles, no long-lived keys for people | User and role lists, MFA status, access review records |
| Monitoring (CC7) | Audit logs in every region, protected log storage, threat detection, alert routing | Log configuration, alert samples, incident tickets |
| Change management (CC8) | Infrastructure as code, peer-reviewed pull requests, deployment pipelines, configuration history | Pull request approvals, pipeline logs, configuration timelines |
| Risk mitigation (CC9) | Vendor reviews of your provider and other subprocessors | Provider SOC 2 reports and your review notes |
| Availability (A1) | Automated backups, cross-region copies, tested restores with RTO and RPO | Backup configuration and restore test reports |
| Confidentiality | Encryption at rest with managed keys, TLS in transit, data retention rules | Key policies, encryption settings, retention configuration |

For the full criteria, see our guide to the [SOC 2 Trust Services Criteria](/blog/soc-2-trust-services-criteria/).

## What about GDPR in the cloud?

GDPR doesn't prescribe specific technical controls. Article 32 asks for security appropriate to the risk, naming measures such as encryption, the ability to restore availability after an incident, and regular testing of security measures. In practice, the cloud controls you build for SOC 2 cover most of that.

The cloud-specific GDPR points to get right are:

- **Data location** — know which regions hold personal data, and pin storage and backups to them where customers require it.
- **Processor agreements** — your cloud provider acts as a processor; accept its data processing terms and record it in your subprocessor list.
- **International transfers** — if personal data leaves the EU, document the transfer mechanism you rely on.
- **Deletion and retention** — make sure deletion requests and retention limits also reach backups, logs and replicas.

## How do you keep cloud compliance continuous?

Compliance in the cloud drifts quickly. A new account, a hurried change in production or a test bucket made public can break a control between audits. The answer is automation plus ownership:

1. **Run posture checks continuously** with your provider's native tools — see our guide to [cloud security posture management for startups](/blog/cloud-security-posture-management/).
2. **Enforce guardrails** with organisation-level policies, so the riskiest settings can't be changed at all.
3. **Define infrastructure in code**, so every change is reviewed and recorded.
4. **Collect evidence automatically** — configuration snapshots, access reviews and backup reports on a schedule.
5. **Review monthly**, with a named owner for each control area.

Our guide to [continuous SOC 2 compliance](/blog/continuous-soc-2-compliance/) covers the operating rhythm in more detail.

## In practice

The pattern we see most often in SaaS companies on AWS is that the cloud is better secured than the evidence suggests. Engineers have done sensible things — SSO, encrypted databases, nightly backups — but nobody has recorded access reviews, the backups have never been restored to another region, and logging is on in some accounts but not all. Closing those gaps is usually a few weeks of focused work, not a rebuild. Mapping each cloud control to SOC 2 first, then checking which ISO 27001 and GDPR requirements it already covers, avoids doing the same work three times.

## FAQ

### Is my company compliant if our cloud provider is SOC 2 certified?

No. Your provider's SOC 2 report covers its infrastructure and services. You still need your own controls — and, if customers ask for it, your own SOC 2 report — for how you configure accounts, manage access, protect data and run your application.

### Which cloud provider is best for compliance?

AWS, Azure and Google Cloud all hold the major certifications and offer the native tooling needed for SOC 2, ISO 27001 and GDPR. The deciding factor is usually how well you configure and operate the provider you already use, not which one you picked.

### Can one set of cloud controls cover SOC 2, ISO 27001 and GDPR?

Largely, yes. Access control, logging, encryption, change management and backups support all three. Each framework adds its own extras — ISO 27001 needs a management system, GDPR needs privacy processes — but the technical cloud controls can be built once and mapped to each.

### How long does it take to make a cloud environment audit-ready?

For a typical SaaS startup with a few accounts, closing the technical gaps takes a few weeks; building enough evidence history for a SOC 2 Type 2 audit takes longer, because the observation period usually runs three to twelve months. See [how long SOC 2 takes](/blog/how-long-does-soc-2-take/).

Related: [AWS security assessment checklist](/blog/aws-security-assessment/) and [cloud security architecture for SaaS startups](/blog/cloud-security-architecture/). See our [cloud security assessment and consulting service](/services/cloud-security-assessment/), our [SOC 2 compliance service](/soc-2-compliance/) or [book a free scoping call](/contact/).
