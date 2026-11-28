---
name: build-evidence
description: Use when tests depend on build or container evidence.
version: 0.1.0
author: Max, Mariko (Hermes Agent)
license: MIT
platforms: [linux]
metadata:
  hermes:
    tags: [testing, build, docker, jfr]
    related_skills: [dev-environment, diagnosing-bugs]
---

# Build-dependent test evidence

- Trigger: a check's result depends on build mode, generated test identifiers, container wiring or process observation.
- Read the reference for the observed mode completely before writing or accepting the check.
- A fixture that reproduces a failure proves that fixture, not the production build, the running page or the real process.

## References

- [Production-build selectors](references/production-build-selectors.md)
- [Portless test containers](references/portless-testcontainers.md)
- [JFR socket observer](references/jfr-observer.md)

## Verification

- Name the build mode, the running target and the observation limit in the result.
- Distinguish a check that exercised the real target from one that exercised a reconstruction.
- If disposable Cypress cleanup deletes the recording, plan pixel capture before the run. For headless Electron, use the native Cypress recording, not the Xvfb root, which can be black.
- Extract only relevant post-login app frames inside the verified test container. Crop out the runner log. Never copy raw recordings that may contain credentials or delay scoped cleanup.
- Report print-interface DOM evidence separately from native PDF evidence.
