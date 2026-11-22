# Maker 2.14.0 – Korrekturen aus Lauf 9

Freigegebener Umsetzungsplan, Dokumentversion 1. Ausgangspunkt: Maker 2.13.1 (`675e051`), ECOG-5 im MTB am 21./22.11.2026. Dieser Plan gilt für das Paket; er ist kein Auftrag zum Team-Update. Vorschlag mit Gegenrechnung und verworfenen Alternativen: `MAKER_PLAN_2.14.0_vorschlag.md` im Laufarchiv `/home/mariko/projects/devteam-tokenprofiling/ecog-replay-2026-11-22-lauf9/`. Alle nachfolgend genannten Laufartefakte liegen dort. Maßgeblich sind Diagnose, Codex-Rollouts, Board und Produktcommit, nicht die Arbeitsprofile des damaligen Teams.

## P1 – Testreparatur vom Produkt trennen

**Befund:** `DIAGNOSE_Cypress-Spec-Lauf9_v1.0.0.md` ordnet die fünf Reparaturen Autorenannahmen, dem Produktionsbuild und der Isolationsprüfung zu; keine wurde durch geänderte UI ausgelöst. Der Autor durfte die echte Seite nicht selbst testen. Die zwei bestandenen Browserfälle verletzten dennoch den Vertrag „genau ein Wegwerf-Patient“.

**Entscheidung:** Beim Testauftrag führt der Autor den Test selbst aus. Nur bei einer geteilten oder umkämpften Ressource bleibt die Laufzeit reserviert. Selektoren aus gerendertem DOM oder Komponentenquelle ableiten; erst nach Ausführung gegen die laufende Seite committen. Vor Änderungen an Anzahl oder Umfang der Fixtures die Isolationsprüfung lesen.

Ein Befund, der auch bei korrektem Produkt bestünde, gehört zum Prüfgerüst. Einzelnen Anker, Datensatz oder Parameter im selben Codex-Thread korrigieren. Für abgrenzbare mehrstufige Harness-Arbeit einen eigenen Codex-Aufruf verwenden: nur Testpfade schreibbar, Produktbaum nur lesbar. Hermes-Subagenten nur für Arbeiten, die Hermes-Werkzeuge oder eigene Skills brauchen. Karte, Commit und Übergabe bleiben beim Coder. Nach einer Ursachenreparatur und einer zweiten ausschließlich vom Prüfgerüst verursachten Runde stoppen. Befehl, Beobachtung, Beleg und kleinsten nächsten Schritt auf die Karte schreiben; bei technischer Blockade `capability`. Außerhalb der Befugnis oder bei kartenübergreifender Wirkung: `kanban_comment` mit Befund und Vorschlag, danach `kanban_block(kind="needs_input")`; keine eigene Karte. Der Planner schneidet eine im Aufbau befindliche Umgebung separat zu. Im Handoff trennt `Harness:` Befund, Ursache und Änderung vom Produkt; offene Punkte unter `Risks / gaps:` zum Planner. Keine neue Rolle, kein Reparaturticket pro Versuch.

## P2 – Codex am gleichen Arbeitsstand fortsetzen

**Befund:** Sieben Threads in Run 25; mehrere Reparaturthreads arbeiteten nacheinander am selben Selektor. Aus den Starts lässt sich kein nennenswerter Kostenvorteil für Resume ableiten. Der Gewinn ist der erhaltene Diagnosezustand.

**Entscheidung:** Ein primärer Thread je Implementierungsauftrag, niemals gleichzeitige Turns darin. Beim ersten `codex exec --json` die `thread_id` aus `thread.started` auf der Karte festhalten, Schlussnachricht aus der Ausgabedatei lesen. Für denselben Fehler, dieselbe Hypothese oder eine Reviewrückgabe am selben Stand über die konkrete Kennung und einen Folgeprompt von stdin fortsetzen; weder `--last` noch Suche nach dem jüngsten Rollout. Neuer Auftrag, unmögliche Fortsetzung oder bewusst frischer Blick: neuer Thread mit Grund auf der Karte. Brief unter 4 KB mit Zeiger auf die genaue Planrevision statt Plankopie; das Ergebnis an Auftragsgrenzen bewerten.

