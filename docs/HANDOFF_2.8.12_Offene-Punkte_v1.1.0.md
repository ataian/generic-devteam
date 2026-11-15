# Übergabe — Stand nach Maker 2.8.12

| Feld | Wert |
|---|---|
| Datum | 2026-11-15 |
| Maker | **2.8.12** / `dbf7cc1`, Branch `v3`, Arbeitsbaum sauber, **nicht gepusht** |
| Team SG1 | installiert 2.8.12 / `dbf7cc173c8a`, 51 verwaltete Ziele, 63 Baselines |
| Pakettests | 212 OK, 1 übersprungen |
| Budget | Skill gesamt 92.425 / 93.000 Bytes; Paar `SKILL.md` + `kanban-phase-release.md` 25.892 / 26.000 |
| MTB-Repo | `maxdevelop` @ `e1482bcd`, Arbeitsbaum sauber; `feature/t_741139dc-maxtest_lauf4` @ `8b1aa423` bleibt als Branch |
| Docs-Repo | `d8725cc`, Arbeitsbaum sauber, **nicht gepusht** |
| Hermes | v0.23.1, Mattermost-Patch **uncommitted** im Checkout |
| Fujiko-Review | fertig, Karte `t_a88bfc3a` (Board `generic-devteam`), Besprechung steht aus |
| Lauf 5 | vorbereitet, Team kennt den ECOG-Auftrag nicht mehr |

## 0. Was diese Session geändert hat

### 0.1 Fujiko: TAS-Review der Maker-Regeltexte — Ergebnis liegt, Besprechung offen

Bewertet wird nicht in dieser Datei, sondern in einer eigenen Sitzung.

| Feld | Wert |
|---|---|
| Board / Karte | `generic-devteam` / `t_a88bfc3a`, `done`, ein Lauf, 18 Minuten |
| Auftrag | `/home/mariko/projects/generic-devteam-review/AUFTRAG_2.8.12_TAS-Review_v1.0.0.md` |
| Bericht | `/home/mariko/projects/generic-devteam-review/REVIEW_2.8.12_TAS_v1.0.0.md` (683 Zeilen) |
| Unabhängige Prüfung | Abschnitt im Bericht; Läufe in `UNABHAENGIG_prompt_v1.0.0/1.md` und `UNABHAENGIG_ergebnis_v1.0.0/1.md` |
| Prüfobjekt | `/home/mariko/projects/generic-devteam-review-2.8.12`, 67 Dateien — Paketkopie laut `manifest.json`, ohne `docs/`, ohne `.git` |

Umfang des Auftrags: Prosa und TAS-Stilverstöße, Doppelungen, Widersprüche, Maker-Text in Rollentexten;
je Finding ALT und NEU als zusammenhängender Block mit Prüfschritt. Geprüft wurden `SKILL.md`,
`references/`, `templates/roles/*.template` und `skills/`; `README.md`, `NOTICE.md`, `AGENTS.md`,
`LICENSE` und die Python-Dateien lagen ausdrücklich außerhalb.

Beim Lesen für diese Übergabe fiel eine Differenz auf, die in der Besprechung zu klären ist: der
Bericht enthält 14 Finding-Blöcke (`### F-…`), der Abschlusskommentar der Karte nennt 11 Findings.

### 0.2 `hermes send --list mattermost` bleibt leer — bewusst

In Teamprofilen fehlt `channel_directory.json`, deshalb zeigt `--list` „no channels discovered yet".
Das ist keine Lücke des Makers: das Verzeichnis ist Laufzeitzustand des Gateways (Aufbau beim Start
und alle 5 Minuten aus Adapter-Erkennung und Session-Origins), der Maker schreibt es nie. Der
Mattermost-Adapter liefert weder `list_channels()` noch `configured_channels()`, und
`channel_aliases.json` gibt es in keinem Profil.

Entschieden: kein Alias-File, kein Maker-Schritt, keine Änderung an Hermes. Der Versand läuft über
`hermes send --to mattermost:<id>`; der Patch lässt 26-stellige IDs verbatim durch
(`_parse_target_ref('mattermost', '1ubob9…') → (id, None, True)`), ein Directory ist dafür nicht nötig.
Kanalname als Ziel (`#kanalname`) bleibt in Teamprofilen wirkungslos, wird aber nicht gebraucht.

### 0.3 `docs/` ist keine Betriebsdoku

`manifest.json` listet 67 Dateien ohne `docs/`; `NOTICE.md:116` und `README.md:54` schließen den Ordner
ausdrücklich aus Paket und Installation aus. Der Ordner ist Weiterentwicklungshistorie des Makers und
wurde für die Review bewusst nicht mitgegeben — nicht per Verbot, sondern physisch nicht vorhanden.
Der Maker-Checkout blieb unberührt.

### 0.4 Lauf 5 vorbereitet (Wissensschnitt am 15.11.)

Archiv: `/home/mariko/.local/share/mariko-comparisons/ecog5-lauf5/20261115_0829/`, 101 Dateien,
290 MB, Rechte 0700, `inventory.json` mit SHA-256 je Datei; Bericht `AUFRAEUMEN_20261115.md` darin.

