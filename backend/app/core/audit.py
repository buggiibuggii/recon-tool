from datetime import datetime, timezone
from typing import Any


def audit_event(actor_id: str | None, action: str, metadata: dict[str, Any] | None = None) -> dict[str, Any]:
    return {
        "actor_id": actor_id,
        "action": action,
        "metadata": metadata or {},
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
