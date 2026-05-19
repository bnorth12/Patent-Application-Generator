"""
test_requirements_format.py – Unit tests for the requirements format checker.

Tests: REQ-046 – The CI pipeline shall validate all requirements documents
       for noun-verb format compliance on every PR.
"""

import sys
from pathlib import Path
import tempfile
import textwrap

import pytest

# Add scripts directory to path so we can import the governance scripts
REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "scripts" / "governance"))

from check_requirements import validate_requirement, check_file  # noqa: E402


class TestValidateRequirement:
    """Unit tests for the validate_requirement function."""

    def _check(self, req_id: str, req_text: str) -> list[str]:
        return validate_requirement(req_id, req_text, Path("test.md"), 1)

    # ------------------------------------------------------------------ #
    # Valid requirements – should produce zero violations                  #
    # ------------------------------------------------------------------ #

    def test_valid_requirement_no_violations(self):
        violations = self._check(
            "REQ-001",
            "The Research Agent shall retrieve at least 10 documents per query."
        )
        assert violations == []

    def test_valid_requirement_with_complex_predicate(self):
        violations = self._check(
            "REQ-042",
            "The frontend shall present the generated patent draft in a readable, editable format."
        )
        assert violations == []

    def test_valid_sprint_requirement(self):
        violations = self._check(
            "SPR-01-R01",
            "The repository shall contain a complete directory structure as defined in the engineering plan."
        )
        assert violations == []

    # ------------------------------------------------------------------ #
    # Missing "The " prefix                                                #
    # ------------------------------------------------------------------ #

    def test_missing_the_prefix(self):
        violations = self._check("REQ-002", "System shall generate a draft.")
        assert any("start with 'The '" in v for v in violations)

    def test_lowercase_the_fails(self):
        violations = self._check("REQ-003", "the system shall do something.")
        assert any("start with 'The '" in v for v in violations)

    # ------------------------------------------------------------------ #
    # Missing "shall"                                                      #
    # ------------------------------------------------------------------ #

    def test_missing_shall(self):
        violations = self._check("REQ-004", "The system generates a draft.")
        assert any("' shall '" in v for v in violations)

    # ------------------------------------------------------------------ #
    # Missing trailing period                                              #
    # ------------------------------------------------------------------ #

    def test_missing_trailing_period(self):
        violations = self._check(
            "REQ-005",
            "The system shall generate a draft"
        )
        assert any("end with '.'" in v for v in violations)

    # ------------------------------------------------------------------ #
    # Disallowed modal verbs                                               #
    # ------------------------------------------------------------------ #

    def test_should_is_disallowed(self):
        violations = self._check("REQ-006", "The system should generate a draft.")
        assert any("should" in v for v in violations)

    def test_must_is_disallowed(self):
        violations = self._check("REQ-007", "The system must generate a draft.")
        assert any("must" in v for v in violations)

    def test_will_is_disallowed(self):
        violations = self._check("REQ-008", "The system will generate a draft.")
        assert any("will" in v for v in violations)

    def test_may_is_disallowed(self):
        violations = self._check("REQ-009", "The system may generate a draft.")
        assert any("may" in v for v in violations)

    def test_shall_is_allowed(self):
        """'shall' must not trigger the disallowed modal check."""
        violations = self._check(
            "REQ-010",
            "The system shall generate a complete draft."
        )
        # No disallowed modal violation
        assert not any("disallowed" in v for v in violations)

    # ------------------------------------------------------------------ #
    # Multiple violations                                                  #
    # ------------------------------------------------------------------ #

    def test_multiple_violations(self):
        """A badly formed requirement should produce multiple violations."""
        violations = self._check(
            "REQ-011",
            "system should produce a result"
        )
        # Missing "The ", missing " shall ", missing ".", has "should"
        assert len(violations) >= 3


class TestCheckFile:
    """Integration tests for check_file() reading actual Markdown files."""

    def _write_requirements_md(self, content: str) -> Path:
        tmp = tempfile.NamedTemporaryFile(
            mode="w", suffix=".md", delete=False, encoding="utf-8"
        )
        tmp.write(content)
        tmp.flush()
        return Path(tmp.name)

    def test_valid_requirements_file(self):
        content = textwrap.dedent("""\
            ## Sprint Requirements

            | ID | Requirement | Backlog Item | Status |
            |----|-------------|-------------|--------|
            | SPR-01-R01 | The repository shall contain a complete directory structure. | BL-001 | To Do |
            | SPR-01-R02 | The governance policy document shall define requirements format. | BL-001 | To Do |
        """)
        path = self._write_requirements_md(content)
        violations = check_file(path)
        assert violations == []

    def test_invalid_requirements_file(self):
        content = textwrap.dedent("""\
            ## Sprint Requirements

            | ID | Requirement | Backlog Item | Status |
            |----|-------------|-------------|--------|
            | SPR-01-R01 | system should do stuff | BL-001 | To Do |
        """)
        path = self._write_requirements_md(content)
        violations = check_file(path)
        assert len(violations) > 0

    def test_empty_file_no_violations(self):
        """A file with no requirement rows should produce zero violations."""
        content = "# No requirements here\n\nJust some prose.\n"
        path = self._write_requirements_md(content)
        violations = check_file(path)
        assert violations == []


class TestActualSystemRequirements:
    """Smoke test: validate the actual system_requirements.md in the repo."""

    def test_system_requirements_pass_format_check(self):
        req_file = REPO_ROOT / "docs" / "requirements" / "system_requirements.md"
        assert req_file.exists(), f"system_requirements.md not found at {req_file}"
        violations = check_file(req_file)
        assert violations == [], (
            f"system_requirements.md has {len(violations)} format violation(s):\n"
            + "\n".join(violations)
        )

    def test_sprint_01_requirements_pass_format_check(self):
        req_file = REPO_ROOT / "sprints" / "sprint_01" / "requirements.md"
        assert req_file.exists(), f"sprint_01/requirements.md not found"
        violations = check_file(req_file)
        assert violations == [], (
            f"sprint_01/requirements.md has {len(violations)} format violation(s):\n"
            + "\n".join(violations)
        )

    def test_sprint_02_requirements_pass_format_check(self):
        req_file = REPO_ROOT / "sprints" / "sprint_02" / "requirements.md"
        assert req_file.exists(), f"sprint_02/requirements.md not found"
        violations = check_file(req_file)
        assert violations == [], (
            f"sprint_02/requirements.md has {len(violations)} format violation(s):\n"
            + "\n".join(violations)
        )
