# Sprint Execution Plan

## Scope And Objective
- Scope: Sprint planning, implementation, verification, and merge governance for this repository
- Objective: Ensure every sprint produces complete implementation and governance evidence before merge

## Owners And Approvers
- Sprint owner: Repository Maintainer
- Implementation owner: Assigned contributor
- Review approver: Code Reviewer
- Governance approver: Governance Owner
- Release approver: Repository Maintainer

## Decision Gates And Criteria

### Sprint Planning Gate
- Trigger: Sprint backlog finalization
- Criteria: Sprint goals, requirement IDs, scope boundaries, and owners are documented
- Pass condition: Every planned work item maps to one or more requirement IDs
- Fail condition: Unmapped or ownerless backlog items
- Required invocation: `Sprint Orchestrator` must run using `.github/prompts/run-sprint-orchestrator.prompt.md` for planning gate status capture
- Required output: `Sprint Execution Summary` and `Gate-by-Gate Status` sections with planning gate status and blocking gaps

### Sprint Implementation Gate
- Trigger: Feature branch ready for PR
- Criteria: Code complete, required docs updated, verification tests added or updated
- Pass condition: Implementation artifacts and traceability entries are present
- Fail condition: Missing traceability or missing verification updates
- Required invocation: `verification-auditor` skill must run using `.github/prompts/run-verification-auditor.prompt.md`
- Required output: `Verification Coverage Table`, `Verification Gap Report`, and `Verification Readiness Decision`

### Sprint Review Gate
- Trigger: PR review cycle
- Criteria: approval evidence present, review decision APPROVED, unresolved review threads count equals zero, linked issues closed
- Pass condition: No unresolved blocking comments and no open linked issues
- Fail condition: Open linked issues or unresolved blocking comments
- Required invocation: `PR Compliance Checker` must run using `.github/prompts/run-pr-compliance-checker.prompt.md`
- Required output: `Compliance Decision`, `Findings By Control`, `Blocking Items`, and `Required PR Updates`

### Sprint Merge Gate
- Trigger: PR ready to merge
- Criteria: Branch merge checks pass, governance checklist complete, required checks green
- Pass condition: local pre-merge-gate passes; pre-merge-governance-gate workflow passes; required PR governance checklist items are all checked; traceability fields are complete
- Fail condition: Any pre-merge gate failure
- Required invocation: `Sprint Orchestrator` must run for merge gate decision evidence before merge approval
- Required output: explicit `Next Gate Decision` with merge gate status and remediation actions when status is `conditional` or `fail`

### Sprint Retrospective Gate
- Trigger: Sprint close
- Criteria: Outcomes, gaps, action owners, and dates documented
- Pass condition: Action register complete with owners and due dates
- Fail condition: Unowned or undated actions
- Required invocation: `Sprint Orchestrator` must run for retrospective closure, and `release-evidence-packager` must run when sprint scope contributes to release candidate scope
- Required output: retrospective `Required Remediation Actions`; when release scope applies, `Evidence Manifest` and `Release Alignment Summary`

## Agent And Skill Invocation Matrix

| Gate | Required Agent/Skill | Starter Prompt | Mandatory Inputs | Mandatory Outputs | Pass/Fail Usage Rule |
| --- | --- | --- | --- | --- | --- |
| Planning | Sprint Orchestrator | `.github/prompts/run-sprint-orchestrator.prompt.md` | Sprint ID, objective, scope, requirement IDs, owners, gate target dates | Sprint Execution Summary; Gate-by-Gate Status | Planning gate is blocked when invocation output is missing or ownerless |
| Implementation | verification-auditor | `.github/prompts/run-verification-auditor.prompt.md` | Requirement IDs, implementation artifacts, test artifacts, result artifacts, owners | Verification Coverage Table; Verification Gap Report; Verification Readiness Decision | Implementation gate fails when mandatory requirement-to-test-to-result mappings are missing |
| Review | PR Compliance Checker | `.github/prompts/run-pr-compliance-checker.prompt.md` | PR number, linked issues, changed requirement IDs, changed artifacts | Compliance Decision; Findings By Control; Blocking Items; Required PR Updates | Review gate fails when PR compliance output includes unresolved blocking items |
| Merge | Sprint Orchestrator | `.github/prompts/run-sprint-orchestrator.prompt.md` | Current gate states, merge evidence, unresolved gap status, owners | Next Gate Decision; Required Remediation Actions | Merge gate fails when decision output is not `pass` |
| Retrospective | Sprint Orchestrator and release-evidence-packager (conditional on release scope) | `.github/prompts/run-sprint-orchestrator.prompt.md`; `.github/prompts/run-release-evidence-packager.prompt.md` | Retrospective outcomes, open gaps, action owners, release scope, evidence paths | Required Remediation Actions; Evidence Manifest; Release Alignment Summary | Retrospective gate fails when actions are ownerless or due dates are missing; release scope is blocked when evidence packager outputs blockers |

## Invocation Control Requirements
- Every gate must include a recorded invocation timestamp, invoker identity, and artifact path references.
- Every invocation output must include owner accountability for each blocking gap.
- Any gate decision marked `conditional` must include target closure date and governance approver acceptance.
- Missing invocation evidence is treated as a governance control failure.

## Evidence Requirements
- Sprint plan: backlog with requirement mappings and owners
- Implementation evidence: changed files and capability mapping updates
- Verification evidence: test artifacts in `tests/` and outputs in `test-results/`
- Review evidence: approvals, resolved findings, and closed linked issues
- Merge evidence: passing `pre-merge-gate` task and required workflow checks
- Agent and skill evidence: stored outputs from required gate invocations, including blocker ownership and closure targets

## Escalation Path
1. Gate owner marks gate as failed and records blocking criteria.
2. Sprint owner assigns remediation owner and target date.
3. Governance approver validates remediation before gate re-evaluation.

## Review Cadence And Revision Date
- Cadence: Once per sprint at planning, merge, and retrospective checkpoints
- Last revised: 2026-05-19 (agent and skill invocation controls added)

## Sprint Execution Sequence
1. Plan sprint and map all backlog items to requirements, then run Sprint Orchestrator planning gate invocation.
2. Implement work in feature branches, then run verification-auditor invocation for implementation gate evidence.
3. Run local pre-merge gate tool before opening PR.
4. Run PR Compliance Checker and complete PR governance checklist; resolve all linked issues.
5. Run Sprint Orchestrator merge gate invocation; merge only after required checks and approvals pass.
6. Run Sprint Orchestrator retrospective invocation and capture remediation ownership; run release-evidence-packager when sprint scope feeds release scope.
