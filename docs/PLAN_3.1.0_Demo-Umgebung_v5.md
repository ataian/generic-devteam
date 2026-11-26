# PLAN 3.1.0 — Optionale Demo, vollständige Docker-Freigabe

**Dokumentversion:** v5 — die gewünschte Demo beginnt beim Planner unmittelbar nach Planannahme, vor Plan-Commit und vor jedem Ticket. Scheitert das Abräumen, wartet der gesamte Plan. Der Reviewer prüft ausschließlich die fertige Demo.
**Stand:** Vorschlag für Fujikos zweites Review; Basis 3.1.0 (`8add46c0`). Kein Implementierungsauftrag. Ziel 3.1.1 (PATCH): Korrektur bestehender Maker-Rollen und Setup-/Update-Rezepte gemäß `AGENTS.md`; kein neues Produkt, Kommando, Renderfeld oder Skill. Umsetzung einschließlich Planner- und Reviewer-Template erst nach ausdrücklicher Freigabe durch Max. Live-Rollout ist separat.

| Entscheidung im Annahmegespräch | Erster Schritt nach ausdrücklicher Planannahme | Weiter |
|---|---|---|
| Kein Demo-Wunsch | Direkt in den normalen Ablauf; für keine Rolle entsteht Demo-Arbeit. | Kein Demo-spezifisches Laden, Sichten, Prüfen, Testen, Aufräumen, Ticket oder Nachweis. Eine vorhandene Demo bleibt unangetastet. |
| Neue Demo gewünscht | Planner lädt die Abräumanleitung. Existiert eine alte Demo, entfernt er sie. | Erst bei feststehender Abwesenheit oder erfolgreichem Abräumen: Plan-Commit, danach Tickets einschließlich abschließender Demo-Karte. |
| Prüfung oder Abräumen nicht erfolgreich | Planner stoppt und klärt das konkrete Problem direkt mit dem User. | Kein Plan-Commit, kein Ticket irgendeiner Art, kein Dispatcherstart. Erst nach Lösung weiter. |

Die Docker-Freigaben für Planner, Coder und Reviewer gelten unabhängig von dieser Entscheidung. Keine Änderung an Coder-Template, Profilen, `settings` oder Compose-Stacks. Kein neuer eigenständiger Demo-Skill in dieser Version.

## 1. Entscheidung und Rollen

### `templates/roles/planner.SOUL.md.template:64`

ALT (1 Treffer):
```text
5. Request explicit customer acceptance of the plan. Do not create implementation tickets before acceptance.
```
NEU:
```text
5. At plan acceptance, ask whether the customer wants a new demonstration. Record their answer and obtain explicit plan acceptance before creating tickets.
   Without an explicit demo request, proceed to step 6 without demo work. If requested, immediately load `skill_view(name="dev-environment", file_path="references/requested-demo.md")` and retire any previous demo before step 6 or any ticket. If absence or successful retirement cannot be established, stop the entire plan and resolve the issue directly with the customer before proceeding.
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
   Only for a requested demonstration, add a final `Demo handover` card assigned to {{CODER_PROFILE}}, blocked on the last implementation ticket. The password is `{{DEMO_PASSWORD}}`; never write it on a card.
```

### `skills/brownfield-feature-planning/references/kanban-phase-release.md:21`

ALT (1 Treffer):
```text
5. When the planned change repairs the demo teardown command itself, check before plan acceptance whether the existing approved teardown can satisfy the pre-release gate. If not, escalate the circular prerequisite to the operator and keep the release blocked. Do not propose applying and reverting the same product fix simply to get through the gate.
```
NEU: ersatzlos streichen.

Der Sonderfall „dieser Plan repariert erst den defekten Teardown“ fällt unter denselben Stopp **vor** Schritt 6. Der Hinweis gegen einen Vorab-Fix wandert zum Verfahren; kein zweiter Test im Releaseablauf.

