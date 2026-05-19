# Requirements Template

Use this template when writing requirements for sprint or system-level documents.

---

## Format Rule

**All requirements MUST follow noun-verb format:**

```
The <noun> shall <verb> <object/predicate>.
```

- **Noun**: The subject (system, agent, component) that has the obligation.
- **shall**: The mandatory modal verb. Use "shall" for mandatory requirements. Never use "should", "may", "might", or "must".
- **verb**: The action the noun performs.
- **predicate**: What the action produces or achieves; should be measurable where possible.

---

## Examples

### Compliant Requirements ✅
```
The Research Agent shall retrieve at least 10 relevant documents per query.
The system shall generate a patent draft within 120 seconds.
The vector database shall persist embeddings across system restarts.
The CI pipeline shall block PR merge when governance violations are detected.
```

### Non-Compliant Requirements ❌
```
Patent generation must be fast.          → No noun; "must" not allowed; not measurable
Agents should search the web.            → "should" not allowed
The system will validate inputs.         → "will" not allowed
Research documents need to be retrieved. → No "shall"; passive construction
```

---

## Requirement ID Format

| Scope | Format | Example |
|-------|--------|---------|
| System-level | `REQ-NNN` | `REQ-001` |
| Sprint-specific | `SPR-NN-RNN` | `SPR-01-R01` |
| Feature-specific | `FTR-XXX-NNN` | `FTR-RAG-001` |

---

## Requirement Entry Template

```markdown
| ID | Requirement |
|----|-------------|
| REQ-NNN | The <noun> shall <verb> <predicate>. |
```

---

## Automated Validation

Requirements are validated by `scripts/governance/check_requirements.py`. The script checks:
1. Each requirement line starts with `The `.
2. Each requirement contains ` shall `.
3. Each requirement ends with `.`.
4. No requirement uses "should", "must", "will", or "may" in place of "shall".

The check runs automatically on every PR via the `governance-check.yml` workflow.
