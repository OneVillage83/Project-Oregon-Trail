# World generation, spatial hierarchy and simulation fidelity

Version 0.2 | Owner: world-systems lead

## Representation

The campaign exists independently of discovery. Use World → Region → LocalArea → Scene → Entity partitions. Terrain, watershed topology, resources, routes and settlement identities derive from a pinned seed and generator version. Mutable state and consequential generated commitments are persisted separately. Re-running a new generator against an old save is not a migration.

Geometry uses explicit coordinate systems, region boundaries and integer units. Local scenes have transforms into their local areas. Direction, orientation and upstream/downstream relationships come from shared spatial data. The renderer may simplify detail but cannot reverse a river or relocate an actionable door.

## Generation pipeline

Generate elevation/climate and drainage, resource/ecology baselines, settlement/territory suitability, route networks, initial population/institutions and provenance in deterministic stage order. Validate connectivity, reachability, building constraints and starting resources. Reject a failed campaign candidate with a bounded retry policy rather than looping forever.

The final historical versus fictional setting is open. Test packs use fictional names and explicit assumptions. Historical geography and peoples require researched content, not procedural claims of fact.

## Lazy detail without retroactive truth

A seed can determine latent detail without rendering every object. Use independent site generators and fixed constraints. Commit any geometry, witness, ownership or route fact before an event depends on it. An investigation interior is fixed before the causal crime uses a window or passage, not after the player asks about escape routes.

Observed, materially used or historically referenced facts are pinned or represented by persistent deltas. Later generation must satisfy those commitments. Contradiction is a generation bug; do not replace prior measurements, doors or inventories silently.

## Resolution levels

Local consequential simulation retains individual entities, physical objects, task steps, evidence and spatial relationships. Regional scheduling tracks travel, deliveries, production, households, institutions and significant health/environment events. Distant aggregation tracks cohorts, stocks, demand, production capacity, migration and adoption.

Rendering detail is independent of simulation resolution. A portrait-based shop still has exact inventory. Distant named witnesses, player property and active shipments can remain individually tracked.

## Promotion and demotion

A transition records source revision, target resolution, conversion algorithm, pinned entities, before/after accounting and a commit event. Preserve quantities, ownership, obligations, identities, schedules and known facts. Named people, evidence, player property, active contracts and significant sites cannot disappear into anonymous aggregates.

Creating an individual from a cohort decrements the cohort through a deterministic identity-allocation rule. Repeated loading cannot create extra people or goods. Every region has one accounting owner. Boundary shipments exist once, with custody/location updates. Region transfer is transactional or uses a persisted pending-transfer ledger with exactly-once reconciliation.

## Determinism policy

A save records its fidelity policy. Exact replay requires the same policy, versions and accepted commands. A coarse model need not produce bit-identical individual trajectories to a different full-detail model, but transitions must satisfy invariants and declared aggregate tolerances. Device load changes processing speed and visual quality, not the authoritative policy of an existing campaign.

Offscreen catch-up integrates scheduled changes over explicit horizons and splits around consequential events. Never reroll the same drought, shipment or migration when loading a region again.

## Budgets and acceptance

World-size presets are workload choices, not verified hardware promises. Measure entity counts, schedules, transfers, memory growth and time-to-advance. Too-large saves fail compatibility checks transparently instead of discarding entities.

SC-WORLD compares exploration order, reload and deterministic generation. SC-FIDELITY tests repeated promotion/demotion, pinned entities, cohort allocation, boundary shipments and accounting. SC-CONTINUITY revisits a site after decades and verifies geography and history preservation.
