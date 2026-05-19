# Agent & Skills Design – Patent Application Generator

## 1. Overview

The Patent Application Generator uses a **LangGraph-based multi-agent architecture**. Each agent is a node in a directed graph; skills are the callable tools available to agents. This document defines each agent, its responsibilities, inputs, outputs, and the skills it uses.

---

## 2. Agent Graph Overview

```
START
  │
  ▼
[Research Agent]──────────────────────────────────┐
  │  (research complete)                            │ (insufficient context)
  ▼                                                 │
[Synthesis Agent]                                   │
  │  (synthesis complete)                           │
  ▼                                                 │
[Drafting Agent]                                    │
  │  (draft complete)                               │
  ▼                                                 │
[Review & Compliance Agent]                         │
  │  (approved)        │ (revise)                   │
  ▼                    └──► [Drafting Agent]         │
END                                                 │
                                                    │
        ┌───────────────────────────────────────────┘
        │ (re-research loop, max 2 iterations)
        ▼
[Research Agent]
```

---

## 3. Agent Definitions

### 3.1 Research Agent

**Purpose**: Gather relevant literature, prior art, and technical information on the given topic.

**Inputs**:
- `topic`: string – the patent topic provided by the user
- `iteration`: int – current research iteration (supports re-research loop)

**Outputs**:
- `research_results`: list of structured findings with source URLs/titles
- `context_sufficient`: bool – whether enough context was found to proceed

**Skills Used**:
| Skill | Purpose |
|-------|---------|
| `web_search_skill` | Search the public web for recent papers and news |
| `semantic_search_skill` | Query the vector database for pre-ingested documents |
| `summarisation_skill` | Condense large documents into key points |
| `cybersecurity_taxonomy_skill` | Classify findings within the cybersecurity domain taxonomy |

---

### 3.2 Synthesis Agent

**Purpose**: Analyse research findings to identify novel aspects and prior-art gaps.

**Inputs**:
- `research_results`: output from Research Agent

**Outputs**:
- `novel_aspects`: list of potentially patentable novel aspects
- `prior_art_summary`: summary of existing prior art
- `differentiation_rationale`: explanation of how the invention differs from prior art

**Skills Used**:
| Skill | Purpose |
|-------|---------|
| `prior_art_analysis_skill` | Identify overlapping prior-art claims |
| `summarisation_skill` | Condense research into synthesis narrative |

---

### 3.3 Drafting Agent

**Purpose**: Produce the structured patent application document.

**Inputs**:
- `novel_aspects`: output from Synthesis Agent
- `prior_art_summary`: output from Synthesis Agent
- `topic`: original user topic

**Outputs**:
- `draft`: PatentDraft object with:
  - `title`
  - `abstract`
  - `claims` (independent and dependent)
  - `detailed_description`
  - `brief_description_of_drawings`

**Skills Used**:
| Skill | Purpose |
|-------|---------|
| `patent_claim_formatter_skill` | Format claims to USPTO/EPO style |
| `summarisation_skill` | Draft abstract from novel aspects |

---

### 3.4 Review & Compliance Agent

**Purpose**: Check the draft for legal compliance, claim clarity, and prior-art conflicts.

**Inputs**:
- `draft`: PatentDraft from Drafting Agent
- `prior_art_summary`: from Synthesis Agent

**Outputs**:
- `approved`: bool
- `issues`: list of compliance issues with suggested fixes
- `prior_art_flags`: specific claim elements that may conflict with prior art

**Skills Used**:
| Skill | Purpose |
|-------|---------|
| `prior_art_analysis_skill` | Re-check individual claims against prior art |
| `patent_claim_formatter_skill` | Verify claim structure |

---

## 4. Skill Definitions

### 4.1 `web_search_skill`
- **Input**: `query: str`, `max_results: int = 10`
- **Output**: `list[SearchResult]` (title, url, snippet)
- **Implementation**: Wraps a search API (e.g., Tavily, SerpAPI, or DuckDuckGo)

### 4.2 `semantic_search_skill`
- **Input**: `query: str`, `top_k: int = 5`, `filters: dict = None`
- **Output**: `list[Document]` (content, metadata, similarity_score)
- **Implementation**: Queries ChromaDB / pgvector via LangChain retriever

### 4.3 `summarisation_skill`
- **Input**: `text: str`, `max_tokens: int = 500`
- **Output**: `str` – condensed summary
- **Implementation**: LLM call with summarisation prompt template

### 4.4 `cybersecurity_taxonomy_skill`
- **Input**: `text: str`
- **Output**: `list[str]` – matched taxonomy tags (e.g., `zero_trust`, `PKI`, `intrusion_detection`)
- **Implementation**: Keyword matching + LLM classification against NIST / MITRE ATT&CK taxonomy

### 4.5 `prior_art_analysis_skill`
- **Input**: `claims: list[str]`, `prior_art_documents: list[Document]`
- **Output**: `list[PriorArtConflict]` (claim_index, conflicting_doc, explanation)
- **Implementation**: LLM-based comparison with structured output

### 4.6 `patent_claim_formatter_skill`
- **Input**: `raw_claims: list[str]`, `style: str = "USPTO"`
- **Output**: `list[str]` – formatted claims
- **Implementation**: Prompt template with USPTO/EPO claim structure rules

---

## 5. Skill Registry

Skills are registered at orchestrator start-up from `src/skills/__init__.py`. Each skill is a Python callable wrapped in a `Skill` dataclass:

```python
@dataclass
class Skill:
    name: str
    description: str
    callable: Callable
    input_schema: type  # Pydantic model
    output_schema: type  # Pydantic model
```

Agents reference skills by name; the orchestrator resolves and injects them at runtime.

---

## 6. State Object

The LangGraph state object passed between agent nodes:

```python
class AgentState(TypedDict):
    topic: str
    iteration: int
    research_results: list
    novel_aspects: list
    prior_art_summary: str
    differentiation_rationale: str
    draft: dict
    issues: list
    approved: bool
    citations: list
```

---

## 7. Related Documents

- [Conceptual Architecture](../architecture/conceptual_architecture.md)
- [System Requirements](../requirements/system_requirements.md)
- [Technology Stack](../architecture/technology_stack.md)
