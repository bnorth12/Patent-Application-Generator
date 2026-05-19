# Overall Development Plan – Patent Application Generator

**Version**: 1.0  
**Date**: 2026-05-19  
**Owner**: @bnorth12

---

## 1. Executive Summary

The Patent Application Generator will be developed over multiple sprints using an agile, sprint-based methodology. Each sprint delivers a set of verified, production-ready increments. The system is designed to reach full capability in approximately 8–10 sprints, each 2 weeks in duration.

---

## 2. High-Level Roadmap

| Phase | Sprints | Theme | Key Deliverables |
|-------|---------|-------|-----------------|
| **Foundation** | 1–2 | Framework, governance, infrastructure | Repo structure, CI/CD, tech stack setup, RAG pipeline skeleton |
| **Core Agents** | 3–4 | Research and Synthesis agents | Research Agent, Semantic Search Skill, RAG population, Synthesis Agent |
| **Drafting** | 5–6 | Patent drafting capability | Drafting Agent, patent claim formatter, Review Agent |
| **Backend** | 7 | CakePHP integration | REST API, job queue, database schema, user auth |
| **Frontend** | 8 | HTML GUI | Patent submission form, draft viewer, knowledge-base uploader |
| **Integration & QA** | 9 | End-to-end integration | Full workflow testing, performance tuning, security review |
| **Release** | 10 | Release v1.0 | Deployment packaging, documentation, release tag |

---

## 3. Sprint Overview

### Sprint 1 – Repository Framework & Governance Foundation
- **Goal**: Establish the complete project structure, governance policies, and development environment.
- **Branch**: `sprint/sprint-01`
- **Key Deliverables**:
  - Repository structure (all directories, templates, governance docs)
  - CI/CD workflows (ci.yml, governance-check.yml, sprint-close.yml)
  - Governance scripts and tests
  - System requirements document (noun-verb format)
  - Technology stack decisions documented
  - Vector database schema design
  - Sprint 2 backlog prepared

### Sprint 2 – Development Environment & RAG Infrastructure
- **Goal**: Working local development environment with Docker Compose; RAG pipeline capable of ingesting documents.
- **Branch**: `sprint/sprint-02`
- **Key Deliverables**:
  - Docker Compose stack (Nginx, PHP-FPM, PostgreSQL, ChromaDB, Redis)
  - Python virtual environment and dependency management
  - RAG ingestion pipeline (chunking, embedding, vector DB write)
  - Initial cybersecurity knowledge base population
  - CakePHP skeleton application with database migrations

### Sprint 3 – Research Agent & Web Search Skill
- **Goal**: Functional Research Agent that can gather and summarise literature.
- **Branch**: `sprint/sprint-03`
- **Key Deliverables**:
  - LangGraph agent graph skeleton
  - Research Agent implementation
  - Web Search Skill (Tavily / SerpAPI)
  - Semantic Search Skill (ChromaDB retriever)
  - Summarisation Skill
  - Unit tests for all agent and skill components

### Sprint 4 – Synthesis Agent & Cybersecurity Taxonomy
- **Goal**: Synthesis Agent identifies novel aspects from research results.
- **Branch**: `sprint/sprint-04`
- **Key Deliverables**:
  - Synthesis Agent implementation
  - Prior Art Analysis Skill
  - Cybersecurity Taxonomy Skill (NIST / MITRE ATT&CK mapping)
  - Expanded RAG knowledge base (security standards, patents)

### Sprint 5 – Drafting Agent & Patent Claim Formatter
- **Goal**: Drafting Agent produces complete patent application structures.
- **Branch**: `sprint/sprint-05`
- **Key Deliverables**:
  - Drafting Agent implementation
  - Patent Claim Formatter Skill (USPTO / EPO style)
  - Draft data model and persistence

### Sprint 6 – Review & Compliance Agent
- **Goal**: Automated review and compliance checking of patent drafts.
- **Branch**: `sprint/sprint-06`
- **Key Deliverables**:
  - Review & Compliance Agent
  - End-to-end agent graph (Research → Synthesis → Drafting → Review)
  - Re-drafting loop (compliance failures trigger Drafting Agent retry)

### Sprint 7 – CakePHP Backend API
- **Goal**: REST API exposing all agent capabilities to the frontend.
- **Branch**: `sprint/sprint-07`
- **Key Deliverables**:
  - PatentJob API (create, read, list)
  - User authentication (JWT)
  - Job queue integration (Celery + Redis)
  - API documentation (OpenAPI spec)

### Sprint 8 – HTML Frontend
- **Goal**: Functional web GUI for end-to-end patent generation.
- **Branch**: `sprint/sprint-08`
- **Key Deliverables**:
  - Patent submission form
  - Real-time job status display
  - Draft review and edit interface
  - Knowledge-base document uploader

### Sprint 9 – Integration, QA & Security
- **Goal**: System validated end-to-end; security hardened.
- **Branch**: `sprint/sprint-09`
- **Key Deliverables**:
  - End-to-end integration tests
  - Performance benchmarks
  - Security review and remediation
  - Load testing

### Sprint 10 – Release v1.0
- **Goal**: Production-ready release.
- **Branch**: `sprint/sprint-10`
- **Key Deliverables**:
  - Release packaging (Docker images)
  - Deployment documentation
  - Release notes
  - v1.0.0 tag on `main`

---

## 4. Dependencies

```
Sprint 1 → Sprint 2 → Sprint 3 → Sprint 4 → Sprint 5 → Sprint 6
                                                              │
Sprint 7 ─────────────────────────────────────────────────────
                                                              │
Sprint 8 ─────────────────────────────────────────────────────
                                                              │
                                                        Sprint 9 → Sprint 10
```

Sprints 7 and 8 depend on Sprint 6 (complete agent pipeline) and may run partially in parallel once the Drafting Agent API contract is defined.

---

## 5. Risks

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| LLM API rate limits slow agent testing | Medium | Medium | Use Ollama locally for dev/test |
| Vector DB performance insufficient | Low | High | Migrate to pgvector early if ChromaDB is too slow |
| Patent legal requirements change | Low | Medium | Review USPTO/EPO guidelines at start of Sprint 5 |
| CakePHP / Python integration complexity | Medium | Medium | Define API contract in Sprint 2; build adapter layer |

---

## 6. Resource Plan

- 1 developer / architect (@bnorth12) driving all sprints
- AI coding assistant (Copilot) supporting implementation
- External LLM API access required from Sprint 3

---

## 7. Related Documents

- [Project Plan](project_plan.md)
- [Implementation Plan](implementation_plan.md)
- [Engineering Plan](engineering_plan.md)
- [Verification Plan](verification_plan.md)
- [Product Backlog](../../backlog/product_backlog.md)
