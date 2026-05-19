# Backlog Refinement Guide – Patent Application Generator

**Version**: 1.0  
**Owner**: @bnorth12

---

## 1. Purpose

Backlog refinement ensures that backlog items are well-defined, correctly estimated, and ready for sprint planning before they are assigned to a sprint.

---

## 2. Refinement Schedule

Backlog refinement shall occur:
- **Weekly**: Review and update the top 2–3 sprints of backlog items.
- **Pre-sprint**: All items planned for the next sprint must be in "Ready" state before sprint planning.

---

## 3. Backlog Item Readiness Criteria ("Ready")

A backlog item is **Ready** for sprint planning when ALL of the following are true:

- [ ] User story written: "As a [role], I want [capability] so that [benefit]."
- [ ] Requirements written in noun-verb format with IDs assigned.
- [ ] Acceptance criteria defined (at least 3 criteria).
- [ ] Story points estimated (Fibonacci: 1, 2, 3, 5, 8, 13, 21).
- [ ] Dependencies identified and are either resolved or tracked.
- [ ] GitHub issue created using the Backlog Item template.
- [ ] Item prioritised (P1–P4) and sprint tentatively assigned.

---

## 4. Story Point Scale

| Points | Complexity |
|--------|-----------|
| 1 | Trivial – less than 1 hour |
| 2 | Small – a few hours |
| 3 | Small-medium – half a day |
| 5 | Medium – 1 day |
| 8 | Medium-large – 2–3 days |
| 13 | Large – most of a sprint week |
| 21 | Extra-large – consider splitting |

---

## 5. Splitting Large Items

Items with ≥ 21 points shall be split into smaller items before assignment to a sprint. Common splitting strategies:
- By data or input type (e.g., split "support PDF and DOCX" into two items).
- By acceptance criterion (each criterion becomes its own story).
- By component (e.g., split agent + tests into separate items).

---

## 6. Refinement Checklist (per session)

- [ ] Review and close completed items from previous sprint.
- [ ] Update priorities of unassigned items.
- [ ] Ensure all Sprint N+1 items are in "Ready" state.
- [ ] Identify any new items surfaced during the current sprint.
- [ ] Check for items that should be split.
- [ ] Update `backlog/product_backlog.md` with any changes.
