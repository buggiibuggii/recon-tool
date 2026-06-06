# 10. Security Architecture

## Controls

- JWT access tokens and refreshable sessions.
- Role-based access for users, moderators, lawyers, and admins.
- Password hashing with Argon2/bcrypt-compatible context.
- Signed object storage URLs and strict upload validation.
- Audit logging for auth, uploads, profile changes, and admin actions.
- Rate limiting for authentication, chat, OCR, and document generation.
- Encryption in transit and at rest.
- Prompt-injection defenses for RAG and OCR text.

## Evidence privacy

Evidence belongs to the uploading user. No evidence object is embedded in vector search without explicit consent. Generated summaries should be redacted before support/admin visibility.
