# Conceptual Design – Patent Application Generator

## 1. Vision

The Patent Application Generator automates the labour-intensive process of drafting patent applications for innovations in **system security** and **cyber security architecture**. A researcher provides a high-level topic; the system returns a complete, draft-quality patent application ready for attorney review.

---

## 2. User Roles

| Role | Description |
|------|-------------|
| Researcher | Submits topics, reviews generated drafts, populates the RAG knowledge base |
| Patent Attorney | Reviews and finalises drafts exported from the system |
| Administrator | Manages users, monitors job queue, maintains the vector database |
| System Agent | Automated actor (agent) that executes research, synthesis, and drafting tasks |

---

## 3. Core User Journeys

### Journey 1 – Generate a Patent Application
1. Researcher logs in.
2. Researcher enters a topic title and description.
3. System dispatches the Research Agent to gather and rank literature.
4. Synthesis Agent identifies novel aspects and prior-art gaps.
5. Drafting Agent produces claims, abstract, and specification sections.
6. Review Agent flags compliance issues and prior-art conflicts.
7. Draft is presented to the researcher for review.
8. Researcher exports the finalised draft as PDF / DOCX.

### Journey 2 – Populate the RAG Knowledge Base
1. Researcher or Administrator uploads documents (papers, standards, existing patents).
2. System chunks, embeds, and stores documents in the vector database.
3. Documents are tagged with topic domains (e.g., `access_control`, `zero_trust`, `cryptography`).
4. Agents subsequently use the enriched knowledge base during research steps.

### Journey 3 – Review and Refine a Draft
1. Researcher opens a previously generated draft.
2. Researcher edits individual sections inline.
3. Researcher re-triggers specific agents (e.g., re-run compliance check).
4. Updated draft is saved and version-tracked.

---

## 4. Key Design Principles

### 4.1 Modularity
Every agent and every skill is independently replaceable. Adding a new skill requires implementing a single Python callable and registering it in the Skill Registry.

### 4.2 Traceability
Every piece of text in a draft links back to the source documents (RAG citations) and the agent/skill that produced it.

### 4.3 Governance by Design
- Requirements are maintained in noun-verb format throughout all documents.
- Governance checks run automatically on every PR.
- Sprint artefacts (plan, requirements, stories, entry/exit criteria) are mandatory before a sprint can be marked "In Progress".

### 4.4 Incremental Knowledge
Each sprint populates the vector database with research materials relevant to the features planned for that sprint, ensuring the RAG pipeline improves continuously.

### 4.5 Human-in-the-Loop
Agents produce drafts; humans (researchers, attorneys) make final decisions. The system surfaces confidence scores and citations to support informed human review.

---

## 5. Conceptual Data Model

```
User
  └── has many PatentJob
PatentJob
  ├── topic: string
  ├── status: enum(queued, running, review, done)
  └── has one PatentDraft
PatentDraft
  ├── title: string
  ├── abstract: text
  ├── claims: text[]
  ├── specification: text
  ├── prior_art_flags: json
  └── citations: json
Document (RAG store)
  ├── title: string
  ├── content: text
  ├── embedding: vector
  └── tags: string[]
```

---

## 6. Interface Design Principles

- **Minimal cognitive load**: the primary action (submit topic) is always one click away.
- **Progressive disclosure**: advanced options (agent configuration, knowledge-base filters) are hidden by default.
- **Transparent processing**: a live job-status indicator shows which agent is currently active.
- **Exportable artefacts**: every draft can be exported as PDF, DOCX, or plain text.

---

## 7. Related Documents

- [Conceptual Architecture](../architecture/conceptual_architecture.md)
- [Agent Design](agent_design.md)
- [System Requirements](../requirements/system_requirements.md)
