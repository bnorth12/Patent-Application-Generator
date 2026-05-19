# Project Plan – Patent Application Generator

**Version**: 1.0  
**Date**: 2026-05-19  
**Owner**: @bnorth12

---

## 1. Project Overview

| Item | Detail |
|------|--------|
| Project Name | Patent Application Generator |
| Repository | `bnorth12/Patent-Application-Generator` |
| Project Type | Multi-agent AI platform |
| Domain | System security / Cyber security architecture |
| Target Release | v1.0.0 |
| Estimated Duration | 10 sprints × 2 weeks = ~5 months |
| Start Date | TBD (pending Sprint 1 entry criteria completion) |

---

## 2. Objectives

1. Deliver a fully functional, multi-agent patent application generation system.
2. Establish a robust governance framework enforced automatically via CI/CD.
3. Build and populate a RAG knowledge base focused on cybersecurity topics.
4. Deliver a production-ready CakePHP REST API and HTML frontend.
5. Achieve ≥ 80% automated test coverage across all components.

---

## 3. Milestones

| Milestone | Sprint | Target Completion | Criteria |
|-----------|--------|-------------------|----------|
| M1: Governance Foundation | Sprint 1 | +2 weeks | All governance docs in place, CI passing |
| M2: Development Environment | Sprint 2 | +4 weeks | Docker Compose stack running, RAG ingestion working |
| M3: Research Capability | Sprint 3 | +6 weeks | Research Agent producing results |
| M4: Synthesis Capability | Sprint 4 | +8 weeks | Novel aspects identified from research |
| M5: Drafting Capability | Sprint 5–6 | +12 weeks | Complete patent draft generated end-to-end |
| M6: Backend API | Sprint 7 | +14 weeks | REST API endpoints tested and documented |
| M7: Frontend | Sprint 8 | +16 weeks | HTML GUI functional |
| M8: QA Complete | Sprint 9 | +18 weeks | All integration tests passing |
| M9: Release v1.0.0 | Sprint 10 | +20 weeks | System deployed, release tagged |

---

## 4. Work Breakdown Structure (WBS)

```
1.0 Patent Application Generator
  1.1 Governance & Framework
    1.1.1 Repository structure
    1.1.2 CI/CD workflows
    1.1.3 Governance scripts and tests
    1.1.4 Documentation (architecture, design, plans, requirements)
  1.2 Infrastructure
    1.2.1 Docker Compose stack
    1.2.2 PostgreSQL database setup
    1.2.3 Vector database (ChromaDB → pgvector)
    1.2.4 Task queue (Celery + Redis)
  1.3 Agent Orchestration
    1.3.1 LangGraph graph skeleton
    1.3.2 Research Agent
    1.3.3 Synthesis Agent
    1.3.4 Drafting Agent
    1.3.5 Review & Compliance Agent
  1.4 Skills
    1.4.1 Web Search Skill
    1.4.2 Semantic Search Skill
    1.4.3 Summarisation Skill
    1.4.4 Cybersecurity Taxonomy Skill
    1.4.5 Prior Art Analysis Skill
    1.4.6 Patent Claim Formatter Skill
  1.5 RAG Knowledge Base
    1.5.1 Ingestion pipeline
    1.5.2 Cybersecurity standards documents
    1.5.3 Example patents
    1.5.4 MITRE ATT&CK / NIST content
  1.6 CakePHP Backend
    1.6.1 Application skeleton
    1.6.2 Database migrations
    1.6.3 REST API (PatentJob, User)
    1.6.4 Job queue integration
    1.6.5 Authentication (JWT)
  1.7 HTML Frontend
    1.7.1 Patent submission form
    1.7.2 Job status display
    1.7.3 Draft review interface
    1.7.4 Knowledge-base uploader
  1.8 Testing
    1.8.1 Governance tests
    1.8.2 Agent unit tests
    1.8.3 Skill unit tests
    1.8.4 API integration tests
    1.8.5 End-to-end tests
  1.9 Release
    1.9.1 Deployment packaging
    1.9.2 Release documentation
    1.9.3 v1.0.0 release tag
```

---

## 5. RACI Matrix

| Activity | Responsible | Accountable | Consulted | Informed |
|----------|------------|-------------|-----------|---------|
| Architecture decisions | @bnorth12 | @bnorth12 | Copilot | — |
| Sprint planning | @bnorth12 | @bnorth12 | — | — |
| Development | @bnorth12, Copilot | @bnorth12 | — | — |
| Governance enforcement | CI/CD | @bnorth12 | — | — |
| Code review | @bnorth12 | @bnorth12 | — | — |
| Release sign-off | @bnorth12 | @bnorth12 | — | — |

---

## 6. Assumptions and Constraints

**Assumptions**:
- External LLM API access available from Sprint 3.
- Docker available in the development environment.
- GitHub Actions minutes available for CI/CD.

**Constraints**:
- Single developer; automation and tooling are critical force multipliers.
- Open-source or low-cost dependencies preferred.
- All code and documents must remain in the GitHub repository.

---

## 7. Related Documents

- [Overall Development Plan](overall_development_plan.md)
- [Implementation Plan](implementation_plan.md)
- [Engineering Plan](engineering_plan.md)
- [Verification Plan](verification_plan.md)
