# PLAN 3.1.0 — Demo und Dev-Umgebung optional halten

**Dokumentversion:** v1 (Erstfassung).
**Status:** Vorschlag. Keine Datei des Pakets geändert, nichts committet. Umsetzung erst nach Freigabe.

**Entscheidungen des Betreibers (2026-11-25):**
1. Das Verbot, Container, Volumes, Netze oder Verzeichnisse selbst per Compose zu entfernen, entfällt. Existiert ein `demo.sh`, kennt der Planner es und nutzt es; nutzt er Compose, ist das Ergebnis dasselbe. Die Rolle behält die Freiheit.
2. Eine Demo-Handover-Karte entsteht nur, wenn der Kunde sie will. Gefragt wird im Planannahme-Gespräch; ohne Ja gibt es keine Karte und keine Pflicht.

## Ausgangslage

Gemessen am Stand 3.1.0 (`8add46c0`), Trefferzahlen mit `read_text().count(...)` am 2026-11-25:

| Datei:Zeile | heutiger Text (Anfang) | Wirkung |
|---|---|---|
| `templates/roles/planner.SOUL.md.template:74` | „Before card release: retire a running demonstration runtime. Use the project's documented teardown verb (`demo.sh retire` or equivalent); never compose container, volume, network or directory removal yourself …" | unbedingte Pflicht in Schritt 7; nennt ein Verb, das es nicht überall gibt, und verbietet den Rückfall |
| `templates/roles/planner.SOUL.md.template:75` | „When the project has a demonstration runtime, add a final `Demo handover` card …" | Bedingung ist der Besitz einer Demo-Runtime, nicht der Kundenwunsch; „add" ist eine Anordnung |
| `skills/demo-handover/SKILL.md:19` | „Use the project's documented teardown verb (`demo.sh retire` or equivalent); never compose … — an unattended guard refuses it." | dasselbe Verbot im Skill |
| `skills/demo-handover/SKILL.md:21` | „Create the demonstration user via `demo.sh user` …" | bindet die Benutzeranlage an ein Skript, das nur manche Projekte haben |
| `skills/dev-environment/SKILL.md:47` | „Retire it through the project's teardown verb and verify they are gone …" | unbedingtes Verb im Abschnitt „Demonstration lifecycle" |
| `skills/dev-environment/SKILL.md:48` | „Do not compose container, volume, network or directory removal yourself; an unattended guard refuses it." | dasselbe Verbot |

Beleg für die praktische Wirkung: `/home/mariko/projects/soos` hat kein `demo.sh` (0 Treffer im Baum), nur `docker/docker-compose.yml` und `scripts/seed_demo.py`. Der Planner hätte dort eine Teardown-Pflicht ohne Werkzeug und ohne erlaubten Ausweg.

## Schritte

### Schritt 1 — `templates/roles/planner.SOUL.md.template:74`

**ALT** (eine Zeile, `count == 1`):

```text
   Before card release: retire a running demonstration runtime. Use the project's documented teardown verb (`demo.sh retire` or equivalent); never compose container, volume, network or directory removal yourself — an unattended guard refuses it. Verify its containers, volumes, network and private runtime directory are gone, and record the readback on the card; a stopped runtime is not a retired one. Create the branch from the confirmed start commit and check it out in the assigned checkout. Record branch name and start commit on the card, then read back the card fields and the branch's git status.
```

**NEU:**

```text
   Before card release: when a demonstration runtime is running, retire it — with the project's documented teardown verb if the project has one, otherwise with the project's own container, volume and network removal commands — and verify its containers, volumes, network and private runtime directory are gone; a stopped runtime is not a retired one. Record the readback on the card. When the project has no demonstration runtime, record that fact on the card and continue. Create the branch from the confirmed start commit and check it out in the assigned checkout. Record branch name and start commit on the card, then read back the card fields and the branch's git status.
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
- Retire the previous runtime with the project's documented teardown verb when the project has one (`demo.sh retire` or equivalent), otherwise with the project's own container, volume and network removal commands.
```

**ALT Zeile 21** (`count == 1`):

```text
- Create the demonstration user via `demo.sh user`, with the password supplied only through the environment variable the script documents.
```

**NEU Zeile 21:**

```text
- Create the demonstration user with the project's documented user-creation command (`demo.sh user` or equivalent), with the password supplied only through the environment variable that command documents.
```

