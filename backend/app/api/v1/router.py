from fastapi import APIRouter, UploadFile, File
from backend.app.schemas.contracts import ChatRequest, ChatResponse, ReadinessRequest, ReadinessResponse, SUPPORTED_LANGUAGES
from backend.app.services.ai.rag import LegalRAGService
from backend.app.services.ocr.document_analyzer import DocumentAnalyzer

api_router = APIRouter()
rag_service = LegalRAGService()
document_analyzer = DocumentAnalyzer()


@api_router.get("/meta/languages")
def languages() -> dict[str, list[str]]:
    return {"languages": SUPPORTED_LANGUAGES}


@api_router.post("/auth/register")
def register_placeholder() -> dict[str, str]:
    return {"status": "registration endpoint scaffolded"}


@api_router.post("/auth/login")
def login_placeholder() -> dict[str, str]:
    return {"status": "login endpoint scaffolded"}


@api_router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    return rag_service.answer(request)


@api_router.get("/constitution/articles")
def constitution_articles(query: str | None = None) -> dict[str, object]:
    return {"query": query, "items": [], "message": "Searchable Constitution explorer scaffold"}


@api_router.get("/guides")
def legal_guides(category: str | None = None) -> dict[str, object]:
    return {"category": category, "items": [], "message": "Legal guides scaffold"}


@api_router.post("/evidence")
def create_evidence_metadata() -> dict[str, str]:
    return {"status": "evidence metadata endpoint scaffolded"}


@api_router.post("/documents/ocr")
async def analyze_document(file: UploadFile = File(...), language: str = "en") -> dict[str, object]:
    content = await file.read()
    result = document_analyzer.analyze_text(content.decode("utf-8", errors="ignore"), language)
    return result.__dict__


@api_router.post("/documents/generate")
def generate_document(template_type: str) -> dict[str, str]:
    return {"template_type": template_type, "status": "document generation scaffolded"}


@api_router.post("/readiness", response_model=ReadinessResponse)
def analyze_readiness(request: ReadinessRequest) -> ReadinessResponse:
    required = ["Identity proof", "Dated fact timeline", "Relevant notices/messages", "Proof of loss or harm"]
    missing = [item for item in required if item.lower() not in {e.lower() for e in request.available_evidence}]
    return ReadinessResponse(
        checklist=required,
        missing_documents=missing,
        risk_indicators=["Delay may affect remedies", "Incomplete evidence can weaken complaint drafting"],
        suggested_next_steps=["Organize evidence by date", "Identify forum or authority", "Seek legal-aid or advocate review"],
    )


@api_router.get("/notifications")
def notifications() -> dict[str, list[object]]:
    return {"items": []}


@api_router.get("/profile")
def profile() -> dict[str, str]:
    return {"status": "profile endpoint scaffolded"}
