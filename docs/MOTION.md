# Motion

Motion should communicate connection, progression, and relationships rather
than exist as decoration.

## Technology choice

- Use CSS transitions and keyframes for simple local state changes.
- Use GSAP + ScrollTrigger for coordinated timelines, complex scroll
  storytelling, SVG drawing, and complicated sequencing.
- Keep SVG path animation accessible and meaningful; never make it the only way
  information is conveyed.

## Rules

- No scroll hijacking.
- Every meaningful animation needs a reduced-motion strategy.
- Scroll animation must not block access to information.
- Avoid excessive simultaneous animation and universal fade-up effects.
- Prefer transforms and opacity; avoid layout thrashing.
- Register bounded listeners/triggers and clean them up with component lifecycles.
- Mobile motion may be simplified when density, input, or performance requires it.

GSAP is installed as capability only. No production timelines or ScrollTrigger
behavior exist yet.
