# Production-build selectors

Use when a UI test needs an anchor that a framework adds only in some build modes.

- Check the repository for an existing test-ID pattern before using one: `git grep -n 'data-testid' -- <source-root>`.
  No hit means no such anchor exists.
- MUI emits `data-testid` only when `process.env.NODE_ENV !== 'production'`
  (`@mui/material/utils/createSvgIcon.js`). A production build drops the attribute.
- Derive selectors from rendered DOM at the target build mode or from the component source.
  Prefer an existing stable anchor: `aria-label`, role, visible text, or a source-defined attribute.
- Verify the selector against the production build or the running page.
  A development-mode fixture, a component test mount or a synthetic page proves only that mode.
- Record the build mode and the verified target in the result. A green fixture with different
  build mode remains an open check.
