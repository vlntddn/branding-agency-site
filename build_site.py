#!/usr/bin/env python3
"""Generates the Studio Dudin static site into ./build (shared header/footer)."""
import os

OUT = os.path.dirname(os.path.abspath(__file__))
EMAIL = "hello@studiodudin.com"
# Google Apps Script web-app URL (form → "Studio Dudin — Site inquiries" sheet + email to EMAIL).
# Empty = the form falls back to composing an email in the visitor's mail app.
FORM_ENDPOINT = "https://script.google.com/macros/s/AKfycbz1nMEwYZVbA4vdsZsjTs1JgqZWeOoLk9m_YjhgDcfxmfBoQBJPPGKQM6UPHVeDYTHi6w/exec"
FORM_BUTTON = "Send" if FORM_ENDPOINT else "Write the email"
GUMROAD = "https://vlntddn.gumroad.com"   # one place to change the store link
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link href="https://fonts.googleapis.com/css2?family=Archivo:ital,wght@0,500;0,700;0,800;1,500;1,700&family=Inter:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">')

NAV = [("index.html", "Home"), ("approach.html", "Approach"), ("work.html", "Work"), ("contact.html", "Contact")]


def head(title, desc):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta name="theme-color" content="#FAFAFA">
{FONTS}
<link rel="icon" type="image/svg+xml" href="images/favicon.svg">
<link rel="icon" type="image/png" sizes="32x32" href="images/favicon-32.png">
<link rel="apple-touch-icon" href="images/apple-touch-icon.png">
<link rel="stylesheet" href="styles.css">
</head>
<body>
"""


def header(active):
    act = ' class="active" aria-current="page"'
    links = "\n".join(
        f'      <a href="{h}"{act if h == active else ""}>{t}</a>'
        for h, t in NAV)
    return f"""
<header class="site">
  <div class="wrap">
    <a href="index.html" class="logo"><img src="brand-assets/lockup-signature-ink.svg" alt="Studio Dudin" width="145" height="48"></a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="main-nav">Menu</button>
    <nav class="main" id="main-nav" aria-label="Main">
{links}
    </nav>
  </div>
</header>
<main>
"""


FOOTER = f"""
</main>
<footer class="site">
  <div class="wrap">
    <div class="foot-top">
      <div>
        <a href="index.html" class="logo"><img src="brand-assets/lockup-signature-paper.svg" alt="Studio Dudin" width="170" height="56"></a>
        <p class="foot-tagline">Brand strategy built with the rigor of a luxury house — sized for where you are now.</p>
      </div>
      <div class="foot-links">
        <a href="mailto:{EMAIL}">{EMAIL}</a>
        <a href="approach.html">Approach</a>
        <a href="work.html">Work</a>
        <a href="approach.html#products">Self-serve products</a>
        <a href="contact.html">Contact</a>
      </div>
    </div>
    <p class="small-print">Valentin Dudin · P.IVA — pending · Milano, Italia · © 2026 Studio Dudin</p>
  </div>
</footer>
<script src="site.js" defer></script>
</body>
</html>
"""


def page(fname, title, desc, body, active=None):
    html = head(title, desc) + header(active or fname) + body + FOOTER
    with open(os.path.join(OUT, fname), "w", encoding="utf-8") as f:
        f.write(html)


def closing(h2="Want a clear read on your brand?", sub=None,
            btn="Book a Positioning Audit", note="€1,200 · 1 week · no obligation beyond the audit itself"):
    sub_html = f'<p class="lede" style="margin-top: var(--space-md);">{sub}</p>' if sub else ""
    note_html = f'<p class="reassure" style="color: rgba(255,255,255,0.66);">{note}</p>' if note else ""
    return f"""
<section class="section-black closing">
  <img src="brand-assets/d-mark-paper.svg" alt="" class="closing-d" aria-hidden="true">
  <div class="wrap">
    <h2>{h2}</h2>
    {sub_html}
    <div class="cta-row">
      <a href="contact.html" class="btn btn-primary">{btn}</a>
    </div>
    {note_html}
  </div>
</section>
"""


# ---------------------------------------------------------------- shared blocks

SERVICES_SHORT = """
    <div class="index-list">
      <div class="index-row">
        <div class="index-num">01</div>
        <div class="index-body">
          <span class="index-timeline">1 week</span>
          <h3 class="index-title">Positioning Audit</h3>
          <p class="index-desc">A fast, honest read of where your brand stands today — and exactly what's costing you clarity.</p>
        </div>
        <div class="index-side"><div class="index-price">€1,200</div><a href="approach.html#services" class="btn btn-outline">Details</a></div>
      </div>
      <div class="index-row">
        <div class="index-num">02</div>
        <div class="index-body">
          <span class="index-timeline">3 weeks</span>
          <h3 class="index-title">Brand Strategy Core</h3>
          <p class="index-desc">Positioning, message architecture and brand voice — built to survive contact with real customers.</p>
        </div>
        <div class="index-side"><div class="index-price">€4,500</div><a href="approach.html#services" class="btn btn-outline">Details</a></div>
      </div>
      <div class="index-row">
        <div class="index-num">03</div>
        <div class="index-body">
          <span class="index-timeline">5–6 weeks</span>
          <h3 class="index-title">Brand Platform</h3>
          <p class="index-desc">Strategy plus the verbal and visual direction to carry it — ready to hand to a designer, a developer or your own team.</p>
        </div>
        <div class="index-side"><div class="index-price">€9,000</div><a href="approach.html#services" class="btn btn-outline">Details</a></div>
      </div>
      <div class="index-row">
        <div class="index-num">04</div>
        <div class="index-body">
          <span class="index-timeline">Monthly</span>
          <h3 class="index-title">Brand Advisory</h3>
          <p class="index-desc">Ongoing strategic counsel once the foundation exists — a monthly call, new-launch positioning reviews, quick answers by email.</p>
        </div>
        <div class="index-side"><div class="index-price">€1,800<small>/mo</small></div><a href="contact.html" class="btn btn-outline">Ask</a></div>
      </div>
    </div>
"""

PRODUCTS = f"""
    <div class="products">
      <div class="product">
        <span class="price">€5.99</span>
        <h3>Positioning in a Weekend</h3>
        <p>Three worksheets, five AI prompts and a five-second test: one position that survives testing, in a weekend.</p>
        <a href="{GUMROAD}/l/nstvsw" target="_blank" rel="noopener">Get it on Gumroad →</a>
      </div>
      <div class="product">
        <span class="price">€29</span>
        <h3>AI Prompt Pack for Founders</h3>
        <p>28 tested prompts across audit, positioning, meaning, messaging, naming and launch.</p>
        <a href="{GUMROAD}/l/uhhlwm" target="_blank" rel="noopener">Get it on Gumroad →</a>
      </div>
      <div class="product">
        <span class="price">€149</span>
        <h3>The Brand Strategy System</h3>
        <p>The full method, self-serve: eight modules from audit to launch, a 69-page PDF, a Notion template and fillable canvases.</p>
        <a href="{GUMROAD}/l/gajjex" target="_blank" rel="noopener">Get it on Gumroad →</a>
      </div>
      <div class="product">
        <span class="price">€299</span>
        <h3>The System + 1:1 Positioning Call</h3>
        <p>Everything in the System, plus a 45-minute session with me to pressure-test your positioning.</p>
        <a href="{GUMROAD}/l/llfjd" target="_blank" rel="noopener">Get it on Gumroad →</a>
      </div>
    </div>
    <p class="products-note">The €5.99 and €29 purchases count in full toward the System. The System and the System + Call count in full toward a Positioning Audit (€1,200) if you book one within 90 days.</p>
"""

CASE_CARDS = {
    "socialbooth": ("case-study-socialbooth.html", "images/socialbooth-home-hero-it.jpg",
                    "Positioning Audit · Past affiliation disclosed", "Socialbooth",
                    "A mission built on emotion, hidden on the one page buyers don't read — and a homepage that sounds like every competitor."),
    "velasca": ("case-study-velasca.html", "images/velasca-stringate-grid.jpg",
                "Spec project · Positioning Audit", "Velasca",
                "Family workshops in Montegranaro, 20+ shops, shoes named in Milanese dialect — and a homepage that only says “Made in Italy.”"),
    "cafezal": ("case-study-cafezal.html", "images/cafezal-catalog-grid-0926.jpg",
                "Spec project · Brand Platform", "Cafezal Milano",
                "A roaster whose farmers have names and stories — and a catalogue that leads with a score and a price."),
    "ivana": ("case-study-ivana-vegetti.html", "images/ivana-vegetti-homepage.jpg",
              "Spec project · Brand Strategy Core", "Ivana Vegetti",
              "A wedding studio that promises artistry — while its own clients keep praising something else."),
}


def work_cards(keys):
    html = '\n    <div class="work-grid">'
    for k in keys:
        href, img, kicker, name, blurb = CASE_CARDS[k]
        html += f"""
      <a href="{href}" class="work-card">
        <div class="work-thumb" style="background-image:url('{img}');"></div>
        <span class="work-kicker">{kicker}</span>
        <h3>{name}</h3>
        <p>{blurb}</p>
      </a>"""
    html += """
      <a href="contact.html" class="work-card is-next">
        <div class="work-thumb no-photo"><span class="next-mark">Next case</span></div>
        <span class="work-kicker">Open slot</span>
        <h3>Your brand could be next.</h3>
        <p>Send me your site. If there's a clear gap between what you say and what makes you worth choosing, this is where the audit goes.</p>
      </a>
    </div>