## P3 – Auf Prozessende warten

**Befund:** Run 25: 70 Prozessaufrufe, davon 49 Timeouts; die Karten hatten kein Laufzeitlimit. Der Standard von 180 Sekunden erzwang kurze Wartefenster.

**Entscheidung:** Jede Coder-Karte mit `--max-runtime 8h` anlegen (Hängerschutz für den ganzen Worker, kein Arbeitsbudget). Setup und Update setzen `terminal.timeout: 14400` bei Coder und Reviewer. Beim Warten vier Stunden anfordern; Prozessende beendet den Wait sofort. Ohne Ergebnis am Reaktionspunkt: letzten Output festhalten, als `capability` blockieren, nicht erneut warten. Kein Wrapper, keine Hermes-Kernänderung.

## P4 – Vollmatrix am finalen Kandidaten

**Befund:** Zwischen `54662123` und `b6eea944` liefen sechs vollständige Matrizen, fünf auf später verworfenen Ständen (`ledger/`, Run 25). **Entscheidung:** Zwischenstände mit `check` und ausgewähltem Test prüfen. Alle vorgeschriebenen Suiten einmal am finalen Kandidatencommit ausführen; erneut nur nach Änderungen, die eine bereits geprüfte Grenze berühren. Der Planner bindet dieses Kriterium an den *finalen* Commit. Umfang und unabhängiges Review bleiben unverändert.

## P5 – Projektbindung und lokaler Deployment-Input

**Befund:** `ledger/board.json`, Karte `t_6ba4a84a`, Run 24: widersprechende Boardangaben und ein vom Entwicklungseinstieg abgelehnter lokaler Input. **Entscheidung:** Vor Kartenfreigabe gleicht der Planner die Board- und Workspace-Einträge der lokalen `HERMES.md` mit der Kartenbindung ab, korrigiert abweichende Einträge selbst und protokolliert es auf der Karte. Setup und Planner-SOUL verleihen diese eng begrenzte Befugnis; der Coder erhält kein Schreibrecht dafür. Deployment-Dateien und Entwicklungscheckout trennen; bei gemeinsamem Checkout und abgelehntem lokalem Input in einem sauberen, abgetrennten Worktree am Kandidatencommit prüfen. Lokale Inputs weder entfernen noch umschreiben oder maskieren. Kein Umbau von `dev.sh` im MTB.

## P6 – Abnahmedemo und Zugang

**Befund:** `ledger/board.json`, Karte `t_83a3536e`: Die vorige gestoppte Demo belegte die festen Namen. Der Wechsel erforderte Eingriffe am Terminal; ein reproduzierbarer Login fehlte. **Entscheidung:** Höchstens eine ersetzbare Abnahmedemo, auf dem letzten unabhängig geprüften Commit. Zum Wechsel zuerst exklusives Eigentum nachweisen, nur diese Demo stilllegen und entfernen; fremde Ressourcen und Reviewbelege erhalten. Der Reviewer prüft die angegebenen Zugangsdaten am laufenden System.

Ein Team-Demopasswort für alle Demo-Benutzer. Kein Default, keine Auswahl pro Demo: vom Operator beim Anlegen geschützt erfragen und in alle drei SOULs rendern. Bei Altteams das fehlende Feld einmal erfragen; `confirmed_values.DEMO_PASSWORD` im privaten Setup-Datensatz ergänzen. Die Installation übernimmt den Wert erst nach erfolgreicher Zielprüfung; spätere Updates rendern daraus. Renderer-Vertrag und Freigabeliste mitändern. Der Wert gehört weder in Git noch in Hindsight, Karten oder Prüfberichte. Kein neues Passwortfenster bei Übergabe.

## P7 – Zwei Verben im MTB

