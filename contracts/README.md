# Executable contract seed

Contract version 0.1.0 | Architecture baseline 0.2

These JSON Schema Draft 2020-12 contracts and operation-parameter schemas are executable development checks. They are not implemented game operations. The canonical seed supports ACTION and nested PLAN envelopes, physical object prototypes, three representative committed-event payloads and save manifests. Full GOAL, DIRECTIVE, QUERY, HYPOTHESIS and additional domain event/component schemas are required before their handlers ship; their design is retained in the architecture documents.

## Files

- [Intent schema](walang-intent.schema.json): strict envelope, bounded plan structure and typed constraints.
- [Operation registry](operation-registry.json): declared operation parameter contracts; every entry remains runtime-unimplemented.
- [Object prototype](object-prototype.schema.json): physical prototype seed, not the complete component model.
- [World event](world-event.schema.json): authoritative event examples, not permission for a model to emit events.
- [Save manifest](save-manifest.schema.json): version/hash/retention metadata, not an implemented database.

The validator rejects unknown properties, duplicate JSON keys, nonfinite numbers, oversized/deep input, unknown operations, invalid operation parameters and excessive action plans. It additionally checks save replay bounds and UTC timestamp validity. Runtime reference knowledge, actor/session authority, material physics, reservations, time and persistence cannot be proven without the core and are not claimed validated here.

## Development commands

From the repository root, install `requirements-architecture.txt`, run `python scripts/validate_contracts.py`, `python scripts/validate_architecture.py`, and `python -m unittest discover -s tests -p 'test_*.py'`. The fixtures in [examples/contracts](../examples/contracts/README.md) include positive and intentional negative cases.

## Extension procedure

Add a registered typed contract, positive/negative fixtures, native handler/conformance tests, state/event ownership, projection behavior and save compatibility. Update the capability profile and run history. Never accept a future operation merely because it resembles an existing verb. Do not let schema-valid output bypass runtime authority or reinterpret an intent as an outcome.
