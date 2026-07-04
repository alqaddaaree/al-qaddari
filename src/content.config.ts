import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const books = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/books" }),
  schema: z.object({
    title: z.string(),
    author: z.string(),
    description: z.string(),
    cover: z.string().optional(),
    file: z.string(),
    date: z.date().optional(),
    tags: z.array(z.string()).optional(),
    featured: z.boolean().default(false), // ← add this
  }),
});

const apps = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/apps" }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    type: z.enum(["pwa", "website"]),
    category: z.enum(["تعليمي", "نشر", "مجتمعي", "أداة", "أخرى"]),
    tags: z.array(z.string()).optional(),
    featured: z.boolean().default(false),
    image: z.string().optional(),
    url: z.string().optional(),
    note: z.string().optional(),
    date: z.date().optional(), // ← new field
  }),
});

const articles = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/articles" }),
  schema: z.object({
    title: z.string(),
    date: z.date(),
    description: z.string(),
    tags: z.array(z.string()).optional(),
    draft: z.boolean().default(false),
    source: z.enum([
      'en-armalqaddaaree',
      'armalqaddaaree',
      'al-albaanee',
      'scourgeofphotography',
      'raqmanat',
      'islaamchildrenbooks',
    ]),
    language: z.enum(['ar', 'en']).default('ar'),
    sourceUrl: z.string().optional(),
  }),
});

export const collections = { books, apps, articles };