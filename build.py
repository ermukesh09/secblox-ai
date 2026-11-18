#!/usr/bin/env python3
"""Static site generator for Secblox.
Edit SITE settings + page content below, run `python3 build.py`, push the /docs folder (or repo root) to GitHub Pages.
"""
import json, os, shutil, datetime, html

SITE = {
    "name": "Secblox",
    "domain": "https://secblox.io",
    "email": "connect@secblox.io",
    "booking": "https://cal.com/mukesh-bhakar-vzmbyl/30min",  # Cal.com booking page
    "linkedin": "https://www.linkedin.com/company/secblox",
    "indexnow_key": "2a4b273c96120af49169c533023737c6",  # IndexNow key (public by design; served at /<key>.txt)  # <-- your LinkedIn
    "tagline": "SOC 2 & AI Governance for SaaS and AI Companies",
    # Google Ads conversion tracking — leave blank to disable all tracking.
    "google_ads_id": "",            # e.g. "AW-123456789"
    "ads_label_booking": "",        # conversion label for "Booked call (Cal.com)"
    "ads_label_click": "",          # conversion label for "Clicked Book a call" (secondary)
}
OUT = "site"
TODAY = datetime.date.today().isoformat()

NAV = [("/soc-2-compliance/", "SOC 2"), ("/ai-governance/", "AI Governance"),
       ("/iso-42001/", "ISO 42001"), ("/soc-2-for-ai-companies/", "SOC 2 for AI"),
       ("/blog/", "Blog"), ("/about/", "About")]

def esc(s): return html.escape(s, quote=True)

def org_schema():
    d = SITE["domain"]
    return {
        "@type": "ProfessionalService", "@id": d + "/#org", "name": SITE["name"],
        "url": d + "/", "logo": d + "/assets/logo.png",
        "image": d + "/assets/og-image.png", "email": SITE["email"],
        "description": "Secblox helps SaaS and AI companies achieve SOC 2 and build AI governance programs aligned to ISO/IEC 42001, NIST AI RMF and the EU AI Act.",
        "areaServed": [{"@type": "Country", "name": "United States"}, {"@type": "Country", "name": "United Kingdom"},
                       {"@type": "Place", "name": "European Union"}, {"@type": "Country", "name": "India"}],
        "knowsAbout": ["SOC 2", "AI governance", "ISO/IEC 42001", "NIST AI RMF", "EU AI Act", "AI risk management",
                       "Cloud security", "AWS security", "Penetration testing", "Compliance automation"],
        "founder": {"@type": "Person", "name": "Mukesh Bhakar", "jobTitle": "Founder & Principal Consultant"},
        "sameAs": [SITE["linkedin"]],
    }

def page(path, title, desc, body, schema=None, crumbs=None, ptype="WebPage", noindex=False, minimal=False):
    d = SITE["domain"]; url = d + path
    graph = [org_schema(), {"@type": "WebSite", "@id": d + "/#website", "url": d + "/", "name": SITE["name"],
                            "publisher": {"@id": d + "/#org"}},
             {"@type": ptype, "@id": url + "#page", "url": url, "name": title, "description": desc,
              "isPartOf": {"@id": d + "/#website"}, "inLanguage": "en-US", "dateModified": TODAY}]
    if crumbs:
        items = [{"@type": "ListItem", "position": 1, "name": "Home", "item": d + "/"}]
        for i, (u, n) in enumerate(crumbs, 2):
            items.append({"@type": "ListItem", "position": i, "name": n, "item": d + u})
        graph.append({"@type": "BreadcrumbList", "itemListElement": items})
    if schema: graph.extend(schema)
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False)
    nav = "" if minimal else "".join(f'<li><a href="{u}"{" aria-current=page" if path.startswith(u) else ""}>{n}</a></li>' for u, n in NAV)
    crumb_html = ""
    if crumbs:
        crumb_html = '<nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a>' + "".join(
            f' / <a href="{u}">{esc(n)}</a>' for u, n in crumbs[:-1]) + f' / <span>{esc(crumbs[-1][1])}</span></nav>'
    body = body.replace("{{CRUMBS}}", crumb_html)
    robots = "noindex, follow" if noindex else "index, follow, max-image-preview:large, max-snippet:-1"
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#070b14">
<meta property="og:type" content="{"article" if ptype == "Article" else "website"}">
<meta property="og:site_name" content="{SITE["name"]}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{d}/assets/og-image.png">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}">
<meta name="twitter:image" content="{d}/assets/og-image.png">
<link rel="icon" href="/assets/favicon-32.png" sizes="32x32" type="image/png">
<link rel="icon" href="/assets/favicon-64.png" sizes="64x64" type="image/png">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="stylesheet" href="/assets/style.css">
<link rel="alternate" type="application/rss+xml" title="Secblox Blog" href="/feed.xml">
<script type="application/ld+json">{ld}</script>
{tracking_head()}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap nav">
<a class="logo" href="/">{LOGO_SVG}<span class="wordmark">Secblox</span></a>
{"" if minimal else '<button class="menu-btn" aria-expanded="false" aria-controls="menu">Menu</button>'}
{f'<a class="btn btn-primary" href="#book">Book a call</a>' if minimal else f'<ul id="menu">{nav}<li><a class="btn btn-primary" href="{SITE["booking"]}" target="_blank" rel="noopener">Book a call</a></li></ul>'}
</div></header>
<main id="main">
{body}
</main>
<footer><div class="wrap">
<div class="foot">
<div><a class="logo" href="/">{LOGO_SVG}<span class="wordmark">Secblox</span></a><p style="margin-top:14px;max-width:340px">SOC 2 and AI governance for SaaS and AI companies. Practitioner-led readiness, implementation and audit support.</p></div>
<div><h3 class="fh">Services</h3><ul><li><a href="/soc-2-compliance/">SOC 2 Compliance</a></li><li><a href="/ai-governance/">AI Governance</a></li><li><a href="/iso-42001/">ISO 42001 Readiness</a></li><li><a href="/soc-2-for-ai-companies/">SOC 2 for AI Companies</a></li><li><a href="/services/penetration-testing/">Penetration Testing</a></li></ul></div>
<div><h3 class="fh">Frameworks</h3><ul><li><a href="/ai-governance/#nist-ai-rmf">NIST AI RMF</a></li><li><a href="/ai-governance/#eu-ai-act">EU AI Act</a></li><li><a href="/iso-42001/">ISO/IEC 42001</a></li><li><a href="/soc-2-compliance/#trust-services-criteria">SOC 2 TSC</a></li></ul></div>
<div><h3 class="fh">Company</h3><ul><li><a href="/about/">About</a></li><li><a href="/blog/">Blog</a></li><li><a href="/contact/">Contact</a></li><li><a href="/privacy-policy/">Privacy Policy</a></li><li><a href="mailto:{SITE["email"]}">{SITE["email"]}</a></li><li><a href="{SITE["linkedin"]}" rel="noopener">LinkedIn</a></li></ul></div>
</div>
<div class="copy"><span>© {datetime.date.today().year} Secblox. All rights reserved.</span><span>SOC 2 · ISO/IEC 42001 · NIST AI RMF · EU AI Act</span></div>
</div></footer>
<script>const b=document.querySelector('.menu-btn'),m=document.getElementById('menu');if(b)b.onclick=()=>{{const o=m.classList.toggle('open');b.setAttribute('aria-expanded',o)}};</script>
</body>
</html>'''

def tracking_head():
    """Google Ads tag + conversion events. Emits nothing unless SITE['google_ads_id'] is set."""
    aw = SITE["google_ads_id"]
    if not aw:
        return ""
    click = f"'{aw}/{SITE['ads_label_click']}'" if SITE["ads_label_click"] else "null"
    book = f"'{aw}/{SITE['ads_label_booking']}'" if SITE["ads_label_booking"] else "null"
    return f"""<script async src="https://www.googletagmanager.com/gtag/js?id={aw}"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','{aw}');
window.SBX_CONV={{click:{click},book:{book}}};
document.addEventListener('click',function(e){{var a=e.target.closest&&e.target.closest('a[href*="cal.com/"]');if(a&&SBX_CONV.click)gtag('event','conversion',{{send_to:SBX_CONV.click}});}});</script>"""

LOGO_SVG = '<img src="/assets/logo-96.png" width="34" height="34" alt="">'

def faq_block(faqs):
    h = "".join(f"<details><summary>{esc(q)}</summary><p>{a}</p></details>" for q, a in faqs)
    sch = {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q,
           "acceptedAnswer": {"@type": "Answer", "text": html.unescape(a).replace("<a href=", "<a href=")}} for q, a in faqs]}
    return h, sch

def service_schema(name, desc, path, stype):
    return {"@type": "Service", "name": name, "serviceType": stype, "description": desc,
            "provider": {"@id": SITE["domain"] + "/#org"}, "url": SITE["domain"] + path,
            "areaServed": "Worldwide", "audience": {"@type": "BusinessAudience", "audienceType": "SaaS and AI companies"}}

def cta(h="Ready to get audit-ready — and AI-ready?", p="Book a free 30-minute scoping call. You'll leave with a clear view of your gaps, timeline and realistic budget — no obligation."):
    return f'''<section><div class="wrap"><div class="cta-band"><h2>{h}</h2><p>{p}</p>
