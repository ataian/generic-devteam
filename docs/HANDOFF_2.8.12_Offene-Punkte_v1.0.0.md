# Übergabe — Stand nach Maker 2.8.12

| Feld | Wert |
|---|---|
| Datum | 2026-11-15 |
| Maker | **2.8.12** / `dbf7cc1`, Branch `v3`, Arbeitsbaum sauber, **nicht gepusht** |
| Team SG1 | installiert 2.8.12 / `dbf7cc173c8a`, 51 verwaltete Ziele |
| Pakettests | 212 OK, 1 übersprungen |
| Budget | Skill gesamt 92.425 / 93.000 Bytes; Paar `SKILL.md` + `kanban-phase-release.md` 25.892 / 26.000 |
| MTB-Repo | Branch `feature/t_741139dc-maxtest_lauf4` @ `8b1aa423`; `maxdevelop` @ `e1482bcd` |
| Docs-Repo | `081daff` (Lauf-4-Plan), Arbeitsbaum sauber, **nicht gepusht** |
| Hermes | v0.23.1, Mattermost-Patch **uncommitted** im Checkout |

## 1. Was seit dem letzten Stand entschieden und umgesetzt wurde

| Version | Inhalt |
|---|---|
| 2.8.9 | Branch je Ticket, Startpunkt erfragen, Invarianten mit ihren Tests, Rot-vor-grün, Daten-/Exportverträglichkeit, Quelle gegen Ausführung getrennt, Retro nur erwähnt |
| 2.8.10 | Planner legt den Branch an und setzt `branch_name`; Jira-Ticket erfragen; Namensregel als Vorschlag (Jira-Key, Kundenname gewinnt); Preflight von Einrichtungsprüfungen befreit; `hermes send --to mattermost:<id>`; Aufräumen aus der Coder-Rolle entfernt; Abschlussbericht auf Abweichungen begrenzt; neuer Skill `devteam-cleanup` |
| 2.8.11 | Send-Satz ohne Prosa und ohne Update-Klausel; Cleanup-Skill mit Auslöser statt Verbot; Budget-Regel in `AGENTS.md` geschärft |
| 2.8.12 | Planner-Regel „Use the installed tool for a job; do not build a script with the same purpose." ersetzt die Validierungswerkzeug-Formulierung; die Einzelfall-Zeile zum fehlgeschlagenen Send ist gestrichen |

Die Lauf-4-Analyse liegt vollständig unter `/home/mariko/projects/devteam-tokenprofiling/ecog-replay-2026-11-14-lauf4/` (fünf Stränge plus `VERGLEICH_2.8.9_Laeufe-1-2-3-4_v1.0.0.md`).

## 2. Offene Entscheidungen

### 2.1 PR-Paket (größter offener Block)

Datei: `/home/mariko/projects/generic-devteam/docs/PLAN_2.8.9_Pull-Request-Prozess_v1.0.0.md`.

Enthält: 2.2 PR durch den Planner, 2.3 Pipeline rücklesen, 2.10 Ticket↔PR-Verknüpfung, 5.2 `gh`, 5.3 GitHub Actions (nicht `deploy-dev.yml`), 5.4 Merge bleibt Menschensache. Sechs Entscheidungen sind dort offen: wer pusht, welches Credential, `gh` oder API, welche Workflows laufen dürfen, Rückweg bei roter Pipeline, Branch nach dem Merge.

**Nebenbefund:** Der Plan ist auf Ausgangsversion 2.8.9 benannt, der Maker steht bei 2.8.12. Vor der Besprechung entweder auf 2.8.12 neu benennen oder im Kopf der Datei die Basis fortschreiben.

### 2.2 Regelumfang allgemein

Max' Maßstab aus dieser Session: eine neue Regel nur für einen wiederkehrenden, ursächlich verstandenen Fall. Vorfall-Regeln blähen die Referenzen auf. Beim nächsten Vorschlag zuerst prüfen, ob eine bestehende Regel den Fall schon deckt.

### 2.3 Budget des Planungsskills

575 Bytes Luft im Gesamtdeckel. Die nächste Prosa-Ergänzung dort muss kürzen oder auslagern. Kandidat für eine Aufteilung ist `operator-script-acceptance.md` (18.203 Bytes, eigener Deckel 32.500) — nicht entschieden, nur notiert.

