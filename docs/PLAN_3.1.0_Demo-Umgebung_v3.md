# PLAN 3.1.0 — Demo und Dev-Umgebung optional halten

**Dokumentversion:** v3 (Änderung gegenüber v2: keine Bindung mehr an `demo.sh` oder ein benanntes Dev-Skript — die Rollen nutzen die Umgebung des Projekts, die Kommandos liefert künftig ein eigener Demo-/Dev-Skill).
**Status:** Vorschlag. Keine Datei des Pakets geändert, nichts committet. Umsetzung erst nach Freigabe.

**Entscheidungen des Betreibers (2026-11-25):**
1. Das Verbot, Container, Volumes, Netze oder Verzeichnisse selbst per Compose zu entfernen, entfällt. Existiert ein `demo.sh`, kennt der Planner es und nutzt es; nutzt er Compose, ist das Ergebnis dasselbe.
2. Eine Demo-Handover-Karte entsteht nur, wenn der Kunde sie will. Gefragt wird im Planannahme-Gespräch; ohne Ja gibt es keine Karte.
3. Alle Docker-Befehle sind mit diesem Plan erlaubt: `docker *` in jeder Rolle, ohne Aufzählung einzelner Verben.
4. Keine Bindung mehr an `demo.sh` oder ein benanntes Dev-Skript. Das Team entscheidet, welches Werkzeug es für seine Demo- und Dev-Umgebung nutzt; die konkreten Kommandos liefert später ein eigener Skill. Die Rollentexte halten nur noch Autorität, Grenzen und Prüfpflichten, keine Werkzeugnamen.

## Ausgangslage

Gemessen am Stand 3.1.0 (`8add46c0`), Trefferzahlen mit `read_text().count(...)` am 2026-11-25:

| Datei:Zeile | heutiger Text (Anfang) | Wirkung |
|---|---|---|
| `templates/roles/planner.SOUL.md.template:74` | „Before card release: retire a running demonstration runtime. Use the project's documented teardown verb (`demo.sh retire` or equivalent); never compose container, volume, network or directory removal yourself …" | unbedingte Pflicht in Schritt 7; nennt ein Verb, das es nicht überall gibt, und verbietet den Rückfall |
| `templates/roles/planner.SOUL.md.template:75` | „When the project has a demonstration runtime, add a final `Demo handover` card …" | Bedingung ist der Besitz einer Demo-Runtime, nicht der Kundenwunsch; „add" ist eine Anordnung |
| `skills/demo-handover/SKILL.md:19` | „Use the project's documented teardown verb (`demo.sh retire` or equivalent); never compose … — an unattended guard refuses it." | Werkzeugbindung und Verbot im Skill |
| `skills/demo-handover/SKILL.md:21` | „Create the demonstration user via `demo.sh user` …" | bindet die Benutzeranlage an ein Skript, das nur manche Projekte haben |
| `skills/dev-environment/SKILL.md:39` | „give the guide one script with one verb per operation (`docker/dev/dev.sh up`, `check`, `stop`, `test`, `reset`)" | schreibt ein bestimmtes Dev-Skript vor |
| `skills/dev-environment/SKILL.md:47` | „Retire it through the project's teardown verb and verify they are gone …" | unbedingtes Verb im Abschnitt „Demonstration lifecycle" |
| `skills/dev-environment/SKILL.md:48` | „Do not compose container, volume, network or directory removal yourself; an unattended guard refuses it." | dasselbe Verbot |
| `references/setup.md:136` | „Never grant `docker compose *`, `docker *`, `docker-compose *` or an `env *` wrapper …" | verbietet genau die Freigabe, die Punkt 3 verlangt |
| `references/setup.md:141` | Grant-Block mit sechs lesenden Docker-Einträgen | Docker nur lesend freigegeben |
| `references/update.md:93` | „Propose replacing legacy broad patterns, including `docker compose *`, with those entries." | erklärt ein weites Docker-Muster zum Altlast-Befund |

Belege für die Laufzeit: `docker compose down` fällt unter den Container-Lebenszyklus (`tools/approval_detection.py:603`) und liefert `ask-approval`. Die permanente Allowlist wird **vor** dieser Prüfung ausgewertet (`tools/approval.py:1228`, `tools/approval_floors.py:184-205`: exakter Text oder fnmatch-Glob, zusammengesetzte Zeilen nie). Gemessen in einem isolierten `HERMES_HOME` mit `["docker *"]`:

