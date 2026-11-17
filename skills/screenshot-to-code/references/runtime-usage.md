# Usage in Hermes and Codex

Both runtimes use the same package. Project rules, roles, and permissions come from the respective deployment context, not from a specific installation or a specific team.

## Capabilities instead of built-in infrastructure

| Need | Hermes | Codex |
| --- | --- | --- |
| Skill and references | `skill_view` loads the installed skill and relative references; alternatively read files, without presenting this as catalogue evidence. | Invoke the skill explicitly with `$screenshot-to-code` or let it be selected by its description; open referenced files with the actually available read tools. |
| Rules and project files | `read_file`, `search_files`; changes only with existing write rights. | Available file/shell tools; preserve applicable sandbox/approval rules. |
| View source/render | `vision_analyze` when offered; establish actual image inspection capability first. | Available image view, for example an offered `view_image`; do not treat it as available merely because of a file path. |
| Browser, capture, offline probe | Available browser tool or approved project CLI. | Available browser binding or approved project CLI. Do not infer browser capability from the runtime name alone. |
| Checks/build/extraction | `terminal` with available approved project tools. | Available execution tool with the same project constraints. |
| Open product decision | Available conversation/clarification path; `clarify` if available. | Available conversation/clarification path. Do not assume Hermes tools. |

Tool names describe available options, not installation requirements. Report a missing tool concretely; introduce no invented tools, hidden installations, or new services. A text reader does not replace image view. Tool schemas of the running session take precedence over examples.

## Loading and roles

Load only needed references: source/assets for extraction or provenance questions, visual comparison for a rebuild, offline export only on an export assignment. Skill copies of the same name can resolve differently; when in doubt, check the actually loaded path and content. An old conversation does not prove the current package identity.

Planners clarify open product questions and plan. Implementers work in approved phases; reviewers check independently. An accepted specification is not reopened for discussion by the runtime change. Report new material gaps in the correct role and stop only dependent work. Neither skill invocation nor tool availability extends rights or commissions commit, publication, or operations.
