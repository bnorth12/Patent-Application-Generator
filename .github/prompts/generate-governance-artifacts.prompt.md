---
name: Generate Governance Artifacts
description: "Generate policy-driven governance artifacts for this repository in one run, including HITL gates, traceability matrix, sprint governance, and alignment report."
argument-hint: "Objective, scope, compliance level (light|standard|strict), and output folder"
agent: "agent"
tools: [read, search, edit, todo]
---

Generate governance artifacts for this repository using the argument values as inputs.

## Inputs To Parse
- Governance objective
- Scope (whole repository or selected paths)
- Compliance level: `light`, `standard`, or `strict` (default to `standard` if omitted)
- Output folder (default: `docs/governance`)

## Required Outputs
Create or update the following files in the output folder using exact names:
- `governance-baseline.md`
- `hitl-gate-checklist.md`
- `traceability-matrix.md`
- `sprint-governance-plan.md`
- `governance-alignment-report.md`

Also create `governance-exceptions-log.md` when any exception is needed.

## Starter Template Source
- Use starter templates from `docs/governance/templates` as the first source of structure.
- If a target file does not exist, initialize it from its matching `*.template.md` file.
- Preserve template headings and tables unless the user explicitly requests custom structure.

## Content Rules
- Enforce policy-first language with explicit owners and approval points.
- Include pass/fail criteria for each gate.
- Include requirement to implementation to validation mappings in the matrix.
- Identify governance gaps with impact, priority, owner, and closure date.

## Execution Steps
1. Discover existing governance artifacts in the repository.
2. Initialize missing outputs from `docs/governance/templates`.
3. Generate missing artifacts and update incomplete ones.
4. Validate internal consistency across all generated artifacts.
5. Summarize what was created, what was reused, and remaining risks.

## Completion Check
- All required files exist.
- Gate checklist includes planning, implementation, review, release, post-release, and issue/PR closure gates.
- Traceability matrix has no unmapped requirements without documented exceptions.

Use the governance skill for workflow details: [Repo Governance Skill](../skills/repo-governance/SKILL.md)
