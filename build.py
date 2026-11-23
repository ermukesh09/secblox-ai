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
    "linkedin_personal": "https://www.linkedin.com/in/mukeshbhakar/",
    "indexnow_key": "2a4b273c96120af49169c533023737c6",  # IndexNow key (public by design; served at /<key>.txt)  # <-- your LinkedIn
    "tagline": "SOC 2 & AI Governance for SaaS and AI Companies",
    # Google Ads conversion tracking — leave blank to disable all tracking.
    "ga4_id": "G-QLRDW036PD",  # Google Analytics 4 property (secblox.io)
    "google_ads_id": "AW-18579239124",  # Google Ads account 839-854-9045
    "ads_label_booking": "KieaCN_5_LodENThoptF",  # "Booked call" (primary)
    "ads_label_click": "W5KeCI6W_bodENThoptF",
  "brevo_form_action": "https://2ba31f1a.sibforms.com/serve/MUIFABKPg0jcW0xgwwUqQL5n_mcraInvHJwhqEdNVY0DbaPYnGwsW-7flRUaHe3d5WLgWNCH3V7TVAR7E5aSMwxFtu4aGsEA6ZRjWG2cndjketLoW4IINa6qZ4eCEBZijkW141Fe7QETnjWXTpdw39OXy3Ea-VulNpfw4BIsL7rMG8jRynsrJU3DWBdS6Fj6475sf2GX_IeJSfPqug==",  # "Clicked Book a call" (secondary)
}
OUT = "site"
TODAY = datetime.date.today().isoformat()
PAGES_UPDATED = "2026-11-22"  # bump when service/static page content changes (used in sitemap + schema)

NAV = [("/soc-2-compliance/", "SOC 2"), ("/ai-governance/", "AI Governance"),
       ("/iso-42001/", "ISO 42001"), ("/soc-2-for-ai-companies/", "SOC 2 for AI"),
       ("/soc-2-readiness-checklist/", "Readiness Check"), ("/blog/", "Blog"), ("/mukesh-bhakar/", "About")]

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

def iso_dt(d):
    """Schema.org dates as full ISO 8601 datetimes (Google flags date-only values on some types)."""
    return d if "T" in d else f"{d}T09:00:00+05:30"

