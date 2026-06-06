export type LanguageCode =
  | 'en' | 'hi' | 'kn' | 'ta' | 'te' | 'ml' | 'mr' | 'bn' | 'gu' | 'pa' | 'ur' | 'or' | 'as'
  | 'ks' | 'kok' | 'mai' | 'ne' | 'sa' | 'sd' | 'sat' | 'brx' | 'doi' | 'mni';

export const supportedLanguages: { code: LanguageCode; label: string; nativeLabel: string }[] = [
  { code: 'en', label: 'English', nativeLabel: 'English' },
  { code: 'hi', label: 'Hindi', nativeLabel: 'हिन्दी' },
  { code: 'kn', label: 'Kannada', nativeLabel: 'ಕನ್ನಡ' },
  { code: 'ta', label: 'Tamil', nativeLabel: 'தமிழ்' },
  { code: 'te', label: 'Telugu', nativeLabel: 'తెలుగు' },
  { code: 'ml', label: 'Malayalam', nativeLabel: 'മലയാളം' },
  { code: 'mr', label: 'Marathi', nativeLabel: 'मराठी' },
  { code: 'bn', label: 'Bengali', nativeLabel: 'বাংলা' },
  { code: 'gu', label: 'Gujarati', nativeLabel: 'ગુજરાતી' },
  { code: 'pa', label: 'Punjabi', nativeLabel: 'ਪੰਜਾਬੀ' },
  { code: 'ur', label: 'Urdu', nativeLabel: 'اردو' },
  { code: 'or', label: 'Odia', nativeLabel: 'ଓଡ଼ିଆ' },
  { code: 'as', label: 'Assamese', nativeLabel: 'অসমীয়া' },
  { code: 'ks', label: 'Kashmiri', nativeLabel: 'कॉशुर' },
  { code: 'kok', label: 'Konkani', nativeLabel: 'कोंकणी' },
  { code: 'mai', label: 'Maithili', nativeLabel: 'मैथिली' },
  { code: 'ne', label: 'Nepali', nativeLabel: 'नेपाली' },
  { code: 'sa', label: 'Sanskrit', nativeLabel: 'संस्कृतम्' },
  { code: 'sd', label: 'Sindhi', nativeLabel: 'سنڌي' },
  { code: 'sat', label: 'Santali', nativeLabel: 'ᱥᱟᱱᱛᱟᱲᱤ' },
  { code: 'brx', label: 'Bodo', nativeLabel: 'बड़ो' },
  { code: 'doi', label: 'Dogri', nativeLabel: 'डोगरी' },
  { code: 'mni', label: 'Manipuri', nativeLabel: 'মৈতৈলোন্' }
];

export const strings = {
  en: {
    appName: 'NyayaAI',
    tagline: 'Know Your Rights',
    chat: 'AI Legal Chat',
    constitution: 'Constitution',
    guides: 'Legal Guides',
    evidence: 'Evidence Vault',
    readiness: 'Case Readiness',
    settings: 'Settings'
  }
} as const;
