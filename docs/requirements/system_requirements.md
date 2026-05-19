# System Requirements – Patent Application Generator

**Version**: 1.0  
**Date**: 2026-05-19  
**Owner**: @bnorth12  
**Format**: All requirements use noun-verb format – `The <noun> shall <verb> <predicate>.`

---

## 1. System-Level Requirements

| ID | Requirement |
|----|-------------|
| REQ-001 | The system shall generate a complete patent application draft from a user-provided topic description. |
| REQ-002 | The system shall complete patent draft generation within 120 seconds for standard requests. |
| REQ-003 | The system shall support concurrent processing of at least 10 simultaneous patent generation jobs. |
| REQ-004 | The system shall persist all generated patent drafts in a relational database. |
| REQ-005 | The system shall provide a web-based user interface accessible via modern HTML5 browsers. |
| REQ-006 | The system shall authenticate all users before granting access to any functionality. |
| REQ-007 | The system shall encrypt all data in transit using TLS 1.2 or higher. |
| REQ-008 | The system shall log all agent actions with timestamps and source citations. |
| REQ-009 | The system shall be deployable via Docker Compose in a single command. |
| REQ-010 | The system shall achieve ≥ 80% automated test coverage for all new source files. |

---

## 2. Agent Requirements

| ID | Requirement |
|----|-------------|
| REQ-011 | The Research Agent shall retrieve at least 10 relevant documents per research query. |
| REQ-012 | The Research Agent shall query both the vector database and external web sources during research. |
| REQ-013 | The Research Agent shall classify retrieved documents using the cybersecurity taxonomy. |
| REQ-014 | The Research Agent shall retry research up to 2 times if context is insufficient. |
| REQ-015 | The Synthesis Agent shall identify at least one novel aspect from research results. |
| REQ-016 | The Synthesis Agent shall produce a prior-art summary for every synthesis task. |
| REQ-017 | The Drafting Agent shall produce a patent draft containing title, abstract, claims, and detailed description. |
| REQ-018 | The Drafting Agent shall format patent claims in compliance with USPTO or EPO style. |
| REQ-019 | The Review & Compliance Agent shall check every claim against known prior art. |
| REQ-020 | The Review & Compliance Agent shall flag claims identified as potentially conflicting with existing patents. |
| REQ-021 | The orchestrator shall re-invoke the Drafting Agent when the Review Agent identifies critical issues. |

---

## 3. Skill Requirements

| ID | Requirement |
|----|-------------|
| REQ-022 | The Web Search Skill shall return results from at least one publicly accessible search API. |
| REQ-023 | The Semantic Search Skill shall return top-K documents ranked by semantic similarity. |
| REQ-024 | The Summarisation Skill shall reduce input text to a configurable maximum token length. |
| REQ-025 | The Cybersecurity Taxonomy Skill shall classify input text against NIST and MITRE ATT&CK taxonomy. |
| REQ-026 | The Prior Art Analysis Skill shall compare patent claims against provided prior-art documents. |
| REQ-027 | The Patent Claim Formatter Skill shall structure claims in independent and dependent claim format. |
| REQ-028 | The Skill Registry shall support dynamic registration of new skills without code changes to agents. |

---

## 4. RAG Requirements

| ID | Requirement |
|----|-------------|
| REQ-029 | The RAG pipeline shall chunk and embed documents into the vector database upon upload. |
| REQ-030 | The vector database shall persist embeddings across system restarts. |
| REQ-031 | The RAG pipeline shall support ingestion of PDF and plain-text document formats. |
| REQ-032 | The system shall populate the vector database with cybersecurity research materials during each sprint. |
| REQ-033 | The Semantic Search Skill shall retrieve documents with a similarity score above a configurable threshold. |

---

## 5. Backend API Requirements

| ID | Requirement |
|----|-------------|
| REQ-034 | The CakePHP backend shall expose a REST API for patent job creation and retrieval. |
| REQ-035 | The API shall return appropriate HTTP status codes for all request outcomes. |
| REQ-036 | The API shall validate and sanitise all user inputs before processing. |
| REQ-037 | The API shall reject unauthenticated requests with HTTP 401. |
| REQ-038 | The API shall document all endpoints in an OpenAPI specification. |
| REQ-039 | The job queue shall dispatch patent generation jobs to the Python orchestrator asynchronously. |

---

## 6. Frontend Requirements

| ID | Requirement |
|----|-------------|
| REQ-040 | The frontend shall provide a form for users to submit patent topics. |
| REQ-041 | The frontend shall display real-time job status during patent generation. |
| REQ-042 | The frontend shall present the generated patent draft in a readable, editable format. |
| REQ-043 | The frontend shall allow users to export patent drafts as PDF or plain text. |
| REQ-044 | The frontend shall provide an interface for uploading documents to the RAG knowledge base. |
| REQ-045 | The frontend shall meet WCAG 2.1 Level AA accessibility requirements. |

---

## 7. Governance Requirements

| ID | Requirement |
|----|-------------|
| REQ-046 | The CI pipeline shall validate all requirements documents for noun-verb format compliance on every PR. |
| REQ-047 | The CI pipeline shall enforce sprint folder structure completeness before sprint work begins. |
| REQ-048 | The governance scripts shall block PR merge when violations are detected. |
| REQ-049 | The sprint entry criteria shall be verified before the sprint branch is created and work begins. |
| REQ-050 | The sprint exit criteria shall be verified before the sprint-close PR is merged to main. |

---

## 8. Security Requirements

| ID | Requirement |
|----|-------------|
| REQ-051 | The system shall store no credentials or API keys in source code or committed files. |
| REQ-052 | The system shall scan all new dependencies for known vulnerabilities before introduction. |
| REQ-053 | The CakePHP backend shall apply input sanitisation to prevent injection attacks. |
| REQ-054 | The agent orchestrator shall apply prompt injection mitigations to all user-supplied text. |
| REQ-055 | The system shall restrict vector database write access to the orchestrator service account only. |