"""
    return html


WORK_CARDS = work_cards(["socialbooth", "velasca", "cafezal", "ivana"])
HOME_CARDS = work_cards(["socialbooth", "velasca"])

# ---------------------------------------------------------------- index

INDEX = f"""
<section class="hero">
  <img src="brand-assets/d-mark-ink.svg" alt="" class="hero-d" aria-hidden="true">
  <div class="wrap">
    <span class="eyebrow">Brand strategy · Milano</span>
    <h1>Brand strategy built with the <em>rigor</em> of a luxury house — sized for where you are now.</h1>
    <p class="lede">Studio Dudin is a brand strategy practice for small businesses and founders who want more than a logo: a clear position, a voice people remember, and a plan they can actually run.</p>
    <div class="cta-row">
      <a href="contact.html" class="btn btn-primary">Book a Positioning Audit</a>
      <a href="approach.html" class="btn btn-outline">How it works</a>
    </div>
    <p class="reassure">The first call is 20 minutes, no slides, no pitch. If it's not a fit, I'll say so.</p>
  </div>
</section>

<section class="section-white">
  <div class="wrap">
    <span class="eyebrow">Why this matters now</span>
    <h2>An unclear brand doesn't stay neutral. It costs you something every day it stays unclear.</h2>
    <div class="compare">
      <div class="compare-col compare-bad">
        <h3>Left unclear</h3>
        <ul>
          <li>Every euro of ad spend works harder than it should, re-explaining the business from zero each time.</li>
          <li>Pricing turns into a negotiation, because nothing separates the offer from the next option.</li>
          <li>Every new hire, freelancer or agency writes in a slightly different voice — and the drift compounds.</li>
          <li>Your best customers can't repeat back what makes you different, so they don't refer you.</li>
        </ul>
      </div>
      <div class="compare-col compare-good">
        <h3>Made clear, once</h3>
        <ul>
          <li>New copy, new hires and new campaigns pull in the same direction without a rulebook attached to each one.</li>
          <li>Customers can say in one sentence why you and not the next option — the cheapest marketing there is.</li>
          <li>Every future decision — a new product, a new market, a rebrand five years out — has something real to check itself against.</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section-paper tight">
  <div class="wrap">
    <p class="lead-line">Most brand strategy is priced and paced for companies that already have a marketing department. Studio Dudin is built for the ones that <em>don't — yet</em>.</p>
  </div>
</section>

<section class="section-white">
  <div class="wrap">
    <span class="eyebrow">Who's behind it</span>
    <div class="founder">
      <div class="founder-mark"><img src="brand-assets/d-mark-ink.svg" alt=""></div>
      <div class="founder-text">
        <h2>Research first. Opinion last.</h2>
        <p>Studio Dudin is Valentin Dudin. I came to brand strategy through research: consumer insights at MTS Bank and full-cycle market research at O+K Research — hall tests, customer journey maps, competitive benchmarks. Before that, a sociology degree with economics and statistics.</p>
        <p>I hold the Inside LVMH Certificate in Creation &amp; Branding. The method is the same one I'd apply to any brand: find out what's true about your customers and your market before deciding what to say.</p>
      </div>
    </div>
    <div class="stats">
      <div class="stat"><span class="num">15%</span><span class="label">engagement lift after a product was changed to match what the research found (MTS Bank)</span></div>
      <div class="stat"><span class="num">8</span><span class="label">moderated hall tests run for one product</span></div>
      <div class="stat"><span class="num">5+</span><span class="label">competing platforms benchmarked, mapped to a 5-stage customer journey</span></div>
    </div>
    <div class="cta-row">
      <a href="approach.html" class="btn btn-outline">Read the full approach</a>
    </div>
  </div>
</section>

<section class="section-paper">
  <div class="wrap">
    <span class="eyebrow">Work with me</span>
    <h2>Four ways to work together.</h2>
{SERVICES_SHORT}
  </div>
</section>

<section class="section-white" id="products">
  <div class="wrap">
    <span class="eyebrow">Start on your own</span>
    <h2>Not ready for an engagement? Start with the method.</h2>
    <p class="lede">Self-serve versions of the same work, for founders who want to do the first pass themselves.</p>
{PRODUCTS}
  </div>
</section>

<section class="section-paper">
  <div class="wrap">
    <span class="eyebrow">Work</span>
    <h2>Real thinking, published in full — not a portfolio of mockups.</h2>
{HOME_CARDS}
    <div class="cta-row"><a href="work.html" class="btn btn-outline">All work and notes</a></div>
  </div>
</section>
{closing(sub="Studio Dudin is one person by design — every engagement gets full attention, so only a few run at once.")}"""

page("index.html", "Studio Dudin — Brand Strategy for Small Businesses & Founders",
     "Brand strategy built with the rigor of a luxury house — sized for where you are now. Positioning, messaging and voice for small businesses and founders, from Milan.",
     INDEX)

# ---------------------------------------------------------------- approach

APPROACH = f"""
<section class="hero page-hero">
  <img src="brand-assets/d-mark-ink.svg" alt="" class="hero-d" aria-hidden="true">
  <div class="wrap">
    <span class="eyebrow">Who, what, how</span>
    <h1 class="page-title">Find out what's true first. Then decide what to <em>say</em>.</h1>
    <p class="lede">Everything you'd want to know before writing the first email: who's behind this, what each engagement includes, what it costs, and how it runs.</p>
  </div>
</section>

<section class="section-white">
  <div class="wrap">
    <span class="eyebrow">Who</span>
    <div class="founder">
      <div class="founder-mark"><img src="brand-assets/d-mark-ink.svg" alt=""></div>
      <div class="founder-text">
        <p>It started with research, not a swatch book. As a consumer insights researcher at MTS Bank in Moscow, I ran moderated hall tests, built a five-stage customer journey map and benchmarked the product against five-plus competing platforms. The findings changed the product — and engagement rose 15% after launch. Before that, at O+K Research, I ran full-cycle market research projects for several brand clients, from brief to final report.</p>
        <p>The foundation underneath is a sociology degree from Novosibirsk State University, with economics and statistics, and the Inside LVMH Certificate in Creation &amp; Branding. Both point at the same question: why people choose what they choose, and what a brand has to be for them to choose it on purpose.</p>
        <p>Here's the part that isn't on a CV. Almost everyone doing this work well is doing it for companies that already have a marketing department. The businesses that need a clear position most — the ones still deciding what they are — usually get a logo and a font pairing instead of an answer. Studio Dudin exists to close that gap: research-first strategy, sized for a small business.</p>
      </div>
    </div>
  </div>
</section>

<section class="section-paper">
  <div class="wrap">
    <span class="eyebrow">Principles</span>
    <h2>Three things every engagement runs on.</h2>
    <div class="grid-3">
      <div><h3>Clarity</h3><p>You never leave a session more confused than you came in. Strategy that can't be said in one sentence isn't finished.</p></div>
      <div><h3>Candor</h3><p>If your idea doesn't hold up, you'll hear it from me before you hear it from your customers.</p></div>
      <div><h3>Craft</h3><p>Every deliverable is a document you can use, written in plain language, with the evidence behind every claim.</p></div>
    </div>
  </div>
</section>

<section class="section-white" id="services">
  <div class="wrap">
    <span class="eyebrow">Services &amp; pricing</span>
    <h2>Pick the depth that fits where you are.</h2>
    <p class="lede">Not sure what a Positioning Audit reads like? <a href="work.html" class="text-link">See published examples</a> — same format, real companies.</p>
    <div class="index-list">
      <div class="index-row">
        <div class="index-num">01</div>
        <div class="index-body">
          <span class="index-timeline">1 week</span>
          <h3 class="index-title">Positioning Audit <span class="index-flag">Start here</span></h3>
          <p class="index-desc">A fast, honest read of where your brand stands today — and exactly what's costing you clarity.</p>
          <ul class="index-includes"><li>Competitive scan</li><li>Audience read</li><li>Messaging gap analysis</li><li>45-minute working session</li><li>One-page action plan</li></ul>
        </div>
        <div class="index-side"><div class="index-price">€1,200</div><a href="contact.html" class="btn btn-primary">Book</a></div>
      </div>
      <div class="index-row">
        <div class="index-num">02</div>
        <div class="index-body">
          <span class="index-timeline">3 weeks</span>
          <h3 class="index-title">Brand Strategy Core</h3>
          <p class="index-desc">Positioning, message architecture and brand voice — built to survive contact with real customers.</p>
          <ul class="index-includes"><li>Stakeholder interviews</li><li>Competitive &amp; market research</li><li>Positioning statement</li><li>Messaging framework</li><li>Brand voice guide</li></ul>
        </div>
        <div class="index-side"><div class="index-price">€4,500</div><a href="contact.html" class="btn btn-outline">Enquire</a></div>
      </div>
      <div class="index-row">
        <div class="index-num">03</div>
        <div class="index-body">
          <span class="index-timeline">5–6 weeks</span>
          <h3 class="index-title">Brand Platform</h3>
          <p class="index-desc">Strategy plus the verbal and visual direction to carry it — ready to hand to a designer, a developer or your own team.</p>
          <ul class="index-includes"><li>Everything in Core</li><li>Visual identity direction</li><li>Brand guidelines document</li><li>Launch messaging kit</li></ul>
        </div>
        <div class="index-side"><div class="index-price">€9,000</div><a href="contact.html" class="btn btn-outline">Enquire</a></div>
      </div>
      <div class="index-row">
        <div class="index-num">04</div>
        <div class="index-body">
          <span class="index-timeline">Monthly</span>
          <h3 class="index-title">Brand Advisory</h3>
          <p class="index-desc">A monthly strategy call, a positioning review for each new launch, and quick answers by email within two business days.</p>
        </div>
        <div class="index-side"><div class="index-price">€1,800<small>/mo</small></div><a href="contact.html" class="btn btn-outline">Ask</a></div>
      </div>
    </div>
    <p class="reassure">Every price above is what you pay — no add-ons that surface later.</p>
  </div>
