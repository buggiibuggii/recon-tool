# 2. Folder Structure

```text
backend/
  app/
    api/v1/              Versioned REST routers
    core/                Settings, security, rate limits, audit
    db/                  SQLAlchemy engine/session/base
    models/              Database ORM models
    schemas/             Pydantic request/response contracts
    services/            AI, OCR, storage, notification, document services
    workers/             Async jobs for OCR, ingestion, notifications
  alembic/versions/      Database migrations
  tests/                 Backend unit/integration tests
frontend/
  app/                   Expo Router screens and route groups
  src/api/               API client and React Query hooks
  src/components/        Reusable UI components
  src/i18n/              Language catalog and translations
  src/store/             Zustand stores
  src/theme/             React Native Paper theme
  src/types/             Shared TypeScript types
  src/utils/             Formatting, validation, voice helpers
docs/                    Specification and architecture documents
infra/                   Deployment, nginx, monitoring, backups
scripts/                 Seeds and operational utilities
```
