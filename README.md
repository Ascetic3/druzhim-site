# ДРУЖИМ — public website

Production website project for АНО «Центр социализации детей и молодежи
\"ДРУЖИМ\"».

The current repository contains the technical bootstrap only. Production visual
design, content, site sections, and motion have not been implemented.

## Stack

React, Vite, TypeScript, SCSS Modules, CSS custom-property tokens, and GSAP for
future complex motion where justified.

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
