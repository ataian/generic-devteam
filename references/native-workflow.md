# Rollenbindungen einrichten und prüfen

Diese Referenz ergänzt den [Setupablauf](setup.md): Sie ordnet bestätigte Werte
ihren Zielen zu und beschreibt die Personalisierung der Rollen. Der laufende
Arbeitsprozess und die Reasoning-Eskalation stehen in den Rollen-SOULs; fachliche
Anleitungen bleiben in den jeweils installierten Skills.

## 1. Copy complete skills and bind the recovery launcher

Die [Quellenübersicht](upstream-sources.md#mitgelieferte-bausteine) nennt die
mitgelieferten Skillbäume und ihre Zielrollen. Je Ziel den vollständigen Baum aus
`skills/` einschließlich Referenzen, Skripten und vorhandenen Lizenz-/Notice-Dateien
kopieren. `SKILL.md` bleibt `SKILL.md`.
Bind only `brownfield-feature-planning/scripts/recover-triage` through the Maker's [recovery binding step](setup.md#bind-the-planner-recovery-invocation).
Keep all other skill bytes unchanged.

- Hermes: `<tatsächlich aufgelöster Rollenhome>/skills/<Skillname>/`.
- Team-Codex: `<CODEX_PROCESS_HOME>/.agents/skills/<Skillname>/` gemäß Rollenmatrix.
- Vorhandene Ziele auf Eigentum und Änderungen prüfen; bei Konflikten anhalten.
- Compare the complete file set and bytes, using the bound Maker output for the recovery launcher.
- Check discovery and loading in the target harness after the comparison.

Keep installed skills usable without the Maker package or setup record.
Deliver the bound callable launcher inside the existing planner skill tree.
Do not add a separate runtime configuration file or workflow skill.

## 2. Rollen-SOULs personalisieren

Die Vorlagen für [Planner](../templates/roles/planner.SOUL.md.template),
[Coder](../templates/roles/coder.SOUL.md.template) und
[Reviewer](../templates/roles/reviewer.SOUL.md.template) werden nur an den
vorgesehenen Platzhaltern verändert. Das [Manifest](../manifest.json) beschreibt
je Rolle die tatsächlich vorkommenden `render_fields`.

| Feld | Bestätigter Wert |
|---|---|
| `ROLE_NAME` | Eigener Anzeigename der jeweiligen Rolle |
| `PLANER_NAME` | Planner-Anzeigename; Schreibweise mit einem N |
| `CODER_NAME` | Coder-Anzeigename |
| `REVIEWER_NAME` | Reviewer-Anzeigename |
| `PROJECT_NAME` | Projektkennung als einzelnes Segment; bestimmt nicht den Workspace |
| `PROJECT_DIR` | Confirmed canonical absolute workspace; Planner only |
| `REPOSITORY_ROOTS` | Confirmed repository boundaries as single-line text with separate planning and implementation assignments; Planner only |
| `PLANNER_PROFILE` | Confirmed technical Planner profile ID; Coder only |
| `HINDSIGHT_BANK_NAME` | Tatsächlich zugeordnete gemeinsame Projektbank |
| `KANBAN_BOARD_NAME` | Native Boardkennung, nicht der Anzeigetitel |
| `CODER_PROFILE` | Technische Coderprofilkennung, soweit in der Vorlage vorhanden |
| `REVIEWER_PROFILE` | Technische Reviewerprofilkennung, soweit in der Vorlage vorhanden |
| `CODEX_REASONING_DEFAULT` / `CODEX_REASONING_MAX` | Bestätigter Team-Codex-Standard und erlaubte Obergrenze; nur Coder-Vorlage |
| `ROLE_REASONING_DEFAULT` / `ROLE_REASONING_HIGH` | Bestätigter Reviewer-Standard und höchste erlaubte Prüfstufe; nur Reviewer-Vorlage |

Anzeigenamen und technische Kennungen getrennt halten. Alle Mehrfachvorkommen
aus demselben bestätigten Datensatz ersetzen. Der eigene Anzeigename liefert
`ROLE_NAME`; weder zusätzliche Persona noch neue Rollenregeln anhängen.

Der reine [Textrenderer](render_text.py) validiert die rollenbezogene Feldmenge
und ersetzt in einem Durchlauf. Fehlende, zusätzliche oder beschädigte Felder
sind Fehler. Werte bleiben unverändert: keine stille Kürzung oder Normalisierung.
Namen sind nichtleerer einzeiliger Klartext; technische Kennungen und Projektname
müssen außerdem die jeweiligen Syntax- und Pfadprüfungen bestehen. Markdown wird
kontextgerecht maskiert; technische Werte in Codekontexten bleiben unverfälscht.
Alle Nichtplatzhalterbytes der bestätigten Vorlage bleiben erhalten.

Use the role personalization accepted during preparation.
Compare the rendered output with that scope before writing only `SOUL.md` in each confirmed role home.
Read back complete bytes against the generated output and check effective full loading through the established native interface.
Do not overwrite foreign or concurrently changed files.
Ask again only for a newly observed conflict or scope change.

## 3. Bind technical values to actual targets

| Value | Target/readback |
|---|---|
| Role identity | Native registration, canonical home, personalized SOUL |
| Workspace/repositories | Confirmed workspace, `terminal.cwd`, board default workspace and Planner repository-boundary fields |
| Board | Native board ID, explicit board selection and dispatcher DB |
| Bank | Effective provider/bank and exact per-role tags/match settings |
| Models/reasoning | Native configuration and effective overrides; existing role default/max fields |
| Team-Codex | Actual binary, separate process/config homes, access and identity under [Integrations](integrations.md#team-codex) |
| Analysis | Planner, Coder, Reviewer and Team-Codex: exactly the confirmed branch, complete assets and native connection/configuration readbacks |
| Communication | Planner-only bot, exact authorized user/channel/DM IDs and genuine Home binding; later task subscriptions remain operational |

Reuse the confirmed workspace as `PROJECT_DIR` in the Planner SOUL.
Reuse the confirmed repository boundaries as `REPOSITORY_ROOTS` in the Planner SOUL.
Keep planning and implementation assignments separate in that value.
Preserve nested checkouts and roots that differ from the workspace.
If no repository exists yet, record that confirmed fact instead of inventing a root.
Bind the workspace natively as `terminal.cwd` and the board default workspace.
Keep the current Git-root, cwd, board, and ticket checks in the Planner workflow.
Render the confirmed technical `PLANNER_PROFILE` directly into the Coder SOUL.
Check that ID against the native profile registration.
Use that bound ID for the existing Planner wake and TIMER routes.
For a missing customer decision, the Coder keeps assignment and blocks the same card with `kind="needs_input"`.
The existing subscription wakes the Planner for Mattermost coordination.
After recording the sufficient answer, the Planner uses ordinary unblock or guarded triage recovery.
Keep `kanban_request_review` bound to the independent Reviewer, not customer clarification.
Do not derive paths from display names. Derive only new profile IDs under the setup normalization rule; preserve confirmed IDs.
Do not ask the user to repeat confirmed values.
If bindings conflict, resolve the conflict before writing role files.
Keep branch, plan revision, and ticket/run/event IDs specific to the current task.
Do not generate a second runtime binding file.

Keep fixed Planner/Hermes-Coder reasoning in native configuration.
Keep Reviewer/Team-Codex default and maximum in the existing role fields.
Resolve native model IDs, supported levels, and limits during preparation.
For the six VoltAgent specialists, verify unchanged TOMLs and original model/reasoning availability through [their recipe](integrations.md#codex-agents).
Read back actual configuration and overrides; do not probe reasoning boundaries with model calls.
A role maximum is a policy rule, not a technical execution barrier.

Kommunikationszugänge und Kanalbindungen bleiben beim Planner. Geheimnisse gehören
in geschützte native Zugangswege. Der private [Setuprecord](../templates/setup-record.md)
dokumentiert Werte, Ziele und Nachweise; er ist keine zusätzliche Laufzeitkonfiguration.

## 4. Setup readbacks and resume

Compare profiles, board/workspace, bank, actual homes, effective model configuration, complete skill trees,
full SOUL loading, recovery output and modes with confirmed values.
Use established discovery/configuration readbacks, not synthetic handoff, wake, or worker experiments.
Reuse preparation acceptance for role personalization; compare exact rendered output with that scope before writing.
A concrete mismatch needs resolution before the affected write or activation.
On resume, read the single setup JSON and actual targets; continue only the incomplete step.
Correct stale descriptive prose without repeating confirmed decisions or creates.

Diese Schritte gehören zum später ausdrücklich beauftragten Zielsetup. Beim
Bearbeiten dieses Pakets werden keine Profile, Dienste oder Agenten aktiviert.
