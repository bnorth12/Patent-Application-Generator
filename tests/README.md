# Tests – Patent Application Generator

## Overview

All automated tests are stored here, mirroring the `src/` structure.

## Test Structure

```
tests/
├── governance/              # Governance enforcement tests (Sprint 1)
│   ├── test_requirements_format.py
│   └── test_sprint_structure.py
├── agents/                  # Agent unit tests (Sprint 3+)
├── skills/                  # Skill unit tests (Sprint 3+)
├── rag/                     # RAG pipeline tests (Sprint 2+)
├── backend/                 # PHP API tests (Sprint 7+)
└── e2e/                     # End-to-end tests (Sprint 6+)
```

## Running Tests

```bash
# Install development dependencies
pip install -r src/requirements-dev.txt

# Run governance tests only
pytest tests/governance/ -v

# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ -v --cov=src --cov-report=term-missing
```

## Test Conventions

- Test files named `test_<module>.py`.
- Each test function starts with `test_`.
- Each test includes a comment linking to the requirement(s) it verifies.
- Tests use only pytest and Python stdlib (unless the component under test requires otherwise).

## Related Documents

- [Verification Plan](../docs/plans/verification_plan.md)
- [Definition of Done](../docs/governance/definition_of_done.md)
