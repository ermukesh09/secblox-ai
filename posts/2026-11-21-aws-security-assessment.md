---
title: AWS Security Assessment: Checklist and Process
description: How an AWS security assessment works: what to review, a 10-area checklist, AWS-native tools, pen testing rules and how findings map to SOC 2.
date: 2026-11-21
updated: 2026-11-21
tags: AWS, cloud security, SOC 2
keyword: aws security assessment
takeaways: An AWS security assessment reviews how your AWS accounts are configured, accessed, monitored and recovered, and produces a prioritised list of fixes.|Most findings in startup AWS environments are configuration and access issues — old access keys, over-broad roles, logging gaps and untested backups — not exotic attacks.|AWS-native tools such as Security Hub CSPM, IAM Access Analyzer and the CIS AWS Foundations Benchmark automate much of the baseline; expert review covers the rest.|For SaaS companies, a good AWS security assessment doubles as SOC 2 preparation, because the same controls feed the audit evidence.
draft: false
---

**An AWS security assessment is a structured review of how your AWS environment is configured, accessed, monitored and recovered, ending in a prioritised list of fixes.** It covers identity and access, logging, network exposure, data protection, backups and incident response across every account and region you use. For SaaS companies, it also doubles as preparation for SOC 2, because the same controls become audit evidence.

## What is an AWS security assessment?

An AWS security assessment checks your side of the shared responsibility model: AWS secures the underlying cloud, and you secure how you use it — your accounts, identities, configurations and data. The assessment combines automated checks against established baselines with expert review of things tools can't judge, such as whether a role's permissions actually match what the workload needs.

It's sometimes called an **AWS security audit**. The difference is mostly emphasis: an audit checks against a defined standard and reports compliance, while an assessment also prioritises risk and recommends fixes. A useful engagement does both.

## Why do SaaS companies need one?

- **Enterprise security reviews** ask detailed questions about your cloud controls.
- **SOC 2 and ISO 27001** auditors test the same controls — access, logging, change management, backups.
- **Configuration drift**: environments built quickly by small teams accumulate old keys, broad permissions and public resources.
- **Incidents in AWS** usually start with exposed credentials or misconfiguration rather than sophisticated exploits.

## What does an AWS security assessment checklist cover?

| Area | What gets reviewed |
|---|---|
| 1. Account structure | AWS Organizations, separate production and non-production accounts, guardrails (service control policies) |
| 2. Root and identity | Root user MFA and no root access keys; SSO via IAM Identity Center; MFA for all humans |
| 3. Permissions | Least privilege, unused users, roles and access keys, external access found by IAM Access Analyzer |
| 4. Logging | CloudTrail in all regions with protected storage; AWS Config recording; log retention |
| 5. Threat detection | GuardDuty enabled across accounts and regions; alerts routed to a person who acts on them |
| 6. Network exposure | Security groups open to the internet, public IPs, default VPC use, administrative ports |
| 7. Data protection | Encryption at rest with KMS, TLS in transit, S3 Block Public Access, secrets in Secrets Manager |
| 8. Vulnerabilities | Patching and scanning of instances, containers and functions, for example with Amazon Inspector |
| 9. Backup and recovery | Automated backups, cross-region or cross-account copies, and a tested restore with RTO/RPO evidence |
| 10. Incident response | A written plan, tested runbooks and the access needed to investigate quickly |

## How does the assessment process work?

1. **Scope** — accounts, regions, workloads and the standard you want to measure against.
2. **Read-only access** — a dedicated, read-only, time-limited role for the assessor.
3. **Automated baseline** — run posture checks across all accounts and regions.
4. **Expert review** — IAM policies, architecture, data flows and anything automated checks can't judge.
5. **Optional penetration test** — of your application and exposed infrastructure.
6. **Report** — findings ranked by risk, with clear remediation steps and owners.
7. **Re-test** — confirm the critical and high findings are fixed.

## Which AWS tools help with an assessment?

AWS provides strong native tooling, and it's usually the cheapest place to start:

- **AWS Security Hub CSPM** — cloud security posture management (CSPM) that runs automated best-practice checks; the AWS Foundational Security Best Practices standard is built in, alongside standards such as the CIS AWS Foundations Benchmark.
- **IAM Access Analyzer** — finds resources shared outside your account and unused access.
- **Amazon GuardDuty** — threat detection from logs and network activity.
- **AWS Config** — records configuration changes and evaluates rules.
- **Amazon Inspector** — vulnerability scanning for instances, containers and Lambda functions.

Tools find misconfigurations. They don't decide whether a permission is actually needed, whether your recovery plan would work, or which finding matters most for your business — that's the expert part of the assessment.

## Can you penetration test AWS?

Yes, within limits. Under the AWS penetration testing policy, customers can test their own resources on a list of permitted services without prior approval, but testing AWS's own infrastructure or services is not allowed, and some activities — such as command-and-control simulations or DDoS testing — need separate approval or follow separate policies. A penetration tester should confirm scope against the current policy before starting. See our [penetration testing service](/services/penetration-testing/).

## How does an AWS security assessment help with SOC 2?

Most SOC 2 security criteria for a cloud-native company are implemented in AWS: logical access, change management, monitoring, encryption, backups and incident response. Fixing assessment findings closes the same gaps an auditor would find, and the AWS-native tools can produce continuous evidence. If SOC 2 is on your roadmap, run the assessment early — see [what a SOC 2 readiness assessment covers](/blog/soc-2-readiness-assessment/) and how to keep controls running with [continuous SOC 2 compliance](/blog/continuous-soc-2-compliance/).

## In practice

In the AWS environments we assess, the findings are rarely exotic. The usual list: access keys that haven't been rotated or used in months, roles with far broader permissions than the workload needs, logging switched on in the main region but not in others, and backups that run every night but have never been restored somewhere else. Cross-region restore tests in particular tend to surface surprises. We also regularly find cost savings along the way — idle resources and over-provisioned services — which helps pay for the security work.

## FAQ

### How long does an AWS security assessment take?

For a typical SaaS startup with a few AWS accounts, about one to two weeks including the report. Larger multi-account environments or adding a penetration test extends that.

### What access does the assessor need?

Read-only access through a dedicated IAM role, limited in time and removed after the assessment. No write access or long-lived keys are needed for the review itself.

### Is an AWS security assessment the same as a SOC 2 audit?

No. The assessment finds and prioritises security gaps in AWS. A SOC 2 audit is performed by a licensed CPA firm and reports on whether your controls were designed and operated effectively. Fixing assessment findings is good preparation for that audit.

### How often should we assess our AWS security?

Run continuous automated checks all year, and a full expert assessment at least annually — or after major architecture changes, new regions or before a SOC 2 audit.

Related: [how long SOC 2 takes](/blog/how-long-does-soc-2-take/) and the [SOC 2 audit checklist for AI startups](/blog/soc-2-checklist-for-ai-startups/). See our [cloud security assessment service](/services/cloud-security-assessment/) or [book a free scoping call](/contact/).
