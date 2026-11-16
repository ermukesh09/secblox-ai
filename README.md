# Secblox AI — static website + blog

Static, SEO-first site. Hosted free on GitHub Pages and rebuilt automatically every time you push.

## Folder layout
| Path | What it is |
|---|---|
| `posts/` | **Your blog.** One Markdown file per article. |
| `build.py` | Site settings (top of file) + service page content + templates |
| `assets/` | CSS, logo, social preview image |
| `.github/workflows/deploy.yml` | Builds and publishes the site on every push to `main` |
| `site/` | Generated output (not committed — GitHub builds it) |

## Write a new blog post (the everyday workflow)
1. Copy `posts/_TEMPLATE.md.example` to `posts/2026-12-01-your-url-slug.md`
2. Fill in `title`, `description`, `date`, `tags`, write the article in Markdown.
3. Commit and push (or create the file directly on github.com → **Add file → Create new file**).
4. ~1 minute later it is live at `/blog/your-url-slug/`, listed on `/blog/` and the home page,
   added to `sitemap.xml` and `feed.xml`, with Article structured data and related-post links.

Set `draft: true` to keep a post unpublished. You can write posts entirely from the GitHub website or mobile app — no software needed.

## One-time setup on GitHub
1. Create a repo (e.g. `secblox-ai`) and upload/push everything in this folder.
2. Repo → **Settings → Pages → Build and deployment → Source: GitHub Actions**.
3. Push any change (or Actions tab → *Build and deploy site* → Run workflow).
4. Settings → Pages → **Custom domain** → enter your domain → tick **Enforce HTTPS**.

## Domain / DNS (domain stays at Hostinger)
Keep the domain registered at Hostinger; only change DNS records in Hostinger's DNS zone editor:
- Apex (`secblox.io`): four **A** records → `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
- `www`: **CNAME** → `<your-github-username>.github.io`
- Do **not** touch MX records — your Hostinger email keeps working.




## Before launch — edit the `SITE` block in `build.py`
`domain`, `email`, `booking` (Calendly), `linkedin`.

## Test locally (optional)
```
pip install -r requirements.txt
python3 build.py
cd site && python3 -m http.server 8000   # open http://localhost:8000
```

## After launch (SEO checklist)
- Google Search Console + Bing Webmaster Tools: verify, submit `/sitemap.xml`.
- If moving from WordPress on the same domain, add 301 redirects for old URLs that have traffic/backlinks
  (GitHub Pages can't do server redirects — create small redirect pages or keep the old URLs).
- Publish 2–4 posts a month, each answering one specific buyer question.
