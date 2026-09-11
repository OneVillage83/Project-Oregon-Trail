# Contributing

Read [AGENTS.md](AGENTS.md), the [documentation index](docs/README.md), [backlog](docs/production/IMPLEMENTATION_BACKLOG.md) and [change policy](project-control/CHANGE_LOG_POLICY.md). The repository currently contains design, architecture and development contract validation; a playable client and native simulation are not implemented.

## Development validation

Use a supported Python environment, currently Python 3.12 in architecture CI. From the repository root:

```sh
python -m pip install -r requirements-architecture.txt
python scripts/validate_contracts.py
python -m unittest discover -s tests -p 'test_*.py' -v
python scripts/validate_architecture.py
python scripts/validate_run_history.py --base origin/main
```

Select the actual review base for a stacked PR rather than blindly using main. The history validator examines the committed diff; staged/untracked work still needs to be included and logged before review. Large models are not required for these tests.

## Pull requests

Keep changes scoped to a requirement/backlog package, include positive and negative fixtures, document compatibility/security/observer effects and append timestamped history. Update the documentation index and traceability when appropriate. Separate proposed targets from measured results. Do not change public save formats, fundamental product constraints or licensing without review.

Existing foundation work is in a draft PR until the maintainer merges it. Preserve branch history and avoid force pushes. An architecture CI pass verifies only its named checks; it does not prove the full game works. Native, device and model suites become required as their implementation arrives.

## Bug reports

Provide version/commit, minimal reproduction, expected versus observed result, and a redacted trace or authored fixture when useful. Player saves and raw command text can be private and are not required by default. Use [diagnostics guidance](docs/quality/OBSERVABILITY_AND_DIAGNOSTICS.md) and [support runbook](docs/operations/RELEASE_SAVE_MIGRATION_AND_SUPPORT.md).
