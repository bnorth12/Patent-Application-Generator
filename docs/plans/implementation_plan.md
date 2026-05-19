# Implementation Plan – Patent Application Generator

**Version**: 1.0  
**Date**: 2026-05-19  
**Owner**: @bnorth12

---

## 1. Purpose

This plan describes **how** the Patent Application Generator will be implemented: technology choices, component build order, integration approach, and per-sprint implementation focus.

---

## 2. Implementation Principles

1. **Framework First**: Infrastructure and governance are established before any feature code is written (Sprint 1–2).
2. **Agent-first, API-second**: Agent capabilities are proven in isolation (Sprints 3–6) before exposing them via the CakePHP API (Sprint 7).
3. **Incremental RAG Enrichment**: Each sprint populates the vector database with domain-relevant materials before the skills that consume them are implemented.
4. **Test-Driven Governance**: Governance scripts and tests are the first automated code written.
5. **Docker from Day 1**: All components run in containers from Sprint 2 onward.

---

## 3. Sprint Implementation Detail

### Sprint 1 – Framework & Governance
**Primary focus**: Scaffold the repository; write and enforce governance.

Implementation steps:
1. Create full directory structure (`docs/`, `src/`, `tests/`, `scripts/`, `sprints/`, `backlog/`).
2. Write all governance documents (policy, standards, DoD, branching strategy).
3. Implement `scripts/governance/check_requirements.py` – validates noun-verb format.
4. Implement `scripts/governance/check_sprint_structure.py` – validates sprint folder completeness.
5. Implement `scripts/governance/check_dod_references.py` – checks DoD links in sprint docs.
6. Write `tests/governance/` test suite exercising all governance scripts.
7. Create GitHub Actions workflows: `ci.yml`, `governance-check.yml`, `sprint-close.yml`.
8. Write system requirements document.
9. Define product backlog with all known backlog items.
10. Prepare Sprint 2 plan artefacts.

### Sprint 2 – Development Environment
1. Write `docker-compose.yml` with Nginx, PHP-FPM, PostgreSQL, ChromaDB, Redis.
2. Write `Dockerfile` for CakePHP application.
3. Write `Dockerfile` for Python orchestrator.
4. Implement RAG ingestion pipeline: `src/rag/ingestor.py`.
5. Implement ChromaDB client wrapper: `src/rag/vector_store.py`.
6. Write ingestion tests.
7. Create CakePHP skeleton (`src/backend/`).
8. Write database migration for `users`, `patent_jobs`, `patent_drafts`.
9. Populate RAG with initial cybersecurity documents (NIST SP 800-53, etc.).

### Sprint 3 – Research Agent
1. Implement LangGraph state: `src/agents/state.py`.
2. Implement agent graph skeleton: `src/agents/orchestrator.py`.
3. Implement Research Agent: `src/agents/research_agent.py`.
4. Implement Skill Registry: `src/skills/registry.py`.
5. Implement Web Search Skill: `src/skills/web_search_skill.py`.
6. Implement Semantic Search Skill: `src/skills/semantic_search_skill.py`.
7. Implement Summarisation Skill: `src/skills/summarisation_skill.py`.
8. Write unit tests for all above.

### Sprint 4 – Synthesis Agent
1. Implement Synthesis Agent: `src/agents/synthesis_agent.py`.
2. Implement Prior Art Analysis Skill: `src/skills/prior_art_analysis_skill.py`.
3. Implement Cybersecurity Taxonomy Skill: `src/skills/cybersecurity_taxonomy_skill.py`.
4. Expand RAG knowledge base with security standards and patents.
5. Write unit tests for all above.

### Sprint 5 – Drafting Agent
1. Implement Drafting Agent: `src/agents/drafting_agent.py`.
2. Implement Patent Claim Formatter Skill: `src/skills/patent_claim_formatter_skill.py`.
3. Implement draft data model: `src/agents/models.py`.
4. Write unit tests for all above.

### Sprint 6 – Review Agent & Full Pipeline
1. Implement Review & Compliance Agent: `src/agents/review_agent.py`.
2. Wire full LangGraph pipeline: Research → Synthesis → Drafting → Review.
3. Implement re-drafting loop (conditional edge).
4. Write integration tests for the full agent pipeline.

### Sprint 7 – CakePHP Backend API
1. Implement PatentsController (CRUD for PatentJob).
2. Implement AuthController (JWT login/logout).
3. Implement OrchestratorService (dispatch jobs to Python orchestrator).
4. Write CakePHP API tests (PHPUnit).
5. Write OpenAPI spec at `src/backend/api.yaml`.

### Sprint 8 – HTML Frontend
1. Implement `src/frontend/templates/` CakePHP view templates.
2. Build patent submission form.
3. Build real-time job status page (polling or WebSocket).
4. Build draft review and edit interface.
5. Build knowledge-base document upload page.

### Sprint 9 – Integration, QA & Security
1. Write end-to-end tests (`tests/e2e/`).
2. Run performance benchmarks; optimise slow paths.
3. Conduct security review: input validation, dependency audit, secrets scan.
4. Fix identified issues.

### Sprint 10 – Release
1. Build and tag Docker images.
2. Write `DEPLOYMENT.md`.
3. Write `CHANGELOG.md`.
4. Tag `v1.0.0` on `main`.

---

## 4. Integration Strategy

### CakePHP ↔ Python Orchestrator
- CakePHP dispatches jobs to the Python orchestrator via its REST API (`POST /orchestrator/jobs`).
- The orchestrator endpoint is configured via environment variable `ORCHESTRATOR_URL`.
- Job polling uses a background Celery task that updates the `patent_jobs` table.
- Alternative: use a shared Redis queue; CakePHP publishes, Python consumes.

### Agent ↔ Vector Database
- LangChain's `Chroma` retriever wraps ChromaDB for development.
- Production switches to `PGVector` retriever with the same interface.
- Swap is achieved by changing a configuration value, not code.

---

## 5. Development Environment Setup (Developers)

```bash
# Clone repository
git clone https://github.com/bnorth12/Patent-Application-Generator.git
cd Patent-Application-Generator

# Python setup (Sprint 3+)
python -m venv .venv
source .venv/bin/activate
pip install -r src/requirements-dev.txt

# Docker stack (Sprint 2+)
docker compose up -d

# Run governance tests
pytest tests/governance/ -v
```

---

## 6. Related Documents

- [Overall Development Plan](overall_development_plan.md)
- [Engineering Plan](engineering_plan.md)
- [Architecture](../architecture/conceptual_architecture.md)
