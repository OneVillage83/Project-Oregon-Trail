# Dependency-ordered delivery roadmap

Version 0.2 | Gates are future work unless evidence says otherwise

## Gate definitions

| Gate | Work and dependencies | Exit evidence | Accountable role |
|---|---|---|---|
| G-0 | Consolidate original foundation and production package; record assumptions and owners | Reviewed baseline, navigation, history, requirement mapping; merge decision remains explicit | Product/technical lead |
| G-1 | Object properties, canonical intents, knowledge/event/save contracts; depends G-0 | Valid/invalid fixtures plus semantic validators; initial proof profile cannot be mistaken for every planned verb | Simulation lead |
| G-2 | Native client bridge, headless executable spike, local-model harness, SQLite recovery experiment, mobile package spike; needs minimal G-1 | Reproducible PC build, observed device results, toolchain/model decision records and fallback plan | Technical lead |
| G-3 | Entity store, operation registry, deterministic scheduling, reservations, event batches, save/reload and trace tooling; depends G-1/G-2 | Replayed state hashes, contention tests, cancellation and crash recovery | Simulation lead |
| G-4 | Travel, camp, needs, inventories, barter, repair/craft and rough modular scene; depends G-3 | Crossing has at least three causally distinct solutions and meaningful failures | Gameplay lead |
| G-5 | Knowledge projections, Perception Mode, evidence, bounded NPC planning and communication; depends G-3/G-4 | Hunter/carpenter/physician observations, causal case, transmitted reputation, no-leak test suite | Gameplay/AI-systems lead |
| G-6 | Production interpreter/dialogue/narration, clarification, cancellation and offline installer; evaluation begins G-2 | Held-out command metrics, grounded critical statements, installed-model offline play, fault fallback | Language lead |
| G-7 | Regional production, logistics, ecology, health, institutions, law and emergent opportunities; depends G-4/G-5 | Multi-settlement causal chains, bounded population/economy, named-entity continuity | Simulation/gameplay lead |
| G-8 | Aging, succession, history, discovery, adoption, industrial and modern infrastructure; depends G-3/G-7 | Same places/families survive time; mixed-era development; vehicles and modern materials are real mechanics | Systems/content lead |
| G-9 | Content scale-up, editorial review, audio, localization, tutorial and asset-state coverage; starts tools earlier | Content packs validate and support complete loops at the approved scope | Content lead |
| G-10 | External alpha/beta, accessibility, performance, device coverage, migrations, soak, security | Approved quality thresholds with reproducible evidence and no unresolved release blockers | QA/release lead |
| G-11 | Packaging, store/legal review, support, recovery, update channels | Signed/verified release artifacts where required, notices, rollback exercise, user-facing scope disclosure | Release/product lead |

## Parallel work and critical path

The core dependency is contracts → headless state changes → persistence → integrated choices → regional continuity. Test language feasibility and Godot/native integration before the kernel becomes expensive to replace. Asset naming, state manifests, interface design, and authoring tools start in G-1/G-2; final art quantity waits for stable state coverage. G-9 does not mean postponing every content tool until all systems exist.

An early UI demo, language-only chatbot, or accelerated aging script does not substitute for the relevant integrated gate. A gate may have partial evidence without being complete. Record the exact unsupported cases and next blocker.

## Evidence bundle for every gate

A gate report records code commit, rules/content/model/runtime versions, build configuration, test inputs/seeds, measured results, known failures, owner review, and a go/no-go decision. Store small reports in source control and large traces as versioned build artifacts with checksums. All metrics identify hardware and whether they are targets or observations.

## Public milestones

An internal slice is not automatically a public demo. A demo needs a comprehensible opening, coherent ending or continuation point, save integrity, explicit included systems/eras, accessibility basics, and installation testing. Early access, a paid first release, and the full multi-era destination require separate scope approvals. Do not market future plans as shipped features.

## Estimation and staffing

Do not convert these gates into arbitrary dates. At G-2, estimate work packages using measured throughput for validated operations, asset families/states, scenarios, and device builds. Account for engineering review, design iteration, bug fixing, legal/content review, QA and migration maintenance. Use available weekly capacity rather than assuming full-time work.

If resources are constrained, shrink the number of towns, asset variants, or authored situations in a proof; do not remove the architectural boundaries that make the real destination possible. Product scope reductions need an explicit decision.

## Initial sequence

First implement the entity/quantity/operation contracts and a minimal headless action executor. Then prove resource contention, save/reload and observer filtering with temporary art. The first natural-language model is connected to this real pipeline, not to a parallel fake world. The [implementation backlog](IMPLEMENTATION_BACKLOG.md) breaks this into reviewable work packages.
