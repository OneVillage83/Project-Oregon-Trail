# Native bridge and build architecture

Version 0.2 | Owner: technical/build lead

## Stack qualification

Godot presentation with standalone C++20 simulation is the working design. GDExtension is an official native path with platform-specific builds and compatible bindings; source S-007 documents the workflow. G-2 proves engine/binding/compiler compatibility, debugging, headless execution, installer and early mobile packaging. Desktop compilation alone does not prove portability.

Keep one production core. A bounded alternative spike is justified only by a failed gate or demonstrated maintenance concern, with its decision logged.

## Planned source layout

```text
apps/godot/             presentation and typed UI scripts
native/core/            engine-independent entities, time and transactions
native/domains/         domain rules and reducers
native/godot_bridge/    thin native binding
native/inference/       replaceable runtime adapters
native/persistence/     database, backup and migration implementation
tools/                  inspectors, compiler and evaluation harnesses
content/                authored packs and manifests
contracts/              versioned wire/content contracts
tests/                  unit, property, integration, replay and devices
docs/                   specifications and production plans
project-control/        history, status and evidence
```

These are future game-source directories. This package adds architecture, contracts and validation tooling, not an implemented game client/core.

## Bridge API

Use coarse calls: create/load world; get_observer_view(observer, known_revision); submit_intent(bound_session, intent); accept/cancel plan; advance_until(horizon, interruption_policy, work_budget); save/export a consistent boundary; poll public events; and privileged developer diagnostics in explicit developer mode.

Messages have versions, bounded sizes and ownership rules. Do not cross the native boundary once per component per frame. Convert C++ exceptions into typed infrastructure errors; do not allow exceptions across an ABI. Use lifetime-checked opaque handles. Expose no arbitrary mutable entity pointers or general-purpose set-property API to UI scripts.

## Concurrency and resource safety

Godot scene changes remain on the proper client thread. The core has one authoritative writer. Inference and heavy preparation use immutable inputs and return revision/cancellation-tagged proposals. Join workers and release resources during shutdown. Define native/engine object ownership to avoid cycles and use-after-free.

Bound queues and apply backpressure. Superseded cosmetic updates may be coalesced; committed events and save receipts may not be dropped. Use static analysis, sanitizers where supported and fuzz tests at save/contract boundaries.

## Builds and manifests

G-2 produces a headless executable, native extension, minimal Godot client, content compiler skeleton and model-evaluation harness. Select core build tooling and binding-compatible packaging deliberately; the official Godot example uses SCons. Pin tested engine, bindings, compiler, dependency and runtime revisions; never float release dependencies on main/master.

A build manifest records source/dirty state, toolchain, target architecture, compile flags, dependency hashes, rules/schema versions and content/model hashes. Build packages in clean environments. Release credentials and signing material belong in approved release infrastructure, not source or logs.

## CI progression

Current architecture CI validates documents and the contract seed. Future jobs add compiler matrix, native unit/property tests, deterministic golden fixtures, sanitizers/fuzzing, content compilation, headless integration, package smoke tests and migrations. Large model evaluation runs separately with licensed pinned weights and identified hardware.

Required branch-check enforcement is a repository setting; adding a workflow does not enable it automatically. Signing, platform credentials and device access remain separate release prerequisites.

## Feasibility evidence

Display a real core ObserverView in Godot, submit a structured operation, commit/save/reload it, connect a local parser and cancel it without freezing the UI. Record memory, latency and failures. Missing physical device tests are explicitly not run, leaving that qualification open. A fake UI-only world is not acceptable evidence.
