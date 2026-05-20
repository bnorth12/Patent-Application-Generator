import json
import tempfile
import time
import unittest
from pathlib import Path

import sys


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from patent_draft_generator import PatentInput, generate_patent_draft, write_draft


class TestPatentDraftGenerator(unittest.TestCase):
    def test_generate_draft_contains_required_sections(self) -> None:
        draft = generate_patent_draft(
            PatentInput(
                title="Example Invention",
                inventors=["Alex Inventor"],
                field_of_invention="Automation",
                background="Background text.",
                summary="Summary text.",
                abstract="Abstract text.",
                claims=["A system comprising..."],
            )
        )

        required_headers = [
            "# Patent Application Draft",
            "## Title",
            "## Inventors",
            "## Field Of The Invention",
            "## Background",
            "## Summary",
            "## Abstract",
            "## Claims",
        ]
        for header in required_headers:
            self.assertIn(header, draft)

    def test_write_draft_generates_output_file(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            input_path = temp_path / "input.json"
            output_path = temp_path / "output.md"

            payload = {
                "title": "Generated From File",
                "inventors": ["Casey Tester"],
                "claims": ["A generated claim."],
            }
            input_path.write_text(json.dumps(payload), encoding="utf-8")

            write_draft(input_path, output_path)

            self.assertTrue(output_path.exists())
            text = output_path.read_text(encoding="utf-8")
            self.assertIn("Generated From File", text)
            self.assertIn("A generated claim.", text)

    def test_generation_performance_under_two_minutes(self) -> None:
        start = time.perf_counter()
        _ = generate_patent_draft(
            PatentInput(
                title="Performance Check",
                inventors=["Speed Validator"],
                claims=["A performance validation claim."] * 10,
            )
        )
        elapsed = time.perf_counter() - start
        self.assertLess(elapsed, 120.0)


if __name__ == "__main__":
    unittest.main()
