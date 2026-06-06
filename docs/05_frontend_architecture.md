# 5. Frontend Architecture

The Expo app uses Expo Router for file-based routing, React Query for server-state, Zustand for local preferences/session state, and React Native Paper for accessible Material components.

## Screen groups

- `(auth)`: login and registration.
- `(tabs)`: home, chat, constitution, guides, evidence, profile.
- `documents`: OCR upload and document generator flows.
- `readiness`: readiness questionnaire and checklist.
- `settings`: language, voice, privacy, notification preferences.

## State

- `useAuthStore`: token and user state.
- `useSettingsStore`: selected language, TTS/STT preferences, theme.
- React Query: cached API responses with invalidation by route.
