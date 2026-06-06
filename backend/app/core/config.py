from functools import lru_cache
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "NyayaAI"
    environment: str = "development"
    api_v1_prefix: str = "/api/v1"
    database_url: str = "postgresql+psycopg://nyaya:nyaya@postgres:5432/nyaya"
    redis_url: str = "redis://redis:6379/0"
    jwt_secret_key: str = Field(default="change-me-in-production", min_length=16)
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    openai_api_key: str | None = None
    chroma_host: str = "chroma"
    chroma_port: int = 8000
    s3_bucket: str = "nyayaai-evidence"
    aws_region: str = "ap-south-1"
    max_upload_mb: int = 50

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


@lru_cache
def get_settings() -> Settings:
    return Settings()
