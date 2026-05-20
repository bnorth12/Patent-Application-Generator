# Program Plan

## Scope And Objective
- Scope: Repository-wide planning and execution for patent application generation capabilities
- Objective: Deliver a governed, auditable MVP and release-ready operating model
- Planning horizon: Two initial sprints plus release readiness review

## End-State Outcomes
- The repository must contain executable source code that generates draft patent application outputs.
- The repository must enforce requirement traceability from planning through verification.
- The repository must enforce sprint and release governance gates before merge and release.

## Program Requirements Management
- Requirements source of truth: `docs/planning/requirements.md`
- Requirement format: noun shall verb with measurable condition
- Requirement ownership: each requirement must have a named owner and verification method
- Requirement change control: updates must be linked to issue and pull request evidence

## Capability Delivery Plan
1. Capability foundation: draft generation pipeline and template model
2. Governance foundation: HITL gates, traceability checks, and branch/merge controls
3. Verification foundation: mapped tests and stored evidence
4. Release foundation: immutable release candidate snapshots and gate decisions

## Architecture Direction
- Preferred path: modular Python service and template engine, with governance-as-code artifacts in markdown
- Architecture style: layered workflow
  - Input and validation layer
  - Draft assembly and template layer
  - Verification and evidence layer
  - Governance and release gate layer
- Extensibility rule: new patent type support must be added by new template/rule modules without rewriting core workflow

## Agents And Skills Operating Model
- Planning skill: `repo-planner` produces and maintains planning artifacts
- Governance skill: `repo-governance` produces and maintains governance artifacts
- Release gate agent: `Release Gate Governor` evaluates go/no-go evidence and unresolved gaps

## Delivery Milestones
1. Planning and governance baseline complete
2. MVP draft generation implementation complete
3. Verification mapping and result capture complete
4. Pre-merge governance gate automation complete
5. Release candidate package and release decision complete

## Dependencies
- Branch protections configured to require code owner review and required status checks
- Maintainer-defined release approver role
- Repeatable local pre-merge command execution

## Risks And Mitigations
- Risk: ambiguous requirements reduce implementation quality
  - Mitigation: strict requirement format and measurable condition checks
- Risk: late governance evidence collection blocks release
  - Mitigation: collect evidence per sprint and enforce pre-merge gates
- Risk: merge friction from unresolved issues and review debt
  - Mitigation: automated merge gate and explicit issue-resolution controls

## Acceptance Criteria
- Planning artifacts exist and are internally consistent.
- Each planned capability maps to one or more requirements.
- Branch/merge governance controls are documented and executable.
- Sprint execution plan defines mandatory governance evidence per sprint.
- Standard compliance readiness must include evidence that mandatory merge controls are CI-enforced: approved review decision, zero unresolved review threads, closed linked issues, and completed governance checklist.
- Each milestone must identify owner and validation artifact location.
