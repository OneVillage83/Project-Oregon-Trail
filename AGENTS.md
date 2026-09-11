# Contributor and agent operating rules

## Start here

Read docs/README.md, docs/production/PRODUCTION_MASTER_PLAN.md, docs/production/IMPLEMENTATION_BACKLOG.md, project-control/IMPLEMENTATION_STATUS.json and recent project-control/RUN_HISTORY.jsonl entries before work. Read the specific domain contracts and acceptance scenarios for the issue. The original six foundation documents remain authoritative product intent.

## Non-negotiable boundaries

The simulation owns outcomes. Models propose intents and express permitted facts; they cannot mutate state, create clues or grant authority. UI/menu actions use the same contracts. Every normal presentation surface is observer-filtered. Offline baseline play, meaningful Perception Mode, composable actions, persistent geography/history and multi-era/generational development must not be silently reduced.

Gemma 4 is the lead evaluation family, not a qualified shipping choice. llama.cpp is a runtime, not a mandatory Meta Llama model. Godot/C++/SQLite are working implementation defaults pending feasibility evidence. Do not invent benchmark results or minimum hardware.

## Work discipline

Implement a bounded backlog issue with requirement and scenario IDs. Preserve unrelated user work. Do not build a second fake world in a client/model demo. New operations require typed contracts, handlers, failure behavior, save/projection implications and tests. Keep native simulation independent of Godot and inference.

Before changing architectural intent, save compatibility or public release scope, record a proposed decision and obtain maintainer review. Ordinary implementation can proceed within established contracts. Never add a blanket project license, publish a release, purchase services or merge protected work without authorization.

## Validation

Run `python scripts/validate_contracts.py`, `python -m unittest discover -s tests -p 'test_*.py'`, and `python scripts/validate_architecture.py` for architecture/contract changes after installing requirements-architecture.txt. Run relevant native/gameplay checks once implemented. Check history with `python scripts/validate_run_history.py --base <review-base>` against the correct committed diff.

Report tests actually run, failures and unavailable devices. Static schema tests are not gameplay, model or save-durability proof. Keep implementation status and gate evidence honest. Update docs/README.md for every Markdown document under docs.

## Mandatory audit log

Every meaningful logical change appends a UTC ISO-8601 entry to project-control/RUN_HISTORY.jsonl in the same PR/change set. Preserve all existing lines. Cover every changed repository path and record why, decisions, actual validation, limitations and follow-up. Failed consequential experiments and reversions are history too. Follow project-control/CHANGE_LOG_POLICY.md.

## Handoff

Summarize exact branch/commit, changed contracts, actual tests, known limitations and next bounded work package. Do not describe a draft PR as merged or specifications as implemented features.
