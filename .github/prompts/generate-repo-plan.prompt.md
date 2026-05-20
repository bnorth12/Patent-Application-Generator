---
name: Generate Repo Plan
description: "Generate a full repository plan with requirements, capabilities, path research, agent/skill recommendations, and roadmap. Outputs to docs/planning using starter templates."
argument-hint: "Objective, constraints, planning horizon, and output folder (default: docs/planning)"
agent: "agent"
tools: [read, search, edit, todo]
---

Generate a repository plan using the argument values as inputs.

## Inputs To Parse
- Repo objective and measurable outcomes
- Constraints (time, tooling, policy, compliance, budget)
- Planning horizon (e.g., next release, quarter)
- Output folder (default: docs/planning)

## Required Outputs
Create or update the following files in the output folder using exact names:
- `repo-plan-baseline.md`
- `requirements.md`
- `capability-map.md`
- `path-research.md`
- `agent-skill-recommendations.md`
- `roadmap.md`

## Starter Template Source
- Use starter templates from `docs/planning/templates` as the first source of structure.
- If a target file does not exist, initialize it from its matching `*.template.md` file.
- Preserve template headings and tables unless the user explicitly requests custom structure.

## Content Rules
- Requirements must use noun shall verb format with mandatory measurable condition.
- Capabilities must map to requirements and include success metrics.
- Path research must include 2-3 options with evidence and tradeoffs.
- Agent/skill recommendations must specify role, scope, triggers, and outputs.
- Roadmap must include milestones, owners, dependencies, and acceptance criteria.

## Execution Steps
1. Discover existing planning artifacts in the repository.
2. Initialize missing outputs from `docs/planning/templates`.
3. Generate missing artifacts and update incomplete ones.
4. Validate internal consistency across all generated artifacts.
5. Summarize what was created, what was reused, and remaining risks.

## Completion Check
- All required files exist.
- Requirements are in correct format and mapped to capabilities.
- Path research includes evidence and tradeoffs.
- Agent/skill recommendations and roadmap are present.

Use the repo-planner skill for workflow details: [Repo Planner Skill](../skills/repo-planner/SKILL.md)