def page(path, title, desc, body, schema=None, crumbs=None, ptype="WebPage", noindex=False, minimal=False, modified=None, alt_md=None):
    yr = datetime.date.today().year
    if minimal:
        footer_html = (f'<footer><div class="wrap"><div class="copy" style="border-top:0;padding-top:0"><span>© {yr} Secblox · '
                       f'<a href="mailto:{SITE["email"]}">{SITE["email"]}</a></span><span><a href="/privacy-policy/">Privacy Policy</a> · '
                       f'<a href="{SITE["linkedin"]}" rel="noopener">LinkedIn</a></span></div></div></footer>')
    else:
        footer_html = f'''<footer><div class="wrap">
<div class="foot">
<div><a class="logo" href="/">{LOGO_SVG}<span class="wordmark">Secblox</span></a><p style="margin-top:14px;max-width:340px">SOC 2 and AI governance for SaaS and AI companies. Practitioner-led readiness, implementation and audit support.</p></div>
<div><h3 class="fh">Services</h3><ul><li><a href="/soc-2-compliance/">SOC 2 Compliance</a></li><li><a href="/soc-2-readiness-checklist/">Free SOC 2 Readiness Check</a></li><li><a href="/ai-governance/">AI Governance</a></li><li><a href="/iso-42001/">ISO 42001 Readiness</a></li><li><a href="/soc-2-for-ai-companies/">SOC 2 for AI Companies</a></li><li><a href="/services/penetration-testing/">Penetration Testing</a></li><li><a href="/services/cloud-security-assessment/">Cloud Security Assessment</a></li></ul></div>
<div><h3 class="fh">Frameworks</h3><ul><li><a href="/ai-governance/#nist-ai-rmf">NIST AI RMF</a></li><li><a href="/ai-governance/#eu-ai-act">EU AI Act</a></li><li><a href="/iso-42001/">ISO/IEC 42001</a></li><li><a href="/soc-2-compliance/#trust-services-criteria">SOC 2 TSC</a></li></ul></div>
<div><h3 class="fh">Company</h3><ul><li><a href="/mukesh-bhakar/">About Mukesh Bhakar</a></li><li><a href="/blog/">Blog</a></li><li><a href="/contact/">Contact</a></li><li><a href="/privacy-policy/">Privacy Policy</a></li><li><a href="mailto:{SITE["email"]}">{SITE["email"]}</a></li><li><a href="{SITE["linkedin"]}" rel="noopener">LinkedIn</a></li></ul></div>
</div>
<div class="copy"><span>© {yr} Secblox. All rights reserved.</span><span>SOC 2 · ISO/IEC 42001 · NIST AI RMF · EU AI Act</span></div>
</div></footer>'''
    d = SITE["domain"]; url = d + path
    graph = [org_schema(), {"@type": "WebSite", "@id": d + "/#website", "url": d + "/", "name": SITE["name"],
                            "publisher": {"@id": d + "/#org"}},
             {"@type": "WebPage" if ptype == "Article" else ptype, "@id": url + "#page", "url": url, "name": title, "description": desc,
              "isPartOf": {"@id": d + "/#website"}, "inLanguage": "en-US", "dateModified": iso_dt(modified or PAGES_UPDATED)}
             | ({"mainEntity": {"@id": d + "/#mukesh"}} if ptype == "ProfilePage" else {})]
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
{f'<link rel="alternate" type="text/markdown" href="{d}{alt_md}">' + chr(10) if alt_md else ""}<meta name="theme-color" content="#070b14">
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
{footer_html}
<script>const b=document.querySelector('.menu-btn'),m=document.getElementById('menu');if(b)b.onclick=()=>{{const o=m.classList.toggle('open');b.setAttribute('aria-expanded',o)}};</script>
</body>
</html>'''

def tracking_head():
    """GA4 + Google Ads tag + conversion events. Emits nothing unless an ID is set."""
    aw = SITE["google_ads_id"]
    ga = SITE.get("ga4_id", "")
    if not aw and not ga:
        return ""
    click = f"'{aw}/{SITE['ads_label_click']}'" if SITE["ads_label_click"] else "null"
    book = f"'{aw}/{SITE['ads_label_booking']}'" if SITE["ads_label_booking"] else "null"
    first = ga or aw
    ga_js = f"'{ga}'" if ga else "null"
    configs = "".join(f"gtag('config','{i}');" for i in (ga, aw) if i)
    return f"""<script async src="https://www.googletagmanager.com/gtag/js?id={first}"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());{configs}
window.SBX_CONV={{click:{click},book:{book},ga:{ga_js}}};
function sbxGA(n,p){{try{{if(SBX_CONV.ga)gtag('event',n,Object.assign({{send_to:SBX_CONV.ga}},p||{{}}));}}catch(e){{}}}}
var sbxClicked=false;document.addEventListener('click',function(e){{var a=e.target.closest&&e.target.closest('a[href*="cal.com/"],a[href="#book"]');if(a&&!sbxClicked){{sbxClicked=true;if(SBX_CONV.click)gtag('event','conversion',{{send_to:SBX_CONV.click}});sbxGA('book_call_click',{{link_text:(a.textContent||'').trim().slice(0,60),link_type:a.getAttribute('href')==='#book'?'on_page_calendar':'cal_com'}});}}}});</script>"""

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
<div class="cta-row"><a class="btn btn-primary" href="{SITE["booking"]}" target="_blank" rel="noopener">Book a free scoping call</a><a class="btn btn-ghost" href="/soc-2-readiness-checklist/">Take the free SOC 2 readiness check →</a></div>
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
PAGES["/soc-2-compliance/"] = page("/soc-2-compliance/", "SOC 2 Compliance & Audit Readiness Consulting | Secblox",
 "SOC 2 consulting and audit preparation for SaaS and AI startups: gap assessment, controls, policies, evidence and audit support for Type I and II.",
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

<h2>SOC 2 guides</h2>
<ul><li><a href="/blog/soc-2-cost-for-startups/">SOC 2 cost for startups: audit, tools and budget</a></li>
<li><a href="/blog/soc-2-audit-process/">The SOC 2 audit process, step by step</a></li>
<li><a href="/blog/how-to-choose-a-soc-2-auditor/">How to choose a SOC 2 auditor</a></li>
<li><a href="/blog/soc-2-consultant-vs-compliance-platform/">SOC 2 consultant vs compliance platform</a></li>
<li><a href="/blog/soc-2-readiness-assessment/">What a SOC 2 readiness assessment covers</a></li>
<li><a href="/soc-2-readiness-checklist/">Free SOC 2 readiness checklist and self-assessment</a></li></ul>

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
cloud_faqs = [
 ("What is a cloud security assessment?", "A structured review of how your AWS, Azure or Google Cloud environment is configured, accessed, monitored and recovered. It combines automated posture checks with expert review and ends in a prioritised list of fixes, a target architecture and a mapping to SOC 2 controls."),
 ("How long does a cloud security assessment take?", "For a typical SaaS startup with a few cloud accounts, about one to two weeks including the report. Larger multi-account environments, or adding a penetration test, extend that."),
 ("What access do you need?", "Read-only access through a dedicated, time-limited role that is removed when the assessment ends. No write access or long-lived keys are needed for the review."),
 ("Do you only assess, or do you also fix?", "Both. Cloud security consulting continues after the report if you want it: hands-on remediation, posture management set-up, architecture changes and evidence for your SOC 2 audit."),
 ("Do we need a commercial cloud security platform?", "Often not at first. For a startup on one cloud provider, the native tools — AWS Security Hub CSPM, Microsoft Defender for Cloud or Google Security Command Center — usually cover the baseline. We help you decide when a platform is worth the cost."),
 ("How does this help with SOC 2?", "Most SOC 2 security controls for a cloud-native company live in the cloud: access, logging, encryption, change management and backups. Every finding is mapped to the SOC 2 criteria it affects, so fixing it also closes audit gaps."),
]
fh, fs = faq_block(cloud_faqs)
PAGES["/services/cloud-security-assessment/"] = page("/services/cloud-security-assessment/", "Cloud Security Assessment & Consulting | Secblox",
 "Cloud security assessment and consulting for SaaS and AI companies on AWS, Azure and GCP: posture, IAM, logging, architecture and SOC 2 mapping.",
f'''<div class="page-hero"><div class="wrap">{{{{CRUMBS}}}}<span class="eyebrow">AWS · Azure · GCP</span><h1>Cloud security assessment and consulting for <em>SaaS and AI companies</em>.</h1>
<p class="lead">An architecture-level review of your AWS, Azure or Google Cloud environment, mapped to SOC 2 — then hands-on help fixing what matters, which often reduces your cloud bill as well as your risk.</p>
<div class="cta-row"><a class="btn btn-primary" href="{SITE["booking"]}" target="_blank" rel="noopener">Book a cloud review</a></div></div></div>
<section><div class="wrap layout"><article class="prose">
<p><strong>A cloud security assessment is a structured review of how your cloud environment is configured, accessed, monitored and recovered, ending in a prioritised list of fixes.</strong> Our cloud security consulting covers the assessment and the work after it: closing gaps, setting up continuous posture management, improving your architecture and producing evidence your SOC 2 auditor will accept.</p>
<h2>What does the cloud security assessment cover?</h2>
<table><thead><tr><th>Area</th><th>What we review</th></tr></thead><tbody>
<tr><td>Account structure</td><td>Organisation layout, separation of production and non-production, guardrail policies</td></tr>
<tr><td>Identity and access</td><td>SSO, MFA, privileged access, least privilege, unused users, roles and keys</td></tr>
<tr><td>Network exposure</td><td>Segmentation, internet-facing services, open admin ports, ingress and egress controls</td></tr>
<tr><td>Logging and detection</td><td>CloudTrail, AWS Config, GuardDuty, Defender for Cloud, Security Command Center — coverage across every account and region</td></tr>
<tr><td>Data protection</td><td>Encryption at rest and in transit, key management, public storage, secrets handling</td></tr>
<tr><td>Backup and recovery</td><td>Cross-region and cross-account backups, tested restores, RTO and RPO evidence</td></tr>
<tr><td>AI workloads</td><td>Bedrock, Azure OpenAI and Vertex AI access, data flows, prompt and output logging</td></tr>
<tr><td>Cost and hygiene</td><td>Idle and oversized resources that add cost and attack surface</td></tr>
</tbody></table>
<h2>How does the assessment work?</h2>
<ol><li><strong>Scope</strong> — accounts, regions, workloads and the standard to measure against.</li>
<li><strong>Read-only access</strong> — a dedicated, time-limited role for the review.</li>
<li><strong>Automated baseline</strong> — posture checks against the CIS Benchmarks and the provider's best-practice standards.</li>
<li><strong>Expert review</strong> — IAM policies, architecture, data flows and anything automated checks can't judge.</li>
<li><strong>Optional penetration test</strong> — of your application and exposed infrastructure, performed in-house.</li>
<li><strong>Report and walkthrough</strong> — findings ranked by risk, owners, a target architecture and SOC 2 mapping.</li>
<li><strong>Re-test</strong> — confirm critical and high findings are fixed.</li></ol>
<h2>Cloud security consulting beyond the assessment</h2>
<ul><li><strong>Remediation</strong> — hands-on fixes alongside your engineers, not just a report.</li>
<li><strong>Cloud security posture management</strong> — native tooling enabled organisation-wide, tuned, and routed to an owner.</li>
<li><strong>Cloud security architecture</strong> — multi-account structure, central identity, private networking and central logging.</li>
<li><strong>Cloud security compliance</strong> — controls mapped to SOC 2, ISO 27001 and GDPR, with evidence collected automatically.</li></ul>
<h2>Deliverables</h2>
<p>A prioritised findings report with remediation steps, a target architecture, a SOC 2 control mapping and a re-test letter — plus hands-on remediation support if you want it. See also our <a href="/services/penetration-testing/">penetration testing</a> and <a href="/soc-2-compliance/">SOC 2 compliance</a> services.</p>
<h2>Cloud security guides</h2>
<ul><li><a href="/blog/aws-security-assessment/">AWS security assessment: checklist and process</a></li>
<li><a href="/blog/cloud-security-posture-management/">Cloud security posture management (CSPM) for startups</a></li>
<li><a href="/blog/cloud-security-compliance/">Cloud security compliance for SaaS companies</a></li>
<li><a href="/blog/cloud-security-architecture/">Cloud security architecture for SaaS startups</a></li></ul>
<h2>FAQ</h2>
{fh}
</article>{aside()}</div></section>{cta("Want a clear view of your cloud risk?", "Book a free 30-minute scoping call. We'll talk through your cloud setup, likely gaps and what an assessment would cover — no obligation.")}''',
 schema=[service_schema("Cloud Security Assessment and Consulting", "Cloud security assessment and consulting for AWS, Azure and GCP, mapped to SOC 2.", "/services/cloud-security-assessment/", "Cloud security consulting"), fs],
 crumbs=[("/services/cloud-security-assessment/", "Cloud Security Assessment")])

# ---------------- ABOUT ----------------
MUKESH_FAQ = [
 ("Are you a SOC 2 auditor?", "No. Only licensed CPA firms can perform SOC 2 audits and issue reports. I prepare your company for the audit — scoping, implementing controls, policies and evidence — and support you through it with your chosen auditor."),
 ("Do I need a specific compliance platform to work with you?", "No. I'm platform-agnostic: I work inside the compliance automation platform you already use, or help you choose one sized to your stage and budget — including when you don't need one yet."),
 ("Which companies do you work with?", "SaaS and AI companies in the US and UK — typically startups and scale-ups that need SOC 2 for enterprise deals, or that are being asked how they govern their AI."),
 ("What happens on the first call?", "A free 30-minute conversation about your product, cloud, deadline and customer requirements. You leave with a clear scope, a realistic timeline and a budget range — no sales pitch."),
]
_mfh, _mfsch = faq_block(MUKESH_FAQ)
PAGES["/mukesh-bhakar/"] = page("/mukesh-bhakar/", "Mukesh Bhakar — SOC 2 & AI Governance Consultant | Secblox",
 "Mukesh Bhakar is a hands-on SOC 2 and AI governance consultant helping SaaS and AI companies get audit-ready, stay compliant and pass security reviews.",
f'''<div class="page-hero"><div class="wrap profile-hero">
<div><div>{{{{CRUMBS}}}}</div><span class="eyebrow">Founder & Principal Consultant, Secblox</span>
<h1>Mukesh Bhakar — <em>SOC 2 & AI governance</em> consultant</h1>
<p class="lead"><strong>I help SaaS and AI companies get SOC 2-ready, keep it running and answer the AI governance questions enterprise buyers now ask.</strong> Hands-on implementation — not slide decks — with tooling sized to your budget.</p>
<div class="cta-row"><a class="btn btn-primary" href="/contact/">Book a free 30-minute call</a><a class="btn btn-ghost" href="/soc-2-readiness-checklist/">Take the SOC 2 readiness check →</a></div>
<p style="margin-top:18px;font-size:15px"><a style="text-decoration:underline" href="{SITE["linkedin_personal"]}" rel="noopener me">Connect with Mukesh on LinkedIn</a></p></div>
<img class="profile-photo" src="/assets/mukesh-bhakar.jpg" srcset="/assets/mukesh-bhakar-320.jpg 320w, /assets/mukesh-bhakar.jpg 600w" sizes="(max-width: 760px) 220px, 320px" width="320" height="320" alt="Mukesh Bhakar, SOC 2 and AI governance consultant and founder of Secblox">
</div></div>
<section><div class="wrap"><h2>What I help with</h2><div class="grid g3" style="margin-top:28px">
<div class="card"><h3>SOC 2, readiness to report</h3><p>Scoping, gap assessment, policies, control implementation and audit support for Type I and Type II.</p></div>
<div class="card"><h3>Renewals & continuous compliance</h3><p>Keeping controls and evidence running all year so every renewal is routine, not a new project.</p></div>
<div class="card"><h3>AI governance</h3><p>AI inventory, risk assessments and policies aligned to ISO/IEC 42001, NIST AI RMF and the EU AI Act.</p></div>
<div class="card"><h3>Cloud security</h3><p>Security assessments and architecture across AWS, Azure and GCP — identity, logging, backups and disaster recovery.</p></div>
<div class="card"><h3>Penetration testing</h3><p>Performed directly, not subcontracted, so findings feed straight into your SOC 2 evidence.</p></div>
<div class="card"><h3>Security programs from zero</h3><p>Standing up the core controls — identity, endpoint, email security, device management — where little exists yet.</p></div>
</div></div></section>
<section class="alt"><div class="wrap layout"><article class="prose">
<h2>Experience</h2>
<ul>
<li><strong>15+ years in security</strong> across cloud security architecture, identity, endpoint security and compliance.</li>
<li>Takes <strong>SaaS platforms on AWS through SOC 2 end to end</strong> — readiness, the audit report and annual renewals — including cost savings in the cloud environments along the way.</li>
<li>Has <strong>built security programs from zero</strong>: EDR, email security, identity controls and device management where no security tooling existed.</li>
<li>Runs <strong>business continuity and disaster recovery testing</strong> for SOC 2, including cross-region recovery tests with documented RTO/RPO evidence.</li>
<li>Hands-on with <strong>identity and access management, DLP, EDR, email security and SASE/CASB</strong>, and with the leading compliance automation platforms.</li>
<li>Framework experience: <strong>SOC 2, GDPR and NIST</strong>, with a focus on AI security and governance — <strong>ISO/IEC 42001, NIST AI RMF, MITRE ATLAS and the EU AI Act</strong>.</li>
</ul>
<h2>How I work</h2>
<ul><li><strong>Hands-on</strong> — I configure the controls, not just recommend them.</li>
<li><strong>Budget-conscious</strong> — tooling sized to your stage; I'll tell you when you don't need to buy something.</li>
<li><strong>Security first, compliance as proof</strong> — controls that reduce real risk, with evidence as a by-product.</li>
<li><strong>Direct</strong> — you work with me, not a rotating team of juniors.</li></ul>
<h2>Ways to work together</h2>
<table><thead><tr><th>Engagement</th><th>Best for</th></tr></thead><tbody>
<tr><td><strong>SOC 2 readiness project</strong></td><td>Getting from "a customer asked for our report" to audit-ready, with controls implemented</td></tr>
<tr><td><strong>Ongoing compliance support</strong></td><td>Keeping SOC 2 running between audits and handling renewals</td></tr>
<tr><td><strong>AI governance program</strong></td><td>Answering buyers' AI questions and preparing for ISO/IEC 42001</td></tr>
<tr><td><strong>One-off assessments</strong></td><td>Penetration tests, cloud security assessments and readiness assessments</td></tr>
</tbody></table>
<h2>Writing</h2>
<p>Practical guides on <a href="/blog/soc-2-cost-for-startups/">what SOC 2 costs</a>, <a href="/blog/soc-2-audit-process/">how the audit works</a>, <a href="/blog/soc-2-consultant-vs-compliance-platform/">consultants vs compliance platforms</a> and <a href="/blog/iso-42001-vs-nist-ai-rmf/">ISO 42001 vs NIST AI RMF</a> — all on the <a href="/blog/">Secblox blog</a>.</p>
<h2>Frequently asked questions</h2>{_mfh}
</article>{aside()}</div></section>{cta("Let's talk about your SOC 2 or AI governance plans", "Book a free 30-minute call with me. You'll leave with a clear scope, a realistic timeline and a budget range — no sales pitch.")}''',
 schema=[{"@type": "Person", "@id": SITE["domain"] + "/#mukesh", "name": "Mukesh Bhakar",
          "jobTitle": "Founder & Principal Consultant", "url": SITE["domain"] + "/mukesh-bhakar/", "image": SITE["domain"] + "/assets/mukesh-bhakar.jpg",
          "worksFor": {"@id": SITE["domain"] + "/#org"}, "sameAs": [SITE["linkedin_personal"], SITE["linkedin"]],
          "knowsAbout": ["SOC 2", "AI governance", "ISO/IEC 42001", "NIST AI RMF", "EU AI Act", "GDPR", "Cloud security", "Penetration testing"]},
         _mfsch],
 crumbs=[("/mukesh-bhakar/", "Mukesh Bhakar")], ptype="ProfilePage")


CAL_EMBED = """<script>
(function(){function load(){(function (C, A, L) { let p = function (a, ar) { a.q.push(ar); }; let d = C.document; C.Cal = C.Cal || function () { let cal = C.Cal; let ar = arguments; if (!cal.loaded) { cal.ns = {}; cal.q = cal.q || []; d.head.appendChild(d.createElement("script")).src = A; cal.loaded = true; } if (ar[0] === L) { const api = function () { p(api, arguments); }; const namespace = ar[1]; api.q = api.q || []; if (typeof namespace === "string") { cal.ns[namespace] = cal.ns[namespace] || api; p(cal.ns[namespace], ar); p(cal, ["initNamespace", namespace]); } else p(cal, ar); return; } p(cal, ar); }; })(window, "https://app.cal.com/embed/embed.js", "init");
Cal("init", "30min", {origin: "https://app.cal.com"});
Cal.ns["30min"]("inline", {elementOrSelector: "#cal-inline", config: {layout: "month_view", theme: "dark"}, calLink: "mukesh-bhakar-vzmbyl/30min"});
Cal.ns["30min"]("ui", {theme: "dark", hideEventTypeDetails: false, layout: "month_view", cssVarsPerTheme: {dark: {"cal-brand": "#3ee6c4"}}});
var sent=false;function conv(){if(sent)return;sent=true;if(window.gtag&&window.SBX_CONV&&SBX_CONV.book)gtag('event','conversion',{send_to:SBX_CONV.book});if(window.sbxGA)sbxGA('booked_call',{method:'cal_embed'});}
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

REFS = [  # official sources auto-cited on posts that mention them (keyword match, case-insensitive)
    (("soc 2",), "AICPA — 2017 Trust Services Criteria (revised points of focus, 2022)",
     "https://www.aicpa-cima.com/resources/download/2017-trust-services-criteria-with-revised-points-of-focus-2022"),
    (("42001",), "ISO/IEC 42001:2023 — Artificial intelligence management system (ISO)", "https://www.iso.org/standard/81230.html"),
    (("ai rmf", "ai risk management framework"), "NIST AI Risk Management Framework (AI RMF 1.0)", "https://www.nist.gov/itl/ai-risk-management-framework"),
    (("generative ai profile", "600-1"), "NIST AI 600-1 — Generative Artificial Intelligence Profile", "https://doi.org/10.6028/NIST.AI.600-1"),
    (("eu ai act", "article 50"), "Regulation (EU) 2024/1689 — the EU Artificial Intelligence Act (EUR-Lex)", "https://eur-lex.europa.eu/eli/reg/2024/1689/oj"),
    (("27001",), "ISO/IEC 27001 — Information security management systems (ISO)", "https://www.iso.org/standard/27001"),
    (("prompt injection",), "OWASP Top 10 for Large Language Model Applications", "https://genai.owasp.org/llm-top-10/"),
    (("security hub", "cspm", "foundational security best practices"), "AWS Security Hub CSPM — AWS Foundational Security Best Practices standard",
     "https://docs.aws.amazon.com/securityhub/latest/userguide/fsbp-standard.html"),
    (("cis aws foundations", "cis amazon web services"), "CIS Amazon Web Services Foundations Benchmark", "https://www.cisecurity.org/benchmark/amazon_web_services"),
    (("shared responsibility",), "AWS Shared Responsibility Model", "https://aws.amazon.com/compliance/shared-responsibility-model/"),
    (("well-architected",), "AWS Well-Architected Framework — Security Pillar", "https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html"),
    (("cloud controls matrix",), "Cloud Security Alliance — Cloud Controls Matrix (CCM)", "https://cloudsecurityalliance.org/research/cloud-controls-matrix/"),
    (("gdpr",), "Regulation (EU) 2016/679 — General Data Protection Regulation (EUR-Lex)", "https://eur-lex.europa.eu/eli/reg/2016/679/oj"),
    (("zero trust for ai agents",), "Anthropic — Zero Trust for AI Agents (guide)", "https://claude.com/resources/guides/zero-trust-for-ai-agents"),
    (("800-207",), "NIST SP 800-207 — Zero Trust Architecture", "https://csrc.nist.gov/pubs/sp/800/207/final"),
    (("aws penetration testing policy",), "AWS Customer Support Policy for Penetration Testing", "https://aws.amazon.com/security/penetration-testing/"),
]
AUTHOR = {"name": "Mukesh Bhakar", "role": "Founder, Secblox",
          "bio": ("Mukesh Bhakar is the founder of Secblox, with 15+ years in security. He works hands-on with SaaS and AI companies "
                  "on SOC 2 — from readiness to the audit report and annual renewals — AI governance (ISO/IEC 42001, NIST AI RMF, "
                  "the EU AI Act), cloud security across AWS, Azure and GCP, and penetration testing."),
          "knows": ["SOC 2", "ISO/IEC 42001", "NIST AI Risk Management Framework", "EU AI Act", "AI governance",
                    "Cloud security", "Penetration testing"]}

def author_schema():
    d = SITE["domain"]
    return {"@type": "Person", "@id": d + "/#mukesh", "name": AUTHOR["name"], "jobTitle": "Founder",
            "url": d + "/mukesh-bhakar/", "image": d + "/assets/mukesh-bhakar.jpg", "sameAs": [SITE["linkedin_personal"]], "worksFor": {"@id": d + "/#org"}, "knowsAbout": AUTHOR["knows"], "description": AUTHOR["bio"]}

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
        low = m.group(2).lower() + " " + meta.get("title", "").lower()
        refs = [(n, u) for keys, n, u in REFS if any(k in low for k in keys)]
        takeaways = [t.strip() for t in meta.get("takeaways", "").split("|") if t.strip()]
        posts.append({"slug": slug, "url": f"/blog/{slug}/", "title": meta["title"], "desc": meta["description"],
                      "date": meta["date"], "tags": [t.strip() for t in meta.get("tags", "").split(",") if t.strip()],
                      "html": html_body, "faqs": faqs, "mins": max(1, round(words / 220)),
                      "updated": meta.get("updated") or meta["date"], "keyword": meta.get("keyword", ""), "refs": refs, "takeaways": takeaways, "md": m.group(2).strip()})
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
    upd = f' · Updated <time datetime="{p["updated"]}">{p["updated"]}</time>' if p["updated"] != p["date"] else ""
    kt = ('<div class="takeaways"><p class="kt-title">Key takeaways</p><ul>' + "".join(f"<li>{esc(t)}</li>" for t in p["takeaways"])
          + '</ul></div>') if p["takeaways"] else ""
    refs_html = ('<h2 id="references">References</h2><ul class="refs">' + "".join(
        f'<li><a href="{u}" rel="noopener" target="_blank">{esc(n)}</a></li>' for n, u in p["refs"]) + "</ul>") if p["refs"] else ""
    author_box = (f'<div class="author-box"><p class="ab-name"><a href="/mukesh-bhakar/">{AUTHOR["name"]}</a> · {AUTHOR["role"]}</p>'
                  f'<p>{esc(AUTHOR["bio"])}</p><p><a href="{SITE["linkedin"]}" rel="noopener">Secblox on LinkedIn</a> · '
                  f'<a href="/contact/">Book a free scoping call</a></p></div>')
    md_url = p["url"].rstrip("/") + ".md"
    PAGES[p["url"]] = page(p["url"], f'{p["title"]} | Secblox', p["desc"],
        f'''<div class="page-hero"><div class="wrap">{{{{CRUMBS}}}}{tags_html}<h1>{esc(p["title"])}</h1><p class="lead">{esc(p["desc"])}</p>
