#!/usr/bin/env python3
"""Check local documentation paths, JSON syntax and requirement/scenario coverage."""
from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

from validate_contracts import ROOT, read_json

SKIP_PARTS = {".git", ".venv", "venv", "__pycache__"}
LINK = re.compile(r"\[[^\]]*\]\(([^\s)]+)(?:\s+\"[^\"]*\")?\)")
SCENARIO = re.compile(r"\bSC-[A-Z]+(?:-[A-Z]+)*\b")


def included(path: Path) -> bool:
    return not (set(path.relative_to(ROOT).parts) & SKIP_PARTS)


def main() -> int:
    errors: list[str] = []
    json_files = [p for p in ROOT.rglob("*.json") if included(p)]
    for path in json_files:
        try:
            read_json(path)
        except (OSError, ValueError) as exc:
            errors.append(f"{path.relative_to(ROOT)}: {exc}")
    docs = [p for p in ROOT.rglob("*.md") if included(p)]
    links_checked = 0
    for path in docs:
        text = re.sub(r"```.*?```", "", path.read_text(encoding="utf-8"), flags=re.S)
        for raw in LINK.findall(text):
            parts = urlsplit(raw.strip("<>"))
            if parts.scheme or parts.netloc or not parts.path:
                continue
            target = (path.parent / unquote(parts.path)).resolve()
            links_checked += 1
            if not target.is_relative_to(ROOT) or not target.exists():
                errors.append(f"{path.relative_to(ROOT)}: unresolved local link {raw}")
    try:
        catalog = (ROOT / "docs/quality/SCENARIO_ACCEPTANCE_CATALOG.md").read_text(encoding="utf-8")
        declared = set(re.findall(r"^\| (SC-[A-Z]+(?:-[A-Z]+)*) \|", catalog, flags=re.M))
        rows = read_json(ROOT / "project-control/REQUIREMENTS_TRACEABILITY.json")["requirements"]
        required = {f"PR-{i:03d}" for i in range(1, 33)}
        found = [row["id"] for row in rows]
        if set(found) != required or len(found) != len(set(found)):
            errors.append("requirement IDs must cover PR-001 through PR-032 exactly once")
        requirements_doc = (ROOT / "docs/production/PRODUCT_REQUIREMENTS.md").read_text(encoding="utf-8")
        for row in rows:
            if not row.get("owner") or row["id"] not in requirements_doc:
                errors.append(f"{row['id']}: missing owner or product requirement")
            target = (ROOT / row["document"]).resolve()
            if not target.is_relative_to(ROOT) or not target.is_file():
                errors.append(f"{row['id']}: missing architecture document")
            if not row["scenarios"] or not set(row["scenarios"]).issubset(declared):
                errors.append(f"{row['id']}: undefined acceptance scenario")
            if row["status"] != "specified_not_runtime_verified":
                errors.append(f"{row['id']}: revise evidence policy before changing baseline status")
        for path in docs:
            if path.is_relative_to(ROOT / "docs"):
                unknown = set(SCENARIO.findall(path.read_text(encoding="utf-8"))) - declared
                if unknown:
                    errors.append(f"{path.relative_to(ROOT)}: undefined scenarios {sorted(unknown)}")
        index = (ROOT / "docs/README.md").read_text(encoding="utf-8")
        for path in (ROOT / "docs").rglob("*.md"):
            relative = path.relative_to(ROOT / "docs").as_posix()
            if relative != "README.md" and relative not in index:
                errors.append(f"documentation index is missing {relative}")
    except (OSError, ValueError, KeyError, TypeError) as exc:
        errors.append(f"traceability check: {exc}")
    if errors:
        print("FAIL:\n" + "\n".join(errors))
        return 1
    print(f"PASS: {len(docs)} Markdown files, {links_checked} local link paths, {len(json_files)} JSON files")
    print(f"PASS: {len(rows)} requirements mapped to {len(declared)} declared acceptance scenarios")
    print("Scope: local path/JSON/coverage checks; not external-link, gameplay or benchmark verification.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
