# Governance Baseline

## Scope And Objective
- Repository: Patent-Application-Generator
- Scope: Whole repository, including root documentation and `.github` governance customizations
- Objective: Establish a standard governance baseline with auditable controls, explicit accountability, and release-ready decision gates
- Compliance level: standard

## Owners And Approvers
- Governance owner: Repository Maintainer
- Implementation owner: Contributor assigned to each work item
- Review approver: Code Reviewer
- Release approver: Repository Maintainer

## Control Domains
- Change control: All changes must be linked to an issue or governance requirement.
- Review integrity: Changes require independent review before merge.
- Traceability: Each requirement must map to implementation and validation evidence.
- Release readiness: Release decisions must pass all mandatory HITL gates.
- Exceptions management: Any exception requires rationale, approver, and expiration date.

## Decision Gates And Criteria

### Planning Gate
- Trigger condition: New feature, policy update, or governance-affecting change proposed
- Required evidence: Scope, acceptance criteria, owner assignment
- Approver role: Governance owner
- Pass criteria: Scope and acceptance criteria are explicit and testable
- Fail criteria: Ambiguous scope, missing owner, or missing acceptance criteria

### Implementation Gate
- Trigger condition: Work completed and ready for review
- Required evidence: Linked implementation artifacts and updated governance references when applicable
- Approver role: Implementation owner
- Pass criteria: Implementation aligns to requirement and control domain
- Fail criteria: Unlinked changes or undocumented control impact

### Review Gate
- Trigger condition: Pull request is open and ready for approval
- Required evidence: Reviewer comments, approvals, and addressed findings
- Approver role: Code reviewer
- Pass criteria: Independent review completed and all blocking findings resolved
- Fail criteria: Missing independent review or unresolved blocking findings

### Release Gate
- Trigger condition: Release candidate identified
- Required evidence: Gate summary, outstanding risk log, rollback readiness note
- Approver role: Repository maintainer
- Pass criteria: No failed mandatory controls and rollback path documented
- Fail criteria: Any failed mandatory control or no rollback readiness

### Post-Release Retrospective Gate
- Trigger condition: Release deployed
- Required evidence: Retrospective notes, incidents, follow-up actions with owners
- Approver role: Governance owner
- Pass criteria: Action items captured with due dates and owners
- Fail criteria: No retrospective evidence or unassigned actions

### Issue And PR Closure Gate
- Trigger condition: Issue or PR closure request
- Required evidence: Requirement mapping, implementation link, validation link
- Approver role: Governance owner or delegated reviewer
- Pass criteria: Traceability complete and evidence accessible
- Fail criteria: Missing requirement mapping or missing validation evidence

## Evidence Requirements
- Planning artifacts: Scope statement and acceptance criteria in issue body or governance document
- Implementation artifacts: Files changed and mapped requirement IDs
- Validation artifacts: Reviewer approvals, checklist confirmations, and verification notes
- Release artifacts: GO/NO-GO summary and risk disposition

## Escalation Path
1. Gate owner flags `fail` or unresolved `conditional` status.
2. Repository maintainer reviews blocking condition within one business day.
3. If unresolved, escalate to governance owner for disposition and documented exception or deferral.

## Review Cadence And Revision Date
- Governance review cadence: Every sprint end or monthly, whichever comes first
- Gate effectiveness review: After each release
- Last revised: 2026-05-19

## Initial Gaps
- Branch protection required checks are not yet confirmed as enabled in repository settings.
- Sprint artifacts are established but require active per-sprint population and review discipline.