<p style="color:var(--muted);font-size:14px">By <a href="/mukesh-bhakar/">{AUTHOR["name"]}</a>, {AUTHOR["role"]} · Published <time datetime="{p["date"]}">{p["date"]}</time>{upd} · {p["mins"]} min read</p></div></div>
<section><div class="wrap layout"><article class="prose">{kt}{p["html"]}{refs_html}{author_box}</article>{aside('<div class="card"><h3>More articles</h3><p>' + rel_html + '</p></div>')}</div></section>{cta()}''',
        schema=[{"@type": "BlogPosting", "@id": SITE["domain"] + p["url"] + "#article", "headline": p["title"], "description": p["desc"],
                 "datePublished": iso_dt(p["date"]), "dateModified": iso_dt(p["updated"]), "keywords": ", ".join(p["tags"]),
                 "about": [{"@type": "Thing", "name": t} for t in p["tags"]], "inLanguage": "en-US",
                 "wordCount": len(re.sub("<[^>]+>", " ", p["html"]).split()),
                 "author": author_schema(), "publisher": {"@id": SITE["domain"] + "/#org"}, "image": SITE["domain"] + "/assets/og-image.png",
                 "mainEntityOfPage": SITE["domain"] + p["url"]}
                | ({"abstract": " ".join(p["takeaways"])} if p["takeaways"] else {})
                | ({"citation": [{"@type": "CreativeWork", "name": n, "url": u} for n, u in p["refs"]]} if p["refs"] else {})]
               + ([{"@type": "FAQPage", "mainEntity": [
                 {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faqs"]]}] if p["faqs"] else []),
        crumbs=[("/blog/", "Blog"), (p["url"], p["title"])], ptype="Article", modified=p["updated"], alt_md=md_url)

PAGES["/blog/"] = page("/blog/", "SOC 2 & AI Governance Blog | Secblox",
 "Practical guides on SOC 2, ISO 42001, NIST AI RMF and the EU AI Act for SaaS and AI companies: checklists, comparisons, timelines and templates.",
 f'''<div class="page-hero"><div class="wrap">{{{{CRUMBS}}}}<span class="eyebrow">Blog</span><h1>Guides on SOC 2 and <em>AI governance</em>.</h1><p class="lead">Practical, practitioner-written guidance for founders, CTOs and security leads.</p>
