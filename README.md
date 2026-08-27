# Project Oregon Trail

A simulation-first, natural-language-driven game project focused on player freedom, emergent stories, persistent world history, and deterministic world simulation rather than graphics-heavy presentation.

## Core idea

The game aims to spend its complexity budget on **what the player can do and what the world can meaningfully simulate**, rather than on high-end 3D graphics. Players interact through a hybrid interface centered on free-form natural-language input, supported by conventional menus and contextual controls.

The simulation is authoritative. Local AI models may interpret player language and narrate results, but they do not invent or directly modify world state.

> **The simulation determines what exists. The renderer determines what can be shown. Perception determines what the observing character notices.**

## Foundational architecture

Start with [`docs/README.md`](docs/README.md).

Current foundation documents cover:

- project vision and emergent campaign philosophy;
- core design principles;
- Perception Mode and modular 2D rendering;
- seeded persistent world generation and technological aging;
- local/offline AI architecture;
- World Action Language V1.

## Mandatory project history

Every meaningful change to this repository must be recorded in the append-only timestamped log at [`project-control/RUN_HISTORY.jsonl`](project-control/RUN_HISTORY.jsonl).

The governing rules are defined in [`project-control/CHANGE_LOG_POLICY.md`](project-control/CHANGE_LOG_POLICY.md). The requirement applies to design decisions, documentation, source code, schemas, assets, configuration, tests, tooling, experiments, fixes, reversions, and other consequential project work.

Pull requests are checked by `.github/workflows/run-history-check.yml`; changed paths must be covered by newly appended run-history entries.

## Current next architecture layer

The next major design target is the **World Object & Affordance System**: the universal entity/property model that gives WALang concrete objects, materials, states, capabilities, and transformations to operate upon.
