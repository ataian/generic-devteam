# PLAN — Settings-Parität zwischen Setup und Update

| Feld | Wert |
|---|---|
| Appversion (Ausgangsstand) | Maker **2.8.15** |
| Dokumentversion | v1 |
| Datum | 2026-11-15 |
| Charakter | Vorbereitung. Nicht umgesetzt; der Checkout bleibt bis zur Freigabe unverändert. |
| Betrifft | `references/update.md`, `references/setup.md`, `references/verification.md` — kein Code im Helfer |

## 1. Anlass

Das Setup schreibt Konfigurationswerte, das Update schreibt sie nicht. Werte, die der Maker als
Politik vorschreibt, können dadurch in einem bestehenden Team dauerhaft vom Sollstand abweichen,
obwohl die Dateien korrekt sind. Max' Einordnung: Der Updater soll gelernte Team-Erweiterungen
sanft einarbeiten statt zu überschreiben — Settings dagegen sind dazu gedacht, dass sie gesetzt
werden.

Belege für den heutigen Zustand:

- `references/update_team.py:3` — „No Hermes bootstrap, networking, worker control, configuration
  writes or deletion." Der Helfer kann Konfiguration grundsätzlich nicht schreiben.
- `references/update.md:16` — „Do not change models, plugins, integrations, configuration, or
  external services through the file helper."
- `references/update.md:205–209` — für `skills.creation_nudge_interval` ist der Sonderweg schon
  ausformuliert: melden, nicht setzen, eigene Freigabe einholen. Für die übrigen Setup-Werte fehlt
  jede entsprechende Regel.
- `references/setup.md:125–155, 203–205` — das Setup setzt `terminal.cwd`, `model.provider`,
  `model.default`, `agent.reasoning_effort`, `kanban.auto_subscribe_on_create`,
  `security.protected_instruction_files`, `skills.creation_nudge_interval` und die
  Kanban-Tool-Auswahl je Plattform.

Ist-Stand SG1 nach dem 2.8.15-Update (2026-11-15, gemessen): alle drei Rollen führen
`terminal.cwd=/home/mariko/projects/mtb`, `kanban.auto_subscribe_on_create=false`,
`security.protected_instruction_files=false`; Jack führt `skills.creation_nudge_interval=0`,
Carter und Daniel haben keinen eigenen Wert (Default 10, so gewollt); `kanban.auto_decompose` steht
in den Rollenprofilen auf `true`, zentral in `/home/mariko/.hermes/config.yaml:225` auf `false` und
wirkt über den Dispatcher. Keine Drift erreicht das Team heute — der Plan schließt die Lücke, bevor
sie auftritt.

## 2. Die Entscheidung, die dieser Plan vorlegt

Settings werden in zwei Klassen geteilt. Die Klasse bestimmt, was ein Update tun darf.

**Maker-Politik** — der Wert folgt aus dem Maker, nicht aus dem Kunden. Ein Update setzt ihn oder
verifiziert ihn und meldet jede Abweichung. Kandidaten: `skills.creation_nudge_interval` (Planner),
`kanban.auto_subscribe_on_create`, effektives `security.protected_instruction_files`, die
Kanban-Tool-Auswahl des Planner, effektives `kanban.auto_decompose`.

**Kundenentscheidung** — der Wert gehört dem Team. Ein Update liest ihn, berichtet eine Abweichung
gegen den Setup-Record und überschreibt ihn nie. Kandidaten: `model.provider`, `model.default`,
`agent.reasoning_effort`, `terminal.cwd`, Board, Hindsight-Bank, Mattermost-Kanal und `/sethome`,
Codex-CLI-Pfad und `config.toml`-Modell des Team-Codex.

Einordnungskriterium: Lässt sich der Wert allein aus dem Maker ableiten, ohne eine Kundenangabe zu
brauchen, ist er Politik. Braucht er eine Angabe, die nur das Team kennt, ist er Kundenentscheidung.

## 3. Vorgesehene Schritte

