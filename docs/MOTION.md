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

## Selected-direction storyboard

`design/concept/screens/motion-storyboard.svg` describes the provisional
«Живая нить» motion. Hero text is accessible immediately; a connecting path
draws once over roughly 180–900 ms, the meeting node resolves by about 1200 ms,
and the composition then rests. Foster-family photography may reveal once in
400 ms; second-season paths may converge once in 500 ms. Menu and FAQ state
changes are local 160–200 ms transitions. This is a design specification, not
implemented behavior.

At reduced motion, paths and nodes appear in their final state with no masks,
movement or scroll-linked effects. Mobile uses a static connecting line. Text
and actions remain visible if animation code does not load. No pinning,
parallax, or scroll interception is planned.

The one-time hero path sequence is implemented with GSAP on widths at least
900 px and is skipped for reduced motion. The foster-family reference image
and second-season paths are static so they are visible before scrolling and
cannot pause in a partially drawn state. Mobile lines stay static. Menu and
FAQ state changes use short CSS motion. No pinning, scrubbing, parallax or
scroll interception is used.
