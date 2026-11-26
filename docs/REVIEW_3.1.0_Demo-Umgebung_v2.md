# REVIEW 3.1.0 — Optionale Demo, vollständige Docker-Freigabe (Runde 2)

**Gegenstand:** `docs/PLAN_3.1.0_Demo-Umgebung_v5.md`, SHA-256 `87b77b280fba97691e4901c76dd5e77ea3936e92994fc0bf91f05afeabdecff2`
**Vorlauf (Kriterium, nicht Gegenstand):** `docs/REVIEW_3.1.0_Demo-Umgebung_v1.md`, SHA-256 `95c4b8c4e9c2c7a6d3e1b7ffdc1288716f390444314a09f901b8d5d7a8b307b0`
**Basis:** Maker-Repo `generic-devteam`, HEAD `8add46c01a31dd3f149819fd29305c5d16fa05c8`; `git diff HEAD` = SHA-256 `e3b0c442…b855` (leer).
**Prüfumfang:** Plan v5, Review v1, getrackte Maker-Quellen/Instruktionen/Tests, `/home/mariko/projects/cac/SKILL.md` samt `cac-notation.md` und `cac-authoring-contract.md`. Keine Tests, kein Docker, keine Profile, keine Delegation, kein Kanban, keine Konfiguration, keine Änderung am Plan.

## 0 Urteil

APPROVED. Alle dreizehn Vorprüfpunkte sind erledigt: K1 löst den Selbstwiderspruch, indem die `*`-Regel auf Skript-Einträge begrenzt und die vier Docker-Grants separat eingeführt werden; K2 verortet Laden, Verfahren und Stopp vor Schritt 6 und jedem Ticket; W1 ersetzt den gestrichenen Release-Sperrhinweis durch denselben Stopp plus Anti-Bypass-Satz in der Referenz. Die Umsetzung kann v5 allein folgen: 20 eindeutige ALT-Blöcke, neun geänderte Dateien plus eine neue Referenz, alle betroffenen Testpins benannt, Versions- und Autorisierungsklausel vorhanden. Zwei wichtige, nicht blockierende Restpunkte bleiben: das Coder-Bereitschaftskriterium aus `dev-environment:50` wird ersatzlos gestrichen, und das Abräumverfahren nennt nur noch „project commands" statt des dokumentierten Teardown-Verbs; beides ist mit einer Zeile behebbar und ändert keine der von Max entschiedenen Regeln. Die vier geringen Punkte sind Präzisierungen ohne Einfluss auf die Umsetzbarkeit.

## 1 Altbefunde

