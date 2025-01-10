// import Image from 'next/image';

import { getDictionary } from '../../get-dictionnary';

export default async function Home({
  params,
}: {
  params: Promise<{ lang: 'en' | 'fr' }>;
}) {
  const lang = (await params).lang;
  const dictionary = await getDictionary(lang);
  console.log('dictionary: ', dictionary);
  return (
    <div className='grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]'>
      <h1>{dictionary.title}</h1>
    </div>
  );
}
