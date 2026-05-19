# Path Research

| Path ID | Supported Capabilities | Evidence/References | Risks/Mitigations | Tradeoffs | Recommendation Status |
| --- | --- | --- | --- | --- | --- |
| PATH-001 | CAP-001, CAP-005 | Use Python scripts with Jinja2 templates for draft generation; proven in document automation | Python/Jinja2 skills required; mitigated by templates and docs | Fast to prototype, easy to extend, but less GUI | Recommended |
| PATH-002 | CAP-001, CAP-005 | Use a low-code workflow tool (e.g., n8n, Node-RED) for patent generation | Tooling lock-in, less control; mitigated by open-source selection | Visual, user-friendly, but more setup | Alternative |
| PATH-003 | CAP-002, CAP-003, CAP-004 | Use markdown-based governance artifacts and GitHub Actions for gate enforcement | Manual errors possible; mitigated by checklists and CODEOWNERS | Simple, transparent, but not fully automated | Recommended |
| PATH-004 | CAP-002, CAP-003, CAP-004 | Integrate a workflow engine (e.g., Temporal, Airflow) for governance and traceability | High complexity; mitigated by phased adoption | Powerful, scalable, but overkill for MVP | Not recommended for MVP |
