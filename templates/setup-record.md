# Privates Zielsetup-Protokoll

Vorlage; erst beim beauftragten Zielsetup ausfüllen. Ziel ist ausschließlich
`<tatsächlich aufgelöster Plannerhome>/devteam/setup.md`, Besitzerverzeichnis 0700,
Datei 0600, außerhalb Projekt/Git/Export. Keine Token-/Passwort-/Authinhalte,
keine unbereinigten Configdumps. Secretort und Prüfstatus genügen.
Dieses Protokoll dokumentiert; native Profile, Board und Dienstobjekte bleiben
Zustandsautorität. Bei Wiederaufnahme erneut lesen, nicht blind Create wiederholen.

## Projekt und Objektidentität

- Setupzuordnung / Paketversion / Quellenrevision / Datum: offen
- Projektname / absoluter Workspace: offen
- Repositorygrenzen (Workspace selbst muss kein Git-Root sein): offen
- Je Repository: Root- und Bereichs-AGENTS, Manifest/Lockfile/Wrapper, bestehende Änderungen: offen
- Boardkennung / nativer Rücklesebeleg / Standardworkspace: offen
- Projektbank / vorhandener Hindsight-Dienst / Eigentumsbeleg: offen
- Codeanalyse (genau eine) / Rezeptrevision / Funktionsprüfung: offen

## Rollen

| Funktion | Technische Kennung | Anzeigename | Tatsächlicher Profilhome | Eigentums-/Kollisionsprüfung | SOUL-Annahme / vollständige effektive Aufnahme |
|---|---|---|---|---|---|
| planner | offen | offen | offen | offen | offen |
| coder | offen | offen | offen | offen | offen |
| reviewer | offen | offen | offen | offen | offen |

## Bestätigte Render-Rohwerte und Wiederaufnahme

Keine Persona-Abfrage; rollenfeste Texte nicht ergänzen. Jeden Rohwert im folgenden
einzigen JSON-Block speichern, nicht seine Markdownmaskierung. Mit `json.dumps`
gemäß [Setupweg](../references/setup.md) befüllen und mit `json.loads` rücklesen;
Tabellen sind Belegübersichten, keine verlustfreie Datenquelle. Bei Resume wiederverwenden,
nur fehlende Werte oder Drift klären; native Objekte bleiben Zustandsautorität.
`confirmed_values` enthält Namen, Projekt, Bank, Board, technische Profil-IDs,
die vier Reasoning-Renderwerte sowie feste Planner-/Hermes-Coder-Stufen und die
bereits bestätigte Codex-ID nur für die technische Konfiguration; `confirmed_bindings`
enthält die bestätigten Bindungsrohdaten. Leere Objekte bedeuten noch nicht erfasst.

```json
{
  "confirmed_values": {},
  "confirmed_bindings": {}
}
```

| Feld | Bestätigter Rohwert | Annahme / native Rücklese / Driftprüfung |
|---|---|---|
| PLANER_NAME | offen | offen |
| CODER_NAME | offen | offen |
| REVIEWER_NAME | offen | offen |
| PROJECT_NAME | offen | offen |
| HINDSIGHT_BANK_NAME | offen | offen |
| KANBAN_BOARD_NAME = BOARD (Kennung, nicht Anzeigetitel) | offen | offen |
| PLANNER_PROFILE | offen | offen |
| CODER_PROFILE | offen | offen |
| REVIEWER_PROFILE | offen | offen |
| CODEX_MODEL (bereits bestätigte Codex-ID) | offen | offen |
| PLANNER_REASONING (feste native Stufe, kein Rollenfeld) | offen | offen |
| CODER_REASONING (feste Hermes-Stufe, kein Rollenfeld) | offen | offen |
| CODEX_REASONING_DEFAULT | offen | offen |
| CODEX_REASONING_MAX (erlaubte Obergrenze) | offen | offen |
| ROLE_REASONING_DEFAULT (Reviewer) | offen | offen |
| ROLE_REASONING_HIGH (höchste erlaubte Reviewer-Prüfstufe) | offen | offen |

