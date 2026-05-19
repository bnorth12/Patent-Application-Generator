# System Architecture – Patent Application Generator

## 1. Purpose

This document describes the **detailed system architecture** for the Patent Application Generator, expanding on the conceptual architecture with deployment topology, component interfaces, and non-functional requirements.

---

## 2. Deployment Topology

```
┌─────────────────────  Host / Container Network  ──────────────────────┐
│                                                                         │
│  ┌──────────────┐   ┌──────────────────────┐   ┌────────────────────┐  │
│  │  Nginx       │   │  CakePHP App          │   │  Python Orchestr.  │  │
│  │  (Reverse    │──▶│  Container (PHP-FPM)  │──▶│  Container         │  │
│  │   Proxy)     │   │  Port 9000            │   │  Port 8001         │  │
│  └──────────────┘   └──────────────────────┘   └────────────────────┘  │
│        :443                    │                          │              │
│                        ┌───────▼──────┐         ┌────────▼───────────┐  │
│                        │  MySQL/PG    │         │  ChromaDB /         │  │
│                        │  Database   │         │  pgvector           │  │
│                        │  Port 5432  │         │  Port 8000          │  │
│                        └─────────────┘         └────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Component Interfaces

### 3.1 CakePHP ↔ Frontend
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/patents` | Submit new patent generation request |
| GET | `/api/patents/{id}` | Retrieve generated patent draft |
| GET | `/api/patents` | List all drafts for authenticated user |
| POST | `/api/auth/login` | Authenticate user |
| POST | `/api/auth/logout` | End session |

### 3.2 CakePHP ↔ Python Orchestrator
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/orchestrator/jobs` | Dispatch a new agent job |
| GET | `/orchestrator/jobs/{id}` | Poll job status |
| GET | `/orchestrator/health` | Health-check endpoint |

### 3.3 Orchestrator ↔ Vector DB
- ChromaDB REST API (development)
- pgvector via SQLAlchemy (production)
- Operations: `upsert`, `query`, `delete`

### 3.4 Orchestrator ↔ LLM API
- OpenAI-compatible REST API (supports OpenAI, Anthropic via proxy, Ollama locally)
- Calls made via `langchain` / `langchain-openai` clients

---

## 4. Non-Functional Requirements

| Category | Requirement |
|----------|-------------|
| Performance | Patent draft generation shall complete within 120 seconds for standard requests |
| Availability | The system shall target 99.5% uptime for the web frontend |
| Security | All data in transit shall be encrypted with TLS 1.2 or higher |
| Scalability | The orchestrator shall support at least 10 concurrent agent jobs |
| Maintainability | All components shall have unit test coverage ≥ 80% |
| Portability | The system shall be deployable via Docker Compose in a single command |

---

## 5. Technology Versions (Target)

| Component | Technology | Version |
|-----------|-----------|---------|
| Frontend | HTML5 / CSS3 / Vanilla JS | N/A |
| Backend | CakePHP | 5.x |
| Backend Runtime | PHP | 8.2+ |
| Agent Orchestrator | Python | 3.11+ |
| Agent Framework | LangGraph | 0.2+ |
| LLM Client | LangChain | 0.3+ |
| Vector DB (dev) | ChromaDB | 0.5+ |
| Vector DB (prod) | pgvector | 0.7+ |
| Relational DB | PostgreSQL | 16+ |
| Web Server | Nginx | 1.25+ |
| Containerisation | Docker / Docker Compose | 24+ |

---

## 6. Security Architecture Detail

### 6.1 Authentication & Authorisation
- CakePHP Authentication plugin (JWT + session).
- Role-based access: `admin`, `researcher`, `viewer`.
- Python orchestrator validates a service-to-service API key on every request.

### 6.2 Secrets Management
- Development: `.env` files (never committed, covered by `.gitignore`).
- Production: environment injection via container orchestrator secrets.

### 6.3 Input Validation
- All user inputs sanitised at the CakePHP controller layer.
- Prompt injection mitigations applied before forwarding topic text to agents.

---

## 7. Logging & Observability

- CakePHP writes structured JSON logs to `logs/`.
- Python orchestrator writes structured logs via Python `logging` module.
- Health-check endpoints expose readiness and liveness probes.

---

## 8. Related Documents

- [Conceptual Architecture](conceptual_architecture.md)
- [Technology Stack](technology_stack.md)
- [Engineering Plan](../plans/engineering_plan.md)
