from dataclasses import dataclass
from backend.app.schemas.contracts import ChatRequest, ChatResponse, Citation
from .language import detect_language

LEGAL_DISCLAIMER = (
    "NyayaAI provides legal information for awareness only and is not a substitute for advice from "
    "a qualified advocate. For urgent danger, contact local emergency services or appropriate authorities."
)


@dataclass(frozen=True)
class RetrievedSource:
    title: str
    source_type: str
    url: str | None
    locator: str | None
    snippet: str


class LegalRAGService:
    """RAG orchestrator with deterministic fallback for development and tests."""

    def retrieve(self, query: str, language: str) -> list[RetrievedSource]:
        return [
            RetrievedSource(
                title="Constitution of India",
                source_type="primary_law",
                url="https://legislative.gov.in/constitution-of-india/",
                locator="Part III / Fundamental Rights",
                snippet="Fundamental rights and constitutional remedies are primary legal awareness anchors.",
            )
        ]

    def rerank(self, query: str, sources: list[RetrievedSource]) -> list[RetrievedSource]:
        return sources[:5]

    def answer(self, request: ChatRequest) -> ChatResponse:
        language = detect_language(request.query, request.language)
        sources = self.rerank(request.query, self.retrieve(request.query, language))
        citations = [
            Citation(title=s.title, source_type=s.source_type, url=s.url, locator=s.locator)
            for s in sources
        ]
        return ChatResponse(
            answer=(
                "Here is a plain-language legal-awareness summary based on retrieved primary sources. "
                "Preserve documents, note dates, identify the correct authority, and seek professional advice for case-specific strategy."
            ),
            language=language,
            citations=citations,
            next_steps=["Write a dated fact timeline", "Collect identity and evidence documents", "Consult a licensed advocate or legal-aid clinic"],
            risks=["Limitation periods and local procedure can affect remedies", "Facts may require urgent escalation"],
            confidence="medium",
            disclaimer=LEGAL_DISCLAIMER,
        )
