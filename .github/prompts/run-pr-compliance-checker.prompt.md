---
name: Run PR Compliance Checker
description: "Run governance preflight checks on a pull request and return deterministic compliance findings before review and merge."
argument-hint: "PR number, linked issue IDs, changed requirement IDs, and governance controls in scope"
agent: "PR Compliance Checker"
tools: [read, search, edit, todo]
---

Run PR Compliance Checker for the target pull request using the provided arguments.

## Inputs To Parse
- Pull request number
- Linked issue IDs
- Changed requirement IDs
- Changed files and evidence paths
- Required governance controls in scope

## Required Outputs
Produce the following sections in order:
- `Compliance Decision`
- `Findings By Control`
- `Blocking Items`
- `Required PR Updates`
- `Recheck Criteria`

## Mandatory Controls
1. PR template required fields must be complete.
2. Governance checklist items must be complete and accurate.
3. Linked issue closure intent must be present and valid.
4. Traceability fields must map changed requirements to implementation and validation artifacts.
5. Evidence references must be present and current.

## Decision Rules
- Any missing required field must be marked as `fail`.
- Any open required issue closure dependency must be marked as `fail`.
- Non-blocking issues may be `conditional` only with owner and closure date.

## Evidence References
Use repository controls and templates, including:
- `.github/pull_request_template.md`
- `docs/governance/traceability-matrix.md`
- `docs/governance/branch-merge-governance.md`

## Completion Check
- All control findings are explicit and auditable.
- Blocking items include owner and remediation action.
- Recheck criteria are deterministic.
