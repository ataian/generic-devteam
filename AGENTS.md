# Maker package changes

## Version and evidence

Apply one SemVer bump per delivered Maker changeset or release. Update `SKILL.md` and `manifest.json` together.
Use MAJOR for incompatibility, MINOR for compatible functionality, and PATCH for compatible fixes, docs, recipes or script extraction.
Preserve historical commits and versions. Record package version and exact Maker commit separately in setup and update evidence.

## Instruction changes

Read and apply [CAC authoring](references/cac-authoring.md) before editing agent instructions.
Keep durable role decisions in the SOUL templates. Role-template edits and live-team rollout require separate authorization.

`test_brownfield_planning` caps the combined bytes of `skills/brownfield-feature-planning/SKILL.md` and each reference. Measure each affected pair with `wc -c` before and after prose edits. Prune or split `kanban-phase-release.md` to fit its near-full budget. Keep the ceiling.

Use [Development verification](references/development-verification.md) for explicit Maker development or review only.
Run `python3 -B -m unittest discover -s references -p 'test_*.py'` before committing package changes. Re-run after deletions because contract tests pin exact phrases.