<p style="font-size:14px;color:var(--muted)">Prefer a feed reader? Add <code>https://secblox.io/feed.xml</code> to Feedly, Inoreader or Outlook.</p></div></div>
<section><div class="wrap"><h2>All articles</h2><p class="sub">{len(POSTS)} guides and counting.</p><div class="grid g3">{"".join(post_card(p) for p in POSTS)}</div></div></section>''',
 schema=[{"@type": "Blog", "name": "Secblox Blog", "url": SITE["domain"] + "/blog/",
          "blogPost": [{"@type": "BlogPosting", "headline": p["title"], "url": SITE["domain"] + p["url"], "datePublished": iso_dt(p["date"])} for p in POSTS]}],
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



# ---------------- SOC 2 READINESS CHECKLIST (lead magnet; email via Brevo) ----------------
CHECK_ITEMS = [
 ("Scope & governance", "We know which product, systems and Trust Services Criteria will be in scope.", "Define your scope and criteria first — most startups start with Security only."),
 ("Scope & governance", "Security policies are written, approved and acknowledged by staff.", "Write a right-sized policy set and collect staff acknowledgements."),
 ("Scope & governance", "We have a documented risk assessment from the last 12 months.", "Run and document a risk assessment; auditors expect one every year."),
 ("Access control", "SSO and MFA protect production systems and key SaaS tools.", "Enforce SSO and MFA on production and critical SaaS tools."),
 ("Access control", "User access is reviewed at least quarterly, with evidence kept.", "Schedule quarterly access reviews and keep dated evidence."),
 ("Access control", "Joiners and leavers follow a documented onboarding and offboarding process.", "Document onboarding/offboarding and remove leaver access promptly."),
 ("Change & operations", "Code changes are peer-reviewed and production deployments are approved.", "Require pull-request reviews and approvals before production deploys."),
 ("Change & operations", "Logging and alerting cover production infrastructure.", "Centralise logs and alert on security-relevant events."),
 ("Change & operations", "Vulnerability scanning runs regularly and findings are tracked to closure.", "Scan regularly and track findings to closure with target dates."),
 ("Data & resilience", "Customer data is encrypted at rest and in transit.", "Turn on encryption at rest and enforce TLS everywhere."),
 ("Data & resilience", "Backups run automatically and a restore has been tested.", "Automate backups and test a restore — keep the evidence."),
 ("Data & resilience", "We have an incident response plan and have tested it.", "Write an incident response plan and run a tabletop exercise."),
 ("Vendors & people", "We keep a vendor inventory and review critical vendors, including AI/LLM providers.", "Build a vendor inventory and review critical vendors annually."),
 ("Vendors & people", "Staff complete security awareness training.", "Roll out annual security awareness training and track completion."),
 ("Vendors & people", "We have had a penetration test in the last 12 months.", "Book a penetration test scoped to your product and cloud."),
]

def checklist_page():
    groups = {}
    for i, (g, q, _) in enumerate(CHECK_ITEMS):
        groups.setdefault(g, []).append((i, q))
    qhtml = "".join(f'<fieldset class="chk-group"><legend>{esc(g)}</legend>' + "".join(
        f'<label class="chk"><input type="checkbox" name="q{i}" value="1"><span>{esc(q)}</span></label>' for i, q in items)
        + "</fieldset>" for g, items in groups.items())
    gaps_js = json.dumps([g for _, _, g in CHECK_ITEMS])
    faqs = [("What is a SOC 2 readiness checklist?", "A list of the controls and evidence an auditor will expect to see, used to find gaps before the audit starts. This one covers the 15 areas where startups most often fall short."),
            ("Is a high score a guarantee I will pass?", "No. It shows how much of the groundwork is in place. The auditor tests whether each control is designed properly and, for a Type II, operated consistently over the whole period."),
            ("What should I do with my gaps?", "Fix the biggest gaps first — scope, access and evidence collection — then run a fuller <a href=\"/blog/soc-2-readiness-assessment/\">SOC 2 readiness assessment</a> before booking the audit."),
            ("Will you share my email?", "No. We use it to send your results and occasional SOC 2 guidance. You can unsubscribe at any time.")]
    fh, fsch = faq_block(faqs)
    action = SITE["brevo_form_action"]
    body = f'''<div class="page-hero"><div class="wrap">{{{{CRUMBS}}}}<span class="eyebrow">Free tool</span><h1>SOC 2 Readiness Checklist &amp; <em>Self-Assessment</em></h1>