- Zielkonto-Home / unabhängig vom Projektnamen bestätigter kanonischer absoluter Workspace / Abgleich mit Projektkontext und nativen Profil-/Boardbindungen oder offene Klärung: offen
- ROLE_NAME je Rolle aus PLANER_NAME / CODER_NAME / REVIEWER_NAME: offen
- Je Rolle: Vorlagenrevision/Hash, deklarierte und tatsächlich vorkommende Felder, gerenderter Solltext/Hash, exaktes SOUL.md-Ziel, Annahme und bytegenaue Rücklese: offen

## Native Zuständigkeit und Freigaben

- Hermesrevision / Resolver / Terminalbackend: offen
- Gateway-/Multi-Profile-Owner / bedienter Planneradapter: offen
- Dispatcher-/Notifierbesitzer, Configquelle / tatsächlicher Workerpfad: offen
- PM-Bestand / gemeinsame Generation / konkrete Aufnahmewirkung: offen
- Freigegebene Installationen / Bootstrap-/PM-/Aktivierungswirkung: offen
- Dienst-/Modell-/Nachrichten-/Testfreigabe und begrenzter Umfang: offen
- Erhaltene Schutz-/Freigabeeinstellungen und betroffene gemeinsame Bestände: offen
- Tatsächliche Timeout-/Retry-/Rate-Limit-Behandlung, Grenzen / Zielrevision / offene Probleme: noch ungeprüft

## Modelle und Codex

- Je Rolle: Provider, Modell, Reasoning, native Configquelle, Overrides, echter Call: offen
- Unterstützte Stufen je Modell/Provider und Rangfolge / ausdrücklich bestätigte Grenzen / Standard nicht über Obergrenze / nativer Wechselweg und Beleg: offen
- Helferpins und gegebenenfalls abweichende Stufensemantik / bestätigte Zuordnung zur Grenze / Konflikte vor Nutzung geklärt: offen
- Hilfsmodell-/Analysewege und Zugang separat: offen
- Team-Codex Prozess-HOME / CODEX_HOME / aufgelöste Binary: offen
- PFLICHT Team-Codex Git-Identität: bestätigter user.name / user.email, Herkunft und Übernahmefreigabe / reguläre CODEX_PROCESS_HOME/.gitconfig, Modus 0600 / Vorzustand und Rückweg: offen
- PFLICHT Git-Nachweis: --show-origin aus Team-.gitconfig, GIT_AUTHOR_IDENT und GIT_COMMITTER_IDENT in frischen Workerprozessen ohne Identitäts-Envhilfen; Testrepo ohne lokale Identität und vorgesehener Repo-Kontext / Autor und Committer am Probelaufcommit: noch ungeprüft
- Effektive Skill-/Plugin-/Agent-/Configroots; Projekt-/Admin-/Systemquellen: offen
- Projekttool-PATH/Caches im echten Worker nach HOME-Wechsel: offen
- Regulärer Codexlogin / separater Hermeszugang / Secretort, nie Inhalte: offen

## Planner-Kommunikation und Memory

- Server / eigene Botidentität / Team- und Projektkanalmitgliedschaft: offen
- Menschliche User-ID und Zulassung, kein Allow-all: offen
- Projektkanal-ID / Typ (öffentlich channel, privat group): offen
- Getrennte DM-Kanal-ID / Typ / tatsächliche Teilnehmer / Home-Rücklese: offen
- Effektive Allowlist / Free-Response / Mention / normale Antwortkonfiguration: offen
- Native Subscriptionidentität: Board, Task, Kanal, Typ, Mensch, Planner, wake, leere Thread-ID: offen
- Erwähnungsantwort / Antwort ohne Erwähnung / DM / veröffentlichter Planner-Wake: offen
- Pro Rolle: Hindsight-JSON-Ort / Originaladapterrevision / SDK-/Serververträglichkeit: offen
- Recall-/Retain-/Reflect-Requestfelder und gespeicherte Tags / zwei Turns / Konsolidierung: offen
- Reflect-Freigabe erst nach Rollenfilterweitergabe, sonst gefilterter Recall: offen

