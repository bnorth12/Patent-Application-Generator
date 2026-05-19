# Development Standards – Patent Application Generator

**Version**: 1.0  
**Owner**: @bnorth12

---

## 1. Python Standards

### 1.1 Style
- Follow PEP-8 with a maximum line length of 120 characters.
- Enforced by `flake8` with `--max-line-length=120`.
- All public functions and classes shall have docstrings.
- Type hints required for all function signatures.

### 1.2 Structure
- Source code lives in `src/`.
- Tests live in `tests/` mirroring the `src/` structure.
- Each module shall have an `__init__.py`.

### 1.3 Testing
- `pytest` is the test runner.
- Test files named `test_<module>.py`.
- Minimum 80% coverage for new files (enforced by `pytest-cov`).

### 1.4 Dependency Management
- Dependencies pinned in `src/requirements.txt`.
- Development dependencies in `src/requirements-dev.txt`.

---

## 2. PHP / CakePHP Standards

### 2.1 Style
- Follow PSR-12 coding standard.
- Enforced by PHP_CodeSniffer (`phpcs`).
- CakePHP conventions (Controller, Model, View naming) shall be followed.

### 2.2 Testing
- PHPUnit 10+ as the test framework.
- CakePHP test helpers used for controller/model testing.
- Minimum 80% coverage for new PHP files.

### 2.3 Dependency Management
- `composer.json` and `composer.lock` committed to the repository.

---

## 3. HTML / Frontend Standards

### 3.1 Style
- HTML5 semantic elements preferred.
- CSS follows a BEM naming convention.
- No inline styles; all styles in `.css` files.
- JavaScript in dedicated `.js` files; no inline scripts.

### 3.2 Accessibility
- All form inputs have associated `<label>` elements.
- WCAG 2.1 Level AA compliance targeted.

---

## 4. Documentation Standards

### 4.1 Format
- All documentation in Markdown (`.md`).
- Diagrams in ASCII or Mermaid syntax.
- Headers use ATX style (`#`, `##`, etc.).

### 4.2 Requirements
- Written in noun-verb format: `The <noun> shall <verb> <predicate>.`
- Assigned unique IDs (`REQ-NNN` or `SPR-NN-RNN`).
- Updated in the same PR as code changes that affect them.

---

## 5. Security Standards

- No secrets, credentials, or API keys in source code.
- All secrets injected via environment variables.
- `.env` files covered by `.gitignore`.
- All user inputs validated and sanitised before processing.
- Dependencies scanned for known vulnerabilities before introduction.

---

## 6. Git Standards

- See [Branching Strategy](branching_strategy.md) for branch naming and workflow.
- Commit messages follow the Conventional Commits format defined in the branching strategy.
- No force-push to `main` or sprint branches.
- No large binary files committed (use Git LFS if necessary).