### `templates/roles/reviewer.SOUL.md.template:86`

ALT (1 Treffer):
```text
- Demo handover card: a demonstration runtime is not permanent; at most one exists and shows the last independently reviewed commit. Replacing it includes retiring the previous one after verifying exclusive ownership of its containers, volumes, network and private runtime directory, and verifying they are gone; a stopped runtime is not a retired one. Preserve review evidence and unrelated resources. Verify the runtime runs at that commit, the recorded login works on the running system with the password `{{DEMO_PASSWORD}}`, and the recorded data shows the changed criteria. A running runtime alone is not evidence. Report each criterion the demo cannot demonstrate.
```
NEU:
```text
- On the final demo handover card, verify the demo runs at the reviewed commit, the recorded login works on the running system with the password `{{DEMO_PASSWORD}}`, and the promised functionality works with the recorded data. Report what the demo cannot demonstrate. Container uptime alone is not a functional check.
```

## 2. Verfahren an der Stelle, die die Rolle tatsächlich lädt

### `skills/dev-environment/SKILL.md:39`

ALT (1 Treffer):
```text
- Entrypoint: give the guide one script with one verb per operation (`docker/dev/dev.sh up`, `check`, `stop`, `test`, `reset`). `check` runs the selected component's static checks without the test suites. A compound command line, or `$` expansion inside double quotes, never matches an agent grant.
```
NEU:
```text
- Entrypoint: give the guide one verb per operation with the exact invocation the project uses. `check` runs the selected component's static checks without the test suites. A compound command line, or `$` expansion inside double quotes, never matches an agent grant.
```

### `skills/dev-environment/SKILL.md:44–50`

ALT (1 Treffer):
```text
## Demonstration lifecycle

- A demonstration runtime is not permanent. At most one acceptance demo exists; it shows the last independently reviewed commit.
- Before replacing it, verify exclusive ownership of the previous demo's containers, volumes, network and private runtime directory. Retire it through the project's teardown verb and verify they are gone; a stopped runtime is not a retired one. Preserve review evidence and unrelated resources.
- Do not compose container, volume, network or directory removal yourself; an unattended guard refuses it.
- If the build or start verb refuses existing runtime state, stop and report the exact refusal. Do not purge, rename or bypass that state.
- Judge readiness from the project's status and version output, not from container uptime. A started container is not a working demo.
```
NEU:
```text
## Optional reference

- [Requested demo](references/requested-demo.md): Planner only, immediately after plan acceptance and only for an explicit demo request. Skip this reference during ordinary development-environment work.
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

### `skills/dev-environment/references/requested-demo.md` — neu, nur im bestehenden Planner-Skill

```text
# Retire the previous demo

Use only as the first step after acceptance of a plan with a requested demonstration. Inspect the project’s demo state, including stopped remnants. Verified absence completes this step; an inspection failure does not.

Before removal, verify exclusive ownership of the old demo’s containers, volumes, network and private runtime directory. Retire it with project commands and verify those resources are gone. Preserve review evidence and unrelated resources. A stopped runtime is not retired.

If inspection, ownership, removal or verification fails, stop before committing the plan or writing any ticket. Tell the customer exactly what failed and resolve it with them. Do not apply and revert a planned product fix to bypass this prerequisite.
```

Das Rücklesen geschieht **vor** den Tickets; es ist kein Protokoll auf einer nicht existierenden Karte. Ein geklärter Fehler ersetzt die Feststellung „entfernt oder nicht vorhanden“ nicht. Der allgemeine Dev-Skill bleibt für echte Dev-Aufträge ladbar; der Demo-Text liegt nicht in seinem Hauptteil.

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

### `skills/demo-handover/SKILL.md:20`

ALT (1 Treffer):
```text
- Start the runtime at the reviewed commit.
```
NEU:
```text
- Start the runtime at the reviewed commit. If build or start refuses existing state, stop and report the refusal; do not purge, rename or bypass it.
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