<div class="cta-row" style="justify-content:center"><a class="btn btn-primary" href="{SITE["booking"]}" target="_blank" rel="noopener">Book a free scoping call</a><a class="btn btn-ghost" href="/soc-2-for-ai-companies/">SOC 2 for AI companies →</a></div></div></div></section>'''

def aside(extra=""):
    return f'''<aside class="aside">
<div class="card"><h3>Free scoping call</h3><p>30 minutes. Your gaps, a realistic timeline and a tooling budget that fits.</p><a class="btn btn-primary" style="margin-top:16px" href="/contact/">Book now</a></div>
{extra}
<div class="card"><h3>Related</h3><p><a href="/soc-2-compliance/">SOC 2 compliance</a><br><a href="/ai-governance/">AI governance</a><br><a href="/iso-42001/">ISO 42001 readiness</a><br><a href="/soc-2-for-ai-companies/">SOC 2 for AI companies</a></p></div>
</aside>'''

PAGES = {}

# ---------------- HOME ----------------
home_faqs = [
 ("What does Secblox do?", "Secblox is a security and compliance consultancy that takes SaaS and AI companies from zero to a clean SOC 2 report and builds AI governance programs aligned to ISO/IEC 42001, the NIST AI Risk Management Framework and the EU AI Act."),
 ("How long does SOC 2 take?", "Most startups reach SOC 2 Type I readiness in 6–10 weeks. A Type II report adds an observation window, typically 3–6 months for a first report, before the auditor issues the opinion."),
 ("Do you replace compliance automation platforms?", "No — we make them work. We are platform-agnostic: we implement and operate the leading compliance automation platforms, and we will tell you honestly if a lighter, cheaper setup is enough for your stage."),
 ("Can you help us with AI governance if we already have SOC 2?", "Yes. Most of our AI governance work maps onto an existing SOC 2 control set, so you extend what you have — AI inventory, model risk assessments, AI policies and ISO 42001 controls — instead of starting a second program from scratch."),
 ("Do you perform penetration testing?", "Yes. Penetration testing and cloud security assessments are performed in-house by our principal consultant, not subcontracted, and findings feed directly into your SOC 2 evidence."),
]
fh, fs = faq_block(home_faqs)
PAGES["/"] = page("/", "SOC 2 & AI Governance Consulting for AI Companies | Secblox",
 "Pass SOC 2 and build AI governance aligned to ISO 42001, NIST AI RMF and the EU AI Act. Practitioner-led consulting for SaaS and AI companies.",
f'''<section class="hero"><div class="wrap">
<span class="eyebrow">SOC 2 · ISO 42001 · NIST AI RMF · EU AI Act</span>
<h1>SOC 2 and <em>AI governance</em> for companies that ship AI.</h1>
<p class="lead">Enterprise buyers now ask two questions: <strong>“Do you have SOC 2?”</strong> and <strong>“How do you govern your AI?”</strong> Secblox gets you a clean answer to both — with hands-on implementation, not slide decks.</p>
<div class="cta-row"><a class="btn btn-primary" href="{SITE["booking"]}" target="_blank" rel="noopener">Book a free scoping call</a><a class="btn btn-ghost" href="/soc-2-for-ai-companies/">How SOC 2 works for AI products →</a></div>
<div class="trust"><span><b>15+ years</b> in security</span><span><b>AWS · Azure · GCP</b></span><span><b>Platform-agnostic</b> compliance automation</span><span><b>In-house</b> penetration testing</span></div>
</div></section>

<section><div class="wrap">
<h2>One program. Two of the questions that close enterprise deals.</h2>
<p class="sub">SOC 2 proves your security controls work. AI governance proves your AI is managed responsibly. We build them as one connected control set, so you don't pay twice for evidence.</p>
<div class="grid g3">
<a class="card" href="/soc-2-compliance/"><div class="icon">🛡️</div><span class="tag">Core</span><h3>SOC 2 Compliance</h3><p>Readiness, gap assessment, control implementation, policies, evidence and auditor management for SOC 2 Type I and Type II.</p><span class="more">SOC 2 services →</span></a>
<a class="card" href="/ai-governance/"><div class="icon">🧭</div><span class="tag">AI</span><h3>AI Governance</h3><p>AI inventory, risk assessment, AI policies and controls aligned to NIST AI RMF and EU AI Act obligations — practical, not theoretical.</p><span class="more">AI governance →</span></a>
<a class="card" href="/iso-42001/"><div class="icon">📐</div><span class="tag">Certification</span><h3>ISO/IEC 42001 Readiness</h3><p>Build an AI Management System (AIMS) ready for certification audit — scoped, documented and mapped to your existing SOC 2 controls.</p><span class="more">ISO 42001 →</span></a>
<a class="card" href="/soc-2-for-ai-companies/"><div class="icon">🤖</div><span class="tag">Specialty</span><h3>SOC 2 for AI Companies</h3><p>LLM apps, model APIs, RAG pipelines and AI agents raise audit questions traditional SaaS doesn't. We know which ones your auditor will ask.</p><span class="more">SOC 2 for AI →</span></a>
<a class="card" href="/services/penetration-testing/"><div class="icon">🎯</div><span class="tag">Add-on</span><h3>Penetration Testing</h3><p>Web app, API and cloud penetration testing performed in-house, including LLM-specific tests such as prompt injection and data leakage.</p><span class="more">Pen testing →</span></a>
<a class="card" href="/services/cloud-security-assessment/"><div class="icon">☁️</div><span class="tag">Add-on</span><h3>Cloud Security Assessment</h3><p>AWS, Azure and GCP architecture reviews that harden your environment, satisfy SOC 2 — and often cut your cloud bill.</p><span class="more">Cloud security →</span></a>
</div></div></section>

<section class="alt"><div class="wrap">
<h2>How we get you audit-ready</h2>
<p class="sub">A clear, fixed path from “we need SOC 2 for this deal” to a report in hand.</p>
<div class="steps">
<div class="step"><h3>Scope & gap assessment</h3><p>System boundary, Trust Services Criteria, AI use cases and a prioritized gap list in week one.</p></div>
<div class="step"><h3>Implement controls</h3><p>Policies, IAM, logging, vendor risk, change management, AI controls — implemented with your team, not just recommended.</p></div>
<div class="step"><h3>Automate evidence</h3><p>Right-sized compliance tooling and integrations so evidence collects itself during the observation window.</p></div>
<div class="step"><h3>Audit & renew</h3><p>We manage the auditor, answer requests and run year-over-year renewals so compliance doesn't decay.</p></div>
</div></div></section>

<section><div class="wrap">
<div class="grid g2" style="align-items:center">
<div><h2>Why companies choose <em>Secblox</em></h2>
<p class="sub" style="margin-bottom:0">You get a practitioner who has built security programs from zero and taken SaaS platforms through SOC 2 end to end — not a junior consultant reading from a template.</p></div>
<div class="grid g2">
<div class="card"><h3>Hands-on</h3><p>We implement controls in AWS, Azure, GCP, Entra ID and your SaaS stack.</p></div>
<div class="card"><h3>Budget-smart</h3><p>Tooling sized to your stage. No over-buying platforms you don't need yet.</p></div>
<div class="card"><h3>AI-native</h3><p>Governance that understands models, prompts, training data and agents.</p></div>
<div class="card"><h3>Renewal-ready</h3><p>Programs designed to survive year two, not just pass year one.</p></div>
</div></div></div></section>