<p class="lead"><strong>Tick what's already in place to see how close you are to a SOC 2 audit.</strong> 15 questions, about 3 minutes — you'll get a readiness score and your top gaps to fix first.</p></div></div>
<section><div class="wrap" style="max-width:860px">
<form id="chk-form" onsubmit="return false">{qhtml}
<div class="cta-row" style="margin-top:28px"><button type="button" class="btn btn-primary" id="chk-next">See my readiness score</button></div></form>
<div id="chk-gate" class="card" style="display:none;margin-top:28px">
<h2 style="font-size:1.4rem">Where should we send your results?</h2>
<p class="sub">Enter your work email to see your score and your top gaps. We'll also send occasional SOC 2 guidance — unsubscribe any time. See our <a style="text-decoration:underline" href="/privacy-policy/">privacy policy</a>.</p>
<form id="chk-email" style="display:flex;gap:12px;flex-wrap:wrap;margin-top:16px">
<label for="chk-mail" class="sr-only">Work email</label>
<input id="chk-mail" type="email" required autocomplete="email" placeholder="you@company.com" style="flex:1;min-width:220px;padding:14px 16px;border-radius:10px;border:1px solid var(--line);background:var(--bg2);color:var(--text);font:inherit">
<button class="btn btn-primary" type="submit">Show my results</button></form></div>
<div id="chk-result" class="card" style="display:none;margin-top:28px" aria-live="polite"></div>
</div></section>
<section class="alt"><div class="wrap prose" style="max-width:860px">
<h2>What does the SOC 2 readiness checklist cover?</h2>
<p>The 15 questions map to the areas auditors test most and where startups most often have gaps: scope and governance, access control, change management and operations, data protection and resilience, and vendors and people. Together they reflect the core of the AICPA Trust Services Criteria for Security.</p>
<h2>How should you read your score?</h2>
<ul><li><strong>13–15:</strong> close to audit-ready — confirm evidence exists for each control and pick an auditor.</li>
<li><strong>8–12:</strong> a solid foundation with focused gaps — a readiness project of a few weeks usually closes them.</li>
<li><strong>0–7:</strong> early stage — start with scope, policies and access control before choosing tools or an auditor.</li></ul>
<p>Next steps: read <a href="/blog/soc-2-readiness-assessment/">what a SOC 2 readiness assessment covers</a>, <a href="/blog/soc-2-audit-process/">how the SOC 2 audit process works</a> and <a href="/blog/soc-2-cost-for-startups/">what SOC 2 costs for startups</a>. Building an AI product? See the <a href="/blog/soc-2-checklist-for-ai-startups/">SOC 2 checklist for AI startups</a>.</p>
<h2>Frequently asked questions</h2>{fh}
</div></section>{cta("Want help closing your gaps?", "Book a free 30-minute scoping call. Bring your score — you'll leave with a clear scope, a realistic timeline and a budget range.")}
<script>
(function(){{
var GAPS={gaps_js},N=GAPS.length,f=document.getElementById('chk-form'),gate=document.getElementById('chk-gate'),res=document.getElementById('chk-result');
document.getElementById('chk-next').onclick=function(){{gate.style.display='block';gate.scrollIntoView({{behavior:'smooth',block:'center'}});document.getElementById('chk-mail').focus();}};
function show(){{
 var yes=0,miss=[];for(var i=0;i<N;i++){{if(f['q'+i].checked)yes++;else miss.push(GAPS[i]);}}
 var band=yes>=13?['Close to audit-ready','Confirm evidence exists for every control, then choose your auditor.']:yes>=8?['Solid foundation, focused gaps','A short readiness project usually closes these gaps.']:['Early stage','Start with scope, policies and access control before choosing tools or an auditor.'];
 var top=miss.slice(0,5).map(function(g){{return '<li>'+g+'</li>';}}).join('');
 res.innerHTML='<p class="eyebrow">Your result</p><h2 style="font-size:2rem;margin:6px 0">'+yes+' / '+N+' — '+band[0]+'</h2><p>'+band[1]+'</p>'+(top?'<h3 style="margin-top:18px">Your top gaps to fix first</h3><ol>'+top+'</ol>':'<p>No gaps flagged — nice work.</p>')+'<div class="cta-row" style="margin-top:18px"><a class="btn btn-primary" href="/contact/">Book a free call to plan your fixes</a></div>';
 gate.style.display='none';res.style.display='block';res.scrollIntoView({{behavior:'smooth',block:'center'}});
}}
document.getElementById('chk-email').onsubmit=function(e){{
 e.preventDefault();var m=document.getElementById('chk-mail').value.trim();if(!m)return;
 var d=new FormData();d.append('EMAIL',m);d.append('email_address_check','');d.append('locale','en');
 try{{fetch({json.dumps(action)},{{method:'POST',mode:'no-cors',body:d}});}}catch(err){{}}
 try{{if(window.gtag){{gtag('event','generate_lead',{{form_name:'soc2_checklist'}});if(window.SBX_CONV&&SBX_CONV.lead)gtag('event','conversion',{{send_to:SBX_CONV.lead}});}}}}catch(err){{}}
 show();
}};
}})();
</script>'''
    return page("/soc-2-readiness-checklist/", "SOC 2 Readiness Checklist & Free Self-Assessment | Secblox",
        "Free SOC 2 readiness checklist and self-assessment: 15 questions, about 3 minutes, with a readiness score and the top gaps to fix before your audit.",
        body, schema=[fsch], crumbs=[("/soc-2-readiness-checklist/", "SOC 2 Readiness Checklist")])

PAGES["/soc-2-readiness-checklist/"] = checklist_page()

# ---------------- PRIVACY ----------------
ADS_PRIVACY = ("<h2>Advertising and analytics</h2><p>We use Google Ads conversion tracking to understand which of our ads lead to enquiries. "
               "When you visit from an ad, Google may set cookies and process technical data such as your IP address, browser and the pages you view, "
               "under Google's own privacy policy. We see aggregated results, not your identity. You can manage ad personalisation at "
               "<a href=\"https://adssettings.google.com\" rel=\"noopener\">adssettings.google.com</a> or block cookies in your browser.</p>"
               if SITE["google_ads_id"] else "<p>This site does not use tracking cookies or third-party analytics.</p>")
ADS_PRIVACY += ("<h2>Booking calls</h2><p>Calls are scheduled through Cal.com, which processes the details you enter when booking "
                "under its own privacy policy.</p>"
                "<h2>Email sign-ups</h2><p>Email addresses entered in our SOC 2 readiness checklist are stored with Brevo, our email service provider, "
                "under its own privacy policy. We use them to send your results and occasional SOC 2 guidance; every email includes an unsubscribe link, "
                "and you can ask us to delete your address at any time.</p>")
PAGES["/privacy-policy/"] = page("/privacy-policy/", "Privacy Policy | Secblox",
 "How Secblox handles personal information shared through this website, our booking calendar, Google Ads measurement and email, and how to contact us.",
 f'''<div class="page-hero"><div class="wrap">{{{{CRUMBS}}}}<h1>Privacy Policy</h1><p class="lead">Last updated: {TODAY}</p></div></div>
