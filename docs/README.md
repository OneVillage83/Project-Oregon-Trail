# Documentation index

Production architecture 0.2 | Contract seed 0.1.0

## Read first

[Production master plan](production/PRODUCTION_MASTER_PLAN.md) describes the full destination and delivery approach. [Product requirements](production/PRODUCT_REQUIREMENTS.md), [delivery gates](production/DELIVERY_ROADMAP.md) and [implementation backlog](production/IMPLEMENTATION_BACKLOG.md) turn it into reviewable work. [Implementation status](../project-control/IMPLEMENTATION_STATUS.json) and [validation report](../project-control/VALIDATION_REPORT.md) distinguish specification, static checks and actual runtime evidence.

The original foundation below remains the source of product intent. New documents refine implementation contracts; they do not silently reduce player freedom, Perception Mode, offline play, persistent history or later-era mechanics.

## Preserved foundation

| Document | Purpose |
|---|---|
| [Project vision](PROJECT_VISION.md) | Emergent campaigns, professions, offline play and generational world aging |
| [Core principles](CORE_DESIGN_PRINCIPLES.md) | Simulation authority, meaningful objects, knowledge and debug boundaries |
| [Perception and rendering](PERCEPTION_AND_RENDERING.md) | Observer-dependent perception and stateful modular 2D scenes |
| [World simulation and generation](WORLD_SIMULATION_AND_GENERATION.md) | Seeded geography, persistence, society, information and time |
| [Local AI foundation](LOCAL_AI_ARCHITECTURE.md) | Replaceable offline models interpreting and expressing—not resolving—the game |
| [WALang V1](WORLD_ACTION_LANGUAGE_V1.md) | Semantic breadth of actions, plans, goals, directives, hypotheses and queries |

## Production and decisions

| Document | Purpose |
|---|---|
| [Master plan](production/PRODUCTION_MASTER_PLAN.md) | Tracks, integration strategy and completion criteria |
| [Requirements](production/PRODUCT_REQUIREMENTS.md) | PR-001 through PR-032 and acceptance boundaries |
| [Roadmap](production/DELIVERY_ROADMAP.md) | G-0 through G-11, dependencies, ownership and evidence |
| [Clearwater slice](production/VERTICAL_SLICE_SPEC.md) | Crossing, investigation and changing-town integrated proofs |
| [Decisions and risks](production/DECISIONS_AND_RISKS.md) | Inherited rules, working defaults, open decisions and mitigations |
| [Implementation backlog](production/IMPLEMENTATION_BACKLOG.md) | B-001 through B-032 and first developer handoff |
| [Resources and release governance](production/RESOURCE_AND_RELEASE_PLAN.md) | Roles, estimates, costs and approval boundaries |
| [Architecture decisions](decisions/ARCHITECTURE_DECISIONS.md) | Thirteen explicit decisions and amendment process |

## Core architecture

| Document | Purpose |
|---|---|
| [System architecture](architecture/SYSTEM_ARCHITECTURE.md) | Ownership, dependency rules and end-to-end data flow |
| [Objects and affordances](architecture/WORLD_OBJECT_AND_AFFORDANCE_SYSTEM.md) | Components, units, functional properties and bounded physics |
| [WALang execution](architecture/WALANG_EXECUTION_CONTRACT.md) | Strict intents, validation, planning, authority and failure categories |
| [Kernel and time](architecture/SIMULATION_KERNEL_AND_TIME.md) | Scheduling, transactions, randomness and determinism |
| [Knowledge, perception and evidence](architecture/KNOWLEDGE_PERCEPTION_AND_EVIDENCE.md) | Truth/belief separation, detection and causal evidence |
| [Generation and fidelity](architecture/WORLD_GENERATION_AND_FIDELITY.md) | Prior commitments, region resolution and identity/accounting invariants |
| [Persistence and replay](architecture/PERSISTENCE_AND_REPLAY.md) | Durable commits, snapshots, recovery, replay boundaries and migrations |
| [AI and model qualification](architecture/LOCAL_AI_AND_MODEL_QUALIFICATION.md) | Gemma evaluation, runtime separation, grounding and offline packaging |
| [Client and rendering](architecture/CLIENT_RENDERING_AND_INPUT.md) | Hybrid input, previews, projections, scenes and interruption UI |
| [Native bridge and build](architecture/NATIVE_BRIDGE_AND_BUILD.md) | Planned source layout, APIs, threading, toolchains and feasibility proof |
| [Security and privacy](architecture/SECURITY_AND_PRIVACY.md) | Input/package limits, model authority, privacy and trust tiers |
| [Content and modding](architecture/CONTENT_AND_MODDING.md) | Versioned packs, capabilities, validation and safe data extensibility |

