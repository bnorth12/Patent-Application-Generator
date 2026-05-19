---
name: release-evidence-packager
description: 'Assemble release evidence bundles from governance, traceability, and verification artifacts and produce release alignment manifests with owner accountability.'
argument-hint: 'Release version, release scope, evidence paths, owners, and target approval date'
user-invocable: true
disable-model-invocation: false
---

# Release Evidence Packager

## What This Skill Produces
- Release evidence bundle inventory and manifest
- Release governance alignment snapshot with pass or fail summary
- Explicit list of missing evidence and required remediation actions
- Packaged evidence path under release-specific folder conventions

## When To Use
- At release candidate cut
- Before release go or no-go decision
- During release gate review and approval workflow

## Required Inputs
- Release identifier and scope
- Required governance artifacts
- Required traceability and verification artifacts
- Approver roles and owners
- Release evidence destination path

## Procedure
1. Confirm release scope and required control set.
2. Collect required governance artifacts and decision records.
3. Collect traceability matrix and verification result artifacts.
4. Build release evidence manifest with source paths and owners.
5. Validate evidence completeness against required controls.
6. Mark missing items as release blockers with remediation owners.
7. Produce release alignment summary for approver decision.

## Required Artifact Checks
- Governance baseline and active gate criteria
- Traceability matrix with current status
- Verification evidence for in-scope requirements
- Exceptions log with approver and expiration metadata
- Repository settings and merge control evidence

## Decision Logic
- Pass: all mandatory evidence is present, current, and owned.
- Conditional: approved exceptions exist with expiration and owner.
- Fail: mandatory evidence is missing, stale, or ownerless.

## Output Templates

### Evidence Manifest
- Artifact name
- Source path
- Owner
- Last updated
- Status

### Release Alignment Summary
- Control area
- Evidence status
- Gap impact
- Remediation owner
- Target closure date

## Quality Criteria And Completion Checks
- Mandatory controls are fully mapped to evidence artifacts.
- Every evidence item has an accountable owner.
- Missing evidence is treated as a blocker unless approved exception exists.
- Output is concise, auditable, and decision-ready.