| ID | Status | Beleg (Plan / Maker) |
|---|---|---|
| K1 | erledigt | plan:226 begrenzt `*` ausdrücklich auf „For script entries" und führt die Docker-Grants mit „Independently" ein; plan:237 listet `docker`, `docker *`, `docker-compose`, `docker-compose *`; ALT `setup.md:136` entfällt. Kein Widerspruch mehr im selben Absatz. |
| K2 | erledigt | plan:24–26: Annahme → Ja-Zweig lädt `skill_view(name="dev-environment", file_path="references/requested-demo.md")` und räumt vor Schritt 6 bzw. jedem Ticket ab; Stopp bei fehlender Feststellung. plan:117–124: Eigentum, Abwesenheit, Entfernen, Nachprüfung, Stopp, kein Vorab-Fix. plan:126: Rücklesen vor Tickets, kein Kartenprotokoll. `planner:45` bleibt der bedingte Dev-Aufruf; der neue Aufruf ist ein anderer String, `test_render_reasoning.py:111,120` bleiben gültig. |
| W1 | erledigt | plan:50–58 streicht `kanban-phase-release.md:21` ersatzlos; Failure-Exit jetzt plan:25 („stop the entire plan") und plan:123 („stop before committing the plan or writing any ticket"). Anti-Bypass-Satz plan:123. Kein Test pinnt die alte Klausel (`git grep` auf „circular"/„keep the release blocked": nur Quelle, kein Test). |
| W2 | erledigt | plan:226 offenbart „any daemon accessible to the CLI, including an alternate context or remote daemon", „not project-scoped", „can affect other workloads"; Ablage ist der Abschnitt „Setup targets and readbacks" (`setup-record.md:36–38`, in plan:273 zitiert). Rest: kein eigenes Feld (N4). |
| W3 | erledigt | plan:4 nennt die PATCH-Begründung („Korrektur bestehender Maker-Rollen und Setup-/Update-Rezepte …, kein neues Produkt, Kommando, Renderfeld oder Skill") und verlangt ausdrückliche Freigabe „einschließlich Planner- und Reviewer-Template"; Live-Rollout separat. Deckt `AGENTS.md:5–6` und `AGENTS.md:12`. |
| W4 | erledigt | plan:68 (`reviewer.SOUL.md.template:86` NEU) enthält nur die funktionale Endprüfung: läuft am Review-Commit, Login funktioniert mit `{{DEMO_PASSWORD}}`, zugesagte Funktion mit den erfassten Daten, „Container uptime alone is not a functional check". „At most one"/„Replacing/retiring" entfällt. |
| W5 | erledigt | plan:181 (`upstream-sources.md:30` NEU) ohne „retire the previous runtime"; beschreibt genau den Zustand nach den `demo-handover`-Edits (plan:137–160). |
| M1 | erledigt | plan:226 „in all three profiles" ersetzt durch „Planner, Coder and Reviewer profiles"; `setup-record.md:26` bindet genau diese drei Allowlist-Profile, `team-codex` hat keine Allowlist (`setup-record.md:25`). |
| M2 | erledigt | plan:259 (`update.md:87` NEU) erklärt eine Baseline ohne erforderliche Docker-Einträge, auch eine verifizierte 3.1.0, für obsolet; plan:270 (`update.md:93` NEU) verweist auf die vier Einträge; plan:282 (§4.6) prüft Migration der 3.1.0-Diagnoseeinträge, aktuellen Baseline-Abgleich ohne Diff sowie `docker ps`, `docker volume ls`, `docker network ls`, `docker inspect`. Widerspruch und Listing-Lücke geschlossen. |
| M3 | erledigt | plan:226/237 gewähren bare `docker` und `docker-compose` zusätzlich zu den Wildcards; plan:282 testet beide nackten Aufrufe. |
| M4 | erledigt | Plan deutsch für Max (Adressat), alle NEU-Blöcke in technischem Englisch; entspricht der CAC-Zielgruppenregel (`cac-authoring-contract.md`, Absatz „audience rule"). |
| M5 | erledigt | plan:81 (`dev-environment:39` NEU) entfernt das feste Skript und die Verb-Beispiele; „one verb per operation with the exact invocation the project uses" bleibt. Kein Test pinnt das entfernte Beispiel (`git grep` „one script with one verb": nur Quelle). |
| §6.5 | erledigt | plan:148 (`demo-handover:20` NEU) ergänzt „If build or start refuses existing state, stop and report the refusal; do not purge, rename or bypass it." Der Coder-Pfad hat den Zweig jetzt selbst. |
| §6.6 | erledigt | plan:24–26 und plan:117–124 verlangen Nachprüfung vor Commit und Tickets; plan:126 verneint Karten-Evidenz; plan:281 §4.5(d) fordert null Tickets/keinen Commit bei unbekanntem Status, unklarer Zugehörigkeit oder Fehlschlag. |

## 2 Neue materielle Befunde

| ID | Schwere | Befund | Beleg | Wirkung / Empfehlung |
|---|---|---|---|---|
| N1 | wichtig | Das Coder-seitige Bereitschaftskriterium entfällt ersatzlos. | ALT `dev-environment:50` („Judge readiness from the project's status and version output, not from container uptime. A started container is not a working demo.") wird nach plan:96–101 ersetzt; der Pin `test_build_evidence.py:144` wird nach plan:280 ersetzt; `demo-handover:20` NEU (plan:148) hat nur die Startverweigerung; `reviewer:86` NEU (plan:68) hat nur die Review-Sicht („Container uptime alone is not a functional check"). | Ein Coder kann eine gestartete, aber nicht bedienbare Runtime übergeben; der Reviewer fängt es, kostet aber eine Runde. Empfehlung: den Satz einzeilig in `demo-handover:20` mitführen oder im Plan ausdrücklich festhalten, dass allein die Reviewer-Prüfung das Gate ist. |
| N2 | wichtig | Das Abräumverfahren verliert die Verb-Spezifität und das Verbot handkomponierter Entfernung. | plan:121 sagt nur „Retire it with project commands and verify those resources are gone."; gestrichen sind `planner:74` („Use the project's documented teardown verb (`demo.sh retire` or equivalent); never compose … yourself — an unattended guard refuses it.", plan:32) und `demo-handover:19` (plan:133). `planner:12` verlangt zwar die Guide-Lektüre, was „project commands" auflösbar macht. | Mit `docker *` greift der alte Guard ohnehin nicht mehr; die prozedurale Präferenz ist aber keine Berechtigungsfrage. Empfehlung: in der Referenz „the project's documented teardown verb" statt „project commands" schreiben. |
| N3 | gering | „Record their answer" hat keinen Ort. | plan:24. | Im Nein-Zweig könnte eine Plan- oder Kartennotiz entstehen, obwohl Max dort „kein Ticket, whatever" und keinen Demo-Nachweis will. Empfehlung: „record in the conversation" oder auf den Ja-Zweig begrenzen. |
| N4 | gering | Die Reichweiten-Offenlegung hat im Setup-Record kein eigenes Feld. | plan:226 nennt den Abschnitt; `setup-record.md:36–38` beschreibt nur Identität/Pfade/Hashes/Modus/Readback, die Bullets 40–52 enthalten keine Zeile für Grant-Reichweite; `setup-record.md` wird nicht editiert. | Die Offenlegung kann stillschweigend ausbleiben. Empfehlung: eine Bullet-Zeile in `templates/setup-record.md:40–52`. |
| N5 | gering | §4.4 benennt den Legacy-Zeilen-Pin nicht. | `test_build_evidence.py:102` pinnt `` `docker compose *` `` in der `update.md:93`-Zeile; die Zeile wird nach plan:270 umgeschrieben. plan:280 nennt „Verbots-, Teardown- und Listing-Tail-Assertions", nicht diesen Pin. | Der Test bricht nach der Edit, wird von §4.7 gefunden, also nicht still. Empfehlung: den Pin in §4.4 ausdrücklich nennen. |
| N6 | gering | „(including `docker compose *`)" ist mehrdeutig. | plan:226 gegen plan:270 („the four Docker entries"). | Ein Operator könnte eine fünfte, redundante Zeile anlegen (harmlos). Empfehlung: „`docker *`, which covers `docker compose *`". |