Reihenfolge nach benötigter Berechtigung: C1 und C2 sind reine Textänderungen und brauchen keine
neue Berechtigung. C3 ändert die Setup-Aufzeichnung und berührt bestehende Teams nicht.

### C1 — Eigener Update-Abschnitt „Required configuration parity"

**Ort:** `references/update.md`, neuer Abschnitt zwischen „Planner Kanban tools" (endet Zeile 225)
und „Required upstream companion update" (beginnt Zeile 227). Zusätzlich ein Satz in der
Scope-Liste Zeile 17, damit der Abschnitt als eigener freigabepflichtiger Prosa-Schritt gilt.

**Voraussetzung:** keiner; der Abschnitt verweist auf die Werte, die C2 im Setup-Record ablegt.

**Vorgeschlagener Text (englisch, TAS):**

```
## Required configuration parity

Apply this procedure on every requested team update, including unchanged-version and no-op file updates.
The file helper does not write configuration; installation metadata does not certify these bindings.
Read the recorded policy values from `confirmed_values` in the team's private setup record before comparing.
Policy settings are the Planner's `skills.creation_nudge_interval`, `kanban.auto_subscribe_on_create`, the effective `security.protected_instruction_files`, and the Planner's Kanban tool selections.
Customer settings are provider, model, reasoning level, working directory, board, memory bank, and communication bindings; read them but never overwrite them.

1. **Inspect:** Capture each policy setting and each customer setting through the native configuration path before any write.
   Record the current value, its source (profile-local, central, or default) and the effective override.
   Compare the policy settings with the recorded values and list every difference.
2. **Approve:** Include the concrete differences and the exact writes in the complete update scope.
   Obtain one authorization for those configuration writes; `--dependency-decision` alone does not grant it.
   Preserve unrelated configuration, central policy and every customer setting.
3. **Back up:** Save the affected configuration files and complete readbacks outside the profile homes before writing.
4. **Apply:** Recheck each inspected value for concurrent drift immediately before writing, and stop on a difference.
   Set only the approved policy values through the supported native commands.
   Accept a central setting that already provides the required effective value without adding a duplicate profile entry.
5. **Verify:** Read back each written value and each preserved customer value.
   Compare unrelated settings against the captured state and record the readbacks in the existing private update record.
Configuration readbacks do not establish adoption by a running session; do not restart one to obtain that claim.
Report `files updated; team update incomplete` while an approved parity write is pending.
```

**Erhalten bleibt:** der bestehende Sonderweg für `skills.creation_nudge_interval` in Zeile 208
bleibt als Zeiger stehen oder verweist auf den neuen Abschnitt — die dortige Aussage „der Helfer
setzt es nicht" ist weiterhin wahr und wird durch C1 nicht doppelt erzählt. Beim Umsetzen ist genau
eine der beiden Stellen zu wählen, nicht beide.

**Prüfschritt:** Der Abschnitt steht im Freigabe-Ablauf, nicht im Setup; jede Zahl der genannten
Settings muss in `setup.md` belegbar sein.

**Aufwand:** rund eine Stunde inklusive Anpassung der Prosa-Vertragstests.

### C2 — Politikwerte im Setup-Record festhalten

**Ort:** `references/setup.md`, Abschnitt 3 nach Zeile 155, plus ein Eintrag im
`confirmed_values`-Block des Record-Templates (`templates/setup-record.md`).

**Voraussetzung:** C1 braucht diese Werte als Vergleichsbasis.

**Vorgeschlagener Text (englisch, TAS):**

```
Record the confirmed policy values in `confirmed_values` as `PLANNER_SKILL_NUDGE_INTERVAL`, `KANBAN_AUTO_SUBSCRIBE_ON_CREATE` and `PROTECTED_INSTRUCTION_FILES_EFFECTIVE`.
Record each value with its effective source; a central setting is recorded as the central value, not as a profile override.
These values are the comparison basis for later updates; do not recompute them from the package version.
```

**Erhalten bleibt:** der bestehende Satz, dass ein korrektes zentrales `security.protected_instruction_files`
ohne Doppelung akzeptiert wird (`setup.md:148–149`), und die Kanban-Readback-Pflicht in Zeile 216.

