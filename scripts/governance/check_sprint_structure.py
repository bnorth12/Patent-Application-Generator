#!/usr/bin/env python3
"""
check_sprint_structure.py – Verify that every sprint folder under sprints/
contains the required four artefact files:

  - sprint_plan.md
  - requirements.md
  - stories.md
  - entry_exit_criteria.md

The sprint_template/ folder is excluded from validation.

Exit codes:
  0 – all sprint folders are complete
  1 – one or more sprint folders are missing required files
"""

import sys
from pathlib import Path


REQUIRED_FILES = {
    "sprint_plan.md",
    "requirements.md",
    "stories.md",
    "entry_exit_criteria.md",
}

EXCLUDED_DIRS = {"sprint_template"}


def find_sprint_dirs(repo_root: Path) -> list[Path]:
    sprints_root = repo_root / "sprints"
    if not sprints_root.exists():
        return []
    return sorted(
        d for d in sprints_root.iterdir()
        if d.is_dir() and d.name not in EXCLUDED_DIRS
    )


def check_sprint_dir(sprint_dir: Path) -> list[str]:
    violations = []
    existing = {f.name for f in sprint_dir.iterdir() if f.is_file()}
    for required in sorted(REQUIRED_FILES):
        if required not in existing:
            violations.append(
                f"{sprint_dir.name}: Missing required file '{required}'"
            )
    return violations


def main() -> int:
    repo_root = Path(__file__).resolve().parents[2]
    sprint_dirs = find_sprint_dirs(repo_root)

    if not sprint_dirs:
        print("WARNING: No sprint directories found under sprints/.")
        return 0

    all_violations = []
    for sprint_dir in sprint_dirs:
        print(f"Checking sprint: {sprint_dir.name}")
        violations = check_sprint_dir(sprint_dir)
        all_violations.extend(violations)

    if all_violations:
        print(f"\n{len(all_violations)} sprint structure violation(s) found:\n")
        for v in all_violations:
            print(f"  ERROR: {v}")
        return 1

    print(f"\nAll {len(sprint_dirs)} sprint folder(s) have the required artefacts.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