## 3 Verifizierte Anker

| Anker | Prüfung | Ergebnis |
|---|---|---|
| Fingerprints | `sha256sum` Plan, Review; `git rev-parse HEAD`; `git diff HEAD \| sha256sum` | Alle vier stimmen mit der Vorgabe überein; Arbeitsbaum bis auf untracked Pläne/Reviews leer. |
| 20 ALT-Blöcke | `git grep -F` je Blocktext gegen die genannte Datei | Jeder Block genau ein Treffer in der genannten Datei (Testdatei-Treffer sind erwartete Pins, nicht Quelle). |
| Zeilennummern | Plan-Überschriften gegen Datei | `planner:64,74,75`; `kanban-phase-release:21`; `reviewer:86`; `dev-environment:39,44–50,59`; `demo-handover:18–19,20,21`; `upstream-sources:28,30`; `manifest:70,256–259`; `setup:136,141,145`; `update:87,93` — alle korrekt. |
| `test_render_reasoning.py` | 109–120: Trigger `skill_view(name="dev-environment")` in 111, Karten-Pin 117; 140–168: Lifecycle 144–151, Planner-Pins 154–158, `demo.sh user` 160, Reviewer-Login 163, Platzhalter 166–168; 306 `assertNotIn` Coder; 319–320 Coder 8422 B/70 Zeilen | Pins bestätigt; 306 und 319–320 bleiben unberührt (Coder-SOUL unverändert), die übrigen sind in §4.2 benannt. |
| `test_update_team.py` | 487–503: Reviewer-Lifecycle 491, zwei `demo.sh`-Pins 498/499, Reviewer-Login 502; 770–788: exakte Quellmenge 773, keine Kopie 779–780; 790–827: Hauptdatei 796, `retained_additions` 826 | Pins bestätigt; „beide `demo.sh`-Pins invertieren" (plan:278) trifft genau 498/499. |
| `test_dev_environment.py` | 25–45: Transport 32, Inventar 33–35, `local_links` 45; 97: kein „demonstration" im Acceptance-Abschnitt | Bestätigt; 35 fordert nach der Edit `{"SKILL.md","references"}`, 33 die zweite Datei — von plan:279 (25–45) gedeckt. Die NEU-Formulierung in plan:111 sagt „demo", 97 bleibt grün. |
| `test_build_evidence.py` | 82–109: Verbot 92, Legacy-Zeile 100–102, `assertNotIn('"docker *"')` 107; 137–155: Lifecycle 140–147, Tail-Split 151–155 | 82–109/137–155 in §4.4 benannt; 107 bleibt wegen der Escape-Schreibweise (`\"docker *\"`) grün, 152 wirft nach der Edit `IndexError` — plan:280 nennt den Split ausdrücklich. |
| `manifest.json` | 70 exakt (4 Leerzeichen), 256–259 Block | Je genau ein Treffer; Einfügen nach 70 hält die Sortierung. |
| Transport tatsächlich | `update_team.py:313–326` | Der Updater liefert per `git ls-tree -r` unter `skills/<name>/`, nicht über `manifest.transport`; die neue Referenz wird also ausgeliefert, `files` und `transport` sind testgepinnt. Kein vierter Verbraucher. |
| Readback/Ort | `setup.md:142,147`; `setup-record.md:36–38` | `config get command_allowlist` / Baseline-Speicherung und Berichtsabschnitt existieren wie in plan:273 zitiert. |
| Grant-Mechanik | plan:226/237 gegen Review-1-Befund (fnmatch) | `docker *` deckt `docker compose …`; bare `docker` und `docker-compose` sind separat gewährt; zusammengesetzte Zeilen bleiben gegated; §4.6 testet alle acht Entscheidungen. |

