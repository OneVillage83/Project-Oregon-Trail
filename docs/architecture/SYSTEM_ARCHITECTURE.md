# System architecture and ownership boundaries

Version 0.2 | Implementation specification | Owner: technical lead

## Deployment shape

One local game application contains a presentation client, a native simulation library, local persistence and replaceable language adapters. Development tools can run headlessly against the same contracts. No cloud account, vector service, orchestration platform or external model server is required for baseline play. Optional diagnostics exports remain outside the simulation authority boundary.

The production default is Godot 4.x presentation with typed GDScript, a C++20 core, a thin GDExtension bridge and SQLite saves, pending G-2 qualification. Pin exact engine, bindings, compiler, runtime and database revisions in the build manifest when tested. See [native bridge](NATIVE_BRIDGE_AND_BUILD.md) and verified external [sources](../references/VERIFIED_TECHNICAL_SOURCES.md).

## Data flow

```text
Text / selected object / menus / optional local speech
  -> observer-scoped InputContext
  -> interpreter or deterministic input adapter
  -> canonical WALang Intent
  -> schema, semantic, reference and authority validation
  -> preview or clarification when material
  -> execution plan, resource reservations and scheduler
  -> simulation domain operations
  -> atomic committed event/state batch
  -> knowledge and presentation projections
  -> UI, scene, journal, permitted dialogue and narration
```

The model does not receive a database handle. The renderer does not receive an omniscient WorldState. A UI button does not mutate an inventory node directly. NPC goals also enter the shared operation framework.

## Module ownership

| Module | Owns | May consume | Must not do |
|---|---|---|---|
| Kernel | IDs, authoritative entities, clocks, transactions, RNG, scheduler | Validated plans and domain reducers | Depend on scene nodes, wall-clock time or model text |
| Domain systems | Rules and typed event proposals in their namespace | Stable world read view, owned components, authorized requests | Mutate another domain through hidden side effects |
| Knowledge | Actor observations, beliefs, provenance, disclosure rules | Committed facts and sensory/communication rules | Turn a rumor into truth |
| Planner | Bounded decomposition, dependencies, reservations, execution status | Actor knowledge, supported capabilities, authority | Invent missing operations or search without budgets |
| Persistence | Durable snapshots, event batches, manifests, migrations | Kernel commit batches and consistent snapshots | Rewrite gameplay rules during deserialization |
| Client | Input state, selection, layout, scene/audio presentation | ObserverView, PlanPreview, ActionReceipt | Infer secret state from internal IDs or omitted fields |
| Language | Proposed intent and wording | Minimal permitted context and schemas | Call shell, filesystem, network, or state setters |
| Content compiler | Validated prototypes/processes/scenes/localized data | Authored packs and schemas | Execute arbitrary mod code in the default trust tier |
| Diagnostics | Traces, hashes, metrics, export bundles | Redacted public traces; privileged developer traces in dev mode | Upload by default or leak private world facts into play |

## Commands, events and transactions

Intent means requested behavior. Plan means an executable schedule after validation. Event means a committed occurrence. These are different types and stored separately. Synchronous domain subscribers must have a specified order; cross-domain effects enter scheduled commands/events, not recursive unbounded callbacks.

One simulation owner commits an ordered batch: verify preconditions, reserve/consume resources, apply domain changes, advance event sequence, update required projections and persist. Failure before durable commit publishes nothing. Long activities produce checkpoints and partial completion; canceling a project does not roll back yesterday's work.

## Read models and revisioning

ObserverView includes a view revision, observer identity, observed entities, known facts with precision/provenance, selected references, public action capabilities, and accessible text/audio hints. It excludes hidden component names and debug reasons. Cached views are keyed by world, observer, knowledge revision and location/scene revision.

An intent refers to its context revision. Materially stale or conflicting references require revalidation/preview. A stale displayed price cannot silently authorize a more expensive purchase. Queries return permitted information without advancing simulation time unless the query represents an actual examination, journey or conversation.

## Dependency rules

Kernel types have no Godot imports. Domain modules depend on kernel interfaces and explicit shared contracts, not other domains' private stores. Renderer and language depend on projections. Tools depend on the same content and simulation APIs used by the game. A service locator that exposes unrestricted world mutation to all modules is forbidden.

## Cross-cutting requirements

Determinism, versioned saves, bounded execution, observer isolation, accessibility, content provenance and diagnostics are part of each subsystem definition. Future technology adds data and rule families without replacing the action language or entity identity model. Mobile may change visual/model fidelity; it may not silently change the rules of an existing save.

## Verification

Architecture tests inspect module dependencies. Integration scenarios submit the same intent through text/menu/NPC pathways and compare outcomes. Tests deliberately crash inference, invalidate UI caches, resume a save mid-task and send an unauthorized target reference. Any alternate world implementation inside a client or chatbot is a release-blocking divergence.
