# External-data discovery

Trigger: supplied files, reference catalogs, export mappings, or an optional datastore. Use only sections required by the accepted goal. Discovery grants no implementation, source-copy, or target-mutation authority.

## Establish source identity and format

1. Locate inputs through maintained import docs and the supplied location. Narrow ambiguity with a parent-directory inventory. Do not search the whole home for documented bulk input.
2. Before proposing import or lookup rules, read each source with its schema/README. Check encoding per file, delimiters, field meanings, multiplicity, version, and null representation. Compare actual shapes with current builders. Historical names and cardinalities can differ.
3. Before relying on a sample, verify canonical identity and hashes. A mock can share an operational filename. Keep permitted provenance in the existing plan or task.
4. Inspect sensitive content machine-side with narrow projections. Return only required schema-known field names, types, and collection sizes. Exclude values, arbitrary dictionary keys, free text, and identifying filenames. Pseudonymized data remains sensitive.
5. Store restricted source identity and case-to-filename mappings in authorized protected local storage. Use neutral aliases in plans, tickets, delegated prompts, and reports. Use synthetic shareable fixtures. Source-read access grants no database writes, exports, or implementation release.
6. For operational-file or populated-database tests, load [Authorized local source-data acceptance](replacement-imports.md#authorized-local-source-data-acceptance). A supplied directory or service address proves neither a matching record nor a successful prior job.

## Resolve coverage and intended use

- Decide explicitly whether the source aids search or governs validation. Shape and descriptive richness do not settle authority. Labels/synonyms can omit valid identifiers. Do not silently turn its search results into an allowlist.
- Time coverage: a current edition covers its published scope and period. A historical union can retain retired identifiers. Coverage of user records does not establish coverage of every issued identifier.
- Check whether retired identifiers must remain searchable. If historical labels are required, find a source containing them. Do not infer past meanings or historical completeness from the latest edition.
- Record unresolved source/coverage choices as questions in the plan. Ask one consequential domain question at a time. Reuse settled decisions across phases.

## Trace transformation semantics

1. Preserve purpose. An incomplete viewing snapshot does not imply backup restoration or an editable record. Add completeness rules, editing locks, or frontend work only for an agreed need.
2. Trace the active exporter/builder from source storage to output paths. Record consequential filters, identity substitutions, version mappings, and losses. Keep requested mapping explanations short. Mapping documentation needs no separate implementation phase.
3. For a clone's exporter, derive routine inverse mappings from code. Ask only about consequential ambiguity. Explain any many-to-one loss once. Never claim an exact inverse after information loss.
4. Inspect receiving storage, migrations, and read APIs separately from create/edit DTOs. Authoring may require more than the snapshot read path. Distinguish absence, partial values, and inconsistent relationships. Check nullability and supported precision before choosing defaults.
5. Preserve absent facts unless the owner expressly permits normalization. Distinguish generated technical IDs from supplied facts. Encode and test the exact approved normalization rule, including its limits. Accept approved representations. Stop re-proposing unapproved alternatives. A partial-value default grants no authority to populate a wholly absent value or other missing components.
6. Reject or represent inconsistent input per the agreed contract. Preserve supplied facts and report partial imports as partial. Check safe parsing, assignment, and persistence separately from product completeness.

Load [Replacement-import planning](replacement-imports.md) for protected ownership, document-local ID remapping, full replacement, or restoration of processed imports. Keep source-derived findings distinct from execution-verified behavior.

## Match catalog behavior to the existing input

1. Trace live call site, bound state, persistence/output, API, and tests. Exclude commented/removed interfaces and superseded plans. Follow limits, truncation, normalization, and downstream matches. A full display identifier can become a prefix or another effective query.
2. Resolve multi-code results against the existing input before choosing controls. Distinguish individual selection from individual submission. Explain collapsed inputs before submission. Do not promise independent exact queries for merged values.
3. Guard broad results and page-only actions against unintended submission. Preserve selection across filtering/pagination when in scope. Derive controls and feedback from the agreed interaction. No fixed widget or counter layout is required.
4. For bounded clients, define server-side result limits, request timing, response size, and failure behavior. Server capacity alone does not justify sending a full catalog to the browser.
5. Keep manual input when lookup is optional. Bind acceptance to the actual submitted value and persisted result. The displayed label alone is insufficient.

## Plan a reproducible load path

- Bulk data outside Git: include a repeatable atomic importer, versioned schema, small synthetic tests, and short instructions with real import and verification commands. Keep mostly static loads opt-in and outside routine startup. Database-backed search needs a reproducible population path.
- Check existing import logic and repository methods before proposing a replacement. Name producer repository and consuming runtime separately.
- Operator entrypoint: load [Operator script acceptance](operator-script-acceptance.md). Keep build, execution, and verification within accepted scope.

## Optional data features

- Configuration: define one authoritative enable flag and its default. Trace the value into each consumer. Prevent accidental new datastore dependencies in existing installations.
- When disabled, require no optional datastore, connection attempt, migration, import, or dependent UI. Verify the original workflow. Keep disablement separate from data deletion.
- Enabled but unavailable: preserve the core application for optional features. Show a lightweight unavailable state, log the cause for operators, and allow recovery without restart. Distinguish temporary outage from intentional disablement. Choose presentation from accepted interaction requirements without prescribing a tooltip or control.
- Verify failure containment through application behavior. Distinguish per-database dumps from cluster/volume backups. A separate datastore still shares CPU, memory, storage, and backup costs.

## Verification boundary

- Use synthetic cases for relevant format variants, coverage limits, transformation losses, normalization exceptions, effective queries, and disabled/unavailable paths. Tie checks to accepted requirements or concrete changed-code risks.
- Retain independent review and all required real-operation gates. Label planned imports, source inspection, parser tests, and end-to-end runs separately.
- Keep project mappings and decisions in the existing approved plan or task. Do not add a discovery report or acceptance framework.
