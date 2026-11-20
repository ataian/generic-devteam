# Replacement-import planning

Trigger: external records create local aggregates that later imports replace completely. For undoing processing of an accepted import, use the restoration section. These rules govern planning and acceptance. Importer/reset execution requires separate evidence.

## Submission, identity, and protected ownership

1. Trace document origin, actual submitter, endpoint, and stored aggregate. External origin does not establish machine-to-machine submission. For internal uploads, reuse existing session/role checks unless another model was requested. Verify backend authority independently of role display names.
2. Identify source key, local aggregate ID, stable visible identity, and nested object IDs separately. Determine global or source-scoped keys from the sender contract. UUID-like syntax proves no uniqueness. Agree which identities survive reimport before selecting deletion behavior.
3. Resolve replacement targets only through the importer-owned mapping. Compare protected provenance with expected local identity/namespace. On mismatch, abort without mutation or silent ownership repair. Never select a deletion target from supplied IDs, names, business identifiers, or a matching prefix alone.
4. Keep stable mapping and visible identity outside replaceable payload. Protect uniqueness and concurrent access. Prove forged input cannot nominate an internally created record.

Load [External-data discovery](data-discovery.md#trace-transformation-semantics) for formats, export losses, receiving read contracts, and normalization. Leave absent facts empty unless expressly authorized. Encode only the permitted exception, without unrelated values or precision. Do not infer authorization or completed workflow states to satisfy authoring DTOs. Distinguish optional absent groups from inconsistent relationships.

## Document-local identity graph

1. If external IDs need not survive, allocate local IDs with a schema-aware map keyed by object kind and source ID. Inventory foreign keys, join tables, parent/history links, and nested JSON references. Preserve domain codes and external terminology IDs. Avoid blanket UUID rewriting and global string substitution.
2. With ORM-generated IDs, distinguish managed entity IDs from nested JSON-object IDs. Obtain actual managed IDs via supported persistence before finalizing references. Test save/merge. Manually assigned generated IDs may fail.
3. Before mutation, specify handling for duplicate, ambiguous, or unresolved references. Never resolve an unknown import reference against existing application records. Under agreed strict rejection, fail the whole import and preserve the prior snapshot.

## Replacement and atomicity

Choose deletion by the required active state. A complete snapshot need not supply every section. Remove omitted sections/scalars from active reads.

1. Prefer existing soft deletion when it meets the contract and physical erasure is unnecessary. Avoid annotation bypasses or purges for obsolete proposals. Inspect deletion filters, global business-key uniqueness, incoming references, cycles, and unenforced links.
2. If deletion leaves a unique key occupied, consider retaining the stable identity row. Replace its full mutable payload and active children. Full replacement cannot use null-ignoring patch mapping.
3. Inventory all old active children before deactivating parents whose filters hide them. Deactivate children still readable after parent removal. Replace parent-scoped records and direct fields. Use ordinary repository deletion for owned records without soft-delete where appropriate.
4. Preserve shared dictionaries and unrelated records. If physical erasure is required, include historical soft-deleted owned rows and verify removal independently of filtered reads. Archived rows alone do not justify retention or history-browsing features.
5. Honor controller/service/repository and persistence boundaries. A native-query helper does not override a repository-only contract.
6. In one transaction on the actual target datasource, recheck ownership, deactivate old state, clear payload, create new snapshot, and update mapping. Identify filesystem and external effects separately. Database rollback cannot undo them. Avoid unrelated authoring notifications, schedulers, and outbound transfers.

## Minimum acceptance matrix

Use synthetic data and an isolated mutation target. Verify that the existing harness supplies required migrations, views, foreign keys, and sequences. Copied tables alone cannot establish a view-backed read path. Use the smallest faithful setup without redesigning the shared framework. Leave setup planned until executed.

| Scenario | Required observable result |
| --- | --- |
| First import | One mapping and one visible aggregate. Supported supplied data are readable. |
| Same source key again | Agreed identity survives. Only the new snapshot is active. |
| Omitted former group, scalar, or parent-scoped record | No stale current content through any relevant active read. |
| Same nested IDs in different source records | Independent local identities with no cross-record attachment or overwrite. |
| Payload supplies an internal ID | No replacement of or attachment to an internally created record through that ID. |
| Mapping disagrees with expected identity | Atomic rejection without deletion, reassignment, or silent repair. |
| Failure after deactivation or clearing | Prior committed fields, children, parent-scoped records, and mapping survive rollback. |
| Concurrent first imports or reimports | No duplicate mapping, unstable visible identity, partial aggregate, or unsafe interleaving. |
| Optional groups absent or values partially supplied | Apply the agreed representation policy without fabricating completeness. |
| Duplicate IDs or unresolved relationships | Apply the agreed rejection policy atomically. Reject silent skips and existing-record fallbacks. |

Distinguish allowed archives from forbidden active leftovers. Assert physical removal only if required. Test the agreed viewing path without adding UI or a lifecycle platform. Keep migrations, implementation commits, and independent review within their actual repository boundaries.

## Restoring previously accepted imports

Trigger: reset or reassignment undoes processing without accepting a new snapshot.

1. Trace parsing, mapping, processing, persistence, and export. For each mutated field, identify path, save point, and available original source. Inspect nested setters and ORM dirty checking. Distinguish detached export copies from managed import records.
2. Separate association removal, override reversal, and original-value recovery. A later processing pass that may overwrite values cannot prove restoration. Matching setters indicate possible reuse. Prove recovery and compatibility separately.
3. Classify field ownership before reconstruction. Overwritten values/absence require retained history. Use original file or immutable snapshot when original facts are required. A new snapshot column cannot recover lost legacy facts.
4. If the owner identifies processing-owned system fields and accepts loss of legacy values, reset only the explicit leaf allowlist. Require neither source reconstruction nor speculative age/version gates. Distinguish null from defaults like false or an empty string. Preserve measurements, siblings, list order, and entries outside owned positions. Check actual processing setters, excluding container-creation setters. Fresh nested IDs alone do not require rereading source.
5. Separate reconstruction from upload admission. A previously accepted file may fail current mandatory-field/version rules. Define bounded compatibility for structural readability, safe interpretation, consistent relationships, and atomic failure. Do not blindly apply current admission or disable all validation. Keep new-upload rules unless separately authorized. Report uninterpretable originals as unresolved recovery boundaries.
6. Protect historical objects before clearing associations or renewing identities. Deep-copy shared mutable data as needed. Capture old result IDs before renewal so reprocessing cannot restore removed links. Do not mutate archived results through shared nested objects.

Test the selected policy:

- Reconstruction: overwritten source values, processing-created nested objects, and a previously accepted fixture current admission rejects.
- Approved system-field reset: exact allowlist, preserved sibling sentinels, and reset without source-file access. Remove superseded parser work and file/admission error responses from plan and tests.
- Both: changed processing configuration/type, null or empty nested data, protected history, and rollback after failure.

Keep routine regressions synthetic. Real-source acceptance requires authorization below. Design clarification grants no execution authority.

## Authorized local source-data acceptance

Trigger: owner supplies operational files or a populated local test database. Separate source permission from plan approval, implementation dispatch, and mutation permission.

1. Record permitted source, purpose, local service, and credential location without secret values. Inspect metadata first. Count allowed file types without revealing identifying filenames. Label facts owner-provided, metadata-verified, database-verified, or execution-verified. File presence proves neither matching import nor completed historical job.
2. Bind scenario to actor, entrypoint, and persisted state. Verify ordinary restrictions and privileged exceptions separately with correct roles and separation-of-duty rules. Disabled UI proves neither server enforcement nor authority for new UI work.
3. Inspect only necessary fields and narrow database projections under the grant. Keep real identifier/filename mappings in protected local storage. Use neutral aliases in shared artifacts. Verify required associations and historical states. Label synthetic prerequisite setup as synthetic.
4. Preserve originals and use a separately scoped local test target. Mutate a populated source database only with express authorization. Copy minimum authorized related data. A sample-file grant permits no whole-DB export. Clarify unbounded data needs before copying. No automatic migrations, cleanup, volume deletion, or schedulers against source.
5. Before execution, define finite workflow, postconditions, and stop boundary. Compare prior/current active records, preserved source values, regenerated processing fields, protected history, and actual workflow state. Verify earlier gates independently of the last processing step. If external submission is excluded, disable outbound clients/jobs and verify no new submission jobs or external calls via before/after inventories and mock-call assertions. Never transmit test data to prove readiness.
6. Read credentials locally only for the next authorized operation. Keep source content and credentials out of Git, chat, delegates, task attachments, memory, and reusable fixtures. Protect needed local copies and clean only owned test resources.
7. Existing task evidence: exact commit, neutral alias, source/target mode, result, and verification gaps. Directory inventory and connectivity cannot prove end-to-end acceptance. Retain independent review and separate execution/publication gates.

## Schema-only confirmation on an authorized local database

Use only if catalog evidence can settle a storage question left open by source inspection. Read no application records or run imports/migrations during planning.

1. Resolve exact local service and target from authorized configuration. Parse resolved Compose configuration locally and emit only allowlisted metadata. Verify Docker endpoint before querying.
2. Use the existing database client. Do not install host dependencies for a catalog read. Supply credentials through the authorized path without printing them. On PostgreSQL, enforce read-only mode and stop on SQL errors.
3. Use a read-only transaction and bounded statement timeout. Query only needed catalog definitions for nullability, types, and incoming foreign keys. For PostgreSQL, filter `information_schema.columns` and `pg_constraint`, use `pg_get_constraintdef(oid)`, then `ROLLBACK`. Catalog evidence cannot establish importer execution, tested rollback, or application reads.

Store concrete entity maps, table lists, protected locations, and approved defaults in existing authorized project records. Technical recommendations remain proposed until their design gate. Selecting authentication grants no credential provisioning or deployment authority.