### `references/upstream-sources.md:28`

ALT (1 Treffer):
```text
- **`dev-environment`.** Requested Docker development-environment creation, adoption and revision, including a project database when needed. Check name collisions and native loading without constructing an environment. The generated repository guide supplies routine commands to all roles. The construction skill stays Planner-only.
```
NEU:
```text
- **`dev-environment`.** Requested Docker development-environment creation, adoption and revision, including a project database when needed. Check name collisions and native loading without constructing an environment. The generated repository guide supplies routine commands to all roles. The construction skill stays Planner-only. Its requested-demo reference is loaded only after plan acceptance for a requested demo.
```

### `references/upstream-sources.md:30`

ALT (1 Treffer):
```text
- **`demo-handover`.** Demo runtime procedure for a released demo handover card: retire the previous runtime, start at the reviewed commit, create the demonstration user, seed data, record the card facts. Coder only, copied unchanged; the password stays in the role instructions. [Delivery recipe](integrations.md#demo-handover).
```
NEU:
```text
- **`demo-handover`.** Demo runtime procedure for a released demo handover card: start at the reviewed commit, create the demonstration user, seed data, record the card facts. Coder only, copied unchanged; the password stays in the role instructions. [Delivery recipe](integrations.md#demo-handover).
```

**Auslieferung:** Bestehende Planner-Zuordnung unverändert. Referenz im Inventar und in der Transporttabelle des vorhandenen Skills ergänzen (kein vierter Verbraucher, kein neuer Skill). Bei Setup/Update werden Dateien verifiziert; das ist kein Aufruf des Demo-Verfahrens im Kundenprojekt.

### `manifest.json:70`

ALT (1 Treffer):
```text
    "skills/dev-environment/SKILL.md",
```
NEU:
```text
    "skills/dev-environment/SKILL.md",
    "skills/dev-environment/references/requested-demo.md",
```

### `manifest.json:256–259`

ALT (1 Treffer):
```text
      "skill_path": "skills/dev-environment/SKILL.md",
      "transport": {
        "SKILL.md": "SKILL.md"
      }
```
NEU:
```text
      "skill_path": "skills/dev-environment/SKILL.md",
      "transport": {
        "SKILL.md": "SKILL.md",
        "references/requested-demo.md": "references/requested-demo.md"
      }
```

## 3. Beide Docker-CLIs vollständig freigeben

### `references/setup.md:136`

ALT (1 Treffer):
```text
Grant the project's development and demonstration entrypoints in all three profiles, so a standard operation does not become an approval question. Take the exact absolute script paths and one verb per entry from the project agent guide; grant each reviewed command as written, with a `*` only for a script-validated argument such as a commit SHA or test selector. The runtime matches a grant only against a simple command line: a compound line (`;`, `&&`, `|`, a heredoc) or `$` expansion inside double quotes never matches, and a leading variable assignment changes the command text away from the bare entry. Never grant `docker compose *`, `docker *`, `docker-compose *` or an `env *` wrapper: the entrypoints own container, volume and network lifecycle, and a broad Docker pattern also grants removal outside the accepted scope. Keep read-only `docker ps`, `docker ps -a`, `docker logs *`, `docker inspect *`, `docker volume ls` and `docker network ls` for diagnosis and for verifying that a retired demo left no container, volume or network behind.
```
NEU:
```text
Grant the project's reviewed development and demonstration scripts in the Planner, Coder and Reviewer profiles. For script entries, use absolute paths from the project guide, one verb per entry, and `*` only for a script-validated argument. Independently grant `docker`, `docker *` (including `docker compose *`), `docker-compose` and `docker-compose *` in all three profiles. A grant matches a simple command line, not a compound line (`;`, `&&`, `|`, a heredoc) or `$` expansion inside double quotes. A leading variable assignment changes the command text. Never grant an `env *` wrapper. Under “Setup targets and readbacks” in the setup record, disclose that these grants cover all operations on any daemon accessible to the CLI, including an alternate context or remote daemon. They are not project-scoped and can affect other workloads; existing deny rules remain binding.
```

