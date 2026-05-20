# Requirements

| Requirement ID | Statement (noun shall verb) | Rationale | Owner | Measurable Condition | Verification Method | Traceability Links |
| --- | --- | --- | --- | --- | --- | --- |
| REQ-001 | The system shall generate a patent application draft from structured user input | Enable automation and reduce manual drafting effort | Maintainer | Draft is generated in under 2 minutes for valid input | Functional test with sample input | CAP-001 |
| REQ-002 | The system shall enforce governance controls on all workflow changes | Ensure auditability and compliance | Maintainer | All changes are linked to governance artifacts and pass HITL gates | Governance review checklist | CAP-002 |
| REQ-003 | The system shall provide traceability from requirements to implementation and validation | Support compliance and change impact analysis | Maintainer | Every requirement is mapped to code and test evidence | Traceability matrix review | CAP-003 |
| REQ-004 | The system shall support human-in-the-loop (HITL) approval gates | Ensure quality and accountability | Maintainer | All major workflow steps require explicit approval | Gate checklist review | CAP-004 |
| REQ-005 | The system shall allow easy extension for new patent types or jurisdictions | Support future growth and flexibility | Maintainer | New templates or rules can be added with < 1 day effort | Extension test and review | CAP-005 |
