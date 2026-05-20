# Patent Application Generator — Agent Instructions

## Project Overview
Python CLI that generates structured patent draft documents from JSON input.
Governed by a six-gate HITL model; all changes flow through feature branches with squash-merge-only PR closures.
Single maintainer: `@bnorth12` (exception EXC-2026-001 active — see [exceptions log](../docs/governance/governance-exceptions-log.md)).

## Quick Commands
| Action | Command |
|--------|---------|
| Run tests | `python -m pytest tests/` from repo root |
| Local merge gate | VS Code task `pre-merge-gate`, or `powershell -File scripts/pre-merge-gate.ps1 -BaseBranch main` |
| Install git hooks | `powershell -File scripts/install-git-hooks.ps1` |

## Key Files
| Path | Purpose |
|------|---------|
| `src/patent_draft_generator.py` | Core module: `PatentInput` dataclass, `generate_patent_draft()`, `write_draft()` |
| `tests/test_patent_draft_generator.py` | pytest suite: section headers, file I/O, performance |
| `src/sample-input.json` | Reference JSON input structure |
| `scripts/pre-merge-gate.ps1` | Local merge readiness check — **required** before every PR push |
| `docs/governance/` | All governance artifacts (baseline, HITL checklist, traceability, alignment report) |
| `docs/sprint-details/` | Sprint backlog and gate execution plans |
| `.github/pull_request_template.md` | PR template — all fields are required, no section may be left blank |

## Architecture
Single-module Python CLI. JSON input → `PatentInput` dataclass → `generate_patent_draft()` → markdown output.
No external runtime dependencies. Tests use `pytest` only.

## Governance Model
Six mandatory HITL gates in sequence: Planning → Implementation → Review → Release → Post-Release → Issue/PR Closure.
- Full gate definitions: [governance-baseline.md](../docs/governance/governance-baseline.md)
- Branch and merge rules: [branch-merge-governance.md](../docs/governance/branch-merge-governance.md)
- Current sprint execution plan: [sprint-execution-plan.md](../docs/sprint-details/sprint-execution-plan.md)

## PR and Merge Rules — Non-Negotiable
- Merge strategy: **squash merge only**. No merge commits. No rebase merges.
- Branch protection enforces: code owner approval (`@bnorth12`), all conversations resolved, `pre-merge-governance-gate` CI status check passed.
- **All linked issues must be closed before merge.** Exception EXC-2026-001 does NOT waive this requirement.
- Never push directly to `main` — `pre-push-gate.ps1` blocks it; `pre-merge-gate.ps1` must pass locally first.

## Available Agents and Skills
| Name | Type | When to Use |
|------|------|-------------|
| `Sprint Orchestrator` | Agent | Full sprint gate orchestration: planning → retrospective |
| `PR Compliance Checker` | Agent | Pre-merge governance preflight on any PR |
| `Release Gate Governor` | Agent | Multi-stage release go/no-go decisions |
| `verification-auditor` | Skill | Requirement-to-test traceability gap analysis |
| `release-evidence-packager` | Skill | Assemble release evidence bundles for milestone artifacts |

Invoke agents via their matching prompt files in `.github/prompts/`.
For Sprint 1 close: use `/close-sprint-1`.

## Traceability Requirement
Every code or governance change must map to a requirement ID in [traceability-matrix.md](../docs/governance/traceability-matrix.md).
Missing mappings are governance gaps and must be resolved before merge.

## Common Pitfalls
- Do not import `dataclasses` or `json` at module top-level in utility scripts — prefer lazy imports (per project convention).
- `pre-merge-governance-gate` CI workflow must produce a passing status check; a `blocked` mergeable state without CI pass is still a blocker.
- All PR template sections must be filled; partial templates fail PR Compliance Checker.
