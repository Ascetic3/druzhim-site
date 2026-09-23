# Motion

Motion should clarify state changes rather than exist as decoration.

## Technology choice

- Use CSS transitions and keyframes for simple local state changes.
- Add a dedicated animation library only if a future interaction requires
  coordinated motion that CSS cannot express clearly.

## Rules

- No scroll hijacking.
- Every meaningful animation needs a reduced-motion strategy.
- Scroll animation must not block access to information.
- Avoid excessive simultaneous animation and universal fade-up effects.
- Prefer transforms and opacity; avoid layout thrashing.
- Register bounded listeners/triggers and clean them up with component lifecycles.
- Mobile motion may be simplified when density, input, or performance requires it.

## Current implementation

Menu and FAQ state changes use short CSS transitions. Text, images and actions
remain visible without animation. The old
`design/concept/screens/motion-storyboard.svg` records an earlier decorative
path proposal; none of its path or node animation is implemented. There is no
GSAP dependency, scroll animation, pinning, parallax or scroll interception.
