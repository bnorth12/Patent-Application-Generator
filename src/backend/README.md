# Backend – Patent Application Generator (CakePHP)

This directory will contain the CakePHP 5.x backend application.

## Structure (Sprint 2+)

```
backend/
├── bin/
├── config/
├── src/
│   ├── Controller/
│   │   ├── PatentsController.php   (Sprint 7)
│   │   └── AuthController.php      (Sprint 7)
│   ├── Model/
│   │   ├── Entity/
│   │   └── Table/
│   └── Service/
│       └── OrchestratorService.php (Sprint 7)
├── templates/                       (Sprint 8 – HTML frontend)
├── tests/
├── webroot/
│   ├── css/
│   ├── js/
│   └── index.php
├── composer.json
└── .env.example
```

## Setup (Sprint 2+)

```bash
cd src/backend
composer install
cp .env.example .env
# Edit .env with your database credentials
bin/cake migrations migrate
bin/cake server   # Development server on port 8765
```

## API Endpoints (Sprint 7+)

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/auth/login` | Authenticate user (returns JWT) |
| POST | `/api/auth/logout` | End session |
| POST | `/api/patents` | Create patent generation job |
| GET | `/api/patents/{id}` | Get patent job and draft |
| GET | `/api/patents` | List user's patent jobs |
| GET | `/health` | Health check |

## Related Documents

- [System Architecture](../../docs/architecture/system_architecture.md)
- [Implementation Plan – Sprint 7](../../docs/plans/implementation_plan.md)
