# PLAN 3.1.0 — Optionale Demo, vollständige Docker-Freigabe

**Dokumentversion:** v4 — gegenüber v3 hängt jede Demo-Aktion vom Kundenwunsch ab; auch `docker-compose` ist freigegeben.
**Stand:** Entwurf zum Review. Basis: Maker 3.1.0, `8add46c0`. Ziel nach separater Umsetzungsfreigabe: 3.1.1. Dieser Plan ändert kein Team.

| Antwort bei der Planannahme | Verhalten des Devteams |
|---|---|
| Ja | Planner räumt eine etwa vorhandene alte Demo ab, auch gestoppte Restbestände. Erst danach legt er die abschließende Demo-Karte an. Ohne Vorgänger direkt zur Karte. Ist sicheres Abräumen nicht möglich, keine vorzeitige Demo-Karte. |
| Nein / kein ausdrückliches Ja | Kein Demo-Auftrag für irgendeine Rolle: keine Existenzprüfung, kein Aufräumen, keine Karte, kein Laufzeitnachweis. Eine vorhandene Demo bleibt unangetastet. Normale Entwicklungsarbeit geht weiter. |

Unabhängig davon dürfen Planner, Coder und Reviewer sämtliche Docker-Unterbefehle verwenden: `docker`, einschließlich `docker compose`, und `docker-compose`. Der spätere Demo-Skill übernimmt das Verfahren; er ist **kein** Liefergegenstand dieser Version.

## 1. Kundenwunsch statt Kartenfreigabe als Auslöser

### `templates/roles/planner.SOUL.md.template:64`

ALT (1 Treffer):
```text
5. Request explicit customer acceptance of the plan. Do not create implementation tickets before acceptance.
```
NEU:
```text
5. At plan acceptance, ask whether the customer wants a new demonstration and record the answer in the plan. Request explicit customer acceptance of the plan. Do not create implementation tickets before acceptance.
```

### `templates/roles/planner.SOUL.md.template:74`

ALT (1 Treffer):
```text
   Before card release: retire a running demonstration runtime. Use the project's documented teardown verb (`demo.sh retire` or equivalent); never compose container, volume, network or directory removal yourself — an unattended guard refuses it. Verify its containers, volumes, network and private runtime directory are gone, and record the readback on the card; a stopped runtime is not a retired one. Create the branch from the confirmed start commit and check it out in the assigned checkout. Record branch name and start commit on the card, then read back the card fields and the branch's git status.
```
NEU:
```text
   Before card release: create the branch from the confirmed start commit and check it out in the assigned checkout. Record branch name and start commit on the card, then read back the card fields and the branch's git status.
```

### `templates/roles/planner.SOUL.md.template:75`

ALT (1 Treffer):
```text
   When the project has a demonstration runtime, add a final `Demo handover` card assigned to {{CODER_PROFILE}}, blocked on the last implementation ticket: demonstration runtime at the reviewed commit, data that exercises the changed criteria, the demonstration user and its login name, the exact implementation commit, the URL and the exact data-creation command. The password is `{{DEMO_PASSWORD}}`; never write it on a card.
```
NEU:
```text
   Only if the customer requested a new demonstration, retire any previous demo, then add a final `Demo handover` card assigned to {{CODER_PROFILE}}, blocked on the last implementation ticket. The password is `{{DEMO_PASSWORD}}`; never write it on a card.
```

### `skills/brownfield-feature-planning/references/kanban-phase-release.md:21`

ALT (1 Treffer):
```text
5. When the planned change repairs the demo teardown command itself, check before plan acceptance whether the existing approved teardown can satisfy the pre-release gate. If not, escalate the circular prerequisite to the operator and keep the release blocked. Do not propose applying and reverting the same product fix simply to get through the gate.
```
NEU:
```text
5. If a new demo was requested and the planned change repairs its teardown command, escalate a circular cleanup prerequisite to the operator before creating the demo card. Do not apply and revert the product fix to unblock cleanup.
```

Die normale Kartenfreigabe bleibt unabhängig von der Demo. Der Planner arbeitet nur im Ja-Zweig an der Demo; kein vorgezogener Check. Der Sonderfall im Freigabe-Skill darf weder das Annahmegespräch vorwegnehmen noch normale Karten bei Nein blockieren. Die bisherigen Übergabeinhalte bleiben im bestehenden Handover-Skill bzw. auf der angeforderten Karte, nicht als zusätzliche Checkliste in der Planner-SOUL.

## 2. Projektkommandos statt Skriptpflicht

### `skills/demo-handover/SKILL.md:18–19`

