# Sprint 02 – Stories

**Sprint Number**: 02  
**Sprint Branch**: `sprint/sprint-02`

---

### STORY-02-001

**Title**: Create Docker Compose Development Stack  
**Story**: As a developer, I want a Docker Compose stack that starts all required services so that I can develop and test the full system locally.

**Requirements**: SPR-02-R01, SPR-02-R02  
**Backlog Item**: BL-010

**Acceptance Criteria**:
1. `docker-compose.yml` in the repository root defines services: `nginx`, `app` (PHP-FPM), `orchestrator` (Python), `db` (PostgreSQL + pgvector), `chroma` (ChromaDB), `redis`.
2. `docker compose up -d` starts all services without errors.
3. The CakePHP application is accessible at `http://localhost:8080`.
4. All service health checks pass after startup.
5. `Dockerfile` files exist for `app` and `orchestrator` services.

**Story Points**: 8  
**Assignee**: @bnorth12  
**Status**: To Do

---

### STORY-02-002

**Title**: Implement RAG Ingestion Pipeline  
**Story**: As a researcher, I want to ingest documents into the vector database so that agents can retrieve relevant knowledge during research tasks.

**Requirements**: SPR-02-R03, SPR-02-R04, SPR-02-R05  
**Backlog Item**: BL-011

**Acceptance Criteria**:
1. `src/rag/ingestor.py` implements `ingest_file(path: str) -> int` that returns the number of chunks stored.
2. The ingestor handles PDF (via `pypdf`) and plain-text (`.txt`) input files.
3. Documents are split into chunks of 500 tokens with 50-token overlap.
4. Embeddings are generated and stored in ChromaDB.
5. Running the ingestor twice on the same file does not create duplicate chunks (upsert semantics).

**Story Points**: 8  
**Assignee**: @bnorth12  
**Status**: To Do

---

### STORY-02-003

**Title**: Implement Vector Database Client Wrapper  
**Story**: As a developer, I want a vector database abstraction layer so that agents and skills can perform semantic search without knowing the underlying database implementation.

**Requirements**: SPR-02-R06, SPR-02-R07  
**Backlog Item**: BL-012

**Acceptance Criteria**:
1. `src/rag/vector_store.py` defines a `VectorStore` class with methods: `upsert(documents)`, `query(text, top_k)`, `delete(doc_ids)`.
2. `VectorStore` uses ChromaDB in development (configurable via `VECTOR_STORE_BACKEND` env var).
3. `query()` returns a list of `Document` objects ordered by descending similarity score.
4. All methods have type hints and docstrings.

**Story Points**: 5  
**Assignee**: @bnorth12  
**Status**: To Do

---

### STORY-02-004

**Title**: Populate RAG Knowledge Base with Cybersecurity Documents  
**Story**: As a researcher, I want the vector database pre-populated with NIST SP 800-53 control documents so that agents have foundational cybersecurity knowledge from the start.

**Requirements**: SPR-02-R08  
**Backlog Item**: BL-013

**Acceptance Criteria**:
1. At least 5 NIST SP 800-53 controls are ingested into ChromaDB.
2. A `scripts/rag/populate_initial_knowledge_base.py` script performs the ingestion and can be re-run idempotently.
3. Source documents are stored in `data/rag/sources/` (not committed; documented in README).
4. Ingested document metadata includes: title, source, date, and domain tags.

**Story Points**: 5  
**Assignee**: @bnorth12  
**Status**: To Do

---

### STORY-02-005

**Title**: Create CakePHP Skeleton Application  
**Story**: As a developer, I want a CakePHP skeleton application with database connectivity so that the backend development foundation is ready for Sprint 7.

**Requirements**: SPR-02-R09  
**Backlog Item**: BL-014

**Acceptance Criteria**:
1. `src/backend/` contains a CakePHP 5.x application.
2. `GET /health` returns HTTP 200 with JSON body `{"status": "ok"}`.
3. The application connects to the PostgreSQL database defined in `docker-compose.yml`.
4. `.env.example` in `src/backend/` documents all required environment variables.

**Story Points**: 5  
**Assignee**: @bnorth12  
**Status**: To Do

---

### STORY-02-006

**Title**: Create Database Migrations  
**Story**: As a developer, I want database migrations for the core tables so that the relational database schema is defined and versioned.

**Requirements**: SPR-02-R10  
**Backlog Item**: BL-015

**Acceptance Criteria**:
1. CakePHP migrations create `users`, `patent_jobs`, and `patent_drafts` tables.
2. `users` table has: `id`, `email`, `password_hash`, `role`, `created`, `modified`.
3. `patent_jobs` table has: `id`, `user_id`, `topic`, `status`, `created`, `modified`.
4. `patent_drafts` table has: `id`, `job_id`, `title`, `abstract`, `claims`, `specification`, `citations`, `created`, `modified`.
5. Migrations run successfully with `bin/cake migrations migrate`.

**Story Points**: 3  
**Assignee**: @bnorth12  
**Status**: To Do

---

### STORY-02-007

**Title**: Write RAG Pipeline Tests  
**Story**: As a developer, I want automated tests for the RAG ingestion pipeline and vector store so that I can verify the pipeline is working correctly.

**Requirements**: SPR-02-R11  
**Backlog Item**: BL-016

**Acceptance Criteria**:
1. `tests/rag/test_ingestor.py` tests: ingest a plain-text file, ingest a PDF file, verify chunk count, verify idempotency.
2. `tests/rag/test_vector_store.py` tests: upsert documents, query returns top-K results, delete removes documents.
3. Tests use pytest fixtures; no real network calls (ChromaDB in-memory or mocked).
4. `pytest tests/rag/ --cov=src/rag --cov-report=term-missing` shows ≥ 80% coverage.

**Story Points**: 3  
**Assignee**: @bnorth12  
**Status**: To Do
