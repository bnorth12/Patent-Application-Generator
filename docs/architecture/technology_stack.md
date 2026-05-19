# Technology Stack – Patent Application Generator

## Summary

| Layer | Technology | Rationale |
|-------|-----------|-----------|
| Web Frontend | HTML5 / CSS3 / Vanilla JS | Lightweight, browser-universal, no build step required |
| Backend Framework | CakePHP 5.x (PHP 8.2+) | Rapid REST API development, ORM, built-in security features |
| Agent Orchestration | Python 3.11 + LangGraph 0.2+ | Stateful multi-agent workflows with directed graph model |
| LLM Abstraction | LangChain 0.3+ | Provider-agnostic LLM client, tool integration |
| LLM Providers | OpenAI GPT-4o / Anthropic Claude / Ollama | Flexible; can swap without code changes |
| Embeddings | OpenAI text-embedding-3-small / sentence-transformers | Semantic search support |
| Vector Database (dev) | ChromaDB 0.5+ | Zero-config local vector store |
| Vector Database (prod) | pgvector on PostgreSQL 16+ | Production-grade, SQL-native vector search |
| Relational Database | PostgreSQL 16+ | Primary structured data store |
| Task Queue | Celery + Redis | Async job dispatch from CakePHP to Python |
| Web Server | Nginx 1.25+ | Reverse proxy, TLS termination |
| Containerisation | Docker / Docker Compose 24+ | Reproducible local dev and deployment |
| CI/CD | GitHub Actions | Automated governance, lint, test, sprint-close |
| Testing (Python) | pytest 8+ | Unit and integration tests |
| Testing (PHP) | PHPUnit 10+ | CakePHP test framework |
| Linting (Python) | flake8 | PEP-8 compliance |
| Linting (PHP) | PHP_CodeSniffer | PSR-12 compliance |

---

## Dependency Decision Log

### Why CakePHP?
- Mature MVC framework with convention-over-configuration.
- Built-in ORM reduces boilerplate for patent draft persistence.
- Authentication plugin supports JWT natively.

### Why LangGraph?
- Enables complex, stateful agent workflows expressed as graphs.
- Supports conditional branching, loops, and human-in-the-loop patterns.
- Native integration with LangChain tools and retrievers.

### Why ChromaDB → pgvector?
- ChromaDB eliminates vector DB infrastructure overhead during development.
- pgvector allows production vector search inside the existing PostgreSQL instance, reducing operational complexity.

### Why GitHub Actions?
- Native CI/CD for GitHub repositories.
- Governance workflow triggers on PR creation to enforce policies.
- Sprint-close workflow automates end-of-sprint PR creation.

---

## Version Pinning Policy

All production dependencies shall be pinned to a specific version in:
- `src/requirements.txt` (Python)
- `composer.json` (PHP / CakePHP)

Development dependencies may use minor-version ranges.
