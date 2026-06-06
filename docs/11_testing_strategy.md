# 11. Testing Strategy

## Test types

- Unit tests for schemas, language utilities, prompt contracts, security helpers, and readiness rules.
- Integration tests for auth, chat, evidence upload, OCR, and document generation endpoints.
- API tests using FastAPI TestClient in backend CI.
- Localization tests verifying all supported language codes have labels and core UI keys.
- Security tests for JWT rejection, rate limit boundaries, upload validation, and ownership checks.

## Current smoke checks

`backend/tests/test_project_contracts.py` verifies required tables, language codes, API route declarations, and documentation ordering without requiring external services.
