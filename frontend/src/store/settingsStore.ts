import { create } from 'zustand';
import type { LanguageCode } from '@/i18n/languages';

type SettingsState = {
  language: LanguageCode;
  voiceEnabled: boolean;
  setLanguage: (language: LanguageCode) => void;
  setVoiceEnabled: (enabled: boolean) => void;
};

export const useSettingsStore = create<SettingsState>((set) => ({
  language: 'en',
  voiceEnabled: true,
  setLanguage: (language) => set({ language }),
  setVoiceEnabled: (voiceEnabled) => set({ voiceEnabled })
}));
