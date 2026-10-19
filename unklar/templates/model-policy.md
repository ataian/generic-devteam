# Bestätigte Modell- und Risikopolicy

Beim Zielsetup ausfüllen und je Rollenhome als `devteam/model-policy.md`
schreiben; lokal über MODEL_POLICY_REF erreichbar. Nichtgeheime Daten, keine
Zugangsdateien/Tokenwerte. Jede Rolle erhält dieselbe bestätigte Policyrevision.
„Offen“ ist kein erlaubter Fallback und blockiert die betroffene Fähigkeit.

- Policyrevision / Datum / bestätigender Nutzer / Freigabequelle: offen
- Hermes-/Codex-Zielversion und relevante native Leser: offen

## Tatsächliche Auswahl und Zugang

| Verbraucher | Provider / Modell-ID | Reasoning / Unterstützung | Nativer Configpfad und Auswahlweg | Effektive Overrides | Zugriff / echter Call / Beleg |
|---|---|---|---|---|---|
| Planner | offen | high empfohlen, Unterstützung prüfen | offen | offen | offen |
| Coder | offen | medium empfohlen, Unterstützung prüfen | offen | offen | offen |
| Reviewer | offen | medium empfohlen, Unterstützung prüfen | offen | offen | offen |
| Team-Codex | offen | Nutzerwahl | CODEX_HOME/config.toml, tatsächlich aufgelöst: offen | offen | offen |
| Hilfsmodelle / Analysepfade | benötigte Pfade einzeln aufführen | offen | offen | offen | offen |

Ein geeigneter Anbieter genügt; getrennte Hermes-/Codex-/Hilfsmodellzugänge
nachweisen. Nicht benötigte Hilfswege als „nicht benötigt, weil …“ begründen.
SOULs enthalten keine konkreten Pins. Policy ist kein technischer Enforcementlayer;
Config und echter Worker bestimmen die tatsächlich verwendete Route.

Team-Codex-Aufrufbindung: ausschließlich dieser Prozess erhält das bestätigte
HOME und CODEX_HOME sowie `PONYTAIL_DEFAULT_MODE=full`; Hermes-HOME bleibt erhalten.
Effektive Binary, PATH, Original-Ponytail-Hookdatenroot und injiziertes `full` in
neuem Prozess/Resume/Child: offen. Coder/Hermes separat: Originaldefaultresolver
(Env, Userconfig, eingebautes full), wirksame Auswahl und neuer Prozessbeleg: offen.
Gemeinsame abweichende Userdefaults werden nicht still für andere Profile geändert.

Feste Team-Codex-Auftragsregel für den Coder: Übergib `$caveman` ausdrücklich in
jedem neuen Auftrag, auch nach Neustart/Resume. Der Zusatz gehört wörtlich in den
Auftragstext, nicht als zu expandierende Shellvariable in die Prozessumgebung.
Die installierte Skillkopie allein und eine frühere Aktivierung genügen nicht.
Nur Chat wird verkürzt; Code, Dokumentation, Commits, Memory und Sicherheitsklarheit
bleiben normal verständlich. Geladener Originalskill und tatsächliche Aktivierung
im neuen Team-Codex-Kontext sind separat als B01 nachzuweisen: offen.

## Gewählte Codeanalyse

Beim Setup genau einen Zweig bestätigen und den anderen entfernen; dieser
Abschnitt muss in allen drei Rollenpolicies dieselbe Auswahl tragen.

- Auswahl / Originalrevision / Runtime / Discoverybelege je Rolle und Team-Codex: offen
- Absolute Corpus-/Repositoryroots, Output-CWD, Ausschlüsse und Updateweg: offen
- Letzter erfolgreicher Indexstand / gespeicherte Revision bzw. zugeordnete
  Dateihashes / relevanter Arbeitsbaum / offene Coverage: offen
- CBM nur bei Auswahl: G2/A01-CBM-Originaloutput-/Bytevergleich, gemeinsame
  Cache-/Daemonbindung und tatsächliche MCP-Workspace-/Hooknachweise: offen

Feste Ladepflicht vor jeder Analyse, auch in neuen Sitzungen und nach Resume:
Hermes lädt den installierten Originalskill des gewählten Wegs und die benötigten
Originalreferenzen. Coder übergibt den passenden ausdrücklichen Skillaufruf in
jedem Team-Codex-Analyseauftrag, nicht als Shellvariable.

- Bei Graphify: Hermes `skill_view(name="graphify")`, Team-Codex `$graphify`;
  `references/query.md` für vorhandenen Graph, `references/update.md` für
  Änderungen, `references/github-and-merge.md` für mehrere Repos laden.
- Bei CBM: Hermes `skill_view(name="codebase-memory")`, Team-Codex
  `$codebase-memory`; zuerst `list_projects`/`index_status` mit echter Rootbindung,
  bei Änderungen erfolgreiche native Indexaktualisierung vor der Relationsquery.

Vor relevanten Queries Corpus und Arbeitsbaum gegen den letzten erfolgreichen
Indexstand prüfen; Änderungen zuerst über den gewählten Originalweg nachführen.
Fehlende/stale/teilweise Indizes offenlegen, keinen Erfolg aus Dateiexistenz oder
Zeitstempel ableiten. Bei Fehlern anhalten, nicht still den Analyseweg wechseln.
Installation ist keine Produktanalysefreigabe; Produktanalyse braucht Projektauftrag.

## Erlaubte höhere Stufen

| Rolle / Anlass | Freigegebene Modell-/Reasoningroute | Konkreter nativer Wechselweg | Verfügbarkeitsbeleg | Nutzerfreigabe / Grenze |
|---|---|---|---|---|
| Coder: hohe Komplexität oder hohe Fehlerfolgen | offen | offen | offen | offen |
| Coder: beides, stärkstes freigegebenes Codingmodell erwägen | offen | offen | offen | offen |
| Reviewer: Sicherheit/Rechte, Datenverlust/Migration, Parallelität/Transaktionen, zentrale Invarianten, weitreichende Verträge/Architektur | offen | offen | offen | offen |

Architektur-/Spezifikationswidersprüche gehen zum Planner statt in autonomes
Redesign. Kritische Funde verlangen erneute unabhängige Prüfung. Fehlende
notwendige technische Route offenlegen, nicht nur erhöhte Prüftiefe behaupten.
Temporäre Providerüberlastung ändert weder Modell noch Provider; G1 separat prüfen.

## Original-TOMLs — separat vom Elternmodell

Originalrevision und vollständige Dateihashes im Setuprecord; unveränderte Pins
hier nach Bezug eintragen. Kein Umschreiben auf eine bequemere Elternauswahl.

| Originalname | Original-Modell / Reasoning | Parentprovider / Konflikte | Discovery / echter Delegationscall / Beleg |
|---|---|---|---|
| test-automator | offen | offen | offen |
| security-auditor | offen | offen | offen |
| reviewer | offen | offen | offen |
| anti-ui-slop-reviewer | offen | offen | offen |
| ui-fixer | offen | offen | offen |
| docker-expert | offen | offen | offen |

## Änderung und Rücklese

Neue Auswahl nur im genehmigten Scope nativ konfigurieren, rücklesen, im echten
Kontext prüfen und Policyrevision in allen Rollen aktualisieren. Ursprünglichen
nichtgeheimen Zustand geschützt erhalten. Kein automatischer Anbieterwechsel,
Credentialtransfer oder gemeinsame Profiländerung durch diese Datei.
