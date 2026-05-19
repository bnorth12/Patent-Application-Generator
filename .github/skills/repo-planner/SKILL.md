---
name: repo-planner
description: 'Create and manage a repository project plan with requirements management (noun shall verb), capability mapping, path research, and recommendations for agents and skills needed to achieve the end goal.'
argument-hint: 'Repo objective, constraints, target outcomes, and planning horizon'
user-invocable: true
disable-model-invocation: false
---

# Repo Planner

## What This Skill Produces
- Project planning baseline for the repository
- Requirements set using noun shall verb format
- Capability map the repository needs to achieve end goals
- Research-backed path options with tradeoffs and recommendation
- Recommended agent and skill portfolio for execution
- Phased implementation roadmap with acceptance criteria
- Default planning artifact files in `docs/planning`

## When To Use
- You need to define or reset repository direction
- Requirements are incomplete, ambiguous, or inconsistent
- Capability needs are known but implementation path is unclear
- You need explicit recommendations for repo-level agents and skills
- You need a governed plan that can be executed and reviewed over sprints

## Required Inputs
- End goal and measurable outcomes
- Constraints (time, tooling, policy, compliance, budget)
- Repository scope (whole repo or selected components)
- Planning horizon (for example: next release, quarter, or annual)
- Stakeholders and decision owners

## Default Output Files
Create or update these files by default unless the user requests a different location:
- `docs/planning/repo-plan-baseline.md`
- `docs/planning/requirements.md`
- `docs/planning/capability-map.md`
- `docs/planning/path-research.md`
- `docs/planning/agent-skill-recommendations.md`
- `docs/planning/roadmap.md`

## Procedure
1. Define planning context, scope, and success criteria.
2. Inventory existing repository assets, workflows, and governance controls.
3. Draft requirements in noun shall verb format.
4. Derive capability model from approved requirements.
5. Research implementation paths for each capability.
6. Evaluate options using evidence, risk, and fit criteria.
7. Recommend best path per capability and identify dependencies.
8. Specify required repository agents and skills to execute the plan.
9. Build phased roadmap with milestones, owners, and acceptance criteria.
10. Validate plan quality and traceability before sign-off.

## Requirements Authoring Standard
- Use the format: `<Noun> shall <verb phrase> <measurable condition>`.
- Keep one obligation per requirement.
- Include unique ID, rationale, owner, and verification method.
- Measurable condition is mandatory for every requirement.

### Requirement Template
- Requirement ID:
- Statement (noun shall verb):
- Rationale:
- Owner:
- Verification method:
- Traceability links:

## Capability Modeling Rules
- Each capability must map to one or more requirements.
- Each capability must include success metric and minimum acceptable threshold.
- Capabilities should be solution-agnostic before option analysis.

### Capability Template
- Capability ID:
- Capability name:
- Supported requirements:
- Success metric:
- Threshold:
- Dependencies:

## Research And Path Evaluation
- Default depth: standard research with 2-3 viable paths and supporting evidence.
- Gather at least two viable paths when feasible.
- Evaluate path quality across:
  - Feasibility
  - Delivery time
  - Operational complexity
  - Governance and compliance fit
  - Long-term maintainability

### Path Evaluation Template
- Path ID and summary:
- Supported capabilities:
- Evidence and references:
- Risks and mitigations:
- Tradeoffs:
- Recommendation status:

## Agent And Skill Planning
- Recommend agents for orchestration, review, and specialized workflows.
- Recommend skills for repeatable, on-demand procedures.
- For each recommendation, define scope, trigger conditions, and expected outputs.

### Agent Recommendation Template
- Agent name:
- Role:
- Required tools:
- Constraints:
- Outputs:

### Skill Recommendation Template
- Skill name:
- Workflow covered:
- Required inputs:
- Deliverables:

## Decision Logic

### Requirements Maturity Branching
- If requirements quality is low, stabilize requirements before capability decomposition.
- If requirements quality is sufficient, proceed directly to capability modeling.

### Research Depth Branching
- If domain uncertainty is high, run deeper research with external validation.
- If uncertainty is low, run focused comparative analysis and decide quickly.

### Execution Architecture Branching
- If work is mostly linear and procedural, prefer skills-first implementation.
- If work requires role isolation, tool constraints, or handoffs, add custom agents.

## Quality Criteria And Completion Checks
- All requirements are in noun shall verb format and uniquely identified.
- Every capability traces to one or more requirements.
- Every recommended path includes evidence, risks, and tradeoffs.
- Agent and skill recommendations include role, scope, triggers, and outputs.
- Roadmap includes milestones, owners, dependencies, and acceptance criteria.
- Open risks and assumptions are documented with resolution actions.

## Suggested Prompts
- `/repo-planner Create a repo plan for next quarter with requirements, capability map, and recommended path options.`
- `/repo-planner Build noun-shall-verb requirements and derive needed capabilities for this repository end goal.`
- `/repo-planner Recommend the agents and skills this repo needs to execute the roadmap with governance controls.`

## Notes
- Prefer concise, testable requirement language.
- Keep planning artifacts traceable and auditable.
- Re-plan incrementally when constraints or goals change.
