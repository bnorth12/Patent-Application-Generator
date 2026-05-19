# Sprint 01 – Entry and Exit Criteria

**Sprint Number**: 01  
**Sprint Branch**: `sprint/sprint-01`

> ⚠️ Sprint 01 is the bootstrap sprint. Entry criteria are satisfied when all governance documents and this sprint plan are committed to the repository. The sprint cannot be marked "In Progress" until all entry criteria are checked.

---

## Entry Criteria

All of the following must be true before the sprint branch is created and work begins:

- [ ] Sprint plan document completed (`sprint_plan.md`) ✅ (this document)
- [ ] Sprint requirements document completed (`requirements.md`)
- [ ] Sprint stories document completed (`stories.md`)
- [ ] Entry/exit criteria document completed (this document)
- [ ] Governance policy document present at `docs/governance/governance_policy.md`
- [ ] Definition of Done document present at `docs/governance/definition_of_done.md`
- [ ] Branching strategy document present at `docs/governance/branching_strategy.md`
- [ ] Development standards document present at `docs/governance/development_standards.md`
- [ ] System requirements document present at `docs/requirements/system_requirements.md`
- [ ] All planning documents present in `docs/plans/`
- [ ] Product backlog defined at `backlog/product_backlog.md`
- [ ] Sprint 01 branch created: `sprint/sprint-01`

---

## Exit Criteria

All of the following must be true before the sprint-close PR is merged:

- [ ] All 9 Sprint 01 stories are in "Done" state
- [ ] All Sprint 01 requirements (SPR-01-R01 through SPR-01-R14) verified
- [ ] Governance scripts (`check_requirements.py`, `check_sprint_structure.py`) execute without errors
- [ ] All governance tests pass: `pytest tests/governance/ -v`
- [ ] CI workflow (`ci.yml`) passes on the `sprint/sprint-01` branch
- [ ] Governance-check workflow (`governance-check.yml`) passes
- [ ] System requirements document validated by `check_requirements.py` with zero violations
- [ ] No open Critical or High severity bugs
- [ ] Sprint 02 artefacts complete (story STORY-01-009 done)
- [ ] Sprint retrospective notes added to `sprint_plan.md`
- [ ] Sprint-close PR created from `sprint/sprint-01` → `main` via the Sprint Close workflow
- [ ] Sprint-close PR references and closes all Sprint 01 GitHub issues
- [ ] Sprint-close PR reviewed and approved by @bnorth12

---

## Verification Status

| Criterion | Status | Evidence |
|-----------|--------|---------|
| All 9 stories Done | ⬜ | |
| Requirements validated (0 violations) | ⬜ | |
| Governance tests pass | ⬜ | |
| CI checks pass | ⬜ | |
| No open Critical/High bugs | ⬜ | |
| Sprint 02 artefacts complete | ⬜ | |
| Retrospective complete | ⬜ | |
| Sprint-close PR created | ⬜ | |
| Sprint-close PR approved | ⬜ | |
