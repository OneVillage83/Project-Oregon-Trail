# Test strategy and definition of done

Version 0.2 | Owner: QA lead

## Evidence categories

Specification coverage means a requirement has an owner, architecture and acceptance scenario. Contract validation means machine-readable examples satisfy or intentionally violate a schema/semantic rule. Runtime correctness means implemented behavior passed tests. Device qualification means a particular build ran on identified hardware. Playtest evidence means people completed/understood tasks. These categories are not interchangeable.

This package contains specifications and contract-validation tooling. It does not contain a gameplay implementation or passing gameplay/model/device benchmarks. See [implementation status](../../project-control/IMPLEMENTATION_STATUS.json) and [validation report](../../project-control/VALIDATION_REPORT.md).

## Test layers

| Layer | Required coverage |
|---|---|
| Static/contract | JSON validity, strict schemas, operation parameters, references, links, requirement mapping |
| Unit | Checked quantities, IDs, geometry predicates, individual reducers, rounding and RNG vectors |
| Property/invariant | Conservation, idempotency, no containment cycles, no duplicated identities, bounded planning |
| Integration | Shared operations across player/NPC/menu/text, cross-domain causality, projection isolation |
| Replay | Snapshot/command or effect replay, hashes, equal-time ordering, cross-build comparison |
| Persistence/fault | Termination, disk-full, corrupt files, migration interruption, backup and rollback |
| Language | Held-out semantics, ambiguity, constraints, grounding and unsupported capability handling |
| Content | Dependencies, prototype/process/asset/localization coverage, licenses and compatibility |
| Performance/device | Frame latency, scheduler/inference costs, memory, thermal/suspension and package behavior |
| Human | Discoverability, alternative solutions, trust, pacing, accessibility and long-time agency |

## Scenario governance

The [acceptance catalog](SCENARIO_ACCEPTANCE_CATALOG.md) names fixtures, attempted behavior and required assertions. Each implemented test records requirement IDs, seed/input, rules/content/model versions, expected events/invariants and evidence location. Planned scenarios remain planned until results exist. A model-generated successful narrative is never a test oracle for world state.

Use authored golden fixtures for regressions and seeded variants for generalization. Test metamorphic properties: rephrasing a command should preserve normalized semantics; changing observer should affect knowledge, not world truth; canceling inference should not consume time/resources; changing render framerate should not change results.

## Language and uncertainty

Score complete semantic correctness and field-level errors separately. Split data by scenario/template family. Keep held-out tests out of fine-tuning and prompt optimization. Report sample counts and confidence intervals; zero observed failures in a finite suite is not proof of zero possible failures. Any known silently executed critical target, authority or budget error blocks qualification.

## CI tiers

Every PR: history coverage, architecture/schema/fixture checks, later unit and small integration tests. Scheduled/release candidates: wider seeds, sanitizers/fuzzing, save/migration fixtures, deterministic compiler matrix and content coverage. Dedicated machines: local-model, GPU/mobile, thermal and sustained-play tests. Human reviews: gameplay/editorial/accessibility and distribution.

Do not add fake passing jobs for unimplemented systems. A skipped required release test is an open gate. Failure artifacts must preserve reproducibility without uploading private player data by default.

## Definition of done

A feature has a reviewed contract; implementation with bounded failure behavior; positive, negative and invariant tests; observer-safe UI/audio/accessibility; correct save/migration behavior; content/state coverage; useful diagnostics; updated documentation and append-only run history. A public release also requires approved scope, supported device matrix, license/notices, recovery/support and external playtesting.

Critical blockers include corrupted saves, unauthorized state mutation, hidden-information leaks in normal interfaces, duplicate resource transfers, unresolved deterministic divergence in promised configurations and misleading distribution claims. Cosmetic defects are prioritized separately but may still block usability.
