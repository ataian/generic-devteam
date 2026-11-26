# PLAN 3.1.0 — Lokale Umgebungsgrenzen in den Maker holen

**Dokumentversion:** v1 (Erstfassung). Prüft, ob der im Team soos gelernte Abschnitt „Local development environment discovery" als Maker-Regel taugt.
**Status:** Vorschlag des Betreibers, nicht des Teams. Keine Datei des Pakets geändert, nichts committet. Umsetzung erst nach Freigabe.

**Herkunft und Verantwortung:** Der Text stammt aus einer lokalen Ergänzung im installierten Skill des Teams soos; das Team hat ihn weder verfasst noch vorgeschlagen, und es kennt diesen Plan nicht. Die Übernahme in den Maker ist eine Entscheidung des Betreibers, weil der Maker der einzige Ort ist, an dem eine solche Regel neue Teams erreicht. Das Team bleibt bei diesem Vorgang unverändert.

## Ausgangslage

- Das Team soos führt seit dem Update auf 1.1.22 einen lokalen Zusatz in `skills/brownfield-feature-planning/SKILL.md`, Zeilen 175–184, Abschnitt „Local development environment discovery", fünf Regeln. Beleg: `installation.json` → `managed[...].baseline` des Ziels und `manual-updates/update-1.1.22/preserved-local-section.md`.
- Abgleich gegen den Stand 3.1.0: `grep -ril 'tunnel\|CORS\|exposure\|free port\|local catcher' templates/ skills/` ergibt keinen Treffer; `loopback` steht nur in `skills/dev-environment/SKILL.md:32` als Satz über Listener-Bindung. Die fünf Regeln sind damit nicht gedeckt.
- Folge: Ein neu erzeugtes Team erbt die Regeln nicht, und das Team soos hält sie außerhalb des Makers.

## Vorschlag

### Schritt 1 — `skills/dev-environment/SKILL.md`

**Ort:** neuer Abschnitt `## Local environment boundaries`, eingefügt vor der Zeile `## Hand over one operating guide` (aktuell Zeile 36; die Zeile kommt in der Datei genau einmal vor, gezählt mit `read_text().count('## Hand over one operating guide')`).

**Englische Fassung nach CAC:**

```markdown
## Local environment boundaries

- Discovery before a recommendation: MUST compare the existing development and container start paths first — read build manifests, package scripts, Dockerfiles and Compose dependencies; distinguish a stack name from the services it really supplies; compare required runtime versions with installed ones; inspect startup commands for generated files, formatters or other writes before calling them read-only checks. MUST report conflicts with repository instructions instead of rewriting them or claiming a passed build.
- SSH-tunneled access: map browser-visible frontend, API, OIDC issuer and redirect URLs together. List every required tunnel with a free port in the owner's range and bind host processes as well as container port mappings to loopback explicitly; a free-port check or a Compose project name does not restrict exposure. Inventory auxiliary listeners from test containers, fixture servers, mail UIs and management endpoints before selecting verification commands. Preserve mandatory verification gates, resolve a concrete conflict explicitly, verify effective listeners after startup and keep synthetic mail in a local catcher.
- Owner-supplied external dependency: retain the approved URL and trace how each consumer builds its request. Distinguish a full browser API endpoint from a backend base URL that appends its own path; document consumer-specific derivations so no segment is appended twice. Probe with synthetic input; inspect redirects, final status, expected response shape and CORS against the intended local browser Origin separately. Report owner approval, server success, browser permission and integrated behavior as distinct evidence; a probe verifies neither an unimplemented proxy nor the end-to-end flow, and an unsuccessful probe is not a validated recipe.
- Failed external operation: record the exact request and bounded impact and route the prerequisite to its owner. After an endpoint correction, probe the replacement and mark old-address findings superseded; a failure at the old URL does not prove the replacement is broken. Keep only the dependent function or gate blocked and continue authorized work without waiving completion criteria.
```

**Voraussetzung:** keine; die Datei ist Planner-eigen und wird nur bei Umgebungsaufgaben geladen.
**Aufwand:** ein Abschnitt, rund 20 Zeilen.

### Schritt 2 — `templates/roles/planner.SOUL.md.template`

**Ort:** `## Role and authority`, direkt nach der Zeile, die mit `- When the project has an assigned development environment or a demonstration runtime, it is yours to operate.` beginnt (aktuell Zeile 12; der Satzanfang kommt in der Datei genau einmal vor, gezählt mit `read_text().count(...)`).

**Englische Fassung nach CAC:**

```markdown
- Record the owner's local operating authority once — target host, permitted updates and restarts, data boundary, exposure and remote access — and carry it into plan and handoff instead of asking again for each already-covered update. New scope, other hosts, publication and changes to shared external services stay outside that authority.
```

**Voraussetzung:** keine; reine Autoritätszeile ohne Renderfeld.
**Aufwand:** eine Zeile.

### Schritt 3 — Verifikation

- `python3 -B -m unittest references.test_dev_environment` (Sekunden).
- Renderprobe der Planner-SOUL mit Beispielbindungen: Platzhaltermenge unverändert, Zeilenzahl plus eins.
- Versionsbump **3.1.0 → 3.1.1** in `SKILL.md` und `manifest.json` (reine Textänderung, kein Renderfeld, kein neuer Helferzustand).

## Nichtziele

- Kein neues Renderfeld, keine Änderung an Coder- oder Reviewer-Template, keine Änderung an `command_allowlist` oder `settings`.
- Kein Tunnel-, Port- oder Proxy-Werkzeug; die Regeln beschreiben Prüfpflichten, keine Automatisierung.
- Der lokale Abschnitt im Team soos bleibt nach der Auslieferung zunächst stehen. Ob das Team ihn danach fallen lässt, ist eine eigene Entscheidung nach dem nächsten Plan und nicht Teil dieses Vorhabens.

## Zurückgezogen gegenüber v1

Nichts; Erstfassung.