{{LATEST}}
<section class="alt"><div class="wrap" style="max-width:860px">
<h2>Frequently asked questions</h2>
<p class="sub">Quick answers on SOC 2 and AI governance.</p>
{fh}
</div></section>
{cta()}''', schema=[fs])

# ---------------- SOC 2 ----------------
soc_faqs = [
 ("What is the difference between SOC 2 Type I and Type II?", "A Type I report assesses whether your controls are suitably designed at a single point in time. A Type II report tests whether those controls operated effectively over an observation period, usually 3 to 12 months. Most enterprise buyers ultimately expect Type II."),
 ("Which Trust Services Criteria do we need?", "Security (the Common Criteria) is mandatory. Availability, Confidentiality, Processing Integrity and Privacy are optional and should be added only when customers or contracts require them. We help you scope this so you don't audit more than you need."),
 ("How much does SOC 2 cost?", "Total cost depends on company size, scope and tooling, and breaks down into the audit fee, compliance automation software, consulting and any security tooling gaps. On the scoping call we give you a realistic range for your situation."),
 ("Is SOC 2 a certification?", "No. SOC 2 is an attestation report issued by a licensed CPA firm under AICPA standards. There is no SOC 2 'certificate' — you receive a report describing your system and the auditor's opinion on your controls."),
 ("Do we need a compliance automation platform?", "Not always. Compliance automation platforms save significant evidence effort for most SaaS teams, but very early-stage companies can sometimes start lighter. We recommend what fits your budget and stage."),
]
fh, fs = faq_block(soc_faqs)
PAGES["/soc-2-compliance/"] = page("/soc-2-compliance/", "SOC 2 Compliance Consulting: Type I & Type II | Secblox",
 "End-to-end SOC 2 consulting for SaaS and AI startups: gap assessment, controls, policies, evidence automation and audit support for Type I and II.",
f'''<div class="page-hero"><div class="wrap">{{{{CRUMBS}}}}<span class="eyebrow">SOC 2 Type I & Type II</span><h1>SOC 2 compliance consulting, <em>done with you</em> — not just for you.</h1>
<p class="lead">From your first gap assessment to a clean Type II report and every renewal after. We implement the controls, build the evidence trail and manage the auditor.</p>
<div class="cta-row"><a class="btn btn-primary" href="{SITE["booking"]}" target="_blank" rel="noopener">Get a SOC 2 scoping call</a></div></div></div>
<section><div class="wrap layout"><article class="prose">
<h2>What is SOC 2?</h2>
<p><strong>SOC 2</strong> (System and Organization Controls 2) is an attestation framework developed by the AICPA. An independent CPA firm examines how your company protects customer data against the <strong>Trust Services Criteria</strong> and issues a report your customers can rely on. For B2B SaaS and AI companies selling to US enterprises, SOC 2 has become a standard procurement requirement.</p>

<h2 id="trust-services-criteria">The five Trust Services Criteria</h2>
<div class="table-wrap"><table><thead><tr><th>Criteria</th><th>What it covers</th><th>Required?</th></tr></thead><tbody>
<tr><td><strong>Security</strong></td><td>Protection against unauthorized access (the Common Criteria, CC1–CC9)</td><td>Always</td></tr>
<tr><td><strong>Availability</strong></td><td>Uptime, capacity, backup and disaster recovery</td><td>Optional</td></tr>
<tr><td><strong>Confidentiality</strong></td><td>Protection of data designated as confidential</td><td>Optional</td></tr>
<tr><td><strong>Processing Integrity</strong></td><td>Complete, valid, accurate and timely processing</td><td>Optional</td></tr>
<tr><td><strong>Privacy</strong></td><td>Collection, use and disposal of personal information</td><td>Optional</td></tr>
</tbody></table></div>

<h2>Our SOC 2 engagement</h2>
<h3>1. Scoping and gap assessment</h3>
<p>We define your system boundary, in-scope infrastructure, people and vendors, select the right Trust Services Criteria and produce a prioritized remediation plan.</p>
<h3>2. Policies and procedures</h3>
<p>A complete, right-sized policy set — information security, access control, change management, incident response, vendor management, BCP/DR, data classification and more — written for how your team actually works.</p>
<h3>3. Control implementation</h3>
<p>Hands-on technical work across AWS, Azure and GCP: IAM and SSO, MFA, logging and monitoring, encryption, vulnerability management, endpoint security (EDR/MDM), backups and cross-region recovery testing.</p>
<h3>4. Evidence automation</h3>
<p>We implement and configure your compliance automation platform and integrations so evidence is collected continuously through the observation period.</p>
<h3>5. Audit support</h3>
<p>We help you select an auditor, write the system description, respond to evidence requests and remediate exceptions before they reach the report.</p>
<h3>6. Renewals</h3>
<p>SOC 2 is annual. We run year-over-year renewals, annual BCP/DR tests, access reviews and risk assessments so your program stays healthy.</p>

<h2>Typical SOC 2 timeline</h2>
<ul><li><strong>Weeks 1–2:</strong> scoping, gap assessment, tooling setup</li>
<li><strong>Weeks 3–8:</strong> policy rollout and control implementation</li>
<li><strong>Weeks 8–10:</strong> Type I audit (optional)</li>
<li><strong>Months 3–9:</strong> Type II observation window and audit</li></ul>

<h2>Frequently asked questions</h2>
{fh}
</article>{aside()}</div></section>{cta()}''',
 schema=[fs, service_schema("SOC 2 Compliance Consulting", "SOC 2 Type I and Type II readiness, implementation and audit support.", "/soc-2-compliance/", "Compliance consulting")],
 crumbs=[("/soc-2-compliance/", "SOC 2 Compliance")])

# ---------------- AI GOVERNANCE ----------------
ai_faqs = [
 ("What is AI governance?", "AI governance is the set of policies, roles, processes and controls an organization uses to develop, buy and use AI responsibly — covering risk assessment, data and model management, transparency, human oversight, security and accountability."),
 ("Which AI governance framework should we start with?", "For most companies, the NIST AI Risk Management Framework is the best starting structure because it is practical and voluntary. If customers want certification, ISO/IEC 42001 is the certifiable standard. If you place AI on the EU market or your outputs are used in the EU, the EU AI Act applies regardless of framework choice."),
 ("Does the EU AI Act apply to US companies?", "It can. The EU AI Act applies to providers placing AI systems on the EU market and, in some cases, to providers and deployers outside the EU whose AI system output is used in the EU. Obligations depend on your role and the system's risk category."),
 ("Can AI governance be combined with SOC 2?", "Yes, and it should be. Many AI governance controls — access control, change management, vendor risk, logging and incident response — already exist in SOC 2. We extend those controls and add AI-specific ones rather than building a separate program."),
]
fh, fs = faq_block(ai_faqs)
PAGES["/ai-governance/"] = page("/ai-governance/", "AI Governance Consulting: NIST AI RMF & EU AI Act | Secblox",
 "AI governance consulting: AI inventory, risk assessments, policies and controls aligned to NIST AI RMF, the EU AI Act and ISO 42001.",
f'''<div class="page-hero"><div class="wrap">{{{{CRUMBS}}}}<span class="eyebrow">Responsible AI · AI Risk Management</span><h1>AI governance that <em>passes buyer scrutiny</em> — and holds up in production.</h1>
<p class="lead">Your customers' security questionnaires now ask about training data, model risk, prompt injection and human oversight. We build the governance program that answers them with evidence.</p>
<div class="cta-row"><a class="btn btn-primary" href="{SITE["booking"]}" target="_blank" rel="noopener">Talk about AI governance</a></div></div></div>
<section><div class="wrap layout"><article class="prose">
<h2>Why AI governance now</h2>
<p>AI adoption has outpaced the controls around it. Enterprise procurement teams, regulators and boards increasingly expect companies to show <strong>which AI systems they use, what risks those systems carry and how those risks are controlled</strong>. A governance program turns that expectation into a repeatable, auditable process.</p>

<h2>What we deliver</h2>
<ul>
<li><strong>AI system inventory</strong> — every model, AI feature, third-party AI API and internal AI tool, with owners and data flows.</li>
<li><strong>AI risk assessments</strong> — structured assessment of each system for security, privacy, bias, reliability and misuse risks.</li>
<li><strong>AI policies</strong> — acceptable use of AI, AI development lifecycle, third-party AI vendor policy, AI incident response.</li>
<li><strong>Technical AI controls</strong> — prompt-injection defenses, output filtering, data leakage prevention, model access control, logging and monitoring.</li>
<li><strong>Vendor AI due diligence</strong> — assessing OpenAI, Anthropic, Azure OpenAI, Bedrock and other providers your product depends on.</li>
<li><strong>Board and customer reporting</strong> — trust-center content and questionnaire answers your sales team can reuse.</li>
</ul>

