#!/usr/bin/env python3
"""
validate_exit_criteria.py – Read the exit criteria checklist for a sprint
and report the status of each item.

Usage:
    python validate_exit_criteria.py --sprint 01

Exit codes:
  0 – all exit criteria are checked (✅)
  1 – one or more exit criteria are unchecked (⬜)
  2 – entry_exit_criteria.md not found for the given sprint
"""

import argparse
import re
import sys
from pathlib import Path


CHECKED_PATTERN = re.compile(r"^\s*-\s*\[x\]", re.IGNORECASE)
UNCHECKED_PATTERN = re.compile(r"^\s*-\s*\[ \]")
EXIT_SECTION_HEADER = re.compile(r"^##\s+Exit Criteria", re.IGNORECASE)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate sprint exit criteria.")
    parser.add_argument("--sprint", required=True, help="Sprint number (e.g., 01)")
    return parser.parse_args()


def find_criteria_file(repo_root: Path, sprint: str) -> Path:
    sprint_dir = repo_root / "sprints" / f"sprint_{sprint}"
    criteria_file = sprint_dir / "entry_exit_criteria.md"
    if not criteria_file.exists():
        return None
    return criteria_file


def parse_exit_criteria(criteria_file: Path) -> tuple[list[str], list[str]]:
    """Parse exit criteria section. Returns (checked_items, unchecked_items)."""
    lines = criteria_file.read_text(encoding="utf-8").splitlines()
    in_exit_section = False
    checked = []
    unchecked = []

    for line in lines:
        if EXIT_SECTION_HEADER.match(line):
            in_exit_section = True
            continue
        # Stop at next section header
        if in_exit_section and re.match(r"^##\s+", line):
            break
        if not in_exit_section:
            continue
        if CHECKED_PATTERN.match(line):
            checked.append(line.strip())
        elif UNCHECKED_PATTERN.match(line):
            unchecked.append(line.strip())

    return checked, unchecked


def main() -> int:
    args = parse_args()
    repo_root = Path(__file__).resolve().parents[2]

    criteria_file = find_criteria_file(repo_root, args.sprint)
    if criteria_file is None:
        print(f"ERROR: entry_exit_criteria.md not found for sprint {args.sprint}")
        return 2

    checked, unchecked = parse_exit_criteria(criteria_file)

    print(f"Sprint {args.sprint} Exit Criteria Status:")
    print(f"  Checked   : {len(checked)}")
    print(f"  Unchecked : {len(unchecked)}")

    if unchecked:
        print("\nUnchecked exit criteria:")
        for item in unchecked:
            print(f"  ⬜ {item}")
        return 1

    print("\nAll exit criteria are verified. Sprint is ready to close.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
