#!/usr/bin/env bash
set -euo pipefail
: "${DATABASE_URL:?DATABASE_URL is required}"
mkdir -p backups
pg_dump "$DATABASE_URL" > "backups/nyayaai-$(date -u +%Y%m%dT%H%M%SZ).sql"