| Kommando | Verdikt |
|---|---|
| `docker ps` | `allow` |
| `docker compose -f docker/docker-compose.yml down -v` | `allow` |
| `docker rm -f soos-control-1` | `allow` |
| `docker system prune -af` | `allow` |
| `docker run --privileged -v /:/host alpine` | `allow` |
| `docker ps && rm -rf /tmp/x` | `ask-approval` |

Und in soos fehlt jeder Teardown-Weg: `grep -rln 'demo.sh' /home/mariko/projects/soos/` ergibt 0 Treffer.

## Schritte

### Schritt 1 — `templates/roles/planner.SOUL.md.template:74`

**ALT** (eine Zeile, `count == 1`):

```text
   Before card release: retire a running demonstration runtime. Use the project's documented teardown verb (`demo.sh retire` or equivalent); never compose container, volume, network or directory removal yourself — an unattended guard refuses it. Verify its containers, volumes, network and private runtime directory are gone, and record the readback on the card; a stopped runtime is not a retired one. Create the branch from the confirmed start commit and check it out in the assigned checkout. Record branch name and start commit on the card, then read back the card fields and the branch's git status.
```

**NEU:**

```text
   Before card release: when a demonstration runtime is running, retire it with the project's own environment commands and verify its containers, volumes, network and private runtime directory are gone; a stopped runtime is not a retired one. Record the readback on the card. When the project has no demonstration runtime, record that fact on the card and continue. Create the branch from the confirmed start commit and check it out in the assigned checkout. Record branch name and start commit on the card, then read back the card fields and the branch's git status.
```

Erhalten bleibt: Zeitpunkt (vor Kartenfreigabe), Prüfpflicht gegen Container, Volumes, Netz und privates Laufzeitverzeichnis, die Unterscheidung „gestoppt ist nicht abgeräumt", die Readback-Pflicht, der Rest der Zeile (Branch und Startcommit).

### Schritt 2 — `templates/roles/planner.SOUL.md.template:75`

**ALT** (`count == 1`):

```text
   When the project has a demonstration runtime, add a final `Demo handover` card assigned to {{CODER_PROFILE}}, blocked on the last implementation ticket: demonstration runtime at the reviewed commit, data that exercises the changed criteria, the demonstration user and its login name, the exact implementation commit, the URL and the exact data-creation command. The password is `{{DEMO_PASSWORD}}`; never write it on a card.
```

**NEU:**

```text
   When the customer asked for a demonstration at plan acceptance, add a final `Demo handover` card assigned to {{CODER_PROFILE}}, blocked on the last implementation ticket: demonstration runtime at the reviewed commit, data that exercises the changed criteria, the demonstration user and its login name, the exact implementation commit, the URL and the exact data-creation command. Without that request no demo card exists; the accepted plan states that no demonstration was requested. The password is `{{DEMO_PASSWORD}}`; never write it on a card.
```

### Schritt 3 — `templates/roles/planner.SOUL.md.template:64` (Angebot im Annahmegespräch)

**ALT** (`count == 1`):

```text
5. Request explicit customer acceptance of the plan. Do not create implementation tickets before acceptance.
```

**NEU:**

```text
5. Request explicit customer acceptance of the plan. In the same conversation, offer a demonstration handover and record the answer in the plan. Do not create implementation tickets before acceptance.
```

### Schritt 4 — `skills/demo-handover/SKILL.md:19` und `:21`

**ALT Zeile 19** (`count == 1`):

```text
- Use the project's documented teardown verb (`demo.sh retire` or equivalent); never compose container, volume, network or directory removal yourself — an unattended guard refuses it.
```

**NEU Zeile 19:**

```text
- Retire the previous runtime with the project's own environment commands.
```

**ALT Zeile 21** (`count == 1`):

```text
- Create the demonstration user via `demo.sh user`, with the password supplied only through the environment variable the script documents.
```

**NEU Zeile 21:**

```text
- Create the demonstration user with the project's documented user-creation command, with the password supplied only through the environment variable that command documents.
```

Damit verlassen beide `demo.sh`-Literale den Skill; die pinnen-den Assertions `references/test_update_team.py:498-499` und `references/test_render_reasoning.py:160` gehen mit (siehe Testanpassungen).

### Schritt 5 — `skills/dev-environment/SKILL.md:47-48`

**ALT** (zwei Zeilen, je `count == 1`):

