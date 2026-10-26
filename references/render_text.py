"""Reine Texttransformation für den geführten Maker, MIT.

Kein CLI, Dateizugriff, Umgebungszugriff, Setup oder Runtimeimport. Der aufrufende
Agent prüft Eigentum/Freigabe, liest Vorlagen und schreibt ausschließlich bestätigte
Ziele. Dieses Modul entscheidet keine Persona-Befugnisse und verifiziert keine
nativen IDs, Dateiexistenz oder Modellverfügbarkeit.
"""
import re
import unicodedata

ROLE_FIELDS = {
    "ROLE_NAME", "PLANER_NAME", "CODER_NAME", "REVIEWER_NAME", "PROJECT_NAME",
    "HINDSIGHT_BANK_NAME", "KANBAN_BOARD_NAME",
}
ROLE_TECHNICAL_FIELDS = {
    "planner": {"CODER_PROFILE", "REVIEWER_PROFILE"},
    "coder": {"REVIEWER_PROFILE", "CODEX_REASONING_DEFAULT", "CODEX_REASONING_MAX"},
    "reviewer": {"ROLE_REASONING_DEFAULT", "ROLE_REASONING_HIGH"},
}
ROLE_NAMES = {"planner": "PLANER_NAME", "coder": "CODER_NAME", "reviewer": "REVIEWER_NAME"}
FIELD = re.compile(r"\{\{([A-Z0-9_]+)\}\}")


def plain(value, *, empty=False, limit=None):
    """Einzeiligen Klartext akzeptieren, nie still trimmen oder normalisieren."""
    if not isinstance(value, str) or (not empty and not value.strip()):
        raise ValueError("Nichtleerer Klartext erforderlich")
    if limit is not None and len(value) > limit:
        raise ValueError("Klartext überschreitet die erklärte Feldlänge")
    if any(unicodedata.category(c).startswith("C") or c in "\u2028\u2029" for c in value):
        raise ValueError("Steuer-/Formatzeichen und Zeilenumbrüche sind unzulässig")
    if "{{" in value or "}}" in value:
        raise ValueError("Eingebettete Templateklammern sind unzulässig")
    return value


def markdown(value):
    """Maskierung für Überschrift, Absatz und Tabellenzelle; keine Shellquotierung."""
    entities = {"&": "&amp;", "<": "&lt;", ">": "&gt;"}
    return "".join(entities[c] if c in entities else
                   "\\" + c if c in "\\`*_{}[]()#+!|." else c for c in value)


def role_fields(template, role):
    """Tatsächlich vorkommende deklarierte Felder, Mehrfachvorkommen erlaubt."""
    if not isinstance(role, str) or role not in ROLE_NAMES or not isinstance(template, str):
        raise ValueError("Unbekannte Rolle oder fehlender Vorlagentext")
    fields = set(FIELD.findall(template))
    rest = FIELD.sub("", template)
    if ("ROLE_NAME" not in fields or
            not fields <= ROLE_FIELDS | ROLE_TECHNICAL_FIELDS[role] or
            "{{" in rest or "}}" in rest or "{{{" in template or "}}}" in template):
        raise ValueError("Unbekannte, fehlende oder beschädigte Rollenfelder")
    return fields


def render_role(template, values, role):
    """Ein Durchlauf, nur Platzhalter ändern; Codekontexte erhalten rohe Werte."""
    fields = role_fields(template, role)
    if not isinstance(values, dict) or set(values) != fields:
        raise ValueError("Exakt die vorkommenden Rollenfelder erforderlich")
    for key, value in values.items():
        plain(value, limit=120 if key in {"ROLE_NAME", "PLANER_NAME", "CODER_NAME", "REVIEWER_NAME"} else None)
        if value != value.strip() or value.startswith("-"):
            raise ValueError("Einrückung oder Absatzmarker unzulässig; Klartext neu bestätigen")
        # Backticks können Inlinecode/Fences schließen; Backslashes ändern dort
        # technische Werte. Keine Reparatur oder Normalisierung von Nutzereingaben.
        if "`" in value or "\\" in value or "~~~" in value:
            raise ValueError("Unsichere Code-/Fencezeichen im Rollenwert")
        if key.endswith("_PROFILE") and not re.fullmatch(r"[a-z0-9][a-z0-9_-]{0,63}", value):
            raise ValueError("Ungültige technische Profilkennung")
        if "_REASONING_" in key and not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]*", value):
            raise ValueError("Reasoningwert muss ein einzelner sicherer nativer Wert sein")
        if key in {"HINDSIGHT_BANK_NAME", "KANBAN_BOARD_NAME"}:
            if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.:/-]*", value):
                raise ValueError("Unsichere technische Kennung")
        if key == "PROJECT_NAME" and (value in {".", ".."} or "/" in value):
            raise ValueError("Projektname muss ein einzelnes Pfadsegment ohne Traversal sein")
    own_name = ROLE_NAMES[role]
    if own_name in values and values[own_name] != values["ROLE_NAME"]:
        raise ValueError("ROLE_NAME widerspricht dem eigenen Rollennamen")

    def replace(text, raw=False):
        return FIELD.sub(lambda match: values[match.group(1)] if raw else
                         markdown(values[match.group(1)]).replace("=", r"\=").replace("~", r"\~"), text)

    result = []
    fence = None
    for line in template.splitlines(keepends=True):
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line.rstrip("\r\n"))
        if fence:
            result.append(replace(line, raw=True))
            if marker and marker[1][0] == fence[0] and len(marker[1]) >= len(fence) and not marker[2].strip():
                fence = None
        elif marker:
            fence = marker[1]
            result.append(replace(line, raw=True))
        else:
            # Inlinecode nur auf der originalen Vorlage erkennen, nie auf Inputs.
            end = 0
            for match in re.finditer(r"(`+)(.*?)\1", line):
                result.append(replace(line[end:match.start()]))
                result.append(replace(match[0], raw=True))
                end = match.end()
            result.append(replace(line[end:]))
    return "".join(result)
