# 4. Backend Architecture

The backend is a FastAPI service organized around versioned routers, SQLAlchemy persistence, service-layer business logic, and background workers.

## API modules

- `auth`: registration, login, refresh, logout, session management.
- `chat`: language detection, RAG retrieval, answer generation, citations, safety warnings.
- `constitution`: article search, rights taxonomy, amendments, cases.
- `guides`: legal guide listing, detail, bookmarks.
- `evidence`: secure upload metadata, tags, timelines.
- `documents`: OCR upload, generated complaint drafts, templates.
- `readiness`: checklist and missing-evidence analysis.
- `notifications`: reminders and preference-aware delivery.
- `profile`: language, voice, accessibility, subscription, lawyer profile.

## Cross-cutting services

- JWT and role checks in `backend/app/core/security.py`.
- Settings in `backend/app/core/config.py`.
- Audit logging in `backend/app/core/audit.py`.
- Rate-limit primitives in `backend/app/core/rate_limit.py`.
