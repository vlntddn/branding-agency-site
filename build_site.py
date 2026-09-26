#!/usr/bin/env python3
"""Generates the Studio Dudin static site into ./build (shared header/footer)."""
import os

OUT = os.path.dirname(os.path.abspath(__file__))
EMAIL = "valentinddn2803@gmail.com"
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

WORK_CARDS = """
    <div class="work-grid">
      <a href="case-study-ivana-vegetti.html" class="work-card">
        <div class="work-thumb" style="background-image:url('images/ivana-vegetti-homepage.jpg');"></div>
        <span class="work-kicker">Spec project · Brand Strategy Core</span>
        <h3>Ivana Vegetti</h3>
        <p>A luxury wedding studio whose homepage promise and its own client testimonials pull in different directions.</p>
      </a>
      <a href="case-study-cafezal.html" class="work-card">
        <div class="work-thumb" style="background-image:url('images/cafezal-homepage.jpg');"></div>
        <span class="work-kicker">Spec project · Brand Platform</span>
        <h3>Cafezal Milano</h3>
        <p>A specialty roaster whose farm-to-cup story is printed on the bag — and missing from the product page.</p>
      </a>
      <a href="case-study-socialbooth.html" class="work-card">
        <div class="work-thumb no-photo"><img src="brand-assets/d-mark-ink.svg" alt=""></div>
        <span class="work-kicker">Positioning Audit · Past affiliation disclosed</span>
        <h3>Socialbooth</h3>
        <p>A strong homepage promise that doesn't survive the trip to the paid landing pages.</p>
      </a>
    </div>
"""

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
{WORK_CARDS}
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
    <p class="lede">Studio Dudin is new: two spec projects and one disclosed audit, no paying clients yet. I'm not going to dress that up — pretending otherwise would be exactly the kind of vague brand move I'd flag in yours.</p>
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
    <form class="contact-form" id="contact-form" data-to="{EMAIL}">
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
        <button type="submit" class="btn btn-primary">Write the email</button>
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

# --- Socialbooth (disclosed past affiliation; audit only)
SB = case_hero("Case study — Positioning Audit",
               "Socialbooth: a strong promise that doesn't travel.",
               "An independent read of Socialbooth's current public brand: where the homepage makes an ownable claim, and where the pages most buyers actually land on quietly take it back.",
               "Reviewed September 2026 · Scope: homepage and paid-search landing pages at socialbooth.it — public material only.") + \
     callout("Disclosure",
             "Before founding Studio Dudin, I worked at Socialbooth. This page is separate from that job: an unsolicited audit of their <em>current</em> public brand, built only from what anyone can see on their site today — not commissioned, and not drawing on anything learned internally. If anyone at Socialbooth would rather this page not exist, email me and it comes down.") + f"""
<section class="section-paper">
  <div class="wrap">
    <span class="eyebrow">Independent read — today's site</span>
    <h2>Where the brand stands now, from the outside.</h2>
    {deliverables([
        ("Category position", "<p>Socialbooth operates across eight Italian cities with a wide capability set — photobooths, videobooths, interactive installations, advergaming, AI-driven experiences, branded merchandise. That range is a real strength. It's also a positioning risk: when a company can build almost anything, the brand has to work harder to say what it's <em>for</em>, or “does everything” reads as “known for nothing.”</p>"),
        ("The promise, on the homepage", "<p>The headline — <em>“Non siamo fornitori. Siamo parte del risultato del tuo evento”</em> (“We're not vendors. We're part of your event's result.”) — is a strong, ownable position. It's close to the sentence a Positioning Audit is built to produce: specific, a little contrarian, and hard for a generic competitor to say with a straight face.</p>"),
        ("Where the promise doesn't travel", "<p>The paid-search page built for “photobooth milano” — plausibly the first page many prospects ever see — is headlined <em>“Photobooth a Noleggio per Eventi e Fiere”</em> (“Photobooth Rental for Events and Trade Shows”) and closes on <em>“Richiedi un preventivo”</em> (“Request a Quote”). That's category-generic rental language, close to indistinguishable from an equipment-hire company. The promise lives on the homepage; for a meaningful share of first-touch traffic, the brand reads like the “vendor” the homepage rejects.</p>"),
        ("One-page action plan", "<p>If this were a paid engagement, the plan would start here:</p><ul class='plain-list'><li>Carry “part of the result,” not “rental,” onto every paid landing page — for many buyers that's the only page they ever see.</li><li>Lead with one differentiator per audience instead of four equally weighted benefits (lead generation for marketers, attendee engagement for event planners). Four claims at once reads as none.</li><li>Group the catalog by outcome — leads, content, engagement, data — instead of by equipment. Buyers remember what a thing gets them, not what it's called.</li></ul>"),
    ])}
  </div>
</section>
""" + CASE_CLOSE
page("case-study-socialbooth.html", "Case Study: Socialbooth — Studio Dudin",
     "A Positioning Audit of Socialbooth's current public brand, with past affiliation disclosed up front.", SB, active="work.html")

