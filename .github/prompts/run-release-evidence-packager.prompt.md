---
name: Run Release Evidence Packager
description: "Assemble a release evidence manifest from governance, traceability, and verification artifacts with explicit blockers and approver-ready summary."
argument-hint: "Release ID, release scope, evidence artifact paths, owners, and approval date"
agent: "agent"
tools: [read, search, edit, todo]
---

Run the `release-evidence-packager` skill using the provided release inputs.

## Inputs To Parse
- Release identifier
- Release scope and included requirement IDs
- Required evidence artifact paths
- Approver roles and owners
- Release target decision date

## Required Outputs
Produce the following sections:
- `Evidence Manifest`
- `Release Alignment Summary`
- `Release Blockers`
- `Remediation Actions`
- `Readiness Decision`

## Mandatory Artifact Checks
- Governance baseline and gate criteria must be present.
- Traceability matrix status must be current for release scope.
- Verification evidence must be present for in-scope requirements.
- Exceptions log entries must include approver and expiration date.
- Repository settings and merge control evidence must be present.

## Decision Rules
- `pass`: all mandatory evidence present, current, and owned.
- `conditional`: approved exception with owner and expiration metadata.
- `fail`: any mandatory evidence missing, stale, or ownerless.

## Evidence References
Use repository sources including:
- `docs/governance/governance-baseline.md`
- `docs/governance/traceability-matrix.md`
- `docs/governance/governance-exceptions-log.md`
- `docs/governance/repo-settings-evidence.md`
- `test-results/`

## Completion Check
- Every required control maps to at least one evidence artifact.
- Every missing item is listed as a blocker with owner and closure date.
- Final readiness decision is explicit and auditable.