### `references/setup.md:141`

ALT (1 Treffer):
```text
hermes -p "$PROFILE" config set command_allowlist "[\"$DEV_ENTRYPOINT check\",\"$DEV_ENTRYPOINT test\",\"$DEV_ENTRYPOINT test-selected *\",\"$DEV_ENTRYPOINT test-all\",\"$DEMO_ENTRYPOINT build *\",\"$DEMO_ENTRYPOINT start *\",\"$DEMO_ENTRYPOINT status\",\"$DEMO_ENTRYPOINT stop\",\"$DEMO_ENTRYPOINT retire\",\"$DEMO_ENTRYPOINT retire *\",\"$DEMO_ENTRYPOINT user\",\"docker ps\",\"docker ps -a\",\"docker logs *\",\"docker inspect *\",\"docker volume ls\",\"docker network ls\"]"
```
NEU:
```text
hermes -p "$PROFILE" config set command_allowlist "[\"$DEV_ENTRYPOINT check\",\"$DEV_ENTRYPOINT test\",\"$DEV_ENTRYPOINT test-selected *\",\"$DEV_ENTRYPOINT test-all\",\"$DEMO_ENTRYPOINT build *\",\"$DEMO_ENTRYPOINT start *\",\"$DEMO_ENTRYPOINT status\",\"$DEMO_ENTRYPOINT stop\",\"$DEMO_ENTRYPOINT retire\",\"$DEMO_ENTRYPOINT retire *\",\"$DEMO_ENTRYPOINT user\",\"docker\",\"docker *\",\"docker-compose\",\"docker-compose *\"]"
```

### `references/setup.md:145`

ALT (1 Treffer):
```text
Omit entries whose entrypoint or verb the project does not have. When the Planner must construct the environment before its guide exists, add only the exact `docker compose -f <absolute dev compose path> build`, `up -d`, `down`, `ps` and `logs` entries; never `-v` and never a wildcard. The `demo.sh user` entry stays the bare script invocation: supply the password only through the environment variable the project documents, never as an argument and never in a grant.
```
NEU:
```text
Omit project entries whose entrypoint or verb the project does not have. Keep the Docker grants regardless of project scripts or demo choice. Supply the demonstration password only through the documented environment variable, never as an argument and never in a grant.
```

### `references/update.md:87`

ALT (1 Treffer):
```text
   - On every update, including a file no-op, compare each role's native `command_allowlist` with its verified list in the private setup JSON (`confirmed_bindings.command_allowlists`). For an absent or obsolete baseline, derive the expected entries as below; never adopt the live list as its own baseline. Report the exact additions, removals and unrelated local grants before approval. Change only approved entries. Save a new baseline only after native readback matches the approved result; otherwise leave reconciliation pending. A role does not extend its own list.
```
NEU:
```text
   - On every update, including a file no-op, compare each role's native `command_allowlist` with its verified list in the private setup JSON (`confirmed_bindings.command_allowlists`). Treat a baseline missing any required Docker entry as obsolete, including a verified 3.1.0 baseline. For an absent or obsolete baseline, derive the expected entries as below; never adopt the live list as its own baseline. Report the exact additions, removals and unrelated local grants before approval. Change only approved entries. Save a new baseline only after native readback matches the approved result; otherwise leave reconciliation pending. A role does not extend its own list.
```

### `references/update.md:93`

