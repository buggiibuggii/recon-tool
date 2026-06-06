from dataclasses import dataclass


@dataclass(frozen=True)
class RateLimitPolicy:
    key: str
    requests: int
    window_seconds: int


AUTH_LIMIT = RateLimitPolicy("auth", 10, 60)
CHAT_LIMIT = RateLimitPolicy("chat", 30, 60)
OCR_LIMIT = RateLimitPolicy("ocr", 5, 60)
