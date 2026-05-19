# RAG Pipeline – Patent Application Generator

This directory contains the Retrieval-Augmented Generation (RAG) pipeline.

## Structure (Sprint 2+)

```
rag/
├── __init__.py
├── ingestor.py        # Document ingestion: chunk, embed, store
├── vector_store.py    # Vector database abstraction (ChromaDB / pgvector)
└── embedder.py        # Embedding model wrapper
```

## Design

1. **Ingestor** (`ingestor.py`): Accepts PDF or plain-text file paths, splits into chunks, generates embeddings, and stores in the vector database.
2. **Vector Store** (`vector_store.py`): Abstraction over ChromaDB (dev) and pgvector (prod). Exposes `upsert`, `query`, `delete`.
3. **Embedder** (`embedder.py`): Wraps `sentence-transformers` model for local embedding generation.

## Configuration

| Environment Variable | Description | Default |
|---------------------|-------------|---------|
| `VECTOR_STORE_BACKEND` | `chroma` or `pgvector` | `chroma` |
| `CHROMA_HOST` | ChromaDB host | `localhost` |
| `CHROMA_PORT` | ChromaDB port | `8000` |
| `EMBEDDING_MODEL` | sentence-transformers model name | `all-MiniLM-L6-v2` |

## Related Documents

- [Conceptual Architecture](../../docs/architecture/conceptual_architecture.md)
- [Implementation Plan – Sprint 2](../../docs/plans/implementation_plan.md)
