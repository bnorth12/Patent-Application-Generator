---
name: Close Sprint 1
description: "Orchestrate full Sprint 1 closure: sprint gate verification, issue closure, PR compliance preflight, pre-merge-gate validation, and squash merge following repo governance rules."
argument-hint: "Sprint 1 scope, open issue IDs, PR number"
tools: [read, search, edit, todo, mcp_gitkraken_git_status, mcp_gitkraken_issues_get_detail, mcp_gitkraken_pull_request_get_detail]
---

Orchestrate a complete, governance-compliant Sprint 1 close using the Sprint Orchestrator and PR Compliance Checker agents, then guide the squash merge of PR #7 following all repo rules.

## Step 1 — Sprint Gate Verification

Invoke the `Sprint Orchestrator` agent with the following inputs:

- Sprint ID: `Sprint-1`
- Sprint objective: Deliver REQ-001, REQ-002, REQ-003 — core patent draft generator, JSON input handling, pytest verification suite
- Scope: `src/patent_draft_generator.py`, `tests/test_patent_draft_generator.py`, all governance artifacts in `docs/`
- Requirement IDs in scope: REQ-001, REQ-002, REQ-003, REQ-GOV-001 through REQ-GOV-008
- Owner: `@bnorth12`
- Evidence sources:
  - `docs/sprint-details/sprint-execution-plan.md`
  - `docs/sprint-details/sprint-1-backlog.md`
  - `docs/governance/traceability-matrix.md`
  - `docs/governance/hitl-gate-checklist.md`
  - `docs/governance/governance-alignment-report.md`
  - `test-results/sprint-1/sprint-1-test-evidence.md`

Gate sequence to evaluate:
1. Planning gate
2. Implementation gate
3. Review gate
4. Merge gate
5. Retrospective gate

**Hard stop**: If any mandatory gate is `fail`, halt and report blockers. Do not proceed to Step 2.

---

## Step 2 — PR Compliance Preflight

Invoke the `PR Compliance Checker` agent with:

- PR number: `7`
- Linked issues required for closure: `#3`, `#4`, `#5`, `#6`
- Changed requirement IDs: REQ-001, REQ-002, REQ-003, REQ-GOV-001 through REQ-GOV-008
- Active exception: EXC-2026-001 (single-maintainer review, expires 2026-06-19)
- Governance controls in scope: all six HITL gates, squash-merge-only policy, branch protection

Required evidence references:
- `.github/pull_request_template.md`
- `docs/governance/traceability-matrix.md`
- `docs/governance/branch-merge-governance.md`
- `docs/governance/governance-exceptions-log.md`

**Decision rule**: Any `fail` finding halts progression. Conditional findings require owner and target closure date before merge.

---

## Step 3 — Issue Closure Verification

Verify that all Sprint 1 issues are closed (required before merge — no exceptions):

| Issue | Title | Required Status |
|-------|-------|-----------------|
| #3 | Sprint 1 kickoff and gate tracking | Closed |
| #4 | REQ-001 prototype implementation | Closed |
| #5 | Sprint 1 tests + evidence | Closed |
| #6 | Traceability matrix and planning updates | Closed |

If any issue is still open:
- Confirm it is referenced in the PR body with `closes #N` syntax.
- Verify all acceptance criteria documented in the issue are met.
- Close the issue manually if all criteria are met and evidence is present in the repository.

**Hard stop**: Do not proceed to Step 4 if any issue from the table above remains open.

---

## Step 4 — Local Pre-Merge Gate

Confirm the local pre-merge gate has been executed successfully. The user must run this before the final push:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/pre-merge-gate.ps1 -BaseBranch main
```

Or use the VS Code task: **pre-merge-gate**

Expected outcome: Script exits with no errors. Any conflict markers, whitespace violations, or merge conflicts block progression.

---

## Step 5 — CI Gate Verification

Confirm the `pre-merge-governance-gate` GitHub Actions workflow has passed on PR #7.

- Workflow file: `.github/workflows/pre-merge-governance-gate.yml`
- Required status: `✅ pass` (not pending, not failed)
- A `blocked` mergeable state without CI pass is still a blocker.

If the workflow is pending: wait for completion. If it failed: report the failure step and halt.

---

## Step 6 — Squash Merge Execution

When all prior steps are `pass`:

1. Confirm the PR branch is up to date with `main`.
2. Confirm all PR conversations are resolved.
3. Confirm code owner review is approved (`@bnorth12`).
4. Execute **squash merge** — not a standard merge, not a rebase merge.
5. Delete the feature branch after merge.

Squash commit message must include:
- PR number reference (`#7`)
- Sprint 1 scope summary
- Linked issue numbers that are closed by this merge

---

## Step 7 — Post-Merge Validation

After merge:

1. Confirm `main` branch reflects the merged commit.
2. Confirm all linked issues (#3, #4, #5, #6) are closed in GitHub.
3. Update `docs/governance/hitl-gate-checklist.md` — Issue/PR Closure gate: mark complete with merge date and commit SHA.
4. Update `docs/governance/governance-alignment-report.md` — resolve any open gaps related to PR #7 merge readiness.
5. Record retrospective findings in `docs/sprint-details/sprint-execution-plan.md`.

---

## Output Format

Return sections in this order:

1. `Sprint 1 Close Summary` — overall pass/fail/conditional verdict
2. `Gate-by-Gate Status` — one row per gate with status, owner, evidence reference
3. `Issue Closure Status` — one row per issue (#3–#6) with open/closed status
4. `PR Compliance Status` — compliance verdict with blocking items if any
5. `Merge Execution Status` — squash merge outcome and commit SHA
6. `Post-Merge Action Items` — any outstanding artifact updates with owners and due dates
