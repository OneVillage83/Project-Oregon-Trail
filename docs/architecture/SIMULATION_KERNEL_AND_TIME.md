# Simulation kernel, time, scheduling and determinism

Version 0.2 | Owner: simulation lead

## Kernel responsibilities

The core owns stable entity IDs, component stores, checked quantities, the simulation clock, operation registration, reservations, deterministic randomness, ordered event batches and durable commit boundaries. It exposes headless APIs for world creation/loading, command submission, observation, time advancement, saving and diagnostics. It has no dependency on Godot, model tokens, wall-clock progression or rendering framerate.

## Clock contract

Use signed 64-bit storage with nonnegative simulation seconds, checked overflow and serialization limits compatible with the JSON contract. One campaign calendar maps elapsed seconds to local date/season; era and localization displays do not change the underlying clock. Paused command composition and local inference do not consume game time. Wall-clock timestamps are for diagnostics/run history, not random seeds or authoritative event ordering.

Time advancement is a request to advance up to a horizon. The scheduler stops at the earliest relevant event, policy interruption, player decision or budget yield. A UI frame budget controls how much work runs before yielding, not which results occur. App suspension checkpoints or preserves a recoverable boundary; app closure does not advance the world by default.

## Scheduling

Scheduled entries contain due_time_s, phase, priority, stable sequence, subject IDs, operation/payload version, plan ID and cancellation token. Sort by that full key; unordered container traversal must not determine outcomes. Same-time phases are specified: complete previously running work; resolve environmental updates; process deliveries/knowledge; evaluate interruptions; activate newly eligible tasks; publish the consistent view. Exact phase values belong in the kernel version and tests.

Prevent zero-time loops with a same-time work cap and explicit deferred scheduling. Detect reentrant callbacks and cyclic dependencies. Recurring work persists its next due time and terminal condition; reload must not replay already completed installments.

## Plans, resources and ownership

Plans reserve exclusive tools/actors and divisible materials/capacity with bounded leases tied to plan lifetime. Acquire resource IDs in stable order, or use a single atomic reservation operation, to avoid deadlocks. Distinguish a reservation from actual consumption. Expired or invalidated reservations produce an event and trigger a documented response.

Only the simulation owner writes authoritative state. Worker threads may calculate on immutable snapshots and return proposals with precondition revisions. The owner validates and commits them in deterministic order. Parallel execution must not make weather, inventory or NPC decisions race-dependent.

## Randomness

Select and pin a reproducible generator algorithm in G-2/G-3. Do not rely on platform-specific standard-library distribution behavior. Derive independent streams from world seed, subsystem key and stable entity/event scope. Serialize counters/state. Record algorithm version and golden vectors. Observation retries use an attempt/conditions identity so toggling a panel cannot farm random successes.

Changing a stream's consumption order can change a campaign; isolate streams and version intentional changes. Model generation randomness is outside the authoritative world RNG. An accepted normalized intent is the replay input regardless of which model produced it.

## Numeric reproducibility

Prefer checked integer/fixed-point domain math. Specify rounding, saturation versus rejection, units, iteration order and deterministic approximation methods. Floating-point graphics calculations are not world truth. Any necessary floating-point domain algorithm requires cross-platform golden fixtures and a declared determinism policy. Cross-platform byte-identical results are a qualification target, not assumed from choosing C++.

## Commit protocol

Build a candidate batch with expected component revisions, domain events and state effects. Validate invariants against the candidate state. Persist state/effects, event sequence and idempotency receipt in one transaction. Only then expose its receipt and updated view. On failure discard the candidate and leave the last durable state intact. Long tasks checkpoint logical progress in separate transactions, preserving prior completed work.

Deterministic serialization produces a state hash over specified authoritative fields and canonical ordering. Exclude cache layout, localized text, wall-clock logs and optional narration. Keep content/rules versions in the hash manifest.

## Invariants and acceptance

No negative quantities, duplicate IDs, containment cycles, unexplained inventory creation, double-spent resources or orphaned active plans. Legal sources/sinks and births/deaths have named events. Test pause/resume, equal-time ordering, worker completion order, duplicate intent, interrupted/canceled tasks, recursion caps, long horizons and save/reload mid-plan. Compare golden runs across qualified compilers and device architectures. Failure reports retain seed, accepted intent stream, version pins, hashes and the first divergent event.
