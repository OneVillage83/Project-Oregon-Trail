# Decisions, assumptions, and risk register

Version 0.2 | Maintainer resolves product choices; technical lead resolves implementation within them

## Decision statuses

Inherited means explicitly established in the foundation. Working default means used to make the implementation concrete but subject to the named gate. Qualified means tested and accepted with evidence. Open means unresolved and may block a specific release decision. No model/runtime or hardware baseline is currently qualified.

| ID | Decision | Status / next resolution |
|---|---|---|
| D-001 | Simulation authority, offline baseline, perception filtering, persistent history | Inherited; changes require explicit product approval |
| D-002 | Modular 2D visuals and hybrid natural language/conventional UI | Inherited |
| D-003 | Godot client + C++20 standalone core + thin GDExtension + SQLite | Working default; qualify G-2 |
| D-004 | Gemma 4 E4B first evaluation; E2B lower resource; 12B enhanced PC | Working evaluation plan; qualify exact artifacts G-2/G-6 |
| D-005 | Desktop llama.cpp and a separately evaluated mobile runtime | Working default; runtime is independent from model family |
| D-006 | Windows first proof; mobile-aware architecture and early device build | Working default; supported devices selected from measurements |
| D-007 | Single-player first, no mandatory external services | Working default consistent with offline requirement; multiplayer requires separate scope |
| D-008 | Pause/advance; no wall-clock offline progress by default | Working default; usability review G-4/G-8 |
| D-009 | Party/heir/institution continuation mechanisms | Working design; select presentation and inheritance defaults G-8 |
| D-010 | Exact setting/start date, historical fidelity and cultural research scope | Open; product/content owner before final writing/art |
| D-011 | Audience/rating and portrayal of violence, illness and sensitive history | Open; product/content owner before public demo |
| D-012 | Final game name, price, store scope and public release era ceiling | Open; product/release owner before marketing or distribution |
| D-013 | Save compatibility horizon and archive/storage budget | Working policies in persistence; ratify before first public save format |
| D-014 | Repository/content licensing, asset/model redistribution approvals | Open for project-owned licensing; do not add a blanket license without owner approval |

## Risks and responses

| Risk | Severity | Trigger / detection | Mitigation and accountable role |
|---|---|---|---|
| Universal simulation scope outruns implementation | High | Large verb/content count with no integrated scenarios | Vertical slice and operation capability matrix; product/engineering |
| Parser silently changes quantities, targets or constraints | Critical | Held-out/field semantic failures | Preview risky actions, deterministic validation, exact limits, bounded retry; language/gameplay |
| Narrator invents evidence or commitments | Critical | Grounding suite or human review finds unsupported claims | Exact critical templates and fact bundles; no prose-to-world updates; language |
| Hidden truth leaks through UI, autocomplete or caches | Critical | Differential observer tests | Projection-only client/model inputs, access tests on all surfaces; security/gameplay |
| Cross-platform or multithread nondeterminism | High | Divergent state hashes | Stable order, specified RNG, integer/fixed-point authoritative math; simulation |
| Native integration costs exceed capacity | High | Packaging/debugging spike fails | Compare one bounded alternative before core expansion; technical lead |
| Model footprint competes with game memory/thermals | High | p95 latency/RSS/device thermal reports | Small contexts, one loaded baseline model, cancel/unload policy, device tiers; language/client |
| Fidelity transitions duplicate people or resources | Critical | Conservation/promotion/demotion fixtures | Named-entity pinning, transfer ledger, versioned aggregates; simulation |
| Save migration destroys a long campaign | Critical | Crash/migration/restore tests | Copy-before-migrate, recovery slots, version pins, rollback; persistence/release |
| Technology is only cosmetic | High | Upgrade bypasses prerequisites or visual-only fixtures | Production/adoption/maintenance chains and same-place tests; systems |
| Centuries are technically possible but boring to play | High | Timeplay tests stall or lose agency | Standing orders, meaningful interruption, summaries and succession; gameplay |
| Content combinatorics explode | High | Asset states multiply without reusable layers | Manifest-driven families, composition, state coverage before volume; technical art |
| Historical or medical content is misleading | High | Editorial review gaps | Clearly bounded game abstractions, research provenance, specialist review; content |
| Third-party license/distribution assumptions fail | High | Missing notices/artifact rights | Provenance registry and release approval; release owner |
| Tests create false confidence | High | Grammar score presented as task accuracy | Separate schema, semantic, runtime and playtest evidence; QA |

## Change discipline

Record alternatives, why one was chosen, affected requirements, migration impact and a revisit condition in [architecture decisions](../decisions/ARCHITECTURE_DECISIONS.md). An unresolved decision blocks only the work that depends on it: a fictional test fixture can exercise physics before the final historical setting is selected. It must not silently become the shipped setting.

Failed spikes, rejected models, regressions and reversions are logged. Do not fabricate passing evidence to close a gate. A draft PR can contain a complete specification without implying implementation readiness.
