#!/usr/bin/env python3
"""Validate Project Oregon Trail's append-only timestamped run history."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

RUN_HISTORY = Path("project-control/RUN_HISTORY.jsonl")
REQUIRED_FIELDS = {
    "timestamp_utc",
    "actor",
    "category",
    "summary",
    "reason",
    "files",
    "validation",
}
ALLOWED_CATEGORIES = {
    "design",
    "architecture",
    "documentation",
    "code",
    "data",
    "schema",
    "asset",
    "test",
    "tooling",
    "build",
    "ci",
    "bugfix",
    "refactor",
    "experiment",
    "decision",
    "revert",
    "release",
}
TIMESTAMP_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")


def git(*args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        check=check,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


def read_lines(path: Path) -> list[str]:
    if not path.exists():
        return []
    return [line for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def read_base_lines(base: str) -> list[str]:
    result = git("show", f"{base}:{RUN_HISTORY.as_posix()}", check=False)
    if result.returncode != 0:
        return []
    return [line for line in result.stdout.splitlines() if line.strip()]


def changed_paths(base: str) -> set[str]:
    result = git("diff", "--name-only", f"{base}...HEAD")
    return {line.strip() for line in result.stdout.splitlines() if line.strip()}


def parse_entry(raw: str, line_number: int) -> dict:
    try:
        entry = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ValueError(f"RUN_HISTORY line {line_number} is not valid JSON: {exc}") from exc

    if not isinstance(entry, dict):
        raise ValueError(f"RUN_HISTORY line {line_number} must be a JSON object")

    missing = sorted(REQUIRED_FIELDS - entry.keys())
    if missing:
        raise ValueError(
            f"RUN_HISTORY line {line_number} is missing required fields: {', '.join(missing)}"
        )

    timestamp = entry["timestamp_utc"]
    if not isinstance(timestamp, str) or not TIMESTAMP_RE.fullmatch(timestamp):
        raise ValueError(
            f"RUN_HISTORY line {line_number} timestamp_utc must use YYYY-MM-DDTHH:MM:SSZ"
        )
    try:
        datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ")
    except ValueError as exc:
        raise ValueError(
            f"RUN_HISTORY line {line_number} contains an invalid UTC timestamp"
        ) from exc

    category = entry["category"]
    if category not in ALLOWED_CATEGORIES:
        raise ValueError(
            f"RUN_HISTORY line {line_number} category '{category}' is not allowed"
        )

    files = entry["files"]
    if not isinstance(files, list) or not files or not all(
        isinstance(path, str) and path.strip() for path in files
    ):
        raise ValueError(
            f"RUN_HISTORY line {line_number} files must be a non-empty list of repository paths"
        )

    for field in ("actor", "summary", "reason", "validation"):
        value = entry[field]
        if not isinstance(value, str) or not value.strip():
            raise ValueError(
                f"RUN_HISTORY line {line_number} field '{field}' must be a non-empty string"
            )

    return entry


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--base",
        required=True,
        help="Git base ref/commit to compare against, e.g. origin/main",
    )
    args = parser.parse_args()

    current_lines = read_lines(RUN_HISTORY)
    base_lines = read_base_lines(args.base)

    if base_lines and current_lines[: len(base_lines)] != base_lines:
        print(
            "ERROR: project-control/RUN_HISTORY.jsonl is append-only; existing base entries were modified or removed.",
            file=sys.stderr,
        )
        return 1

    new_lines = current_lines[len(base_lines) :]
    changes = changed_paths(args.base)
    meaningful_changes = changes - {RUN_HISTORY.as_posix()}

    if meaningful_changes and not new_lines:
        print(
            "ERROR: repository changes were detected but no new RUN_HISTORY.jsonl entries were appended.",
            file=sys.stderr,
        )
        return 1

    entries: list[dict] = []
    try:
        for index, raw in enumerate(current_lines, start=1):
            entries.append(parse_entry(raw, index))
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    new_entries = entries[len(base_lines) :]
    covered_paths = {
        path
        for entry in new_entries
        for path in entry.get("files", [])
    }

    missing_coverage = sorted(meaningful_changes - covered_paths)
    if missing_coverage:
        print(
            "ERROR: changed paths are missing from newly appended RUN_HISTORY entries:",
            file=sys.stderr,
        )
        for path in missing_coverage:
            print(f"  - {path}", file=sys.stderr)
        return 1

    print(
        f"RUN_HISTORY validation passed: {len(new_entries)} new entr"
        f"{'y' if len(new_entries) == 1 else 'ies'} cover {len(meaningful_changes)} changed path(s)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
