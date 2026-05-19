# Skills – Patent Application Generator

This directory contains the pluggable skill callables used by agents.

## Structure (Sprint 3+)

```
skills/
├── __init__.py
├── registry.py                     # Skill Registry – dynamic skill registration
├── web_search_skill.py             # Web Search Skill (Sprint 3)
├── semantic_search_skill.py        # Semantic Search Skill (Sprint 3)
├── summarisation_skill.py          # Summarisation Skill (Sprint 3)
├── cybersecurity_taxonomy_skill.py # Cybersecurity Taxonomy Skill (Sprint 4)
├── prior_art_analysis_skill.py     # Prior Art Analysis Skill (Sprint 4)
└── patent_claim_formatter_skill.py # Patent Claim Formatter Skill (Sprint 5)
```

## Skill Interface

Each skill is a Python callable wrapped in a `Skill` dataclass:

```python
@dataclass
class Skill:
    name: str
    description: str
    callable: Callable
    input_schema: type   # Pydantic model
    output_schema: type  # Pydantic model
```

Skills are registered in the `SkillRegistry` and injected into agent nodes at runtime.

## Related Documents

- [Agent Design](../../docs/design/agent_design.md)
- [Technology Stack](../../docs/architecture/technology_stack.md)