ALT (1 Treffer):
```text
- A demonstration runtime is not permanent; at most one exists and shows the last independently reviewed commit. Replacing it includes retiring the previous one after verifying exclusive ownership of its containers, volumes, network and private runtime directory, and verifying they are gone; a stopped runtime is not a retired one. Preserve review evidence and unrelated resources.
- Use the project's documented teardown verb (`demo.sh retire` or equivalent); never compose container, volume, network or directory removal yourself — an unattended guard refuses it.
```
NEU:
```text
- At most one demonstration runtime exists; use the last independently reviewed commit. Preserve review evidence and unrelated resources.
```

### `skills/demo-handover/SKILL.md:21`

ALT (1 Treffer):
```text
- Create the demonstration user via `demo.sh user`, with the password supplied only through the environment variable the script documents.
```
NEU:
```text
- Create the demonstration user with the project’s documented command. Supply its password only through the documented environment variable.
```

### `skills/dev-environment/SKILL.md:39`

ALT (1 Treffer):
```text
- Entrypoint: give the guide one script with one verb per operation (`docker/dev/dev.sh up`, `check`, `stop`, `test`, `reset`). `check` runs the selected component's static checks without the test suites. A compound command line, or `$` expansion inside double quotes, never matches an agent grant.
```
NEU:
```text
- Entrypoint: give the guide one verb per operation with the exact invocation the project uses. `check` runs the selected component's static checks without the test suites. A compound command line, or `$` expansion inside double quotes, never matches an agent grant.
```

### `skills/dev-environment/SKILL.md:44`

ALT (1 Treffer):
```text
## Demonstration lifecycle
```
NEU:
```text
## Requested demonstration only
```

### `skills/dev-environment/SKILL.md:47–48`

ALT (1 Treffer):
```text
- Before replacing it, verify exclusive ownership of the previous demo's containers, volumes, network and private runtime directory. Retire it through the project's teardown verb and verify they are gone; a stopped runtime is not a retired one. Preserve review evidence and unrelated resources.
- Do not compose container, volume, network or directory removal yourself; an unattended guard refuses it.
```
NEU:
```text
- Before creating the requested demo card, retire any previous demo with project commands. Verify exclusive ownership before removal and verify its containers, volumes, network and private runtime directory are gone. Preserve review evidence and unrelated resources; stopping is not retirement.
```

### `skills/dev-environment/SKILL.md:59`

ALT (1 Treffer):
```text
- Demo handover: separate closure step with its own card, not an environment acceptance case; it runs the built application through the app compose.
```
NEU:
```text
- A requested demo handover has its own card; it is not a development-environment acceptance case.
```

Beim Ja kann der Planner die vorhandene Dev-Referenz nutzen; kein Verweis auf einen noch nicht gelieferten Skill. Der bestehende `demo-handover` wird erst auf der freigegebenen Karte geladen: Laufzeit starten, Benutzer und Beispieldaten anlegen, URL, Login, exakten Commit und Datenkommando festhalten. Kein zweiter Abräumauftrag für den Coder. Reviewer-Prüfung nur auf dieser Karte; Planner-Schlussbericht nur bei abgeschlossener Übergabe. Allgemeine Betriebsbefugnis in den drei SOULs ist kein Prüfauftrag. Keine neue Skript- oder Compose-Pflicht.

## 3. Alle Docker-Kommandos in jeder Rolle

### `references/setup.md:136`

ALT (1 Treffer):
```text
Grant the project's development and demonstration entrypoints in all three profiles, so a standard operation does not become an approval question. Take the exact absolute script paths and one verb per entry from the project agent guide; grant each reviewed command as written, with a `*` only for a script-validated argument such as a commit SHA or test selector. The runtime matches a grant only against a simple command line: a compound line (`;`, `&&`, `|`, a heredoc) or `$` expansion inside double quotes never matches, and a leading variable assignment changes the command text away from the bare entry. Never grant `docker compose *`, `docker *`, `docker-compose *` or an `env *` wrapper: the entrypoints own container, volume and network lifecycle, and a broad Docker pattern also grants removal outside the accepted scope. Keep read-only `docker ps`, `docker ps -a`, `docker logs *`, `docker inspect *`, `docker volume ls` and `docker network ls` for diagnosis and for verifying that a retired demo left no container, volume or network behind.
```
NEU:
```text
Grant the project's development and demonstration entrypoints in all three profiles, so a standard operation does not become an approval question. Take the exact absolute script paths and one verb per entry from the project agent guide; grant each reviewed command as written, with a `*` only for a script-validated argument such as a commit SHA or test selector. The runtime matches a grant only against a simple command line: a compound line (`;`, `&&`, `|`, a heredoc) or `$` expansion inside double quotes never matches, and a leading variable assignment changes the command text away from the bare entry. Grant `docker *` (including `docker compose *`) and `docker-compose *` in every role. Record their host-wide reach in the setup record. Never grant an `env *` wrapper.
```

