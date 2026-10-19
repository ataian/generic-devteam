# Herkunft und Lieferstand

## T6: Statischer Kandidat zur unabhängigen Gesamtprüfung

Die eigenen Skillbäume und ihre Begleitdateien sind enthalten. Der exakte
Bestand steht in [manifest.json](manifest.json), Rollen und Quellen in
[upstream-sources.md](references/upstream-sources.md). Rollen-SOULs und installierte
Skills tragen den Arbeitsprozess unabhängig vom Makerpaket.
Die Makerseite [native-workflow.md](references/native-workflow.md) beschreibt
Einrichtung und Prüfung der Arbeitsbindungen sowie den Render-/Kontextvertrag
für die drei enthaltenen Rollen-SOULs. Der [Maker](SKILL.md), das geführte
[Setup](references/setup.md), allgemeine [Integrationsrezepte](references/integrations.md),
eine private Protokollvorlage und reine Textvalidierung sind enthalten.
Beide [Codeanalysewege](references/code-analysis.md) sind als Einrichtungsrezepte
enthalten. CBM umfasst seine offizielle Codex-Integration einschließlich Unteragenten.
Die Funktionsprüfung erfolgt erst beim Zielsetup. Keine fremde
Runtime oder Originalskillkopie wird in diesem Maker mitexportiert.

## Eigene Texte und G3

Neue Texte und Tests wurden im Auftrag von Max durch Mariko (Hermes Agent) für
Generic Devteam verfasst. Für sie gilt die vollständige [MIT-Lizenz](LICENSE),
`Copyright (c) 2026 generic-devteam contributors`. Diese Notice bezeichnet die
neue Paketfassung; sie behauptet keine historische Rechtekette. Paketversion,
Planversionen und spätere Zielprojektversionen sind unabhängig.

| Anteil | Herkunft und tatsächliche Behandlung |
|---|---|
| Paketvertrag, Tests und Dokumentation | Neu aus bestätigtem Auftrag; MIT dieses Pakets. |
| Drei Rollen-SOUL-Vorlagen | Aktuell: Planner/Coder quellnah aus vorhandenen Rollen-SOULs im ausdrücklich bestätigten Auftrag abgeleitet; Reviewer als maßgebliche Nutzerfassung unverändert integriert. Persönliche Bindungen durch deklarierte Felder ersetzt, genehmigte portable Plannerregel bis drei Budgeterweiterungen erhalten. Frühere T3/T6-Neufassungen sind historischer Lieferstand, nicht die aktuelle Fassung. Kein Export aktiver Profilidentitäten; private Quellen sind keine Testabhängigkeit. |
| `screenshot-to-code` 1.0.0 | Kanonisches eigenständiges Paket, Autorenfeld `Max, Mariko (Hermes Agent)`. Alle sechs Dateien bytegleich, nur `SKILL.md` als `SKILL.md.template` transportiert. Eigene vollständige [Lizenz](templates/skills/screenshot-to-code/LICENSE) mit `Copyright (c) 2026 screenshot-to-code contributors` unverändert. |
| `minimal-change-engineering` 0.1.0 | Portable Sammlung fachlich gelesen; deren `Max (drafted) + Joi`-/MIT-Angabe ohne ursprünglichen vollständigen Lizenztext ist keine neue Rechtebehauptung. Bestätigte Regeln eigenständig neu formuliert, Projektprüfungen/Fixtures und Rollen präzisiert. |
| `brownfield-feature-planning` 0.1.0 | Planungskern neu formuliert, historische Spezialverfahren nur fachlicher Vergleich. Keine historische menschliche Autorenschaft aus Rollenmetadaten abgeleitet. |
| `plan-versioning-semver` 0.1.0 | Neue Formulierung bestätigter Regeln. Ursprüngliche Lizenz bleibt unbelegt; keine produktgebundene Versions-API-/Changelogpflicht übernommen. |
| `project-lib-versioning` 0.1.0 | Neue technologieunabhängige Formulierung mit rekursiven Verbrauchern und Rollenpflichten. Historischer Preservation-Audit bleibt unbelegt, kein alter Text übernommen. |

**G3 für den T2-Lieferstand:** Screenshot besitzt seinen erhaltenen eigenen
Lizenztext; die übrigen fünf Fassungen sind neu verfasst und tragen jeweils eine
vollständige eigene Lizenz und Herkunftsnotice im Skillbaum. Die historischen
Rechtelücken werden nicht rückwirkend geschlossen. Ein späterer Export anderer
historischer Textanteile bleibt davon unberührt.

