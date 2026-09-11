# Observability, debugging and diagnostics

Version 0.2 | Owner: tools/QA lead

## Trace contract

For consequential actions retain request/intent/plan/event IDs, parent causality, schema/rules/content versions, relevant revisions, validation stage, resource reservations, scheduling, committed effects and public result. A trace reconstructs input → intent → references → plan → events → projections. Do not require model-internal reasoning to explain a world result.

Structured fields include simulation time, wall-clock diagnostic timestamp, subsystem, severity, error code, duration, build ID and correlation IDs. Simulation and wall-clock time are distinct. Counters and metrics do not mutate game state or consume authoritative random numbers.

## Public versus privileged views

Player explanations show known reasons and uncertainties. Developer traces may include hidden causes, but require explicit developer mode and are spoiler-marked. A hidden defect cannot appear in a normal 'why did this fail?' tooltip before it is observable. Redact raw prompts, player names and local paths from default exports; never log credentials or signing material.

## Essential tools

Build an entity/component inspector; action/plan trace viewer; scheduler/reservation viewer; observation/belief diff; evidence provenance graph; world/fidelity transfer inspector; save/replay comparator; content dependency viewer; and economy/health/technology balance reports. These tools consume the same contracts as runtime and clearly distinguish expected versus actual state.

## Metrics

Track parse/semantic/clarification/unsupported-operation rates separately. Measure abandoned commands, canceled inference, planner budget exhaustion, duplicate requests, stale previews, recovery events, frame/scheduler/inference latency, memory growth and domain accounting anomalies. A high schema-validity score is not task accuracy.

Use local opt-in diagnostic retention. Remote telemetry is optional and consented to, never a gameplay dependency. Aggregate metrics avoid identifying player content where possible. Bug reports should request the smallest reproducible seed/intent/trace bundle rather than an entire private save by default.

## Failure reports and triage

A reproducible report contains build/versions, seed/fixture, accepted normalized commands, expected invariant, observed event/hash and first divergence. Attach small reports to the issue and large artifacts with checksums/retention. Severity distinguishes save corruption, unauthorized mutation, knowledge leakage, gameplay rule failure, performance and cosmetic defects.

For regressions, preserve the failing fixture before fixing code. Log rejected experiments and reversions with their cause. Do not close an issue based only on improved narration. Exact critical outcomes must be corrected at the owning simulation/projection layer.

## Acceptance

Every SC scenario emits a useful failure bundle. SC-REPLAY finds the first divergent event. SC-KNOWLEDGE verifies public/privileged separation. SC-SECURITY verifies redaction and opt-in export. Diagnostics remain usable when inference is unavailable.
