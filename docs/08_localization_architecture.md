# 8. Localization Architecture

NyayaAI supports 23 Indian languages through translation catalogs, language detection, localized AI prompts, and voice settings.

## Supported language codes

`en`, `hi`, `kn`, `ta`, `te`, `ml`, `mr`, `bn`, `gu`, `pa`, `ur`, `or`, `as`, `ks`, `kok`, `mai`, `ne`, `sa`, `sd`, `sat`, `brx`, `doi`, `mni`.

## Strategy

- Store UI strings in `frontend/src/i18n/languages.ts`.
- Send `language` with chat and document requests.
- Keep legal citations language-neutral; translate explanations, not citations.
- Support speech-to-text and text-to-speech by selected language and device capability.
