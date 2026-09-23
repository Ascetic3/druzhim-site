# Tooling

Last checked: 2026-09-23

## Local runtime

- Node.js: `v24.19.0`
- npm: `11.17.0`
- Git: `2.51.2.windows.1`

Package versions are recorded in `package.json` and locked in
`package-lock.json` after installation.

## Frontend stack

- React / React DOM: `19.3.0`.
- Vite: `8.3.0`; official React plugin: `6.1.1`.
- TypeScript: `6.0.3`, with strict project references. TypeScript 6 is pinned
  because the installed `typescript-eslint` `8.70.1` does not support TypeScript
  7 yet.
- Sass: `1.104.1`, with SCSS Modules for component styles.
- ESLint: `10.11.0`, flat configuration.
- Prettier: `3.9.8`.
- GSAP: `3.15.0`, installed for future justified complex motion; no production
  animation is implemented.

## frontend-app-builder / Build Web Apps

The Build Web Apps plugin was not present in the available plugin directory for
this task. The complete official OpenAI standalone skill was installed from:

`openai/plugins/plugins/build-web-apps/skills/frontend-app-builder`

User-level installation:

`C:\Users\Адм\.codex\skills\frontend-app-builder`

The installation includes `SKILL.md`, `agents/openai.yaml`, and the referenced
supporting material. Its manifest declares `name: frontend-app-builder`, so
future agents should invoke it explicitly as `$frontend-app-builder` when the
creative brief is provided. Codex detects new skills automatically; if it is not
listed in a new task, restart Codex.

The original creative brief is preserved at `design/concept/BRIEF.txt`. The
skill has been used for design exploration and the selected concept; do not
repeat the three-direction exploration.

## Figma integration

The official Figma MCP integration is available and was used to create the
[Druzhim concept file](https://www.figma.com/design/5rxBgN9AgG3vmrmD6eBM9m),
its pages, 49 variables, 11 text styles and a foundations frame. A subsequent
attempt to transfer the complete selected concept returned the Figma Starter
MCP tool-call-limit message. No homepage or mobile frames were written in that
attempt, and further MCP calls were stopped. The local SVG boards and compact
`*-transfer.json` specifications preserve the design for a later transfer.
The transfer data covers editable geometry and text; the still-life image must
be placed separately. The last foundations screenshot predates a structural
layout correction and is not a current QA image.

Browser login and MCP authentication are separate. The Figma file was not
visually verified in the browser while logged out. When the tool allowance is
available, inspect the existing file and transfer the saved boards rather than
recreating the direction studies or generating new references.

Official guidance:

- https://learn.chatgpt.com/docs/plugins
- https://developers.openai.com/blog/building-frontend-uis-with-codex-and-figma

## Commands

```bash
npm install
npm run dev
npm run typecheck
npm run lint
npm run format:check
npm run build
npm run preview
```

## Git

The workspace is a Git repository. Bootstrap commit `fefe72e` exists; design
work is currently uncommitted. No remote is configured by this design task.

## Bootstrap validation

- `npm install`: complete; lockfile created; npm reported 0 vulnerabilities.
- `npm run typecheck`: pass.
- `npm run lint`: pass with zero warnings.
- `npm run format:check`: pass.
- `npm run build`: pass; Vite production bundle created in `dist/`.
- `npm run dev`: pass at `http://127.0.0.1:5173/`.
- Browser smoke test: the minimal Russian-language shell rendered and the
  browser console contained no warnings or errors.