### `references/setup.md:141`

ALT (1 Treffer):
```text
hermes -p "$PROFILE" config set command_allowlist "[\"$DEV_ENTRYPOINT check\",\"$DEV_ENTRYPOINT test\",\"$DEV_ENTRYPOINT test-selected *\",\"$DEV_ENTRYPOINT test-all\",\"$DEMO_ENTRYPOINT build *\",\"$DEMO_ENTRYPOINT start *\",\"$DEMO_ENTRYPOINT status\",\"$DEMO_ENTRYPOINT stop\",\"$DEMO_ENTRYPOINT retire\",\"$DEMO_ENTRYPOINT retire *\",\"$DEMO_ENTRYPOINT user\",\"docker ps\",\"docker ps -a\",\"docker logs *\",\"docker inspect *\",\"docker volume ls\",\"docker network ls\"]"
```
NEU:
```text
hermes -p "$PROFILE" config set command_allowlist "[\"$DEV_ENTRYPOINT check\",\"$DEV_ENTRYPOINT test\",\"$DEV_ENTRYPOINT test-selected *\",\"$DEV_ENTRYPOINT test-all\",\"$DEMO_ENTRYPOINT build *\",\"$DEMO_ENTRYPOINT start *\",\"$DEMO_ENTRYPOINT status\",\"$DEMO_ENTRYPOINT stop\",\"$DEMO_ENTRYPOINT retire\",\"$DEMO_ENTRYPOINT retire *\",\"$DEMO_ENTRYPOINT user\",\"docker *\",\"docker-compose *\"]"
```

### `references/setup.md:145`

ALT (1 Treffer):
```text
Omit entries whose entrypoint or verb the project does not have. When the Planner must construct the environment before its guide exists, add only the exact `docker compose -f <absolute dev compose path> build`, `up -d`, `down`, `ps` and `logs` entries; never `-v` and never a wildcard. The `demo.sh user` entry stays the bare script invocation: supply the password only through the environment variable the project documents, never as an argument and never in a grant.
```
NEU:
```text
Omit project entries whose entrypoint or verb the project does not have. Keep both Docker grants regardless of project scripts or demo choice. Supply the demonstration password only through the documented environment variable, never as an argument and never in a grant.
```

### `references/update.md:87`

ALT (1 Treffer):
```text
   - On every update, including a file no-op, compare each role's native `command_allowlist` with its verified list in the private setup JSON (`confirmed_bindings.command_allowlists`). For an absent or obsolete baseline, derive the expected entries as below; never adopt the live list as its own baseline. Report the exact additions, removals and unrelated local grants before approval. Change only approved entries. Save a new baseline only after native readback matches the approved result; otherwise leave reconciliation pending. A role does not extend its own list.
```
NEU:
```text
   - On every update, including a file no-op, compare each role's native `command_allowlist` with its verified list in the private setup JSON (`confirmed_bindings.command_allowlists`). Treat a baseline missing either current Docker grant as obsolete, including a verified 3.1.0 baseline. For an absent or obsolete baseline, derive the expected entries as below; never adopt the live list as its own baseline. Report the exact additions, removals and unrelated local grants before approval. Change only approved entries. Save a new baseline only after native readback matches the approved result; otherwise leave reconciliation pending. A role does not extend its own list.
```

### `references/update.md:93`

ALT (1 Treffer):
```text
   | Pre-`2.14.0` command grants or missing role baseline | Use the [setup grant recipe](setup.md#project-command-grants) with the bound project's agent guide and verified absolute entrypoints to reconstruct the scoped list per role. Propose replacing legacy broad patterns, including `docker compose *`, with those entries. If a path, verb or unrelated grant cannot be confirmed, keep it unresolved for the operator; do not write configuration or mark the migration complete. |
```
NEU:
```text
   | Pre-`2.14.0` command grants or missing/obsolete role baseline | Use the [setup grant recipe](setup.md#project-command-grants) with the bound project's agent guide and verified absolute entrypoints to reconstruct the scoped list per role. Keep verified project entries. Propose replacing redundant Docker entries with `docker *` and `docker-compose *`; do not narrow either grant to specific verbs. If a path, verb or unrelated grant cannot be confirmed, keep it unresolved for the operator; do not write configuration or mark the migration complete. |
```

