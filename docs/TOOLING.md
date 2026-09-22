# Tooling

Last checked: 2026-09-22

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

Do not run the workflow before the creative brief is available.

## Figma integration

No Figma MCP tools are exposed to this task, so no authenticated read-only check
was possible. The official Figma plugin was listed as available but not installed
in the environment-provided catalog; the plugin suggestion endpoint did not make
it eligible for installation from this task.

Manual action: open the Codex/ChatGPT desktop **Plugins** directory, install the
official **Figma** plugin, complete its connection/authentication prompt, then
start a new Codex task. In the new task, verify the connection with a read-only
request against an actual approved Figma file; do not create a random file.

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

The workspace is a Git repository with no existing commits or configured remote
at bootstrap time. No remote is created and no history is rewritten.

## Bootstrap validation

- `npm install`: complete; lockfile created; npm reported 0 vulnerabilities.
- `npm run typecheck`: pass.
- `npm run lint`: pass with zero warnings.
- `npm run format:check`: pass.
- `npm run build`: pass; Vite production bundle created in `dist/`.
- `npm run dev`: pass at `http://127.0.0.1:5173/`.
- Browser smoke test: the minimal Russian-language shell rendered and the
  browser console contained no warnings or errors.
