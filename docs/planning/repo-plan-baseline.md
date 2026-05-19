# Repo Plan Baseline

## Planning Context
- Objective: Build a policy-driven system for generating, governing, and managing patent application workflows.
- Scope: Whole repository, including governance, planning, and automation assets.
- Planning horizon: Initial implementation and first release (1-2 sprints).
- Stakeholders: Repository maintainer, contributors, legal reviewers, end users.

## Success Criteria
- System can generate patent application drafts from structured inputs.
- Governance artifacts and traceability are enforced for all major changes.
- Planning and architecture docs are up to date and actionable.

## Constraints
- Time: Deliver initial working system in 1-2 sprints.
- Tooling: Prefer open-source, auditable tools and scripts.
- Policy/compliance: Must support traceability, HITL gates, and evidence capture.
- Budget: Minimal; leverage automation and templates.

## Existing Assets
- README with governance and contribution strategy.
- Governance baseline and traceability matrix in docs/governance.
- Planning and governance templates in docs/governance/templates and docs/planning/templates.
- Program plan and sprint execution plan with governance gate criteria.
- Local and CI pre-merge governance gate tooling.

## Initial Gaps
- Source implementation and test suites are not yet populated with working generation logic.
- Branch protection required-check configuration remains to be enabled in repository settings.
- Release candidate packaging process is defined but not yet exercised on a real release.
