# Product Backlog – Patent Application Generator

**Version**: 1.0  
**Date**: 2026-05-19  
**Owner**: @bnorth12

---

## Backlog Priority Legend

| Priority | Description |
|----------|-------------|
| P1 | Must have – system cannot function without it |
| P2 | Should have – significant value, plan for early sprints |
| P3 | Could have – valuable but not blocking |
| P4 | Nice to have – deferred to later sprints or post-v1.0 |

---

## Sprint 1 Backlog Items

| ID | Title | Priority | Points | Sprint |
|----|-------|----------|--------|--------|
| BL-001 | Establish repository directory structure and governance documents | P1 | 8 | Sprint 1 |
| BL-002 | Implement CI/CD workflows (ci, governance-check, sprint-close) | P1 | 5 | Sprint 1 |
| BL-003 | Implement governance scripts (requirements format check, sprint structure check) | P1 | 5 | Sprint 1 |
| BL-004 | Write governance test suite | P1 | 3 | Sprint 1 |
| BL-005 | Write system requirements document (noun-verb format) | P1 | 3 | Sprint 1 |
| BL-006 | Write conceptual architecture and design documents | P1 | 5 | Sprint 1 |
| BL-007 | Write all planning documents (project, implementation, engineering, verification) | P1 | 5 | Sprint 1 |
| BL-008 | Define and document product backlog | P1 | 2 | Sprint 1 |
| BL-009 | Prepare Sprint 2 plan, requirements, stories, and entry/exit criteria | P1 | 3 | Sprint 1 |

---

## Sprint 2 Backlog Items

| ID | Title | Priority | Points | Sprint |
|----|-------|----------|--------|--------|
| BL-010 | Create Docker Compose development stack | P1 | 8 | Sprint 2 |
| BL-011 | Implement RAG ingestion pipeline | P1 | 8 | Sprint 2 |
| BL-012 | Implement vector database client wrapper | P1 | 5 | Sprint 2 |
| BL-013 | Populate RAG with initial cybersecurity documents (NIST SP 800-53) | P1 | 5 | Sprint 2 |
| BL-014 | Create CakePHP skeleton application | P1 | 5 | Sprint 2 |
| BL-015 | Create database migrations (users, patent_jobs, patent_drafts) | P1 | 3 | Sprint 2 |
| BL-016 | Write RAG pipeline tests | P1 | 3 | Sprint 2 |

---

## Sprint 3 Backlog Items

| ID | Title | Priority | Points | Sprint |
|----|-------|----------|--------|--------|
| BL-017 | Implement LangGraph agent state and graph skeleton | P1 | 5 | Sprint 3 |
| BL-018 | Implement Research Agent | P1 | 8 | Sprint 3 |
| BL-019 | Implement Skill Registry | P1 | 3 | Sprint 3 |
| BL-020 | Implement Web Search Skill | P1 | 5 | Sprint 3 |
| BL-021 | Implement Semantic Search Skill | P1 | 5 | Sprint 3 |
| BL-022 | Implement Summarisation Skill | P1 | 3 | Sprint 3 |
| BL-023 | Write unit tests for Research Agent and Sprint 3 skills | P1 | 5 | Sprint 3 |

---

## Sprint 4 Backlog Items

| ID | Title | Priority | Points | Sprint |
|----|-------|----------|--------|--------|
| BL-024 | Implement Synthesis Agent | P1 | 8 | Sprint 4 |
| BL-025 | Implement Prior Art Analysis Skill | P1 | 5 | Sprint 4 |
| BL-026 | Implement Cybersecurity Taxonomy Skill | P1 | 5 | Sprint 4 |
| BL-027 | Expand RAG knowledge base (security standards, MITRE ATT&CK) | P2 | 5 | Sprint 4 |
| BL-028 | Write unit tests for Synthesis Agent and Sprint 4 skills | P1 | 5 | Sprint 4 |

---

## Sprint 5 Backlog Items

| ID | Title | Priority | Points | Sprint |
|----|-------|----------|--------|--------|
| BL-029 | Implement Drafting Agent | P1 | 8 | Sprint 5 |
| BL-030 | Implement Patent Claim Formatter Skill | P1 | 5 | Sprint 5 |
| BL-031 | Implement draft data model and persistence | P1 | 5 | Sprint 5 |
| BL-032 | Write unit tests for Drafting Agent and Sprint 5 skills | P1 | 5 | Sprint 5 |

---

## Sprint 6 Backlog Items

| ID | Title | Priority | Points | Sprint |
|----|-------|----------|--------|--------|
| BL-033 | Implement Review & Compliance Agent | P1 | 8 | Sprint 6 |
| BL-034 | Wire full LangGraph pipeline (Research → Synthesis → Drafting → Review) | P1 | 8 | Sprint 6 |
| BL-035 | Implement re-drafting loop (conditional edge on compliance failure) | P1 | 5 | Sprint 6 |
| BL-036 | Write integration tests for full agent pipeline | P1 | 8 | Sprint 6 |

---

## Sprint 7 Backlog Items

| ID | Title | Priority | Points | Sprint |
|----|-------|----------|--------|--------|
| BL-037 | Implement PatentsController (CRUD) | P1 | 8 | Sprint 7 |
| BL-038 | Implement AuthController (JWT login/logout) | P1 | 5 | Sprint 7 |
| BL-039 | Implement OrchestratorService (job dispatch) | P1 | 5 | Sprint 7 |
| BL-040 | Write CakePHP API tests | P1 | 5 | Sprint 7 |
| BL-041 | Write OpenAPI specification | P2 | 3 | Sprint 7 |

---

## Sprint 8 Backlog Items

| ID | Title | Priority | Points | Sprint |
|----|-------|----------|--------|--------|
| BL-042 | Implement patent submission form (HTML + CakePHP) | P1 | 8 | Sprint 8 |
| BL-043 | Implement job status display page | P1 | 5 | Sprint 8 |
| BL-044 | Implement draft review and edit interface | P1 | 8 | Sprint 8 |
| BL-045 | Implement knowledge-base document uploader | P2 | 5 | Sprint 8 |

---

## Sprint 9 Backlog Items

| ID | Title | Priority | Points | Sprint |
|----|-------|----------|--------|--------|
| BL-046 | Write end-to-end integration tests | P1 | 13 | Sprint 9 |
| BL-047 | Run performance benchmarks; optimise slow paths | P1 | 8 | Sprint 9 |
| BL-048 | Conduct security review; remediate findings | P1 | 8 | Sprint 9 |

---

## Sprint 10 Backlog Items

| ID | Title | Priority | Points | Sprint |
|----|-------|----------|--------|--------|
| BL-049 | Build and tag Docker images | P1 | 5 | Sprint 10 |
| BL-050 | Write deployment documentation | P1 | 3 | Sprint 10 |
| BL-051 | Write release notes and CHANGELOG | P1 | 2 | Sprint 10 |
| BL-052 | Create v1.0.0 release tag | P1 | 1 | Sprint 10 |

---

## Unassigned / Future Backlog

| ID | Title | Priority | Points | Sprint |
|----|-------|----------|--------|--------|
| BL-053 | Multi-language patent claim generation (PCT) | P3 | 13 | Post-v1.0 |
| BL-054 | Automated USPTO e-filing integration | P3 | 21 | Post-v1.0 |
| BL-055 | Patent portfolio dashboard | P3 | 13 | Post-v1.0 |
| BL-056 | Fine-tuned LLM for patent domain | P4 | 21 | Post-v1.0 |
| BL-057 | Mobile-responsive frontend | P3 | 8 | Post-v1.0 |