## 3. Vorbereitung des nächsten Laufs

Die Bereinigung ist in `devteam-run-profiling` (Schritt 6 und 8) beschrieben und in dieser Session zweimal nachgeschärft:
- Rollen-Skills **und** deren `references/*.md` gegen die Paketfassung hashen und zurücksetzen; lokale Anpassungen überleben Maker-Updates bauartbedingt.
- Nach Auftragsresten **nach Dateinamen und nach Inhalt** scannen; eine reine Inhaltssuche hat beim letzten Mal 496 KB übersehen.

Konkret für Lauf 5 zu erledigen:

| Gegenstand | Stand jetzt |
|---|---|
| MTB-Branch | Repo steht auf `feature/t_741139dc-maxtest_lauf4`; Startpunkt für den neuen Lauf festlegen (`maxdevelop` ist der Vor-Lauf-4-Stand) |
| Board sg1 | Karte `t_741139dc` mit Kommentaren, Runs, Events und Wake-Abo entfernen |
| Sessions | fünf Sitzungen des Laufs 4 in jack/carter/daniel |
| Codex | Rollouts beider Häuser; Threads in `carter/devteam/codex-home` gezielt löschen, Datenbanken selbst erhalten |
| Hindsight SG1 | Fakten und Dokumente des Laufs; danach Recall-Probe auf den Auftrag |
| Mattermost `iam/sg1` | 6 Posts aus dem 14.11. (23:24–23:33) |
| Docs-Repo | `PLAN_1.1.0_ECOG-5.md` und `DESIGN_ECOG-5.md` samt Index-Links aus `081daff` |
| Caches | Scratch, Prozess-Ergebnisse, Logs, `state_meta`, `async_delegations`, FTS |
| CBM | Index der MTB liegt jetzt im Archiv und wird beim ersten Gebrauch neu gebaut |

## 4. Was nur ein Lauf beweisen kann

- Ob der Planner den Branch wirklich selbst anlegt und `branch_name` gesetzt wird (in Lauf 4 blieb das Feld leer).
- Ob der Abschlussbericht die Abweichungen nennt und die planmäßige Arbeit weglässt.
- Ob `hermes send --to mattermost:<id>` aus dem Planner heraus ohne Eigenbau funktioniert.
- Ob der Preflight ohne Einrichtungsprüfungen kürzer und trotzdem vollständig ist.
- Ob `devteam-cleanup` als aufgerufener Schritt trägt — er wurde noch nie ausgeführt.

## 5. Bekannte Reste, nicht erledigt

- **Mattermost:** 11 Posts stammen von `ataian` selbst; der Bot darf sie nicht löschen (403). Sie stehen weiter im Kanal. Löschen entweder manuell oder mit Admin-Token.
- **Hermes-Patch:** `plugins/platforms/mattermost/send_targets.py` und der Adapter-Patch sind uncommitted. Nach jedem `hermes update` neu anwenden: `/home/mariko/projects/mattermost-send-target.patch`, Prüfschritt in `System/Hermes-Mattermost-Send-Patch.md`.
- **Nicht gepusht:** Maker `dbf7cc1` (Branch `v3`) und Docs `081daff`.
- **Branches:** `maxtest_lauf3` (`4f06947a`) und die älteren `ecog5`-Branches bleiben lokal bestehen; der Remote-Name des Lauf-3-Branches weicht ab.
- **`--list mattermost`** bleibt in Profilen ohne Kanaldirectory leer. Als Regel im Skill abgefangen, als Hermes-Verbesserung nicht angegangen.

## 6. Ideen, die bewusst nicht weiterverfolgt wurden

- Upstream-PR für die Mattermost-Zielsyntax bei `NousResearch/hermes-agent` (Fork `ataian`, Patch liegt bereit). Nur Max entscheidet, ob das eingereicht wird.
- Aufteilung von `operator-script-acceptance.md`, um Budget zu gewinnen.
- Eine harte Sperre für `devteam-cleanup` gegen unbeabsichtigtes Laden: in Hermes nicht vorhanden (`disable_model_invocation` existiert nicht), deshalb über Auslöser und ersten Satz gelöst.