<h2 id="nist-ai-rmf">NIST AI Risk Management Framework (AI RMF)</h2>
<p>The NIST AI RMF organizes AI risk management into four functions: <strong>Govern</strong>, <strong>Map</strong>, <strong>Measure</strong> and <strong>Manage</strong>. We run NIST AI RMF assessments that score your current maturity in each function and produce a prioritized roadmap, including the Generative AI Profile for LLM-based products.</p>

<h2 id="eu-ai-act">EU AI Act readiness</h2>
<p>The EU AI Act classifies AI systems by risk — prohibited, high-risk, limited-risk (transparency obligations) and minimal-risk — with separate obligations for general-purpose AI models. Its obligations phase in over several years. We help you determine whether you are a provider or deployer, classify your systems, and build the documentation, transparency and oversight measures your category requires.</p>

<h2>ISO/IEC 42001</h2>
<p>ISO/IEC 42001 is the first certifiable international standard for an <strong>AI Management System (AIMS)</strong>. If your customers want a certificate rather than a self-assessment, see our <a href="/iso-42001/">ISO 42001 readiness service</a>.</p>

<h2>Frameworks compared</h2>
<div class="table-wrap"><table><thead><tr><th>Aspect</th><th>NIST AI RMF</th><th>ISO/IEC 42001</th><th>EU AI Act</th></tr></thead><tbody>
<tr><td><strong>Type</strong></td><td>Voluntary framework</td><td>Certifiable standard</td><td>Regulation (law)</td></tr>
<tr><td><strong>Best for</strong></td><td>Structuring AI risk work</td><td>Proving governance to customers</td><td>Legal compliance in the EU</td></tr>
<tr><td><strong>Outcome</strong></td><td>Maturity profile & roadmap</td><td>Third-party certificate</td><td>Conformity & documentation</td></tr>
</tbody></table></div>

<h2>Frequently asked questions</h2>
{fh}
</article>{aside()}</div></section>{cta("Make your AI a sales advantage, not a blocker.", "Book a free call and we'll map your AI systems against NIST AI RMF, ISO 42001 and the EU AI Act in 30 minutes.")}''',
 schema=[fs, service_schema("AI Governance Consulting", "AI inventory, risk assessments, AI policies and controls aligned to NIST AI RMF, ISO/IEC 42001 and the EU AI Act.", "/ai-governance/", "AI governance and risk management")],
 crumbs=[("/ai-governance/", "AI Governance")])

# ---------------- ISO 42001 ----------------
iso_faqs = [
 ("What is ISO/IEC 42001?", "ISO/IEC 42001:2023 is the international standard that specifies requirements for establishing, implementing, maintaining and continually improving an AI Management System (AIMS) within an organization. It is certifiable by accredited certification bodies."),
 ("Who needs ISO 42001 certification?", "Companies that build AI products or embed AI into services and want to demonstrate responsible AI management to enterprise customers, partners or regulators. It is especially valuable for AI-first SaaS vendors selling into regulated industries."),
 ("How does ISO 42001 relate to ISO 27001 and SOC 2?", "ISO 42001 follows the same management-system structure as ISO 27001, so organizations with ISO 27001 or SOC 2 can reuse much of their existing governance, risk and control documentation and focus on AI-specific requirements."),
 ("How long does ISO 42001 readiness take?", "It depends on the number of AI systems in scope and existing maturity. Organizations with an existing SOC 2 or ISO 27001 program usually move faster because core management processes already exist."),
]
fh, fs = faq_block(iso_faqs)
PAGES["/iso-42001/"] = page("/iso-42001/", "ISO 42001 Readiness & AIMS Implementation | Secblox",
 "ISO/IEC 42001 readiness: scope your AI Management System, run impact assessments, implement Annex A controls and prepare for certification.",
f'''<div class="page-hero"><div class="wrap">{{{{CRUMBS}}}}<span class="eyebrow">ISO/IEC 42001:2023</span><h1>ISO 42001 readiness for an <em>AI Management System</em> that certifies.</h1>
<p class="lead">Build your AIMS, implement the controls and walk into your certification audit prepared — reusing the SOC 2 and ISO 27001 work you've already done.</p>
<div class="cta-row"><a class="btn btn-primary" href="{SITE["booking"]}" target="_blank" rel="noopener">Plan your ISO 42001 path</a></div></div></div>
<section><div class="wrap layout"><article class="prose">
<h2>What ISO 42001 requires</h2>
<p>ISO/IEC 42001 follows the harmonized management-system structure (Clauses 4–10) used by ISO 27001, plus AI-specific controls in Annex A. In practice you need to show:</p>
<ul>
<li><strong>Context and scope</strong> — which AI systems and roles (developer, provider, user) are in scope.</li>
<li><strong>Leadership and AI policy</strong> — top-management commitment, roles and an AI policy.</li>
<li><strong>Planning</strong> — AI risk assessment, risk treatment and <strong>AI system impact assessments</strong>.</li>
<li><strong>Support and operation</strong> — resources, competence, documentation and AI lifecycle processes.</li>
<li><strong>Performance evaluation</strong> — monitoring, internal audit and management review.</li>
<li><strong>Improvement</strong> — nonconformity handling and continual improvement.</li>
</ul>

<h2>Our ISO 42001 readiness program</h2>
<h3>Gap assessment</h3><p>Clause-by-clause and Annex A gap analysis against your current state, with effort estimates.</p>
<h3>AIMS design</h3><p>Scope statement, AI policy, roles and responsibilities, Statement of Applicability and risk methodology.</p>
<h3>Impact & risk assessments</h3><p>AI system impact assessments covering individuals, groups and society, plus AI risk treatment plans.</p>
<h3>Control implementation</h3><p>Data quality and provenance, model lifecycle, third-party AI, transparency and human oversight controls — implemented, not just documented.</p>
<h3>Internal audit & certification support</h3><p>Pre-certification internal audit, management review and support through Stage 1 and Stage 2 audits.</p>

<h2>Reuse your SOC 2 investment</h2>
<p>Access control, change management, vendor risk, incident response, logging and risk assessment already exist in a mature SOC 2 program. We map them into your AIMS so the incremental effort goes into the AI-specific requirements. See <a href="/blog/soc-2-vs-iso-42001/">SOC 2 vs ISO 42001</a>.</p>

<h2>Frequently asked questions</h2>
{fh}
</article>{aside()}</div></section>{cta()}''',
 schema=[fs, service_schema("ISO/IEC 42001 Readiness", "AI Management System design, impact assessments, Annex A control implementation and certification support.", "/iso-42001/", "ISO 42001 consulting")],
 crumbs=[("/iso-42001/", "ISO 42001")])

# ---------------- SOC 2 for AI ----------------
s4ai_faqs = [
 ("Does SOC 2 cover AI systems?", "SOC 2 has no AI-specific criteria, but your AI features sit inside your system boundary, so the Trust Services Criteria apply to them. Auditors increasingly ask how AI components, model providers and training data are governed under existing controls."),
 ("Are OpenAI, Anthropic or other model providers in scope for our SOC 2?", "They are typically subservice organizations or vendors. You need vendor risk assessments, a review of their own SOC 2 reports, data-processing terms and a clear description of how they fit into your system — usually using the carve-out method."),
 ("What AI risks do auditors and buyers ask about?", "Common questions cover customer data used for training, data retention by model providers, prompt injection, output data leakage, access to model and prompt configurations, change management for prompts and models, and monitoring of AI behaviour."),
]
fh, fs = faq_block(s4ai_faqs)
PAGES["/soc-2-for-ai-companies/"] = page("/soc-2-for-ai-companies/", "SOC 2 for AI Companies: LLM, RAG & Agents | Secblox",
 "How AI startups pass SOC 2: scoping LLM vendors, training data, prompt injection, model change management and the AI evidence auditors ask for.",
f'''<div class="page-hero"><div class="wrap">{{{{CRUMBS}}}}<span class="eyebrow">LLM apps · RAG · AI agents</span><h1>SOC 2 for <em>AI companies</em>: what changes when your product runs on models.</h1>
<p class="lead">LLM providers, vector databases, prompts-as-code and autonomous agents all live inside your SOC 2 system boundary. Here's how to control them — and prove it.</p>
<div class="cta-row"><a class="btn btn-primary" href="{SITE["booking"]}" target="_blank" rel="noopener">Scope SOC 2 for your AI product</a></div></div></div>
<section><div class="wrap layout"><article class="prose">
<h2>Where AI products trip up SOC 2</h2>
<div class="table-wrap"><table><thead><tr><th>AI component</th><th>SOC 2 concern</th><th>Control approach</th></tr></thead><tbody>
<tr><td>Third-party LLM APIs</td><td>Subservice organization, data retention, training on customer data</td><td>Vendor risk review, SOC 2 report review, zero-retention / no-training terms, carve-out in system description</td></tr>
<tr><td>Prompts & system instructions</td><td>Unreviewed changes alter system behaviour</td><td>Prompts in version control, peer review, change tickets, deployment approvals</td></tr>
<tr><td>RAG / vector stores</td><td>Cross-tenant data exposure</td><td>Tenant isolation, access-filtered retrieval, encryption, logging</td></tr>
<tr><td>Model inputs/outputs</td><td>Prompt injection, sensitive data leakage</td><td>Input validation, output filtering, DLP, red-team / pen testing</td></tr>
<tr><td>AI agents & tool use</td><td>Over-privileged actions</td><td>Least-privilege tool permissions, human approval for high-impact actions, audit logs</td></tr>
<tr><td>Fine-tuning & training data</td><td>Confidentiality and privacy of customer data</td><td>Data classification, consent, retention and deletion procedures</td></tr>
</tbody></table></div>

