# Agent and Skill Recommendations

## Agent Recommendations

| Agent Name | Role | Required Tools | Constraints | Outputs |
| --- | --- | --- | --- | --- |
| repo-planner | Project planning, requirements, roadmap | read, search, edit, todo | Only planning artifacts | docs/planning/* |
| release-gate | Release governance, gate checks | read, search, edit, todo | No code execution | gate checklist, alignment report |

## Skill Recommendations

| Skill Name | Workflow Covered | Required Inputs | Deliverables |
| --- | --- | --- | --- |
| governance | Governance artifact generation | Objective, scope, compliance | docs/governance/* |
| repo-planner | Planning artifact generation | Objective, constraints, horizon | docs/planning/* |
