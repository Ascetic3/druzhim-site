# Project

Druzhim public website for АНО «Центр социализации детей и молодежи \"ДРУЖИМ\"».

Tech stack:

- React
- Vite
- TypeScript
- SCSS Modules
- CSS custom-property design tokens
- GSAP/ScrollTrigger only where appropriate
- Figma as the visual source of truth for approved designs

## Context loading strategy

Before changing code:

1. Read this root `AGENTS.md`.
2. Read `docs/PROJECT_STATE.md`.
3. Read `docs/ARCHITECTURE.md`.
4. Read only documentation relevant to the requested task.
5. Locate relevant code with repository search.
6. Open only the files necessary for the task.

Do not scan or reread the whole repository by default. Use repository search
first. Escalate to broader inspection only when architecture is unclear or a
change actually spans multiple systems.

## Figma

Approved Figma screens are the visual source of truth. Before implementing an
approved Figma section:

- inspect its design context and relevant variables;
- inspect the approved screenshot;
- inspect motion context when relevant;
- reuse existing project conventions and components;
- map relevant Figma variables to project CSS custom properties.

Do not approximate an approved layout from memory.

## Styling

- Use SCSS Modules for component styles.
- Use `global.scss` only for truly global rules.
- Use shared CSS custom properties for design tokens.
- No Tailwind and no CSS-in-JS.
- Avoid inline styles for ordinary styling.
- Do not hardcode an existing design token.

## Components

- Page-level sections belong in `src/sections`.
- Reusable UI belongs in `src/components`.
- Do not create abstractions simply for abstraction's sake.
- Prefer understandable code over framework-like internal infrastructure.

## Motion

- Use CSS for simple motion.
- Use GSAP for complex coordinated timelines, SVG drawing, or scroll
  storytelling.
- Respect reduced motion and ensure information stays accessible without motion.
- Do not hijack scrolling.
- Prefer transforms and opacity; avoid layout-thrashing animation.

## Responsive design

Desktop design must not simply shrink onto mobile. Visual QA should check at
minimum 1440px, 1024px, 768px, and 390px.

## Accessibility

Target WCAG AA where applicable. Use semantic HTML, keyboard-operable controls,
visible focus, sufficient contrast, meaningful alt text, and correct native
control semantics. Do not hide information behind hover alone. Prefer native
HTML over unnecessary ARIA.

## Performance

- Optimize images and prefer AVIF/WebP where sensible.
- Lazy-load below-the-fold media.
- Avoid giant background video unless specifically justified.
- Avoid layout-thrashing animation and unbounded scroll listeners.
- Prefer transforms/opacity and use SVG for suitable vector artwork.
- Do not add dependency bloat.

## Documentation maintenance

- After meaningful implementation changes, update `docs/PROJECT_STATE.md`.
- After architecture changes, update `docs/ARCHITECTURE.md`.
- After design-system changes, update `docs/DESIGN_SYSTEM.md`.
- After motion-system changes, update `docs/MOTION.md`.
- Record only non-obvious, durable decisions in `docs/DECISIONS.md`.
- Do not turn documentation into a chronological stream of tiny edits.

When a complex section develops important local invariants, it may receive a
local `AGENTS.md` such as `src/sections/Hero/AGENTS.md`. Keep only section-specific
Figma references, SVG topology, animation ordering, ownership, mobile
differences, and invariants there. Do not duplicate this root file.

## Quality

Before completing code changes, run the relevant `typecheck`, `lint`, and
`build` commands. Run browser QA for visual changes and fix issues introduced by
the change.