**Prüfschritt:** `confirmed_values` in einem bestehenden Record bleibt rückwärts lesbar; fehlende
Schlüssel werden beim Update als „nicht aufgezeichnet" gemeldet statt erfunden.

**Aufwand:** rund 15 Minuten.

### C3 — Lesecheck im Verifikationsabschnitt

**Ort:** `references/verification.md:38` (Planner skill maintenance).

**Vorgeschlagener Text (englisch, TAS):**

```
Read back the effective policy values named in [Setup](setup.md#3-fresh-profiles-confirmed-models) and confirm the recorded `confirmed_values` entries match.
Read back every customer setting as unchanged against the preparation dataset.
```

**Aufwand:** rund 10 Minuten.

## 4. Offene Entscheidungen

Max entscheidet einzeln; bis dahin bleibt jeder Punkt offen und der Plan unverändert.

1. **Setzen oder melden:** Sollen Politikwerte beim Update gesetzt werden (Abweichung wird
   korrigiert) oder nur verifiziert und gemeldet? Empfehlung: setzen, wie bei
   `skills.creation_nudge_interval` von Max entschieden — sonst bleibt die Lücke bestehen.
2. **`security.protected_instruction_files`:** zentral verwalteter Wert gilt als erfüllt, ohne
   Profil-Eintrag. Soll ein Update eine zentrale Änderung an dieser Stelle überhaupt berichten, oder
   bleibt sie außerhalb des Team-Updates?
3. **Umgang mit Kundenwerten bei Abweichung:** Bericht an Max genügt, oder Rückfrage vor dem
   Abschluss? Empfehlung: Bericht, keine Rückfrage — der Wert gehört dem Team.
4. **Geltung bei unveränderter Maker-Version:** Soll die Paritätsprüfung bei jedem Update-Lauf
   stattfinden (wie die Companion-Prüfung), auch wenn keine Datei sich ändert? Empfehlung: ja.
5. **Ablage der Sollwerte:** `confirmed_values` im Setup-Record (C2) oder ein eigener Abschnitt im
   Record? Empfehlung: `confirmed_values`, weil es die einzige Rohwertquelle bleiben soll.
6. **Alt-Teams ohne aufgezeichnete Werte:** Vergleich gegen den Default des laufenden Hermes, oder
   nur melden, dass keine Aufzeichnung existiert? Empfehlung: nur melden, nichts annehmen.

## 5. Abnahmekriterien

1. Ein Update-Lauf nennt je Rolle den gemessenen Wert jedes Politik-Settings mit Quelle und
   effektiver Wirkung, vor und nach dem Lauf.
2. Eine Abweichung wird nur nach ausdrücklicher Freigabe geschrieben, mit Sicherung und Readback.
3. Kein Kundenwert wird durch ein Update verändert; jede Abweichung erscheint als Bericht.
4. `update_team.py` bleibt unverändert: keine Konfigurationsschreibung, kein Schemawechsel.
5. Ein zweiter Lauf gegen denselben Stand meldet null Abweichungen.
6. Die Paket-Suite läuft einmal am Ende grün.

## 6. Abgrenzung

Nicht enthalten: Änderungen an `update_team.py` oder an `installation.json`; Modelle, Provider und
Reasoning als Sollwerte; Rekonziliation von Mattermost, Hindsight, Board oder Codex-CLI-Version;
Neustarts von Diensten oder Sitzungen; rückwirkende Änderungen an bestehenden Records.

## 7. Aufwand und Testbasis

Summe der Textänderungen: rund 1,5 Stunden, ein Versionsbump (PATCH) für den gesamten Änderungssatz.
Prüfung: `python3 -B -m unittest discover -s references -p 'test_*.py'` einmal am Ende. Betroffen
sind die Prosa-Vertragstests, die Sätze aus `update.md` und `setup.md` wörtlich führen; vor dem
Streichstellen ist je Satz zu prüfen, welche Quelle die Assertion liest.
