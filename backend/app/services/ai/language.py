from backend.app.schemas.contracts import SUPPORTED_LANGUAGES

SCRIPT_HINTS = {
    "hi": "देवनागरी", "ta": "தமிழ்", "te": "తెలుగు", "kn": "ಕನ್ನಡ", "ml": "മലയാളം",
    "bn": "বাংলা", "gu": "ગુજરાતી", "pa": "ਪੰਜਾਬੀ", "ur": "اردو", "or": "ଓଡ଼ିଆ",
}


def normalize_language(language: str | None) -> str:
    code = (language or "en").lower()
    return code if code in SUPPORTED_LANGUAGES else "en"


def detect_language(text: str, preferred: str = "en") -> str:
    if preferred in SUPPORTED_LANGUAGES and preferred != "en":
        return preferred
    for code, marker in SCRIPT_HINTS.items():
        if any(ch in text for ch in marker):
            return code
    return normalize_language(preferred)
