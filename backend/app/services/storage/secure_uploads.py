import hashlib
from dataclasses import dataclass

ALLOWED_MIME_TYPES = {
    "application/pdf", "image/jpeg", "image/png", "audio/mpeg", "audio/wav", "video/mp4",
}


@dataclass(frozen=True)
class UploadValidation:
    ok: bool
    checksum_sha256: str
    error: str | None = None


def validate_upload(content: bytes, content_type: str, max_mb: int) -> UploadValidation:
    checksum = hashlib.sha256(content).hexdigest()
    if content_type not in ALLOWED_MIME_TYPES:
        return UploadValidation(False, checksum, "Unsupported file type")
    if len(content) > max_mb * 1024 * 1024:
        return UploadValidation(False, checksum, "File exceeds maximum size")
    return UploadValidation(True, checksum)
