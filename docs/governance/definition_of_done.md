# Definition of Done – Patent Application Generator

**Version**: 1.0  
**Owner**: @bnorth12

---

## 1. Definition of Done for a User Story

A user story is considered **Done** when ALL of the following criteria are met:

- [ ] All acceptance criteria defined in the story are demonstrably satisfied.
- [ ] Code is committed to the sprint branch and pushed to the remote.
- [ ] Unit tests written covering the new/changed code (≥ 80% coverage for new files).
- [ ] All existing tests continue to pass.
- [ ] Governance tests pass (requirements format, sprint structure).
- [ ] Code lint passes (flake8 for Python, PHPCS for PHP).
- [ ] All new requirements written in noun-verb format and assigned IDs.
- [ ] Related documentation updated (architecture, design, requirements docs as applicable).
- [ ] RAG knowledge base populated with any research artefacts relevant to the story.
- [ ] Peer code review completed and approved.
- [ ] No unresolved critical/high severity bugs introduced.

---

## 2. Definition of Done for a Sprint

A sprint is considered **Done** when ALL of the following criteria are met:

- [ ] All sprint stories meet the Definition of Done for User Stories (above).
- [ ] Sprint exit criteria in `sprints/sprint_NN/entry_exit_criteria.md` are verified.
- [ ] Sprint retrospective document created at `sprints/sprint_NN/retrospective.md`.
- [ ] Sprint branch (`sprint/sprint-NN`) passes all CI checks.
- [ ] Sprint-close PR created from `sprint/sprint-NN` to `main`.
- [ ] Sprint-close PR references and closes all GitHub issues for the sprint.
- [ ] Sprint-close PR reviewed and approved.
- [ ] Sprint-close PR merged to `main`.

---

## 3. Definition of Done for a Feature (Epic)

A feature is considered **Done** when ALL of the following criteria are met:

- [ ] All user stories composing the feature are Done.
- [ ] End-to-end tests demonstrate feature functionality.
- [ ] Feature is documented in the relevant architecture/design documents.
- [ ] Feature requirements are verified (linked to tests).
- [ ] Feature is demonstrated to the product owner.

---

## 4. Definition of Done for a Release

A release is considered **Done** when ALL of the following criteria are met:

- [ ] All planned features for the release are Done.
- [ ] All release requirements verified.
- [ ] Security review completed; no known critical/high vulnerabilities.
- [ ] Deployment tested in a staging environment.
- [ ] Release notes written.
- [ ] Version tagged in git (`v<major>.<minor>.<patch>`).

---

## 5. DoD Enforcement

The governance CI workflow enforces DoD compliance automatically where possible (tests, lint, requirements format). Human reviewers are responsible for verifying acceptance criteria and documentation completeness during code review.
