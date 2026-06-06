from pydantic import BaseModel, EmailStr, Field


SUPPORTED_LANGUAGES = [
    "en", "hi", "kn", "ta", "te", "ml", "mr", "bn", "gu", "pa", "ur", "or", "as", "ks",
    "kok", "mai", "ne", "sa", "sd", "sat", "brx", "doi", "mni",
]


class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)
    full_name: str
    preferred_language: str = "en"


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class Citation(BaseModel):
    title: str
    source_type: str
    url: str | None = None
    locator: str | None = None
    date: str | None = None


class ChatRequest(BaseModel):
    query: str = Field(min_length=2, max_length=4000)
    language: str = "en"
    context: dict = Field(default_factory=dict)


class ChatResponse(BaseModel):
    answer: str
    language: str
    citations: list[Citation]
    next_steps: list[str]
    risks: list[str]
    confidence: str
    disclaimer: str


class ReadinessRequest(BaseModel):
    issue_type: str
    facts: str
    available_evidence: list[str] = Field(default_factory=list)
    language: str = "en"


class ReadinessResponse(BaseModel):
    checklist: list[str]
    missing_documents: list[str]
    risk_indicators: list[str]
    suggested_next_steps: list[str]
