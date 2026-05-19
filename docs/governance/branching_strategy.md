# Branching Strategy – Patent Application Generator

**Version**: 1.0  
**Owner**: @bnorth12

---

## 1. Branch Hierarchy

```
main
├── sprint/sprint-01
├── sprint/sprint-02
├── sprint/sprint-03
└── ...
```

---

## 2. Branch Definitions

### `main`
- **Purpose**: Stable, deployable code.
- **Protection rules**:
  - Direct pushes prohibited.
  - All changes via PR only.
  - Require at least 1 approving review.
  - Require all status checks to pass before merge.
  - Require linear history (no merge commits from sprint branches).

### `sprint/sprint-NN`
- **Purpose**: Development branch for a single sprint (e.g., `sprint/sprint-01`).
- **Created from**: `main` at the start of the sprint.
- **Naming convention**: `sprint/sprint-NN` where `NN` is zero-padded (01, 02, 03…).
- **Lifecycle**:
  1. Created when sprint planning is complete and entry criteria verified.
  2. All sprint work committed to this branch.
  3. At sprint end, Sprint Close workflow creates a PR from this branch to `main`.
  4. Branch is retained (not deleted) after merge for traceability.

---

## 3. Commit Message Convention

All commit messages shall follow the format:

```
<type>(<scope>): <short description>

[optional body]

[optional footer: closes #NN]
```

**Types**: `feat`, `fix`, `docs`, `test`, `refactor`, `chore`, `ci`  
**Scope**: component name – `agents`, `skills`, `rag`, `backend`, `frontend`, `governance`, `sprint-NN`

Examples:
```
feat(agents): add Research Agent base class
docs(sprint-01): add sprint entry/exit criteria
test(governance): add requirements format validation tests
ci: add sprint-close workflow
```

---

## 4. Sprint Branch Workflow

```
1. Sprint planning complete → all sprint artefacts created in sprints/sprint_NN/
2. git checkout main && git pull
3. git checkout -b sprint/sprint-NN
4. git push -u origin sprint/sprint-NN
5. [sprint development work]
6. Trigger: Actions → Sprint Close workflow → inputs: sprint_number, sprint_branch
7. Sprint Close PR created: sprint/sprint-NN → main
8. PR reviewed, exit criteria verified, PR merged
9. main is now updated with sprint deliverables
```

---

## 5. Hotfix Process

If a critical defect is found in `main` between sprints:

1. Create branch `hotfix/HF-NNN` from `main`.
2. Apply fix and add regression test.
3. PR `hotfix/HF-NNN` → `main`.
4. After merge, cherry-pick or rebase the hotfix commit into the active sprint branch.

---

## 6. Tag Naming Convention

Release tags on `main`:

```
v<major>.<minor>.<patch>[-<pre-release>]
```

Examples: `v1.0.0`, `v1.1.0-beta1`, `v2.0.0`
