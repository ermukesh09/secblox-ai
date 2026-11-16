# Secblox website — project brief

Owner: Mukesh Bhakar (Secblox). Live site: **https://secblox.io**. Repo: `ermukesh09/secblox-ai` (public).

## What it is
Static, SEO-first marketing site + blog for **Secblox** — SOC 2 and AI governance consulting
(ISO/IEC 42001, NIST AI RMF, EU AI Act) for SaaS and AI companies, with penetration testing and
cloud security assessment as add-on services. Target buyers: US SaaS/AI companies.
It replaced the old WordPress site on secblox.io (Nov 2026).

## Brand rules (must follow)
- Brand name is **Secblox** — never "Secblox AI". Logo mark sits before the wordmark (like Claude's).
- **Never name compliance-automation vendors** (Vanta, Sprinto, Scrut, Drata) or specific security
  tool brands on the public site. Say "platform-agnostic" / "leading compliance automation platforms".
- No invented testimonials, client logos, client counts or statistics. Real facts only:
  15+ years security, AWS/Azure/GCP, hands-on implementation, in-house penetration testing,
  SOC 2 readiness → report → renewals.
- Tone: practitioner, plain-English, budget-conscious, no hype.

## Contact / links
- Email: connect@secblox.io (Hostinger mail)
- Booking: https://cal.com/mukesh-bhakar-vzmbyl/30min (all "Book a call" buttons; inline embed on /contact/)
- LinkedIn: https://www.linkedin.com/company/secblox
- All of these live in the `SITE` block at the top of `build.py`.

## How it works
- `build.py` — settings, page templates and all service-page content. Run `python3 build.py` → `site/`.
- `posts/*.md` — blog posts (front matter: title, description, date, tags, optional `draft: true`).
  File name `YYYY-MM-DD-slug.md` → URL `/blog/slug/`. Template: `posts/_TEMPLATE.md.example`.
- `assets/` — style.css, logo (logo.png 512, logo-96.png, favicons, apple-touch-icon), og-image.png.
- `.github/workflows/deploy.yml` — every push to `main` builds and deploys to GitHub Pages (~1 min).
- Generated automatically: sitemap.xml, robots.txt, feed.xml (RSS), llms.txt, CNAME, 404,
  JSON-LD (ProfessionalService, Service, FAQPage, BreadcrumbList, BlogPosting, Person).
- `REDIRECTS` in build.py maps old WordPress URLs (/contact-us/, /service-post/*, etc.) to new pages.
- Requirements: Python 3 + `markdown` (requirements.txt).

## Pages
/, /soc-2-compliance/, /ai-governance/, /iso-42001/, /soc-2-for-ai-companies/,
/services/penetration-testing/, /services/cloud-security-assessment/, /about/, /contact/,
/blog/ (+ posts), /privacy-policy/.

## SEO conventions
- Title ≤ 60 chars ending "| Secblox"; meta description 120–155 chars; one H1 per page.
- Blog posts: answer the title's question in the first 2–3 sentences; question-style H2s;
  link to the relevant service page; end with a short FAQ when useful.
- Keep Lighthouse at 100 (performance, accessibility, best practices, SEO) — check after changes.

## Hosting / DNS
- GitHub Pages (Source: GitHub Actions), custom domain secblox.io, HTTPS enforced.
- DNS at Hostinger: 4 A records `@` → 185.199.108–111.153; CNAME `www` → ermukesh09.github.io.
  MX, SPF/DKIM/DMARC and autodiscover/autoconfig records belong to Hostinger email — never touch.

## Open to-dos
- [ ] Write first batch of 8–10 blog posts (EU AI Act for US SaaS, does SOC 2 cover OpenAI/LLM
      vendors, ISO 42001 cost & timeline, AI vendor risk questionnaire, prompt-injection controls
      for SOC 2, AI acceptable-use policy, SOC 2 Type I vs Type II for startups, etc.)
- [ ] Google Search Console + Bing Webmaster Tools: verify secblox.io, submit /sitemap.xml
- [ ] Confirm Cal.com inline embed renders on /contact/ (fallback: popup button)
- [ ] Optional: Cal.com username → `secblox`; higher-res / SVG logo
- [ ] Backlinks: LinkedIn company page, Upwork profile, Clutch/GoodFirms listings
