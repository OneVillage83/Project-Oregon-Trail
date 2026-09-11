# Implementation backlog and developer handoff

Version 0.2 | Game implementation is unstarted unless linked evidence says otherwise

## Issue contract

Each work package becomes a bounded issue/PR with requirement IDs, dependencies, owner role, API changes, positive/negative fixtures, persistence/projection implications and actual validation. Documents do not complete runtime work. UI and language demos must use the real core, not parallel fake state. Update [run history](../../project-control/RUN_HISTORY.jsonl) with every meaningful change.

## Work packages

| ID | Package | Depends on | Deliverable / acceptance |
|---|---|---|---|
| B-001 | Core build and checked quantities/IDs | G-0 review | Headless target, units/overflow, stable-ID tests |
| B-002 | Intent decoder/operation registry | B-001 | Bounded strict input, typed parameters, unsupported-operation errors |
| B-003 | Entity/components/containment | B-001 | Revisions, tombstones, acyclic containment, quantity conservation |
| B-004 | Godot/native bridge spike | B-001/B-002 | Real core view/action, typed errors and responsive UI |
| B-005 | Save/backup/migration spike | B-001/B-003 | Consistent boundary and interrupted-write recovery |
| B-006 | Gemma/runtime evaluation harness | B-002 | Pinned artifacts, held-out semantics and measured memory/latency |
| B-007 | Clock/RNG/event kernel | B-001/B-003/B-005 | Golden vectors, atomic events/state and hashes |
| B-008 | Plans/reservations/idempotency | B-002/B-007 | Shared-tool conflicts, partial work, duplicate/cancel/fallback |
| B-009 | Knowledge/observer projection | B-003/B-007 | Facts versus beliefs, scoped tokens, cache/no-leak tests |
| B-010 | Spatial generation/commitments | B-003/B-007 | Seeded topology and exploration-order consistency |
| B-011 | Materials/affordances/physics | B-003/B-008 | Containment, support, attachments, levers, damage and displacement |
| B-012 | Client command/preview/scene | B-004/B-008/B-009 | Menu/text parity, stale-preview handling and accessible selection |
| B-013 | Travel/camp/needs | B-008/B-010/B-011 | Route/time/load/fatigue with interruption and reload |
| B-014 | Trade/property/quotes | B-003/B-008 | Atomic barter, budget/currency and custody/title tests |
| B-015 | Crafting/work orders | B-008/B-011/B-014 | Stages, labor/tools, waste, salvage and persistent progress |
| B-016 | Integrated crossing | B-012/B-013/B-014/B-015 | Three causal alternatives without bespoke success verbs |
| B-017 | Perception/skill progression | B-009/B-012 | Domain-specific detection, no toggle farming, practice provenance |
| B-018 | Evidence/case causality | B-010/B-011/B-017 | Precommitted traces, contamination and unsupported accusation |
| B-019 | NPC plans/communication | B-008/B-009/B-014 | Bounded plans, refusal, delivery/knowledge and commitments |
| B-020 | Production language integration | B-006/B-012/B-019 | Grounding, cancellation, bounded retries and offline package |
| B-021 | Integrated investigator arc | B-018/B-019/B-020 | Case outcome, communicated reputation and new request |
| B-022 | Weather/ecology/health | B-007/B-010/B-013/B-019 | Exposure/timing, stocks/cohorts and route effects |
| B-023 | Regional economy/logistics/fidelity | B-014/B-015/B-019/B-022 | Boundary ledger, shortage chain and transition invariants |
| B-024 | Law/conflict/institutions/education | B-018/B-019/B-023 | Authority, jurisdictions, budgets, shared conflict rules and learning |
| B-025 | Technology/service infrastructure | B-015/B-023/B-024 | Knowledge/capacity/adoption and mixed-era networks |
| B-026 | Generations/history/timeplay | B-007/B-009/B-024/B-025 | Succession, obligations, sites and interruptible advancement |
| B-027 | Changing-town/later-era proof | B-025/B-026 | Real upgrade plus later transport/material capability |
| B-028 | Content compiler/editor | Starts B-002/B-003; full coverage after B-027 | Validated packs, processes, assets, localization and safe data mods |
| B-029 | Art/audio/tutorial/localization | B-012/B-021/B-027/B-028 | State coverage and unfamiliar-player/accessibility evidence |
| B-030 | Soak/performance/devices | B-020/B-023/B-026/B-029 | Long seeded runs and real hardware/thermal/suspension reports |
| B-031 | Public-save/recovery hardening | B-005/B-030 | Compatibility corpus, migration failures and rollback |
| B-032 | Release candidate | B-029/B-030/B-031 | Approved scope, provenance, package tests and go/no-go |

Authoring tools in B-028 begin early; later dependencies describe complete coverage. G-2 combines B-004/B-005/B-006 with platform proofs. G-3 requires implemented kernel behavior, not only schema-valid files.

## First implementation PR

B-001 creates an engine-independent build/test target, checked integer quantity types, namespaced IDs and canonical serialization helpers. Reject overflow/invalid units and prevent ID reuse. Include a minimal headless entry point reporting build/schema versions. Do not add graphics, large models or unrestricted state setters.

B-002 ports the same contract fixtures into native conformance tests. Python validation is a development reference, not a required shipped interpreter. B-003 then supplies real object state for the bridge/save experiments.

## Review handoff

Each PR states implemented versus planned behavior, tests actually run and unavailable devices. Architecture changes update decisions/traceability. Human review precedes changes to foundational product constraints, public save compatibility or distribution terms.
