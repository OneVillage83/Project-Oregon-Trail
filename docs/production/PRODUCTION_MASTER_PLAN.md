# Production master plan

Version 0.2 | Planning baseline dated 2026-09-10 (America/Los_Angeles)

## Purpose and status

Build an offline-first, simulation-driven role-playing sandbox in which natural-language plans cause persistent, explainable consequences. The full destination includes emergent occupations, regional society, generations, and technological change through industrial and modern systems. The small first region is a proving ground, not a reduction of that destination.

This package specifies the production architecture and implementation gates. It does not claim that the simulation, client, models, content, or performance targets are implemented. Machine-readable contracts are an executable validation seed, not the complete universe of possible gameplay. See [implementation status](../../project-control/IMPLEMENTATION_STATUS.json).

The six original foundation documents remain the source of product intent. This package makes their boundaries implementable; it does not silently replace them. The preceding downloadable plan was advisory. This version incorporates the subsequent Gemma discussion and is the repository production baseline.

## Product thesis

The player observes a situation, chooses a goal, investigates or plans, commits time and resources, experiences consequences, and develops knowledge, relationships, abilities, and future opportunities. The simulation—not a narrative model—determines what happens. Conventional interfaces and natural language submit the same commands. Failure can be interesting, but misunderstandings and unavailable mechanics must not masquerade as simulated failure.

Worlds retain identity. A hunter can become known as an investigator through practice and communicated achievements. A bridge can acquire a name, be replaced, and remain in local history. A town can develop brick buildings, electricity, vehicles, plastics, telecommunications, and computing when its knowledge, economy, and infrastructure support them.

## Architecture in one paragraph

Use a modular local application: Godot presentation, a thin native adapter, an engine-independent C++20 simulation, transactional local persistence, and replaceable inference adapters. Godot/C++/SQLite are working stack choices subject to G-2 feasibility qualification. Gemma 4 E4B is the lead model evaluation candidate; E2B is a lower-resource candidate and 12B an enhanced-PC candidate. `llama.cpp` is a runtime candidate, not a requirement to use Meta Llama. No specific checkpoint, quantization, minimum device, or performance claim is approved by writing this plan.

## Production tracks

| Track | Responsibilities | Earliest proof |
|---|---|---|
| Simulation | Objects, material functions, actions, time, events, knowledge, saves | Headless command changes state and survives reload |
| Player experience | Persistent command input, readable consequences, management, Perception Mode | A new player completes the crossing without developer guidance |
| World systems | Health, ecology, economy, society, law, institutions, technology, history | Cross-domain causes remain consistent across time and distance |
| Language | Interpretation, clarification, constrained speech acts, narration | Held-out semantics and grounded dialogue on nominated hardware |
| Content and tools | Authoring, assets, recipes, scenes, sounds, localization, balancing | A designer adds content without adding a bespoke engine branch |
| Quality and delivery | CI, adversarial tests, soak runs, devices, migrations, distribution | Reproducible build and recovered interrupted save |

People may hold multiple roles. Role coverage is mandatory; a six-person hiring requirement is not implied.

## Build order

G-0 consolidates the specification and ownership. G-1 turns the object/affordance and action contracts into validated fixtures. G-2 tests the native bridge, save path, local model, and mobile packaging early. G-3 implements the kernel. G-4 makes the crossing playable. G-5 integrates observer-dependent evidence and NPC agency. G-6 qualifies language and offline packaging. G-7 develops regional life. G-8 proves generational and technological continuity. G-9 scales content production. G-10 hardens the product. G-11 releases and supports it.

These are evidence gates, not calendar estimates. Client prototypes, art standards, content tools, and model benchmarks run alongside kernel work after their interface dependencies exist. Do not finish a huge ontology before testing it; attach each new rule to a representative scenario.

## First integrated proof

The [Clearwater slice](VERTICAL_SLICE_SPEC.md) connects three experiences: an improvised river crossing, a hunter-led investigation, and a settlement upgrade that survives a time advance. It requires several materially different solutions, justified observations, resource accounting, physical state, local history, and reproducible saves. A scripted successful cutscene does not satisfy any of these gates.

## Scope discipline

All major future systems have domain owners and integration boundaries now. More detailed balancing tables and content packs arrive with implementation. Unsupported operations must be reported explicitly, not invented by AI. The architectural destination is not a promise that every feature appears in an early demo. A public release ceiling, setting, title, rating, and business model require product approval before store claims.

Multiplayer is not in the initial execution plan. Preserve authoritative command boundaries and portable saves without paying for multiplayer replication, matchmaking, servers, or anti-cheat before a separate decision.

## Completion criteria

A feature is complete only when its contract, implementation, scenario tests, observer-safe presentation, save/migration behavior, content coverage, diagnostics, and timestamped run-history record are present. A document can be complete as a specification while its feature remains unimplemented. Metrics must separate design targets from actual measurements.

## Navigation

Read [requirements](PRODUCT_REQUIREMENTS.md), [roadmap](DELIVERY_ROADMAP.md), [backlog](IMPLEMENTATION_BACKLOG.md), [system architecture](../architecture/SYSTEM_ARCHITECTURE.md), and [test strategy](../quality/TEST_STRATEGY.md). Track unresolved decisions in [decisions and risks](DECISIONS_AND_RISKS.md). The [documentation index](../README.md) lists every subsystem.
