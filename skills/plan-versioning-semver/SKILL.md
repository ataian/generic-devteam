---
name: plan-versioning-semver
description: "Use when naming plans or app/library SemVer, changelog, API."
version: 1.3.0
author: Mariko
platforms: [linux]
metadata:
  hermes:
    tags: [planning, semver, naming, docs]
    category: devops
---

# Versioning plans, applications and libraries

Four rules stand on their own: plan-file names, the version API, the CHANGELOG, and SemVer
for the application version and each self-owned library. Each one applies whenever its situation occurs — while
writing a plan, in a ticket, or in a conversation. Writing a plan is not a prerequisite.

## When to use

- Name or rename a plan, review, ADR, handoff or specification file.
- Create or change the version API of a project.
- Create or change the `CHANGELOG.md` of a project.
- Set, classify or discuss the version of an application or a self-owned library.

## Plan file naming scheme

```
<TYP>_<Appversion>_<Name>_v<Number>.md
```

- **Type prefix** first, in capitals: `PLAN_`, `REVIEW_`, `ADR_`, `HANDOFF_`, `SPEC_`. It
  names the kind of document, not its version.
- **Appversion** directly after the prefix: the SemVer version of the project from which
  the change is planned.
- **Name:** one or two words, readable, without version numbers. The project name appears
  only on the first plan file; after that the name identifies the feature.
- **Number** last, always with `v`: `v1` for the first revision, `v2` after the first
  change. Plans, reviews and handoffs count whole numbers; SemVer applies to the
  application itself.
- Example: `PLAN_1.3.0_API-Returncode_v1.md`.

## Rules

1. Each new plan file starts at `v1`.
2. Each change to an existing plan file increases its number by one (`v1` → `v2`). Rename
   with `git mv` so the history stays intact.
3. Plans with different name slugs count independently of each other.
4. A new feature on an existing state gets its own plan file and starts at `v1`.
5. Update internal references to the old name (AGENTS.md, README.md, the "Ergänzt …" lines
   in feature plans).
6. Bugfixes in **application code** do not change a plan number; the application version
   follows SemVer.

## After creating the files

- Point AGENTS.md at the current plan name (binding specification).
- Update the README.md structure block to the versioned files.

## Version API

Base equipment for every project that provides an API.
A public endpoint that serves the application version — without auth, because the version
must be readable for health checks and compatibility without a key:

```http
GET /api/version
→ {"version": "2.0.0", "name": "<projectname>"}
```

- One source for the version number; do not maintain it in several places.
- Test: the endpoint answers 200 without a key even when auth is enabled.

## CHANGELOG.md

File in the repository root, Keep-a-Changelog style:

```markdown
# Changelog

## [2.0.0] - YYYY-MM-DD
### Changed
- …

## [1.1.0] - YYYY-MM-DD
### Added
- …
```

- One entry per release version (X.Y.Z) with its date.
- Categories: `Added`, `Changed`, `Fixed`, `Removed`.
- Maintain it with every release (part of the definition of done).

## Application and library versions

The application version follows SemVer:

- **MAJOR** for an incompatible change of API or behavior,
- **MINOR** for a backward-compatible feature,
- **PATCH** for a backward-compatible fix.

Classify each change of the application version by these three cases. The same rule applies
when the version is decided in conversation, in a ticket, or while planning — a plan is not
needed for a version decision.

The three classes apply to the application version and to each self-owned library. A changed library carries its own version step; a consumer library that needs one after its dependency changes carries it as well, and its own consumers follow.
