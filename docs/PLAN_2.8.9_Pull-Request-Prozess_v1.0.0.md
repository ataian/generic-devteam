# PLAN — Pull-Request-Prozess für das Devteam

| Feld | Wert |
|---|---|
| Appversion (Ausgangsversion) | Maker **2.8.9** |
| Dokumentversion | v1.0.0 |
| Datum | 2026-11-14 |
| Charakter | Vorbereitung. Dieser Plan wird **nicht** umgesetzt, bevor die offenen Fragen unten geklärt sind. |
| Vorgänger | `PLAN_2.8.8_Prozessschritte_v1.0.0.md` — dessen Punkte 2.2, 2.3, 2.10 wandern hierher; der Rest ist in 2.8.9 umgesetzt. |

## 1. Warum ein eigener Plan

Der Maker-Prozess endet heute nach dem Review mit DONE. Der geprüfte Commit liegt lokal, es gibt keinen Push, keinen Pull Request und keinen Pipeline-Lauf. Der Planner meldet den Abschluss im Kanal und schreibt ausdrücklich „publication needs separate authorization" — danach passiert nichts.

Dieser Plan beschreibt, wie aus „done" ein „geprüft und zur Übernahme vorgelegt" wird. Er berührt Berechtigungen (Push, Werkzeugzugang) und ist deshalb von den reinen Textänderungen getrennt.

## 2. Befunde aus Lauf 3, die diesen Plan tragen

- Die Karte `t_d3894cd4` hat `branch_name = NULL`; gearbeitet wurde auf einem langlebigen Branch. In Repos mit geschütztem `develop` wäre ein Push ohnehin nicht möglich.
- Der Commit `4f06947a` ist lokal; niemand außerhalb der Maschine kann ihn sehen.
- Das Repo hat neun GitHub-Actions-Workflows (`test-e2e.yml`, `check-format-backend.yml`, `check-format-frontend.yml`, `version-compare.yml`, `config-compare-keys.yml`, `config-generate-files-and-keys.yml`, `docker-build-image.yml`, `docker-build-push-images.yml`, `deploy-dev.yml`). Für diesen Commit lief keiner.
- Der Coder erhält beim APPROVE keine Rückmeldung; nur der Planner sieht das DONE-Ereignis.
- `gh` ist auf dem Host nicht installiert.

## 3. Vorgesehene Schritte (Entwurf, nicht umgesetzt)

### P1 — Branch verbindlich machen

Bereits in 2.8.9 angelegt: Der Planner fragt bei der Planbesprechung nach Branchname und Startpunkt, der Coder legt den Branch an. **Offen ist die Konvention:** `feature/<ticket>` und `hotfix/<ticket>` als Pflicht, und was passiert, wenn der Kunde keinen Namen nennt.

### P2 — Pull Request durch den Planner

- Der Planner stellt den PR nach dem DONE-Ereignis, als Teil seines Abschlussberichts.
- Der PR-Body trägt: Karte, geprüften Commit, Reviewurteil, Prüfzahlen, mitgeführte Grenzen.
- Kein Merge, kein Deploy, kein Force-Push. Der Merge bleibt beim Menschen.

### P3 — Pipeline-Ergebnis rücklesen

Nach dem Push liest der Planner oder der Coder den Status der Prüf-Workflows und hängt ihn an die Karte. Bei rot: Rückweg an den Coder, ohne neue Freigabe.

### P4 — Abschlussbericht um besondere Meldungen erweitern

Der Bericht nennt zusätzlich, was über den Plan hinaus geschah: selbst gefundene Lücken, getroffene Entscheidungen, gemeldete Testlücken, mitgeführte Grenzen. Nichts, was der Plan ohnehin vorsah.

### P5 — Werkzeuge

`gh` installieren oder die REST-API nutzen. Entscheidung offen.

### P6 — Jira (später, eigener Schritt)

Ticket- und Dokumentationsverwaltung wandert später nach Jira. Der Kanban-Board bleibt, was er ist: der Ablauf von Coder und Reviewer. Keine Vermischung.

## 4. Offene Entscheidungen

1. **Wer pusht:** Planner (hat das DONE-Ereignis und schreibt den Bericht) oder Coder (kennt den Branch)? Empfehlung: Planner, weil er den Abschluss ohnehin verantwortet.
2. **Welches Credential:** eigener Bot-Account mit Schreibrecht auf einen Fork, oder ein Deploy-Key am Team-Profil? Push auf `develop` ist in einigen Projekten durch Branch-Protection gesperrt — der PR-Weg ist also ohnehin der einzige.
3. **`gh` oder API:** `gh` ist einfacher zu prüfen und zu protokollieren; API spart eine Installation.
4. **Welche Workflows dürfen laufen:** nur die Prüf-Workflows, oder auch die Build-Workflows? `deploy-dev.yml` bleibt außen vor, das ist die Docker-Dev-Umgebung des Teams.
5. **Rückweg bei roter Pipeline:** direkt an den Coder (ohne neue Karte) oder über den Planner?
6. **Was passiert mit dem Branch nach dem Merge:** löschen oder behalten? Heute schreibt 2.8.9 nur „nach dem Urteil aufräumen" — bei PR-Nutzung wäre der Branch bis zum Merge nötig.

## 5. Abnahmekriterien

1. Ein Lauf endet mit einem PR-Objekt, das Karte, Commit und Urteil verlinkt.
2. Der Push erfolgt ausschließlich nach APPROVE und ausschließlich auf den Ticket-Branch.
3. Die Pipeline läuft und ihr Ergebnis hängt an der Karte.
4. Kein Merge, kein Deploy, kein Force-Push durch einen Agenten.
5. Der Abschlussbericht nennt besondere Meldungen und getrennt die noch offene Übernahme.

## 6. Was dieser Plan nicht behebt

- Er ersetzt keine menschliche Abnahme im laufenden System.
- Er löst nicht das Problem fehlender Tests: das adressiert 2.11 (Invarianten) und 2.12 (Quellen- gegen Ausführungsnachweis) in 2.8.9.
- Er macht die Maker-Regeln nicht wirksam, solange Push-Recht und Werkzeugzugang fehlen.
