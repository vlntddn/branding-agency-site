#!/usr/bin/env node
// Renders the 1200x630 link-preview images (og:image) into images/share/,
// one per page in sitemap.xml, from each page's hero eyebrow and headline.
// Run after build_site.py:  NODE_PATH=$(npm root -g) node make_share_cards.js
// Needs Playwright with Chromium, and network access for Google Fonts (the fonts
// are fetched here and inlined, so the headless browser itself needs no network).
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const ROOT = __dirname;
const OUT = path.join(ROOT, 'images', 'share');
const svg = (f) => 'data:image/svg+xml;base64,' + fs.readFileSync(path.join(ROOT, 'brand-assets', f)).toString('base64');
const text = (s) => s.replace(/<[^>]+>/g, '').replace(/\s+/g, ' ').trim();
const esc = (s) => s.replace(/&(?!\w+;|#\d+;)/g, '&amp;').replace(/</g, '&lt;');

const pages = [...fs.readFileSync(path.join(ROOT, 'sitemap.xml'), 'utf8').matchAll(/<loc>[^<]*\/([^/<]*)<\/loc>/g)]
  .map((m) => m[1] || 'index.html');

// Latin subsets of Archivo 800 and IBM Plex Mono 500, as inline @font-face rules.
async function fonts() {
  const ua = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36';
  const css = await (await fetch('https://fonts.googleapis.com/css2?family=Archivo:wght@800&family=IBM+Plex+Mono:wght@500',
    { headers: { 'User-Agent': ua } })).text();
  const latin = css.split('/*').filter((b) => b.startsWith(' latin */'));
  let out = '';
  for (const b of latin) {
    const family = b.match(/font-family: '([^']+)'/)[1];
    const weight = b.match(/font-weight: (\d+)/)[1];
    const buf = Buffer.from(await (await fetch(b.match(/url\(([^)]+)\)/)[1])).arrayBuffer());
    out += `@font-face { font-family: '${family}'; font-weight: ${weight}; src: url(data:font/woff2;base64,${buf.toString('base64')}) format('woff2'); }\n`;
  }
  if (latin.length !== 2) throw new Error('Could not load the Archivo and IBM Plex Mono fonts');
  return out;
}

const card = (fontCss, eyebrow, h1) => `<!DOCTYPE html><html><head><meta charset="UTF-8">
<style>
  ${fontCss}
  * { margin: 0; box-sizing: border-box; }
  body { width: 1200px; height: 630px; background: #000; color: #fff; overflow: hidden; position: relative;
         padding: 64px 72px; display: flex; flex-direction: column; justify-content: space-between; }
  .d { position: absolute; right: -90px; bottom: -60px; height: 640px; opacity: 0.07; }
  .logo { height: 64px; width: auto; align-self: flex-start; }
  .mono { font: 500 20px/1.3 'IBM Plex Mono', monospace; text-transform: uppercase; letter-spacing: 0.14em; color: rgba(255,255,255,0.72); }
  h1 { font: 800 ${h1.length > 70 ? 52 : 60}px/1.06 Archivo, sans-serif; letter-spacing: -0.02em; max-width: 960px; margin-top: 22px; }
  .rule { border-top: 1px solid rgba(255,255,255,0.18); padding-top: 22px; }
  main, .rule { position: relative; }
</style></head><body>
  <img class="d" src="${svg('d-mark-paper.svg')}" alt="">
  <img class="logo" src="${svg('lockup-signature-paper.svg')}" alt="">
  <main><div class="mono">${esc(eyebrow)}</div><h1>${esc(h1)}</h1></main>
  <div class="rule mono">studiodudin.com</div>
</body></html>`;

(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  const fontCss = await fonts();
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1200, height: 630 } });
  for (const f of pages) {
    const html = fs.readFileSync(path.join(ROOT, f), 'utf8');
    const eyebrow = text((html.match(/<span class="eyebrow">([\s\S]*?)<\/span>/) || [, 'Studio Dudin'])[1]);
    const h1 = text((html.match(/<h1[^>]*>([\s\S]*?)<\/h1>/) || [, ''])[1]);
    await page.setContent(card(fontCss, eyebrow, h1));
    await page.evaluate(async () => { await document.fonts.load("800 60px Archivo"); await document.fonts.load("500 20px 'IBM Plex Mono'"); });
    const out = path.join(OUT, f.replace('.html', '.png'));
    await page.screenshot({ path: out });
    console.log(path.relative(ROOT, out));
  }
  await browser.close();
})();