```text
- Before replacing it, verify exclusive ownership of the previous demo's containers, volumes, network and private runtime directory. Retire it through the project's teardown verb and verify they are gone; a stopped runtime is not a retired one. Preserve review evidence and unrelated resources.
- Do not compose container, volume, network or directory removal yourself; an unattended guard refuses it.
```

**NEU** (eine Zeile, die zweite entfällt):

```text
- Before replacing it, verify exclusive ownership of the previous demo's containers, volumes, network and private runtime directory. Retire it with the project's own environment commands and verify they are gone; a stopped runtime is not a retired one. Preserve review evidence and unrelated resources.
```

### Schritt 6 — `skills/dev-environment/SKILL.md:39` (kein festes Dev-Skript)

**ALT** (`count == 1`):

```text
- Entrypoint: give the guide one script with one verb per operation (`docker/dev/dev.sh up`, `check`, `stop`, `test`, `reset`). `check` runs the selected component's static checks without the test suites. A compound command line, or `$` expansion inside double quotes, never matches an agent grant.
```

**NEU:**

```text
- Entrypoint: give the guide one verb per operation with the exact invocation the project uses. `check` runs the selected component's static checks without the test suites. A compound command line, or `$` expansion inside double quotes, never matches an agent grant.
```

Der Werkzeugname fällt; die Anforderung (ein Verb je Vorgang, grant-fähige einfache Kommandozeile) bleibt. Die spätere Auslagerung des Demo-/Dev-Verfahrens in einen eigenen Skill ersetzt diesen Abschnitt, nicht dieser Plan.

### Schritt 7 — `references/setup.md:136`, `:141`, `:145` (Docker vollständig freigeben)

**ALT Zeile 136** (`count == 1`):

```text
Grant the project's development and demonstration entrypoints in all three profiles, so a standard operation does not become an approval question. Take the exact absolute script paths and one verb per entry from the project agent guide; grant each reviewed command as written, with a `*` only for a script-validated argument such as a commit SHA or test selector. The runtime matches a grant only against a simple command line: a compound line (`;`, `&&`, `|`, a heredoc) or `$` expansion inside double quotes never matches, and a leading variable assignment changes the command text away from the bare entry. Never grant `docker compose *`, `docker *`, `docker-compose *` or an `env *` wrapper: the entrypoints own container, volume and network lifecycle, and a broad Docker pattern also grants removal outside the accepted scope. Keep read-only `docker ps`, `docker ps -a`, `docker logs *`, `docker inspect *`, `docker volume ls` and `docker network ls` for diagnosis and for verifying that a retired demo left no container, volume or network behind.
```

**NEU Zeile 136:**

```text
Grant the project's development and demonstration entrypoints in all three profiles, so a standard operation does not become an approval question. Take the exact absolute script paths and one verb per entry from the project agent guide; grant each reviewed command as written, with a `*` only for a script-validated argument such as a commit SHA or test selector. The runtime matches a grant only against a simple command line: a compound line (`;`, `&&`, `|`, a heredoc) or `$` expansion inside double quotes never matches, and a leading variable assignment changes the command text away from the bare entry. Grant `docker *` in every role: it covers diagnosis, container lifecycle, teardown and cleanup whether or not the project ships a script, and it is the only Docker pattern the roles need. Never grant `docker-compose *` or an `env *` wrapper. The grant reaches every container, volume and network of the host, so record that reach in the setup record.
```

**ALT Zeile 141** (`count == 1`, Grant-Block):

```text
hermes -p "$PROFILE" config set command_allowlist "[\"$DEV_ENTRYPOINT check\",\"$DEV_ENTRYPOINT test\",\"$DEV_ENTRYPOINT test-selected *\",\"$DEV_ENTRYPOINT test-all\",\"$DEMO_ENTRYPOINT build *\",\"$DEMO_ENTRYPOINT start *\",\"$DEMO_ENTRYPOINT status\",\"$DEMO_ENTRYPOINT stop\",\"$DEMO_ENTRYPOINT retire\",\"$DEMO_ENTRYPOINT retire *\",\"$DEMO_ENTRYPOINT user\",\"docker ps\",\"docker ps -a\",\"docker logs *\",\"docker inspect *\",\"docker volume ls\",\"docker network ls\"]"
```

**NEU Zeile 141:**