<h2>Writing the system description for an AI product</h2>
<p>Your SOC 2 system description must explain how AI components process customer data. We draft it so it is accurate for auditors and reassuring for buyers — describing model providers, data flows, retention, and the complementary controls you expect from customers and subservice organizations.</p>

<h2>Going beyond SOC 2</h2>
<p>SOC 2 answers the security question. Buyers increasingly also want AI-specific assurance. We layer <a href="/ai-governance/">AI governance</a> aligned to NIST AI RMF, and <a href="/iso-42001/">ISO 42001</a> when certification is needed, onto the same control set.</p>

<h2>Frequently asked questions</h2>
{fh}
</article>{aside()}</div></section>{cta()}''',
 schema=[fs, service_schema("SOC 2 for AI Companies", "SOC 2 readiness for LLM, RAG and AI-agent products, including AI-specific controls and system description.", "/soc-2-for-ai-companies/", "Compliance consulting")],
 crumbs=[("/soc-2-for-ai-companies/", "SOC 2 for AI Companies")])

# ---------------- PEN TEST ----------------
PAGES["/services/penetration-testing/"] = page("/services/penetration-testing/", "Penetration Testing for SaaS & LLM Apps | Secblox",
 "In-house web application, API, cloud and LLM penetration testing for SaaS and AI companies. Findings mapped to SOC 2 evidence, with retesting included.",
f'''<div class="page-hero"><div class="wrap">{{{{CRUMBS}}}}<span class="eyebrow">Web · API · Cloud · LLM</span><h1>Penetration testing that <em>feeds your SOC 2</em>.</h1>
<p class="lead">Performed in-house by our principal consultant. Clear findings, practical fixes, retesting, and a report your auditor and customers will accept.</p>
<div class="cta-row"><a class="btn btn-primary" href="{SITE["booking"]}" target="_blank" rel="noopener">Request a pen test quote</a></div></div></div>
<section><div class="wrap layout"><article class="prose">
<h2>What we test</h2>
<ul><li><strong>Web applications</strong> — authentication, authorization, session handling, injection and business-logic flaws (OWASP Top 10).</li>
<li><strong>APIs</strong> — REST and GraphQL, broken object-level authorization, rate limiting and data exposure (OWASP API Top 10).</li>
<li><strong>Cloud</strong> — AWS, Azure and GCP misconfigurations, IAM privilege escalation, exposed storage and network paths.</li>
<li><strong>LLM & AI features</strong> — prompt injection, jailbreaks, system-prompt leakage, insecure output handling, data exfiltration via RAG and excessive agency (OWASP Top 10 for LLM Applications).</li></ul>
<h2>What you get</h2>
<ul><li>Executive summary and technical report with risk-rated findings</li><li>Reproduction steps and remediation guidance</li><li>Retest of fixed findings and an attestation letter for customers</li></ul>
</article>{aside()}</div></section>{cta()}''',
 schema=[service_schema("Penetration Testing", "Web, API, cloud and LLM penetration testing.", "/services/penetration-testing/", "Penetration testing")],
 crumbs=[("/services/penetration-testing/", "Penetration Testing")])

# ---------------- CLOUD ----------------
PAGES["/services/cloud-security-assessment/"] = page("/services/cloud-security-assessment/", "Cloud Security Assessment — AWS, Azure & GCP | Secblox",
 "AWS, Azure and GCP security assessments for SaaS and AI companies: IAM, network, logging, encryption and DR — mapped to SOC 2.",
f'''<div class="page-hero"><div class="wrap">{{{{CRUMBS}}}}<span class="eyebrow">AWS · Azure · GCP</span><h1>Cloud security assessments that <em>harden and simplify</em>.</h1>
<p class="lead">An architecture-level review of your cloud environment, mapped to SOC 2 controls — with practical fixes that frequently reduce spend as well as risk.</p>
<div class="cta-row"><a class="btn btn-primary" href="{SITE["booking"]}" target="_blank" rel="noopener">Book a cloud review</a></div></div></div>
<section><div class="wrap layout"><article class="prose">
<h2>Assessment areas</h2>
<ul><li>Identity and access management, SSO, MFA and privileged access</li><li>Network segmentation, ingress and egress controls</li><li>Logging, monitoring and alerting (CloudTrail, GuardDuty, Defender, Security Command Center)</li><li>Encryption at rest and in transit, key management</li><li>Backup, cross-region recovery, RTO/RPO testing</li><li>Security for AI workloads: Bedrock, Azure OpenAI, Vertex AI</li><li>Cost and resource hygiene that reduces attack surface</li></ul>
<h2>Deliverables</h2>
<p>A prioritized findings report, a target architecture, and SOC 2 control mapping — plus hands-on remediation support if you want it.</p>
</article>{aside()}</div></section>{cta()}''',
 schema=[service_schema("Cloud Security Assessment", "AWS, Azure and GCP security architecture assessment.", "/services/cloud-security-assessment/", "Cloud security consulting")],
 crumbs=[("/services/cloud-security-assessment/", "Cloud Security Assessment")])

# ---------------- ABOUT ----------------
PAGES["/about/"] = page("/about/", "About Secblox — Practitioner-Led SOC 2 & AI Governance",
 "Secblox is led by Mukesh Bhakar, a security practitioner with 15+ years building security programs and taking SaaS companies through SOC 2.",
f'''<div class="page-hero"><div class="wrap">{{{{CRUMBS}}}}<span class="eyebrow">About</span><h1>Built by a practitioner, <em>for builders</em>.</h1>
<p class="lead">Secblox exists because compliance should make companies more secure and easier to buy from — not just generate paperwork.</p></div></div>
<section><div class="wrap layout"><article class="prose">
<h2>Mukesh Bhakar — Founder & Principal Consultant</h2>
<p>Mukesh brings <strong>15+ years of security experience</strong> across cloud security architecture, identity, endpoint security and compliance. He has built security programs from zero — deploying EDR, email security, identity controls and MDM where no security tooling existed — and takes SaaS platforms on AWS through SOC 2 end to end, from readiness to report and through annual renewals.</p>
<p>His work spans <strong>AWS, Azure and GCP</strong>, identity and access management, DLP, endpoint detection and response, email security and SASE/CASB, and hands-on operation of the leading <strong>compliance automation platforms</strong>. Framework experience covers <strong>SOC 2, GDPR and NIST</strong>, with a focus on AI security and governance: <strong>NIST AI RMF, MITRE ATLAS, the EU AI Act and ISO/IEC 42001</strong>.</p>
<h2>How we work</h2>
<ul><li><strong>Hands-on implementation</strong> — we configure the controls, not just recommend them.</li>
<li><strong>Budget discipline</strong> — tooling sized to your stage; we'll tell you when you don't need to buy something.</li>
<li><strong>Security first, compliance as proof</strong> — controls that actually reduce risk, with evidence as a by-product.</li>
<li><strong>In-house testing</strong> — penetration testing performed directly, not subcontracted.</li></ul>
</article>{aside()}</div></section>{cta()}''',
 schema=[{"@type": "Person", "name": "Mukesh Bhakar", "jobTitle": "Founder & Principal Consultant", "worksFor": {"@id": SITE["domain"] + "/#org"},
          "knowsAbout": ["SOC 2", "AI governance", "ISO/IEC 42001", "NIST AI RMF", "EU AI Act", "Cloud security", "Penetration testing"]}],
 crumbs=[("/about/", "About")], ptype="AboutPage")


CAL_EMBED = """<script>
(function(){function load(){(function (C, A, L) { let p = function (a, ar) { a.q.push(ar); }; let d = C.document; C.Cal = C.Cal || function () { let cal = C.Cal; let ar = arguments; if (!cal.loaded) { cal.ns = {}; cal.q = cal.q || []; d.head.appendChild(d.createElement("script")).src = A; cal.loaded = true; } if (ar[0] === L) { const api = function () { p(api, arguments); }; const namespace = ar[1]; api.q = api.q || []; if (typeof namespace === "string") { cal.ns[namespace] = cal.ns[namespace] || api; p(cal.ns[namespace], ar); p(cal, ["initNamespace", namespace]); } else p(cal, ar); return; } p(cal, ar); }; })(window, "https://app.cal.com/embed/embed.js", "init");
Cal("init", "30min", {origin: "https://app.cal.com"});
Cal.ns["30min"]("inline", {elementOrSelector: "#cal-inline", config: {layout: "month_view", theme: "dark"}, calLink: "mukesh-bhakar-vzmbyl/30min"});
Cal.ns["30min"]("ui", {theme: "dark", hideEventTypeDetails: false, layout: "month_view", cssVarsPerTheme: {dark: {"cal-brand": "#3ee6c4"}}});
var sent=false;function conv(){if(sent)return;sent=true;if(window.gtag&&window.SBX_CONV&&SBX_CONV.book)gtag('event','conversion',{send_to:SBX_CONV.book});}
Cal.ns["30min"]("on", {action: "bookingSuccessfulV2", callback: conv});
Cal.ns["30min"]("on", {action: "bookingSuccessful", callback: conv});}
if ("requestIdleCallback" in window) requestIdleCallback(load, {timeout: 2000}); else setTimeout(load, 800);})();
</script>"""

# ---------------- CONTACT ----------------
PAGES["/contact/"] = page("/contact/", "Book a Free SOC 2 & AI Governance Call | Secblox",
 "Book a free 30-minute scoping call with Secblox to discuss SOC 2, ISO 42001, AI governance, penetration testing or cloud security assessment.",
f'''<div class="page-hero"><div class="wrap">{{{{CRUMBS}}}}<span class="eyebrow">Contact</span><h1>Let's scope your <em>SOC 2 and AI governance</em> path.</h1>
<p class="lead">30 minutes, no obligation. You'll get your likely gaps, a realistic timeline and a budget range.</p></div></div>
<section><div class="wrap grid g2">
<div class="card"><div class="icon">📅</div><h2 style="font-size:1.2rem">Book a call</h2><p>Pick a 30-minute slot that suits you — the calendar shows times in your own time zone.</p><a class="btn btn-primary" style="margin-top:16px" href="{SITE["booking"]}" target="_blank" rel="noopener">Open booking page</a></div>
<div class="card"><div class="icon">✉️</div><h2 style="font-size:1.2rem">Email us</h2><p>Tell us about your product, cloud provider, deadline and any customer requirements.</p><a class="btn btn-ghost" style="margin-top:16px" href="mailto:{SITE["email"]}?subject=SOC%202%20%2F%20AI%20governance%20enquiry">{SITE["email"]}</a></div>
</div>
<div class="wrap" style="margin-top:48px"><h2>Book your scoping call</h2><p class="sub" style="margin-bottom:20px">Choose a time below. If the calendar doesn't load, <a style="text-decoration:underline" href="{SITE["booking"]}" target="_blank" rel="noopener">open the booking page</a>.</p><div id="cal-inline" style="width:100%;min-height:640px;border:1px solid var(--line);border-radius:14px;overflow:auto;background:var(--card)"></div></div>{CAL_EMBED}
<div class="wrap prose" style="margin-top:48px"><h2>Helpful to share</h2><ul><li>What you sell and who your customers are</li><li>Cloud provider(s) and team size</li><li>Which framework you need (SOC 2, ISO 42001, EU AI Act) and by when</li><li>Any compliance tooling you already use</li></ul></div></section>''',
 crumbs=[("/contact/", "Contact")], ptype="ContactPage")

# ---------------- INSIGHTS ----------------
# ---------------- BLOG (Markdown posts in /posts) ----------------
# To publish a post: add posts/YYYY-MM-DD-your-slug.md with the front matter below, commit, push.
#   ---
#   title: Your title (aim for <= 60 characters)
#   description: One-sentence summary (aim for 120-155 characters)
#   date: 2026-12-01
#   tags: SOC 2, AI governance
#   ---
import glob, re, markdown as _md
from email.utils import format_datetime

def load_posts():
    posts = []
    for f in sorted(glob.glob("posts/*.md"), reverse=True):
        raw = open(f, encoding="utf-8").read()
        m = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", raw, re.S)
        if not m: raise SystemExit(f"Missing front matter in {f}")
        meta = dict(l.split(":", 1) for l in m.group(1).strip().splitlines() if ":" in l)
        meta = {k.strip(): v.strip() for k, v in meta.items()}
        if meta.get("draft", "").lower() == "true": continue
        slug = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", os.path.basename(f)[:-3])
        html_body = _md.markdown(m.group(2), extensions=["tables", "fenced_code", "toc", "sane_lists"])
        faqs = []
        fm = re.search(r"^##\s+(FAQ|FAQs|Frequently asked questions)\s*$(.*?)(?=^##\s|\Z)", m.group(2), re.S | re.M | re.I)
        if fm:
            for q, ans in re.findall(r"^###\s+(.+?)\s*$\n(.*?)(?=^###\s|\Z)", fm.group(2), re.S | re.M):
                text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", ans).replace("**", "").strip()
                text = " ".join(l for l in text.splitlines() if l.strip() and not l.lstrip().startswith(("Want", "Need help")))
                if text: faqs.append((q.strip(), text))
        words = len(re.sub("<[^>]+>", " ", html_body).split())
        posts.append({"slug": slug, "url": f"/blog/{slug}/", "title": meta["title"], "desc": meta["description"],
                      "date": meta["date"], "tags": [t.strip() for t in meta.get("tags", "").split(",") if t.strip()],
                      "html": html_body, "faqs": faqs, "mins": max(1, round(words / 220))})
    return posts

POSTS = load_posts()

def post_card(p):
    return (f'<a class="card" href="{p["url"]}"><span class="tag">{esc(p["tags"][0]) if p["tags"] else "Guide"}</span>'
            f'<h3>{esc(p["title"])}</h3><p>{esc(p["desc"])}</p>'
            f'<p style="margin-top:12px;font-size:13px">{p["date"]} · {p["mins"]} min read</p></a>')

for i, p in enumerate(POSTS):
    related = [q for q in POSTS if q is not p and set(q["tags"]) & set(p["tags"])][:3] or [q for q in POSTS if q is not p][:3]
    rel_html = "".join(f'<a href="{q["url"]}">{esc(q["title"])}</a><br>' for q in related)
    tags_html = " ".join(f'<span class="tag">{esc(t)}</span>' for t in p["tags"])
    PAGES[p["url"]] = page(p["url"], f'{p["title"]} | Secblox', p["desc"],
        f'''<div class="page-hero"><div class="wrap">{{{{CRUMBS}}}}{tags_html}<h1>{esc(p["title"])}</h1><p class="lead">{esc(p["desc"])}</p>
