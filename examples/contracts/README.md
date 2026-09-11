# Contract fixtures

`baselines.json` contains four authored positive examples: intent, physical prototype, committed event and save manifest. IDs, timestamps and hashes are fictional fixture values, not real saves or benchmark output. `tests/test_contracts.py` derives positive and intentional negative cases without contacting a model or executing gameplay.

The fixtures check bounded decoding, strict fields/units, operation parameters, plan limits, budget contradictions, event shape and save metadata. Runtime knowledge, authority, actual physics, transaction durability and NPC behavior require the future native/integration scenarios and remain untested by these files.
