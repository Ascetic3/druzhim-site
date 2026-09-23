# ДРУЖИМ — public website

Production website project for АНО «Центр социализации детей и молодежи
\"ДРУЖИМ\"».

The homepage follows the provisional local «Живая нить» design concept. Its
desktop and mobile design boards are in `design/concept/`; factual content and
imagery still awaiting approval are labeled on the page and in
`docs/CONTENT_TODO.md`.

[View the GitHub Pages demo](https://ascetic3.github.io/druzhim-site/).

## Stack

React, Vite, TypeScript, SCSS Modules, CSS custom-property tokens, and focused
GSAP/ScrollTrigger motion.

## Setup and development

```bash
npm install
npm run dev
```

## Checks and build

```bash
npm run typecheck
npm run lint
npm run format:check
npm run build
```

Use `npm run preview` to inspect the production build locally.

## Demo deployment

The Vite base is `/druzhim-site/`. A push to `master` runs
`.github/workflows/pages.yml`, which validates, builds and deploys `dist` through
GitHub Pages Actions. The source repository includes the earlier bootstrap
commit and the design artifacts; generated `dist` is not committed.

## Folder map

- `src/app`: root application composition.
- `src/components`: reusable UI.
- `src/sections`: page-level sections.
- `src/hooks`: reusable hooks.
- `src/lib`: utilities and integrations.
- `src/data`: editable organization content.
- `src/styles`: global styles and tokens.
- `src/assets`: project-owned assets.
- `src/types`: shared types.
- `docs`: project state, architecture, design, motion, decisions, content, and
  tooling notes.

Agents must start with [`AGENTS.md`](./AGENTS.md), then read the short project
state and architecture documents it references.