# --- Ivana Vegetti (spec)
IV = case_hero("Spec project — Brand Strategy Core",
               "Ivana Vegetti: the page says one thing. Her clients say another.",
               "A homepage built entirely on artistry and emotion. Three client testimonials that praise something else almost completely — honesty, directness, someone who won't give you a generic answer. That gap is the whole job.",
               "Reviewed 18 September 2026 · Scope: homepage, About and published client testimonials at ivanavegetti.it — the same material a client would hand over on day one. No interviews, no private information.") + \
     callout("This is speculative work, not a client relationship",
             "I picked Ivana Vegetti's studio and this gap on my own initiative — no engagement, no affiliation, nothing commissioned, nothing beyond what's public on her site. It exists to show how I'd approach a Brand Strategy Core, not to claim I was hired for one. If Ivana Vegetti would rather this page not exist, email me and it comes down.") + f"""
<section class="section-paper">
  <div class="wrap">
    <span class="eyebrow">Scorecard</span>
    <h2>Where the brand stands today, in four categories.</h2>
    {scorecard([("Aesthetic execution", "Strong"), ("Message–proof alignment", "Weak"), ("Differentiation", "Mixed"), ("Conversion clarity", "Mixed")])}
    <p class="measure muted small" style="margin-top: var(--space-lg);">Aesthetic execution is strong — photography, copy rhythm and polish are well above what a boutique studio usually manages alone. The gap isn't craft. It's that the brand's strongest asset — what clients say about working with her — never makes it into the words she's chosen for herself.</p>
  </div>
</section>

<section class="section-white">
  <div class="wrap">
    <span class="eyebrow">The gap</span>
    <h2>What the homepage promises vs. what clients actually praise.</h2>
    <figure class="evidence-figure">
      <img src="images/ivana-vegetti-homepage.jpg" alt="Screenshot of the Ivana Vegetti homepage hero: 'Every wedding designed by Ivana Vegetti, wedding planner in Italy, tells a story of modern elegance — tailored like a bespoke gown: unique, unrepeatable, and deeply moving.'">
      <figcaption>ivanavegetti.it — homepage, as published, 18 September 2026</figcaption>
    </figure>
    {gap("What she says about herself", "“Modern elegance,” “bespoke gown,” “an emotion, a journey, a promise.” Aesthetic, aspirational, unattached to anyone's actual experience.",
         "What clients say about her", "“Honest, and direct.” “Found the right compromises.” “Respecting our taste, with remarkable professionalism.” Grounded, about trust and judgment under pressure.")}
    <div class="compare">
      <div class="compare-col compare-bad">
        <h3>The homepage says</h3>
        <ul>
          <li>Weddings framed as “one-of-a-kind pieces of art,” “tailored like a bespoke gown.”</li>
          <li>Italy itself described as “an emotion, a journey, a promise.”</li>
          <li>The pitch is aesthetic and emotional — beauty as the organizing idea.</li>
        </ul>
      </div>
      <div class="compare-col compare-good">
        <h3>Her clients actually say</h3>
        <ul>
          <li>Ilaria: “She was our anchor — supportive, patient, honest, and direct. You'll never get a generic suggestion from her.”</li>
          <li>Isabel: “She didn't just understand us as a couple — she empathized with us, found the right compromises.”</li>
          <li>Erica: “Always respecting our taste, with remarkable professionalism.”</li>
        </ul>
      </div>
    </div>
    <p class="measure muted" style="margin-top: var(--space-xl);">Nobody came back talking about “emotion” or “journey.” They came back talking about trust, judgment and being told the truth. Three separate people volunteered a version of the same trait — and right now it's buried under language that could belong to almost any luxury wedding studio in Italy.</p>
  </div>
</section>

<section class="section-paper">
  <div class="wrap">
    <span class="eyebrow">What a Brand Strategy Core would produce</span>
    <h2>Not a critique — a draft of the real deliverable.</h2>
    <p class="lede">A first pass at four pieces of a Brand Strategy Core — unsolicited, not yet sharpened by client input or interviews.</p>
    {deliverables([
        ("Draft positioning statement", "<p class='lead-line'>“The wedding planner who won't tell you what you want to hear — only what actually works, and then makes it beautiful.”</p><p>This keeps the artistry she clearly delivers, but leads with the trait three clients volunteered: she's direct. That's harder to copy than “bespoke,” because it can't be claimed — it has to be shown on every call.</p>"),
        ("Audience read: who's actually deciding", "<p>Her “Real Weddings” portfolio and press features (Elle Spose, Lovenozze, The Real Wedding) put her in front of couples who've already shortlisted 3–4 planners on aesthetics alone. At that stage aesthetics are table stakes. What breaks the tie is what the testimonials show and the homepage doesn't: proof that she'll say no to a bad idea before it costs them money.</p>"),
        ("Messaging framework, two audiences", "<p><strong>Full Planning</strong> — lead with judgment: “You're not hiring someone to say yes to everything. You're hiring someone who'll tell you when an idea won't work — before it costs you money to find out.”</p><p><strong>Day-of Coordination</strong> — lead with trust under pressure: “The day only goes wrong when no one in the room is willing to make a call. That's the job.”</p>"),
        ("Voice guide, one do/don't pair", "<p><strong>Don't:</strong> “Every wedding is a unique journey of beauty and emotion.” — true of every planner's homepage, provable by no one.</p><p><strong>Do:</strong> “I'll tell you if the venue you love won't work for 140 guests. That's what you're actually paying for.” — specific, checkable, and what her own clients say made the difference.</p>"),
    ])}
  </div>
</section>

<section class="section-white">
  <div class="wrap">
    <span class="eyebrow">One-page action plan</span>
    <h2>If this were a paid engagement, it would start here.</h2>
    <ul class="plain-list">
      <li>Move the homepage headline from an aesthetic promise (“bespoke,” “emotion”) to the trait clients cite unprompted — directness and judgment — and let the photography carry the beauty.</li>
      <li>Pull the strongest testimonial lines into the hero and service pages verbatim, with attribution. Right now they sit on a separate page doing none of the persuasive work they could.</li>
      <li>Differentiate the service tiers by the judgment call each one asks of her, not only by scope.</li>
      <li>Interview two or three past clients (the Core deliverable this spec skips) to find the exact moment they started trusting her — that becomes the anchor story for the About page.</li>
    </ul>
    <p class="methodology-note">What this spec version leaves out: a real Brand Strategy Core starts with up to three stakeholder interviews and a written competitive scan against named competitors. Neither happened here. The statement and messaging above are a plausible first draft, not a final answer.</p>
  </div>
</section>
""" + CASE_CLOSE
page("case-study-ivana-vegetti.html", "Spec Project: Ivana Vegetti — Studio Dudin",
     "An unsolicited Brand Strategy Core audit: where Ivana Vegetti's homepage promise and what her clients say pull in different directions.", IV, active="work.html")

