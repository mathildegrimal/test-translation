import type { NextConfig } from 'next';
const nextConfig: NextConfig = {
  /* config options here */
  experimental: {
    turbo: {
      rules: {
        '*.yml': {
          loaders: ['yaml-loader'],
          as: '*.js',
        },
      },
    },
  },
};

export default nextConfig;
