---
name: verification-auditor
description: 'Validate requirement-to-test-to-result traceability coverage and produce deterministic verification gap reports with owners and closure dates.'
argument-hint: 'Requirement IDs, implementation scope, test artifact paths, and evidence locations'
user-invocable: true
disable-model-invocation: false
---

# Verification Auditor

## What This Skill Produces
- Verification coverage assessment for planned or changed scope
- Requirement-to-test and test-to-result mapping validation
- Deterministic verification gap report with owner and target closure date
- Verification readiness decision for review and merge gates

## When To Use
- Before PR review for verification completeness checks
- Before merge gate decisions that require evidence completeness
- During sprint retrospective to identify recurring verification debt
- During release readiness to validate evidence completeness

## Required Inputs
- Requirement IDs in scope
- Changed implementation artifacts in scope
- Test artifacts in `tests/`
- Verification result artifacts in `test-results/`
- Owners for each requirement and verification activity

## Procedure
1. Collect in-scope requirement IDs and changed artifacts.
2. Validate each requirement maps to at least one implementation artifact.
3. Validate each requirement maps to at least one test artifact.
4. Validate each mapped test has at least one result artifact.
5. Mark missing links as verification gaps.
6. Assign owner and target closure date for each gap.
7. Publish verification readiness decision with pass or fail status.

## Decision Logic
- Pass: every in-scope requirement has implementation, test, and result mappings.
- Conditional: low-risk non-blocking gaps have approved owner and closure date.
- Fail: any mandatory mapping is missing or evidence is stale or absent.

## Output Templates

### Verification Coverage Table
- Requirement ID
- Implementation artifact
- Test artifact
- Result artifact
- Owner
- Status
- Notes

### Verification Gap Report
- Gap ID
- Missing mapping type
- Impact
- Priority
- Owner
- Target closure date

## Quality Criteria And Completion Checks
- Every in-scope requirement has full mapping coverage.
- Every mapped item has a named owner.
- Missing mappings are explicitly listed as gaps.
- Gate readiness status is explicit and auditable.
