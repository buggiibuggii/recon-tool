# NyayaAI — Know Your Rights

NyayaAI is a production-oriented multilingual legal-awareness platform for India. It helps citizens understand rights, legal procedures, complaint options, evidence requirements, timelines, costs, and next steps without presenting itself as a substitute for a licensed advocate.

## What is included

- Expo React Native mobile app scaffold with TypeScript, Expo Router, Zustand, React Query, React Native Paper, localization, and voice/OCR-ready flows.
- FastAPI backend scaffold with JWT authentication, role-based access, PostgreSQL models, Alembic migration, RAG services, OCR/document analysis, secure uploads, notifications, audit logging, and rate limiting hooks.
- ChromaDB/OpenAI RAG architecture with citations, language detection, re-ranking, and hallucination-prevention guardrails.
- Docker Compose stack for API, PostgreSQL, Redis, ChromaDB, worker, and frontend development.
- CI/CD, monitoring, backup, disaster-recovery, and security documentation.

## Legal and copyright posture

NyayaAI should cite primary legal sources and summarize secondary commentary only as high-level reference frameworks. It must not reproduce copyrighted books, commentary, or long passages. The product returns legal information and awareness, not legal advice.

## Repository layout

```text
backend/   FastAPI API, SQLAlchemy models, Alembic migrations, tests
frontend/  Expo React Native app scaffold
docs/      Master specification, architecture, ERD, roadmaps, security, testing
infra/     Docker, nginx, monitoring, backup scripts
scripts/   Utility scripts and seed data helpers
```

## Quick start

```bash
cp .env.example .env
docker compose up --build
```

API health endpoint: `http://localhost:8000/health`

## Documentation

Start with [`docs/01_master_technical_specification.md`](docs/01_master_technical_specification.md), then continue through the numbered architecture documents in the requested output order.
