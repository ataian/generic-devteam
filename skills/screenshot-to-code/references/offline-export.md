# Optionaler Offlineexport

Nur bei ausdrücklichem Zusatzauftrag. Kein Standardlieferumfang und keine Umgehung der Projektregeln.

## Eine Implementierung, zusätzliche Ausgabe

Aus denselben Komponenten, Daten und kompilierten Styles wie die reguläre Ansicht exportieren. Vorhandenen Build-/Renderweg wiederverwenden; keinen zweiten HTML-/Frameworkstack pflegen. Falls Interaktionen beauftragt sind, deren Offlinefähigkeit separat erhalten und prüfen; ein statischer Export darf sie nicht still verlieren.

Alle benötigten Styles, Bilder, Originalassets und Schriften einbetten. Keine CDN-Aufrufe, externen Imports, relativen Dateiabhängigkeiten, versteckten Fetches oder Abhängigkeit von Service-Worker-/Browsercache. Pfadprüfung und tatsächlicher Offlinebrowser ergänzen einander. Nicht nur sichtbare img-Quellen prüfen, sondern auch CSS-URLs, Fonts, Imports und Skripte.

## Wiederholbarer und fehlersicherer Lauf

1. Eingaben/Stand und erwartete Assets validieren; Ausgabe zunächst separat vorbereiten.
2. Export mit eindeutigem Erfolgs-/Fehlerstatus erzeugen. Nur nach erfolgreicher Prüfung als aktuelles Ergebnis veröffentlichen. Fehlendes Originalasset ist ein Fehler, keine automatische Ersatzgrafik.
3. Existiert ein alter Export, darf ein fehlgeschlagener Lauf ihn weder als neu ausgeben noch über einen veralteten Erfolgsmarker anbieten. Alten Stand kenntlich lassen; nötige Dateientfernung unterliegt den vorhandenen Rechten.
4. Wiederholten Export desselben Stands prüfen. Falls Zeitstempel o. Ä. Unterschiede erzeugen, Ursache und reproduzierbare Vergleichsbasis dokumentieren, nicht ungeprüft Bytegleichheit behaupten.

## Tatsächliche Offlineabnahme

Die fertige einzelne Datei isoliert ohne Nachbardateien und ohne nutzbare Netzverbindung über `file://` im Browser öffnen, ohne hilfreiche alte Caches. Nur ein Serveraufruf mit eingebetteten Styles reicht nicht.

Beauftragte Viewports prüfen: Inhalte, Bilder/Originalassets, Schriften, lange Texte, Fehlwerte und beauftragte Interaktionen. Quelle, regulären Browserrender und Offlineansicht tatsächlich ansehen. Fehlassetprobe mit vorhandenem altem Export ausführen: Fehler muss sichtbar sein, alter Export darf kein aktueller Erfolg werden.

Handoff nennt Exportpfad/Stand, wiederholbaren Erzeugungsweg, echte positive und negative Ergebnisse, Offline-/Sichtnachweise und offene Grenzen. Ohne diese Prüfungen bleibt die Exportabnahme offen; Deployment entsteht daraus nicht automatisch.
