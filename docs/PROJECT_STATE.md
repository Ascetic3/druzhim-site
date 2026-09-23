# Project state

Last updated: 2026-09-23

## Current phase

The provisional «Живая нить» homepage is implemented in the existing React/Vite project from the local concept. Its typography, palette, content and editorial section order remain in place; decorative connection-line artwork has been removed from the website. The older SVG boards remain historical concept references rather than exact current layouts. Figma canvas transfer and approval are still outstanding.

The configured GitHub Pages URL is
https://ascetic3.github.io/druzhim-site/. The repository is
https://github.com/Ascetic3/druzhim-site, retaining the original bootstrap
commit. `.github/workflows/pages.yml` validates, builds and deploys the Vite
output from `master`. Vite uses `/druzhim-site/` as its asset base.

## Implemented homepage

- Shared CSS custom properties now use the concept palette, spacing, typography and control values; Literata and Golos Text are self-hosted with licenses.
- Header, hero, audience, foster families, activities placeholder, second-season CTA, mission, director, results placeholder, FAQ, final CTA and footer are implemented as semantic React sections with SCSS Modules.
- The responsive layout has been checked locally at 1440, 1024, 768 and 390 px. Audience/Foster Families no longer collide, Foster Families keeps its two-column 1024 px layout, and FAQ height follows expanded content.
- Decorative SVG paths, circles, mobile variants and CSS connection nodes are absent from the rendered website. Hero, Foster Families, Activities, Season, Mission and Contact spacing was tightened; the desktop Contact control now balances its text column. The Hero-only GSAP path animation and dependency were removed. Menu and FAQ retain short CSS state transitions.
- Mobile navigation opens and closes with keyboard support and focus return; FAQ uses native `details/summary`. Internal section links work. The final contact control is deliberately disabled until a verified contact channel exists.
- The illustrative foster-family still life is served as an optimized WebP reference, with a visible provisional caption. No unverified results, contacts, schedule or participation terms were introduced.

## Design inventory

- [Figma project](https://www.figma.com/design/5rxBgN9AgG3vmrmD6eBM9m): pages `00 / Обзор и направления`, `01 / Главная — макеты`, `02 / Система и motion`; two variable collections (`Druzhim / Primitives`: 23 variables; `Druzhim / Concept`: 26 variables), 11 text styles, and one foundations frame (`5:4`) on the system page. The first two pages contain no frames. The foundations frame was corrected structurally after its last screenshot, but the correction has not been visually rechecked in Figma.
- `design/concept/references/`: 15 existing raster references, including the earlier direction studies, selected-section studies, mobile reference and illustrative still life. No further direction exploration was run.
- `design/concept/fonts/`: local Literata and Golos Text font files and licenses.
- `design/concept/sections/`: 12 desktop SVG sections from header through footer.
- `design/concept/screens/desktop-1440.svg`: assembled 1440 px homepage (6896 px tall).
- `design/concept/screens/`: seven 390 px mobile compositions/states: hero, audience, foster families, second-season CTA, contact, open menu and FAQ. Also contains the design-system states board and motion storyboard.
- `design/concept/manifest.json`: board sizes, palette and text inventory. `design/concept/*-transfer.json`: prepared instructions for later editable Figma transfer. `design/concept/build_boards.py` and `transfer_spec.py` reproduce these design artifacts; see `design/concept/README.md`.
- `design/concept/exports/foundations.png` is an earlier Figma screenshot, **stale** after a layout correction. It must not be treated as final visual approval.

## Local concept and implementation

The design boards remain in `design/concept/`. The implementation lives in `src/sections`, `src/components`, `src/data/home.ts`, `src/styles` and `src/assets`. Literata/Golos Text and the paper/forest/clay/sage palette remain. The line motif on the older boards is no longer part of the website. The local concept is still provisional rather than formally approved in Figma.

The visual correction retained the existing copy and section order. The director portrait remains a neutral, labeled placeholder, and the results area still contains only verified provisional statements. No replacement graphics were added for the removed line artwork.

## Incomplete

- The complete homepage and mobile boards are **not yet on the Figma canvas**. An attempted editable transfer was blocked by the Figma Starter MCP tool-call limit; no new frames were written in that attempt. Further Figma calls were stopped immediately.
- Figma canvas visual QA and organization approval remain outstanding. A current, approved portrait and organization photography are still missing.
- Activity details, participation terms, contacts, factual results, portrait and final photography require verification. Draft copy and image placeholders are marked in the boards; see `docs/CONTENT_TODO.md`.
- A confirmed contact method is needed before activating the final CTA. FAQ answers about enrollment and contacts must be supplied; the page currently labels them as pending.

## Next step

Obtain and verify the outstanding organization content and media, then replace the labeled placeholders and activate a real contact action. When Figma access returns, transfer the existing boards to `01 / Главная — макеты` and `02 / Система и motion`, inspect and approve the concept there, and reconcile any approved differences in code.
