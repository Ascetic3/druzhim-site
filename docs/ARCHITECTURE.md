# Architecture

## Directory map

- `src/app`: application composition and root application code.
- `src/components`: reusable UI components.
- `src/sections`: page-level website sections.
- `src/hooks`: reusable React hooks.
- `src/lib`: utilities and third-party integration helpers.
- `src/data`: editable organization/content data separated from presentation.
- `src/styles`: reset, global rules, shared CSS tokens, and restrained SCSS tools.
- `src/assets`: project-owned static assets.
- `src/types`: shared types when multiple features genuinely need them.

The homepage now uses `src/sections/Header`, `Hero`, and named sections in
`HomeSections.tsx`. `src/components/Action` owns shared CTA behavior and
styling; `src/data/home.ts` holds repeatable audience, activity and FAQ copy.
Self-hosted fonts and the provisional WebP image live in `src/assets`. The
remaining mapped directories are populated only when needed.

## Composition

`src/main.tsx` mounts the root application. `src/app/App.tsx` composes page
sections. Page-specific blocks live in `src/sections`; UI reused across sections
lives in `src/components`.

The demo is built with Vite's `/druzhim-site/` base so asset URLs work under
GitHub Pages' repository path. `.github/workflows/pages.yml` validates, builds,
and deploys the `dist` artifact on pushes to `master`.

## Data and content

Keep editable facts and repeatable content in `src/data`, typed when that adds
safety. Components should receive content through props instead of embedding
large organization datasets in JSX.

## Styling

Global reset and document-level defaults live in `src/styles`. Shared runtime
design values are CSS custom properties. Component and section styles use
co-located `*.module.scss` files.

## Motion and integrations

Keep simple motion in component SCSS. Put reusable GSAP setup, ScrollTrigger
helpers, and cleanup utilities in `src/lib` or focused hooks; keep section-only
timelines beside their section. Third-party integrations belong in `src/lib`.

The current page uses local effects in Hero and HomeSections for one-time GSAP
path/photo motion. Each effect cleans up through GSAP context or matchMedia;
mobile and reduced-motion views remain static. This motion is section-specific,
so no shared animation infrastructure was added.

Local `AGENTS.md` files are reserved for future complex sections with durable,
section-specific invariants; they must not duplicate the root contract.