<p style="color:var(--muted);font-size:14px">By Mukesh Bhakar · <time datetime="{p["date"]}">{p["date"]}</time> · {p["mins"]} min read</p></div></div>
<section><div class="wrap layout"><article class="prose">{p["html"]}</article>{aside('<div class="card"><h3>More articles</h3><p>' + rel_html + '</p></div>')}</div></section>{cta()}''',
        schema=[{"@type": "BlogPosting", "headline": p["title"], "description": p["desc"], "datePublished": p["date"],
                 "dateModified": p["date"], "keywords": ", ".join(p["tags"]), "wordCount": len(p["html"].split()),
                 "author": {"@type": "Person", "name": "Mukesh Bhakar", "url": SITE["domain"] + "/about/"},
                 "publisher": {"@id": SITE["domain"] + "/#org"}, "image": SITE["domain"] + "/assets/og-image.png",
                 "mainEntityOfPage": SITE["domain"] + p["url"]}] + ([{"@type": "FAQPage", "mainEntity": [
                 {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faqs"]]}] if p["faqs"] else []),
        crumbs=[("/blog/", "Blog"), (p["url"], p["title"])], ptype="Article")

PAGES["/blog/"] = page("/blog/", "SOC 2 & AI Governance Blog | Secblox",
 "Practical guides on SOC 2, ISO 42001, NIST AI RMF and the EU AI Act for SaaS and AI companies.",
 f'''<div class="page-hero"><div class="wrap">{{{{CRUMBS}}}}<span class="eyebrow">Blog</span><h1>Guides on SOC 2 and <em>AI governance</em>.</h1><p class="lead">Practical, practitioner-written guidance for founders, CTOs and security leads.</p>
