---
name: plan-versioning-semver
description: "Use when naming plans or app/library SemVer, changelog, API."
version: 1.3.1
author: Mariko
platforms: [linux]
metadata:
  hermes:
    tags: [planning, semver, naming, docs]
    category: devops
---

# Versioning plans, applications and libraries

Apply each rule independently wherever its trigger occurs, including in plans, tickets and conversation. No plan required.

## When to use

- File naming: name or rename a plan, review, ADR, handoff or specification.
- Version API or `CHANGELOG.md`: create or change it.
- SemVer: set, classify or discuss an application or self-owned library version.

## Plan file naming scheme

```
<TYP>_<Appversion>_<Name>_v<Number>.md
```

- Type prefix: capitals first. `PLAN_`, `REVIEW_`, `ADR_`, `HANDOFF_`, `SPEC_` identify document kinds.
- Appversion: immediately after the prefix. Use the project's SemVer at the state from which the change is planned.
- Name: one or two readable words without version numbers. Use the project name only on the first plan file. Later names identify features.
- Number: last, with `v`. Plans, reviews and handoffs use whole revisions (`v1` first, `v2` after the first change). Application versions use SemVer.
- Example: `PLAN_1.3.0_API-Returncode_v1.md`.

## Rules

- Give each new feature its own plan file. Start every new plan at `v1`; count revisions independently per name slug.
- Changed plan: increase the number by one (`v1` → `v2`). Rename with `git mv` to keep history, then update all internal references, including `AGENTS.md`, `README.md` and "Ergänzt …" lines in feature plans.
- Bugfix in application code: retain the plan number. Version the application by SemVer.

## After creating the files

- Point AGENTS.md at the current plan name (binding specification).
- Update the README.md structure block to the versioned files.

## Version API

Every API project needs a public version endpoint without authentication for keyless health and compatibility checks.

```http
GET /api/version
→ {"version": "2.0.0", "name": "<projectname>"}
```

- Version number: one source.
- Test: HTTP 200 without a key, including when auth is enabled.

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
- Update on every release as part of the definition of done.

## Application and library versions

- **MAJOR** for an incompatible change of API or behavior,
- **MINOR** for a backward-compatible feature,
- **PATCH** for a backward-compatible fix.

Classify each application and self-owned library version change by these three cases. Bump a changed library independently. Bump each consuming library that needs a version change after its dependency changes, and follow the same rule through its consumers.

Every change on its own branch increments the application version once, from the version checked out at the start branch, in the same commit as the change. A `-SNAPSHOT` suffix is a version like any other; treating the work as a pre-release addition is not an exemption. Name the class (`MAJOR`/`MINOR`/`PATCH`) when proposing the branch, and name the version fields the project actually carries.
