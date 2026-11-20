# CAC-HERMES — Compact Artifact & Communication Notation

**Purpose:** Compact, precise, agent-readable expression of existing information in Hermes SOULs, skills, technical documents, and agent-to-agent messages.

**Scope:** Writing and representation **only**. CAC-HERMES is intended to replace TAS/Caveman *as a writing convention*. It neither defines nor changes roles, permissions, procedures, workflow, document obligations, or team architecture. Examples below are **notation samples, not new rules or required fields**.

## 1. Principle: minimum complete expression

Prefer **declarative structure over explanatory prose** when it expresses the same meaning with fewer tokens.

- Preserve meaning, including actor, obligation strength (`MUST` / `SHOULD` / `MAY`), conditions, exceptions, scope, order, and uncertainty.
- Keep identifiers, paths, commands, code symbols, and quoted values exact.
- Remove linguistic padding, repeated context, obvious restatements, and decorative transitions.
- Preserve needed qualifications. Compression must not create ambiguity.
- Use ordinary technical English. Avoid invented abbreviations, cryptic codes, and glossary-dependent mini-languages.
- Use natural language when it is clearer or more compact than a schema.

## 2. Notation selection

Choose the smallest *readable* representation that fits the content:

| Information | Preferred form | Example |
|---|---|---|
| Single fact / property | `key: value` | `source: repository` |
| Related properties | YAML-like mapping | `format: markdown` |
| Alternatives / sets | Inline or multiline list | `formats: [md, yaml]` |
| Condition / exception | `when` / `then` / `except` | `when: input_missing` |
| Single normative rule | Short technical directive | `MUST preserve explicit exclusions.` |
| Cause / observation | Named factual fields | `observed: ...` / `expected: ...` |
| Simple message | One line with labeled fields | `ref: T42 | status: ready` |
| Nuanced explanation | Short prose | One clear paragraph |

**Not YAML-only.** Use Markdown headings and fenced YAML blocks when they improve grouping. Keep existing syntactic requirements (for example, skill frontmatter) intact. No new parser or machine-validation requirement is implied.

### Compact syntax conventions

```yaml
name: descriptive_snake_case     # familiar, self-explanatory keys
flags: [alpha, beta]             # short collections inline
scope:
  include: [item_a, item_b]
  exclude: [item_c]
condition:
  when: relevant_condition
  then: stated_effect
  except: explicit_exception
```

The fields are illustrative; **no universal schema is mandatory**. Avoid empty keys and sections. If a one-line directive uses fewer tokens than a nested mapping, use the directive.

## 3. SOUL and skill text: representation examples

### Example A — paragraph to declaration

**Verbose sample:**

> The supported report representations are Markdown and YAML. Markdown is preferred for longer explanations, while YAML is preferred for small sets of structured values.

**CAC:**

```yaml
report_format:
  supported: [markdown, yaml]
  prefer:
    long_explanation: markdown
    small_structured_values: yaml
```

### Example B — scoped statement

**Verbose sample:**

> The identifier may be omitted if it is unknown. However, the value `0` is valid and must not be treated as missing.

**CAC:**

```yaml
identifier:
  unknown: omission_allowed
  value_0: valid; MUST retain
```

### Example C — short directive beats a schema

```text
MUST preserve quoted literals and exact file paths.
```

This is preferable to creating multiple nested fields for one straightforward rule.

**For long agent-authored texts:** use compact headings plus mappings, lists, and short directives. Retain details when they carry meaning; do not compress distinct requirements into an ambiguous slogan.

## 4. Agent-to-agent message suggestions

Suggested **notation**, not a prescribed protocol. Existing channels, statuses, responsibilities, and message content remain authoritative. Include only fields actually relevant to the given message.

### Short event

```text
ref: T42 | state: ready | rev: a1b2c3d
```

### Handoff / update

```yaml
ref: T42
change: <brief factual summary>
result: <observed result>
refs: [<existing artifact or commit>]
open: <remaining relevant detail, if any>
```

### Finding / technical disagreement

```yaml
ref: T42
at: <file:line or artifact reference>
observed: <actual behavior>
expected: <expected behavior>
impact: <consequence>
evidence: <reference or concise fact>
```

### Clarification / decision exchange

```yaml
ref: T42
question: <precise point>
options: [<A>, <B>]
context: <only what is needed to interpret the question>
```

### Longer artifact

```markdown
## Context
<compact facts or references>

## Details
<structured entries, short directives, or concise prose>

## Open points
<only if present>
```

These shapes demonstrate compression, **not** requirements to produce a particular document, section, status, or action. References are useful only when recipients can actually resolve them.

## 5. Audience adaptation

- **Agent-facing:** compact technical notation by default.
- **Human-facing (including customer communication):** clear, concise natural language in the recipient's language; explanations remain available where they help interpretation or decisions.
- **Mixed audience:** preserve human readability; compact structured data may be embedded where useful.

**Core test:** Could another reader recover every relevant distinction from the compressed expression without guessing? If not, add the missing words.
