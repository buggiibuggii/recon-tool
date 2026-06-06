import uuid
from datetime import datetime
from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, Numeric, String, Text, UniqueConstraint
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from backend.app.db.base import Base


class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)


class User(Base, TimestampMixin):
    __tablename__ = "users"
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email: Mapped[str] = mapped_column(String(320), unique=True, index=True, nullable=False)
    phone: Mapped[str | None] = mapped_column(String(32), unique=True)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    full_name: Mapped[str] = mapped_column(String(200), nullable=False)
    preferred_language: Mapped[str] = mapped_column(String(16), default="en", nullable=False)
    role: Mapped[str] = mapped_column(String(32), default="user", nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    sessions = relationship("Session", back_populates="user")


class Session(Base):
    __tablename__ = "sessions"
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    refresh_token_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    device_info: Mapped[dict] = mapped_column(JSONB, default=dict, nullable=False)
    ip_address: Mapped[str | None] = mapped_column(String(64))
    expires_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    revoked_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    user = relationship("User", back_populates="sessions")


class ChatHistory(Base, TimestampMixin):
    __tablename__ = "chat_history"
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    document_upload_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("document_uploads.id", ondelete="SET NULL"))
    language: Mapped[str] = mapped_column(String(16), nullable=False)
    query: Mapped[str] = mapped_column(Text, nullable=False)
    response: Mapped[str] = mapped_column(Text, nullable=False)
    sources: Mapped[list] = mapped_column(JSONB, default=list, nullable=False)
    confidence: Mapped[str] = mapped_column(String(32), default="medium", nullable=False)


class LegalArticle(Base, TimestampMixin):
    __tablename__ = "legal_articles"
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    source_type: Mapped[str] = mapped_column(String(80), nullable=False)
    jurisdiction: Mapped[str] = mapped_column(String(120), default="India", nullable=False)
    title: Mapped[str] = mapped_column(String(500), nullable=False)
    article_number: Mapped[str | None] = mapped_column(String(80))
    body_summary: Mapped[str] = mapped_column(Text, nullable=False)
    canonical_url: Mapped[str | None] = mapped_column(String(1000))
    metadata_json: Mapped[dict] = mapped_column(JSONB, default=dict, nullable=False)
    search_vector: Mapped[str | None] = mapped_column(Text)


class LegalGuide(Base, TimestampMixin):
    __tablename__ = "legal_guides"
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    slug: Mapped[str] = mapped_column(String(160), unique=True, nullable=False)
    category: Mapped[str] = mapped_column(String(120), nullable=False)
    title: Mapped[str] = mapped_column(String(300), nullable=False)
    summary: Mapped[str] = mapped_column(Text, nullable=False)
    steps: Mapped[list] = mapped_column(JSONB, default=list, nullable=False)
    evidence_checklist: Mapped[list] = mapped_column(JSONB, default=list, nullable=False)
    search_vector: Mapped[str | None] = mapped_column(Text)


class LegalTemplate(Base, TimestampMixin):
    __tablename__ = "legal_templates"
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    slug: Mapped[str] = mapped_column(String(160), unique=True, nullable=False)
    template_type: Mapped[str] = mapped_column(String(120), nullable=False)
    title: Mapped[str] = mapped_column(String(300), nullable=False)
    fields_schema: Mapped[dict] = mapped_column(JSONB, default=dict, nullable=False)
    body_markdown: Mapped[str] = mapped_column(Text, nullable=False)
    language: Mapped[str] = mapped_column(String(16), default="en", nullable=False)


class EvidenceFile(Base, TimestampMixin):
    __tablename__ = "evidence_files"
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    filename: Mapped[str] = mapped_column(String(500), nullable=False)
    content_type: Mapped[str] = mapped_column(String(160), nullable=False)
    size_bytes: Mapped[int] = mapped_column(Integer, nullable=False)
    storage_key: Mapped[str] = mapped_column(String(1000), nullable=False)
    checksum_sha256: Mapped[str] = mapped_column(String(64), nullable=False)
    timeline_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    description: Mapped[str | None] = mapped_column(Text)
    tags = relationship("EvidenceTag", back_populates="evidence_file")


class EvidenceTag(Base):
    __tablename__ = "evidence_tags"
    __table_args__ = (UniqueConstraint("evidence_file_id", "tag", name="uq_evidence_file_tag"),)
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    evidence_file_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("evidence_files.id", ondelete="CASCADE"), nullable=False)
    tag: Mapped[str] = mapped_column(String(80), nullable=False)
    evidence_file = relationship("EvidenceFile", back_populates="tags")


class DocumentUpload(Base, TimestampMixin):
    __tablename__ = "document_uploads"
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    filename: Mapped[str] = mapped_column(String(500), nullable=False)
    content_type: Mapped[str] = mapped_column(String(160), nullable=False)
    storage_key: Mapped[str] = mapped_column(String(1000), nullable=False)
    extracted_text: Mapped[str | None] = mapped_column(Text)
    summary: Mapped[str | None] = mapped_column(Text)
    language: Mapped[str] = mapped_column(String(16), default="en", nullable=False)
    status: Mapped[str] = mapped_column(String(32), default="pending", nullable=False)


class Bookmark(Base, TimestampMixin):
    __tablename__ = "bookmarks"
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    legal_article_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("legal_articles.id", ondelete="CASCADE"))
    legal_guide_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("legal_guides.id", ondelete="CASCADE"))
    note: Mapped[str | None] = mapped_column(Text)


class Notification(Base, TimestampMixin):
    __tablename__ = "notifications"
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    title: Mapped[str] = mapped_column(String(240), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    channel: Mapped[str] = mapped_column(String(40), default="in_app", nullable=False)
    read_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    scheduled_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))


class Subscription(Base, TimestampMixin):
    __tablename__ = "subscriptions"
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    plan: Mapped[str] = mapped_column(String(80), default="free", nullable=False)
    status: Mapped[str] = mapped_column(String(40), default="active", nullable=False)
    amount_inr: Mapped[float | None] = mapped_column(Numeric(10, 2))
    renews_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))


class LawyerProfile(Base, TimestampMixin):
    __tablename__ = "lawyer_profiles"
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False)
    bar_registration_number: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    practice_areas: Mapped[list] = mapped_column(JSONB, default=list, nullable=False)
    languages: Mapped[list] = mapped_column(JSONB, default=list, nullable=False)
    city: Mapped[str] = mapped_column(String(120), nullable=False)
    state: Mapped[str] = mapped_column(String(120), nullable=False)
    verified_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