Die aktuelle Rollenherkunft ist die oben benannte quellnahe Ableitung bzw.
Nutzerfassung, nicht mehr eine unveränderte T3-Neufassung. Die Paketlizenz bleibt
erhalten; damit wird keine ungeprüfte historische Rechtekette behauptet.
Autorenprüfung und Integrationschecks sind kein unabhängiger Review.

## Fremdkomponenten und technische Grenzen

Fremdkomponenten sind Bezugsidentitäten mit dokumentierten Zielrezepten, keine
mitexportierten Installationen. Ihre konkreten Bezugsstände behalten eigene
Lizenzen/Notices; unsere MIT-Lizenz lizenziert sie nicht um. Rechercheidentitäten
in nativen Rezepten sind keine Installationspins oder Runtimegarantien.

Timeout-, Retry- und Rate-Limit-Behandlung werden am tatsächlichen Zielstand
geprüft; konkrete Einschränkungen und ihre Auswirkungen gehören ins Setup-Protokoll.

## Dateivertrag

`files` ist die sortierte, duplikatfreie Liste aller regulären Paketdateien außer
`manifest.json`. Symlinks, Bytecode und interne Evidenz gehören nicht hinein.
Im Standalone-Checkout zählen `.git/`, `.gitignore` und die Vortragsbeilage
`vortrag/` nicht zum Skillpaket; alle übrigen Dateien werden vollständig geprüft.
`own_skills.targets` nennt direkte Zielrollen/Harnesse; Auftragspflichten an Codex
sind keine zusätzliche Skillinstallation. `status: included` meint vorhandene
Dateien, nicht aktivierte Fähigkeiten. `skill_path`, `license_path`, `notice_path`
und `origin_ref` sind paketrootrelativ; die Transportabbildung benennt nur den
Einstieg um. `source_sha256` beim Screenshot enthält die kanonischen Dateiidentitäten
vor Transportumbenennung. Der öffentliche Test braucht keinen privaten Quellbaum.

`role_templates` enthält genau Planner, Coder und Reviewer; `targets` bindet jede
Vorlage an ihr eigenes Hermes-Profil. `template_path`, `origin_ref`, `license_path`
und `notice_path` sind paketrootrelativ. `transport` bezeichnet das spätere
Renderziel `SOUL.md` in diesem Profil, nicht eine Aktivierung im Bauprojekt.
`render_fields` enthält die sortierte eindeutige Menge der tatsächlich vorkommenden
deklarierten Rollenfelder; Mehrfachvorkommen sind erlaubt. Herkunft, Validierung
und Kontextgrenzen stehen in der Makerreferenz. Technische Werte stammen aus
denselben bestätigten Daten wie die Zielkonfiguration.

`upstream_components.subpaths` sind originalrepositoryrelative Pfade; `.` meint
den Repositoryroot. `recipe_status: pending` ist ein offener Folgeauftrag, kein
Setupnachweis. `recipe_status: documented` bedeutet ein vorhandenes Rezept,
nicht dessen erfolgreiche Ausführung. Nur die Rollenfelder werden beim Zielsetup
mit bestätigten Werten gerendert; eigene Skillbäume bleiben vollständig unverändert.

Analysemetadaten im Manifest: `reviewed_revision` ist ein Rechercheanker,
`asset_bundles.source_to_target` bildet die vollständigen Graphify-Originalbäume
auf relative Skillziele ab; `sha256` bezieht sich auf gelesene Originalbytes.
`legal_files` sind beim Bezug unverändert beizulegende Rechtstexte. CBM-
`release_members` ist eine Packagerableitung, kein geprüfter Archivinhalt;
`asset_evidence` benennt ausdrücklich statische Ableitung statt Installeroutput.
Die tatsächliche Codeanalyse-Funktion wird beim Zielsetup geprüft. Graphify trägt Apache-2.0 samt MIT-
Vorgeschichte/NOTICE, CBM MIT samt Release-THIRD_PARTY_NOTICES; keine Umlizenzierung.

## Dateibasierte Prüfung

Die [Prüfanleitung](references/verification.md) beschreibt die Prüfung des aktuellen
Dateibestands, der Links, Skillpakete, Rollenpersonalisierung und Syntax. Reine
Textprüfungen belegen weder Agentenverhalten noch ein funktionsfähiges Zielteam.
Die gesonderte Zielprüfung umfasst die eingerichteten Fähigkeiten und einen kleinen
gemeinsamen Probelauf. Ergebnisse gehören mit geprüftem Stand und kurzem Beleg ins
Setup-Protokoll. Diese Notice erklärt keinen Review oder Export der aktuellen
Fassung für abgeschlossen.