**Entscheidung aus dem Demo-Block:** Nur `docker/demo/demo.sh` und dessen `README.md` im MTB ändern. `retire` prüft Container, Volume, Netzwerk, privates Runtime-Verzeichnis, exklusives Eigentum und Provenienz-Commit vor dem Entfernen und verifiziert danach die Abwesenheit. Nicht eindeutig eigene Ressourcen bleiben unangetastet. `user` legt den Demo-Benutzer an oder setzt sein Team-Demopasswort ohne zweite UID und ohne interaktives Prompt. Beide Verben mit Beispiel dokumentieren; keine SSH-Sitzung des Kunden erforderlich. Der Coder nutzt diese dokumentierten Verben oder das Projektäquivalent statt einzelner Löschbefehle. Keine Änderungen an Compose, Auswahl synthetischer Daten oder allgemeiner Demo-Erzeugungsanleitung.

## P8 – Wissen und Freigaben aus dem Maker

**Befund:** Der Verlauf auf dem Board und in den Rollouts zeigt, welche Arbeit bei einer Neuinstallation sonst neu erfunden werden müsste. Lokale Skill-, Memory- und Konfigurationsstände sind keine Quellen für die Umsetzung.

**Entscheidung:** Die belegten Lehren im jeweils geladenen Maker-Text verankern: begrenzte Abbruchregel und Demo-Lebenszyklus im Umgebungsskill; Produktionsbuild-Selektoren, portlose Testcontainers, Canary/Hash je Evidenzphase und Beobachterprobe in einer Maker-eigenen Referenz statt im Codex-Bundleskill. Beim Phasenrelease das Wake-Abo ans richtige Board und den unabhängigen Reviewer an seine Rolle binden; bei unterbrochenem Review den vorhandenen `reopen-review`-Weg mit Reviewprovenienz verwenden.

Setup und Update richten die benötigten Docker-Freigaben für Projektentwicklung und Demo ein und lesen sie zurück. Keine Selbstfreigaben: Bei zusätzlichem Bedarf blockiert die Rolle mit `needs_input`. Vor dem Ersetzen einer lokalen Abweichung an verwalteten Rollen-SOULs und Skills Datei und Version melden, dann den Maker-Stand liefern. Backup, Driftprüfung, Rückbau und fremdes Eigentum bleiben geschützt. Die lokale Skillpflege bleibt möglich; ihre Ergebnisse sind keine Voraussetzung für ein neues Team.

## Abnahme und Wirkungsgrenze

- Eine lokale Commitgruppe je Punkt; zwei Paketversionsquellen gemeinsam auf 2.14.0. Kein Push.
- Renderer-Vertrag und alle `references/test_*.py`; Setup, Altteam-Adoption und abweichende Bestände nur an künstlichen Zielbäumen prüfen. MTB-Verben an isolierten Ressourcen oder Test-Doubles prüfen, ohne die bestehende Demo anzutasten.
- Fujiko prüft die endgültige Fassung der geänderten SOUL-Vorlagen und Skills unabhängig auf CAC, semantische Doppelungen und Ladestellen.
- Nicht beauftragt: Teamprofile aktualisieren oder aufräumen, Dienste oder Sitzungen neu starten, den Umgebungsskill insgesamt umbauen oder Lauf 10 beginnen. Erst ein späterer Lauf kann Warteaufrufe (Ziel ≤ 3 je Run), Matrixzahl (Ziel: ein Vollauf), Threads, Reparaturrunden, Token und Demo-Login unter realen Bedingungen vergleichen.

## Belege und Umsetzungsnotizen (Review-Runde 1)

**Herkunft der Build-Evidence-Lehren.** Die drei Referenzen unter `skills/build-evidence/` tragen keine Archivzeiger mehr; ein frisches Team kann sie ohne Laufarchiv lesen. Die Belege bleiben hier:

- Produktionsbuild-Selektoren: `DIAGNOSE_Cypress-Spec-Lauf9_v1.0.0.md:24-27` (MUI-Quelle, null `data-testid`-Treffer in `frontend/src` bei `b6eea944`), `:56-57` (aus der Produktquelle abgeleiteter Selektor hielt), `:99-109` (Fixture ohne Login, Routing und API war Teil des Problems); Selektor-Fixture mit `NODE_ENV=production` in `codex/carter/rollout-2026-11-21T21-50-57-01a1ffe0-5e64-7af0-95fe-0b0439c1a42b.jsonl`.
- Portlose Testcontainer: Board `sg1`, Karte `t_83a3536e`, Kommentare #33 und #35 (feste Namen `mtb-demo_data`, `mtb-demo_default` und vier `mtb-demo-*-1`-Container blockierten einen Ersatz; der Port war frei, der zurückgehaltene Zustand nicht); `DIAGNOSE_Cypress-Spec-Lauf9_v1.0.0.md:28-30` (`docker/isolated/runtime.sh` verlangt genau einen Wegwerf-Patienten); `codex/carter/rollout-2026-11-21T21-28-06-01a1ffcb-7472-7c63-9c42-e3cb3442ebb0.jsonl` (Integrationstests brauchen Docker/Testcontainers und isolierte Testkonfiguration).
- JFR-Beobachter: `codex/carter/rollout-2026-11-21T21-28-06-01a1ffcb-7472-7c63-9c42-e3cb3442ebb0.jsonl` (JFR zeichnet Backend-Socket-I/O, Prozessstarts und Java-17-Connect-Prüfungen samt abgelehnter Verbindung auf; eine synthetische Loopback-Ablehnung beweist den Beobachter); `codex/daniel/rollout-2026-11-21T22-48-52-01a20015-63ac-79a2-99a4-50e061c8457f.jsonl` (Lauf-8-`startup-jfr-summary.log` als Beleg).

**N1 – Abweichung von P8, dokumentiert.** P8 nennt „begrenzte Abbruchregel und Demo-Lebenszyklus im Umgebungsskill". Der Demo-Lebenszyklus steht in `skills/dev-environment/SKILL.md`; die Abbruchregel steht in `coder.SOUL`, weil der Coder den Umgebungsskill laut Manifest nie lädt (Ziel ist nur der Planner). Die Regel erreicht damit ihren Leser; die Abweichung ist hier vermerkt.

**K3 – geprüfte Semantik.** Der native Matcher (`tools/approval_floors.py`) vergleicht exakten Kommandotext oder ein `fnmatch`-Glob gegen die ganze Zeile; eine Verbundzeile mit `;`, `&&`, `|`, Heredoc oder `$`-Expansion in doppelten Anführungszeichen matcht nie, und eine führende Variablenzuweisung verändert den Kommandotext gegenüber dem blanken Eintrag. Die realen Projektskripte wurden statisch gelesen: `docker/dev/dev.sh` kennt `check`, `test`, `test-selected`, `test-all`; `docker/demo/demo.sh` kennt `retire [SHA]`, `user`, `build SHA`, `start SHA`, `status`, `stop`; `user` liest `MTB_DEMO_PASSWORD` aus der Umgebung und nie aus einem Argument. Freigaben nennen deshalb exakte absolute Entrypoints und Verben, kein `docker compose *`, kein `env *`. `process_manage.wait` wird auf `TERMINAL_TIMEOUT` geklemmt; der Dispatcher hebt diesen Wert für Worker auf `max_runtime − 30 s` (bei 8h also rund 8h), deshalb fordert der Coder `timeout=14400` ausdrücklich an.

**W1 und W3.** `check` ist jetzt als Verb des Entwicklungsentrypoints definiert (`dev-environment`), sodass P4 für ein frisches Team auflösbar bleibt. Der Karten-Hängerschutz (`--max-runtime 8h`) steht nur noch in der Phasenrelease-Prozedur, also an der Stelle der tatsächlichen Kartenerzeugung; die Planner-SOUL verweist darauf, statt die Regel zu wiederholen.
