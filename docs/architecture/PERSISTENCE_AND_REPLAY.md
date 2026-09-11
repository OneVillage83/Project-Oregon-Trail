# Persistence, recovery, replay and migrations

Version 0.2 | Owner: persistence/release lead

## Storage decision

Use one local SQLite database per campaign as the working default, subject to G-2/G-3 testing. Keep authoritative state in memory between commits with transactionally consistent persistence. SQLite supplies atomic-commit and backup mechanisms; application crash, corruption, disk-full and migration tests remain necessary. See S-004/S-005 in the [source register](../references/VERIFIED_TECHNICAL_SOURCES.md).

WALang means World Action Language. SQLite WAL means write-ahead logging. Select and test journal/synchronous settings rather than assuming defaults satisfy durability goals.

## Logical records

| Record | Required contents |
|---|---|
| Campaign manifest | World ID/seed, generator/rules/save versions, content hashes, fidelity policy |
| Entities/components | Stable identity, revisions, locations, lifecycle and state |
| Accepted intents/plans | Normalized request, authority limits, dependencies and status |
| Schedules/reservations | Due time, stable ordering, progress and resource claims |
| Events/effects | Ordered batch, causality, typed payload/effects and checksums |
| Observations/beliefs | Actor access, sources, precision, time and contradictions |
| Institutions/property | Titles, contracts, offices, obligations and custody |
| History/snapshots | Significant references and consistent state at committed sequences |
| Idempotency/migrations | Request receipts, source/target versions, backup identity and progress |

These are logical records, not final SQL migrations. G-3 establishes DDL, indexes and migration tests before public save compatibility. Current inventory queries must not replay every historical event.

## Commit protocol

Validate a candidate kernel batch and invariants. Persist state, events, task progress and idempotency receipt in one transaction. Commit durably before publishing success. Retain the previous committed memory state until success is known. A disk failure must not leave the UI claiming an unsaved transfer succeeded.

User saves capture consistent boundaries. Asynchronous persistence uses immutable snapshots or serialized ownership, not racing writes. Suspension checkpoints where possible; recovery must also work when the operating system terminates the process without a callback.

## Backups and exports

Use the database backup API or a correctly closed/checkpointed copy. Do not copy only a live database while omitting required journal files. A portable save contains a manifest, checksums, consistent database and content references. Validate extracted paths, size limits, checksums and schemas before loading.

Keep rotating recovery slots plus manual saves. Never migrate the only valid copy. Validate the newest slot at startup and offer recovery with an explicit potentially lost-progress boundary. Do not silently replace a damaged campaign with a new world.

## Replay and retention

Exact replay consumes a snapshot plus normalized accepted commands and pinned rules/content, or applies committed versioned effect batches through a compatible projector. Declare which mode a replay tool uses. Narrative summaries alone cannot reproduce state. Replay never calls a language model or updated generator.

Keep a bounded exact-debug window and permanent consequential history. Compact routine detail only after a validated snapshot and recorded retention boundary. Exact replay before that boundary requires archived segments and compatible versions. Save manifests identify the oldest replayable event/time. Summaries supplement retained facts; they do not overwrite provenance.

## Versioning and migrations

Separate wire schema, save schema, generator, rules, content, projection and runtime versions. Changing a language model does not itself migrate world state. New rules/materials may need a compatibility policy. Unsupported future saves fail safely.

Migrate a copy, record source/target, execute transactional steps, validate accounting and representative queries, then promote it. Interrupted migrations retain the original or a recoverable copy. Test supported upgrades and document downgrade limitations. Cross-version exact simulation reproduction is not automatic.

## Acceptance

SC-SAVE covers termination before/during/after commit, disk-full, truncated exports, checksum mismatch, active-plan reload, duplicate retries, backup restoration and interrupted migration. SC-REPLAY compares hashes across qualified builds and identifies the first divergent event. Retain fixtures for every public save version. Installing SQLite does not count as passing these tests.
