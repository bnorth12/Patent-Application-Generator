# Repository Settings Evidence

## Scope And Objective
- Scope: Repository-level branch protection and merge controls that cannot be enforced by files alone
- Objective: Record auditable evidence that required repository settings are enabled

## Owners And Approvers
- Owner: Repository Maintainer
- Approver: Governance Owner

## Decision Gates And Criteria

### Settings Verification Gate
- Trigger: Initial setup and any repository policy change
- Required evidence: screenshot or settings export references and verification date
- Pass criteria: all required settings are enabled and validated
- Fail criteria: any required setting is disabled or unverifiable

## Evidence Requirements
- Branch protection requires at least one approving review
- Branch protection requires conversation resolution before merge
- Branch protection requires status check `pre-merge-governance-gate`
- Branch protection requires code owner review
- Last verified date and verifier name

## Escalation Path
1. Owner records missing setting and impact.
2. Governance approver sets remediation deadline.
3. Owner re-verifies and records closure evidence.

## Review Cadence And Revision Date
- Cadence: monthly and after repository settings changes
- Last revised: 2026-05-19

## Verification Log
| Date | Verifier | Required Setting | Status | Evidence Reference | Notes |
| --- | --- | --- | --- | --- | --- |
| 2026-05-19 | Repository Maintainer | Approving review required | Configured | GitHub Ruleset `Main Branch Governance Gate` (ID 16603189) | Required approvals set to 1 |
| 2026-05-19 | Repository Maintainer | Conversation resolution required | Configured | GitHub Ruleset `Main Branch Governance Gate` (ID 16603189) | Enabled under pull request additional settings |
| 2026-05-19 | Repository Maintainer | Required status check pre-merge-governance-gate | Pending | GitHub Ruleset `Main Branch Governance Gate` (ID 16603189) | No check contexts currently available in repository UI; add after first workflow run |
| 2026-05-19 | Repository Maintainer | Code owner review required | Configured | GitHub Ruleset `Main Branch Governance Gate` (ID 16603189) | Enabled under pull request additional settings |
