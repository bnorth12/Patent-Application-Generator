"""
test_sprint_structure.py – Unit tests for the sprint structure checker.

Tests: REQ-047 – The CI pipeline shall enforce sprint folder structure
       completeness before sprint work begins.
"""

import sys
import tempfile
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "scripts" / "governance"))

from check_sprint_structure import (  # noqa: E402
    REQUIRED_FILES,
    check_sprint_dir,
    find_sprint_dirs,
    EXCLUDED_DIRS,
)


class TestCheckSprintDir:
    """Unit tests for check_sprint_dir."""

    def _make_sprint_dir(self, files: list[str]) -> Path:
        """Create a temporary directory with the given files."""
        tmp = Path(tempfile.mkdtemp())
        for fname in files:
            (tmp / fname).write_text("content", encoding="utf-8")
        return tmp

    def test_complete_sprint_dir_no_violations(self):
        sprint_dir = self._make_sprint_dir(list(REQUIRED_FILES))
        violations = check_sprint_dir(sprint_dir)
        assert violations == []

    def test_missing_sprint_plan(self):
        files = [f for f in REQUIRED_FILES if f != "sprint_plan.md"]
        sprint_dir = self._make_sprint_dir(files)
        violations = check_sprint_dir(sprint_dir)
        assert any("sprint_plan.md" in v for v in violations)

    def test_missing_requirements(self):
        files = [f for f in REQUIRED_FILES if f != "requirements.md"]
        sprint_dir = self._make_sprint_dir(files)
        violations = check_sprint_dir(sprint_dir)
        assert any("requirements.md" in v for v in violations)

    def test_missing_stories(self):
        files = [f for f in REQUIRED_FILES if f != "stories.md"]
        sprint_dir = self._make_sprint_dir(files)
        violations = check_sprint_dir(sprint_dir)
        assert any("stories.md" in v for v in violations)

    def test_missing_entry_exit_criteria(self):
        files = [f for f in REQUIRED_FILES if f != "entry_exit_criteria.md"]
        sprint_dir = self._make_sprint_dir(files)
        violations = check_sprint_dir(sprint_dir)
        assert any("entry_exit_criteria.md" in v for v in violations)

    def test_missing_all_required_files(self):
        sprint_dir = self._make_sprint_dir(["some_other_file.md"])
        violations = check_sprint_dir(sprint_dir)
        assert len(violations) == len(REQUIRED_FILES)

    def test_extra_files_do_not_cause_violations(self):
        files = list(REQUIRED_FILES) + ["backlog.md", "retrospective.md"]
        sprint_dir = self._make_sprint_dir(files)
        violations = check_sprint_dir(sprint_dir)
        assert violations == []


class TestFindSprintDirs:
    """Unit tests for find_sprint_dirs with a simulated repo structure."""

    def _make_repo(self, sprint_names: list[str]) -> Path:
        tmp = Path(tempfile.mkdtemp())
        sprints_root = tmp / "sprints"
        sprints_root.mkdir()
        for name in sprint_names:
            (sprints_root / name).mkdir()
        return tmp

    def test_finds_sprint_dirs(self):
        repo = self._make_repo(["sprint_01", "sprint_02"])
        dirs = find_sprint_dirs(repo)
        assert len(dirs) == 2

    def test_excludes_sprint_template(self):
        repo = self._make_repo(["sprint_01", "sprint_template"])
        dirs = find_sprint_dirs(repo)
        names = [d.name for d in dirs]
        assert "sprint_template" not in names
        assert "sprint_01" in names

    def test_no_sprints_returns_empty(self):
        repo = self._make_repo([])
        dirs = find_sprint_dirs(repo)
        assert dirs == []

    def test_missing_sprints_dir_returns_empty(self):
        tmp = Path(tempfile.mkdtemp())
        dirs = find_sprint_dirs(tmp)
        assert dirs == []


class TestActualSprintStructure:
    """Smoke tests: verify actual sprint folders in the repository."""

    def test_sprint_01_has_required_files(self):
        sprint_dir = REPO_ROOT / "sprints" / "sprint_01"
        assert sprint_dir.exists(), "sprints/sprint_01 directory not found"
        violations = check_sprint_dir(sprint_dir)
        assert violations == [], (
            f"sprint_01 is missing required files: {violations}"
        )

    def test_sprint_02_has_required_files(self):
        sprint_dir = REPO_ROOT / "sprints" / "sprint_02"
        assert sprint_dir.exists(), "sprints/sprint_02 directory not found"
        violations = check_sprint_dir(sprint_dir)
        assert violations == [], (
            f"sprint_02 is missing required files: {violations}"
        )

    def test_sprint_template_is_excluded(self):
        """sprint_template must not appear in the list of sprint dirs to validate."""
        sprint_dirs = find_sprint_dirs(REPO_ROOT)
        names = [d.name for d in sprint_dirs]
        assert "sprint_template" not in names
