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
`confirmed_values` enthält Namen, Projekt, Bank, Board, technische Profil-IDs und
die bereits bestätigte Codex-ID nur für die technische Konfiguration; `confirmed_bindings`
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

- Zielkonto-Home / absolut aufgelöstes `~/projects/<PROJECT_NAME>` / tatsächlicher Workspace / Gleichheitsbeleg oder offene Klärung: offen
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
- G1: open; konkrete fehlende Gesamtgrenze / Zielrevision / Belegpfad je Rolle: offen

## Modelle und Codex

- Je Rolle: Provider, Modell, Reasoning, native Configquelle, Overrides, echter Call: offen
- Unterstützte höhere Reasoning-Stufen am eingerichteten Modell / nativer Wechselweg und Beleg: offen
- Hilfsmodell-/Analysewege und Zugang separat: offen
- Team-Codex Prozess-HOME / CODEX_HOME / aufgelöste Binary: offen
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

Ergebnis je Kriterium: offen / bestanden / konkreter Blocker / nicht anwendbar
mit Begründung. Nie aus Quellenprüfung einen echten Lauf ableiten.

| ID | Kriterium | Geprüfter Stand | Ergebnis und Belegpfad |
|---|---|---|---|
| A01 | Vollständige Ausstattung, Codeanalyse-Funktionsprüfung gesondert | offen | offen |
| A02 | Portabler Export ohne private Abhängigkeiten | offen | offen |
| A03 | Rollen-/Modell-/Git-/Freigabekonsistenz, G1 sichtbar | offen | offen |
| A04 | Statische Qualität und Datenprüfungen | offen | offen |
| A05 | Anleitung und sichere Wiederaufnahme | offen | offen |
| A06 | Unabhängiger Review des eingefrorenen Pakets | offen | offen |
| B01 | Profile, vollständige Promptaufnahme, Discovery und persistente Modi | offen | offen |
| B02 | Echte Hermes-/Codex-/Hilfsmodellzugänge und Originalpins | offen | offen |
| B03 | Team-Codex-Artefakt, sechs echte begrenzte Delegationen | offen | offen |
| B04 | Neue Bank, echte Rollenfilter-/Speichernachweise | offen | offen |
| B05 | Erwähnung, Free-Response, DM und Wake im Projektkanal | offen | offen |
| B06 | Getrennte Planannahme → Dispatcher → Codex-Commit → unabhängiger Review → Plannerbericht | offen | offen |
| B07 | Produktprojekt unberührt, begrenzte Testressourcen und ehrliches Urteil | offen | offen |

- Gesamturteil: Paket geprüft / Zielsetup teilweise / Team technisch geprüft — mit Belegen ausfüllen.
- Offene Gates / konkret benötigte nächste Freigabe: offen
- Empfehlung: Nutzer erteilt dem Planner später einen konkreten ersten Planungsauftrag.