<section><div class="wrap prose">
<h2>Who we are</h2><p>This website is operated by Secblox. Contact: <a href="mailto:{SITE["email"]}">{SITE["email"]}</a>.</p>
<h2>What we collect</h2><p>If you email us or book a call, we receive your name, email address and whatever you choose to include. If you use our SOC 2 readiness checklist, we receive the email address you enter; your checklist answers stay in your browser and are not sent to us.</p>
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
<div class="trust"><span><b>Hands-on</b> implementation</span><span><b>Audit support</b> included</span><span><b>In-house</b> pen testing</span><span><b>AWS · Azure · GCP</b></span></div>
</div></section>
<section><div class="wrap"><h2>What you get</h2><div class="grid g3" style="margin-top:28px">{gets_html}</div>
<div class="cta-row" style="margin-top:32px"><a class="btn btn-primary" href="#book">Book a free 30-minute call</a></div></div></section>
<section class="alt"><div class="wrap"><h2>How it works</h2><div class="steps" style="margin-top:28px">{steps_html}</div></div></section>
<section id="book"><div class="wrap"><h2>Book your free call</h2>
<p class="sub" style="margin-bottom:8px"><strong style="color:var(--text)">30 minutes, no sales pitch.</strong> You'll leave with a clear scope, a realistic timeline and a budget range.</p>
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
       "Audit support included: auditor selection, system description and evidence requests handled with you."]