# --- Cafezal (spec)
CZ = case_hero("Spec project — Brand Platform",
               "Cafezal: the specificity already exists. It just never leaves the bag.",
               "The homepage sells direct farmer relationships and a coffee academy. The product grid sells a score out of 100 and a name. The real story — origin, process, tasting notes — is already printed on the packaging. It just isn't on the page.",
               "Reviewed 18 September 2026 · Scope: homepage, full coffee catalog (16 products) and product packaging photography at cafezal.it — public material only. No interviews, no private information.") + \
     callout("This is speculative work, not a client relationship",
             "I picked Cafezal Milano and this gap on my own initiative — no engagement, no affiliation, nothing commissioned, nothing beyond what's public on their site. It exists to show how I'd approach a Brand Platform, not to claim I was hired for one. If Cafezal would rather this page not exist, email me and it comes down.") + f"""
<section class="section-paper">
  <div class="wrap">
    <span class="eyebrow">Scorecard</span>
    <h2>Where the brand stands today, in four categories.</h2>
    {scorecard([("Sourcing story (exists)", "Strong"), ("Sourcing story (on the page)", "Weak"), ("Packaging system", "Strong"), ("Catalog scannability", "Mixed")])}
    <p class="measure muted small" style="margin-top: var(--space-lg);">Splitting “sourcing story” into two rows is the point of this audit: the same brand scores completely differently depending on whether you look at the packaging photography or the page text next to it. One brand whose best material didn't make it into every format.</p>
  </div>
</section>

<section class="section-white">
  <div class="wrap">
    <span class="eyebrow">The gap</span>
    <h2>Zoom into any product photo. The story's already there.</h2>
    <div class="evidence-row">
      <figure class="evidence-figure">
        <img src="images/cafezal-product-grid.jpg" alt="Screenshot of the Cafezal coffee catalog grid: product cards showing only a name, an SCA score like '84.5pts', a star rating and a price — no origin, process or tasting notes in the text.">
        <figcaption>cafezal.it/collections/coffee — catalog grid, as published</figcaption>
      </figure>
      <figure class="evidence-figure">
        <img src="images/cafezal-aurora-label.jpg" alt="Zoomed detail of the Aurora Bio packaging photography: Meti Kebele, Guji, Ethiopia; notes of raspberry, milk chocolate and strawberry biscuit; cultivar 74110/74112; altitude 2000m; natural process; cupping score 89.">
        <figcaption>Same product — text printed on its own packaging photo</figcaption>
      </figure>
    </div>
    {gap("What the page text says", "“Aurora Bio” · Specialty Coffee Capsules · €5.90–€65.00. No origin, no process, no tasting note in the copy a buyer reads while scrolling.",
         "What the packaging photo says", "“Meti Kebele, Guji, Ethiopia · notes of raspberry, milk chocolate and strawberry biscuit · altitude 2000m · natural process · cupping score 89.” All of it, already written — on the bag.")}
    <p class="measure muted">A sharper finding than “Cafezal has no sourcing story” — they clearly do, and their packaging already has a clean template for telling it (origin → tasting notes → cultivar/altitude → process → cupping score). That template just never becomes page text, so it's invisible to anyone scanning the grid, to search engines and to screen readers.</p>
  </div>
</section>

<section class="section-paper">
  <div class="wrap">
    <span class="eyebrow">What a Brand Platform would produce</span>
    <h2>Not a critique — a draft of the real deliverable.</h2>
    <p class="lede">A first pass built only from Cafezal's own, already-public packaging copy — nothing invented.</p>
    {deliverables([
        ("Draft positioning statement", "<p class='lead-line'>“Everything we know about a bag, you know too — before you open it.”</p><p>This turns “direct relationships with farmers” — today a homepage claim with nothing on the product page to check it against — into a standard the catalog can visibly meet, because the information already exists.</p>"),
        ("Product-page voice, before/after (real data)", "<p><strong>Now, on the grid:</strong> “Aurora Bio (Bio) — Ethiopia · Specialty Coffee Capsules · €5.90”</p><p><strong>With the packaging's own words on the page:</strong> “Aurora Bio — Meti Kebele, Guji, Ethiopia. Notes of raspberry, milk chocolate and strawberry biscuit. Natural process, 2000m altitude, cupping score 89.”</p>"),
        ("Direction note", "<p>The packaging's label structure is already a good template. A Brand Platform's guidelines would make it the mandatory copy block for every format — product page, shelf card, and the Coffee Academy's teaching materials — so the specificity survives everywhere the product appears.</p>"),
    ])}
  </div>
</section>

<section class="section-white">
  <div class="wrap">
    <span class="eyebrow">One-page action plan</span>
    <h2>If this were a paid engagement, it would start here.</h2>
    <ul class="plain-list">
      <li>Transcribe the packaging label template into a standard product-page copy block for all 16 products. Copywork, not new research — the facts already exist.</li>
      <li>Fold the Coffee Academy's expertise into product pages — a one-line “what this means” per tasting term — instead of keeping education and retail apart.</li>
      <li>Put the same block in indexable page text, not only image alt text, so it shows up when someone searches “Ethiopia natural process coffee Milan.”</li>
    </ul>
    <p class="methodology-note">What this spec version leaves out: a real Brand Platform includes stakeholder interviews, a full competitive scan and a visual-direction document ready for a designer. None of that happened here; the template above is a first draft built from Cafezal's own packaging text.</p>
  </div>
</section>
""" + CASE_CLOSE
page("case-study-cafezal.html", "Spec Project: Cafezal Milano — Studio Dudin",
     "An unsolicited Brand Platform audit: Cafezal's packaging already carries the specificity its product pages are missing.", CZ, active="work.html")

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
