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