<p style="font-size:14px;color:var(--muted)">Prefer a feed reader? Add <code>https://secblox.io/feed.xml</code> to Feedly, Inoreader or Outlook.</p></div></div>
<section><div class="wrap"><h2>All articles</h2><p class="sub">{len(POSTS)} guides and counting.</p><div class="grid g3">{"".join(post_card(p) for p in POSTS)}</div></div></section>''',
 schema=[{"@type": "Blog", "name": "Secblox Blog", "url": SITE["domain"] + "/blog/",
          "blogPost": [{"@type": "BlogPosting", "headline": p["title"], "url": SITE["domain"] + p["url"], "datePublished": p["date"]} for p in POSTS]}],
 crumbs=[("/blog/", "Blog")], ptype="CollectionPage")

def rss():
    d = SITE["domain"]
    items = "".join(
        f"<item><title>{esc(p['title'])}</title><link>{d}{p['url']}</link><guid>{d}{p['url']}</guid>"
        f"<pubDate>{format_datetime(datetime.datetime.fromisoformat(p['date']).replace(tzinfo=datetime.timezone.utc))}</pubDate>"
        f"<description>{esc(p['desc'])}</description></item>" for p in POSTS)
    return (f'<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom"><channel>'
            f'<title>Secblox Blog</title><link>{d}/blog/</link><description>SOC 2 and AI governance guides</description>'
            f'<language>en-us</language><atom:link href="{d}/feed.xml" rel="self" type="application/rss+xml"/>{items}</channel></rss>\n')



# ---------------- PRIVACY ----------------
ADS_PRIVACY = ("<h2>Advertising and analytics</h2><p>We use Google Ads conversion tracking to understand which of our ads lead to enquiries. "
               "When you visit from an ad, Google may set cookies and process technical data such as your IP address, browser and the pages you view, "
               "under Google's own privacy policy. We see aggregated results, not your identity. You can manage ad personalisation at "
               "<a href=\"https://adssettings.google.com\" rel=\"noopener\">adssettings.google.com</a> or block cookies in your browser.</p>"
               if SITE["google_ads_id"] else "<p>This site does not use tracking cookies or third-party analytics.</p>")
ADS_PRIVACY += ("<h2>Booking calls</h2><p>Calls are scheduled through Cal.com, which processes the details you enter when booking "
                "under its own privacy policy.</p>")
PAGES["/privacy-policy/"] = page("/privacy-policy/", "Privacy Policy | Secblox",
 "How Secblox handles personal information shared through this website and by email.",
 f'''<div class="page-hero"><div class="wrap">{{{{CRUMBS}}}}<h1>Privacy Policy</h1><p class="lead">Last updated: {TODAY}</p></div></div>
<section><div class="wrap prose">
<h2>Who we are</h2><p>This website is operated by Secblox. Contact: <a href="mailto:{SITE["email"]}">{SITE["email"]}</a>.</p>
<h2>What we collect</h2><p>This site does not use forms. If you email us or book a call, we receive your name, email address and whatever you choose to include.</p>
{ADS_PRIVACY}
<h2>How we use it</h2><p>We use information you send only to respond to your enquiry and, if we work together, to deliver our services. We do not sell or rent personal information.</p>
<h2>Retention</h2><p>We keep correspondence only as long as needed for the purpose it was shared and to meet legal or contractual obligations.</p>
<h2>Hosting</h2><p>The site is hosted on GitHub Pages, which may log technical data such as IP addresses for security purposes under GitHub's own privacy statement.</p>
<h2>Your rights</h2><p>You can ask us to access, correct or delete personal information we hold about you by emailing <a href="mailto:{SITE["email"]}">{SITE["email"]}</a>.</p>
</div></section>''', crumbs=[("/privacy-policy/", "Privacy Policy")])

# ---------------- AD LANDING PAGES (noindex; not in sitemap, llms.txt or IndexNow) ----------------
def landing(path, title, desc, eyebrow, h1, lead, gets, steps, why, faqs):
    gets_html = "".join(f'<div class="card"><h3>{esc(t)}</h3><p>{esc(d)}</p></div>' for t, d in gets)
    steps_html = "".join(f'<div class="step"><h3>{esc(t)}</h3><p>{esc(d)}</p></div>' for t, d in steps)
    why_html = "".join(f"<li>{w}</li>" for w in why)
    fh, _ = faq_block(faqs)
    body = f'''<section class="hero"><div class="wrap">
