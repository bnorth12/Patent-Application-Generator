---
name: Repo Governance Language And Artifact Standards
description: "Use when creating or updating repository governance content, compliance checklists, traceability artifacts, sprint governance plans, or release alignment reports. Enforces policy-driven language and naming standards."
applyTo: "**"
---

# Repository Governance Standards

Use these standards whenever governance-related content is authored in this repository.

## Language Standards
- Use policy-first wording with explicit accountability.
- Prefer deterministic verbs: `must`, `required`, `approved`, `blocked`, `escalated`.
- Avoid ambiguous language such as "maybe", "should probably", or "consider if possible".
- For each control, state owner, trigger, evidence, and pass/fail criteria.

## Artifact Naming Standards
- Governance baseline: `governance-baseline.md`
- HITL checklist: `hitl-gate-checklist.md`
- Traceability matrix: `traceability-matrix.md`
- Sprint governance plan: `sprint-governance-plan.md`
- Alignment report: `governance-alignment-report.md`
- Exceptions log: `governance-exceptions-log.md`

## Required Sections Per Artifact
- Scope and objective
- Owners and approvers
- Decision gates and criteria
- Evidence requirements
- Escalation path
- Review cadence and revision date

## Traceability Requirements
- Every requirement must map to one implementation artifact and one validation artifact.
- Every mapped item must have a named owner and status.
- Missing mappings are treated as governance gaps and must be listed in the alignment report.

## HITL Gate Requirements
- Planning gate includes objective, scope, and acceptance criteria.
- Implementation gate confirms control implementation evidence.
- Review gate confirms independent verification.
- Release gate confirms go/no-go and rollback readiness.
- Post-release gate confirms retrospective findings and action ownership.
- Issue/PR closure gate confirms traceability and evidence completeness.

## Quality Bar
- Governance output must be auditable, concise, and actionable.
- Gaps must include impact, priority, owner, and target closure date.
