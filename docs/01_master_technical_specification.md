# 1. Master Technical Specification

## Product

**NyayaAI** — **Know Your Rights** — is a multilingual legal-awareness platform for India. It provides guided explanations of rights, legal procedures, document checklists, complaint pathways, evidence organization, document generation, and AI-assisted summaries.

## Non-advice boundary

NyayaAI provides legal information, not professional legal advice. Every AI response must include jurisdictional caveats, emergency escalation guidance where appropriate, and a recommendation to consult a licensed advocate for case-specific advice.

## Personas

- Citizens seeking plain-language legal awareness.
- Students and community volunteers using constitutional and rights explainers.
- NGOs and legal-aid clinics organizing evidence and complaint drafts.
- Advocates optionally listed through verified profiles.

## Functional requirements

1. Authentication with JWT sessions and role-based access.
2. AI Legal Chat with citations and multilingual responses.
3. Constitution Explorer with searchable articles, rights, DPSP, amendments, and landmark case references.
4. Legal Guides for consumer, cybercrime, police, tenant, labour, women, RTI, and other rights.
5. Evidence Vault for images, PDFs, audio, video, timelines, and tags.
6. OCR Document Analysis to extract, summarize, and simplify text.
7. Document Generator for RTI, consumer complaint, cybercrime complaint, police complaint, and legal notice drafts.
8. Case Readiness Analyzer with evidence checklist, missing documents, risks, and next steps.
9. Notifications for reminders, drafts, and updates.
10. User Profile, Settings, subscriptions, bookmarks, language, and accessibility preferences.
11. Multi-language support for English, Hindi, Kannada, Tamil, Telugu, Malayalam, Marathi, Bengali, Gujarati, Punjabi, Urdu, Odia, Assamese, Kashmiri, Konkani, Maithili, Nepali, Sanskrit, Sindhi, Santali, Bodo, Dogri, and Manipuri.
12. Voice assistant with speech-to-text and text-to-speech integration points.

## Knowledge policy

Primary legal sources include the Constitution of India, BNS, BNSS, BSA, judgments, Law Commission reports, Gazette notifications, and parliamentary materials. Secondary sources such as leading treatises may inform taxonomy and pedagogy but must not be copied.

## System qualities

- Privacy-first evidence storage.
- Secure uploads and encryption at rest.
- Audit logging for sensitive actions.
- Low-latency search with re-ranking.
- Transparent citations and uncertainty handling.
- Production deployments in AWS Mumbai (`ap-south-1`).