<span class="eyebrow">{esc(eyebrow)}</span><h1>{h1}</h1><p class="lead">{lead}</p>
<div class="cta-row"><a class="btn btn-primary" href="#book">Book a free 30-minute call</a></div>
<div class="trust"><span><b>15+ years</b> in security</span><span><b>Hands-on</b> implementation</span><span><b>AWS · Azure · GCP</b></span><span><b>Remote</b> · US time zones</span></div>
</div></section>
<section><div class="wrap"><h2>What you get</h2><div class="grid g3" style="margin-top:28px">{gets_html}</div></div></section>
<section class="alt"><div class="wrap"><h2>How it works</h2><div class="steps" style="margin-top:28px">{steps_html}</div></div></section>
<section id="book"><div class="wrap"><h2>Book your free call</h2>
<p class="sub" style="margin-bottom:20px">Pick a time that suits you — the calendar shows your local time zone. If it doesn't load, <a style="text-decoration:underline" href="{SITE["booking"]}" target="_blank" rel="noopener">open the booking page</a>.</p>
<div id="cal-inline" style="width:100%;min-height:640px;border:1px solid var(--line);border-radius:14px;overflow:auto;background:var(--card)"></div></div>{CAL_EMBED}</section>
<section class="alt"><div class="wrap grid g2" style="align-items:start">
<div><h2>Why Secblox</h2><ul class="prose" style="padding-left:22px;margin-top:16px;color:#c9d2e3">{why_html}</ul></div>
<div><h2>Questions</h2><div style="margin-top:16px">{fh}</div></div></div></section>'''
    return page(path, title, desc, body, noindex=True, minimal=True)

WHY = ["Practitioner-led: you work directly with a consultant who has taken SaaS platforms from readiness to report and through renewals.",
       "We implement the controls with your team — not just a gap report.",
       "Platform-agnostic and budget-conscious: tooling sized to your stage.",
       "Penetration testing in-house, so findings feed straight into your evidence.",
       "Fully remote, with meeting times that work for US teams."]

LANDING = {}
LANDING["/lp/soc-2-readiness/"] = landing("/lp/soc-2-readiness/",
 "SOC 2 Readiness for SaaS Startups | Secblox",
 "Get audit-ready for SOC 2 with hands-on help: gap assessment, policies, controls and auditor support. Book a free 30-minute scoping call.",
 "SOC 2 for SaaS & AI startups",
 "Get <em>SOC 2-ready</em> without slowing your roadmap.",
 "A customer is asking for your SOC 2 report. We scope it, close the gaps, implement the controls with your team and walk you through the audit — so you can answer “yes” and close the deal.",
 [("Clear scope", "System boundary, Trust Services Criteria and in-scope tools agreed in week one."),
  ("Gap assessment", "A prioritised list of what's missing, with effort estimates — no guesswork."),
  ("Right-sized policies", "A complete policy set written for how your team actually works."),
  ("Controls implemented", "Access, logging, change management, vulnerability management, backups and vendor risk across your cloud."),
  ("Evidence that collects itself", "Automation set up so the Type II window runs smoothly."),
  ("Audit support", "Auditor selection, system description and evidence requests handled.")],
 [("Free scoping call", "30 minutes: your deadline, stack and likely gaps."),
  ("Readiness", "Gap assessment, policies and control implementation."),
  ("Audit", "Type I if you need it fast, then Type II."),
  ("Renewal", "Recurring controls kept running year after year.")],
 WHY,
 [("How long does SOC 2 take?", "Readiness for a typical SaaS startup takes about 6–10 weeks. A first Type II report usually follows a 3-month or longer observation window."),
  ("What does it cost?", "It depends on scope, team size and how much is already in place. On the call we give you a realistic range for your situation."),
  ("Do we need a compliance automation platform?", "Usually it helps, but not always. We are platform-agnostic and recommend what fits your stage and budget."),
  ("We use AI or LLMs in our product. Is that a problem?", "No — but AI components sit inside your SOC 2 scope. We cover model-provider reviews, prompt change management and data isolation as part of readiness.")])

LANDING["/lp/ai-governance/"] = landing("/lp/ai-governance/",
 "AI Governance & ISO 42001 Readiness | Secblox",
 "Practical AI governance for AI companies: AI inventory, risk assessments, policies and ISO 42001 readiness, aligned to NIST AI RMF and the EU AI Act.",
 "ISO 42001 · NIST AI RMF · EU AI Act",
 "<em>AI governance</em> your enterprise buyers will accept.",
 "Buyers now ask how you govern your AI — training data, model risk, prompt injection, human oversight. We build the program that answers with evidence, on top of the security controls you already have.",
 [("AI inventory", "Every model, AI feature and AI tool, with owners and data flows."),
  ("AI risk assessments", "Security, privacy, accuracy, fairness and legal risk for each system."),
  ("AI policies", "Acceptable use, AI development lifecycle and AI vendor policies."),
  ("Technical controls", "Prompt-injection defences, data isolation, change management and monitoring."),
  ("EU AI Act readiness", "Role, risk classification and transparency obligations mapped to your products."),
  ("ISO 42001 readiness", "An AI Management System ready for certification, reusing your SOC 2 work.")],
 [("Free scoping call", "30 minutes: your AI systems, buyers' questions and deadlines."),
  ("Assess", "AI inventory plus a NIST AI RMF-aligned gap assessment."),
  ("Build", "Policies, controls and evidence; questionnaire-ready answers."),
  ("Certify", "ISO 42001 internal audit and certification support, if you need a certificate.")],
 WHY,
 [("Do we need ISO 42001?", "Not always. Many companies start with a NIST AI RMF-aligned program and move to ISO 42001 when customers ask for a certificate."),
  ("Does the EU AI Act apply to US companies?", "It can, if your AI system is offered in the EU or its output is used there. We help you work out your role and obligations alongside your legal counsel."),
  ("We already have SOC 2. Do we start again?", "No. Access control, change management, vendor risk and incident response carry over; we add the AI-specific pieces."),
  ("How long does it take?", "An initial AI governance program typically takes around 90 days; ISO 42001 certification depends on scope and existing maturity.")])

# ---------------- REDIRECTS (old WordPress URLs -> new pages) ----------------
REDIRECTS = {
    "/contact-us/": "/contact/",
    "/privacy-policy-2/": "/privacy-policy/",
    "/service-post/compliance/": "/soc-2-compliance/",
    "/service-post/cloud-security/": "/services/cloud-security-assessment/",
    "/service-post/security-architecture/": "/services/cloud-security-assessment/",
    "/service-post/cyber-security/": "/services/penetration-testing/",
    "/service-post/disaster-planning/": "/soc-2-compliance/",
    "/service-post/secure-awareness-training/": "/soc-2-compliance/",
    "/service-post/secure-managed-it/": "/",
    "/cloud-security/": "/services/cloud-security-assessment/",
    "/security-in-a-fragment-world-of-workload/": "/blog/",
    "/security-in-a-fragment-world-of-workload-for-your-business-2/": "/blog/",
}

def redirect_page(target):
    t = SITE["domain"] + target
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Moved</title>'
            f'<link rel="canonical" href="{t}">'
            f'<meta http-equiv="refresh" content="0; url={target}"><script>location.replace("{target}")</script></head>'
            f'<body><p>This page has moved to <a href="{target}">{t}</a>.</p></body></html>')

# ---------------- BUILD ----------------
def build():
    if os.path.exists(OUT): shutil.rmtree(OUT)
    os.makedirs(OUT)
    shutil.copytree("assets", f"{OUT}/assets")
    latest = ('<section><div class="wrap"><h2>Latest from the blog</h2><p class="sub">Practical guides on SOC 2 and AI governance.</p><div class="grid g3">'
              + "".join(post_card(p) for p in POSTS[:3]) + '</div><p style="margin-top:28px"><a class="btn btn-ghost" href="/blog/">All articles →</a></p></div></section>') if POSTS else ""
    PAGES["/"] = PAGES["/"].replace("{LATEST}", latest)
    for path, content in PAGES.items():
        d = OUT + path
        os.makedirs(d, exist_ok=True)
        open(d + "index.html", "w").write(content)
    for path, content in LANDING.items():  # ad landing pages: built but kept out of sitemap/llms/IndexNow
        os.makedirs(OUT + path, exist_ok=True)
        open(OUT + path + "index.html", "w").write(content)
    for old, new in REDIRECTS.items():
        os.makedirs(OUT + old, exist_ok=True)
        open(OUT + old + "index.html", "w").write(redirect_page(new))
    # 404
    open(f"{OUT}/404.html", "w").write(page("/404.html", "Page not found | Secblox", "The page you were looking for doesn't exist.",
        '<section class="hero"><div class="wrap"><h1>Page not found</h1><p class="lead">That page has moved or never existed.</p><a class="btn btn-primary" href="/">Go home</a></div></section>', noindex=True))
    # favicon
    shutil.copy("assets/favicon-32.png", f"{OUT}/favicon.ico")  # browsers that request /favicon.ico get the PNG
    # sitemap
    pri = {"/": "1.0"}
    pdates = {p["url"]: p["date"] for p in POSTS}
    urls = "".join(f"<url><loc>{SITE['domain']}{p}</loc><lastmod>{pdates.get(p, TODAY)}</lastmod></url>" for p in PAGES)
    open(f"{OUT}/feed.xml", "w").write(rss())
    open(f"{OUT}/sitemap.xml", "w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
    bots = ["Googlebot", "Bingbot", "OAI-SearchBot", "ChatGPT-User", "GPTBot", "Claude-SearchBot", "Claude-User", "ClaudeBot",
            "PerplexityBot", "Perplexity-User", "Google-Extended", "Applebot", "DuckDuckBot"]
    robots = "".join(f"User-agent: {b}\nAllow: /\n\n" for b in bots) + "User-agent: *\nAllow: /\n\n"
    open(f"{OUT}/robots.txt", "w").write(robots + f"Sitemap: {SITE['domain']}/sitemap.xml\n")
    open(f"{OUT}/{SITE['indexnow_key']}.txt", "w").write(SITE["indexnow_key"])
    # llms-full.txt: full plain-text of every blog post for AI assistants
    full = [f"# {SITE['name']} — full content", f"> {SITE['tagline']}. Website: {SITE['domain']}. Contact: {SITE['email']}. Book a call: {SITE['booking']}", ""]
    for p in POSTS:
        txt = re.sub(r"<[^>]+>", "", p["html"]); txt = html.unescape(re.sub(r"\n{3,}", "\n\n", txt))
        full += [f"## {p['title']}", f"URL: {SITE['domain']}{p['url']} | Published: {p['date']}", "", txt.strip(), ""]
    open(f"{OUT}/llms-full.txt", "w").write("\n".join(full))
    open(f"{OUT}/CNAME", "w").write(SITE["domain"].replace("https://", "") + "\n")
    open(f"{OUT}/.nojekyll", "w").write("")
    # llms.txt for AI search engines
    lines = [f"# {SITE['name']}", f"> {SITE['tagline']}. SOC 2 readiness, AI governance (NIST AI RMF, EU AI Act), ISO/IEC 42001, penetration testing and cloud security assessments.", ""]
    lines += [f"- [{p}]({SITE['domain']}{p})" for p in PAGES]
    open(f"{OUT}/llms.txt", "w").write("\n".join(lines) + "\n")
    print(f"Built {len(PAGES)} pages into ./{OUT}")

if __name__ == "__main__":
    build()
