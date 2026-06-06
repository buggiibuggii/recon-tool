"""initial nyayaai schema

Revision ID: 0001_initial_nyayaai
Revises:
Create Date: 2026-06-06
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "0001_initial_nyayaai"
down_revision = None
branch_labels = None
depends_on = None


def uuid_pk():
    return sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True, nullable=False)


def timestamps():
    return [
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
    ]


def upgrade() -> None:
    op.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp"')
    op.create_table("users", uuid_pk(), sa.Column("email", sa.String(320), nullable=False), sa.Column("phone", sa.String(32)), sa.Column("password_hash", sa.String(255), nullable=False), sa.Column("full_name", sa.String(200), nullable=False), sa.Column("preferred_language", sa.String(16), nullable=False, server_default="en"), sa.Column("role", sa.String(32), nullable=False, server_default="user"), sa.Column("is_active", sa.Boolean(), nullable=False, server_default=sa.text("true")), *timestamps(), sa.UniqueConstraint("email"), sa.UniqueConstraint("phone"))
    op.create_table("sessions", uuid_pk(), sa.Column("user_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("users.id", ondelete="CASCADE"), nullable=False), sa.Column("refresh_token_hash", sa.String(255), nullable=False), sa.Column("device_info", postgresql.JSONB(), nullable=False, server_default="{}"), sa.Column("ip_address", sa.String(64)), sa.Column("expires_at", sa.DateTime(timezone=True), nullable=False), sa.Column("revoked_at", sa.DateTime(timezone=True)))
    op.create_table("legal_articles", uuid_pk(), sa.Column("source_type", sa.String(80), nullable=False), sa.Column("jurisdiction", sa.String(120), nullable=False, server_default="India"), sa.Column("title", sa.String(500), nullable=False), sa.Column("article_number", sa.String(80)), sa.Column("body_summary", sa.Text(), nullable=False), sa.Column("canonical_url", sa.String(1000)), sa.Column("metadata_json", postgresql.JSONB(), nullable=False, server_default="{}"), sa.Column("search_vector", sa.Text()), *timestamps())
    op.create_table("legal_guides", uuid_pk(), sa.Column("slug", sa.String(160), nullable=False, unique=True), sa.Column("category", sa.String(120), nullable=False), sa.Column("title", sa.String(300), nullable=False), sa.Column("summary", sa.Text(), nullable=False), sa.Column("steps", postgresql.JSONB(), nullable=False, server_default="[]"), sa.Column("evidence_checklist", postgresql.JSONB(), nullable=False, server_default="[]"), sa.Column("search_vector", sa.Text()), *timestamps())
    op.create_table("legal_templates", uuid_pk(), sa.Column("slug", sa.String(160), nullable=False, unique=True), sa.Column("template_type", sa.String(120), nullable=False), sa.Column("title", sa.String(300), nullable=False), sa.Column("fields_schema", postgresql.JSONB(), nullable=False, server_default="{}"), sa.Column("body_markdown", sa.Text(), nullable=False), sa.Column("language", sa.String(16), nullable=False, server_default="en"), *timestamps())
    op.create_table("evidence_files", uuid_pk(), sa.Column("user_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("users.id", ondelete="CASCADE"), nullable=False), sa.Column("filename", sa.String(500), nullable=False), sa.Column("content_type", sa.String(160), nullable=False), sa.Column("size_bytes", sa.Integer(), nullable=False), sa.Column("storage_key", sa.String(1000), nullable=False), sa.Column("checksum_sha256", sa.String(64), nullable=False), sa.Column("timeline_at", sa.DateTime(timezone=True)), sa.Column("description", sa.Text()), *timestamps())
    op.create_table("evidence_tags", uuid_pk(), sa.Column("evidence_file_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("evidence_files.id", ondelete="CASCADE"), nullable=False), sa.Column("tag", sa.String(80), nullable=False), sa.UniqueConstraint("evidence_file_id", "tag", name="uq_evidence_file_tag"))
    op.create_table("document_uploads", uuid_pk(), sa.Column("user_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("users.id", ondelete="CASCADE"), nullable=False), sa.Column("filename", sa.String(500), nullable=False), sa.Column("content_type", sa.String(160), nullable=False), sa.Column("storage_key", sa.String(1000), nullable=False), sa.Column("extracted_text", sa.Text()), sa.Column("summary", sa.Text()), sa.Column("language", sa.String(16), nullable=False, server_default="en"), sa.Column("status", sa.String(32), nullable=False, server_default="pending"), *timestamps())
    op.create_table("chat_history", uuid_pk(), sa.Column("user_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("users.id", ondelete="CASCADE"), nullable=False), sa.Column("document_upload_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("document_uploads.id", ondelete="SET NULL")), sa.Column("language", sa.String(16), nullable=False), sa.Column("query", sa.Text(), nullable=False), sa.Column("response", sa.Text(), nullable=False), sa.Column("sources", postgresql.JSONB(), nullable=False, server_default="[]"), sa.Column("confidence", sa.String(32), nullable=False, server_default="medium"), *timestamps())
    op.create_table("bookmarks", uuid_pk(), sa.Column("user_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("users.id", ondelete="CASCADE"), nullable=False), sa.Column("legal_article_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("legal_articles.id", ondelete="CASCADE")), sa.Column("legal_guide_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("legal_guides.id", ondelete="CASCADE")), sa.Column("note", sa.Text()), *timestamps())
    op.create_table("notifications", uuid_pk(), sa.Column("user_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("users.id", ondelete="CASCADE"), nullable=False), sa.Column("title", sa.String(240), nullable=False), sa.Column("body", sa.Text(), nullable=False), sa.Column("channel", sa.String(40), nullable=False, server_default="in_app"), sa.Column("read_at", sa.DateTime(timezone=True)), sa.Column("scheduled_at", sa.DateTime(timezone=True)), *timestamps())
    op.create_table("subscriptions", uuid_pk(), sa.Column("user_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("users.id", ondelete="CASCADE"), nullable=False), sa.Column("plan", sa.String(80), nullable=False, server_default="free"), sa.Column("status", sa.String(40), nullable=False, server_default="active"), sa.Column("amount_inr", sa.Numeric(10, 2)), sa.Column("renews_at", sa.DateTime(timezone=True)), *timestamps())
    op.create_table("lawyer_profiles", uuid_pk(), sa.Column("user_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("users.id", ondelete="CASCADE"), nullable=False, unique=True), sa.Column("bar_registration_number", sa.String(120), nullable=False, unique=True), sa.Column("practice_areas", postgresql.JSONB(), nullable=False, server_default="[]"), sa.Column("languages", postgresql.JSONB(), nullable=False, server_default="[]"), sa.Column("city", sa.String(120), nullable=False), sa.Column("state", sa.String(120), nullable=False), sa.Column("verified_at", sa.DateTime(timezone=True)), *timestamps())


def downgrade() -> None:
    for table in ["lawyer_profiles", "subscriptions", "notifications", "bookmarks", "chat_history", "document_uploads", "evidence_tags", "evidence_files", "legal_templates", "legal_guides", "legal_articles", "sessions", "users"]:
        op.drop_table(table)
