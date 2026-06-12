# Hum&Net — Landing Page Design Spec

**Date:** 2026-06-09
**Status:** Approved (design validated via visual companion)

## Goal

A dynamic, animated marketing landing page for **Hum&Net** (humandnet.com), an
enterprise software company. Dark navy + neon aesthetic inspired by the brand's
glassy ampersand mark. Spanish language. Single deployable page.

## Stack

- Plain **HTML + CSS + JavaScript**, single page, no build tools.
- **GSAP + ScrollTrigger** (CDN) for scroll-triggered animations and timelines.
- Fonts: **Inter Tight** (headlines) + **DM Sans** (body) via Google Fonts.
- All Bloom-generated brand assets downloaded locally into `assets/` so the page
  is self-contained and deployable (the Bloom logo signed URL expires ~7 days).

## Brand System (from Bloom analysis)

- Colors: magenta `#E91E63`, cyan `#00BCD4`, orange `#FF9800`, ink `#424242`, paper `#F5F5F5`.
- Page base: navy `#070b1a` / `#0b0f21`.
- Signature gradient: magenta → purple → cyan → orange.
- Product: **Hôlos ERP®** (cloud ERP). Partner badge: **Platinum Business Partner CONTPAQi®**. 30+ years.

## Assets (Bloom, brand session 70fed438-1581-496a-9cdf-03e242175698)

| Purpose | Bloom image | Notes |
|---|---|---|
| Logo (nav + footer) | `logo_url` from bloom_get_brand | wordmark PNG; download locally |
| Hero ampersand | `3c2f2f96-e7fd-4152-b56a-1bb146323ade` | chosen Variant 2, glassy glass, background removed (transparent PNG) |
| Page background watermark | same transparent ampersand (faint) | fixed, low-opacity, behind all sections |
| Hôlos ERP section visual | `5978323e-73ef-44f8-8080-a4e8db7e49cd` | businessman + holographic interface |

## Page Structure (Option A — Impact First)

1. **Nav** (fixed, glass blur) — logo, links (Servicios, Hôlos ERP, Nosotros, Contacto), "Agendar demo" CTA.
2. **Hero** (cinematic) — full viewport.
3. **Stats** — 4 columns: 30+ años, 200+ empresas, 500+ proyectos, 98% satisfacción.
4. **Servicios** — 6 cards: Consultoría, Hôlos ERP®, CONTPAQi®, Talento, BI, Cloud.
5. **Hôlos ERP** — two-column: copy + feature list left, real businessman image right.
6. **CTA** — email capture, gradient headline.
7. **Footer** — logo, copyright, links.

## Hero — Detailed

- **Background**: navy with radial magenta/cyan glows; faint 64px grid overlay; 3 blurred drifting orbs (magenta, cyan, orange); a cyberpunk **scanline** sweeping top→bottom on a loop.
- **Ampersand**: transparent glassy cutout, ~58% viewport width (max 720px), right side.
  - Neon glow via `drop-shadow` (magenta + cyan).
  - **CSS reflection** below it: `-webkit-box-reflect: below -28px linear-gradient(transparent 46%, rgba(255,255,255,0.40))` (user requested stronger reflection).
  - Continuous floating "bob" animation.
  - **Motion A — Cursor Tilt 3D**: ampersand rotates in 3D toward the mouse position
    (`rotateY`/`rotateX` up to ~28°/22°, slight scale), eased, resets on mouse leave.
    Disabled on touch / `prefers-reduced-motion`.
- **Text** (left): eyebrow tag, headline "Tecnología y desarrollo humano que transforman
  organizaciones." (with gradient on "desarrollo humano"), subhead, the
  "Innovación. Integración. Evolución." color tags, two CTA buttons.
  Entrance: GSAP staggered fade-up on load.
- **Trust row**: "Platinum Partner CONTPAQi®" + "+30 años".

## Page-wide ampersand watermark

- Fixed-position transparent ampersand, huge (~140vw), centered, rotated ~-8°,
  opacity ~0.06–0.10, slight blur, slow "breathe" animation. Sits at z-index 0
  behind all content so the mark is felt through the whole page. `pointer-events:none`.

## Other sections — Motion (smooth/professional, per "dramatic hero, clean content")

- **Stats**: GSAP ScrollTrigger — count-up animation on enter; cards fade-up.
- **Servicios**: staggered fade-up of the 6 cards on enter; hover lifts card + accent bar.
- **Hôlos**: text slides in from left, image from right on enter; subtle parallax on the image.
- **CTA**: fade + scale-in on enter.
- All scroll animations one-shot (no reverse jank); respect `prefers-reduced-motion`.

## Responsiveness

- Desktop-first; breakpoints at ~1024px and ~640px.
- Mobile: ampersand moves above/behind text or scales down centered; stats 2×2; services 1 col; Hôlos stacks; nav collapses to a simple menu.
- Cursor-tilt replaced by device-orientation-free gentle float on touch.

## Out of scope (YAGNI)

- No backend / form submission wiring (CTA form is visual; can POST later).
- No CMS, routing, or multi-page.
- No real testimonials section (Option A excludes it).

## File layout

```
index.html
assets/css/styles.css
assets/js/main.js
assets/img/logo.png
assets/img/ampersand.png        (transparent glassy hero mark)
assets/img/holos-erp.png        (businessman/holographic)
```
