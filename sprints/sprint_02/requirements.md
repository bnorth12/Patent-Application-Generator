# Sprint 02 – Requirements

**Sprint Number**: 02  
**Sprint Branch**: `sprint/sprint-02`  
**Format**: All requirements use noun-verb format – `The <noun> shall <verb> <predicate>.`

---

## Sprint 02 Requirements

| ID | Requirement | Backlog Item | Status |
|----|-------------|-------------|--------|
| SPR-02-R01 | The Docker Compose stack shall start all services (Nginx, PHP-FPM, PostgreSQL, ChromaDB, Redis) with a single `docker compose up -d` command. | BL-010 | To Do |
| SPR-02-R02 | The Docker Compose stack shall expose the CakePHP application on port 8080 of the host. | BL-010 | To Do |
| SPR-02-R03 | The RAG ingestion pipeline shall accept PDF and plain-text file paths as input. | BL-011 | To Do |
| SPR-02-R04 | The RAG ingestion pipeline shall split documents into chunks of 500 tokens with 50-token overlap. | BL-011 | To Do |
| SPR-02-R05 | The RAG ingestion pipeline shall generate embeddings and store them in the vector database. | BL-011 | To Do |
| SPR-02-R06 | The vector database client shall expose `upsert`, `query`, and `delete` operations. | BL-012 | To Do |
| SPR-02-R07 | The vector database client shall return the top-K most similar documents for a given query. | BL-012 | To Do |
| SPR-02-R08 | The RAG knowledge base shall contain at least 5 ingested NIST SP 800-53 control documents after Sprint 02. | BL-013 | To Do |
| SPR-02-R09 | The CakePHP skeleton application shall respond to a GET request at `/health` with HTTP 200. | BL-014 | To Do |
| SPR-02-R10 | The database migrations shall create `users`, `patent_jobs`, and `patent_drafts` tables in PostgreSQL. | BL-015 | To Do |
| SPR-02-R11 | The RAG pipeline tests shall achieve ≥ 80% line coverage for `src/rag/ingestor.py` and `src/rag/vector_store.py`. | BL-016 | To Do |

---

## Requirements Verification

Each requirement above shall be verified against the acceptance criteria in [stories.md](stories.md).
