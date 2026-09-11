# Architecture decision records

Version 0.2 | Decision date: 2026-09-10, America/Los_Angeles

## ADR-001 — Simulation authority

Status: inherited. Keep world state, outcomes and causality in the deterministic/rule-driven core. Reject a narrative-model world engine. Consequence: more explicit domain rules and tests, but reproducible consequences and offline reliability. Revisit only through explicit product approval.

## ADR-002 — Hybrid interaction and observer projections

Status: inherited. Language, menus and selected objects enter the same intent path. Every presentation surface consumes observer-permitted data. Reject UI-direct inventory writes and omniscient context. Consequence: projection/version/cache discipline across client and AI.

## ADR-003 — Modular monolith and standalone core

Status: working design, qualify G-2. Godot client, C++20 core, thin native bridge and local SQLite. Reject mandatory cloud microservices. Native integration has maintenance costs; a failed build/device spike can justify a bounded alternative before core expansion. No alternate full implementation runs in parallel.

## ADR-004 — Model/runtime independence

Status: evaluation plan. Lead with Gemma 4 E4B, test E2B lower-resource and 12B enhanced-PC candidates. Evaluate llama.cpp desktop and an appropriate mobile runtime separately. No comparative winner, exact artifact or device performance is assumed. Revisit with held-out semantics, resource results and license provenance.

## ADR-005 — Canonical intents versus plans versus events

Status: production contract. Store requested intent, executable plan and committed events separately. Persist accepted normalized input for replay. Reject outcome fields in interpreter output. Consequence: clear validation/failure stages and safe idempotency.

## ADR-006 — Composable properties and bounded physics

Status: inherited direction, working implementation. Use components/materials/functions rather than bespoke object verbs. Implement useful bounded models, not unrestricted real-world physics. Unknown capability is explicit. New phenomena require reviewed handlers and tests.

## ADR-007 — Deterministic scheduled time

Status: working design. Integer simulation time, stable event order, specified RNG streams and checked quantities. Pause command composition/inference. No wall-clock offline progress by default. Changes require replay/version review and timeplay testing.

## ADR-008 — Lazy detail with prior commitments

Status: production clarification of foundation. Materialize details when needed, but commit any fact before an event depends on it and preserve observed/history-referenced facts. Reject retroactive crime geometry chosen to match a question. Test exploration order and event provenance.

## ADR-009 — Explicit fidelity policy

Status: production design. Local detail, regional schedules and distant aggregates share accounting and pinned identities. Save the policy. Exact replay is policy/version-scoped; coarse and detailed trajectories need not be identical but transitions preserve invariants. Hardware load cannot silently alter rules.

## ADR-010 — Durable snapshots and bounded exact replay

Status: working design, qualify G-3. Transactional state/events, recovery slots, copy-before-migrate and permanent consequential history. Compact routine detail only with a recorded replay boundary. Reject promises of unlimited exact replay after required data is deleted.

## ADR-011 — Real adoption and generational continuity

Status: inherited destination, working mechanisms. Technology requires knowledge/capacity/resources/adoption/maintenance; sites persist across reconstruction. Party/heir/institution continuation is evaluated before final UX approval. Reject global cosmetic era switches or deleting modern technologies from the architecture because the slice starts earlier.

## ADR-012 — Data-driven content and conservative mod trust

Status: working design. Validated packs and reusable rules; data-only mods by default. Arbitrary native extensions are a separately enabled developer tier, not a promised secure sandbox. Exact content versions are recorded in saves.

## ADR-013 — Evidence-based delivery

Status: production governance. Specifications, schema tests, gameplay tests, device results and human findings are distinct. Gate completion requires observed evidence. Preserve append-only UTC history, including failures. Exact stack/model/hardware and public-release scope remain unqualified until their gates.

## Amendment format

Add a new record with context, alternatives, decision/status, consequences, affected requirements, migration impact, evidence and revisit condition. Supersede older records explicitly rather than rewriting history. Update the decision/risk and run-history records in the same change set.