Beide Verbliterale `` `demo.sh retire` `` und `` `demo.sh user` `` bleiben im Text; die Verträge in `references/test_update_team.py:498-499` bleiben damit erfüllt.

### Schritt 5 — `skills/dev-environment/SKILL.md:47-48`

**ALT** (zwei Zeilen, je `count == 1`):

```text
- Before replacing it, verify exclusive ownership of the previous demo's containers, volumes, network and private runtime directory. Retire it through the project's teardown verb and verify they are gone; a stopped runtime is not a retired one. Preserve review evidence and unrelated resources.
- Do not compose container, volume, network or directory removal yourself; an unattended guard refuses it.
```

**NEU** (eine Zeile, die zweite entfällt):

```text
- Before replacing it, verify exclusive ownership of the previous demo's containers, volumes, network and private runtime directory. Retire it through the project's teardown verb when the project has one, otherwise with the project's own container, volume and network removal commands, and verify they are gone; a stopped runtime is not a retired one. Preserve review evidence and unrelated resources.
```

### Schritt 6 — `references/setup.md:145` (Compose-Teardown in die Freigabeliste)

Ohne Freigabe bleibt die erlaubte Handlung im Worker unbenutzbar: `docker compose down` fällt unter den Container-Lebenszyklus (`tools/approval_detection.py:603`) und liefert `ask-approval`. Die permanente Allowlist wird jedoch **vor** dieser Prüfung ausgewertet (`tools/approval.py:1228`, `tools/approval_floors.py:184-205`: exakter Text oder fnmatch-Glob, zusammengesetzte Zeilen nie). Gemessen in einem isolierten `HERMES_HOME` am 2026-11-25:

| Freigabe | Kommando | Verdikt |
|---|---|---|
| `docker compose -f * down` | `docker compose -f docker/docker-compose.yml down` | `allow` |
| `docker compose -f * down -v` | `docker compose -f /home/mariko/projects/soos/de.uke.iam.soos/docker/docker-compose.yml down -v` | `allow` |
| — | `docker compose down` (ohne `-f`) | `ask-approval` |
| — | `docker stop <container>` | `ask-approval` |

