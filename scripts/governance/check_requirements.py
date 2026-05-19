#!/usr/bin/env python3
"""
check_requirements.py – Validate that all requirements in the repository
follow the mandatory noun-verb format:

    The <noun> shall <verb> <predicate>.

Rules enforced:
  1. Each requirement line must start with "The ".
  2. Each requirement line must contain " shall ".
  3. Each requirement line must end with ".".
  4. Each requirement line must NOT use "should", "must", "will", or "may"
     as a modal verb in place of "shall".

The script scans every requirements.md file under docs/requirements/
and sprints/*/requirements.md.

Exit codes:
  0 – no violations found
  1 – one or more violations found
"""

import re
import sys
from pathlib import Path


# Paths to scan (relative to repository root)
REQUIREMENTS_GLOB_PATTERNS = [
    "docs/requirements/system_requirements.md",
    "sprints/*/requirements.md",
]

# Regex to identify a requirement row in a Markdown table
# Matches lines that look like: | REQ-NNN | The ... |
REQUIREMENT_ROW_RE = re.compile(
    r"^\|\s*(REQ-\d+|SPR-\d+-R\d+|FTR-\w+-\d+)\s*\|\s*(.+?)\s*\|",
)

# Disallowed modal verbs
DISALLOWED_MODALS = re.compile(r"\b(should|must|will|may)\b", re.IGNORECASE)


def find_requirements_files(repo_root: Path) -> list[Path]:
    """Return all requirements.md files matching the scan patterns."""
    files = []
    for pattern in REQUIREMENTS_GLOB_PATTERNS:
        files.extend(repo_root.glob(pattern))
    return sorted(set(files))


def extract_requirement_text(row_text: str) -> str:
    """Extract the requirement text from the second column of a table row."""
    # The table cell may contain trailing pipe characters or whitespace
    return row_text.strip().rstrip("|").strip()


def validate_requirement(req_id: str, req_text: str, file_path: Path, line_no: int) -> list[str]:
    """Validate a single requirement and return a list of violation messages."""
    violations = []

    if not req_text.startswith("The "):
        violations.append(
            f"{file_path}:{line_no}: [{req_id}] Requirement must start with 'The '. "
            f"Got: '{req_text[:60]}...'"
        )

    if " shall " not in req_text:
        violations.append(
            f"{file_path}:{line_no}: [{req_id}] Requirement must contain ' shall '. "
            f"Got: '{req_text[:60]}...'"
        )

    if not req_text.rstrip().endswith("."):
        violations.append(
            f"{file_path}:{line_no}: [{req_id}] Requirement must end with '.'. "
            f"Got: '...{req_text[-30:]}'"
        )

    match = DISALLOWED_MODALS.search(req_text)
    if match:
        violations.append(
            f"{file_path}:{line_no}: [{req_id}] Requirement uses disallowed modal verb "
            f"'{match.group()}'. Use 'shall' instead."
        )

    return violations


def check_file(file_path: Path) -> list[str]:
    """Scan a single requirements file and return all violations."""
    all_violations = []
    lines = file_path.read_text(encoding="utf-8").splitlines()

    for line_no, line in enumerate(lines, start=1):
        match = REQUIREMENT_ROW_RE.match(line)
        if not match:
            continue
        req_id = match.group(1)
        req_text = extract_requirement_text(match.group(2))
        violations = validate_requirement(req_id, req_text, file_path, line_no)
        all_violations.extend(violations)

    return all_violations


def main() -> int:
    repo_root = Path(__file__).resolve().parents[2]
    files = find_requirements_files(repo_root)

    if not files:
        print("WARNING: No requirements files found. Check REQUIREMENTS_GLOB_PATTERNS.")
        return 0

    all_violations = []
    for f in files:
        print(f"Checking: {f.relative_to(repo_root)}")
        all_violations.extend(check_file(f))

    if all_violations:
        print(f"\n{len(all_violations)} requirement violation(s) found:\n")
        for v in all_violations:
            print(f"  ERROR: {v}")
        return 1

    print(f"\nAll requirements in {len(files)} file(s) pass format validation.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