## World domains

| Document | Purpose |
|---|---|
| [Characters and party](domains/CHARACTER_PARTY_AND_PROGRESSION.md) | Attributes, meaningful learning, professions, control and lifecycle |
| [NPCs and communication](domains/NPC_SOCIAL_AND_COMMUNICATION.md) | Bounded planning, social acts, commitments, reports and reputation |
| [Health and medicine](domains/HEALTH_NUTRITION_AND_MEDICINE.md) | Exposure, symptoms, knowledge, care and bounded game abstractions |
| [Ecology and weather](domains/ECOLOGY_WEATHER_AND_RESOURCES.md) | Resources, cohorts, environmental changes and visibility/travel effects |
| [Economy and property](domains/ECONOMY_LOGISTICS_AND_PROPERTY.md) | Markets, production, money, custody, contracts and shipments |
| [Crafting and construction](domains/CRAFTING_ENGINEERING_AND_CONSTRUCTION.md) | Functional substitutions, work stages, structures and maintenance |
| [Law and conflict](domains/LAW_CRIME_AND_CONFLICT.md) | Cases, jurisdictions, evidence, force, authority and consequences |
| [Institutions and education](domains/GOVERNANCE_INSTITUTIONS_AND_EDUCATION.md) | Budgeted policies, organizations, teaching and research |
| [Technology and infrastructure](domains/TECHNOLOGY_INDUSTRY_AND_INFRASTRUCTURE.md) | Discovery, capacity, adoption and industrial/modern services |
| [Generations and timeplay](domains/GENERATIONS_HISTORY_AND_TIMEPLAY.md) | Succession, permanent history and controllable long-duration play |
| [Emergent opportunities](domains/EMERGENT_SITUATIONS_AND_OPPORTUNITIES.md) | Real needs becoming communicated requests and causal story opportunities |

## Content production

| Document | Purpose |
|---|---|
| [Art and audio](content/ART_AUDIO_AND_ASSET_PIPELINE.md) | Asset-state manifests, directional consistency, pipelines and rights |
| [Accessibility and localization](content/ACCESSIBILITY_LOCALIZATION_AND_TUTORIAL.md) | Equivalent knowledge, input paths, language and onboarding |
| [Authoring, balance and research](content/AUTHORING_BALANCE_AND_RESEARCH.md) | Editor workflow, experiments, provenance and editorial approval |

## Quality and operations

| Document | Purpose |
|---|---|
| [Test strategy](quality/TEST_STRATEGY.md) | Evidence levels, CI progression and feature/release definition of done |
| [Acceptance scenarios](quality/SCENARIO_ACCEPTANCE_CATALOG.md) | Named regression, integration and human-test contracts |
| [Performance and devices](quality/PERFORMANCE_AND_DEVICE_MATRIX.md) | Measurable targets and unqualified device/hardware assumptions |
| [Observability](quality/OBSERVABILITY_AND_DIAGNOSTICS.md) | Causal traces, developer tools, metrics and privacy-aware diagnostics |
| [Release and support](operations/RELEASE_SAVE_MIGRATION_AND_SUPPORT.md) | Packaging, migration, incident response, recovery and rollback |
| [Licensing and distribution](operations/DEPENDENCIES_LICENSING_AND_DISTRIBUTION.md) | Provenance, notices, AI disclosure and release approvals |
| [Technical source register](references/VERIFIED_TECHNICAL_SOURCES.md) | Dated primary-source technology verification and its limits |

## Executable seed and project control

[Contracts](../contracts/README.md) and [fixtures](../examples/contracts/README.md) start structural validation. They are not an implemented simulator. [Requirement traceability](../project-control/REQUIREMENTS_TRACEABILITY.json) maps requirements to owners, documents and scenarios. Follow [contributing](../CONTRIBUTING.md), [agent rules](../AGENTS.md), the [change policy](../project-control/CHANGE_LOG_POLICY.md) and append-only [run history](../project-control/RUN_HISTORY.jsonl).

Every future document under docs must appear in this index. Every runtime feature requires actual tests and evidence before its status changes from specified to verified.
