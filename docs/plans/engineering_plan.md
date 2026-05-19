# Engineering Plan – Patent Application Generator

**Version**: 1.0  
**Date**: 2026-05-19  
**Owner**: @bnorth12

---

## 1. Purpose

This plan defines the engineering practices, tooling, build system, and technical standards that govern the construction of the Patent Application Generator.

---

## 2. Repository Structure

```
Patent-Application-Generator/
├── .github/                    # CI/CD workflows, PR templates, issue templates
│   ├── workflows/
│   │   ├── ci.yml
│   │   ├── governance-check.yml
│   │   └── sprint-close.yml
│   ├── PULL_REQUEST_TEMPLATE.md
│   ├── ISSUE_TEMPLATE/
│   └── CODEOWNERS
├── docs/                       # All project documentation
│   ├── architecture/
│   ├── design/
│   ├── governance/
│   ├── plans/
│   └── requirements/
├── backlog/                    # Product backlog
├── sprints/                    # Sprint artefacts (one folder per sprint)
│   ├── sprint_template/
│   └── sprint_01/
├── src/                        # All source code
│   ├── agents/                 # Python LangGraph agents
│   ├── skills/                 # Python skill callables
│   ├── rag/                    # RAG pipeline (ingestion, retrieval)
│   ├── backend/                # CakePHP application
│   └── frontend/               # HTML templates and static assets
├── tests/                      # Automated tests
│   ├── governance/             # Governance validation tests
│   ├── agents/                 # Agent unit tests
│   ├── skills/                 # Skill unit tests
│   ├── rag/                    # RAG pipeline tests
│   ├── backend/                # PHP unit tests
│   └── e2e/                    # End-to-end tests
├── scripts/                    # Utility scripts
│   ├── governance/             # Governance enforcement scripts
│   └── sprint/                 # Sprint lifecycle scripts
├── docker-compose.yml          # Local development stack (Sprint 2+)
└── README.md
```

---

## 3. Build and Development Environment

### 3.1 Python
```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# Install development dependencies
pip install -r src/requirements-dev.txt

# Run tests
pytest tests/ -v --cov=src --cov-report=term-missing

# Lint
flake8 src/ tests/ scripts/ --max-line-length=120
```

### 3.2 PHP / CakePHP
```bash
# Install PHP dependencies
cd src/backend
composer install

# Run tests
vendor/bin/phpunit

# Lint
vendor/bin/phpcs --standard=PSR12 src/
```

### 3.3 Docker Compose (Sprint 2+)
```bash
# Start full stack
docker compose up -d

# View logs
docker compose logs -f orchestrator

# Stop stack
docker compose down
```

---

## 4. Continuous Integration Pipeline

Every push and PR triggers the following in sequence:

1. **Governance Check** (`governance-check.yml`)
   - Requirements format validation
   - Sprint structure check
   - DoD references check
   - Governance tests

2. **Lint** (within `ci.yml`)
   - Python: flake8
   - PHP: PHP_CodeSniffer (Sprint 2+)

3. **Tests** (within `ci.yml`)
   - Python: pytest
   - PHP: PHPUnit (Sprint 2+)

---

## 5. Code Quality Standards

| Metric | Target | Enforcement |
|--------|--------|-------------|
| Python test coverage | ≥ 80% (new files) | pytest-cov (informational in CI initially) |
| PHP test coverage | ≥ 80% (new files) | PHPUnit coverage (Sprint 2+) |
| Lint warnings | 0 errors | CI fail on flake8/phpcs errors |
| Governance tests | 100% pass | CI fail |
| Open critical bugs | 0 before sprint close | Sprint exit criteria |

---

## 6. Dependency Management

### Python
- Production: `src/requirements.txt` (pinned versions)
- Development: `src/requirements-dev.txt` (pinned versions)
- Security scan: `pip-audit` run in CI (Sprint 2+)

### PHP
- `src/backend/composer.json` and `composer.lock`
- `composer audit` for security scan (Sprint 7+)

---

## 7. Environment Configuration

All environment-specific values configured via `.env` files (never committed):

```bash
# .env.example (committed as template)
OPENAI_API_KEY=
DATABASE_URL=postgresql://user:pass@localhost:5432/patentgen
CHROMA_HOST=localhost
CHROMA_PORT=8000
ORCHESTRATOR_URL=http://localhost:8001
REDIS_URL=redis://localhost:6379
APP_SECRET=
JWT_SECRET=
```

---

## 8. Logging and Observability

- Python: `logging` module with JSON formatter; log level configurable via `LOG_LEVEL` env var.
- CakePHP: built-in `Log` class with JSON formatter.
- Log files: `logs/` directory (in `.gitignore`).
- Health endpoints: `/health` (CakePHP) and `/orchestrator/health` (Python).

---

## 9. Security Engineering Practices

- Dependency vulnerability scanning before each new dependency is added.
- Secrets management via environment variables; `.env` in `.gitignore`.
- Prompt injection mitigations in the CakePHP controller before dispatch.
- HTTPS enforced via Nginx configuration (Sprint 2+).
- Authentication required for all API endpoints except health checks.

---

## 10. Related Documents

- [Implementation Plan](implementation_plan.md)
- [Verification Plan](verification_plan.md)
- [Technology Stack](../architecture/technology_stack.md)
- [Development Standards](../governance/development_standards.md)