```text
hermes -p "$PROFILE" config set command_allowlist "[\"$DEV_ENTRYPOINT check\",\"$DEV_ENTRYPOINT test\",\"$DEV_ENTRYPOINT test-selected *\",\"$DEV_ENTRYPOINT test-all\",\"$DEMO_ENTRYPOINT build *\",\"$DEMO_ENTRYPOINT start *\",\"$DEMO_ENTRYPOINT status\",\"$DEMO_ENTRYPOINT stop\",\"$DEMO_ENTRYPOINT retire\",\"$DEMO_ENTRYPOINT retire *\",\"$DEMO_ENTRYPOINT user\",\"docker *\"]"
```

**ALT Zeile 145** (`count == 1`):

```text
Omit entries whose entrypoint or verb the project does not have. When the Planner must construct the environment before its guide exists, add only the exact `docker compose -f <absolute dev compose path> build`, `up -d`, `down`, `ps` and `logs` entries; never `-v` and never a wildcard. The `demo.sh user` entry stays the bare script invocation: supply the password only through the environment variable the project documents, never as an argument and never in a grant.
```

**NEU Zeile 145:**

```text
Omit entries whose entrypoint or verb the project does not have. `docker *` covers constructing, starting, stopping and tearing down a development Compose stack, including volume arguments and wildcard paths, so no separate Compose entry is needed; keep the script entrypoints for the operations those scripts own. A demonstration user-creation entry stays the bare script invocation: supply the password only through the environment variable the project documents, never as an argument and never in a grant.
```

### Schritt 8 — `references/update.md:93` (Altlast-Zeile)

**ALT** (`count == 1`, Zelleninhalt der Zeile `Pre-2.14.0`):

```text
Use the [setup grant recipe](setup.md#project-command-grants) with the bound project's agent guide and verified absolute entrypoints to reconstruct the scoped list per role. Propose replacing legacy broad patterns, including `docker compose *`, with those entries.
```

**NEU:**

```text
Use the [setup grant recipe](setup.md#project-command-grants) with the bound project's agent guide and verified absolute entrypoints to reconstruct the scoped list per role. `docker *` is the granted baseline for container work, so a legacy broad Docker pattern needs no replacement; replace only patterns that reach beyond Docker.
```

### Schritt 9 — geprüft, keine Änderung

