# Replacement-import planning

Use when external records create local aggregates that later imports replace completely.
Also use the restoration section when processing of an accepted import must be undone.
These are planning and acceptance rules, not evidence that an importer or reset has run.

## Submission, identity, and protected ownership

1. Trace document origin, actual submitting actor, endpoint, and stored aggregate.
   External file origin does not imply machine-to-machine submission.
   Reuse existing session and role checks for an internal upload unless another access model is requested.
   Verify backend authority separately from the user-facing role name.
2. Distinguish the source key, local aggregate ID, stable visible identity, and nested object IDs.
   Establish whether source keys are global or source-scoped from the sender contract.
   Do not infer uniqueness from UUID-like syntax.
   Agree which identities survive reimport before selecting deletion behavior.
3. Resolve replacement targets only through the importer-owned mapping.
   Check that protected provenance agrees with the expected local identity or namespace.
   Abort without mutation on disagreement.
   Never select a deletion target from supplied IDs, names, business identifiers, or a matching prefix alone.
4. Keep the stable mapping and visible identity outside the replaceable payload.
   Protect uniqueness and concurrent access.
   Prove that a forged payload cannot nominate an internally created record.
   Do not silently repair inconsistent ownership during import.

For source formats, export losses, receiving read contracts, and normalization decisions,
load [External-data discovery](data-discovery.md#trace-transformation-semantics).
Keep absent facts empty unless the owner expressly permits normalization.
Encode the exact permitted exception without inventing unrelated values or precision.
Do not infer authorization decisions or completed workflow states to satisfy authoring DTOs.
Optional absent groups are not inconsistent relationships.

## Document-local identity graph

When external IDs need not be retained, allocate local IDs through a schema-aware map
keyed by object kind and source ID.
Inventory foreign keys, join tables, parent/history links, and nested JSON references.
Preserve domain codes and external terminology identifiers.
Do not rewrite every UUID-looking string or perform global string replacement.

For ORM-generated IDs, distinguish entity identity from nested JSON-object identity.
Obtain actual managed entity IDs through the supported persistence path before finalizing references.
Test save/merge behavior rather than assuming manually assigned generated IDs are accepted.
Never resolve an unknown imported reference by searching existing application records.
Specify the response to duplicate, ambiguous, or unresolved references before mutation.
Under agreed strict rejection, fail the whole import and preserve the prior snapshot.

## Replacement and atomicity

Choose deletion from the required active-state outcome.
A complete snapshot replaces the old content; it does not require every possible section.
An omitted section or scalar must disappear from active reads rather than retain its old value.

1. Prefer existing soft-delete behavior if it satisfies the contract and physical erasure is not required.
   Do not build annotation bypasses or purge infrastructure to preserve an obsolete proposal.
   Inspect deletion filters, global business-key uniqueness, incoming references, cycles, and unenforced links.
2. If deletion leaves a unique key occupied, consider preserving the stable identity row.
   Replace its entire mutable payload and active child snapshot.
   Do not use null-ignoring patch mapping for full replacement.
3. Load the complete old active child inventory before deactivating parents whose filters hide those children.
   Deactivate children themselves if removing only their parent leaves them readable.
   Replace parent-scoped records as well as direct fields.
   Use ordinary repository deletion for owned records without soft-delete where appropriate.
4. Preserve shared dictionaries and unrelated records.
   If physical erasure is required, include historical soft-deleted owned rows.
   Verify physical removal independently of filtered application reads.
   Do not add retention or history-browsing features merely because archived rows remain.
5. Honor the agreed controller/service/repository and persistence boundaries.
   An existing native-query helper does not authorize bypassing a repository-only contract.
6. Keep ownership recheck, old-state deactivation, payload clearing, new snapshot creation,
   and mapping update in one transaction on the actual target datasource.
   Identify filesystem and external effects separately; database rollback does not undo them.
   Avoid unrelated authoring notifications, schedulers, and outbound transfers.

## Minimum acceptance matrix

Use synthetic data and an isolated mutation target.
Verify that the existing harness supplies required migrations, views, foreign keys, and sequences.
Copied tables alone do not prove a view-backed read path.
Use the smallest faithful setup instead of redesigning the shared framework.
Keep setup marked planned until executed.

| Scenario | Required observable result |
| --- | --- |
| First import | One mapping and one visible aggregate; supported supplied data are readable. |
| Same source key again | Agreed identity survives; only the new snapshot is active. |
| Omitted former group, scalar, or parent-scoped record | No stale current content through any relevant active read. |
| Same nested IDs in different source records | Independent local identities; no cross-record attachment or overwrite. |
| Payload supplies an internal ID | No replacement of or attachment to an internally created record through that ID. |
| Mapping disagrees with expected identity | Atomic rejection without deletion, reassignment, or silent repair. |
| Failure after deactivation or clearing | Prior committed fields, children, parent-scoped records, and mapping survive rollback. |
| Concurrent first imports or reimports | No duplicate mapping, unstable visible identity, partial aggregate, or unsafe interleaving. |
| Optional groups absent or values partially supplied | Apply the agreed representation policy; no fabricated completeness. |
| Duplicate IDs or unresolved relationships | Apply the agreed rejection policy atomically; no silent skip or existing-record fallback. |

Distinguish allowed archived rows from forbidden active leftovers.
Assert physical removal only when the contract requires it.
Test the agreed viewing path rather than adding a new UI or lifecycle platform.
Keep migrations, implementation commits, and independent review in their actual repository boundaries.

## Restoring previously accepted imports

Use when reset or reassignment must undo processing, not accept a new snapshot.

1. Trace parsing, mapping, processing, persistence, and downstream export.
   Identify each mutated field path, its save point, and an available original source.
   Inspect nested setters and ORM dirty checking as well as top-level assignments.
   Distinguish detached export copies from managed import records.
2. Separate association removal, reversal of overrides, and recovery of original source values.
   A later processing pass that might overwrite current values is not full restoration.
   Matching setters support a reuse hypothesis, not proof of recovery or future compatibility.
3. Classify field ownership before choosing reconstruction.
   An overwritten field cannot reveal its original value or original absence without retained history.
   Use an original file or immutable snapshot when original facts must be recovered.
   A new snapshot column cannot restore already-lost legacy values.
4. If the owner identifies processing-owned system fields and accepts discarding their legacy values,
   reset only the explicit leaf-field allowlist.
   Do not require source reconstruction or speculative age/version gates for that policy.
   Distinguish null from importer defaults such as false or an empty string.
   Preserve measurements, sibling values, list order, and entries outside owned positions.
   Check the allowlist against actual processing setters, excluding container-creation setters.
   Fresh nested IDs alone do not require rereading a source file.
5. Separate reconstruction from new-upload admission.
   A previously accepted file can fail today's mandatory-field or supported-version rules.
   Define a bounded compatibility policy that retains structural readability, safe interpretation,
   relationship consistency, and atomic failure.
   Do not blindly call current upload validation or disable all validation.
   Keep new-upload rules unchanged unless separately authorized.
   Report an uninterpretable original format as an unresolved recovery boundary.
6. Protect historical objects before clearing associations or renewing identities.
   Deep-copy shared mutable data where needed.
   Capture old result IDs before renewal so reprocessing cannot restore removed links.
   Do not mutate archived results through shared nested objects.

Test the selected policy rather than a superseded one:

- For reconstruction, cover overwritten source values, processing-created nested objects,
  and a previously accepted fixture rejected by current upload admission.
- For an approved system-field reset, assert the exact allowlist and preserved sibling sentinels.
  Prove reset without source-file access.
  Remove superseded parser work and file/admission error responses from the plan and tests.
- For either path, cover changed processing configuration/type, null or empty nested data,
  protected history, and rollback after failure.

Keep routine regressions synthetic.
Any real-source acceptance requires the authorization below.
A design clarification does not itself approve execution.

## Authorized local source-data acceptance

Use when the owner supplies operational files or a populated local test database.
Source permission is separate from plan approval, implementation dispatch, and mutation permission.

1. Record the permitted source, purpose, local service, and credential location without secret values.
   Inspect metadata first and count allowed file types without exposing identifying filenames.
   Label facts as owner-provided, metadata-verified, database-verified, or execution-verified.
   File presence does not prove a matching import or completed historical job.
2. Bind the scenario to actor, entrypoint, and persisted state.
   Resolve an ordinary restriction separately from a privileged exception.
   Verify each with the correct role and existing separation-of-duty rules.
   A disabled control alone is not server-side enforcement or authority for new UI work.
3. Inspect only necessary source fields and narrow database projections under the granted permission.
   Keep real identifier/filename mappings in protected local storage.
   Use neutral case aliases in shared artifacts.
   Verify required associations and historical states instead of assuming them.
   Label synthetic prerequisite setup as synthetic rather than an exercised operational case.
4. Preserve supplied originals and use a separately scoped local test target.
   Mutate the populated source database only when expressly authorized.
   Copy only the minimum authorized related data; a sample-file grant is not a whole-database export grant.
   Clarify unbounded data needs before copying.
   Do not run automatic migrations, cleanup, volume deletion, or schedulers against the source.
5. Define the finite workflow, postconditions, and stop boundary before execution.
   Compare prior/current active records, preserved source values, regenerated processing fields,
   protected history, and actual workflow state.
   Success of the last processing step does not prove earlier gates.
   If external submission is excluded, disable outbound clients and jobs.
   Verify no new submission jobs or external calls with before/after inventory and mock-call assertions.
   Do not transmit test data to prove readiness.
6. Read credentials locally only when needed for the next authorized operation.
   Keep source content and credentials out of Git, chat, delegates, task attachments, memory, and reusable fixtures.
   Protect necessary local copies and clean only owned test resources.
   Report the exact code commit, neutral alias, source/target mode, assertions, and gaps on the existing task.
   Directory inventory or connectivity is not end-to-end acceptance.
   Retain independent review and separate execution/publication gates.

## Schema-only confirmation on an authorized local database

Use only when catalog evidence can settle a storage question left open by source inspection.
Read no application records and run no import or migration during planning.

1. Resolve the exact local database service and target from authorized configuration.
   Parse resolved Compose configuration locally; emit only an explicit metadata allowlist.
   Verify the Docker endpoint before querying.
2. Use the existing database client rather than installing host dependencies for a catalog read.
   Supply credentials through the authorized mechanism without printing them.
   For PostgreSQL, enforce read-only operation and stop on SQL errors.
3. Use a read-only transaction with a bounded statement timeout.
   Query only required catalog definitions for nullability, types, and incoming foreign keys.
   For PostgreSQL, use filtered `information_schema.columns` and `pg_constraint` queries
   with `pg_get_constraintdef(oid)`, then `ROLLBACK`.
   Do not treat catalog evidence as importer execution, rollback testing, or application-read verification.

Keep concrete entity maps, table lists, protected source locations, and approved defaults
in the project's existing authorized records, not this reusable reference.
Keep technical recommendations proposed until their design gate is satisfied.
Selecting authentication does not authorize credential provisioning or deployment.
