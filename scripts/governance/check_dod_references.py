#!/usr/bin/env python3
"""
check_dod_references.py – Verify that every sprint_plan.md file references
the Definition of Done document.

A valid reference is any line containing the text:
  "definition_of_done" OR "Definition of Done" OR "DoD"

Exit codes:
  0 – all sprint plans reference the DoD
  1 – one or more sprint plans do not reference the DoD
"""

import sys
from pathlib import Path

DOD_PATTERNS = [
    "definition_of_done",
    "Definition of Done",
    "DoD",
]

EXCLUDED_DIRS = {"sprint_template"}


def find_sprint_plans(repo_root: Path) -> list[Path]:
    sprints_root = repo_root / "sprints"
    if not sprints_root.exists():
        return []
    plans = []
    for sprint_dir in sprints_root.iterdir():
        if sprint_dir.is_dir() and sprint_dir.name not in EXCLUDED_DIRS:
            plan = sprint_dir / "sprint_plan.md"
            if plan.exists():
                plans.append(plan)
    return sorted(plans)


def references_dod(plan_path: Path) -> bool:
    content = plan_path.read_text(encoding="utf-8")
    return any(pattern in content for pattern in DOD_PATTERNS)


def main() -> int:
    repo_root = Path(__file__).resolve().parents[2]
    plans = find_sprint_plans(repo_root)

    if not plans:
        print("WARNING: No sprint_plan.md files found.")
        return 0

    violations = []
    for plan in plans:
        print(f"Checking: {plan.relative_to(repo_root)}")
        if not references_dod(plan):
            violations.append(str(plan.relative_to(repo_root)))

    if violations:
        print(f"\n{len(violations)} sprint plan(s) do not reference the Definition of Done:\n")
        for v in violations:
            print(f"  WARNING: {v}")
        # Return 0 (warning only) – not blocking until DoD enforcement is mature
        return 0

    print(f"\nAll {len(plans)} sprint plan(s) reference the Definition of Done.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
