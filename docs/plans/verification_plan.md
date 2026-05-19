# Verification Plan – Patent Application Generator

**Version**: 1.0  
**Date**: 2026-05-19  
**Owner**: @bnorth12

---

## 1. Purpose

This plan defines the strategy for verifying that the Patent Application Generator meets all stated requirements. It covers test levels, test types, tools, and per-sprint verification activities.

---

## 2. Verification Strategy

### 2.1 Levels of Testing

| Level | Description | Tools | When |
|-------|-------------|-------|------|
| Unit | Individual function/class behaviour | pytest (Python), PHPUnit (PHP) | Every commit |
| Integration | Component interaction (e.g., Agent + Skill) | pytest | Every sprint |
| System | End-to-end patent generation workflow | pytest + Playwright (or requests) | Sprints 6+ |
| Performance | Response time, throughput | locust / pytest-benchmark | Sprint 9 |
| Security | Vulnerability scan, input validation | pip-audit, OWASP ZAP | Sprint 9 |
| Governance | Requirements format, sprint structure | custom pytest suite | Every PR |

### 2.2 Test Coverage Target

- New Python source files: ≥ 80% line coverage.
- New PHP files: ≥ 80% line coverage.
- Governance tests: 100% pass (no tolerance for failure).

---

## 3. Test Organisation

```
tests/
├── governance/               # Governance enforcement tests
│   ├── test_requirements_format.py
│   ├── test_sprint_structure.py
│   └── test_dod_references.py
├── agents/                   # Agent unit tests (Sprint 3+)
│   ├── test_research_agent.py
│   ├── test_synthesis_agent.py
│   ├── test_drafting_agent.py
│   └── test_review_agent.py
├── skills/                   # Skill unit tests (Sprint 3+)
│   ├── test_web_search_skill.py
│   ├── test_semantic_search_skill.py
│   ├── test_summarisation_skill.py
│   ├── test_prior_art_analysis_skill.py
│   ├── test_cybersecurity_taxonomy_skill.py
│   └── test_patent_claim_formatter_skill.py
├── rag/                      # RAG pipeline tests (Sprint 2+)
│   ├── test_ingestor.py
│   └── test_vector_store.py
├── backend/                  # PHP API tests (Sprint 7+)
│   ├── PatentsControllerTest.php
│   └── AuthControllerTest.php
└── e2e/                      # End-to-end tests (Sprint 6+)
    └── test_patent_generation_workflow.py
```

---

## 4. Test Automation in CI

| Workflow | Tests Executed | Trigger |
|----------|---------------|---------|
| `ci.yml` | Governance tests + all Python tests | Every push / PR |
| `governance-check.yml` | Governance tests only | Every PR |
| `sprint-close.yml` | Governance tests + sprint exit criteria | Sprint-close trigger |

---

## 5. Per-Sprint Verification Plan

### Sprint 1
**What to verify**: Governance framework is complete and enforced.
- All governance scripts execute without errors.
- All governance pytest tests pass.
- CI workflow runs successfully on the sprint branch.
- Requirements document follows noun-verb format (validated by script).

### Sprint 2
**What to verify**: Development environment is functional; RAG ingestion works.
- `docker compose up` starts all services without errors.
- RAG ingestion pipeline successfully chunks and embeds a test document.
- Vector database stores and retrieves embeddings correctly.
- CakePHP application responds to health check.

### Sprint 3
**What to verify**: Research Agent produces correct output.
- Research Agent unit tests pass (≥ 80% coverage).
- Web Search Skill returns results for a test query.
- Semantic Search Skill retrieves relevant documents from the vector DB.
- Summarisation Skill produces coherent summaries.

### Sprint 4
**What to verify**: Synthesis Agent identifies novel aspects.
- Synthesis Agent unit tests pass.
- Prior Art Analysis Skill correctly identifies conflicts.
- Cybersecurity Taxonomy Skill correctly classifies test inputs.

### Sprint 5
**What to verify**: Drafting Agent produces valid patent structure.
- Drafting Agent unit tests pass.
- Patent Claim Formatter Skill produces USPTO-compliant claim structure.
- Draft data model persists correctly.

### Sprint 6
**What to verify**: Full agent pipeline produces a complete patent draft.
- End-to-end integration test: topic in → patent draft out.
- Re-drafting loop triggers correctly on compliance failure.
- All agent unit tests pass.

### Sprint 7
**What to verify**: REST API is correct and secure.
- All PatentJob API endpoints return correct status codes and data.
- Authentication rejects unauthenticated requests.
- Job queue dispatches jobs to the orchestrator correctly.

### Sprint 8
**What to verify**: Frontend is functional and usable.
- Patent submission form submits successfully.
- Job status page reflects real-time status.
- Draft review interface displays and saves edits.

### Sprint 9
**What to verify**: System meets non-functional requirements.
- Patent draft generation completes in ≤ 120 seconds.
- System handles 10 concurrent jobs without degradation.
- Security scan produces no critical/high vulnerabilities.
- All end-to-end tests pass.

### Sprint 10
**What to verify**: Release readiness.
- All tests passing on `main`.
- Docker images build and run successfully.
- Release notes complete and accurate.
- v1.0.0 tag created.

---

## 6. Requirements Traceability

Each test shall be linked to one or more requirements via a comment in the test file:

```python
# Tests: REQ-015 – The Research Agent shall retrieve at least 10 relevant documents per query.
def test_research_agent_returns_min_results():
    ...
```

A requirements traceability matrix will be maintained at `docs/requirements/traceability_matrix.md` from Sprint 3 onward.

---

## 7. Defect Management

- Defects raised as GitHub issues using the Bug Report template.
- Severity: Critical, High, Medium, Low.
- Critical and High defects shall be resolved before sprint close.
- All defects linked to the requirement(s) they violate.

---

## 8. Related Documents

- [Engineering Plan](engineering_plan.md)
- [Definition of Done](../governance/definition_of_done.md)
- [System Requirements](../requirements/system_requirements.md)
