# Branding Agency — website

Public marketing site: homepage, services, about, contact.

## Stack

- **Next.js (App Router) + TypeScript** — file-based routing gives us
  separate `/`, `/services`, `/about`, `/contact` routes for free, static
  generation by default, and a straight line to Vercel deploys.
- **Tailwind CSS v4** — utility classes keep the editorial, grid-heavy
  layout consistent (shared paper/ink/signal-red theme in
  `src/app/globals.css`) without hand-rolling a component library.
- **Vercel** — zero-config deploys from this repo; pushes to `main`
  redeploy production automatically.

Optimized for shipping a real, on-brand site fast — not for architectural
ambition. No CMS, no database, no auth: copy lives in the page files and
is meant to be edited directly until there's a real content-management
need.

## Structure

```
src/
  app/
    layout.tsx       shared shell: <Nav>, <Footer>, fonts, metadata
    page.tsx          /            homepage
    services/page.tsx /services
    about/page.tsx    /about
    contact/page.tsx  /contact
    globals.css        theme tokens (paper / ink / signal accent)
  components/
    nav.tsx, footer.tsx, ui.tsx (Container, Eyebrow, Index)
```

## Getting started

```bash
npm install
npm run dev       # http://localhost:3000
npm run build     # production build
```

## Deploy

Linked to Vercel; every push to `main` deploys to production automatically.
