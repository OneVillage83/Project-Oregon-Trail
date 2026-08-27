# Change Logging Policy

## Purpose

Project Oregon Trail maintains an append-only, timestamped history of meaningful project changes so design evolution, implementation decisions, tests, failures, and corrections can be reconstructed without relying on chat history or memory.

The canonical machine-readable log is:

`project-control/RUN_HISTORY.jsonl`

This policy applies to **all project work**, including documentation, source code, schemas, assets, configuration, tests, data pipelines, tooling, workflows, architectural decisions, experiments, and reversions.

## Non-negotiable rule

> Every meaningful logical change must add at least one timestamped entry to `project-control/RUN_HISTORY.jsonl` in the same pull request/change set.

A change is not considered fully documented until its run-history entry exists.

## Timestamp standard

Use UTC ISO-8601 timestamps with second precision:

`YYYY-MM-DDTHH:MM:SSZ`

Example:

`2026-08-27T07:36:43Z`

UTC is canonical so entries remain unambiguous across contributors and machines.

## JSONL format

Each line of `RUN_HISTORY.jsonl` is one independent JSON object. Existing lines are append-only and must not be rewritten except to repair proven corruption.

Required fields:

- `timestamp_utc` — UTC ISO-8601 timestamp ending in `Z`.
- `actor` — person, assistant, automation, or tool responsible for the logical change.
- `category` — broad change class.
- `summary` — concise statement of what changed.
- `reason` — why the change was made.
- `files` — repository paths affected by the logical change.
- `validation` — checks performed, or an explicit statement that validation was not applicable.

Recommended optional fields:

- `decisions` — architectural/product decisions established by the change.
- `related_pr` — pull request number or URL.
- `related_issue` — issue number or URL.
- `related_commits` — commit SHA(s) when known.
- `supersedes` — prior log entry or decision replaced by this change.
- `notes` — additional context, limitations, follow-up work, or observed failures.

## Categories

Use one of these values unless a new category is deliberately added to this policy:

- `design`
- `architecture`
- `documentation`
- `code`
- `data`
- `schema`
- `asset`
- `test`
- `tooling`
- `build`
- `ci`
- `bugfix`
- `refactor`
- `experiment`
- `decision`
- `revert`
- `release`

A logical change spanning multiple categories should use the category that best describes its primary purpose and describe the rest in `summary` or `notes`.

## Granularity

The log tracks **logical changes**, not keystrokes.

Examples that should normally receive separate entries:

- adding or changing a design rule;
- adding a subsystem architecture document;
- implementing a feature;
- fixing a bug;
- changing a schema or save-game format;
- changing an AI model/runtime;
- adding or changing art/asset behavior that affects gameplay state;
- changing tests or validation rules;
- running a consequential experiment whose result influences design;
- reverting prior behavior.

Multiple files changed as part of one coherent operation may share one entry as long as all affected paths are listed and the entry explains the operation.

## Failed work is also history

Important failed experiments, rejected approaches, regressions, and reversions should be logged. The goal is not merely to record what survived; it is to preserve why the project evolved in a particular direction and prevent repeated dead ends.

## Design decisions

When a change establishes or modifies a non-trivial design decision, the run-history entry should record the decision explicitly in `decisions`.

Examples:

- simulation remains authoritative over LLM output;
- Perception Mode is observer-dependent;
- world geography is seeded and persistent;
- local AI is replaceable and cannot directly mutate authoritative world state.

## Validation expectations

For code or schema changes, `validation` should identify relevant tests, static checks, builds, migrations, or simulations actually run.

For documentation/design-only changes, acceptable validation includes review against existing architectural principles and cross-document consistency.

Never claim a test was run when it was not.

## Pull-request enforcement

The repository includes a validation script and GitHub Actions workflow that require pull requests containing meaningful repository changes to also update `project-control/RUN_HISTORY.jsonl` and ensure newly added log entries cover the changed paths.

This automated check is a safety net; it does not replace accurate human documentation.

## Historical reconstruction

When documenting work that occurred before this policy existed, use an entry marked in `notes` as retrospective rather than fabricating exact historical timestamps. The entry timestamp should represent when the retrospective record was created.

## Future assistant/project workflow

For every future Project Oregon Trail work session:

1. Read relevant architecture documents and recent run-history entries.
2. Make the requested logical change.
3. Validate the result.
4. Append a timestamped `RUN_HISTORY.jsonl` entry describing the change.
5. Include all affected repository paths.
6. Update architecture/docs when the implementation changes a documented contract.
7. Never silently alter a foundational decision.

This policy is itself part of the project architecture and should be treated as a durable project-control requirement.
