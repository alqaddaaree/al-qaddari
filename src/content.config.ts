import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const books = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/books" }),
  schema: z.object({
    title: z.string(),
    author: z.string(),
    description: z.string(),
    file: z.string(),
  }),
});

export const collections = { books };
