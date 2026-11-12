# TAS upstream extraction — review handoff

## Candidate and remaining dependency

The Maker consumes TAS as an external authoring dependency, not as team-role equipment.
The normative Maker copy is deleted; authoring routes through `references/upstream-sources.md#tas` to the standalone entrypoint and its required references.
Local commissioned authoring can use the sibling TAS working tree.

The Maker pin remains the real initial TAS commit `95c19de6f443f861a02fc0a71ecec0fd250adaf3` (TAS 1.0.0).
Noninteractive HTTPS `git ls-remote https://github.com/ataian/tas.git refs/heads/main` confirms that exact remote main identity.
SSH lookup failed with `Permission denied (publickey)`; no credentials or Git configuration were changed.
TAS 1.1.0 improvements are local and unpublished.
Max must commit/publish TAS, then advance the Maker pin to that actual verified revision before claiming portable consumption of the enhanced standard.
No future revision was invented, and no commit, push, live skill/profile change, installation, or service action was performed by this worker.

## Baselines and ownership

- TAS: `/home/mariko/projects/tas`, branch `main`, starting HEAD `95c19de6f443f861a02fc0a71ecec0fd250adaf3`.
- Maker: `/home/mariko/projects/generic-devteam`, branch `v3`, starting HEAD `2a71dedc1c697f3aacde5fcfd4c51a14a3089df3`.
- Both working trees were clean at start. HEADs were unchanged at the verification checkpoint.
- Candidate versions: TAS `1.1.0`; Maker `2.2.1`. The parent owns any later coherent release integration.
- Preserve concurrent commits; review starting HEAD through final HEAD plus remaining changes, not only `git diff HEAD`.

Concurrent Retro ownership is excluded from this worker: `skills/retro/**`, `skills/brownfield-feature-planning/references/project-retrospectives.md`, the conditional-retrospective router row in `skills/brownfield-feature-planning/SKILL.md`, and `references/test_retro.py`.
The parent integrates those files into shared manifest/docs/tests/versioning after this handoff.
This candidate does not include Retro manifest entries or semantics.
The Coder/Reviewer standards audit is read-only.

## Changed package files

TAS:
- Modified `SKILL.md`, `README.md`, `NOTICE.md`, `sources.json`, `references/tas-authoring-standard.md`, `tests/test_package.py`.
- Added `references/skill-mechanics.md`, `third_party/mattpocock/LICENSE`.

Maker:
- Modified `AGENTS.md`, `HERMES.md`, `SKILL.md`, `README.md`, `NOTICE.md`, `manifest.json`.
- Modified `references/upstream-sources.md`, `references/development-verification.md`, `references/test_render_reasoning.py`, `references/test_update_team.py`.
- Deleted `references/tas-authoring-standard.md`.
- Added this author-only handoff outside the package manifest.

## Method and preserved contracts

The TAS standard adapts the complete writing-for-agents method: reliable branched context pointers, context versus human cognitive load, information hierarchy, co-location, disclosure/sprawl, completion clarity and exhaustive demand, real sequence context boundaries, leading words for execution/invocation, positive prompting with hard guardrails, one source of truth, environment lookups, and evidence-based pruning.
The skill-only mechanics branch requires verified harness semantics for visibility and invocation controls; it does not claim portable `disable-model-invocation: true` support.
The installed TAS evaluation method is preserved in the standalone standard; the installed skill entry itself remains untouched for the parent to align.

Matt Pocock source: `https://github.com/mattpocock/skills`, commit `4ae2317ddb22b046e26455e4f9c9b3aaaf62212d`.
The full `SKILL.md`, required `SKILL-MECHANICS.md`, and `agents/openai.yaml` were read and compared with their exact Git objects.
`sources.json` records original and adapted hashes; the bundled Matt MIT license is byte-identical to the pinned original.
Original Caveman style/reference/legal bytes remain unchanged.
The current accepted Maker ticket policy was preserved, including the ticket-only short-bullet scope missing from the initial standalone snapshot.
No role template or existing own skill was changed by this worker.

## Executed verification

- TAS: `python3 -m unittest discover -s tests -p 'test_*.py' -v` — 11 tests passed, including relocation, missing/escaping references, source hashes, removed loading branches, and emptied method bodies with retained headings.
- Maker focused: `python3 -B -m unittest discover -s references -p 'test_render_reasoning.py' -v` — 62 passed.
- Maker aggregate: `python3 -B -m unittest discover -s references -p 'test_*.py' -v` — 155 run, OK with 16 native Kanban guard skips. Those transitions remain unexecuted in this delegated context; no guard bypass.
- The existing updater fixture now includes the TAS pin in same-version dependency gating without installing upstream assets.
- `git diff --check` passed in both repositories.
- Read-only package verification passed: exact inventories, sorted/unique manifest, version equality, links/anchors, JSON/YAML/Python syntax, actual source-object hashes, source/legal byte identity, and protected baseline bytes.
- At that checkpoint: TAS 17 public files/34 resolved local links; Maker 47 package files/170 resolved local links; 10 Python files parsed. Later Retro additions require parent integration and renewed inventory checks.
- The new method and routing assertions are static instruction contracts, not measured live-agent compliance, token savings, or runtime discovery. Existing renderer/updater/helper tests execute real code against isolated fixtures.

Evidence under `/home/mariko/.hermes/cache/scratch/`:
- `tas-upstream-tas-tests.txt` — original TAS test output.
- `tas-upstream-maker-tests.txt` — original focused and aggregate Maker output, including skip names.
- `tas-upstream-package-verification.txt` — package/source verification output and Git checkpoint.
- `verify_tas_upstream.py` — disposable read-only verifier; no runtime or installation machinery.

Independent review and parent integration remain outstanding; this handoff is the author's result, not an acceptance verdict.
