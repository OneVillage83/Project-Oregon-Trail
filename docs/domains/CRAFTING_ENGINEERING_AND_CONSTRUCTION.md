# Crafting, engineering and construction

Version 0.2 | Owner: simulation/content lead | Requirement PR-012

## Process definitions

A process defines input functional/material requirements, tools, facility/environment constraints, knowledge/skill requirements, stages, labor/time, outputs, byproducts/waste, quality rules and interruption behavior. Recipes are data using reusable operations, not arbitrary scripts that set the desired result.

A player may specify a known recipe or propose a functional goal. A bounded planner searches supported processes and substitutions from the actor's knowledge. It reports unsupported physics or unavailable knowledge honestly. The language model cannot invent a new manufacturing process and declare it feasible.

## Functional substitution

Evaluate substitutes by needed properties and constraints. A long rigid object may serve as a lever within a bounded geometry/strength model; its usual item category is not decisive. Required material properties, condition and geometry must be present. Unknown is not automatically acceptable. Improvisation can damage tools and change quality.

Construction/repair estimates use the character's measurements and skill. Actual simulation uses the true relevant state. A hidden defect may therefore cause an estimate to differ from the outcome without the model inventing a surprise.

## Work orders

Work orders own design/prototype references, site and permission, stages, assigned labor, reservations, progress, spent inputs, inspection records and completion criteria. States: proposed, designed, authorized, supplied, in-progress, paused, failed, completed, abandoned. Each stage has a durable checkpoint and valid cleanup/refund rules.

Reserve tools, materials, actor time and site capacity before work. Consume inputs at declared stages. Cancellation returns only unconsumed recoverable stock; completed labor/time is not refunded. A failed build can leave work-in-progress or salvage, rather than magically restoring the starting inventory.

## Structures and infrastructure

Use member/connection and load/support abstractions for consequential engineering. Site/parcel IDs survive reconstruction. Replacement structures receive their own lifecycle identity linked to the historical site and prior structure. A building upgrade changes actual material/capabilities and visual state only after appropriate stages complete.

Maintenance consumes supplies/time and affects condition. Degradation, overloading and environmental damage use versioned bounded models. A repair cannot silently restore a destroyed part without replacement material. Infrastructure links to route capacity, energy/water/communication service and institutional permissions.

## Knowledge and technology

Knowing a design differs from owning tools, having suitable inputs and possessing production capacity. Teaching/research can unlock process knowledge; adoption still requires economic and physical prerequisites. Later vehicles, plastics and electronics add processes/components and bounded new rule families without replacing object IDs or WALang.

## Content validation

The compiler verifies references, dependency cycles where prohibited, quantity units, conservation/source-sink accounting, stage transitions, required visual states and valid substitutions. Process definitions include provenance, tested validity range and balance version. New operations require native rule implementation and tests before content can claim them.

## Acceptance

SC-CRAFT tests substitutions, unavailable tools, shared-tool contention, quality, waste, interruptions, salvage and reload. SC-CROSS tests a functional improvised crossing without a special-case verb. SC-TOWN tests a funded prerequisite-gated upgrade and persistent site/ownership. A progress bar reaching 100% without consumed resources is not completion evidence.
