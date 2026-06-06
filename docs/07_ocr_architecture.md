# 7. OCR Architecture

OCR accepts image/PDF uploads, validates MIME type and size, stores originals securely, extracts text, detects language, and produces simplified summaries.

## Flow

```text
Upload -> MIME validation -> Virus-scan hook -> Encrypted object storage -> OCR worker -> Text extraction -> Simplification via RAG-safe prompt -> User summary
```

## Implementation points

- `backend/app/services/ocr/document_analyzer.py` contains OCR orchestration placeholders.
- Production workers can use AWS Textract for PDFs/images and Whisper-compatible transcription for audio evidence.
- Extracted text is stored separately from original documents with per-user access controls.
