# Diagnosing bugs

Owned, portable adaptation of Matt Pocock's diagnosis method for Team-Codex.
[SKILL.md](SKILL.md) uses concrete evidence to select direct fix for clear small bugs or [full diagnosis](references/method.md) when uncertainty warrants deeper investigation. No extra planning round.

## Delivery and use

1. Resolve native name collisions and local edits before replacing an existing tree. Copy the complete tree, including [NOTICE](NOTICE.md), [LICENSE](LICENSE) and `references/`, to the intended Codex user's `.agents/skills/diagnosing-bugs/`. Maker uses its existing whole-tree setup/update mapping for Team-Codex only.
2. In Codex CLI, pass the literal `$diagnosing-bugs`, goal, accepted context, exact symptom, expected behavior and verification criteria in the task prompt. Keep other task cues, process bindings, risk checks and independent review. The description also supports selection for unexplained failures or regressions during ordinary implementation.
3. Verify complete saved bytes, unambiguous native discovery and explicit call policy separately. These readbacks do not establish diagnosis behavior.

No framework installation, shell helper or human-run terminal loop required.
