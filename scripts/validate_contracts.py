#!/usr/bin/env python3
"""Validate the architecture contract seed; does not execute game simulation."""
from __future__ import annotations

import json
import math
from datetime import datetime
from functools import lru_cache
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, ValidationError

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_NAMES = (
    "walang-intent.schema.json", "object-prototype.schema.json",
    "world-event.schema.json", "save-manifest.schema.json",
)
FIXTURE_SCHEMAS = dict(zip(("intent", "prototype", "event", "save"), SCHEMA_NAMES))


class ContractError(ValueError):
    def __init__(self, stage: str, message: str) -> None:
        self.stage = stage
        super().__init__(f"{stage}: {message}")


def bounded_shape(value: Any, max_depth: int = 64, reject_floats: bool = False) -> None:
    stack = [(value, 0)]
    nodes = 0
    while stack:
        item, depth = stack.pop()
        nodes += 1
        if depth > max_depth or nodes > 100000:
            raise ContractError("budget", "JSON depth or node budget exceeded")
        if isinstance(item, float) and (reject_floats or not math.isfinite(item)):
            raise ContractError("decode", "nonfinite/floating numeric values are not allowed here")
        if isinstance(item, dict):
            stack.extend((child, depth + 1) for child in item.values())
        elif isinstance(item, list):
            stack.extend((child, depth + 1) for child in item)


def strict_loads(text: str, max_bytes: int = 4 * 1024 * 1024) -> Any:
    def pairs(items: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in items:
            if key in result:
                raise ContractError("decode", f"duplicate JSON key: {key}")
            result[key] = value
        return result

    def constant(value: str) -> Any:
        raise ContractError("decode", f"invalid JSON numeric constant: {value}")

    try:
        if len(text.encode("utf-8")) > max_bytes:
            raise ContractError("budget", "JSON byte budget exceeded")
        value = json.loads(text, object_pairs_hook=pairs, parse_constant=constant)
        bounded_shape(value)
        return value
    except (json.JSONDecodeError, UnicodeError, RecursionError) as exc:
        raise ContractError("decode", str(exc)) from exc


def read_json(path: Path) -> Any:
    return strict_loads(path.read_text(encoding="utf-8"))


@lru_cache(maxsize=1)
def environment() -> tuple[dict[str, Draft202012Validator], dict[str, Draft202012Validator]]:
    schemas: dict[str, Draft202012Validator] = {}
    for name in SCHEMA_NAMES:
        schema = read_json(ROOT / "contracts" / name)
        Draft202012Validator.check_schema(schema)
        schemas[name] = Draft202012Validator(schema)
    registry = read_json(ROOT / "contracts/operation-registry.json")
    if registry.get("runtime_status") != "not_implemented":
        raise ContractError("configuration", "update qualification before changing runtime status")
    operations: dict[str, Draft202012Validator] = {}
    for name, entry in registry["operations"].items():
        Draft202012Validator.check_schema(entry["parameter_schema"])
        operations[name] = Draft202012Validator(entry["parameter_schema"])
    return schemas, operations


def validate_data(data: Any, schema_name: str) -> None:
    bounded_shape(data, max_depth=20, reject_floats=True)
    try:
        encoded = json.dumps(data, ensure_ascii=False, allow_nan=False).encode("utf-8")
    except (ValueError, UnicodeError, TypeError, RecursionError) as exc:
        raise ContractError("decode", str(exc)) from exc
    if len(encoded) > 65536:
        raise ContractError("budget", "contract instance exceeds 64 KiB")
    schemas, operations = environment()
    if schema_name not in schemas:
        raise ContractError("configuration", "unknown local schema")
    try:
        schemas[schema_name].validate(data)
    except ValidationError as exc:
        raise ContractError("schema", exc.message) from exc

    if schema_name == "walang-intent.schema.json":
        stack = [(data["command"], 0)]
        action_count = 0
        while stack:
            command, depth = stack.pop()
            if depth > 4:
                raise ContractError("budget", "plan nesting exceeds four levels")
            if command["kind"] == "PLAN":
                stack.extend((step, depth + 1) for step in reversed(command["steps"]))
                continue
            action_count += 1
            if action_count > 32:
                raise ContractError("budget", "plan exceeds 32 actions")
            operation = command["operation"]
            if operation not in operations:
                raise ContractError("capability", f"operation not in contract profile: {operation}")
            try:
                operations[operation].validate(command["parameters"])
            except ValidationError as exc:
                raise ContractError("parameters", exc.message) from exc
            singletons: set[str] = set()
            for constraint in command.get("constraints", []):
                kind = constraint["kind"]
                if kind != "ABORT_IF":
                    if kind in singletons:
                        raise ContractError("semantic", f"duplicate {kind} constraint")
                    singletons.add(kind)
                if kind == "MAX_SPEND" and operation == "OFFER":
                    params = command["parameters"]
                    if "max_extra_minor" in params and (
                        params["currency"] != constraint["currency"]
                        or params["max_extra_minor"] > constraint["amount_minor"]
                    ):
                        raise ContractError("semantic", "offer exceeds or conflicts with spending limit")
    elif schema_name == "save-manifest.schema.json":
        if data["oldest_replay_sequence"] > data["last_event_sequence"]:
            raise ContractError("semantic", "replay boundary exceeds last committed event")
        if int(data["seed"]) >= 2 ** 64:
            raise ContractError("semantic", "seed exceeds unsigned 64-bit range")
        try:
            datetime.strptime(data["created_at_utc"], "%Y-%m-%dT%H:%M:%SZ")
        except ValueError as exc:
            raise ContractError("semantic", "invalid UTC timestamp") from exc
    elif schema_name == "world-event.schema.json":
        event = data["event"]
        if event["type"] == "RESOURCE_TRANSFERRED" and event["source_ref"] == event["destination_ref"]:
            raise ContractError("semantic", "transfer source and destination must differ")


def main() -> int:
    try:
        schemas, operations = environment()
        fixtures = read_json(ROOT / "examples/contracts/baselines.json")
        if set(fixtures) != set(FIXTURE_SCHEMAS):
            raise ContractError("configuration", "baseline fixture coverage differs from schema coverage")
        for name, data in fixtures.items():
            validate_data(data, FIXTURE_SCHEMAS[name])
        print(f"PASS: {len(schemas)} schemas, {len(operations)} operation contracts, {len(fixtures)} positive baselines")
        print("Scope: structural/static contract validation only; no gameplay, model or device execution.")
        return 0
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"FAIL: {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