| Gegenstand | Ergebnis |
|---|---|
| Hindsight `SG1` | 490 → 363 Knoten; 5 Dokumente, 69 Fakten, 1 verwaiste Beobachtung entfernt; Treffer für `ecog` oder `mvh` in `documents`, `chunks`, `memory_units`, `invalidated_memory_units` je 0; andere Banken unverändert |
| Board `sg1` | `t_741139dc` samt 53 Events, 2 Kommentaren, 2 Runs und Wake-Abo entfernt; `t_09e86ca3`, `t_68574e8d`, `t_94752144` bleiben mit ihren Abos |
| Sessions | 5 Sitzungen, 648 Nachrichten, Ledger-Zeilen und 4 `state_meta`-Zeilen entfernt, FTS neu gebaut, VACUUM; Stand jack 4, carter 7, daniel 6 |
| Pre-Update-Snapshots | 4 Nachrichten mit Bezug entfernt, Rollback-Dateien bleiben |
| Codex | 6 Threads (394 Items), 3 Rollouts; `state_5` und `thread_history_1` bleiben, `integrity_check: ok` |
| CBM | MTB-Index 139.067.392 Bytes ins Archiv verschoben, Neubau beim nächsten Zugriff |
| Caches/Logs | 66 Dateien gelöscht, 4 Betriebslogs auf 0 Byte geleert, 7.566 KB archiviert |
| Docs-Repo | Plan, Design, 2 Index-Zeilen, 2 `.gitignore`-Zeilen entfernt (Commit `d8725cc`) |
| Mattermost `iam/sg1` | 6 lebende Posts vom 14.11. gelöscht; von 201 archivierten Posts waren 135 schon soft-gelöscht |

Der Arbeitsbaum des MTB-Repos steht auf `maxdevelop` — bewusst, damit der Planner den Startpunkt
erfragt statt ihn abzulesen.

## 1. Was seit dem letzten Stand entschieden und umgesetzt wurde

| Version | Inhalt |
|---|---|
| 2.8.9 | Branch je Ticket, Startpunkt erfragen, Invarianten mit ihren Tests, Rot-vor-grün, Daten-/Exportverträglichkeit, Quelle gegen Ausführung getrennt, Retro nur erwähnt |
| 2.8.10 | Planner legt den Branch an und setzt `branch_name`; Jira-Ticket erfragen; Namensregel als Vorschlag (Jira-Key, Kundenname gewinnt); Preflight von Einrichtungsprüfungen befreit; `hermes send --to mattermost:<id>`; Aufräumen aus der Coder-Rolle entfernt; Abschlussbericht auf Abweichungen begrenzt; neuer Skill `devteam-cleanup` |
| 2.8.11 | Send-Satz ohne Prosa und ohne Update-Klausel; Cleanup-Skill mit Auslöser statt Verbot; Budget-Regel in `AGENTS.md` geschärft |
| 2.8.12 | Planner-Regel „Use the installed tool for a job; do not build a script with the same purpose." ersetzt die Validierungswerkzeug-Formulierung; die Einzelfall-Zeile zum fehlgeschlagenen Send ist gestrichen |

Die Lauf-4-Analyse liegt vollständig unter `/home/mariko/projects/devteam-tokenprofiling/ecog-replay-2026-11-14-lauf4/` (fünf Stränge plus `VERGLEICH_2.8.9_Laeufe-1-2-3-4_v1.0.0.md`).

## 2. Offene Entscheidungen

### 2.1 Fujikos Findings (zuerst in der nächsten Sitzung)

Dort wird entschieden: welche Findings übernommen werden, in welcher Reihenfolge, und ob der Maker vor
einem Team-Update weiterentwickelt wird. Die unabhängige Prüfung hat einzelne Vorschläge bereits
eingeschränkt; ihre Begründungen stehen im Abschnitt „Unabhängige Prüfung" des Berichts.

### 2.2 PR-Paket (größter offener Block)

Datei: `/home/mariko/projects/generic-devteam/docs/PLAN_2.8.9_Pull-Request-Prozess_v1.0.0.md`.

Enthält: 2.2 PR durch den Planner, 2.3 Pipeline rücklesen, 2.10 Ticket↔PR-Verknüpfung, 5.2 `gh`, 5.3 GitHub Actions (nicht `deploy-dev.yml`), 5.4 Merge bleibt Menschensache. Sechs Entscheidungen sind dort offen: wer pusht, welches Credential, `gh` oder API, welche Workflows laufen dürfen, Rückweg bei roter Pipeline, Branch nach dem Merge.

**Nebenbefund:** Der Plan ist auf Ausgangsversion 2.8.9 benannt, der Maker steht bei 2.8.12. Vor der Besprechung entweder auf 2.8.12 neu benennen oder im Kopf der Datei die Basis fortschreiben.

### 2.3 Regelumfang allgemein

Max' Maßstab aus der Session vom 14.11.: eine neue Regel nur für einen wiederkehrenden, ursächlich verstandenen Fall. Vorfall-Regeln blähen die Referenzen auf. Beim nächsten Vorschlag zuerst prüfen, ob eine bestehende Regel den Fall schon deckt.

