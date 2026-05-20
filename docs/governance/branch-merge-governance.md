# Branch And Merge Governance

## Scope And Objective
- Scope: All branch, pull request, and merge operations in this repository
- Objective: Eliminate avoidable merge challenges and block merges until linked issues and governance criteria are resolved

## Owners And Approvers
- Branch policy owner: Repository Maintainer
- PR approver: Code Reviewer
- Governance approver: Governance Owner

## Decision Gates And Criteria

### Branch Readiness Gate
- Trigger: Feature branch opened for PR
- Required evidence: Requirement mapping and implementation scope
- Pass criteria: Branch is up to date with base branch and no conflict markers in changed files
- Fail criteria: Branch divergence introduces merge conflict risk or unresolved conflict markers exist

### Issue Resolution Gate
- Trigger: PR review start
- Required evidence: Linked issues list and resolution status
- Pass criteria: All linked issues are closed before merge
- Fail criteria: Any linked issue remains open

### Merge Quality Gate
- Trigger: PR marked ready for merge
- Required evidence: Passing local pre-merge tool, passing workflow checks, and completed PR governance checklist
- Pass criteria: pre-merge-governance-gate workflow is successful; review decision is APPROVED; unresolved review threads count is zero; all required checklist items are checked; linked issues are closed
- Fail criteria: any required check fails; review decision is not APPROVED; unresolved review thread exists; required checklist item is unchecked; linked issue is open

## Evidence Requirements
- Local gate evidence: output from `pre-merge-gate` task
- CI gate evidence: successful `pre-merge-governance-gate` workflow run
- Process evidence: completed PR checklist and review approvals

## Escalation Path
1. Contributor records failed gate and reason in PR notes.
2. Maintainer assigns remediation owner and due date.
3. Governance approver validates remediation before merge proceeds.

## Review Cadence And Revision Date
- Cadence: Per pull request
- Last revised: 2026-05-19

## Required Local Tooling
- VS Code task: `pre-merge-gate`
- Script: `scripts/pre-merge-gate.ps1`

## Required Repository Controls
- Branch protection must require code owner approval.
- Branch protection must require successful status checks.
- Required checks must include `pre-merge-governance-gate`.
