import argparse
import json
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import List


@dataclass
class PatentInput:
    title: str
    inventors: List[str] = field(default_factory=list)
    abstract: str = ""
    field_of_invention: str = ""
    background: str = ""
    summary: str = ""
    claims: List[str] = field(default_factory=list)


def _bulleted(lines: List[str], fallback: str) -> str:
    if not lines:
        return f"- {fallback}"
    return "\n".join(f"- {line}" for line in lines)


def generate_patent_draft(patent_input: PatentInput) -> str:
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    inventors = ", ".join(patent_input.inventors) if patent_input.inventors else "Not specified"

    sections = [
        "# Patent Application Draft",
        "",
        f"Generated: {timestamp}",
        "",
        f"## Title\n{patent_input.title or 'Untitled Invention'}",
        "",
        f"## Inventors\n{inventors}",
        "",
        f"## Field Of The Invention\n{patent_input.field_of_invention or 'To be provided.'}",
        "",
        f"## Background\n{patent_input.background or 'To be provided.'}",
        "",
        f"## Summary\n{patent_input.summary or 'To be provided.'}",
        "",
        f"## Abstract\n{patent_input.abstract or 'To be provided.'}",
        "",
        "## Claims",
        _bulleted(patent_input.claims, "Claim text to be provided."),
    ]
    return "\n".join(sections).strip() + "\n"


def load_input(input_path: Path) -> PatentInput:
    payload = json.loads(input_path.read_text(encoding="utf-8"))
    return PatentInput(
        title=payload.get("title", "").strip(),
        inventors=payload.get("inventors", []),
        abstract=payload.get("abstract", "").strip(),
        field_of_invention=payload.get("field_of_invention", "").strip(),
        background=payload.get("background", "").strip(),
        summary=payload.get("summary", "").strip(),
        claims=payload.get("claims", []),
    )


def write_draft(input_path: Path, output_path: Path) -> None:
    patent_input = load_input(input_path)
    draft = generate_patent_draft(patent_input)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(draft, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a patent draft from structured input JSON.")
    parser.add_argument("--input", required=True, help="Path to input JSON")
    parser.add_argument("--output", required=True, help="Path to output markdown draft")
    args = parser.parse_args()

    write_draft(Path(args.input), Path(args.output))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
