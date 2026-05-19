# Sprint 02 – Sprint Plan

**Sprint Number**: 02  
**Sprint Branch**: `sprint/sprint-02`  
**Start Date**: TBD (after Sprint 01 closes)  
**End Date**: TBD (Start Date + 2 weeks)  
**Sprint Goal**: Stand up the complete local development environment and implement the RAG ingestion pipeline so that subsequent sprints can develop agents and skills against a running stack with a populated vector database.

> All stories in this sprint must satisfy the [Definition of Done](../../docs/governance/definition_of_done.md) before the sprint can be closed.

---

## 1. Sprint Backlog Items

| Backlog ID | Title | Story Points | Assignee | Status |
|------------|-------|-------------|---------|--------|
| BL-010 | Create Docker Compose development stack | 8 | @bnorth12 | To Do |
| BL-011 | Implement RAG ingestion pipeline | 8 | @bnorth12 | To Do |
| BL-012 | Implement vector database client wrapper | 5 | @bnorth12 | To Do |
| BL-013 | Populate RAG with initial cybersecurity documents (NIST SP 800-53) | 5 | @bnorth12 | To Do |
| BL-014 | Create CakePHP skeleton application | 5 | @bnorth12 | To Do |
| BL-015 | Create database migrations (users, patent_jobs, patent_drafts) | 3 | @bnorth12 | To Do |
| BL-016 | Write RAG pipeline tests | 3 | @bnorth12 | To Do |

**Total Points**: 37

---

## 2. Sprint Goal Detail

At the end of Sprint 02:
- `docker compose up` starts all services (Nginx, PHP-FPM, PostgreSQL, ChromaDB, Redis) without errors.
- The RAG ingestion pipeline successfully chunks, embeds, and stores documents.
- At least 5 NIST SP 800-53 control documents are ingested into the vector database.
- The CakePHP skeleton responds to a health-check endpoint.
- Database migrations create the `users`, `patent_jobs`, and `patent_drafts` tables.
- All RAG pipeline tests pass with ≥ 80% coverage.

---

## 3. Technical Approach

### 3.1 Docker Compose Stack
Services:
- `nginx`: Reverse proxy; serves static files and forwards `/api/` to PHP-FPM.
- `app`: CakePHP PHP-FPM container.
- `orchestrator`: Python LangGraph orchestrator container.
- `db`: PostgreSQL 16 with pgvector extension.
- `chroma`: ChromaDB vector database.
- `redis`: Job queue backend for Celery.

### 3.2 RAG Ingestion Pipeline
`src/rag/ingestor.py`:
- Accept file paths (PDF or TXT).
- Split text into chunks (500 tokens, 50 token overlap).
- Generate embeddings via `sentence-transformers` (local, no API key required).
- Store in ChromaDB collection.

### 3.3 Vector Database Client
`src/rag/vector_store.py`:
- Abstraction layer over ChromaDB (development) / pgvector (production).
- Methods: `upsert(documents)`, `query(text, top_k)`, `delete(doc_ids)`.

### 3.4 CakePHP Skeleton
- `composer create-project cakephp/app:^5.0 src/backend`.
- Configure `.env` for database connection.
- Add `/health` endpoint.

---

## 4. Dependencies

- Docker and Docker Compose available in development environment.
- Python 3.11 with `sentence-transformers`, `chromadb`, `langchain` available.

---

## 5. Risks

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| ChromaDB breaking API change | Low | Medium | Pin ChromaDB version in requirements.txt |
| Large embedding model size slows CI | Medium | Low | Use `all-MiniLM-L6-v2` (small, fast model) |
| PDF parsing complexity | Medium | Low | Use `pypdf` for PDF; fallback to plain text |

---

## 6. Sprint Progress Log

| Date | Summary |
|------|---------|
| (TBD) | Sprint started |

---

## 7. Sprint Retrospective

_To be completed at sprint end._