### 2.4 Budget des Planungsskills

575 Bytes Luft im Gesamtdeckel. Die nächste Prosa-Ergänzung dort muss kürzen oder auslagern. Kandidat für eine Aufteilung ist `operator-script-acceptance.md` (18.203 Bytes, eigener Deckel 32.500) — nicht entschieden, nur notiert.

## 3. Vorbereitung des nächsten Laufs — erledigt

Ablauf und Fallen stehen in `devteam-run-profiling` („Wiederholungslauf vorbereiten") und dessen
`references/replay-preparation.md`. Beide Lehren aus dem 14.11. gelten weiter: Rollen-Skills **und**
deren `references/*.md` gegen die Paketfassung hashen, und Reste **nach Dateinamen und nach Inhalt**
getrennt suchen.

| Gegenstand | Stand |
|---|---|
| MTB-Branch | `maxdevelop` @ `e1482bcd`, sauber; der Planner fragt nach dem Startpunkt (Absicht) |
| Board sg1 | keine Karte des Vorlaufs, keine ECOG-Kommentare; drei Docker-Karten als Vorgeschichte |
| Sessions | keine Sitzung des Vorlaufs in jack, carter, daniel |
| Codex | keine Threads und keine Rollouts des Vorlaufs in beiden Häusern |
| Hindsight SG1 | 363 Knoten, kein ECOG-Treffer; Wissen zur Entwicklungsumgebung bleibt |
| Mattermost `iam/sg1` | keine Abschluss- oder Statusposts des Vorlaufs |
| Docs-Repo | `d8725cc`, Plan und Design des Auftrags entfernt |
| Caches, Snapshots, FTS | gescannt, archiviert, geleert bzw. bereinigt |
| CBM | Index archiviert, Neubau beim ersten Zugriff |
| Archiv | `~/.local/share/mariko-comparisons/ecog5-lauf5/20261115_0829/` mit Inventar |

Der Nachscan über die drei Profile hat 16 Restdateien mit Treffern aus dem 09./10.11.-Lauf stehen
lassen: dort steht `MVH` als `PseudonymType.MVH` im Produktcode und `ecog` als Verzeichnispfad
(`cypress/ecog/`). Kein Wissen zum Auftrag, deshalb belassen und hier benannt.

## 4. Was nur ein Lauf beweisen kann

- Ob der Planner den Branch wirklich selbst anlegt und `branch_name` gesetzt wird (in Lauf 4 blieb das Feld leer).
- Ob er Branchname und Startpunkt erfragt, statt `maxdevelop` abzulesen.
- Ob der Abschlussbericht die Abweichungen nennt und die planmäßige Arbeit weglässt.
- Ob `hermes send --to mattermost:<id>` aus dem Planner heraus ohne Eigenbau funktioniert.
- Ob der Preflight ohne Einrichtungsprüfungen kürzer und trotzdem vollständig ist.
- Ob `devteam-cleanup` als aufgerufener Schritt trägt — er wurde noch nie ausgeführt.

## 5. Bekannte Reste, nicht erledigt

- **Mattermost:** 59 Posts vom 09.11. aus dem Lauf zur Entwicklungsumgebung und ein menschlicher Post vom 13.11. stehen weiter im Kanal. Sie tragen kein ECOG-Wissen und bleiben absichtlich.
- **Kanalname als Ziel:** `--to mattermost:#kanalname` bleibt in Teamprofilen wirkungslos, weil dort kein Kanalverzeichnis liegt. Bewusst offen.
- **Hermes-Patch:** `plugins/platforms/mattermost/adapter.py` und `send_targets.py` sind uncommitted. Nach jedem `hermes update` neu anwenden: `/home/mariko/projects/mattermost-send-target.patch`, Prüfschritt in `System/Hermes-Mattermost-Send-Patch.md`.
- **Nicht gepusht:** Maker `dbf7cc1` (Branch `v3`) und Docs `d8725cc`.
- **Branches:** `maxtest_lauf3` (`4f06947a`), `feature/t_741139dc-maxtest_lauf4` (`8b1aa423`) und die älteren `ecog5`-Branches bleiben lokal bestehen; der Remote-Name des Lauf-3-Branches weicht ab.
- **Review-Kopie:** `/home/mariko/projects/generic-devteam-review-2.8.12` bleibt liegen, solange die Besprechung läuft; danach löschbar.

## 6. Ideen, die bewusst nicht weiterverfolgt wurden

- `channel_aliases.json` vom Maker schreiben lassen, damit Kanalnamen in `--list` erscheinen. Nicht nötig, weil der Versand über IDs läuft.
- Upstream-PR für die Mattermost-Zielsyntax bei `NousResearch/hermes-agent` (Fork `ataian`, Patch liegt bereit). Nur Max entscheidet, ob das eingereicht wird.
- Aufteilung von `operator-script-acceptance.md`, um Budget zu gewinnen.
- Eine harte Sperre für `devteam-cleanup` gegen unbeabsichtigtes Laden: in Hermes nicht vorhanden (`disable_model_invocation` existiert nicht), deshalb über Auslöser und ersten Satz gelöst.
