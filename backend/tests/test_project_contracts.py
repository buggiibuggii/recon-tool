from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

REQUIRED_TABLES = {
    "users", "sessions", "chat_history", "legal_articles", "legal_guides", "legal_templates",
    "evidence_files", "evidence_tags", "document_uploads", "bookmarks", "notifications",
    "subscriptions", "lawyer_profiles",
}

REQUIRED_LANGUAGES = {
    "en", "hi", "kn", "ta", "te", "ml", "mr", "bn", "gu", "pa", "ur", "or", "as", "ks",
    "kok", "mai", "ne", "sa", "sd", "sat", "brx", "doi", "mni",
}


def test_requested_documentation_order_exists():
    for index, name in enumerate([
        "master_technical_specification", "folder_structure", "database_schema", "backend_architecture",
        "frontend_architecture", "ai_rag_architecture", "ocr_architecture", "localization_architecture",
        "devops_architecture", "security_architecture", "testing_strategy", "mvp_roadmap",
        "phase_2_roadmap", "phase_3_roadmap",
    ], start=1):
        assert (ROOT / "docs" / f"{index:02d}_{name}.md").exists()


def test_database_migration_declares_required_tables():
    migration = (ROOT / "backend" / "alembic" / "versions" / "0001_initial_nyayaai.py").read_text()
    for table in REQUIRED_TABLES:
        assert f'"{table}"' in migration


def test_frontend_and_backend_language_catalogs_match():
    frontend = (ROOT / "frontend" / "src" / "i18n" / "languages.ts").read_text()
    backend = (ROOT / "backend" / "app" / "schemas" / "contracts.py").read_text()
    for code in REQUIRED_LANGUAGES:
        assert f'"{code}"' in backend
        assert f"'{code}'" in frontend


def test_api_routes_cover_core_features():
    router = (ROOT / "backend" / "app" / "api" / "v1" / "router.py").read_text()
    for route in ["/auth/register", "/auth/login", "/chat", "/constitution/articles", "/guides", "/evidence", "/documents/ocr", "/documents/generate", "/readiness", "/notifications", "/profile"]:
        assert route in router
