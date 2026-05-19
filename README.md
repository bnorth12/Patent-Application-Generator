# Patent-Application-Generator

Policy-driven patent application generator with governance gates, traceability, and release controls.

## Purpose

This repository establishes a governed system for planning, building, verifying, and releasing patent application generation capabilities. It combines program planning, sprint governance, branch and merge controls, and auditable release packaging.

## Repository Structure

- src/ - Source code for generator logic and supporting modules
- tests/ - Verification tests mapped to planning requirements
- test-results/ - Verification evidence and run outputs
- docs/planning/ - Program plan, requirements, capability map, path research, and roadmap
- docs/governance/ - Governance baseline, traceability, branch/merge governance, and settings evidence
- docs/sprint-details/ - Sprint execution plan and sprint-level governance artifacts
- releases/ - Immutable release-candidate snapshots and release evidence
- scripts/ - Local governance and merge gate scripts

## Governance Model

Mandatory HITL gates:
1. Planning gate
2. Implementation gate
3. Review gate
4. Release gate
5. Post-release retrospective gate
6. Issue and PR closure gate

Branch and merge governance enforces:
- pull request based changes
- one approving review minimum
- code owner review for owned files
- conversation resolution before merge
- linked issue closure before merge

## Planning Model

Planning artifacts are maintained in docs/planning:
- program-plan.md
- repo-plan-baseline.md
- requirements.md
- capability-map.md
- path-research.md
- agent-skill-recommendations.md
- roadmap.md

Requirements standard:
- format is noun shall verb with measurable condition
- each requirement has owner, rationale, and verification method

## Merge Gate Controls

Local gate:
- script: scripts/pre-merge-gate.ps1
- task: pre-merge-gate in .vscode/tasks.json

CI gate:
- workflow: .github/workflows/pre-merge-governance-gate.yml
- checks mergeability, issue closure, review decision, thread resolution, and PR governance checklist completion

## Templates And Automation

Governance templates:
- docs/governance/templates/index.md

Planning templates:
- docs/planning/templates/index.md

Governance prompt and skill:
- .github/prompts/generate-governance-artifacts.prompt.md
- .github/skills/repo-governance/SKILL.md

Planning prompt and skill:
- .github/prompts/generate-repo-plan.prompt.md
- .github/skills/repo-planner/SKILL.md

## Release Process

1. Complete sprint and governance evidence.
2. Pass local and CI merge gates.
3. Confirm release gate GO decision.
4. Copy release candidate into releases/<version>/ as an immutable snapshot.
5. Capture verification and governance evidence with release notes.

## Current Status

Repository foundations are in place:
- governance and planning artifacts established
- branch ruleset established for main
- merge gate automation added
- structure prepared for implementation and verification expansion
