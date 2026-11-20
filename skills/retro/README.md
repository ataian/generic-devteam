# Process retrospective

An explicit, read-only retrospective of how agents worked and what in their environment could improve.
It proposes changes; it does not judge product acceptance or apply maintenance automatically.

## Use without installation

Read [SKILL.md](SKILL.md) and its required [method](references/method.md), then request a process retrospective. The complete package works from its own directory without Maker or an upstream skill installation.

Required access is read-only: files, relevant history search and available task/run records. Missing history limits the result and is never reconstructed.

Examples:

- `/retro`
- `machen wir Retro`
- `Retrospektive zum letzten Lauf`
- `Run a process retrospective for session <session-id>.`
- `Run a process retrospective for ticket <ticket-id>, phases <range>.`

The default target is the current conversation. For a historical target, the skill needs accessible original records, including relevant worker records when available.

## Optional registration

1. Obtain explicit installation authorization. Before copying, inspect the target's active skill roots and built-in commands for a `retro` collision. Preserve existing packages and report conflicts. Do not rename or overwrite silently.
2. Copy the complete directory as `retro/` into the intended runtime's skill location. Keep `SKILL.md`, `README.md`, `references/method.md`, `LICENSE` and `NOTICE.md` together and unchanged.
3. In Hermes, verify one intended `retro` identity and complete loaded content with native catalog/main/reference readbacks. Verify that native discovery supplies `/retro` on the intended communication surface before claiming registration. The description also supports explicit natural-language requests. Do not rely on `disable-model-invocation` to enforce explicit-only use in Hermes.

Package files alone establish neither target installation nor discovery.

## Output and authority

Expect short, sourced process proposals in severity order, with causes, owners, benefits and trade-offs. A smooth or poorly evidenced run may support no changes.
Any change requires user selection and explicit implementation scope. Native `/refine` skill-and-memory maintenance remains a separate user action.

## Verification and provenance

The Maker development check is `python3 -B -m unittest discover -s references -p 'test_retro.py' -v`, run from the Maker root.
It uses an already available `ruamel.yaml` or PyYAML safe parser.
That check covers package structure, metadata, reference reachability, source attribution, and static instruction scenarios with deletion mutations.
It does not run inference, prove model behavior, measure token savings, or verify a live target.
The test is development equipment, not an installed runtime dependency.

See [NOTICE](NOTICE.md) for Matt Pocock's exact upstream revision and the deliberate adaptations.
See [LICENSE](LICENSE) for MIT terms.
