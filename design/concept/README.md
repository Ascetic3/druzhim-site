# «Живая нить» — design handoff

This directory contains the provisional selected homepage concept. It is
design-only: the React/Vite site is still the technical bootstrap. The source
of the local boards is `build_boards.py`; `manifest.json` lists all board sizes,
titles and text. The earlier raster studies in `references/` are retained for
traceability and should not be regenerated.

## Open for review

- `screens/desktop-1440.svg` — assembled 1440 px homepage, header through footer.
- `sections/01-header.svg` through `sections/12-footer.svg` — 12 separate desktop sections.
- `screens/mobile-hero-390.svg`, `mobile-audience-390.svg`, `mobile-foster-390.svg`, `mobile-season-390.svg`, `mobile-contact-390.svg` — five key mobile compositions.
- `screens/mobile-menu-open-390.svg`, `mobile-faq-390.svg` — two mobile interaction states.
- `screens/system-states.svg` and `screens/motion-storyboard.svg` — shared design states and motion intent.

The SVGs reference local files in `fonts/` and `references/still-life.png`.
Open them from this directory or through a local file server so those assets
resolve correctly. The still life is illustrative, pending approved photography.

## Figma transfer status

[Figma file](https://www.figma.com/design/5rxBgN9AgG3vmrmD6eBM9m) has the
pages, variables, text styles and a foundations frame. The page for homepage
layouts is empty. The last MCP attempt hit the Starter tool-call limit before
creating any homepage or mobile frames; further calls were stopped. Existing
`desktop-transfer.json`, `mobile-transfer.json` and `other-transfer.json` hold
compact, editable geometry/text instructions extracted by `transfer_spec.py`.
Image placement, Figma visual QA and design approval remain to do. Do not use
`exports/foundations.png` for approval: it predates a Figma layout correction.

## Content status

Activity names, enrollment terms, contact channel, results, portrait and final
photography require verification. The boards label major placeholders. See
`docs/CONTENT_TODO.md` and `docs/PROJECT_STATE.md` in the project root.