**ALT** (`count == 1`, die Zeile endet mit „… never a wildcard."):

```text
Omit entries whose entrypoint or verb the project does not have. When the Planner must construct the environment before its guide exists, add only the exact `docker compose -f <absolute dev compose path> build`, `up -d`, `down`, `ps` and `logs` entries; never `-v` and never a wildcard. The `demo.sh user` entry stays the bare script invocation: supply the password only through the environment variable the project documents, never as an argument and never in a grant.
```

**NEU:**

```text
Omit entries whose entrypoint or verb the project does not have. When the Planner must construct the environment before its guide exists, add only the exact `docker compose -f <absolute dev compose path> build`, `up -d`, `down`, `ps` and `logs` entries; never `-v` and never a wildcard. The `demo.sh user` entry stays the bare script invocation: supply the password only through the environment variable the project documents, never as an argument and never in a grant.

When the project has a demonstration Compose stack and no teardown script, grant its teardown as `docker compose -f * down` and `docker compose -f * down -v`. The wildcard covers relative and absolute Compose paths; both entries stay limited to the `down` verb, and the wildcard ban above continues to apply to the development entries. The permanent allowlist is matched before the dangerous-command gate, so a matching entry runs unattended; the bare `docker compose down` form remains gated, so the guide names the explicit `-f` form.
```

**Voraussetzung:** keine; betrifft nur Teams, die eine Demo ohne Teardown-Skript betreiben.
**Aufwand:** ein Absatz. `references/update.md` braucht keine Änderung: der Policy-Abgleich vergleicht je Team gegen die gespeicherte Baseline, die den neuen Eintrag nach dem nächsten Lauf enthält.

### Schritt 7 — geprüft, keine Änderung

- `templates/roles/reviewer.SOUL.md.template:86` und `templates/roles/coder.SOUL.md.template:54` greifen erst, wenn eine Demo-Karte existiert; sie ordnen keine an. Bleiben.
- `templates/roles/planner.SOUL.md.template:98` („For a completed demo handover …") ist ebenfalls kartenbedingt. Bleibt.
- `skills/brownfield-feature-planning/references/kanban-phase-release.md:21` gilt nur, wenn die geplante Änderung den Teardown-Befehl selbst repariert. Diese Bedingung trägt bereits. Bleibt.
- Die Zeile `- When the project has an assigned development environment or a demonstration runtime, it is yours to operate.` in allen drei SOULs ist bedingt formuliert und deckt den Fall „gibt es nicht" schon ab. Bleibt.

## Testanpassungen

Diese Assertions pinnen die gestrichenen Sätze und müssen im selben Changeset mitgehen:

| Datei:Zeile | heute | danach |
|---|---|---|
| `references/test_render_reasoning.py:117` | `assertIn("When the project has a demonstration runtime, add a final \`Demo handover\` card", tickets)` | auf den neuen Kundewunsch-Satz umhängen |
| `references/test_render_reasoning.py:155` | `assertIn("retire a running demonstration runtime.", rendered["planner"])` | auf „when a demonstration runtime is running, retire it" umhängen |
| `references/test_render_reasoning.py:156-159` | `teardown`-String in Planner und Skill | durch den neuen Teardown-Satz ersetzen, beide Fundstellen |
| `references/test_render_reasoning.py:160` | `assertIn("Create the demonstration user via \`demo.sh user\`…")` | auf den neuen Befehlssatz umhängen |
| `references/test_build_evidence.py:141` | Teardown-Satz des Dev-Skills | neuen Satz einsetzen |
| `references/test_build_evidence.py:142` | `assertIn("Do not compose container, volume, network or directory removal yourself")` | zu `assertNotIn` auf das gestrichene Verbot invertieren |

`references/test_update_team.py:498-499` bleibt unverändert grün, weil beide `demo.sh`-Literale im Skill erhalten bleiben.

## Verifikation

1. Neue Assertions gegen den Basisstand rot zeigen (`git stash`, Template-Strings im Scratch zählen), dann grün.
2. `python3 -B -m unittest references.test_render_reasoning` und `references.test_build_evidence` einzeln.
3. Gesamtsuite als Hintergrundlauf (`python3 -B -m unittest discover -s references -p 'test_*.py'`), erwartet `OK (skipped=1)`.
4. Renderprobe der drei SOULs mit Beispielbindungen: Platzhaltermenge unverändert, kein `{{` im Ergebnis.
5. Freigabe-Nachweis nach dem Setzen: `hermes -p <rolle> approvals test --json -- 'docker compose -f <relativer Pfad> down'` erwartet `allow`, dasselbe mit absolutem Pfad und `-v` ebenfalls `allow`, und `docker compose down` ohne `-f` weiter `ask-approval`. Vorher in einem isolierten `HERMES_HOME` vorgeführt; nach dem Rollout am echten Profil zu wiederholen.
6. Bump **3.1.0 → 3.1.1** in `SKILL.md` und `manifest.json` (Textänderung plus eine neue Pflichtzeile in der Freigabeliste; kein Renderfeld, kein Helferzustand).

## Wirkung auf bestehende Teams

Der Text erlaubt danach, was die Laufzeit schon kann; die Freigabezeile macht die Lücke zu. Für Teams mit eigener Demo ohne Teardown-Skript kommen beim nächsten Update zwei Einträge in `command_allowlist` (Schritt 6), sonst keine Änderung. Für das Team soos heißt das konkret: `docker compose -f * down` und `docker compose -f * down -v` in allen drei Rollen, dazu die gespeicherte Baseline in `confirmed_bindings.command_allowlists`. Ob das sofort für soos gesetzt wird, ist eine eigene Freigabe und nicht Teil dieses Maker-Plans.

## Nichtziele

- Kein neues Renderfeld, keine Änderung an Coder- oder Reviewer-Template, keine Änderung an `settings`.
- Die Regel „höchstens eine Demo, sie zeigt den letzten unabhängig geprüften Commit" bleibt unverändert.
- Kein Ersatz für `demo.sh`: Der Maker schreibt weiterhin kein Demo-Skript, er verlangt nur keines mehr.
- Kein Freibrief für `docker compose *`: die zwei Einträge bleiben auf `-f` plus `down` beschränkt; `docker stop` und `docker compose down` ohne `-f` bleiben gegated.

## Zurückgezogen gegenüber v1

Nichts; Erstfassung.
