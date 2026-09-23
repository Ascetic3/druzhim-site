# Design system framework

The provisional «Живая нить» concept has one design language. It is documented in `design/concept/screens/system-states.svg` and represented in the [Figma project](https://www.figma.com/design/5rxBgN9AgG3vmrmD6eBM9m) by two variable collections (49 variables total) and 11 text styles. The local SVG concept is the current implementation reference while Figma canvas review is unavailable. `src/styles/tokens.scss` now maps its palette, spacing, typography and controls to CSS custom properties.

## Concept foundations

- Typography: Literata for display and headings; Golos Text for body and controls. Local font files and licenses are in `design/concept/fonts/`.
- Palette: paper `#F7F5EF`, forest `#203C32`, clay `#9D442F`, sage `#E3E9DE`, muted `#59655D`, border `#B7C1B4`; hover `#142C23`, pressed `#0C2119`, disabled `#D6DBD2`.
- Figma collections: `Druzhim / Primitives` (23) and `Druzhim / Concept` (26), with semantic color, spacing, radius and control-size variables. The same concept values are in shared CSS custom properties; reconcile them with the approved Figma values when canvas access returns.
- Desktop composition: 1440 px, 12 columns, 80 px outer margins, 24 px gutters. The 390 px compositions use four columns, 24 px outer margins and 16 px gutters. Intermediate widths need review during implementation.
- Controls: 56 px primary buttons, navigation targets at least 48 px, visible 2 px focus treatment with 3 px gap. The states board covers default, hover, pressed, focus and disabled, plus menu/FAQ states.
- The older concept boards show connecting lines and nodes. The website no longer uses that decoration; typography, section rhythm, color fields and spacing carry the editorial composition.

## Responsive philosophy

Design content-first breakpoints; do not mirror device names or simply scale the
desktop layout down. Validate at 1440px, 1024px, 768px, and 390px, plus stress
test content between those widths.

## Accessibility constraints

Target WCAG AA where applicable: sufficient contrast, visible focus, semantic
structure, keyboard usability, meaningful alternatives for media, reduced
motion, and no hover-only information. Prefer native elements to unnecessary
ARIA.

The illustrative still life in the foster-family concept is a reference, not approved organization photography. Portrait, results and contact details remain placeholders pending verification.