</section>

<section class="section-paper" id="products">
  <div class="wrap">
    <span class="eyebrow">Start on your own</span>
    <h2>The same method, self-serve.</h2>
    <p class="lede">For founders who want to do the first pass themselves before hiring anyone.</p>
{PRODUCTS}
  </div>
</section>

<section class="section-white" id="process">
  <div class="wrap">
    <span class="eyebrow">Process</span>
    <h2>What happens when we work together.</h2>
    <div class="steps">
      <div class="step"><div class="n">01</div><div><h3>The first call — free, 20 minutes</h3><p>You tell me what's going on, I ask sharp questions, and we work out whether this is a Positioning Audit, a Brand Strategy Core, or something else. If it's not a fit, I'll say so.</p></div></div>
      <div class="step"><div class="n">02</div><div><h3>Scope &amp; kickoff</h3><p>A one-page agreement: scope, price, timeline, no legalese. A 50% deposit starts the work; the rest is due on delivery. Then a short written intake, so I'm not asking you things you've already told me.</p></div></div>
      <div class="step"><div class="n">03</div><div><h3>The work</h3><p>Research first — competitive scan, audience read, stakeholder interviews where the package includes them. Then synthesis. You see a working draft partway through, not a reveal at the end.</p></div></div>
      <div class="step"><div class="n">04</div><div><h3>Delivery</h3><p>Actual documents, not a slide you'll open once: positioning statement, messaging framework, voice guide — per package. Plain language, ready to hand to a designer, a developer or your own team.</p></div></div>
      <div class="step"><div class="n">05</div><div><h3>After</h3><p>A 30-day question window after delivery, at no extra cost. Want ongoing input after that? That's what Brand Advisory is for.</p></div></div>
    </div>
  </div>
</section>

<section class="section-paper">
  <div class="wrap">
    <span class="eyebrow">Before you write the email</span>
    <h2>Questions people actually ask.</h2>
    <div class="faq">
      <details><summary>Why should I trust a studio that's brand new?</summary><p>You shouldn't take it on faith. That's why the Work page publishes real, checkable audits instead of mockups — you can read exactly how I think before you pay for anything.</p></details>
      <details><summary>What if I don't like the direction you come back with?</summary><p>Brand Strategy Core and Brand Platform both include a draft review before anything is final, plus revision rounds — you react to the thinking while it can still change. The Positioning Audit is shorter, but the working session is a conversation, not a handoff.</p></details>
      <details><summary>Do you design logos or build websites?</summary><p>No. Brand Platform sets the visual direction — palette and typography direction, a logo brief — so a designer can execute it correctly. I set the direction; I don't produce the final assets.</p></details>
      <details><summary>I'm not in Italy. Can we still work together?</summary><p>Yes. Everything runs over video calls and email. Milan is where I'm based, not a requirement.</p></details>
      <details><summary>Can I start small and go bigger later?</summary><p>Yes. Starting with the Positioning Audit and moving into Brand Strategy Core is the most common path, and the Core builds on what the Audit already found. If you start with the self-serve System, what you paid counts toward the Audit within 90 days.</p></details>
      <details><summary>What if it's not a fit after the first call?</summary><p>Then I'll say so directly, and it costs you nothing. The first call is free precisely so finding out isn't expensive.</p></details>
    </div>
  </div>
</section>
{closing(h2="Ready for the first call?", btn="Get in touch", note=None)}"""

page("approach.html", "Approach — Studio Dudin",
     "Who's behind Studio Dudin, what each engagement includes, what it costs, and how it runs.", APPROACH)

# ---------------------------------------------------------------- work

WORK = f"""
<section class="hero page-hero">
  <img src="brand-assets/d-mark-ink.svg" alt="" class="hero-d" aria-hidden="true">
  <div class="wrap">
    <span class="eyebrow">Work</span>
    <h1 class="page-title">This could be your <em>case study</em>.</h1>
    <p class="lede">Studio Dudin is new: three spec projects and one disclosed audit, no paying clients yet. I'm not going to dress that up — pretending otherwise would be exactly the kind of vague brand move I'd flag in yours.</p>
  </div>
</section>

<section class="section-white">
  <div class="wrap">
    <span class="eyebrow">Published audits</span>
    <h2>Real companies, real findings, checkable claims.</h2>
{WORK_CARDS}
    <p class="measure muted" style="margin-top: var(--space-xl);">What I can show today is the thinking, not a client list. If you're one of the first clients, you get more of my time, a founding-client price, and a say in how the story is told when it's published here.</p>
  </div>
</section>

<section class="section-paper">
  <div class="wrap">
    <span class="eyebrow">Field notes</span>
    <h2>Written when there's something worth saying.</h2>
    <div class="notes">
      <article class="note">
        <time datetime="2026-09-18">18 September 2026</time>
        <div>
          <h3>Why most positioning work fails before the first slide</h3>
          <p>Almost every brand brief starts the same way: a list of what the company does, followed by adjectives it would like to be associated with. Trustworthy. Innovative. Customer-first. None of that is positioning — it's a description, and a generic one, because every competitor's brief says roughly the same thing.</p>
          <p>Positioning fails early because it's treated as a writing problem: find better words for what we already believe about ourselves. It's a research problem. Who specifically chooses you over the next option, and why that one reason and not the others you'd prefer they cared about? That's the structure behind the Positioning Audit: a competitive scan, an audience read built from evidence, and a messaging gap analysis that shows where the current story contradicts itself.</p>
        </div>
      </article>
      <article class="note">
        <time datetime="2026-09-18">18 September 2026</time>
        <div>
          <h3>The case for auditing in public</h3>
          <p>Most new studios fill their portfolio with mockups — logo concepts for a fictional coffee shop, a rebrand nobody asked for. I understand why: there's no client history yet, and an empty page looks worse than a fake one. But a mockup can't be wrong. Nobody can check it against reality, so it shows taste, not judgment.</p>
          <p>The audits on this page exist instead: real, currently operating companies, their actual public brand, findings anyone can verify, clearly marked as unsolicited — and taken down if a company asks.</p>
        </div>
      </article>
    </div>
  </div>
</section>
{closing(h2="Want to be the first case study?", btn="Get in touch", note=None)}"""

page("work.html", "Work — Studio Dudin",
     "Published brand audits of real companies, plus field notes on positioning.", WORK)

# ---------------------------------------------------------------- contact

CONTACT = f"""
<section class="hero page-hero">
  <img src="brand-assets/d-mark-ink.svg" alt="" class="hero-d" aria-hidden="true">
  <div class="wrap">
    <span class="eyebrow">Get in touch</span>
    <h1 class="page-title">Let's talk about your brand.</h1>
    <p class="lede">Tell me what you're working on. I'll reply with the right starting point — maybe a Positioning Audit, maybe just a conversation.</p>
  </div>
</section>

<section class="section-white">
  <div class="wrap contact-grid">
    <form class="contact-form" id="contact-form" data-to="{EMAIL}" data-endpoint="{FORM_ENDPOINT}">
      <div class="hp" aria-hidden="true"><label for="website">Website</label><input type="text" id="website" name="website" tabindex="-1" autocomplete="off"></div>
      <div class="field"><label for="name">Name</label><input type="text" id="name" name="name" autocomplete="name" required></div>
      <div class="field"><label for="email">Email</label><input type="email" id="email" name="email" autocomplete="email" required></div>
      <div class="field"><label for="company">Company</label><input type="text" id="company" name="company" autocomplete="organization"></div>
      <div class="field"><label for="stage">Where are you?</label>
        <select id="stage" name="stage">
          <option>Just starting out</option>
          <option>Repositioning</option>
          <option>Launching something new</option>
        </select>
      </div>
      <div class="field"><label for="interest">Interested in</label>
        <select id="interest" name="interest">
          <option>Positioning Audit — €1,200</option>
          <option>Brand Strategy Core — €4,500</option>
          <option>Brand Platform — €9,000</option>
          <option>Brand Advisory — €1,800/mo</option>
          <option>Not sure yet</option>
        </select>
      </div>
      <div class="field"><label for="message">Message</label><textarea id="message" name="message" required></textarea></div>
      <div>
        <button type="submit" class="btn btn-primary">{FORM_BUTTON}</button>
        <p class="form-status" id="form-status" role="status" aria-live="polite"></p>
      </div>
    </form>
    <aside class="contact-side">
      <h3>Prefer to write directly?</h3>
      <p><a href="mailto:{EMAIL}" class="text-link">{EMAIL}</a></p>
      <p>No mailing list, no automated sequence — a reply from me, usually within a day.</p>
      <p>Based in Milan. Working in English, Italian and Russian, with clients anywhere.</p>
    </aside>
  </div>
</section>
"""

page("contact.html", "Contact — Studio Dudin",
     "Tell Studio Dudin what you're working on and get a reply about the right starting point.", CONTACT)

# ---------------------------------------------------------------- case studies

def case_hero(eyebrow, h1, lede, method=None):
    m = f'<p class="methodology-note">{method}</p>' if method else ""
    return f"""
<section class="hero page-hero">
  <div class="wrap">
    <span class="eyebrow">{eyebrow}</span>
    <h1 class="page-title">{h1}</h1>
    <p class="lede">{lede}</p>
    {m}
  </div>
</section>
"""


def callout(title, text):
    return f"""
<section class="section-white tight">
  <div class="wrap">
    <div class="callout"><h3>{title}</h3><p>{text}</p></div>
  </div>
