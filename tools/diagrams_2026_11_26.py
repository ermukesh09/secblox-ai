import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
F="/usr/share/fonts/opentype/inter/"
def f(n,s): return ImageFont.truetype(F+n+".otf", s)
BG=(7,11,20); CARD=(17,26,46); LINE=(31,42,68); TEXT=(231,236,245); MUTED=(154,166,191); TEAL=(62,230,196); VIOLET=(124,140,255)
LOGO=Image.open("assets/logo.png").convert("RGBA")
def base(W,H):
    im=Image.new("RGB",(W,H),BG); glow=Image.new("RGB",(W,H),BG); g=ImageDraw.Draw(glow)
    g.ellipse((W-500,-300,W+300,400),fill=(20,60,70)); g.ellipse((-400,H-400,500,H+400),fill=(30,32,80))
    im=Image.blend(im,glow.filter(ImageFilter.GaussianBlur(170)),0.55); d=ImageDraw.Draw(im)
    for x in range(0,W,50): d.line((x,0,x,H),fill=(11,17,30))
    for y in range(0,H,50): d.line((0,y,W,y),fill=(11,17,30))
    return im,d
def brand(im,d,W,H):
    lg=LOGO.resize((38,38)); im.paste(lg,(70,H-78),lg)
    d.text((118,H-76),"Secblox",font=f("InterDisplay-Bold",28),fill=TEXT)
    t="secblox.io"; fw=d.textlength(t,font=f("Inter-SemiBold",24)); d.text((W-70-fw,H-72),t,font=f("Inter-SemiBold",24),fill=TEAL)

# 1. OWASP agentic top 10 -> control
W,H=1200,1320; im,d=base(W,H)
d.text((70,60),"AGENTIC AI SECURITY",font=f("Inter-Bold",24),fill=TEAL)
d.text((70,98),"The 10 agentic risks and the control for each",font=f("InterDisplay-ExtraBold",46),fill=TEXT)
d.text((70,160),"Risk categories from the OWASP Top 10 for Agentic Applications (2026)",font=f("Inter-Medium",22),fill=MUTED)
rows=[("ASI01","Agent goal hijack","Treat all content as untrusted; isolate instructions"),
("ASI02","Tool misuse","Allowlist tools; approval for destructive actions"),
("ASI03","Identity & privilege abuse","Own identity per agent; short-lived, scoped access"),
("ASI04","Agentic supply chain","Vet tools, plugins, MCP servers and models"),
("ASI05","Unexpected code execution","Sandbox code; no production credentials"),
("ASI06","Memory & context poisoning","Scoped, reviewable memory with retention limits"),
("ASI07","Insecure inter-agent comms","Authenticate agents; pass the original requester"),
("ASI08","Cascading failures","Rate, cost and step limits; circuit breakers"),
("ASI09","Human-agent trust exploitation","Show evidence before approval; no blind trust"),
("ASI10","Rogue agents","Monitor behaviour; tested kill switch")]
y=215
for code,risk,ctl in rows:
    d.rounded_rectangle((70,y,1130,y+92),16,fill=CARD,outline=LINE,width=2)
    d.rounded_rectangle((90,y+24,190,y+68),10,fill=(15,45,52))
    cw=d.textlength(code,font=f("Inter-Bold",22)); d.text((140-cw/2,y+33),code,font=f("Inter-Bold",22),fill=TEAL)
    d.text((215,y+16),risk,font=f("Inter-Bold",27),fill=TEXT)
    d.text((215,y+54),"→ "+ctl,font=f("Inter-Medium",21),fill=MUTED)
    y+=102
brand(im,d,W,H); im.save("assets/blog/agentic-ai-security-owasp-top-10.png",optimize=True)

# 2. AI security assessment layers
W,H=1200,1100; im,d=base(W,H)
d.text((70,60),"AI SECURITY ASSESSMENT",font=f("Inter-Bold",24),fill=TEAL)
d.text((70,98),"Six layers we test in an AI product",font=f("InterDisplay-ExtraBold",48),fill=TEXT)
layers=[("Governance","AI inventory, policies, owners, risk register",VIOLET),
("Data","Training, RAG and prompt data; access, retention, leakage",TEAL),
("Model & prompts","System prompts, guardrails, jailbreak and injection resistance",TEAL),
("Application & RAG","Auth, tenant isolation, retrieval permissions, output handling",TEAL),
("Agents & tools","Agent identity, tool permissions, approvals, memory",TEAL),
("Cloud & supply chain","Model endpoints, keys, logging, third-party models and packages",VIOLET)]
y=190
for i,(t,s,c) in enumerate(layers):
    inset=i*0
    d.rounded_rectangle((70,y,1130,y+118),18,fill=CARD,outline=LINE,width=2)
    d.rectangle((70,y+18,78,y+100),fill=c)
    d.text((110,y+22),t,font=f("Inter-Bold",32),fill=TEXT)
    d.text((110,y+70),s,font=f("Inter-Medium",23),fill=MUTED)
    n=str(i+1); d.text((1080,y+36),n,font=f("InterDisplay-Bold",40),fill=LINE if False else (60,74,105))
    y+=132
brand(im,d,W,H); im.save("assets/blog/ai-security-assessment-layers.png",optimize=True)
print("ok")
