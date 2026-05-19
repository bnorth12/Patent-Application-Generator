# Governance Policy – Patent Application Generator

**Version**: 1.0  
**Effective Date**: 2026-05-19  
**Owner**: @bnorth12

---

## 1. Purpose

This policy establishes the governance framework for the development, maintenance, and operation of the Patent Application Generator. It ensures consistent quality, traceability, and compliance throughout the software development lifecycle.

---

## 2. Scope

This policy applies to all contributors, automated processes, and artefacts within the `bnorth12/Patent-Application-Generator` repository.

---

## 3. Requirements Governance

### 3.1 Noun-Verb Format
**All requirements shall be written in noun-verb format:**

> `The <noun> shall <verb> <object/predicate>.`

Examples of compliant requirements:
- `The Research Agent shall retrieve at least 10 relevant documents per query.`
- `The system shall generate a complete patent application draft within 120 seconds.`
- `The vector database shall persist embeddings across system restarts.`

Examples of **non-compliant** requirements:
- ~~"Patent generation must be fast."~~ (no noun, no measurable predicate)
- ~~"Agents should search the web."~~ (uses "should" instead of "shall")

### 3.2 Requirement IDs
Every requirement shall be assigned a unique ID in the format `REQ-NNN` (e.g., `REQ-001`). Sprint-specific requirements use the format `SPR-NN-RNN` (e.g., `SPR-01-R01`).

### 3.3 Automated Enforcement
The `scripts/governance/check_requirements.py` script, executed by the `governance-check.yml` GitHub Actions workflow, shall validate requirement format on every PR. PRs failing this check shall not be merged.

---

## 4. Branching Strategy

See [branching_strategy.md](branching_strategy.md) for full details.

**Summary**:
- `main` – stable, deployable code; protected branch.
- `sprint/sprint-NN` – one branch per sprint; created from `main` before sprint starts.
- Feature work is committed directly to the sprint branch.
- At sprint end, a PR from `sprint/sprint-NN` to `main` is created via the Sprint Close workflow.

---

## 5. Sprint Governance

### 5.1 Sprint Entry (Must be complete before starting a sprint)
- Sprint plan document created at `sprints/sprint_NN/sprint_plan.md`.
- Sprint requirements document created at `sprints/sprint_NN/requirements.md`.
- Sprint stories document created at `sprints/sprint_NN/stories.md`.
- Sprint entry/exit criteria document created at `sprints/sprint_NN/entry_exit_criteria.md`.
- Sprint branch created: `sprint/sprint-NN`.
- All backlog items assigned to the sprint have GitHub issues created.

### 5.2 Sprint Execution
- All commits made to the sprint branch only.
- Governance tests pass on every push.
- No direct commits to `main`.

### 5.3 Sprint Exit (Must be verified before closing a sprint PR)
- All sprint stories marked Done.
- All exit criteria in `entry_exit_criteria.md` verified.
- Governance and CI tests passing on the sprint branch.
- Sprint retrospective notes added to `sprints/sprint_NN/retrospective.md`.

---

## 6. Code Review Policy

- All PRs require at least one approving review from a code owner before merge.
- PRs must pass all required status checks (CI, governance).
- Sprint-close PRs additionally require exit-criteria validation.

---

## 7. Testing Policy

- Unit test coverage shall be ≥ 80% for all new Python source files.
- Governance tests (requirements format, sprint structure) shall always pass.
- No PR shall be merged with known test failures.

---

## 8. Documentation Policy

- Architecture, design, and requirements documents shall be updated in the same PR as any code change that affects them.
- Documents shall use Markdown format.
- Diagrams shall use textual/ASCII representation or Mermaid syntax for version-control compatibility.

---

## 9. Enforcement

| Mechanism | Tool | When |
|-----------|------|------|
| Requirements format | `check_requirements.py` + pytest | Every PR |
| Sprint structure check | `check_sprint_structure.py` + pytest | Every PR |
| Code lint | flake8 (Python), PHP_CodeSniffer (PHP) | Every push |
| Unit tests | pytest / PHPUnit | Every push |
| Code review | GitHub branch protection | Every PR |
| Exit criteria | `validate_exit_criteria.py` | Sprint-close PR |

---

## 10. Policy Violations

Any PR violating this governance policy shall be automatically blocked by GitHub Actions status checks and shall not be merged until violations are resolved.

---

## 11. Policy Review

This policy shall be reviewed at the beginning of each sprint and updated as needed.
