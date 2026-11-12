# Maker package changes

Use the existing package SemVer in `SKILL.md` and `manifest.json`.
Update both version fields together for every delivered Maker package change.
Use a MAJOR bump for an incompatible change.
Use a MINOR bump for compatible functionality.
Use a PATCH bump for a compatible fix, documentation change, recipe change, or script extraction.
Apply one bump to a coherent changeset or release, not one bump per file or test correction.
Keep historical commits and their version values unchanged.
Record the package version and exact Maker commit separately in setup and update evidence.

Before editing agent-context Markdown, load the complete upstream TAS entrypoint and required references through [TAS authoring upstream](references/upstream-sources.md#tas).
Apply TAS to every new or changed instruction in those files.
Keep role-template changes and live-team rollout as separate authorizations.
Run `python3 -B -m unittest discover -s references -p 'test_*.py'` before committing package changes.

For explicit Maker development or review, use [Development verification](references/development-verification.md).
Do not require those checks during ordinary team setup.
