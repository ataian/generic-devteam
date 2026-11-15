---
name: plan-versioning-semver
description: "Use when naming plan files: Typ_Appversion_Name_vN.md."
version: 1.1.0
author: Mariko
platforms: [linux]
metadata:
  hermes:
    tags: [planning, semver, naming, docs]
    category: devops
---

# Versioning plan files

Project plans and specifications carry their own version number in the filename, separate
from the SemVer version of the project they apply to. Document type and revision are
readable from the name without opening the file.

## Naming scheme

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
  change. Plans, reviews and handoffs count whole numbers; SemVer applies to the project
  itself.
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

## Standard: version API and CHANGELOG

Base equipment for every project.

### 1) Version API

Only for projects that provide an API.
A public endpoint that serves the application version — without auth, because the version
must be readable for health checks and compatibility without a key:

```http
GET /api/version
→ {"version": "2.0.0", "name": "<projectname>"}
```

- One source for the version number; do not maintain it in several places.
- Test: the endpoint answers 200 without a key even when auth is enabled.

### 2) CHANGELOG.md

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

### 3) Application version (SemVer) versus plan version

The application version follows SemVer: MAJOR for an incompatible API change, MINOR for a
new feature, PATCH for a bugfix.

A plan file carries two versions in its name: the appversion of the project state from
which the change is planned, and, at the end, the running number of the document's own
revisions. An application change does not rename the plan file.

Example: the application stands at 1.3.0. The plan covers the incompatible change of the
API return code 303→201. The plan file is named `PLAN_1.3.0_API-Returncode_v1.md`; a
revision of the same plan becomes `…_v2.md`. The application receives the MAJOR bump to
2.0.0 during implementation; the filename stays.