Dies sind CLI-Freigaben, keine Beschränkung auf den Projekt-Stack. Der bestehende Approval-Pfad für zusammengesetzte Shell-Zeilen und der Ausschluss pauschaler `env *`-Wrapper bleiben unverändert. Der Maker gleicht jede Rolle gegen die neue Vorgabe ab, berichtet die Differenz, ändert nur genehmigte Einträge und schreibt `confirmed_bindings.command_allowlists` erst nach passendem nativen Readback fort. Ein Team aktualisiert seine Liste nicht selbst.

## 4. Abnahme der späteren Implementierung

1. Gegen den Basisstand die neuen Verträge zuerst rot zeigen. Jede ALT-Stelle unmittelbar vor dem Edit erneut auf genau einen Treffer prüfen. CAC: nur die zuständige Stelle ändern. Kein neuer Rendererparameter, kein neues `settings`-Feld.
2. `references/test_render_reasoning.py:109–120,140–168`: Angebot bei Planannahme; Ja vor Cleanup vor Karte; kein Demo-Schritt im allgemeinen Freigabeabsatz; keine Aufräumanweisung bei Nein und keine `demo.sh`-Bindung. Pins für alten Teardown und Planner-Kartendetails ersetzen, Commit/URL/Login/Datenkommando im Handover-Skill prüfen. Lifecycle-Pins für Reviewer und Handover getrennt führen; alle drei Passwortfelder, Passwortschutz, Reviewer-Kartenbezug und Abschlussbericht erhalten. Renderprobe aller Rollen mit Testbindungen: keine offenen `{{`, gleiche Feldmengen.
3. `references/test_update_team.py:491–501`: installierte Skillbytes, unveränderte Coder-Ladebedingung und Passwortbehandlung prüfen; beide positiven `demo.sh`-Pins invertieren. `references/test_build_evidence.py:82–109,137–155`: Grant-Liste tatsächlich dekodieren und beide Muster je Rolle erwarten, statt nur ein Prosa-Literal zu suchen. Bestehende Projekt-Einträge und Readback schützen. Alte Verbots-, Lifecycle- und Diagnose-Tail-Pins ersetzen. Tests für den Ja-Trigger der Sonderregel im Brownfield-Skill mitziehen; bestehende Bytegrenze mit `wc -c` vor/nach Änderung prüfen. Keine Verfahrenspflicht in den allgemeinen SOUL-Absatz verlagern.
4. Gegenszenarien durchspielen: Nein mit laufender Demo und Nein ohne Demo → identischer Ablauf ohne Demo-Zugriff. Ja ohne Vorgänger → Karte. Ja mit laufendem oder gestopptem Vorgänger → entfernen, dann Karte; bei unklarem Eigentum oder Fehler keine Demo-Karte. Allgemeine Branch-, Ticket- und Reviewpflichten bleiben bestehen. Statische Textprüfungen nicht als beobachteten Teamlauf ausgeben.
5. Setup sowie Update einer vollständigen 3.1.0-Baseline in isolierten Testprofilen prüfen, einschließlich bereits korrekter Liste (kein Diff) und erhaltener Nicht-Docker-Einträge. Mit `approvals test --json --` jeweils **nur die Entscheidung** prüfen: `docker ps`, `docker compose down -v`, `docker-compose down -v` → `allow`; `docker ps && <anderes Kommando>` mit konkretem nicht gedecktem Folgebefehl → `ask-approval`. Keine Docker-Operation ausführen, kein Liveprofil umstellen.
6. `SKILL.md` und `manifest.json` gemeinsam 3.1.0 → 3.1.1; dann betroffene Testmodule und `python3 -B -m unittest discover -s references -p 'test_*.py'` ausführen. Ergebnis und Skips berichten. Kein Commit, Push oder Rollout durch Plan oder Review.

## Zurückgezogen gegenüber v3

- Aufräumen und Beleg vor jeder Kartenfreigabe, auch bei fehlender Demo: entfallen. Nicht die Existenz einer Demo, sondern das Ja des Kunden löst die Arbeit aus.
- `docker-compose *` verbieten oder gegen Einzelfreigaben tauschen: entfällt. Beide CLI-Schreibweisen sind gewollt. Hostweite Reichweite ist offenzulegen, nicht auf einzelne Verben zu verengen.
- Unverändert verworfen: Pflicht zu `demo.sh` oder `docker/dev/dev.sh`, eng begrenzte Compose-Teardown-Grants und sofortige Änderungen an `soos`. Kein vorgezogener Bau des neuen Demo-Skills.
