import pytest

fastapi = pytest.importorskip("fastapi")
pytest.importorskip("email_validator")
from fastapi.testclient import TestClient
from pydantic import ValidationError

from backend.app.main import app
from backend.app.schemas.contracts import UserCreate


def test_fastapi_app_starts_and_serves_health():
    with TestClient(app) as client:
        response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "service": "NyayaAI"}


def test_email_str_models_accept_valid_email():
    user = UserCreate(email="citizen@example.com", password="strong-pass", full_name="Citizen")
    assert str(user.email) == "citizen@example.com"


def test_email_str_models_reject_invalid_email():
    with pytest.raises(ValidationError):
        UserCreate(email="not-an-email", password="strong-pass", full_name="Citizen")
