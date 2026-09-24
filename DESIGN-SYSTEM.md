# Studio Dudin — Design System

Near-monochrome by discipline. Signal Red is the one accent — used sparingly (primary CTAs, key inline links, highlights), never as a large fill. Everything else stays Ink Navy / near-black / paper / gray.

## Color

| Token | Hex | Use |
|---|---|---|
| `--navy` | `#0E1B2C` | Primary dark ink — headlines on light, dark section backgrounds |
| `--navy-light` | `#1C3049` | Secondary dark surfaces, gradients |
| `--navy-dark` | `#0A141F` | Footer, deepest navy |
| `--near-black` | `#111111` | Body text |
| `--red` | `#E8391B` | Signal Red — the one accent. CTAs, key links. Never a large fill. |
| `--red-dark` | `#C22E12` | Red hover state |
| `--paper` | `#F5F5F3` | Off-white ground |
| `--gray` | `#8C8F94` | Secondary/neutral text |
| `--white` | `#FFFFFF` | Text on navy backgrounds |

## Typography

| Token | Stack | Use |
|---|---|---|
| `--font-head` / `--font-display` | Archivo, Helvetica Neue, Arial, sans-serif | Headlines — bold 700–900, tight tracking (`-0.02em`) |
| `--font-body` | Inter, Helvetica Neue, Arial, sans-serif | Body copy, 17px base, 1.55 line-height |
| `--font-mono` | IBM Plex Mono, Courier New, monospace | Labels, prices, metadata, kickers |

Emphasis in headlines (`<em>`) is italic + medium weight, not a color change — except on navy/dark backgrounds, where it switches to white so it stays legible.

## Spacing scale

| Token | Value |
|---|---|
| `--space-xs` | 0.25rem |
| `--space-sm` | 0.5rem |
| `--space-md` | 1rem |
| `--space-lg` | 2rem |
| `--space-xl` | 4rem |
| `--space-2xl` | 7rem |

Max content width: `--max-width: 1120px`. Standard easing: `--ease: cubic-bezier(0.16, 1, 0.3, 1)`.

## Logo

Two marks, each in ink and paper variants, plus a repeating tile pattern — all in `brand-assets/`:

- **Nameplate** (wordmark): `nameplate-ink.svg` / `nameplate-paper.svg` — used in header/footer.
- **D-mark** (monogram): `d-mark-ink.svg` / `d-mark-paper.svg` — used as a large, low-opacity (0.08) watermark graphic (`.dmark-watermark`) on hero and dark sections, and as a placeholder tile on work cards that don't have a photo yet.
- **Tile pattern**: `d-tile-dark.svg` / `d-tile-light.svg` — repeating background texture, used sparingly.

## Core components (see `styles.css`)

- `.hero`, `.section-white` / `.section-paper` / `.section-navy` — page section rhythm
- `.btn-red` (primary CTA) / `.btn-outline` / `.btn-outline-navy` — button variants
- `.index-list` / `.index-row` — numbered service rows
- `.stats` — stat blocks (number + label)
- `.grid-3` — three-column principle/value grid
- `.faq` / `<details>` — expandable FAQ
- `.work-grid` / `.work-card` / `.work-thumb` (`.no-photo` variant uses the D-mark) — case study cards
- `.photo-frame` + variants (`.photo-hero`, `.photo-square`, `.photo-wide`, `.photo-founder`) — image slots with a navy-gradient fallback so a missing photo never breaks the layout
- `.bio-photo-row` — founder bio layout (photo + text side by side)
- `.dmark-watermark` — the D-mark used as a large faint background graphic

## Voice

**Clarity, Candor, Craft** (+ Access as a supporting pillar). Clear, candid, confident — short sentences, no filler or jargon ("synergy," "elevate," generic "storytelling").

## Source of truth

This file documents the tokens as implemented in `styles.css` in this repo. If the two ever disagree, `styles.css` is correct — update this file to match, not the other way around.