- `templates/roles/reviewer.SOUL.md.template:86` und `templates/roles/coder.SOUL.md.template:54` greifen erst, wenn eine Demo-Karte existiert; sie ordnen keine an. Bleiben.
- `templates/roles/planner.SOUL.md.template:98` („For a completed demo handover …") ist ebenfalls kartenbedingt. Bleibt.
- `skills/brownfield-feature-planning/references/kanban-phase-release.md:21` gilt nur, wenn die geplante Änderung den Teardown-Befehl selbst repariert. Diese Bedingung trägt bereits. Bleibt.
- Die Zeile `- When the project has an assigned development environment or a demonstration runtime, it is yours to operate.` in allen drei SOULs ist bedingt formuliert und deckt den Fall „gibt es nicht" schon ab. Bleibt.

## Testanpassungen

Diese Assertions pinnen die geänderten Sätze und müssen im selben Changeset mitgehen:

| Datei:Zeile | heute | danach |
|---|---|---|
| `references/test_render_reasoning.py:117` | `assertIn("When the project has a demonstration runtime, add a final \`Demo handover\` card", tickets)` | auf den Kundewunsch-Satz umhängen |
| `references/test_render_reasoning.py:155` | `assertIn("retire a running demonstration runtime.", rendered["planner"])` | auf „when a demonstration runtime is running, retire it" umhängen |
| `references/test_render_reasoning.py:156-159` | `teardown`-String in Planner und Skill | durch den neuen Teardown-Satz ersetzen, beide Fundstellen |
| `references/test_render_reasoning.py:160` | `assertIn("Create the demonstration user via \`demo.sh user\`…")` | auf den neuen Befehlssatz umhängen; das `demo.sh`-Literal entfällt |
| `references/test_render_reasoning.py:161` | `assertNotIn("demo.sh retire", rendered["coder"])` | bleibt; zusätzlich `assertNotIn("demo.sh", …)` für Planner und den Handover-Skill |
| `references/test_build_evidence.py:92` | `assertIn("Never grant \`docker compose *\`, \`docker *\`, …")` | auf den neuen Freigabesatz umhängen (Verbot jetzt nur `docker-compose *` und `env *`) |
| `references/test_build_evidence.py:102` | `assertIn("\`docker compose *\`", legacy)` | auf die neue Altlast-Zeile umhängen |
| `references/test_build_evidence.py:107-108` | `assertNotIn('"docker *"', text)` in der Schleife über setup und update | aufteilen: `assertIn` für `setup.md`, `assertNotIn` bleibt für `update.md`; `env *`-Verbot bleibt |
| `references/test_build_evidence.py:141` | Teardown-Satz des Dev-Skills | neuen Satz einsetzen |
| `references/test_build_evidence.py:142` | `assertIn("Do not compose container, volume, network or directory removal yourself")` | zu `assertNotIn` auf das gestrichene Verbot invertieren |
| `references/test_build_evidence.py:149-155` | liest den Grant-Block und prüft die lesenden Docker-Einträge im Tail | auf `\"docker *\"` im Grant-Block umstellen, Testname mitziehen |

| `references/test_update_team.py:498-499` | `assertIn('\`demo.sh retire\`' / '\`demo.sh user\`', handover)` | zu `assertNotIn` invertieren, weil beide Literale den Skill verlassen |
| `references/test_update_team.py:500` | `assertNotIn('demo.sh retire', coder)` | bleibt unverändert gültig |

## Verifikation

1. Neue Assertions gegen den Basisstand rot zeigen (`git stash`, geänderte Strings im Scratch zählen), dann grün.
2. `python3 -B -m unittest references.test_render_reasoning` und `references.test_build_evidence` einzeln.
3. Gesamtsuite als Hintergrundlauf (`python3 -B -m unittest discover -s references -p 'test_*.py'`), erwartet `OK (skipped=1)`.
4. Renderprobe der drei SOULs mit Beispielbindungen: Platzhaltermenge unverändert, kein `{{` im Ergebnis.
5. Freigabe-Nachweis am echten Profil: `hermes -p <rolle> approvals test --json -- 'docker compose -f <pfad> down -v'` erwartet `allow`, ebenso `docker rm -f <container>`; `docker ps && <anderes Kommando>` weiter `ask-approval`. In einem isolierten `HERMES_HOME` bereits vorgeführt.
6. Bump **3.1.0 → 3.1.1** in `SKILL.md` und `manifest.json` (Textänderungen, kein Renderfeld, kein Helferzustand).

## Wirkung auf bestehende Teams

Beim nächsten Update setzt der Policy-Abgleich `docker *` in jeder Rolle und ersetzt die bisherigen lesenden Einzeleinträge; alles andere bleibt. Für das Team soos heißt das: `command_allowlist` = bisherige Projekt-Einträge plus `docker *`, danach Baseline in `confirmed_bindings.command_allowlists` fortschreiben. Ob das sofort für soos gesetzt wird, ist eine eigene Freigabe und nicht Teil dieses Maker-Plans.

## Nichtziele

- Kein neues Renderfeld, keine Änderung an Coder- oder Reviewer-Template, keine Änderung an `settings`.
- Die Regel „höchstens eine Demo, sie zeigt den letzten unabhängig geprüften Commit" bleibt unverändert.
- Der Maker nennt kein Demo- oder Dev-Werkzeug mehr. Ein Ersatz für `demo.sh` entsteht hier nicht: die Kommandos liefert künftig ein eigener Skill, den dieser Plan nicht baut.
- `docker-compose *` und `env *` bleiben verboten; zusammengesetzte Kommandozeilen bleiben gegated.

## Zurückgezogen gegenüber v2

- **`demo.sh`-Literale im Text** (`` `demo.sh retire` ``, `` `demo.sh user` ``, „documented teardown verb"): verworfen. Das Team wählt sein Werkzeug selbst; Werkzeugnamen gehören nicht in die Rollentexte.
- **`docker/dev/dev.sh`** als vorgeschriebener Dev-Entrypoint: verworfen, gleiche Begründung. Die Anforderung „ein Verb je Vorgang, grant-fähige Zeile" bleibt.

## Zurückgezogen gegenüber v1

- **Zwei eng gefasste Teardown-Einträge** (`docker compose -f * down`, `docker compose -f * down -v`) statt `docker *` — verworfen, weil der Betreiber alle Docker-Befehle freigeben will; die engere Fassung hätte den Planner bei `docker compose down` ohne `-f` und bei direkten Entfernungen weiter blockiert.
- **„Wirkung: keine Änderung an `command_allowlist`"** als Nichtziel — mit Punkt 3 ist die Freigabeliste selbst Teil des Plans.
