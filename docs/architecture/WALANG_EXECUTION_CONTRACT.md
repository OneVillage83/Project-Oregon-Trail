# WALang execution contract

Version 0.2 | Owner: simulation and language leads

## Relationship to V1

The original [WALang V1](../WORLD_ACTION_LANGUAGE_V1.md) is the semantic design. Its YAML examples are illustrative and do not all share a production wire format. The new contracts directory defines a canonical JSON envelope and an initial operation profile. This does not remove future action families. An unsupported operation must be reported as unavailable, not accepted merely because its JSON is well formed.

## Envelope and trust

An intent carries schema_version, intent_id, actor_ref, observer_ref, context_revision and command. IDs are opaque namespaced references. The client/session sets the initiating actor, observer, context revision and request ID; model-supplied identity is checked against that binding. The model may propose an actor for a delegated step only within allowed references and authority.

Input text, selected entity, discourse state and allowed references are separate from the normalized intent. Never put authoritative outcomes, component writes, hidden facts or arbitrary code in the intent. Successful schema validation does not establish that the referenced entity exists, is known, is owned, or is usable.

## Command families

ACTION requests one registered operation with parameters. PLAN composes child commands sequentially, in parallel or as fallbacks. GOAL requests a bounded planner search for a registered goal predicate. DIRECTIVE installs a bounded recurring/persistent policy under explicit authority. QUERY reads permitted information. HYPOTHESIS records a proposition to test without asserting truth.

The seed machine-readable profile encodes ACTION and PLAN directly; GOAL, DIRECTIVE, QUERY and HYPOTHESIS receive full typed schemas before their implementation gates. Their architecture is required now. A profile version/capability list tells the parser and UI exactly what is executable. A shipping language interface may not imply support for all conceptual V1 examples before these extensions pass tests.

## Validation stages

1. Decode bounded UTF-8 JSON and reject duplicate keys, nonfinite numbers and excessive size/depth.
2. Validate the versioned structural schema and operation-specific parameter schema.
3. Resolve references only against actor-accessible view tokens and valid discourse/selection state.
4. Verify session identity, actor authority and requested delegation limits.
5. Validate units, quantities, spatial relations, conditions, schedules, duration and capability support.
6. Produce a PlanPreview with known costs, uncertain estimates, irreversible steps and unresolved choices.
7. On acceptance, reserve resources and schedule work. Revalidate relevant state revisions at execution.

A materially ambiguous reference produces clarification, not a random target. Model self-reported confidence never grants execution permission. An impossible outcome does not necessarily invalidate a meaningful attempt.

## Planner and lifecycle

Intent lifecycle: received → invalid/needs-clarification/preview-ready → accepted → scheduled. Execution lifecycle: pending → reserving → running → completed/failed/canceled/interrupted. A canceled request cannot later execute when delayed inference finishes.

A plan is an acyclic dependency graph after normalization. Initial caps: 32 action nodes, nesting depth 4, 16 condition clauses and bounded planning expansions configured per capability. These are safety/workload defaults to benchmark. Detect dependency cycles, incompatible actor schedules, recursion and repeated same-time work. Never allow arbitrary loops or unbounded self-delegation.

Parallel plans share the same reservation and time system. A task that loses access to its only axe waits, replans within authority, or fails transparently. It does not create a second tool. Fallbacks activate only on declared terminal reasons. A later fallback does not reverse spent time or consumed materials.

## Conditions and authority

Conditions are typed predicates evaluated through a specified observation/assessment context, not executable strings. 'Return if weather worsens' uses what the scout can perceive, not a hidden future weather schedule. 'Do not spend over 20' is a hard resource authority limit with currency and inclusive ceiling. A planner may optimize within the limit; an NPC's personality cannot authorize exceeding it.

Recurring work needs next_due, termination condition, maximum horizon, owner, cancellation rule and authority renewal. Orders transmitted remotely take effect after delivery/understanding. Requests to independent NPCs are speech acts; they are not forced inventory transfers.

## Receipts and errors

Return separate codes for parse, schema, reference, authority, capability, scheduling, conflict, simulation and infrastructure failures. Public messages explain only allowed information. Receipts include request/plan IDs, public progress, committed event references and a retriable flag. Infrastructure retries are idempotent: an intent_id committed once cannot transfer resources twice.

## Replay and tests

Persist normalized accepted intents and plans; replay never calls the model again. Compare menu, text and NPC intents under identical versions. Exercise wrong actor, wrong target, missing constraints, unknown verb, zero/negative quantity, stale quote, cancellation, duplicate submission, partial completion, fallback and concurrent tool use. See SC-INTENT and SC-SCHEDULER.
