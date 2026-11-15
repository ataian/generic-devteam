# Diagnosing bugs

Owned, portable adaptation of Matt Pocock's diagnosis method for Team-Codex.
[SKILL.md](SKILL.md) classifies concrete evidence before selecting direct fix or [full diagnosis](references/method.md).
Small evidenced bugs keep their direct path; uncertainty triggers deeper investigation without another planning ceremony.

## Delivery and use

Copy this complete tree, including [NOTICE](NOTICE.md), [LICENSE](LICENSE), and `references/`, to the intended Codex user's `.agents/skills/diagnosing-bugs/`.
Resolve native skill-name collisions and local edits before replacing an existing tree.
Maker assigns the method only to Team-Codex and uses its existing whole-tree setup/update mapping.

In Codex CLI, include the literal `$diagnosing-bugs` in the task prompt with the goal, accepted context, exact symptom, expected behavior, and verification criteria.
Preserve the team's other task cues, process bindings, risk checks, and independent review.
The description also makes the skill available for unexplained failures or regressions arising during ordinary implementation.

Verify complete saved bytes, unambiguous native discovery, and explicit call policy separately.
These readbacks do not prove actual diagnosis behavior.
No framework installation, shell helper, or human-run terminal loop is required by this package.
