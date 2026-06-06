from dataclasses import dataclass
from backend.app.services.ai.language import detect_language


@dataclass(frozen=True)
class OCRResult:
    extracted_text: str
    summary: str
    language: str
    warnings: list[str]


class DocumentAnalyzer:
    def analyze_text(self, text: str, preferred_language: str = "en") -> OCRResult:
        language = detect_language(text, preferred_language)
        clean = " ".join(text.split())
        summary = clean[:500] if clean else "No readable text was extracted."
        return OCRResult(
            extracted_text=clean,
            summary=f"Simplified summary: {summary}",
            language=language,
            warnings=["OCR output may contain errors; verify names, dates, amounts, and legal references."],
        )
