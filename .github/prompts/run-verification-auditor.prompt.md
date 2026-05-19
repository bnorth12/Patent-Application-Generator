---
name: Run Verification Auditor
description: "Validate requirement-to-test-to-result coverage for Sprint 1 scope and produce a deterministic verification readiness decision."
argument-hint: "Requirement IDs, implementation artifacts, test artifacts, result artifacts, and owners"
agent: "agent"
tools: [read, search, edit, todo]
---

Run the `verification-auditor` skill for Sprint 1 verification readiness using the provided arguments.

## Inputs To Parse
- In-scope requirement IDs
- Changed implementation artifacts
- Test artifacts in `tests/`
- Verification result artifacts in `test-results/`
- Owners and target closure dates

## Required Outputs
Produce the following sections:
- `Verification Coverage Table`
- `Verification Gap Report`
- `Verification Readiness Decision`

## Mandatory Validation Rules
- Every in-scope requirement must map to one implementation artifact.
- Every in-scope requirement must map to at least one test artifact.
- Every mapped test must map to at least one result artifact.
- Missing mandatory mappings must be treated as blockers.

## Decision Rules
- `pass`: all mandatory mappings present and current.
- `conditional`: only approved non-blocking gaps with owner and closure date.
- `fail`: any missing mandatory mapping or stale evidence.

## Evidence References
Use source evidence from:
- `docs/governance/traceability-matrix.md`
- `tests/`
- `test-results/`

## Completion Check
- Coverage table is complete for every requirement in scope.
- Gap report includes impact, priority, owner, and closure date.
- Readiness decision is explicit and auditable.
