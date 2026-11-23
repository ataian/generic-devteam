"""Reine Texttransformation für den geführten Maker, MIT.

Kein CLI, Dateizugriff, Umgebungszugriff, Setup oder Runtimeimport. Der aufrufende
Agent prüft Eigentum/Freigabe, liest Vorlagen und schreibt ausschließlich bestätigte
Ziele. Dieses Modul entscheidet keine Persona-Befugnisse und verifiziert keine
nativen IDs, Dateiexistenz oder Modellverfügbarkeit.
"""
import re
import shlex
import unicodedata

ROLE_FIELDS = {
    "ROLE_NAME", "PLANER_NAME", "CODER_NAME", "REVIEWER_NAME", "PROJECT_NAME",
    "HINDSIGHT_BANK_NAME", "KANBAN_BOARD_NAME", "DEMO_PASSWORD",
}
ROLE_TECHNICAL_FIELDS = {
    "planner": {"CODER_PROFILE", "REVIEWER_PROFILE", "PROJECT_DIR", "REPOSITORY_ROOTS"},
    "coder": {"PLANNER_PROFILE", "REVIEWER_PROFILE", "CODEX_REASONING_DEFAULT", "CODEX_REASONING_MAX",
              "CODEX_BINARY", "CODEX_PROCESS_HOME", "CODEX_HOME"},
    "reviewer": {"ROLE_REASONING_DEFAULT", "ROLE_REASONING_HIGH"},
}
ROLE_NAMES = {"planner": "PLANER_NAME", "coder": "CODER_NAME", "reviewer": "REVIEWER_NAME"}
FIELD = re.compile(r"\{\{([A-Z0-9_]+)\}\}")
CODEX_PATH_FIELDS = {"CODEX_BINARY", "CODEX_PROCESS_HOME", "CODEX_HOME"}
# Literal value: never Markdown-escaped, so the SOUL carries the exact string.
LITERAL_FIELDS = {"DEMO_PASSWORD"}


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
    """Replace placeholders once; quote Codex paths only inside shell fences."""
    fields = role_fields(template, role)
    if not isinstance(values, dict) or set(values) != fields:
        raise ValueError("Exakt die vorkommenden Rollenfelder erforderlich")
    for key, value in values.items():
        plain(value, limit=120 if key in {"ROLE_NAME", "PLANER_NAME", "CODER_NAME", "REVIEWER_NAME"} else None)
        if value != value.strip() or value.startswith("-"):
            raise ValueError("Einrückung oder Absatzmarker unzulässig; Klartext neu bestätigen")
        if key == "DEMO_PASSWORD" and any(c in value for c in "`\\~"):
            raise ValueError("Demonstrationspasswort darf keine Backticks, Backslashes oder Tilden enthalten")
        # Backticks können Inlinecode/Fences schließen; Backslashes ändern dort
        # technische Werte. Keine Reparatur oder Normalisierung von Nutzereingaben.
        if "`" in value or "\\" in value or "~~~" in value:
            raise ValueError("Unsichere Code-/Fencezeichen im Rollenwert")
        if key == "PROJECT_DIR" and (not value.startswith("/") or
                (value != "/" and any(part in {"", ".", ".."} for part in value[1:].split("/")))):
            raise ValueError("Workspace must be an absolute canonical path")
        if key in CODEX_PATH_FIELDS and (not value.startswith("/") or
                any(part in {"", ".", ".."} for part in value[1:].split("/"))):
            raise ValueError("Codex binding must be an absolute canonical path: " + key)
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

    def replace(text, raw=False, shell=False):
        def one(match):
            key = match.group(1)
            if shell and key in CODEX_PATH_FIELDS:
                return shlex.quote(values[key])
            if raw or key in LITERAL_FIELDS:
                return values[key]
            return markdown(values[key]).replace("=", r"\=").replace("~", r"\~")
        return FIELD.sub(one, text)

    result = []
    fence = None
    shell = False
    for line in template.splitlines(keepends=True):
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line.rstrip("\r\n"))
        if fence:
            result.append(replace(line, raw=True, shell=shell))
            if marker and marker[1][0] == fence[0] and len(marker[1]) >= len(fence) and not marker[2].strip():
                fence = None
        elif marker:
            fence = marker[1]
            shell = marker[2].strip() in {"sh", "bash"}
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
