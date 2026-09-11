# World objects, properties, materials and affordances

Version 0.2 | First implementation contract | Owner: simulation lead

## Purpose

WALang supplies verbs; this system supplies the nouns and reusable properties those verbs operate on. An object is not merely an item label or sprite. A rifle barrel can act as a lever because relevant geometry and material properties permit it, not because the engine contains a USE_RIFLE_AS_LEVER branch.

## Identity and storage

An entity has a stable namespaced ID, prototype ID/version, creation event, component revisions, lifecycle state and spatial/containment references. Never reuse an ID after destruction. Retain tombstones for referenced history. Prototypes define defaults; mutable instances store deviations and persistent components. Prototype upgrades cannot silently overwrite instance damage, ownership or history.

A component-store architecture is preferred over a deep inheritance hierarchy. Storage layout is an implementation detail; serialized schema and stable identity are the contract. The same entity may carry Material, Container, Tool, Structure, Ownable and Observable components. An entity does not need all components.

## Common components

| Component | Required concepts |
|---|---|
| Spatial | Region/local coordinates, orientation, supported/attached/contained relations |
| Physical | Dry mass, geometry approximation, displaced volume, relevant load limits |
| Material | Material ID, bounded mechanical/thermal traits, condition modifiers |
| Container | Capacity, contents, seal state, access, mixture rules |
| Structure | Members/connections, integrity, supported load, failure conditions |
| Tool/function | Functional roles, usable geometry, required handling, wear |
| Inventory | Quantity, stack identity, quality/condition, provenance |
| Ownership | Owner/custodian/title references, access rights, liens or obligations |
| Process state | Work in progress, stage, reserved inputs, labor, waste and outputs |
| Observation | Public appearance, detectable traces, salience, concealment and sensory channels |
| History | Creation/transformation/destruction provenance and significant names |

## Units and numeric rules

Authoritative time uses nonnegative integer seconds. Distances use integer millimeters; mass uses grams; volume uses milliliters; money uses integer minor units plus currency identity. Ratios/probabilities use a documented fixed-point scale. Display adapters convert units and round for the observer; simulations never parse display strings such as 'about five miles'. Conversion rules and overflow limits are explicit and tested.

Exact simulations use checked integer/fixed-point arithmetic where practical. Each bounded physical model records its validity range, approximation error, rounding convention and failure behavior. Do not claim engineering-grade accuracy. A prototype's omitted property means unknown/unsupported, not infinite strength or zero mass.

## Affordance resolution

Resolve an intended functional role against properties, object state, actor ability, environment and available tools. Return supported, supported-with-risk, missing-precondition, physically-infeasible, unknown-model or ambiguous. A dangerous attempt can still be valid. The public response must not reveal hidden defects before observation.

The canonical operation registry controls implemented semantics; the affordance catalog is not a restrictive list of bespoke object verbs. A new material or object that satisfies an existing functional model should work without adding a new verb. A new physical phenomenon does require a reviewed operation/model extension and tests.

## Initial physical model library

Implement containment and transfer; carrying/support/load; attachment and detachment; cutting/breaking; simple lever force and tool damage; volume/displacement and sealing; basic heat/fuel transformations. Include floor/ceiling bounds, overflow checking, declared approximation regimes and conservation ledgers. Hydrodynamics, structural finite-element analysis and molecular chemistry are not prerequisites.

For a barrel-assisted wagon, compute total carried mass and supported displaced volume using the actual assembled objects. Sealing and connection integrity matter. A person's assessment uses their measurements/knowledge; the kernel resolves actual consequences. Do not expose hidden exact safety margins as player UI facts.

## Composition invariants

Containment is acyclic. An object has one authoritative location/containment parent at a time. Attachment graphs can have cycles but require a defined structural solver and bounded traversal. Splitting stacks creates traceable descendants and conserves quantity. Transformations specify inputs, outputs, waste, emitted heat or abstracted sinks; every nonconserved accounting category names its source/sink rule.

A transfer reserves both source quantity and destination capacity. A task cannot consume a material already reserved by an incompatible task. Destruction releases/updates reservations and creates debris/waste according to the process definition rather than deleting obligations silently.

## Content and migration

The prototype schema in contracts is an initial required-field contract. Full component schemas grow with operations. Unknown components fail validation unless explicitly namespaced and supported by the installed content capability manifest. Removing a prototype used by a save produces a clear compatibility failure or an approved migration; no silent substitution.

## Acceptance

Test cargo splitting, nested containers, overloaded supports, an inappropriate improvised tool, damaged attachments, sealed/unsealed displacement, partially completed construction and broken-object reload. The same functional test must run with at least two different prototype families. These are SC-OBJECT and SC-CROSS scenarios, not assertions that a prototype schema alone implements physics.