</section>
"""


def deliverables(items):
    rows = "".join(f'\n      <div class="deliverable"><div class="n">{i:02d}</div><div><h3>{t}</h3>{b}</div></div>'
                   for i, (t, b) in enumerate(items, 1))
    return f'<div class="deliverables">{rows}\n    </div>'


def scorecard(items):
    cells = "".join(f'\n      <div class="scorecard-item"><h4>{t}</h4><span class="scorecard-rating {r.lower()}">{r}</span></div>'
                    for t, r in items)
    return f'<div class="scorecard">{cells}\n    </div>'


def gap(left_t, left, right_t, right):
    return f"""
    <div class="gap-diagram">
      <div class="gap-box"><h4>{left_t}</h4><p>{left}</p></div>
      <div class="gap-arrow" aria-hidden="true">→</div>
      <div class="gap-box gap-box-right"><h4>{right_t}</h4><p>{right}</p></div>
    </div>"""


CASE_CLOSE = closing(h2="Want this kind of read on your own brand?")

# --- shared helpers for case studies
def figure(src, alt, cap, cls=""):
    return f"""
    <figure class="evidence-figure {cls}">
      <img src="images/{src}" alt="{alt}" loading="lazy">
      <figcaption>{cap}</figcaption>
    </figure>"""


def it(q, en):
    """Italian original in quotes, English translation right after it."""
    return f'<em lang="it">“{q}”</em> <span class="tr">(“{en}”)</span>'


def scan_table(rows, subject):
    body = ""
    for r in rows:
        cls = ' class="is-subject"' if r[0] == subject else ""
        body += f"<tr{cls}><td>{r[0]}</td><td>{r[1]}</td><td>{r[2]}</td><td>{r[3]}</td></tr>"
    return f"""
    <div class="table-wrap">
      <table class="scan-table">
        <thead><tr><th>Brand</th><th>Lead message</th><th>Proof on the page</th><th>Who it's for</th></tr></thead>
        <tbody>{body}</tbody>
      </table>
    </div>"""


def tiers(week, month, quarter):
    col = lambda title, items: "<div><h4>" + title + "</h4><ul>" + "".join("<li>" + i + "</li>" for i in items) + "</ul></div>"
    return '<div class="tiers">' + col("This week", week) + col("This month", month) + col("This quarter", quarter) + "</div>"


def section(cls, eyebrow, h2, inner, sid=""):
    idattr = f' id="{sid}"' if sid else ""
    return f"""
<section class="{cls}"{idattr}>
  <div class="wrap">
    <span class="eyebrow">{eyebrow}</span>
    <h2>{h2}</h2>
{inner}
  </div>
</section>
"""


def summary(lead, body):
    return f"""
<section class="section-paper">
  <div class="wrap">
    <span class="eyebrow">The finding in one paragraph</span>
    <div class="summary-box">
      <p class="lead-line">{lead}</p>
      <p>{body}</p>
    </div>
  </div>
