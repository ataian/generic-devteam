# External-data discovery

Use when a feature depends on supplied files, reference catalogs, export mappings,
or an optional datastore. Apply only the sections required by the accepted goal.
Discovery does not authorize implementation, source copying, or target mutation.

## Establish source identity and format

1. Locate inputs through maintained import documentation and the supplied location.
   Narrow an ambiguous location with a parent-directory inventory.
   Do not search the whole home directory for a documented bulk input.
2. Read each source with its schema or README before proposing import or lookup rules.
   Confirm encoding separately for each file.
   Verify delimiters, field meanings, multiplicity, format version, and null representation.
   Compare actual shapes with current builders; historical files can use other names or cardinalities.
3. Verify canonical source identity and hashes before relying on a sample.
   Temporary mocks can have the same filename as an operational catalog.
   Keep permitted provenance in the existing plan or task, not a new evidence document.
4. Inspect sensitive content machine-side with narrowly scoped projections.
   Return only required schema-known field names, types, and collection sizes.
   Do not expose values, arbitrary dictionary keys, free text, or identifying filenames.
   Treat pseudonymized material as sensitive rather than synthetic.
5. Keep restricted source identities and case-to-filename mappings in authorized protected local storage.
   Use neutral case aliases in plans, tickets, delegated prompts, and reports.
   Use synthetic fixtures for shareable tests.
   Source-read permission does not grant database writes, exports, or implementation release.

For tests using operational files or a populated database, load
[Authorized local source-data acceptance](replacement-imports.md#authorized-local-source-data-acceptance).
A supplied directory or service address is not evidence of a matching record or successful prior job.

## Resolve coverage and intended use

Determine whether the dataset is a search aid or an authoritative validation source.
Do not derive that decision from its shape or descriptive richness.
A catalog of labels or synonyms can omit valid identifiers.
Do not silently turn its search results into an allowlist.

For time-dependent data, distinguish these coverage claims:

- A current edition describes its published scope and period.
- A historical union can retain identifiers no longer present in the current edition.
- Coverage of identifiers in the user's records is not coverage of every identifier ever issued.

Check whether retired identifiers must remain searchable.
If historical labels are required, identify a source that actually contains them.
Do not infer old meanings from current labels or promise historical completeness from the latest edition.
Put unresolved source or coverage decisions in the plan as questions, not defaults.
Ask one consequential domain question at a time.
Reuse settled decisions instead of reopening them during each phase.

## Trace transformation semantics

1. Preserve the requested purpose.
   An incomplete snapshot for viewing is not automatically a backup restore or an editable local record.
   Do not add completeness rules, editing locks, or frontend work without an agreed need.
2. Trace the active runtime exporter or builder from source storage to output paths.
   Record consequential filters, identity substitutions, version mappings, and losses.
   Keep a requested mapping explanation compact; mapping documentation is not another implementation phase.
3. If the sender uses a clone's exporter, derive routine inverse mappings from that implementation.
   Do not ask the user to reconstruct mappings already established in code.
   Explain a many-to-one loss once and resolve only the consequential ambiguity.
   Do not claim an exact inverse where the export discarded information.
4. Inspect receiving storage, migrations, and read APIs separately from create/edit DTOs.
   Authoring completeness can be stricter than the required snapshot read path.
   Distinguish absent fields, supplied partial values, and inconsistent relationships.
   Check nullability and supported precision before choosing defaults.
5. Keep absent source facts absent unless the owner expressly authorizes normalization.
   Separate generated technical identities from supplied facts.
   Encode and test the exact approved normalization rule, including its limits.
   Do not reject an approved representation or keep proposing an unapproved alternative.
   A permitted partial-value default does not authorize filling a wholly absent value or other missing components.
6. Reject or represent inconsistent input according to the agreed contract.
   Do not silently drop supplied facts or report a partial import as complete.
   Distinguish safe parsing, assignment, and persistence from product completeness validation.

For protected ownership, document-local ID remapping, full snapshot replacement,
and restoration of processed imports, load [Replacement-import planning](replacement-imports.md).
Keep source-derived conclusions separate from execution-verified behavior.

## Match catalog behavior to the existing input

Inspect the live call site, bound state, persistence/output path, API, and tests.
Exclude commented or removed interfaces and superseded plans from the current-flow description.
Trace input limits, truncation, normalization, and downstream match semantics.
A displayed full identifier can become a prefix or another effective query value.

If distinct selections collapse to the same effective input, make that consequence clear before submission.
Do not promise independent exact queries for values that the current application merges.
Resolve how multi-code results map to the existing input before choosing interaction details.
Distinguish individually selectable values from individually submitted values.
Prevent broad results or page-only actions from silently submitting unintended selections.
Preserve selection semantics across filtering or pagination when that behavior is in scope.
Choose controls and feedback from the agreed interaction contract; no fixed widget or counter layout is required.

For bounded clients, define server-side result limits, request timing, response size, and failure behavior.
Do not send the complete catalog to the browser merely because it fits on the server.
Preserve the existing manual-input path when lookup is optional assistance.
Bind acceptance to the actual submitted value and persisted result, not only the displayed label.

## Plan a reproducible load path

If bulk data must remain outside Git, include an explicit repeatable, atomic importer in the feature scope.
Version its schema and small synthetic tests.
Provide short instructions with real import and verification commands.
Keep a mostly static bulk load opt-in rather than part of ordinary application startup.
A database-backed search is incomplete without a reproducible way to populate it.

Reuse existing import logic and repository methods before proposing replacements.
Name the producing repository and consuming runtime separately.
Load [Operator script acceptance](operator-script-acceptance.md) when delivery includes an operator entrypoint.
Keep its build, execution, and verification requirements within the accepted feature boundary.

## Optional data features

Define one authoritative enable flag and its default explicitly.
Trace its configuration into each consuming process.
Do not let an existing installation accidentally acquire a new datastore dependency.

When disabled, require no optional datastore, connection attempt, migration, import, or dependent UI.
Verify that the original workflow still works.
Keep disablement separate from data deletion.

When enabled but unavailable, preserve the core application if the feature is optional.
Expose a lightweight unavailable state and log the cause for operators.
Allow recovery without an application restart.
Distinguish this temporary failure from intentional disablement.
Choose its visual treatment from the accepted interaction requirements, not a prescribed tooltip or control.

Check containment through actual application behavior rather than datastore packaging alone.
Distinguish a per-database dump from a whole-cluster or volume backup.
A separate datastore does not remove shared CPU, memory, storage, or backup costs.

## Verification boundary

Use synthetic cases to test relevant format variants, coverage limits, transformation losses,
normalization exceptions, effective query values, and disabled/unavailable behavior.
Map each check to an accepted requirement or a concrete changed-code risk.
Retain independent review and all required real-operation gates.
Label planned imports, source inspection, parser tests, and end-to-end runs separately.
Store project-specific mappings and decisions in the existing approved plan or task.
Do not add a separate discovery report or acceptance framework.