LANDING = {}
LANDING["/lp/soc-2-readiness/"] = landing("/lp/soc-2-readiness/",
 "SOC 2 Readiness for SaaS Startups | Secblox",
 "Get audit-ready for SOC 2 with hands-on help: gap assessment, policies, controls and auditor support. Book a free 30-minute scoping call.",
 "SOC 2 readiness & implementation",
 "Get <em>SOC 2-ready</em> without slowing your roadmap.",
 "A customer is asking for your SOC 2 report. We handle SOC 2 readiness and implementation for SaaS startups: we scope it, close the gaps, implement the controls with your team and walk you through the audit — so you can answer “yes” and close the deal.",
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
 "Buyers now ask how you govern your AI — training data, model risk, prompt injection, human oversight. We handle ISO 42001 implementation, NIST AI RMF assessments and EU AI Act compliance, building the program that answers with evidence on top of the security controls you already have.",
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
    "/feed/": "/feed.xml",
    "/about/": "/mukesh-bhakar/",
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


# ---------------- CONTENT STANDARD CHECK (build fails if a post misses the SEO + LLM standard) ----------------
VENDOR_BLOCKLIST = ["vanta", "sprinto", "scrut", "drata", "secureframe", "thoropass"]
PILLARS = ["/soc-2-compliance/", "/ai-governance/", "/iso-42001/", "/soc-2-for-ai-companies/",
           "/services/penetration-testing/", "/services/cloud-security-assessment/", "/gdpr-compliance/"]

def validate_content():
    errs = []
    for p in POSTS:
        u = p["url"]; md = p["md"]; low = md.lower()
        t = f'{p["title"]} | Secblox'
        if len(t) > 60: errs.append(f"{u}: title {len(t)} chars (max 60 incl. ' | Secblox')")
        if not 120 <= len(p["desc"]) <= 160: errs.append(f"{u}: description {len(p['desc'])} chars (need 120-160)")
        if not re.match(r"^\d{4}-\d{2}-\d{2}$", p["date"]) or not re.match(r"^\d{4}-\d{2}-\d{2}$", p["updated"]):
            errs.append(f"{u}: date/updated must be YYYY-MM-DD")
        if not 3 <= len(p["takeaways"]) <= 5: errs.append(f"{u}: needs 3-5 takeaways (front matter 'takeaways:' separated by |)")
        first = next((l for l in md.splitlines() if l.strip()), "")
        if not first.startswith("**"): errs.append(f"{u}: first paragraph must open with a bolded direct answer")
        if len(p["faqs"]) < 3: errs.append(f"{u}: needs a '## FAQ' with at least 3 '### question' entries")
        if not any(f"]({x})" in md for x in PILLARS): errs.append(f"{u}: must link to a service (pillar) page")
        if len(set(re.findall(r"\]\((/blog/[^)]+)\)", md))) < 2: errs.append(f"{u}: must link to at least 2 other blog posts")
        if "](/contact/)" not in md: errs.append(f"{u}: must end with a link to /contact/")
        if not p["refs"]: errs.append(f"{u}: no official reference matched (add a REFS entry or mention the framework)")
        if len(re.findall(r"^## ", md, re.M)) < 4: errs.append(f"{u}: needs at least 4 H2 sections")
        if re.search(r"^# ", md, re.M): errs.append(f"{u}: no H1 in body (the title is the H1)")
        for v in VENDOR_BLOCKLIST:
            if re.search(rf"\b{v}\b", low + " " + p["title"].lower() + " " + p["desc"].lower()): errs.append(f"{u}: vendor name '{v}' not allowed")
    seen = {}
    for p in POSTS:
        k = p.get("keyword", "").lower()
        if k:
            if k in seen: errs.append(f"{p['url']}: primary keyword '{k}' already used by {seen[k]}")
            seen[k] = p["url"]
    if errs:
        raise SystemExit("CONTENT STANDARD FAILED:\n  - " + "\n  - ".join(errs))
    print(f"Content standard: {len(POSTS)} posts passed")

# ---------------- BUILD ----------------
def build():
    validate_content()
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
    pdates = {p["url"]: p["updated"] for p in POSTS}
    urls = "".join(f"<url><loc>{SITE['domain']}{p}</loc><lastmod>{pdates.get(p, PAGES_UPDATED)}</lastmod></url>" for p in PAGES)
    open(f"{OUT}/feed.xml", "w").write(rss())
    open(f"{OUT}/sitemap.xml", "w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
    bots = ["Googlebot", "Bingbot", "OAI-SearchBot", "ChatGPT-User", "GPTBot", "Claude-SearchBot", "Claude-User", "ClaudeBot",
            "PerplexityBot", "Perplexity-User", "Google-Extended", "Applebot", "DuckDuckBot"]
    robots = "".join(f"User-agent: {b}\nAllow: /\n\n" for b in bots) + "User-agent: *\nAllow: /\n\n"
    open(f"{OUT}/robots.txt", "w").write(robots + f"Sitemap: {SITE['domain']}/sitemap.xml\n")
    open(f"{OUT}/{SITE['indexnow_key']}.txt", "w").write(SITE["indexnow_key"])
    # per-post Markdown copies (for AI assistants) + llms-full.txt
    def post_md(p):
        out = [f"# {p['title']}", "", f"> {p['desc']}", "",
               f"- URL: {SITE['domain']}{p['url']}", f"- Author: {AUTHOR['name']}, {AUTHOR['role']}",
               f"- Published: {p['date']}", f"- Updated: {p['updated']}", ""]
        if p["takeaways"]:
            out += ["## Key takeaways", ""] + [f"- {t}" for t in p["takeaways"]] + [""]
        body = re.sub(r"\]\((/[^)]*)\)", lambda mm: "](" + SITE["domain"] + mm.group(1) + ")", p["md"])
        out += [body, ""]
        if p["refs"]:
            out += ["## References", ""] + [f"- [{n}]({u})" for n, u in p["refs"]] + [""]
        out += ["## About the author", "", AUTHOR["bio"], f"Contact: {SITE['email']} · Book a call: {SITE['booking']}", ""]
        return "\n".join(out)
    full = [f"# {SITE['name']} — full content", f"> {SITE['tagline']}. Website: {SITE['domain']}. Contact: {SITE['email']}. Book a call: {SITE['booking']}", ""]
    for p in POSTS:
        md = post_md(p)
        open(OUT + p["url"].rstrip("/") + ".md", "w").write(md)
        full += [md.replace("\n# ", "\n## ", 1), "---", ""]
    open(f"{OUT}/llms-full.txt", "w").write("\n".join(full))
    open(f"{OUT}/CNAME", "w").write(SITE["domain"].replace("https://", "") + "\n")
    open(f"{OUT}/.nojekyll", "w").write("")
    # llms.txt for AI assistants (llmstxt.org format: title, summary, then linked sections with descriptions)
    def meta_of(h):
        t = re.search(r"<title>(.*?)</title>", h); dd = re.search(r'name="description" content="([^"]*)"', h)
        return html.unescape(t.group(1)).replace(" | Secblox", "") if t else "", html.unescape(dd.group(1)) if dd else ""
    lines = [f"# {SITE['name']}",
             f"> {SITE['tagline']}. Secblox helps US and UK SaaS and AI companies get SOC 2 (readiness to report and renewals), "
             "AI governance (ISO/IEC 42001, NIST AI RMF, EU AI Act), penetration testing and cloud security assessments.", "",
             f"Founded and led by {AUTHOR['name']} (15+ years in security). Fully remote, platform-agnostic, hands-on implementation. "
             f"Contact: {SITE['email']}. Book a call: {SITE['booking']}. LinkedIn: {SITE['linkedin']}", "", "## Services", ""]
    post_urls = {p["url"] for p in POSTS}
    for u, h in PAGES.items():
        if u in post_urls or u in ("/blog/", "/privacy-policy/"): continue
        t, dsc = meta_of(h); lines.append(f"- [{t}]({SITE['domain']}{u}): {dsc}")
    lines += ["", "## Guides", ""]
    lines += [f"- [{p['title']}]({SITE['domain']}{p['url']}): {p['desc']} Markdown: {SITE['domain']}{p['url'].rstrip('/')}.md" for p in POSTS]
    lines += ["", "## Optional", "", f"- [Full text of all guides]({SITE['domain']}/llms-full.txt)",
              f"- [Blog index]({SITE['domain']}/blog/)", f"- [RSS feed]({SITE['domain']}/feed.xml)", f"- [Privacy policy]({SITE['domain']}/privacy-policy/)"]
    open(f"{OUT}/llms.txt", "w").write("\n".join(lines) + "\n")
    # Safety check: fail the build if any template placeholder leaked into the output
    import glob as _g
    leaks = []
    for _f in _g.glob(f"{OUT}/**/*.html", recursive=True):
        _t = open(_f).read()
        for _pat in ("{LOGO_SVG}", "{SITE[", "{CRUMBS}", "{{CRUMBS}}", "{yr}", "{LATEST}", "{body}", "{footer_html}"):
            if _pat in _t: leaks.append(f"{_f}: {_pat}")
        for _j in re.findall(r'<script type="application/ld\+json">(.*?)</script>', _t, re.S):
            if re.search(r'"date(Published|Modified|Created)": "\d{4}-\d{2}-\d{2}"', _j): leaks.append(f"{_f}: date-only schema value (use iso_dt)")
            if '"@type": "ProfilePage"' in _j and '"mainEntity"' not in _j: leaks.append(f"{_f}: ProfilePage without mainEntity")
    if leaks:
        raise SystemExit("TEMPLATE PLACEHOLDER LEAKED INTO SITE:\n  - " + "\n  - ".join(leaks[:20]))
    print(f"Built {len(PAGES)} pages into ./{OUT}")

if __name__ == "__main__":
    build()
