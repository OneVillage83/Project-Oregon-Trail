# Production architecture package validation

Architecture version 0.2 | Evidence recorded 2026-09-11T04:52:19Z

## Baseline and scope

Preserved the six foundational design documents at dbff86a9d512488533ffc2d47319a5bfa49d8ebe and the original history policy/validator. The production package at commit `06d26ef5e794bad0508bd2a56a33285592b98679` adds 60 files and modifies three existing paths: root README, documentation index and append-only run history. The 60 additions include 41 production/architecture/domain/content/quality/reference documents, contract tooling and contributor/project-control records.

This is a specification and development-tooling baseline, not a playable game. The canonical schema profile is deliberately limited; conceptual future commands require their own contracts and handlers before execution.

## Actual repository results

GitHub Actions tested the PR merge candidate `8cbae2e1168738d44b07fc38bea68509ebf2a1c4`, combining the package commit with main `eb91a54d04b8e3bdd74ae09e727d760ab5794084`. This is a test merge ref, not a merge into main.

Environment: Ubuntu 24.04.5, CPython 3.12.14, jsonschema 4.26.0. Results observed from the actual job/step summaries and architecture job log:

| Check | Result |
|---|---|
| Architecture and Contract Checks, run 34563726988, job 103151473691 | Completed successfully |
| Schema/registry/baseline validation | 4 schemas, 12 operation contracts and 4 positive baselines passed |
| Positive/negative conformance suite | 32 unittest methods passed; additional operation/variant subtests are within those methods |
| Documentation paths and JSON | 56 Markdown files, 108 local link paths and 8 JSON files passed |
| Requirement/scenario coverage | 32 requirements mapped to 38 declared acceptance scenarios |
| Run History Check, run 34563726965, job 103151473616 | Completed successfully, including append-only and changed-path validation |

Evidence: [architecture workflow](https://github.com/OneVillage83/Project-Oregon-Trail/actions/runs/34563726988) and [history workflow](https://github.com/OneVillage83/Project-Oregon-Trail/actions/runs/34563726965).

The runner emitted a non-blocking deprecation notice for the Node target of actions/checkout@v4 and actions/setup-python@v5; it ran them under Node 24 successfully. Refresh/pin tested action versions during build-toolchain qualification. This is not a claim that all future dependencies/platforms are qualified.

## What these checks prove and do not prove

The checks exercise strict decoding, schema/parameter rules, plan-size limits, unknown/outcome-field rejection, spending contradictions, event shape and save metadata. They validate local link targets and scenario/requirement references. They do not verify external link availability, semantic truth of every paragraph, real actor authority, game physics, transaction durability or player experience.

No native core/game client build, gameplay simulation, persistence crash/migration test, local-model benchmark, device/thermal test, long-world soak or human playtest was run. Those remain implementation/qualification work. Shipping model, hardware minimums and public release scope are unqualified.

## Integration and next work

Changes are on `docs/foundation-architecture` in draft PR #1; main remains unmerged. This evidence-only follow-up updates the report, implementation status and run history without changing the validated contracts or tests. Its own PR workflows must still be checked before handoff.

The next bounded implementation package is B-001: engine-independent core build, checked quantities, stable IDs and native tests. G-0 review and G-2 feasibility decisions remain explicit rather than being marked complete merely because the documents exist.
