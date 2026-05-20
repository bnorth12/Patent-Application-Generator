# Capability Map

| Capability ID | Capability Name | Supported Requirements | Success Metric | Threshold | Dependencies |
| --- | --- | --- | --- | --- | --- |
| CAP-001 | Patent draft generation | REQ-001 | Draft generated from input | <2 min per draft | None |
| CAP-002 | Governance enforcement | REQ-002 | All changes pass governance gates | 100% of changes | CAP-003 |
| CAP-003 | Traceability management | REQ-003 | All requirements mapped to code/tests | 100% mapping | None |
| CAP-004 | HITL approval workflow | REQ-004 | All major steps require approval | 100% of major steps | CAP-002 |
| CAP-005 | Extensibility for new types | REQ-005 | New templates/rules added in <1 day | 1 day per extension | CAP-001 |
