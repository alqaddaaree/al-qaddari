// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// https://astro.build/config
export default defineConfig({
  site: 'https://al-qaddari.com', // ← Replace with your actual domain
  integrations: [
    sitemap({
      // Optional: filter pages
      // filter: (page) => !page.includes('/admin'),
      // Optional: change changefreq
      // changefreq: 'weekly',
      // Optional: change priority
      // priority: 0.7,
    }),
  ],
});