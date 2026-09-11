"""Positive/negative conformance tests for the development contract seed."""
from __future__ import annotations

import copy
import unittest

from scripts.validate_contracts import (
    ROOT, ContractError, FIXTURE_SCHEMAS, read_json, strict_loads, validate_data,
)


class ContractTests(unittest.TestCase):
    def setUp(self) -> None:
        self.base = read_json(ROOT / "examples/contracts/baselines.json")

    def action(self, operation: str, parameters: dict) -> dict:
        value = copy.deepcopy(self.base["intent"])
        value["command"]["operation"] = operation
        value["command"]["parameters"] = parameters
        return value

    def rejected(self, value: object, schema: str, stage: str) -> None:
        with self.assertRaises(ContractError) as caught:
            validate_data(value, schema)
        self.assertEqual(caught.exception.stage, stage)

    def test_baselines(self) -> None:
        for key, schema in FIXTURE_SCHEMAS.items():
            with self.subTest(key=key):
                validate_data(self.base[key], schema)

    def test_each_declared_operation(self) -> None:
        cases = {
            "WAIT": {"duration_s": 1},
            "PERCEIVE": {"scope_ref": "scene:room"},
            "SEARCH": {"target_ref": "item:shelf", "duration_s": 1200},
            "MOVE": {"destination_ref": "site:camp"},
            "SCOUT": {"origin_ref": "site:camp", "direction": "upstream", "max_distance_mm": 8046720, "transport_ref": "animal:horse"},
            "TAKE": {"target_ref": "item:barrel", "quantity_count": 1},
            "MEASURE": {"target_ref": "site:room", "dimension": "width"},
            "ATTACH": {"item_ref": "item:barrel", "target_ref": "item:wagon", "method_ref": "process:strap"},
            "BUILD": {"prototype_ref": "prototype:raft", "site_ref": "site:bank"},
            "OFFER": {"recipient_ref": "actor:merchant", "offer_item_ref": "item:hide", "offer_count": 3, "request_item_ref": "item:tool", "request_count": 1, "max_extra_minor": 50, "currency": "CREDIT"},
            "REPAIR": {"target_ref": "item:wagon", "material_ref": "material:wood", "duration_limit_s": 3600},
            "EXAMINE_PATIENT": {"patient_ref": "actor:sarah", "duration_s": 600},
        }
        registry = read_json(ROOT / "contracts/operation-registry.json")
        self.assertEqual(set(cases), set(registry["operations"]))
        for operation, parameters in cases.items():
            with self.subTest(operation=operation):
                validate_data(self.action(operation, parameters), "walang-intent.schema.json")

    def test_plan_modes(self) -> None:
        for mode in ("SEQUENTIAL", "PARALLEL", "FALLBACK"):
            value = copy.deepcopy(self.base["intent"])
            step = value["command"]
            value["command"] = {"kind": "PLAN", "mode": mode, "steps": [copy.deepcopy(step), copy.deepcopy(step)]}
            with self.subTest(mode=mode):
                validate_data(value, "walang-intent.schema.json")

    def test_guarded_scout(self) -> None:
        value = self.action("SCOUT", {"origin_ref": "site:camp", "direction": "upstream", "max_distance_mm": 8046720})
        value["command"]["constraints"] = [
            {"kind": "RETURN_BEFORE", "time_s": 64800},
            {"kind": "ABORT_IF", "predicate": "WEATHER_WORSENING", "observer_ref": "actor:player", "response": "RETURN"},
        ]
        validate_data(value, "walang-intent.schema.json")

    def test_unknown_outcome_field(self) -> None:
        value = copy.deepcopy(self.base["intent"])
        value["world_state"] = {"secret_passage_open": True}
        self.rejected(value, "walang-intent.schema.json", "schema")

    def test_outcome_inside_parameters(self) -> None:
        value = self.action("WAIT", {"duration_s": 1, "success": True})
        self.rejected(value, "walang-intent.schema.json", "parameters")

    def test_unknown_operation(self) -> None:
        self.rejected(self.action("INVENT_OUTCOME", {}), "walang-intent.schema.json", "capability")

    def test_wrong_parameters(self) -> None:
        self.rejected(self.action("SCOUT", {"distance": "five miles"}), "walang-intent.schema.json", "parameters")

    def test_negative_quantity(self) -> None:
        self.rejected(self.action("TAKE", {"target_ref": "item:barrel", "quantity_count": -1}), "walang-intent.schema.json", "parameters")

    def test_floating_quantity(self) -> None:
        self.rejected(self.action("WAIT", {"duration_s": 1.0}), "walang-intent.schema.json", "decode")

    def test_duplicate_json_keys(self) -> None:
        with self.assertRaises(ContractError):
            strict_loads('{"actor": "a", "actor": "b"}')

    def test_nonfinite_numbers(self) -> None:
        for raw in ('{"x": NaN}', '{"x": Infinity}', '{"x": 1e999}'):
            with self.subTest(raw=raw), self.assertRaises(ContractError):
                strict_loads(raw)

    def test_raw_byte_budget(self) -> None:
        with self.assertRaises(ContractError):
            strict_loads('"' + 'x' * 100 + '"', max_bytes=50)

    def test_contract_byte_budget(self) -> None:
        value = copy.deepcopy(self.base["intent"])
        value["extra"] = "x" * 65536
        self.rejected(value, "walang-intent.schema.json", "budget")

    def test_plan_depth(self) -> None:
        value = copy.deepcopy(self.base["intent"])
        step = copy.deepcopy(value["command"])
        for _ in range(5):
            value["command"] = {"kind": "PLAN", "mode": "SEQUENTIAL", "steps": [value["command"], copy.deepcopy(step)]}
        self.rejected(value, "walang-intent.schema.json", "budget")

    def test_total_action_budget(self) -> None:
        value = copy.deepcopy(self.base["intent"])
        step = value["command"]
        value["command"] = {"kind": "PLAN", "mode": "SEQUENTIAL", "steps": [
            {"kind": "PLAN", "mode": "PARALLEL", "steps": [copy.deepcopy(step) for _ in range(16)]},
            {"kind": "PLAN", "mode": "PARALLEL", "steps": [copy.deepcopy(step) for _ in range(17)]},
        ]}
        self.rejected(value, "walang-intent.schema.json", "budget")

    def test_empty_plan(self) -> None:
        value = copy.deepcopy(self.base["intent"])
        value["command"] = {"kind": "PLAN", "mode": "SEQUENTIAL", "steps": []}
        self.rejected(value, "walang-intent.schema.json", "schema")

    def test_identity_format(self) -> None:
        value = copy.deepcopy(self.base["intent"])
        value["actor_ref"] = "unbound plain name"
        self.rejected(value, "walang-intent.schema.json", "schema")

    def test_unknown_schema_version(self) -> None:
        value = copy.deepcopy(self.base["intent"])
        value["schema_version"] = "99.0.0"
        self.rejected(value, "walang-intent.schema.json", "schema")

    def test_future_command_not_claimed_supported(self) -> None:
        value = copy.deepcopy(self.base["intent"])
        value["command"] = {"kind": "GOAL", "goal": "anything"}
        self.rejected(value, "walang-intent.schema.json", "schema")

    def test_duplicate_limit(self) -> None:
        value = copy.deepcopy(self.base["intent"])
        value["command"]["constraints"] = [{"kind": "RETURN_BEFORE", "time_s": 100}] * 2
        self.rejected(value, "walang-intent.schema.json", "semantic")

    def test_offer_spending_limit(self) -> None:
        value = self.action("OFFER", {"recipient_ref": "actor:merchant", "offer_item_ref": "item:hide", "offer_count": 3, "request_item_ref": "item:tool", "request_count": 1, "max_extra_minor": 50, "currency": "CREDIT"})
        value["command"]["constraints"] = [{"kind": "MAX_SPEND", "amount_minor": 50, "currency": "CREDIT"}]
        validate_data(value, "walang-intent.schema.json")
        value["command"]["constraints"][0]["amount_minor"] = 49
        self.rejected(value, "walang-intent.schema.json", "semantic")

    def test_offer_currency_required(self) -> None:
        value = self.action("OFFER", {"recipient_ref": "actor:merchant", "offer_item_ref": "item:hide", "offer_count": 3, "request_item_ref": "item:tool", "request_count": 1, "max_extra_minor": 50})
        self.rejected(value, "walang-intent.schema.json", "parameters")

    def test_prototype_mass(self) -> None:
        value = copy.deepcopy(self.base["prototype"])
        value["mass_g"] = -1
        self.rejected(value, "object-prototype.schema.json", "schema")

    def test_event_producer(self) -> None:
        value = copy.deepcopy(self.base["event"])
        value["producer"] = "language_model"
        self.rejected(value, "world-event.schema.json", "schema")

    def test_self_transfer(self) -> None:
        value = copy.deepcopy(self.base["event"])
        value["event"]["destination_ref"] = value["event"]["source_ref"]
        self.rejected(value, "world-event.schema.json", "semantic")

    def test_other_event_variants(self) -> None:
        events = [
            {"type": "OBSERVATION_ACQUIRED", "observation_ref": "observation:one", "observer_ref": "actor:player", "subject_ref": "item:shelf", "proposition_ref": "proposition:scratches"},
            {"type": "BUILD_COMPLETED", "work_order_ref": "work:one", "site_ref": "site:bridge", "structure_ref": "structure:bridge", "prototype_ref": "prototype:bridge"},
        ]
        for event in events:
            value = copy.deepcopy(self.base["event"])
            value["event"] = event
            with self.subTest(event=event["type"]):
                validate_data(value, "world-event.schema.json")

    def test_event_cannot_be_intent(self) -> None:
        self.rejected(self.base["event"], "walang-intent.schema.json", "schema")

    def test_save_replay_boundary(self) -> None:
        value = copy.deepcopy(self.base["save"])
        value["oldest_replay_sequence"] = 11
        self.rejected(value, "save-manifest.schema.json", "semantic")

    def test_save_timestamp(self) -> None:
        value = copy.deepcopy(self.base["save"])
        value["created_at_utc"] = "2026-02-30T00:00:00Z"
        self.rejected(value, "save-manifest.schema.json", "semantic")

    def test_seed_overflow(self) -> None:
        value = copy.deepcopy(self.base["save"])
        value["seed"] = str(2 ** 64)
        self.rejected(value, "save-manifest.schema.json", "semantic")

    def test_unknown_schema_path(self) -> None:
        self.rejected({}, "../../outside.json", "configuration")


if __name__ == "__main__":
    unittest.main()
