import 'server-only';
import { Locale } from './i18n-config';

// We enumerate all dictionaries here for better linting and typescript support
// We also get the default import for cleaner types
const dictionaries = {
  en: () =>
    import('./dictionnaries/en/common.yml').then((module) => module.default),
  fr: () =>
    import('./dictionnaries/fr/common.yml').then((module) => module.default),
};

export const getDictionary = async (locale: Locale) =>
  dictionaries[locale]?.() ?? dictionaries.en();
