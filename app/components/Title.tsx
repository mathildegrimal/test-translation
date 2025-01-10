'use-client';

import { useTranslation } from 'react-i18next';

export const Title = ({ lng }: { lng: string }) => {
  const { t } = useTranslation(lng);

  return <h1>{t('title')}</h1>;
};
