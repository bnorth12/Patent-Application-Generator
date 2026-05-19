# Agents – Patent Application Generator

This directory contains the LangGraph-based multi-agent implementations.

## Structure (Sprint 3+)

```
agents/
├── __init__.py
├── state.py               # LangGraph shared state TypedDict
├── orchestrator.py        # LangGraph graph definition and compilation
├── research_agent.py      # Research Agent node
├── synthesis_agent.py     # Synthesis Agent node
├── drafting_agent.py      # Drafting Agent node
├── review_agent.py        # Review & Compliance Agent node
└── models.py              # Pydantic data models (PatentDraft, etc.)
```

## Agent Overview

| Agent | Sprint | Description |
|-------|--------|-------------|
| Research Agent | Sprint 3 | Retrieves literature and prior art |
| Synthesis Agent | Sprint 4 | Identifies novel aspects and prior-art gaps |
| Drafting Agent | Sprint 5 | Generates structured patent application |
| Review & Compliance Agent | Sprint 6 | Validates draft against legal and prior-art criteria |

## Related Documents

- [Agent Design](../../docs/design/agent_design.md)
- [Conceptual Architecture](../../docs/architecture/conceptual_architecture.md)