</section>
"""


TRANSLATION_NOTE = '<p class="measure muted small">Quotes from Italian pages are given in the original, followed by my English translation in brackets.</p>'

# ================================================================ SOCIALBOOTH
SB_Q_HERO = it("Trasformiamo eventi e fiere in spazi che attirano persone, le coinvolgono e generano risultati.", "We turn events and trade fairs into spaces that attract people, engage them and generate results.")
SB_Q_SUB = it("creiamo esperienze interattive che aumentano il tempo di permanenza, producono contenuti condivisibili e raccolgono contatti reali", "we create interactive experiences that increase dwell time, produce shareable content and collect real contacts")
SB_Q_SELFIE = it("Esperienze interattive con foto, video e intelligenza artificiale per aumentare engagement, visibilità e contenuti condivisibili in tempo reale.", "Interactive photo, video and AI experiences to increase engagement, visibility and shareable content in real time.")
SB_Q_NOTSUP = it("Non siamo fornitori. Siamo parte del risultato del tuo evento.", "We're not suppliers. We're part of your event's result.")
SB_Q_VISION = it("il gioco crea emozioni, relazioni e fa sentire vivi", "play creates emotions and relationships, and makes people feel alive")
SB_Q_TP = it("Creiamo emozioni condivise durante gli eventi", "We create shared emotions at events")
SB_Q_FUN = it("super divertente", "great fun") + " and " + it("soluzioni sempre innovative e memorabili", "always innovative, memorable solutions")
SB_Q_STAFF = it("Staff perfetto, servizio ottimo", "Perfect staff, excellent service") + " and " + it("Cortesia, professionalità e disponibilità", "Courtesy, professionalism and availability")
SB_Q_CATALOG = it("Il photobooth giusto si sceglie sull’evento, non sul catalogo.", "The right photobooth is chosen for the event, not from the catalogue.")
SB_Q_TYPO1 = it("Vuoi Noleggiare un Phootbooth a Milano per un’evento?", "Want to rent a photobooth in Milan for an event?")
SB_Q_TYPO2 = it("un importate occasione per fare Lead Generation", "an important opportunity for lead generation")

SB = case_hero("Case study — Positioning Audit",
               "Socialbooth: the mission says <em>emotion</em>. The homepage says results.",
               "A full outside read of Socialbooth's public brand, done the way I'd do it for a paying client. The short version: the company's most distinctive idea is already written down — on the one page almost no buyer ever opens.",
               "Reviewed 26 September 2026 · Scope: homepage, services menu, Photobooth Experience, AI+, Lead generation, Società Benefit, the Milano city page, the case-history archive (70+ entries, 4 read in full), the Trustpilot profile, and the sister domain noleggiophotoboothmilano.it, compared with three direct competitors. Public material only: no interviews, no analytics, nothing internal. Socialbooth's site is in Italian; quotes are given in the original with my English translation in brackets.") + \
     callout("Disclosure",
             "Before founding Studio Dudin, I worked at Socialbooth. While I was there I wrote the line <em>“Bring emotions to life.”</em> A version of it — <em>“BRING EMOTION TO LIFE”</em> — is today the company's published mission. That line is the only thing on this page that comes from the inside. Everything else is an unsolicited audit of Socialbooth's <em>current</em> public brand, built from what anyone can see today, not commissioned and not drawing on anything learned internally. If anyone at Socialbooth would rather this page not exist, email me and it comes down.") + \
     summary("Socialbooth is a company built on play and emotion, selling itself with the same results language as everyone else in its category.",
             "Its proof is genuinely strong — 51 reviews at 4.8 on Trustpilot, more than 70 published case histories, national press. Its mission, its vision, its Trustpilot bio and even the smile inside its logo all say the same thing: people come alive when they play. But the homepage leads with “attract, engage, generate results,” a sentence a direct competitor uses almost word for word. The fix isn't a new idea. It's moving the idea they already have to the place where buyers decide.") + \
     section("section-white", "Scorecard", "Where the brand stands today, in four categories.",
             scorecard([("Proof &amp; credibility", "Strong"), ("Differentiation", "Weak"), ("Message consistency", "Weak"), ("Offer clarity", "Mixed")]) +
             '<p class="measure muted small" style="margin-top: var(--space-lg);">The pattern is common in companies that grew fast: the delivery and the reputation got ahead of the words. Nothing here needs a rebrand. It needs the existing brand to say one thing, in one place, first.</p>') + \
     section("section-paper", "01 — What a buyer sees first", "A homepage that could belong to anyone in the category.",
             figure("socialbooth-home-hero-it.jpg", "Socialbooth homepage hero in Italian, yellow background, Trustpilot 4.8, press logos.", "socialbooth.it — homepage hero, as published, 26 September 2026 (reviewer avatars blurred)") +
             f'<p class="measure">The headline — {SB_Q_HERO} — is clear and competent. It\'s also generic. Here is the hero of Selfieboost, a Milan competitor: {SB_Q_SELFIE} And Socialbooth\'s own line under its headline: {SB_Q_SUB}. Swap the logos and a buyer couldn\'t tell which is which.</p>' +
             f'<p class="measure">Further down, the homepage has a much sharper sentence — {SB_Q_NOTSUP} — followed by an animated line, “We Create →”, cycling through Intrattenimento (entertainment), Valore (value), Future, Connection, Interaction, Lead and Engagement. Seven words, two languages, and the one word the company says it exists for isn\'t among them.</p>' +
             figure("socialbooth-home-not-suppliers.jpg", "Socialbooth homepage section: Non siamo fornitori. Siamo parte del risultato del tuo evento. Followed by an animated We Create line.", "socialbooth.it — homepage, second section; the last pill rotates through seven words")) + \
     section("section-white", "02 — Where the real idea lives", "“Bring emotion to life” is on the Società Benefit page.",
             figure("socialbooth-mission.jpg", "Socialbooth Società Benefit page, Missione section: La nostra missione è BRING EMOTION TO LIFE.", "socialbooth.it/societa-benefit — Missione: “Our mission is BRING EMOTION TO LIFE — we want to bring emotions to life for the people at the events and fairs where Socialbooth is present.” As published, 26 September 2026", "narrow") +
             f'<p class="measure">The same page states a vision a competitor couldn\'t easily copy: {SB_Q_VISION}. The Trustpilot profile says {SB_Q_TP}. The logo turns the two o\'s of “booth” into a smile. The clients who reviewed them talk about fun as much as execution — {SB_Q_FUN}.</p>' +
             gap("What the homepage leads with", "Attract, engage, generate results. Dwell time, shareable content, real leads. True, and claimed by every serious competitor.",
                 "What the company says it's for", "Bring emotion to life. Play makes people feel alive — and that feeling is what makes them stay, share and leave their email.") +
             '<p class="measure muted">These two aren\'t in conflict. Emotion is the mechanism; results are the proof. Right now the homepage shows the proof without the mechanism, which is exactly what makes it sound like everyone else.</p>') + \
     section("section-paper", "03 — Competitive scan", "Nobody in the category owns emotion. Everybody owns “engagement.”",
             scan_table([
                 ("Socialbooth", "Events and fairs that attract people, engage them and generate results.", "Trustpilot 4.8 (51 reviews), 70+ case histories, press logos, ISO badges", "Corporate events, fairs, agencies"),
                 ("Selfieboost", "Interactive photo, video and AI experiences to increase engagement, visibility and shareable content.", "Event photo gallery", "Corporate and weddings"),
                 ("Babooth", "Branded, customised photobooth rental with instant digital sharing.", "Founded 2013, a portfolio of branded projects for well-known brands", "Corporate and weddings"),
                 ("Say Cheese", "A creative studio designing unforgettable experiences for brands and agencies.", "Ten years, case studies, “7 clients out of 10 come back”, openly not the cheapest", "Brands and agencies (weddings under a separate name)"),
             ], "Socialbooth") +
             f'<p class="measure" style="margin-top: var(--space-lg);">Two things stand out. Socialbooth has the strongest proof of the four and one of the least distinctive lead messages. And the only competitor with a clear identity — Say Cheese, positioned as a creative studio that says outright it isn\'t the cheapest supplier on the market — got there by saying what it isn\'t. Socialbooth already has its equivalent line, {SB_Q_NOTSUP}, and a mission nobody else can claim. It just isn\'t using them first.</p>' +
             '<p class="measure muted small">Competitor lines are my English summaries of their Italian homepages as published on 26 September 2026.</p>') + \
     section("section-white", "04 — Audience read", "Two buyers, reading for different things.",
             deliverables([
                 ("The brand marketer", "<p>Has a budget line to justify. The homepage is written for this person — dwell time, content, leads, a dashboard — and that's right. What this buyer is missing is a reason to pick Socialbooth over the next supplier making the same promise, and numbers on the case pages to put in the internal report.</p>"),
                 ("The agency or event producer", "<p>The contact form asks " + it("Chi sei?", "Who are you?") + " with Azienda / Agenzia (company / agency) as the options, so agencies are clearly a core buyer. This person is staking their own client relationship on the supplier. The reviews speak straight to them — " + SB_Q_STAFF + " — but the site never addresses them directly.</p>"),
                 ("What both respond to", "<p>An attendee who is visibly having a good time is the one thing both buyers want and neither can produce alone. That's the emotional outcome the mission describes. Leading with it serves both: the marketer gets a differentiator, the producer gets a partner who makes the event look good.</p>"),
             ])) + \
     section("section-paper", "05 — Messaging gaps", "Four places where the brand works against itself.",
             deliverables([
                 ("A catalogue that contradicts its own advice", f"<p>The Photobooth Experience page says it well: {SB_Q_CATALOG} The navigation above it is a catalogue: five families and 28 products, from Green Screen to Social Bike. A first-time buyer is asked to choose by product — exactly what the page tells them not to do.</p>" + figure("socialbooth-services-menu.jpg", "Socialbooth Servizi (services) menu open with five product families.", "socialbooth.it — the Servizi (services) menu; each family opens into its own sub-list", "narrow")),
                 ("Results promised, rarely shown", "<p>The homepage promises results and a post-event dashboard with the data. Of the four case histories I read in full, one reports numbers — Petronas at the Turin Auto Show: over 1,100 shots, over 123,000 people reached, over 400,000 impressions. Hot Wheels, Fiat 500 at the Deejay Ten and Hoffman Essentials describe full stores and good moments, with no figures. For a brand that sells measurable outcomes, that's the proof buyers look for and mostly don't find.</p>"),
                 ("Two languages, two spellings, two looks", "<p>Visitors with an English-language browser are switched automatically to a machine translation (“engage them , and generate results .”). The logo tagline, the “We Create” line and the service family names are in English inside Italian copy. The Milano city page swaps the homepage's yellow and black for an orange-to-magenta gradient. And a second domain run by the same company, noleggiophotoboothmilano.it, sells the same service while calling the registered trademark “Social Booth” — two words, where the main site writes Socialbooth®.</p>" + figure("socialbooth-home-hero-en-auto.jpg", "Socialbooth homepage auto-translated into English with spacing errors.", "socialbooth.it — the same hero, auto-translated for an English-language browser (reviewer avatars blurred)") + figure("socialbooth-milano-landing.jpg", "Socialbooth Milano city page with large gradient Photobooth lettering.", "socialbooth.it/noleggio-photobooth-milano — a different visual system from the homepage")),
                 ("Small slips that cost trust", f"<p>On the Milano page: {SB_Q_TYPO1} and {SB_Q_TYPO2} — “Phootbooth,” “un’evento” and “importate” are typos in the original. In the case archive, industry tags read “Cyber Securty” and “Food &amp; Bverage,” and AI projects are tagged both “AI” and “IA.” Each is trivial on its own. Together, on a brand that sells polish at corporate events, they read as nobody owning the words.</p>"),
             ])) + \
     section("section-white", "06 — Direction", "What the brand could say instead.",
             '<p class="lede">A draft built only from Socialbooth\'s own published words — the positioning a paid engagement would pressure-test, not a finished answer.</p>' +
             deliverables([
                 ("Draft positioning", "<p class='lead-line'>“Bring emotion to life — and measure what it does for your brand.”</p><p>The first half is their mission, unchanged. The second half is the promise the homepage already makes. Together they say something no competitor in the scan can say: the feeling is the method, and the numbers are the receipt.</p>"),
                 ("Message order", "<p><strong>Promise:</strong> people at your event play, laugh and remember it. <strong>Mechanism:</strong> play is designed, not added — " + SB_Q_VISION + ". <strong>Proof:</strong> dwell time, content, contacts and reach, reported per event, the way the Petronas case already does.</p>"),
                 ("Offer by goal, not by product", "<p>Group the 28 products under four event goals: <strong>Attract</strong> (bring people to the stand), <strong>Engage</strong> (keep them there), <strong>Capture</strong> (leads and data), <strong>Amplify</strong> (content and reach after the event). The products stay the same; the buyer chooses by what they need the event to do, which is the site's own advice.</p>"),
             ])) + \
     section("section-paper", "07 — One-page action plan", "If this were a paid engagement, it would start here.",
             tiers(["Fix the typos on the city pages and the case-archive tags.", "Pick one spelling of the name and use it everywhere.", "Set the page language to Italian and turn off automatic machine translation."],
                   ["Put “Bring emotion to life” in the homepage hero, with “Non siamo fornitori” (“We're not suppliers”) directly under it.", "Add a four-line results block — shots, dwell time, contacts, reach — to every new case history, starting from the Petronas format.", "Speak to agencies directly in one homepage section, using the reviews that already praise the team."],
                   ["Restructure the services menu around the four goals: Attract, Engage, Capture, Amplify.", "Bring the city pages into the homepage's visual system, and decide whether the second domain still earns its place.", "Decide on English: a written English version, or Italian only. Machine translation shouldn't be the choice by default."]) +
             '<p class="methodology-note">What this audit leaves out: a paid Positioning Audit adds a working session with the team, access to analytics and enquiry data, and a read of which pages and products actually bring in revenue. None of that happened here. The direction above is a first draft from public material, meant to be argued with.</p>') + \
     CASE_CLOSE
page("case-study-socialbooth.html", "Case Study: Socialbooth — Studio Dudin",
     "A full Positioning Audit of Socialbooth's public brand: strong proof, a generic homepage, and a mission — Bring emotion to life — hidden on the Società Benefit page.", SB, active="work.html")

# ================================================================ IVANA VEGETTI
IV_Q_IT_HERO = it("un racconto autentico di moderna eleganza, pensato come un abito su misura: unico, irripetibile, che suscita emozioni", "an authentic story of modern elegance, conceived like a made-to-measure gown: unique, unrepeatable, stirring emotion")
IV_Q_SIGN = it("Eleganza e lusso discreto: la mia firma creativa", "Elegance and discreet luxury: my creative signature")

IV = case_hero("Spec project — Brand Strategy Core",
               "Ivana Vegetti: the page says <em>artistry</em>. Her clients say honesty.",
               "A homepage built on elegance and emotion. Three client testimonials that praise something else almost completely — someone honest and direct, who won't give you a generic answer. In a category where every planner promises the same beauty, that gap is the whole job.",
               "Reviewed 18 September 2026, re-checked 26 September 2026 · Scope: Italian and English homepages, About, services, and the published client testimonials at ivanavegetti.it, compared with three Lake Como and Milan planners. Public material only: no interviews, no private information. Quotes from the Italian pages are given in the original with my English translation in brackets; the English pages are quoted as published.") + \
     callout("This is speculative work, not a client relationship",
             "I picked Ivana Vegetti's studio and this gap on my own initiative — no engagement, no affiliation, nothing commissioned, nothing beyond what's public on her site. It exists to show how I'd approach a Brand Strategy Core, not to claim I was hired for one. If Ivana Vegetti would rather this page not exist, email me and it comes down.") + \
     summary("Ivana Vegetti sells what every luxury planner sells. Her clients buy something only she is praised for.",
             "The site is beautiful and says so — bespoke, elegant, unique, emotional. Every competitor in the scan says the same four words. Meanwhile the three published testimonials, unprompted, describe a different person: honest, direct, patient, the one who finds the compromise. That trait is rarer, harder to copy, and it's exactly what a couple choosing between four similar portfolios needs to hear. It's on the page — in the testimonials, below the fold.") + \
     section("section-white", "Scorecard", "Where the brand stands today, in four categories.",
             scorecard([("Aesthetic execution", "Strong"), ("Message–proof alignment", "Weak"), ("Differentiation", "Weak"), ("Conversion clarity", "Mixed")]) +
             '<p class="measure muted small" style="margin-top: var(--space-lg);">The craft is not the problem — photography, copy rhythm and polish are well above what a boutique studio usually manages alone. The gap is that the brand\'s strongest asset, what clients say about working with her, never makes it into the words she has chosen for herself.</p>') + \
     section("section-paper", "01 — What a couple sees first", "Elegance, bespoke, emotion — the category's vocabulary.",
             figure("ivana-vegetti-homepage.jpg", "Ivana Vegetti English homepage hero: Every wedding designed by Ivana Vegetti tells a story of modern elegance, tailored like a bespoke gown.", "ivanavegetti.it/en — homepage hero, as published; text unchanged on 26 September 2026") +
             f'<p class="measure">The English hero reads: “Every wedding designed by Ivana Vegetti, wedding planner in Italy, tells a story of modern elegance — tailored like a bespoke gown: unique, unrepeatable, and deeply moving.” The Italian homepage says the same: {IV_Q_IT_HERO}. The next sections continue in the same register — “a one-of-a-kind piece of art,” “Italy as an emotion, a journey, a promise.”</p>' +
             f'<p class="measure">Her About page describes a real point of view — a sensibility that comes from fashion and the visual arts, “contemporary minimalism,” {IV_Q_SIGN}. It\'s a credible aesthetic. It\'s also the aesthetic every competitor below claims.</p>') + \
     section("section-white", "02 — What her clients actually say", "Three testimonials, one trait nobody asked them to name.",
             gap("What she says about herself", "Modern elegance, bespoke gown, one-of-a-kind art, Italy as emotion. Aesthetic, aspirational, true of the whole category.",
                 "What clients say about her", "Honest, direct, patient, finds the compromise, never generic. About judgment and trust under pressure — and specific to her.") +
             '<div class="compare"><div class="compare-col compare-bad"><h3>The homepage says</h3><ul><li>“Tailored like a bespoke gown: unique, unrepeatable, and deeply moving.”</li><li>“I don\'t follow traditional rules of romance — I believe every wedding should feel like a one-of-a-kind piece of art.”</li><li>“Italy as an emotion, a journey, a promise.”</li></ul></div>'
             '<div class="compare-col compare-good"><h3>Her clients say</h3><ul><li>Ilaria: “She was our anchor — supportive, patient, honest, and direct. You\'ll never get a generic suggestion from her!”</li><li>Isabel: “She didn\'t just understand us as a couple — she empathized with us, found the right compromises, and always the best solutions.”</li><li>Erica: “Warm, professional, honest, and sincere… always respecting our taste with remarkable professionalism.”</li></ul></div></div>' +
             '<p class="measure muted" style="margin-top: var(--space-xl);">Three separate people volunteered a version of the same trait. “Honest” appears in two of three testimonials; “elegant” appears in none. That\'s the brand the market has already assigned her — and it\'s buried under language that could belong to any luxury studio in Italy.</p>') + \
     section("section-paper", "03 — Competitive scan", "Everyone promises beauty. Nobody promises the truth.",
             scan_table([
                 ("Ivana Vegetti", "Modern elegance, tailored like a bespoke gown: unique, unrepeatable, deeply moving.", "Real Weddings portfolio, press (Elle Sposa, Lovenozze, The Real Wedding), three testimonials", "Italian and international couples; Milan, the lakes, all of Italy"),
                 ("Elena Renzi", "“We give shape to big dreams by paying attention to the smallest details.”", "The most wonderful villas on Lake Como", "International couples, Lake Como"),
                 ("WeddingBox Lake Como", "Luxury Lake Como wedding planner since 2009; “a calm, organised approach.”", "Years in business", "Couples from around the world"),
                 ("Love On Lake Como", "“A luxury and stylish affair,” bespoke design emphasising personality.", "Lake Como setting and design", "Destination couples"),
             ], "Ivana Vegetti") +
             '<p class="measure" style="margin-top: var(--space-lg);">Luxury, bespoke, elegant, personal: four planners, one vocabulary. The only competitor that says anything about <em>how it behaves</em> is WeddingBox, with “a calm, organised approach” — and that\'s the most concrete line in the table. Directness is unclaimed. Ivana is the one with the evidence for it.</p>') + \
     section("section-white", "04 — Audience read", "Who is actually deciding, and what breaks the tie.",
             deliverables([
                 ("The shortlist stage", "<p>Her portfolio and press features put her in front of couples who have already shortlisted three or four planners on aesthetics alone — the photos got her this far. At that stage, beauty is table stakes. What breaks the tie is confidence that this person will steer them well.</p>"),
                 ("The international couple", "<p>The site runs in Italian and English, and her own blog writes about why more foreign couples choose Milan and the lakes. A couple planning from abroad can't drop by the venue. Their biggest fear isn't an ugly wedding — it's a planner who says yes to everything and surprises them later. Honesty is the reassurance they're shopping for.</p>"),
                 ("What the testimonials prove", "<p>Every quoted client describes the relationship, not the decoration: understood us, found compromises, guided us, told us the truth. That is the service, as experienced. The homepage should describe it in the same terms.</p>"),
             ])) + \
     section("section-paper", "05 — What a Brand Strategy Core would produce", "Not a critique — a draft of the real deliverable.",
             '<p class="lede">A first pass at four pieces of a Brand Strategy Core — unsolicited, not yet sharpened by client input or interviews.</p>' +
             deliverables([
                 ("Draft positioning statement", "<p class='lead-line'>“The wedding planner who won't tell you what you want to hear — only what actually works, and then makes it beautiful.”</p><p>This keeps the artistry she clearly delivers, but leads with the trait three clients volunteered: she's direct. That's harder to copy than “bespoke,” because it can't be claimed — it has to be shown on every call.</p>"),
                 ("Messaging framework, two services", "<p><strong>Full Planning</strong> — lead with judgment: “You're not hiring someone to say yes to everything. You're hiring someone who'll tell you when an idea won't work — before it costs you money to find out.”</p><p><strong>Day-of Coordination</strong> — lead with trust under pressure: “The day only goes wrong when no one in the room is willing to make a call. That's the job.”</p>"),
                 ("Voice guide, one do/don't pair", "<p><strong>Don't:</strong> “Every wedding is a unique journey of beauty and emotion.” — true of every planner's homepage, provable by no one.</p><p><strong>Do:</strong> “I'll tell you if the venue you love won't work for 140 guests. That's what you're actually paying for.” — specific, checkable, and what her own clients say made the difference.</p>"),
                 ("Proof placement", "<p>Move the strongest testimonial lines — “You'll never get a generic suggestion from her,” “honest, and direct” — from the bottom of the homepage into the hero and the services page, verbatim and attributed. They're the most persuasive words on the site, and right now they're the last thing a visitor reaches.</p>"),
             ])) + \
     section("section-white", "06 — One-page action plan", "If this were a paid engagement, it would start here.",
             tiers(["Put one testimonial line — “You'll never get a generic suggestion from her” — directly under the homepage headline.", "Add “honest, direct” to the About page opening, in her own words.", "Make sure both language versions carry the same testimonials."],
                   ["Rewrite the hero around judgment and honesty, and let the photography carry the beauty.", "Give each service a sentence about the call Ivana makes in it, not only its scope.", "Collect two or three new testimonials with a question about the hardest decision she helped with."],
                   ["Interview past couples (the Core step this spec skips) to find the exact moment they started trusting her — it becomes the About page's anchor story.", "Build a short “how I work” page: the three moments she says no, and why.", "Use the same line in press pitches and wedding-fair material so the trait travels beyond the site."]) +
             '<p class="methodology-note">What this spec version leaves out: a real Brand Strategy Core starts with up to three stakeholder interviews and a written competitive scan against named competitors in depth. Neither happened here. The statement and messaging above are a plausible first draft, not a final answer.</p>') + \
     CASE_CLOSE
page("case-study-ivana-vegetti.html", "Spec Project: Ivana Vegetti — Studio Dudin",
     "An unsolicited Brand Strategy Core audit: Ivana Vegetti's homepage sells elegance; her clients praise honesty and directness.", IV, active="work.html")

# ================================================================ CAFEZAL
CZ_Q_GRID = it("I migliori chicchi selezionati da tutto il mondo, tostati artigianalmente a Milano e spediti freschi.", "The best beans selected from around the world, roasted by hand in Milan and shipped fresh.")
CZ_Q_ALEX = it("Conosciamo Alexandre da anni e abbiamo avuto il privilegio di visitare la sua piantagione nel cuore del Caparaó", "We have known Alexandre for years and had the privilege of visiting his plantation in the heart of Caparaó")
CZ_Q_ABDO = it("partner Cafezal dal 2021", "a Cafezal partner since 2021")
CZ_Q_META = it("Siamo guidati dalla passione per il caffè nella sua concezione moderna", "We are driven by a passion for coffee in its modern form")

CZ = case_hero("Spec project — Brand Platform",
               "Cafezal: the farmers have <em>names</em>. The catalogue shows a score.",
               "Cafezal's product pages tell real stories — Alexandre in Caparaó, Abdo in Ethiopia, years of partnership, a farm visit. The homepage and the catalogue, where people actually choose, show a name, a score out of 100 and a price. The relationship is the brand. It's one click too deep.",
               "Reviewed 18 September 2026, fully re-checked 26 September 2026 · Scope: homepage, the coffee catalogue (16 products), four product pages, packaging photography and the Milano Coffee Academy section at cafezal.it, compared with two specialty roasters. Public material only: no interviews, no private information. Cafezal's site is in Italian; quotes are given in the original with my English translation in brackets.") + \
     callout("This is speculative work, not a client relationship",
             "I picked Cafezal Milano and this gap on my own initiative — no engagement, no affiliation, nothing commissioned, nothing beyond what's public on their site. It exists to show how I'd approach a Brand Platform, not to claim I was hired for one. If Cafezal would rather this page not exist, email me and it comes down.") + \
     callout("Correction",
             "The first version of this page (18 September) said the sourcing story never reached the product pages, and misread details from a blurred packaging photo. Both were wrong: the product pages do carry origin, producer, variety and process, and the packaging matches them. The finding below is the corrected one — narrower, and more useful.") + \
     summary("Cafezal has the most specific story in Milan specialty coffee, and hides it behind the most generic shelf.",
             "Every product page names a producer, a region, a variety, a process, an altitude — and several tell how long Cafezal has worked with that farmer. That is exactly what “From Farmers to Coffee Lovers” promises. But the catalogue grid, where a buyer compares 16 coffees, shows only a name, a brew method, a score and a price, and the homepage talks about passion and craft in general terms. A competitor in Florence puts origin and tasting notes on the card itself. Cafezal already has better material; it just isn't where the decision happens.") + \
     section("section-white", "Scorecard", "Where the brand stands today, in four categories.",
             scorecard([("Sourcing story (exists)", "Strong"), ("Sourcing story (where people choose)", "Weak"), ("Packaging &amp; product pages", "Strong"), ("Language consistency", "Mixed")]) +
             '<p class="measure muted small" style="margin-top: var(--space-lg);">Splitting “sourcing story” into two rows is the point: the same brand scores completely differently depending on whether you\'re on a product page or on the shelf that leads to it.</p>') + \
     section("section-paper", "01 — Where people choose", "The catalogue: a name, a score, a price.",
             figure("cafezal-catalog-grid-0926.jpg", "Cafezal coffee catalogue grid: product cards with name, brew method, score, star rating and price.", "cafezal.it/collections/coffee — catalogue grid, as published, 26 September 2026") +
             f'<p class="measure">The catalogue opens with {CZ_Q_GRID} Then 16 cards: “Garibaldi – Blend · Espresso/Moka – 84.5pts · da €13,90.” “Black Lyon – Ethiopia (decaf) · 83pts · €15,90.” Names like Pink Jaguar, Kilimanjaro, Botero and Sinfonia. For someone who doesn\'t read cupping scores, nothing on the shelf says why one bag should be chosen over another — or who grew it.</p>') + \
     section("section-white", "02 — Where the story actually is", "One click deeper: named farmers, years of partnership.",
             figure("cafezal-product-description.jpg", "Cafezal product page description for Sinfonia - Brasile: producer Alexandre Emerich, region Caparaó, variety, process, altitude.", "cafezal.it — Sinfonia (Brazil) product page, description, as published, 26 September 2026", "narrow") +
             f'<p class="measure">On the Sinfonia page: {CZ_Q_ALEX}. On Aurora Bio, the producer Abdo Abamecha works with a relative who is {CZ_Q_ABDO}. Each page lists notes, region, producer, variety, process and altitude. The packaging carries the same structure. This is the most specific sourcing story I found among Milan roasters — and it is written for people who have already clicked.</p>' +
             gap("What the shelf and homepage say", "Passion for coffee in its modern form, quality, craft, transparency. A score out of 100 and a price.",
                 "What the product pages say", "Alexandre, whose farm in Caparaó the team visited. Abdo, a partner family since 2021. Exact lots, processes and altitudes.")) + \
     section("section-paper", "03 — Competitive scan", "The specificity is table stakes. Where you show it isn't.",
             scan_table([
                 ("Cafezal", "“From Farmers to Coffee Lovers” — specialty roasters, Milan; academy and five locations.", "Named producers and full lot data on product pages; 5.0 ratings on several products", "Home brewers, cafés (B2B), learners (academy)"),
                 ("Ditta Artigianale", "“The artisans of specialty coffee.”", "Origin, process and tasting notes printed on every product card", "Home brewers and specialty fans"),
                 ("Il Cafetero", "“Dalla Terra alla Tazza” (“From the Earth to the Cup”) — selected specialty coffees roasted in Milan.", "Coffees grouped by brew method and tasting boxes", "Daily home drinkers"),
             ], "Cafezal") +
             '<p class="measure" style="margin-top: var(--space-lg);">All three roasters say farm-to-cup in one form or another. Only Ditta Artigianale puts the proof on the card — “Honduras Finca El Puente · washed · Miele, Sciroppo d\'acero, Caramello” (honey, maple syrup, caramel). Cafezal has richer material than either competitor: named people and relationships, not just lot data. On the shelf, it shows less than both.</p>') + \
     section("section-white", "04 — Audience read", "Three customers, one catalogue.",
             deliverables([
                 ("The specialty regular", "<p>Knows what 85 points means and reads the product page anyway. Already well served — this is who the current site is written for.</p>"),
                 ("The gift buyer and the curious newcomer", "<p>Lands on the grid from Instagram or a Smeg subscription, doesn't read scores, and chooses by the first human reason they see. Today the shelf gives them a name and a number. A producer's name and one line of story would give them a reason.</p>"),
                 ("The café and the academy student", "<p>Cafezal also sells to businesses and teaches at the Milano Coffee Academy. Both buy expertise and trust in sourcing. The farmer relationships are the proof they need, and they're currently scattered across individual product pages.</p>"),
             ])) + \
     section("section-paper", "05 — What a Brand Platform would produce", "Not a critique — a draft of the real deliverable.",
             '<p class="lede">A first pass built only from Cafezal\'s own published words — nothing invented.</p>' +
             deliverables([
                 ("Draft positioning statement", "<p class='lead-line'>“Every bag has a name on it — the farmer's.”</p><p>It turns “From Farmers to Coffee Lovers” from a slogan into a rule the shelf can visibly keep, because the names already exist on every product page.</p>"),
                 ("The card, before and after (real data)", "<p><strong>Now:</strong> “Sinfonia – Brasile · Espresso/Moka – 85pts · €16,90”</p><p><strong>With the page's own facts on the card:</strong> “Sinfonia — Alexandre Emerich, Caparaó, Brazil. Caramel, passion fruit, peach. 85 points · €16,90.” Same data, moved up one level to where the choice is made.</p>"),
                 ("Language", f"<p>The homepage mixes English headings — “Let customers speak for us,” “From Farmers to Coffee Lovers” — into Italian copy, and the meta description stays abstract: {CZ_Q_META}. A Brand Platform would set one language per market and one rule: every claim is followed by a name, a place or a number.</p>"),
             ])) + \
     section("section-white", "06 — One-page action plan", "If this were a paid engagement, it would start here.",
             tiers(["Add the producer's name and region to every catalogue card.", "Add the three tasting notes under the name on each card.", "Pick one language for homepage headings."],
                   ["Build a “Our farmers” page from the stories already on the product pages — Alexandre, Abdo and the rest — with how long Cafezal has worked with each.", "Link each producer from the homepage “From Farmers to Coffee Lovers” section.", "Use the same producer line on Academy and B2B pages."],
                   ["Make “name, place, number” the copy rule for packaging, shelf cards, product pages and café menus.", "Film or photograph one farm visit per season and tie it to the matching product.", "Measure whether cards with producer names convert better than cards without — it's a two-week test."]) +
             '<p class="methodology-note">What this spec version leaves out: a real Brand Platform includes stakeholder interviews, a full competitive scan and a visual-direction document for a designer. None of that happened here; the drafts above are built only from Cafezal\'s own published text.</p>') + \
     CASE_CLOSE
page("case-study-cafezal.html", "Spec Project: Cafezal Milano — Studio Dudin",
     "An unsolicited Brand Platform audit: Cafezal's product pages name their farmers; the catalogue where people choose shows only a score and a price.", CZ, active="work.html")

# ================================================================ VELASCA
VL_Q_TITLE = it("Lo stile italiano fatto per durare", "Italian style made to last")
VL_Q_HOME = it("Manifattura artigianale Made in Italy", "Artisan manufacturing, Made in Italy") + " and " + it("Fai un salto — In bottega", "Drop by — in the shop")
VL_Q_ORIGIN = it("Velasca nasce a Milano con un’idea: portare l’artigianato italiano nel presente, direttamente tra le mani di chi lo sceglie.", "Velasca was born in Milan with one idea: to bring Italian craftsmanship into the present, directly into the hands of the people who choose it.")
VL_Q_FAMILY = it("il mestiere non si insegna solamente, ma si tramanda", "the craft isn't just taught, it's handed down")
VL_Q_MONTE = it("dal più antico distretto calzaturiero d’Italia: Montegranaro, nelle Marche", "from Italy's oldest shoemaking district: Montegranaro, in the Marche")
VL_Q_BOTTEGA = it("Noi la chiamiamo casa", "We call it home")
VL_Q_MOON = it("Sarà come andare sulla Luna restando in un paio di scarpe.", "It'll be like going to the Moon without leaving a pair of shoes.")
VL_Q_FUN = it("Comincia subito a divertirti, con stile.", "Start having fun right away, in style.")
VL_Q_SPEC = it("Fatto a: Montegranaro (Fermo – Marche)", "Made in: Montegranaro (Fermo, Marche)")

VL = case_hero("Spec project — Positioning Audit",
               "Velasca: a Milan brand with <em>Milan</em> hidden in the shoe names.",
               "Velasca has everything a direct-to-consumer brand wishes it had: named workshops, a real district, more than twenty shops, a playful voice and shoes named in Milanese dialect. The homepage says “Made in Italy” — like everyone else.",
               "Reviewed 26 September 2026 · Scope: homepage, Chi siamo (About), the shops page, the lace-up collection and a product page at it.velasca.com, compared with three direct competitors. Public material only: no interviews, no data, nothing internal. Velasca's Italian site is quoted in the original with my English translation in brackets.") + \
     callout("This is speculative work, not a client relationship",
             "I picked Velasca and this gap on my own initiative — no engagement, no affiliation, nothing commissioned, nothing beyond what's public on their site. It exists to show how I'd approach a Positioning Audit, not to claim I was hired for one. If Velasca would rather this page not exist, email me and it comes down.") + \
     summary("Velasca owns five things no competitor can copy, and leads with the one thing every competitor says.",
             "It was born in Milan to sell Italian craft directly, without the usual chain in between. It works with family workshops in Montegranaro, Italy's oldest shoemaking district. It has more than twenty “botteghe” it calls home. Its shoes carry Milanese dialect names. And its newsletter writes like a friend with a sense of humour. The homepage, in words, says: artisan manufacturing, Made in Italy, drop by the shop. That is the category's entry ticket, not a reason to choose.") + \
     section("section-white", "Scorecard", "Where the brand stands today, in four categories.",
             scorecard([("Product &amp; proof", "Strong"), ("Differentiation (as said)", "Weak"), ("Voice consistency", "Mixed"), ("Story reaching the buyer", "Mixed")]) +
             '<p class="measure muted small" style="margin-top: var(--space-lg);">The product page shows 4.5 stars from 1,229 reviews and names the town where the shoe is made. The substance is there. What\'s missing is a headline that says what only Velasca can say.</p>') + \
     section("section-paper", "01 — What a buyer sees first", "A beautiful homepage that says “Made in Italy.”",
             f'<p class="measure">The homepage is almost entirely photography. The words a visitor actually reads are the page title, {VL_Q_TITLE}, and two tiles: {VL_Q_HOME}. Each is true. None is specific to Velasca: “Made in Italy,” “artisanal” and “timeless” are what every Italian-made menswear brand says, including the competitors below.</p>' +
             f'<p class="measure muted">Photography can carry mood; it can\'t carry an argument. A first-time visitor leaves the homepage knowing Velasca makes good-looking Italian shoes and clothes — and not knowing why they should buy them here rather than from the next Italian brand.</p>') + \
     section("section-white", "02 — What Velasca actually has", "Five assets, all published, none on the homepage.",
             figure("velasca-chi-siamo.jpg", "Velasca Chi siamo page: Qualità e stile a modo nostro. Velasca nasce a Milano con un’idea.", "it.velasca.com/pages/chi-siamo — “Qualità e stile a modo nostro” (“Quality and style, our way”), as published, 26 September 2026", "narrow") +
             deliverables([
                 ("A founding idea", f"<p>{VL_Q_ORIGIN} “Directly” is the whole business model — Italian workshops, no chain of intermediaries — and it appears once, on the About page.</p>"),
                 ("A real place and real people", f"<p>The shoes come {VL_Q_MONTE}. The workshops are small, often family-run, where {VL_Q_FAMILY}. The product page confirms it: {VL_Q_SPEC}. Named fabric partners follow on the About page — Thomas Mason for shirting, Vitale Barberis Canonico for suiting.</p>"),
                 ("Shops that feel like home", f"<p>More than twenty “botteghe,” from five in Milan to Paris and Munich, described as places for a chat and a hello: {VL_Q_BOTTEGA}. The homepage tile reduces this to “drop by the shop.”</p>"),
                 ("Milan in the names", "<p>The lace-ups are called Giacalustra, Caffettee, Brumista, Cavadent — Milanese dialect, several of them old city trades (the brumista was the coachman, the cavadent the tooth-puller). It's a charming, ownable detail. Nowhere on the collection or product page is it explained.</p>" + figure("velasca-stringate-grid.jpg", "Velasca lace-up collection: Giacalustra, Caffettee and Brumista oxfords at €320.", "it.velasca.com/collections/stringate — the names are shown, never explained")),
                 ("A voice with a smile", f"<p>The newsletter sign-up says {VL_Q_FUN} The confirmation promises {VL_Q_MOON} That's a distinct, likeable voice — and it lives in form messages, while the brand pages speak in heritage and timelessness.</p>"),
             ])) + \
     section("section-paper", "03 — Competitive scan", "“Made in Italy” is the entry ticket. The story is the product.",
             scan_table([
                 ("Velasca", "Italian style made to last; artisan manufacturing, Made in Italy.", "4.5 stars from 1,229 reviews, 20+ shops, named district and mills", "Men (with a separate women's site), in shop and online"),
                 ("Scarosso", "“The best of Made in Italy quality meets style!”", "Online shop, Made in Italy claim", "Men and women, online"),
                 ("Suitsupply", "Made-to-measure and personalised suits — “Don't just fit in, find your own perfect fit.”", "Italian fabrics, in-store alterations, custom programme", "Men, stores and online"),
                 ("Bexley", "Men's shoes and clothes, by category.", "Customer reviews on the homepage", "Men, online and stores"),
             ], "Velasca") +
             '<p class="measure" style="margin-top: var(--space-lg);">Suitsupply owns fit. Scarosso says “Made in Italy” louder. Bexley sells the catalogue. Nobody in the scan owns <em>where</em> and <em>who</em> — a named town, named workshops, a city identity. Velasca has all three on its About page. It is the only one of the four that could lead with Milan and Montegranaro and be telling the truth.</p>' +
             '<p class="measure muted small">Competitor lines are quoted or summarised from their homepages and homepage descriptions as published on 26 September 2026.</p>') + \
     section("section-white", "04 — Audience read", "Who buys, and what tips them.",
             deliverables([
                 ("The first-time online buyer", "<p>Finds a €320 oxford and hesitates: is it worth it next to a department-store brand? The answer — made in Montegranaro, sold directly — is on another page. The product page's “Fatto a” line is the right instinct; it needs a sentence of why.</p>"),
                 ("The shop visitor", "<p>Walks into a bottega and gets the “home” experience the About page describes. The site should send them there with that promise, not with a store locator alone.</p>"),
                 ("The Milanese and the visitor to Milan", "<p>A dialect name is a small joy for someone from Milan and a souvenir for someone who isn't. Both would enjoy knowing what “Brumista” means. Neither is told.</p>"),
             ])) + \
     section("section-paper", "05 — Direction", "What the brand could say instead.",
             '<p class="lede">A draft built only from Velasca\'s own published words — the positioning a paid engagement would pressure-test, not a finished answer.</p>' +
             deliverables([
                 ("Draft positioning", "<p class='lead-line'>“Made in Montegranaro. Sold in Milan's way — directly, and with a smile.”</p><p>It names the place instead of the country, keeps the founding idea (directly), and lets the voice that already exists in the newsletter into the headline.</p>"),
                 ("Message order", "<p><strong>Where:</strong> Montegranaro and the family workshops. <strong>How:</strong> directly from them to you, in shop or online. <strong>Who we are:</strong> a Milan brand — which is why the shoes carry Milanese names. <strong>Proof:</strong> 1,229 reviews, 20+ botteghe.</p>"),
                 ("Name cards", "<p>One line per product: “Brumista — the Milanese coachman. Semi-brogue in calf leather, made in Montegranaro.” It costs nothing to produce, makes every product page more memorable, and turns the catalogue into a small guide to the city.</p>"),
             ])) + \
     section("section-white", "06 — One-page action plan", "If this were a paid engagement, it would start here.",
             tiers(["Add one line under the homepage hero: made in Montegranaro, sold directly.", "Explain each dialect name in one sentence on its product page.", "Move the founding sentence from the About page to the homepage."],
                   ["Rewrite the “In bottega” tile around “We call it home” and the shop experience.", "Let the newsletter's voice into product and collection copy — one smile per page, not a joke per line.", "Put the review score on collection pages, not only product pages."],
                   ["Build a “Montegranaro” page: the district, the workshops, the people, as far as they want to be named.", "Give the Società Benefit status and the impact report a line on the About page instead of only the footer.", "Test the Milan-names angle in one campaign and measure product-page time and conversion."]) +
             '<p class="methodology-note">What this spec version leaves out: a paid Positioning Audit adds a working session with the team, access to analytics and sales data by channel, and customer interviews. None of that happened here. The direction above is a first draft from public material, meant to be argued with.</p>') + \
     CASE_CLOSE
page("case-study-velasca.html", "Spec Project: Velasca — Studio Dudin",
     "An unsolicited Positioning Audit: Velasca has Montegranaro workshops, 20+ botteghe and shoes named in Milanese dialect — and a homepage that only says Made in Italy.", VL, active="work.html")


# ---------------------------------------------------------------- redirects for retired URLs (GitHub Pages ignores _redirects)
REDIRECTS = {"about.html": "approach.html", "services.html": "approach.html#services",
             "process.html": "approach.html#process", "notes.html": "work.html", "clients.html": "work.html"}
for old, new in REDIRECTS.items():
    with open(os.path.join(OUT, old), "w", encoding="utf-8") as f:
        f.write(f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Studio Dudin</title>
<meta http-equiv="refresh" content="0; url={new}"><link rel="canonical" href="https://www.studiodudin.com/{new.split('#')[0]}">
<meta name="robots" content="noindex"></head><body><p><a href="{new}">Continue to Studio Dudin</a></p></body></html>
""")
with open(os.path.join(OUT, "_redirects"), "w") as f:
    f.write("".join(f"/{o}   /{n.split('#')[0]}   301\n" for o, n in REDIRECTS.items()))

# 404 page
page("404.html", "Page not found — Studio Dudin", "This page doesn't exist.", """
<section class="hero page-hero">
  <img src="brand-assets/d-mark-ink.svg" alt="" class="hero-d" aria-hidden="true">
  <div class="wrap">
    <span class="eyebrow">404</span>
    <h1 class="page-title">This page doesn't exist.</h1>
    <p class="lede">It may have moved when the site was reorganised.</p>
    <div class="cta-row"><a href="index.html" class="btn btn-primary">Back to the homepage</a></div>
  </div>
</section>
""", active="")
print("built")
