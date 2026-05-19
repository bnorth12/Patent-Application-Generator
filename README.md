# Patent Application Generator

A **multi-agent, skill-based AI platform** that researches topics in **system security** and **cyber security architecture** and generates complete patent application drafts. Built with Python + LangGraph agents, a CakePHP REST API backend, an HTML5 frontend, and a RAG (Retrieval-Augmented Generation) pipeline backed by a vector database.

---

## Architecture

```
HTML Frontend ──► CakePHP Backend API ──► Python / LangGraph Orchestrator
                                                        │
                                               ┌────────┴────────┐
                                          Vector DB (RAG)    LLM API
```

**Full details**: [Conceptual Architecture](docs/architecture/conceptual_architecture.md) | [System Architecture](docs/architecture/system_architecture.md) | [Technology Stack](docs/architecture/technology_stack.md)

---

## Repository Structure

```
├── .github/          # CI/CD workflows, PR templates, issue templates
├── docs/
│   ├── architecture/ # Conceptual & system architecture, technology stack
│   ├── design/       # Conceptual design, agent & skills design
│   ├── governance/   # Governance policy, DoD, branching strategy, standards
│   ├── plans/        # Overall dev plan, project, implementation, engineering, verification plans
│   └── requirements/ # System requirements (noun-verb format)
├── backlog/          # Product backlog and refinement guide
├── sprints/          # Sprint artefacts (plan, requirements, stories, criteria)
│   ├── sprint_template/
│   ├── sprint_01/    # BUILT – NOT EXECUTED (pending governance completion)
│   └── sprint_02/
├── src/
│   ├── agents/       # LangGraph agents (Sprint 3+)
│   ├── skills/       # Pluggable skill callables (Sprint 3+)
│   ├── rag/          # RAG ingestion pipeline (Sprint 2+)
│   ├── backend/      # CakePHP application (Sprint 2+)
│   └── frontend/     # HTML templates and static assets (Sprint 8+)
├── tests/
│   ├── governance/   # Governance enforcement tests ✅
│   ├── agents/       # Agent unit tests (Sprint 3+)
│   ├── skills/       # Skill unit tests (Sprint 3+)
│   └── rag/          # RAG pipeline tests (Sprint 2+)
└── scripts/
    └── governance/   # check_requirements.py, check_sprint_structure.py, etc.
```

---

## Governance

All requirements follow **noun-verb format**: `The <noun> shall <verb> <predicate>.`

Governance is **automatically enforced** on every PR:
- Requirements format validation (`scripts/governance/check_requirements.py`)
- Sprint structure completeness check (`scripts/governance/check_sprint_structure.py`)
- Definition of Done references check
- Code lint (flake8)
- Full test suite

See [Governance Policy](docs/governance/governance_policy.md) | [Definition of Done](docs/governance/definition_of_done.md) | [Branching Strategy](docs/governance/branching_strategy.md)

---

## Development Approach

Sprint-based, 2-week sprints. One branch per sprint: `sprint/sprint-NN`.

| Phase | Sprints | Theme |
|-------|---------|-------|
| Foundation | 1–2 | Governance, infrastructure, RAG pipeline |
| Core Agents | 3–4 | Research Agent, Synthesis Agent |
| Drafting | 5–6 | Drafting Agent, Review Agent, full pipeline |
| Backend | 7 | CakePHP REST API |
| Frontend | 8 | HTML GUI |
| QA & Release | 9–10 | Integration tests, v1.0.0 release |

Full plan: [Overall Development Plan](docs/plans/overall_development_plan.md)

---

## Quick Start (Governance Tests)

```bash
# Install Python test dependencies
pip install pytest

# Run governance tests
pytest tests/governance/ -v

# Run requirements format check
python scripts/governance/check_requirements.py

# Run sprint structure check
python scripts/governance/check_sprint_structure.py
```

---

## Sprint 1 Status

> ⚠️ **Sprint 01 is BUILT but NOT EXECUTING.**
> The sprint plan, requirements, stories, and entry/exit criteria are all in place.
> Sprint 01 execution starts when all entry criteria in
> [`sprints/sprint_01/entry_exit_criteria.md`](sprints/sprint_01/entry_exit_criteria.md) are verified.

---

## License

MIT – see [LICENSE](LICENSE)
