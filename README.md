# Project Oregon Trail

A simulation-first, natural-language-driven game focused on player freedom, emergent careers, persistent world history and an evolving society—not graphics-heavy spectacle or an AI narrator inventing outcomes.

> **The simulation determines what exists. The renderer determines what can be shown. Perception determines what the observing character notices.**

Players express creative plans through natural language, supported by efficient conventional controls. The world evaluates real objects, knowledge, resources, authority, time and consequences. A hunter can become an investigator through practice and reputation; a settlement can develop from timber buildings into industrial and modern infrastructure across generations.

## Current state

This branch contains the preserved foundational design, production architecture version 0.2 and executable development contract seed 0.1.0. A playable game client and native simulation are **not implemented**. Model/device/gameplay qualification is **not complete**. Specifications and test targets are not shipped features.

Start with the [documentation index](docs/README.md) and [production master plan](docs/production/PRODUCTION_MASTER_PLAN.md). The package defines 32 product requirements, 12 evidence gates, 32 implementation work packages and a scenario acceptance catalog. See [implementation status](project-control/IMPLEMENTATION_STATUS.json) and [validation evidence](project-control/VALIDATION_REPORT.md).

## Working implementation direction

Godot presentation, an independent C++20 simulation with a thin native bridge, local SQLite persistence and replaceable local inference are working choices pending feasibility tests. Gemma 4 E4B is the lead evaluation candidate, with smaller/larger device candidates tested separately. `llama.cpp` is a runtime candidate, not a requirement to use Meta Llama models. No exact shipping model or minimum device is qualified yet.

Offline play, observer-dependent Perception Mode, composable actions, persistent places and mechanical technological aging remain core requirements. A small integrated test region proves these boundaries rather than replacing the full destination.

## First implementation work

[B-001](docs/production/IMPLEMENTATION_BACKLOG.md) starts with the engine-independent build, checked quantities, stable IDs and tests. The [object and affordance contract](docs/architecture/WORLD_OBJECT_AND_AFFORDANCE_SYSTEM.md), [WALang execution contract](docs/architecture/WALANG_EXECUTION_CONTRACT.md) and [kernel specification](docs/architecture/SIMULATION_KERNEL_AND_TIME.md) guide the first code.

## Development checks

```sh
python -m pip install -r requirements-architecture.txt
python scripts/validate_contracts.py
python -m unittest discover -s tests -p 'test_*.py' -v
python scripts/validate_architecture.py
```

These checks validate the contract/documentation seed, not gameplay, model quality or save durability. See [contributing](CONTRIBUTING.md) and [agent rules](AGENTS.md).

## Mandatory timestamped history

Every meaningful change must append a UTC record to [RUN_HISTORY.jsonl](project-control/RUN_HISTORY.jsonl), preserving existing lines and covering changed paths. The [change policy](project-control/CHANGE_LOG_POLICY.md) applies to documentation, code, schemas, assets, tests, experiments, fixes and reversions. The existing history workflow and new architecture workflow provide checks; branch-protection settings and main-branch merge remain separate review decisions.