## 4 Grenzen

| Grenze | Bedeutung |
|---|---|
| Keine Laufzeitprüfung | Kein Docker, keine Profile, keine Tests ausgeführt. Ja/Nein-Gate, Abräumen und Funktionsprüfung sind Textverträge; plan:281 verlangt selbst die getrennte Berichterstattung von Textvertrag und Laufverhalten. |
| Kein dauerhafter Abräum-Nachweis | plan:126 legt bewusst fest, dass das Rücklesen vor den Tickets geschieht und nicht auf einer Karte protokolliert wird. Einzige Evidenz sind Planner-Lauf und User; das folgt Max' Entscheidung, ist aber nicht revisionsfest. |
| Ja-Zweig setzt Demo-Werkzeuge voraus | Die alte Bedingung „When the project has a demonstration runtime" (`planner:75` ALT, plan:43) entfällt; die Referenz wertet „verified absence" als Abschluss (plan:119). Ein Demo-Wunsch in einem Projekt ohne Demo-Kommandos führt zu einer Karte, deren Coder-Skill einen Demo-Entrypoint voraussetzt. Max' Ablauf unterstellt diese Fähigkeit; für 3.1.1 nicht gelöst. |
| Reichweite von `docker *` | Alle Daemons/Kontexte, in plan:226 offengelegt. Dass Hardline und `approvals.deny` vorrangig bleiben, stammt aus Review 1 und wurde hier nicht erneut geprüft (Hermes-Quellen außerhalb des Leserasters). |
| Sprache | Plan deutsch, operative Texte englisch. Die Englischpflicht aus `HERMES.md` wird für das Max-Dokument bewusst nicht angewandt (CAC-Zielgruppenregel). |
| Leseraster | Keine Pläne v1–v4, keine weiteren `docs/`, keine Live-Profile, keine Historie, keine Secrets. |

*Geschrieben: `/home/mariko/projects/generic-devteam/docs/REVIEW_3.1.0_Demo-Umgebung_v2.md`*
