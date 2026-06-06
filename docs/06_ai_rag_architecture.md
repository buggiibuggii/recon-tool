# 6. AI/RAG Architecture

Pipeline:

```text
User Query -> Language Detection -> Query Normalization -> Retrieval -> ChromaDB -> Re-ranking -> OpenAI -> Structured Response -> Citation Validation -> User
```

## Guardrails

- Prefer primary legal sources and current statutes.
- Never fabricate citations; return uncertainty if retrieved evidence is insufficient.
- Distinguish legal information from legal advice.
- Do not reproduce copyrighted secondary sources; use them only as taxonomy/reference frameworks.
- Require source IDs, titles, URLs, dates, and paragraph/article identifiers where available.

## Response contract

AI responses include `answer`, `language`, `citations`, `next_steps`, `risks`, `confidence`, and `disclaimer`.
