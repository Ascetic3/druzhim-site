# Architecture decisions

## React + Vite + TypeScript

**Decision:** Use React with Vite and strict TypeScript.

**Reason:** The stack is fixed and provides a small, fast frontend foundation.

**Consequences:** The project remains a client-side Vite application unless a
future requirement justifies an architectural change.

## SCSS Modules and shared CSS tokens

**Decision:** Use SCSS Modules for local styles and CSS custom properties for
shared runtime design values.

**Reason:** Styles stay component-scoped while tokens remain inspectable,
themeable, and aligned with Figma variables.

**Consequences:** No Tailwind or CSS-in-JS; global styles stay intentionally
small.

## Figma as visual source of truth

**Decision:** Approved Figma designs supersede visual memory or approximation.

**Reason:** Implementation needs verifiable design context, variables,
screenshots, and motion intent.

**Consequences:** Approved screens are inspected before implementation and
compared visually afterward.

## Proportional motion tooling

**Decision:** Use CSS for simple motion and GSAP only for sufficiently complex
motion.

**Reason:** This limits runtime complexity while supporting planned storytelling.

**Consequences:** GSAP timelines require cleanup, reduced-motion behavior, and a
clear reason to exist.

## Concise project-state memory

**Decision:** Maintain focused project documents and a short `PROJECT_STATE.md`.

**Reason:** Future agents should load durable context without rereading the
repository.

**Consequences:** Git remains the detailed change history; documentation records
state and non-obvious decisions, not every edit.

## Selected homepage direction

**Decision:** Continue only «Живая нить» as the provisional homepage concept.
Use Literata, Golos Text, the paper/forest/clay/sage palette and a restrained
connecting-line motif across desktop and mobile. Earlier direction studies are
retained as historical references, not options to regenerate.

**Reason:** One visual language connects the audiences, activities and
second-season invitation while allowing factual content to be read without
animation.

**Consequences:** The local SVG boards are a reviewable design handoff while
Figma canvas transfer is blocked. They do not constitute Figma approval or
authorization to substitute invented program facts, statistics, contacts or
photography. The motif portion of this decision is superseded below.

## Retire decorative connection artwork from the website

**Decision:** Remove the connection-line motif and its path animation from the
website while retaining the existing typography, palette, content and section
order. The older concept boards remain historical references.

**Reason:** The user requested a quieter editorial composition without
decorative paths, circles or mobile variants.

**Consequences:** Spacing and existing content carry section rhythm. GSAP is no
longer needed by the runtime; no replacement graphics are introduced.
