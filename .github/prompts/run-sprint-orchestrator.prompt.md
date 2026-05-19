---
name: Run Sprint Orchestrator
description: "Run a full Sprint 1 gate orchestration with deterministic pass/fail outcomes, blockers, owners, and next-gate decision."
argument-hint: "Sprint ID, objective, scope, requirement IDs, owner roles, and target dates"
agent: "Sprint Orchestrator"
tools: [read, search, edit, todo]
---

Run the Sprint Orchestrator for Sprint 1 using the provided arguments.

## Inputs To Parse
- Sprint ID (default: `Sprint-1`)
- Sprint objective
- Scope boundaries
- In-scope requirement IDs
- Owner and approver roles
- Gate target dates

## Required Outputs
Produce the following sections in order:
- `Sprint Execution Summary`
- `Gate-by-Gate Status`
- `Blocking Gaps`
- `Required Remediation Actions`
- `Next Gate Decision`

## Mandatory Gate Sequence
1. Planning gate
2. Implementation gate
3. Review gate
4. Merge gate
5. Retrospective gate

## Control Rules
- Gate status must be one of: `pass`, `conditional`, `fail`.
- Any missing mandatory evidence must be marked as a blocker.
- Conditional gates must include remediation owner and target closure date.
- Fail status must include escalation recommendation.

## Evidence References
Use repository evidence sources, including:
- `docs/sprint-details/sprint-execution-plan.md`
- `docs/planning/program-plan.md`
- `docs/governance/traceability-matrix.md`
- `docs/governance/branch-merge-governance.md`

## Completion Check
- Every gate has owner, trigger, evidence, and pass/fail criteria.
- Every blocker has impact, priority, owner, and closure date.
- Final next-gate decision is explicit.
