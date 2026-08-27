# Project Oregon Trail Documentation

This directory contains the current foundational architecture for Project Oregon Trail.

## Documents

### [PROJECT_VISION.md](PROJECT_VISION.md)
Defines the product vision, emergent campaign philosophy, persistent history, technological progression, platform goals, and offline-first requirement.

### [CORE_DESIGN_PRINCIPLES.md](CORE_DESIGN_PRINCIPLES.md)
Defines non-negotiable architectural principles that future systems should be checked against.

### [PERCEPTION_AND_RENDERING.md](PERCEPTION_AND_RENDERING.md)
Defines Perception Mode, observer-dependent information, modular 2D scene composition, rendering levels, directional consistency, stateful objects, and UI behavior.

### [WORLD_SIMULATION_AND_GENERATION.md](WORLD_SIMULATION_AND_GENERATION.md)
Defines seeded world generation, discovery, persistence, on-demand scene instantiation, simulation layers, information propagation, technological aging, and long-term world history.

### [LOCAL_AI_ARCHITECTURE.md](LOCAL_AI_ARCHITECTURE.md)
Defines the local/offline AI role, action interpretation, narrative realization, NPC knowledge isolation, validation firewall, training direction, device tiers, and model-replacement boundary.

### [WORLD_ACTION_LANGUAGE_V1.md](WORLD_ACTION_LANGUAGE_V1.md)
Defines WALang V1: the intermediate language for translating free-form player intent into validated simulation actions, plans, goals, directives, hypotheses, conditions, scheduling, delegation, social interaction, and structured world events.

## Current architecture sequence

The current recommended design order is:

1. Project vision and design constraints.
2. World Action Language.
3. World Object & Affordance System.
4. Character stats, knowledge, perception, and memory.
5. World generation and spatial model.
6. Simulation scheduling and event architecture.
7. Rendering/state presentation layer.
8. Local AI parser and narrative interfaces.
9. Individual simulation domains: health, economy, crafting, ecology, society, technology, etc.

The next major architecture document should be the **World Object & Affordance System**, which will define the universal entity/property model WALang operates on.
