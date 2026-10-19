# Visueller Abgleich

## Vergleichsbedingungen zuerst

Im vorhandenen Brief oder Prüfprotokoll festhalten:

- beauftragter CSS-Viewport je Zielgröße, Browserzoom und Pixeldichte (DPR);
- Quelle samt Seite/Ausschnitt, Skalierung und Crop; sichtbarer Viewport oder vollständige Seite;
- Datenstand einschließlich Langtext-/Fehlwertfällen, Schriften und akzeptierte Ersatzschriften;
- genehmigte Inhalts-/Farb-/Layoutabweichungen und vereinbarte Abnahmekriterien;
- Arbeitsbudget und noch verfügbare Render-/Korrekturversuche.

Eine PDF-Seite hat keinen impliziten Browserviewport. Eine Bildbreite darf bei unbekannter Pixeldichte nicht pauschal halbiert werden. Relevante unbekannte Bedingungen klären, nicht passende Werte erfinden.

## Echte Aufnahme und Prüfung

1. Mit zugelassenem Projektwerkzeug tatsächlich bauen/starten. Ladefehler, falsche Daten, Auth-/Mockmodus und Browserfehler sichtbar machen. Keine ungenehmigte Betriebsänderung zum Starten.
2. Auf fertige Inhalte, Bilder und Schriften warten, nicht nur auf den ersten DOM-Aufbau oder eine beliebige Schlafzeit. Verfügbare Bereitschaftssignale wie abgeschlossene Datenabfragen, Bilddekodierung und Fontbereitschaft nutzen.
3. Aufnahmen für den beauftragten Scope erstellen. Quelle **und tatsächlichen Render ansehen**. Ein gespeichertes Bild, DOM-Text oder ein Pixel-Diff allein ist kein vollständiger Sichtnachweis.
4. In dieser Reihenfolge vergleichen: Inhalt/Vollständigkeit und Struktur; Raster/Ausrichtung; Abstände; Typografie/Umbrüche; Farben; Assets/Details. Genehmigte Unterschiede sind Teil des Solls.
5. Lange Texte, variable Listen/Extras und vertraglich unterschiedliche null/fehlend/leer/0-Fälle überprüfen. Kein Weglassen als Layoutfix. Unbeabsichtigten Überlauf, Schnitt oder Überlagerungen nicht als Schriftfallback entschuldigen.
6. Semantik, Alternativtexte, Labels und Kontrast prüfen; bei Interaktionen sichtbaren Fokus und Tastaturbedienung ausüben. Konkrete Konflikte mit Vorlagentreue klären. Keine uneingeschränkte Barrierefreiheitsbehauptung aus einer Sichtprobe.
7. Abweichungen gezielt korrigieren und betroffene Bedingungen erneut prüfen. Vorgeschriebene Projektchecks zusätzlich ausführen; reine Renderfähigkeit ist keine Verhaltens-/Vertragsabnahme.

## Ehrliche Stopplogik

Keine universelle Zahl von Durchläufen und keinen pauschalen Pixel-Diff-Grenzwert vorgeben. Das vereinbarte Budget begrenzt Versuche, nicht die Abnahmequalität.

- Browser/Build fehlt: Rendernachweis offen; andere unabhängige Prüfungen dürfen weiterlaufen.
- Bildsicht fehlt: technische Aufnahme gegebenenfalls belegt, visuelle Übereinstimmung **nicht geprüft**.
- Budget erschöpft: keine weitere automatische Runde; verbleibende Unterschiede, Auswirkungen und fehlende Nachweise übergeben. Nicht durch Formulierungen als bestanden darstellen.

Nachweis nennt Quelle, Code-/Buildstand, Daten und Vergleichsbedingungen, echte Aufnahmen/Testergebnisse, betrachtete Unterschiede, akzeptierte Abweichungen und offene Mängel. Fremdberichte als solche kennzeichnen, nicht als eigene Durchführung.
