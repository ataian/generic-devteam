---
name: project-lib-versioning
description: "Version changed project libraries with verified SemVer."
version: 1.0.0
author: "Derived static template; original authorship recorded in preservation audit"
license: MIT
metadata:
  hermes:
    tags: [libraries, versioning, semver]
    related_skills: [codex, kanban-review-handoff]
---

# Project library versioning

## When to Use

Load for an authorized project task that changes a self-owned library; this does not select a product stack or authorize a release.

## Procedure

When an authorized task changes a self-owned library, require Codex to bump its version according to semantic versioning. This is a versioning requirement, not optional cleanup. Use `pom.xml` and POM-specific rules only for a confirmed Maven structure; otherwise inspect the actual packaging metadata. Before implementation, inspect current version, parent/module inheritance, public API, usages and dependency versions; do not infer the bump from memory alone. Evaluate the diff against consumers: incompatible API or behavior requires MAJOR, backward-compatible functionality MINOR, backward-compatible fix PATCH. For `0.x` or project-specific `-SNAPSHOT`/release conventions, inspect the existing policy and resolve ambiguity with the planner rather than inventing a convention. Trace the full current dependency chain before changing versions. Verify all consumers against the current repository; for confirmed Maven projects include property-managed versions and dependencyManagement, otherwise use the actual packaging metadata. Update each affected consumer dependency and determine whether the consumer library needs its own appropriate version bump, then update its consumers. Follow the chain recursively for every affected library and consumer; do not stop after the first package (or POM in Maven). Verify effective dependency resolution and relevant builds/tests use the intended artifacts. Ensure Codex's task prompt explicitly names the version bumps, chain updates and rationale. Do not implement code directly; only Codex CLI writes productive project code. Confirm commit and Michelin review handoff as required by the task pipeline.
