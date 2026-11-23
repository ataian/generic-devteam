# CAC-CODEX — Compact Technical Instruction & Handoff Notation

**Purpose:** A concise, declarative writing style for Codex-facing instructions, technical artifacts, task messages, findings, and replies.

**Scope:** Representation **only**. CAC-CODEX is intended to replace Caveman/TAS *as a writing convention* in the Codex context. It does not define tasks, implementation methods, reasoning effort, tool usage, verification duties, approval rules, or workflows. Examples are **syntax illustrations, not mandated task or report contents**.

## 1. Core style

Prefer **structured facts and exact technical references** over narrative descriptions, without losing meaning.

- Preserve all existing constraints, conditions, exceptions, negations, and obligation levels (`MUST` / `SHOULD` / `MAY`).
- Preserve identifiers, names, code snippets, paths, commands, and literals exactly.
- State observations as observations; distinguish them from assumptions and proposals.
- Use conventional technical English with descriptive keys, not opaque abbreviations.
- Remove redundant lead-ins, repetitive summaries, filler, and explanations that add no information.
- Use concise prose where relations, rationale, or subtle behavior would otherwise become ambiguous.
- Treat structure as a writing aid, **not** an exact input/output schema unless an existing interface already requires one.

## 2. Notation

| Content | Compact representation |
|---|---|
| One instruction | Brief directive with original modality |
| Related parameters | `key: value` mapping |
| Several constraints | Short list |
| Conditional behavior | `when` / `then` / `except` |
| Code location | Existing `path:line`, symbol, or commit reference |
| Technical difference | `observed` / `expected` / `difference` |
| Simple state | One labeled line |
| Hard-to-compress reasoning | Brief, explicit prose |

Markdown + YAML-like mappings are the default *options*, not compulsory serialization. Avoid nesting that costs more tokens than an ordinary sentence; omit empty fields. Do not impose a glossary or a novel programming language on the reader.

## 3. Instruction and skill wording: examples

### Example A — compact task description

**Verbose sample:**

> In the illustrative parser, dates arrive as ISO strings. If a date has no timezone, the currently configured default timezone applies. The existing error mapping is unchanged.

**CAC:**

```yaml
parser_input: ISO_date_string
timezone:
  when: missing
  use: existing_configured_default
error_mapping: unchanged
```

### Example B — precise exception

**Verbose sample:**

> The value `null` is allowed for optional fields, but it is not allowed for the required field `id`.

**CAC:**

```yaml
null:
  optional_fields: allowed
  id: forbidden
```

### Example C — simple rule without extra structure

```text
MUST retain existing API field names.
```

No behavior is introduced by these examples; they only demonstrate representation of hypothetical existing information.

## 4. Compact Codex-facing messages: suggestions

These are **optional message shapes**. They do not prescribe what Codex must do or report. Select only fields that already belong to the exchange.

### Task context

```yaml
ref: T42
target: <existing target>
change: <requested delta>
constraints: [<existing constraint>]
context: <minimal necessary fact or resolvable reference>
```

### Technical result / handoff

```yaml
ref: T42
revision: <commit or artifact reference>
changes: <concise factual summary>
observed: <relevant observed outcome>
open: <relevant unresolved detail, if any>
```

### Defect / review observation

```yaml
at: src/example/Parser.java:84
observed: null_value_accepted
expected: id_non_null
impact: invalid_record_possible
evidence: <actual evidence reference>
```

### Single-line message

```text
ref: T42 | rev: a1b2c3d | result: <short factual outcome>
```

### Conditional detail

```yaml
case:
  when: <condition>
  observed: <fact>
  exception: <exception if relevant>
```

Field names and examples express a notation only; they do not add obligations, redefine existing fields, or establish status transitions.

## 5. Code and document boundaries

- **Codex-facing text:** use this compact notation when it improves clarity and token economy.
- **Source code:** keep syntax and project coding conventions; CAC is not a code formatter.
- **Code comments and human documentation:** prioritize the intended reader and necessary explanation.
- **Human conversation:** use clear natural language rather than cryptic agent shorthand.
- **Existing machine-readable formats:** keep their required syntax and semantics; CAC does not supersede JSON schemas, APIs, or other formal contracts.

**Core test:** The compact version communicates the same information, with equally clear conditions and fewer unnecessary tokens. If a structure obscures meaning or increases length, use a short sentence instead.
