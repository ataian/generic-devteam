# Process retrospective

An explicit, read-only retrospective of how agents worked and what in their environment could improve.
It proposes changes; it does not judge product acceptance or apply maintenance automatically.

## Use without installation

Read [SKILL.md](SKILL.md) and its required [method](references/method.md), then request a process retrospective.
The complete package works from its own directory without the Maker or any upstream skill installation.
Required capabilities: read files, search relevant history, and inspect available task/run records read-only.
Missing history limits the result; it is not reconstructed.

Examples:

- `/retro`
- `machen wir Retro`
- `Retrospektive zum letzten Lauf`
- `Run a process retrospective for session <session-id>.`
- `Run a process retrospective for ticket <ticket-id>, phases <range>.`

With no named target, the skill uses the current conversation.
A historical target requires accessible original records, including relevant worker records when available.

## Optional registration

After explicit installation authorization, copy this complete directory to the intended runtime's skill location as `retro/`.
Keep `SKILL.md`, `README.md`, `references/method.md`, `LICENSE`, and `NOTICE.md` together and unchanged.
Before copying, inspect the target's active skill roots and built-in commands for a `retro` collision.
Preserve existing packages; report a conflict instead of renaming or overwriting silently.

For Hermes, use native catalog/main/reference readbacks to verify one intended `retro` identity and the complete loaded content.
Native skill discovery supplies `/retro`; verify availability on the intended communication surface before claiming registration.
The description supports selection after an explicit natural-language request too.
Do not rely on `disable-model-invocation` to enforce this policy in Hermes.
No target installation or discovery is established by these package files.

## Output and authority

Expect a short severity-ordered set of sourced process proposals, including causes, owners, benefits, and trade-offs.
A smooth or poorly evidenced run may support no changes.
User selection and an explicit implementation scope precede any change.
Native `/refine` skill-and-memory maintenance remains a separate user action.

## Verification and provenance

The Maker development check is `python3 -B -m unittest discover -s references -p 'test_retro.py' -v`, run from the Maker root.
It uses an already available `ruamel.yaml` or PyYAML safe parser.
That check covers package structure, metadata, reference reachability, source attribution, and static instruction scenarios with deletion mutations.
It does not run inference, prove model behavior, measure token savings, or verify a live target.
The test is development equipment, not an installed runtime dependency.

See [NOTICE](NOTICE.md) for Matt Pocock's exact upstream revision and the deliberate adaptations.
See [LICENSE](LICENSE) for MIT terms.
