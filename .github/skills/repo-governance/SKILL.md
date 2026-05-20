---
name: repo-governance
description: 'Create and enforce policy-driven repository governance artifacts. Use for governance baseline setup, HITL gate checklists, traceability matrices, phased sprint governance, and alignment reports.'
argument-hint: 'Governance objective, scope, and compliance level (light, standard, strict)'
user-invocable: true
disable-model-invocation: false
---

# Repo Governance

## What This Skill Produces
- Governance baseline documentation for a repository
- Human-in-the-loop (HITL) gate checklist with approval points
- Traceability matrix linking requirements, changes, tests, and owners
- Phased sprint governance plan with entry and exit criteria
- Governance alignment report with gaps, risks, and actions

## When To Use
- A repository has weak or missing governance controls
- A team needs auditable delivery and accountability
- A project must map work items to policy and verification artifacts
- A release or milestone needs explicit go or no-go gates
- Stakeholders request a governance maturity review

## Required Inputs
- Governance objective and constraints
- Repository scope (whole repo or selected paths)
- Compliance level: `light`, `standard`, or `strict` (default: `standard`)
- Existing artifacts (if any): policies, SOPs, issue templates, PR templates, test strategy
- Review cadence and decision owners

## Procedure
1. Establish scope and governance intent.
2. Inventory existing governance artifacts in the repository.
3. Select governance depth using the compliance level.
4. Draft the governance baseline and define control domains.
5. Define HITL gates for planning, implementation, review, and release.
6. Build a traceability matrix from requirement to validation evidence.
7. Create phased sprint governance checkpoints and risk thresholds.
8. Produce an alignment report with prioritized remediation actions.
9. Validate completeness against quality criteria before sign-off.

## Decision Logic

### Compliance Level Branching
- `light`: minimal controls for early-stage projects; fast checklist and simplified matrix
- `standard`: balanced controls for most teams; full checklist, matrix, and sprint gates
- `strict`: regulated or high-risk delivery; mandatory approvals, stronger evidence, explicit exceptions log

### Existing Maturity Branching
- If governance artifacts already exist, perform gap analysis first and preserve working conventions.
- If no meaningful artifacts exist, create baseline artifacts before proposing process changes.

### Risk Branching
- If high-risk areas are identified (security, legal, safety, data handling), elevate to stricter gate requirements.
- If risk remains low and ownership is clear, keep controls lean but traceable.

## Quality Criteria And Completion Checks
- Every governance control has an owner and review cadence.
- HITL gates define approver roles and objective pass or fail criteria.
- Traceability matrix links each requirement to implementation and verification evidence.
- Sprint phases include explicit entry and exit criteria.
- Alignment report includes gaps, impact, priority, and target closure date.
- Exceptions are documented with rationale, approver, and expiration date.

## Mandatory HITL Gates (Default)
- Planning gate
- Implementation gate
- Review gate
- Release gate
- Post-release retrospective gate
- Issue and PR closure gate

## Deliverable Templates

### HITL Gate Checklist
- Gate name
- Trigger condition
- Required evidence
- Approver role
- Pass or fail criteria
- Escalation path

### Traceability Matrix Columns
- Requirement ID
- Policy or control reference
- Implementation artifact
- Test or validation artifact
- Owner
- Status
- Notes

### Alignment Report Sections
- Current state summary
- Confirmed strengths
- Gaps and risk impact
- Recommended actions by priority
- Timeline and accountable owners

## Suggested Prompts
- `/repo-governance Establish strict governance for this repository with release gates and evidence requirements.`
- `/repo-governance Create a standard governance baseline and traceability matrix for the current codebase.`
- `/repo-governance Audit existing governance docs and produce an alignment report with remediation actions.`

## Notes
- Favor incremental adoption: introduce controls by phase to reduce team friction.
- Keep governance artifacts concise and auditable.
- Preserve repository conventions unless they conflict with mandatory controls.
