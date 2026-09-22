# Design system framework

The production design system is not approved. Current values in
`src/styles/tokens.scss` are neutral bootstrap-only defaults, not brand choices.

## Pending creative direction

- Typography will be defined after creative direction and Figma approval.
- Palette will be defined after creative direction and Figma approval.
- Spacing, sizing, radius, and motion tokens will map approved Figma variables
  to CSS custom properties.
- Reusable interaction states will cover default, hover, focus-visible, active,
  disabled, loading, and error states where applicable.

## Responsive philosophy

Design content-first breakpoints; do not mirror device names or simply scale the
desktop layout down. Validate at 1440px, 1024px, 768px, and 390px, plus stress
test content between those widths.

## Accessibility constraints

Target WCAG AA where applicable: sufficient contrast, visible focus, semantic
structure, keyboard usability, meaningful alternatives for media, reduced
motion, and no hover-only information. Prefer native elements to unnecessary
ARIA.
