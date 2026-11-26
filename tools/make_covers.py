"""Generate 1200x630 cover images for blog posts -> assets/blog/<slug>.png.
Run locally after adding a post:  python3 tools/make_covers.py   (add --force to redo all).
Needs Pillow and the Inter font family (not needed in CI; covers are committed)."""
import glob, os, re, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
FONT_DIRS = ["/usr/share/fonts/opentype/inter/", os.path.expanduser("~/Library/Fonts/"), "/Library/Fonts/"]
def font(name, size):
    for d in FONT_DIRS:
        p = os.path.join(d, name + ".otf")
        if os.path.exists(p): return ImageFont.truetype(p, size)
    raise SystemExit(f"Font {name} not found; install Inter.")
BG=(7,11,20); TEXT=(231,236,245); MUTED=(154,166,191); TEAL=(62,230,196); LINE=(11,17,30)
W, H = 1200, 630
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGO = Image.open(os.path.join(ROOT, "assets/logo.png")).convert("RGBA")

def wrap(d, text, f, maxw):
    lines, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if d.textlength(t, font=f) <= maxw: cur = t
        else: lines.append(cur); cur = w
    if cur: lines.append(cur)
    return lines

def cover(title, kicker, out):
    im = Image.new("RGB", (W, H), BG)
    glow = Image.new("RGB", (W, H), BG); g = ImageDraw.Draw(glow)
    g.ellipse((700, -350, 1500, 350), fill=(20, 60, 70)); g.ellipse((-350, 380, 450, 1000), fill=(30, 32, 80))
    im = Image.blend(im, glow.filter(ImageFilter.GaussianBlur(160)), 0.55); d = ImageDraw.Draw(im)
    for x in range(0, W, 50): d.line((x, 0, x, H), fill=LINE)
    for y in range(0, H, 50): d.line((0, y, W, y), fill=LINE)
    d.text((80, 70), kicker.upper(), font=font("Inter-Bold", 24), fill=TEAL)
    for size in (68, 60, 54, 48, 42):
        f = font("InterDisplay-ExtraBold", size); lines = wrap(d, title, f, W - 160)
        if len(lines) <= 4: break
    y = 120 + (4 - len(lines)) * size * 0.35
    for ln in lines:
        d.text((80, y), ln, font=f, fill=TEXT); y += size * 1.18
    lg = LOGO.resize((40, 40)); im.paste(lg, (80, H - 92), lg)
    d.text((132, H - 89), "Secblox", font=font("InterDisplay-Bold", 30), fill=TEXT)
    t = "secblox.io"; fw = d.textlength(t, font=font("Inter-SemiBold", 26))
    d.text((W - 80 - fw, H - 85), t, font=font("Inter-SemiBold", 26), fill=TEAL)
    im.save(out, optimize=True)

force = "--force" in sys.argv
for f in sorted(glob.glob(os.path.join(ROOT, "posts/*.md"))):
    raw = open(f, encoding="utf-8").read()
    meta = dict(l.split(":", 1) for l in raw.split("---")[1].strip().splitlines() if ":" in l)
    meta = {k.strip(): v.strip() for k, v in meta.items()}
    slug = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", os.path.basename(f)[:-3])
    out = os.path.join(ROOT, "assets/blog", slug + ".png")
    if os.path.exists(out) and not force: continue
    kicker = (meta.get("tags", "Guide").split(",")[0].strip() or "Guide")
    cover(meta["title"], kicker, out); print("cover:", slug)