ALT (1 Treffer):
```text
   | Pre-`2.14.0` command grants or missing role baseline | Use the [setup grant recipe](setup.md#project-command-grants) with the bound project's agent guide and verified absolute entrypoints to reconstruct the scoped list per role. Propose replacing legacy broad patterns, including `docker compose *`, with those entries. If a path, verb or unrelated grant cannot be confirmed, keep it unresolved for the operator; do not write configuration or mark the migration complete. |
```
NEU:
```text
   | Pre-`2.14.0` command grants or missing/obsolete role baseline | Use the [setup grant recipe](setup.md#project-command-grants) with the bound project's agent guide and verified absolute entrypoints to reconstruct the scoped list per role. Keep verified project entries. Propose replacing redundant Docker entries with the four Docker entries in the setup recipe; do not narrow the wildcard grants to specific verbs. If a path, verb or unrelated grant cannot be confirmed, keep it unresolved for the operator; do not write configuration or mark the migration complete. |
```

Skriptpfade bleiben projektspezifisch; die Einzelaufrufe ohne Argument sind exakt, die beiden Wildcards decken Unterbefehle ab. Keine zusätzliche `docker compose *`-Zeile nötig. Keine zusätzliche Genehmigung pro Docker-Verb. Setup-Readback (`references/setup.md:142,147`), Berichtsabschnitt (`templates/setup-record.md:36–38`) und genehmigter Update-Abgleich (`references/update.md:87,93`) bleiben die bestehenden Mechanismen. Kein Live-Test an `soos`.

## 4. Umsetzung und Abnahme nach Freigabe

1. Neue Vertragsprüfungen am Basisstand zunächst rot, dann nach den obigen Edits grün. Alle ALT-Blöcke vor Änderung auf einen Treffer prüfen. Beim Entfernen der Brownfield-Klausel die kombinierte Größe von Hauptskill und `kanban-phase-release.md` vor/nach mit `wc -c` vergleichen. Keine neue Demo-Regel an ihre Stelle setzen.
2. `references/test_render_reasoning.py:109–120,140–168`: die explizite Demo-Referenz **zwischen** Annahme und Schritt 6 prüfen (unabhängiger bestehender Dev-Aufruf vor Schritt 3 bleibt). Danach Schritt 7: bedingte Demo-Karte mit Coder und letztem Implementationsticket als Abhängigkeit, kein Cleanup dort. Alte Lifecycle-/Teardown-Pins ersetzen: Planner lädt und stoppt, Coder startet erst auf freigegebener Karte, Reviewer prüft nur die funktionierende Demo am Ende. Passwortliteral je Rolle genau einmal, kein Passwort auf Karten, vollständige Platzhalterauflösung und Abschlussbericht erhalten. Login, URL, Commit und Datenkommando im Coder-Skill prüfen. `references/test_update_team.py:487–503`: Reviewer-Lifecycle-Pin durch funktionale Endprüfung ersetzen; beide `demo.sh`-Pins invertieren. Coder-Größenvertrag und sein SOUL-Text bleiben unverändert.
3. `references/test_dev_environment.py:25–45` und `references/test_update_team.py:770–788,790–827`: Inventar, Transport, rekursiver Dateivergleich und lokale Links für Hauptdatei **und** Referenz; keine Kopie in Coder, Reviewer oder Team-Codex. Die Additions-/Rollback-Fixture muss beide Dateien sichern, wiederherstellen und im Resultat berücksichtigen. Separat 3.1.0 → Zielstand: bereits installierter Hauptskill, neue Referenz fehlt; beide nach genehmigtem Update nativ im Planner-Profil lesbar. Kollision mit nicht verwalteter Referenz bleibt Konflikt. Setup prüft einmal die tatsächliche Auflösbarkeit des im Planner-Text verwendeten `skill_view`-Aufrufs; ohne funktionierende Auslieferung kein Fertigbefund.
4. `references/test_build_evidence.py:82–109,137–155`: JSON der Grant-Beispielzeile dekodieren, beide CLI-Namen und beide Wildcards prüfen; keine Aufteilung nach Verben. Alte Verbots-, Teardown- und Listing-Tail-Assertions ersetzen, keine `split("docker inspect *")`-Annahme. Sonderskript-Einträge, Nicht-Docker-Grants, ungeklärte Abweichungen, natives Readback und Wrapper-Grenzen bleiben bestehen. Abräumkriterien an der neuen Referenz, Startverweigerung im Coder-Skill prüfen; kein neuer Nachweis im Nein-Zweig.
5. Szenarien am gerenderten Verfahren: (a) Nein mit oder ohne laufende Alt-Demo: derselbe normale Ablauf, **null Demo-Aktionen**. (b) Ja + verifizierte Abwesenheit: weiter. (c) Ja + laufende/gestoppte Alt-Demo: nur Planner entfernt und verifiziert vor Commit und allen Tickets. (d) Status unbekannt, unklare Zugehörigkeit, Entfernung oder Nachprüfung fehlgeschlagen: null Tickets, kein Commit/Start; Planner benennt konkretes Hindernis direkt dem User; kein Reviewer-Handoff. Auch bei einem Plan zur Reparatur des Abräumbefehls kein Vorab-Fix. (e) Fertige Demo: loginfähig und zugesagte Funktion tatsächlich benutzbar; bloße Containerlaufzeit genügt nicht. Textvertrag und echtes Laufverhalten getrennt berichten.
6. Isolierte Profil-Fixtures: frisches Setup aller drei Rollen, Migration der bisherigen 3.1.0-Diagnoseeinträge und wiederholter Abgleich einer bereits aktuellen Baseline (kein Diff). Für jede Rolle mit `hermes -p <rolle> approvals test --json -- '<Kommando>'` nur die Entscheidung testen: `docker`, `docker-compose`, `docker ps`, `docker volume ls`, `docker network ls`, `docker inspect example`, `docker compose down -v`, `docker-compose down -v` → `allow`. Eine zusammengesetzte Zeile mit nicht freigegebenem Folgebefehl bleibt gegated. Keine Docker-Operation ausführen. Kein Zugriff auf Live-Teamprofile.
7. Paketversion in `SKILL.md` und `manifest.json` gemeinsam auf 3.1.1 setzen. Geänderte Testmodule gezielt, dann `python3 -B -m unittest discover -s references -p 'test_*.py'` und Paketprüfung nach `references/development-verification.md`. Ergebnis und Skips berichten. Kein Commit, Push oder Team-Rollout mit diesem Auftrag.