## Bezogene Komponenten und eigene Ausgaben

| Bestandteil / Rolle / Harness | Originalrepo und Unterpfad | Revision / Release / Lizenz | Vollständige Dateimenge / Hashbeleg | Tatsächliches Ziel / eigene Identität | Discovery / Modus / Funktionsbeleg |
|---|---|---|---|---|---|
| aus Manifest einzeln aufführen | offen | offen | offen | offen | offen |

Alle sechs VoltAgent-Original-TOMLs einzeln: Originalpfad, Hash, Modell-/Reasoningpin,
Discovery, tatsächlicher Delegationscall. Konfigurationsnachweis, Originalidentität
und Runtimebeleg bleiben getrennt. Bei CBM zusätzlich die vom offiziellen Installer
bereitgestellten Codex-Unteragenten und ihre Discovery dokumentieren.

| Repository / Fähigkeit | Quellmanifest / Constraint | Aufruf-CWD / Wrapper / Lockfile | Tatsächliche Toolauflösung | Prüfstatus / Beleg |
|---|---|---|---|---|
| vom Zielprojekt abgeleitet | offen | offen | offen | offen |

## Fortschritt, Wiederaufnahme und Rückweg

| Phase | Eigenes Objekt / genaue Datei oder Eintragsidentität | Vorherzustand / Hash | Letzter erfolgreich geprüfter Teilstand | Offene Voraussetzung / nächste Maßnahme | Erfolgssignal / Beleg | Konkreter Rückweg / gesonderte Löschfreigabe |
|---|---|---|---|---|---|---|
| noch nicht begonnen | offen | offen | offen | offen | offen | offen |

Geschützte gemeinsame Bestände: fremde Profile/Skills/Subscriptions, gemeinsame
Binaries/PM-Runtime, persönliche Codexausstattung, Produktdateien/AGENTS,
Dienst-/Bank-/Kanalinhalte und Graphcaches. Änderungen nur eindeutig zugeordnet;
Datenlöschung benötigt gesonderte Freigabe.

## Abnahme nach geprüftem Stand

Gemäß [Prüfanleitung](../references/verification.md) je Prüfung festhalten:
bestanden / konkreter Fehler / noch ungeprüft. Bei Fehlern Auswirkung und nächste
Maßnahme nennen. Nicht benötigte Fähigkeiten mit Begründung kennzeichnen.

| Prüfung | Geprüfter Stand | Ergebnis und kurzer Beleg |
|---|---|---|
| Paket: Dateibestand, Links, vollständige Skills, Personalisierung, Syntax und Konsistenz | offen | noch ungeprüft |
| Rollen, vollständige SOUL-Aufnahme, Skills und Modi | offen | noch ungeprüft |
| Planner-Interview: Originale grill-me/grilling samt Begleitdateien/Lizenz, Bytevergleich, native Discovery/Laden, SOUL-Pflicht und Planungsdialog im neuen Kontext/Resume | offen | noch ungeprüft |
| Modelle und wirksame Reasoning-Stufen einschließlich Grenzprüfung bei HIGH+HIGH, Resume und Helferdelegation | offen | noch ungeprüft |
| Team-Codex und installierte Helfer | offen | noch ungeprüft |
| Memory und Rollenfilter | offen | noch ungeprüft |
| Mattermost: Erwähnung, Free-Response, DM und Planner-Wake | offen | noch ungeprüft |
| Gewählte Codeanalyse: Index, Aufrufbeziehung und Aktualisierung | offen | noch ungeprüft |
| Tatsächliche Betriebsgrenzen und Erhalt fremder Zustände | offen | noch ungeprüft |
| Gemeinsamer Probelauf bis zum Plannerbericht | offen | noch ungeprüft |

- Gesamturteil: Paket geprüft / Zielsetup teilweise / Team technisch geprüft — mit Belegen ausfüllen.
- Offene Gates / konkret benötigte nächste Freigabe: offen
- Empfehlung: Nutzer erteilt dem Planner später einen konkreten ersten Planungsauftrag.
