# Conceptual Architecture – Patent Application Generator

## 1. Overview

The Patent Application Generator is a multi-agent, skill-based AI platform designed to:

1. Research topics in **system security** and **cyber security architecture**.
2. Synthesise research using a **Retrieval-Augmented Generation (RAG)** pipeline backed by a vector database.
3. Produce structured, legally compliant **patent application drafts** through specialised LangGraph agents.
4. Expose the entire capability through an **HTML/CakePHP web GUI**.

---

## 2. High-Level Architecture Diagram (Textual)

```
┌─────────────────────────────────────────────────────────────────────┐
│                          Web Browser (HTML)                          │
│  - Patent request form                                               │
│  - Research dashboard                                                │
│  - Draft review / edit                                               │
└───────────────────────┬─────────────────────────────────────────────┘
                        │ HTTPS / REST
┌───────────────────────▼─────────────────────────────────────────────┐
│                  CakePHP Backend (PHP 8.2+)                          │
│  - REST API layer                                                     │
│  - Session & auth management                                          │
│  - Job queue (dispatch to Python agent orchestrator)                  │
│  - Database: MySQL / PostgreSQL (structured data, job state)          │
└───────────────────────┬─────────────────────────────────────────────┘
                        │ Internal API / Message Queue
┌───────────────────────▼─────────────────────────────────────────────┐
│            Python / LangGraph Agent Orchestrator                     │
│                                                                       │
│  ┌────────────┐  ┌────────────┐  ┌────────────┐  ┌───────────────┐  │
│  │  Research  │  │ Synthesis  │  │  Drafting  │  │  Review &     │  │
│  │   Agent    │  │   Agent    │  │   Agent    │  │  Compliance   │  │
│  └────────────┘  └────────────┘  └────────────┘  │   Agent       │  │
│                                                   └───────────────┘  │
│  Skills (pluggable):                                                  │
│    - Web search skill           - Patent claim formatter skill        │
│    - Semantic search skill      - Prior art analysis skill            │
│    - Summarisation skill        - Cybersecurity taxonomy skill        │
└───────────────────────┬─────────────────────────────────────────────┘
                        │
        ┌───────────────┴──────────────┐
        │                              │
┌───────▼──────────┐        ┌──────────▼─────────┐
│  Vector Database  │        │  External LLM API   │
│  (ChromaDB /      │        │  (OpenAI / Ollama / │
│   pgvector)       │        │   Anthropic)        │
│  RAG knowledge    │        └────────────────────┘
│  store            │
└──────────────────┘
```

---

## 3. Core Subsystems

### 3.1 Web Frontend (HTML + CakePHP)
- Single-page-style HTML5 interface.
- CakePHP 5.x MVC framework for routing, templating, and API exposure.
- REST endpoints consumed by frontend via `fetch` / AJAX.

### 3.2 Agent Orchestrator (Python + LangGraph)
- LangGraph manages stateful, multi-step agent workflows as directed acyclic graphs.
- Each node in the graph corresponds to a **skill invocation** or **agent decision**.
- Agents communicate through a shared **state object** passed along the graph edges.

### 3.3 Skills Layer
- Skills are discrete, reusable Python callables injected into agent nodes.
- A **Skill Registry** allows dynamic loading of skills at orchestrator start-up.
- Skills include: web search, vector search, patent formatting, claim generation, compliance check.

### 3.4 RAG Pipeline
- Documents (papers, patents, cyber standards) are chunked and embedded into the vector database.
- At query time, the semantic search skill retrieves top-K relevant chunks.
- Retrieved context is injected into the LLM prompt to ground responses.

### 3.5 Vector Database
- **ChromaDB** (development) / **pgvector** (production) for persistent embeddings.
- Populated incrementally each sprint with research materials relevant to planned features.

### 3.6 Relational Database
- MySQL / PostgreSQL for user accounts, job state, audit logs, and patent draft storage.

---

## 4. Data Flow – Patent Generation Request

```
1. User submits topic via HTML form
2. CakePHP validates input, enqueues a PatentJob
3. Orchestrator picks up the job
4. Research Agent invokes:
     a. Web Search Skill → gather recent literature
     b. Semantic Search Skill → query vector DB for related context
5. Synthesis Agent: summarise findings, identify novel aspects
6. Drafting Agent: generate patent claims, abstract, and description
7. Review & Compliance Agent: verify legal terminology, prior-art flags
8. Draft stored in relational DB; result returned to CakePHP
9. Frontend displays draft for user review and export
```

---

## 5. Security Architecture

- All API endpoints authenticated via JWT / session tokens.
- Agent–backend communication is over TLS on an internal network.
- LLM API keys stored in environment variables / secrets manager.
- Vector DB access is restricted to the orchestrator service account.
- Input sanitisation at the CakePHP layer before dispatch to agents.

---

## 6. Scalability Considerations

- Orchestrator runs as a stateless service behind a task queue (Celery / Redis).
- Multiple orchestrator workers can run in parallel.
- Vector DB scales horizontally with pgvector on managed PostgreSQL.

---

## 7. Related Documents

- [Technology Stack](technology_stack.md)
- [System Architecture](system_architecture.md)
- [Conceptual Design](../design/conceptual_design.md)
- [Agent Design](../design/agent_design.md)