## Zurückgezogen gegenüber v4

- Nur die Demo-Karte bei Abräumfehler zurückhalten: ersetzt durch Stopp des gesamten Plans unmittelbar nach Annahme, **vor jedem Ticket**. Ansprechpartner ist der User, nicht der Reviewer oder ein Board.
- Den Skill lediglich als mögliche Quelle nennen oder die Anleitung erneut in die SOUL schreiben: ersetzt durch gezieltes Laden der Planner-Referenz im Ja-Zweig. Endprüfung statt zweiter Abräumzuständigkeit beim Reviewer.
- Allgemeine Wildcard-Beschränkung auch für Docker: gilt ausschließlich für zusätzliche projektspezifische Skriptmuster. Beide Docker-CLIs sind einschließlich parameterlosem Aufruf freigegeben.

## Bezug zu Review 1 (vom Autor zugeordnet, kein Reviewurteil)

K1/W2/M1/M3: §3; K2/W1 und Rücklesen vor Karten: §1–2, §4.2/5; W3: Kopf und §4.7; W4/W5: Reviewer-SOUL, Coder-Skill, Herkunftsreferenz; M2 und Listing-Nachweis: §4.4/6; M4: Plan auf Deutsch für Max, operative Maker-Texte auf Englisch; M5: kein festes Dev-Skript gemäß früherer Entscheidung, ein Verb je Vorgang bleibt. Startverweigerung: §2 Coder-Skill. Keine echte Demo und kein Profilbetrieb im Planreview.
