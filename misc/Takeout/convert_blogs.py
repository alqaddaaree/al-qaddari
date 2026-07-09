#!/usr/bin/env python3
"""
Convert Blogger Atom feeds to Markdown files for Astro content collections.
"""

import os
import re
import feedparser
from pathlib import Path
from datetime import datetime
import html2text

# Configuration
SOURCE_MAP = {
    "Abdurrahmaan Al-Qaddaary": "en-armalqaddaaree",
    "Islamic Chidren_s Books": "islaamchildrenbooks",
    "رقمنة": "raqmanat",
    "عبد الرحمن بن ميهوب القداري": "armalqaddaaree",
}

LANGUAGE_MAP = {
    "Abdurrahmaan Al-Qaddaary": "en",
    "Islamic Chidren_s Books": "ar",
    "رقمنة": "ar",
    "عبد الرحمن بن ميهوب القداري": "ar",
}

def slugify(text):
    """Convert text to a URL-friendly slug."""
    # Remove special characters
    text = re.sub(r'[^\w\s-]', '', text)
    # Convert to lowercase
    text = text.lower()
    # Replace spaces with hyphens
    text = re.sub(r'[-\s]+', '-', text)
    # Remove leading/trailing hyphens
    text = text.strip('-')
    # Limit length
    return text[:100] if text else "post"

def extract_tags(entry):
    """Extract tags/categories from the entry."""
    tags = []
    if hasattr(entry, 'tags'):
        for tag in entry.tags:
            if hasattr(tag, 'term') and tag.term:
                tags.append(tag.term)
    return tags[:5]  # Limit to 5 tags

def extract_description(content, title):
    """Extract first 2-3 sentences as description."""
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', content)
    # Clean up whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    # Get first 250 characters
    if len(text) > 250:
        text = text[:250]
        # Try to cut at a sentence boundary
        last_period = text.rfind('.')
        if last_period > 100:
            text = text[:last_period + 1]
    # If still empty, use title
    if not text or len(text) < 10:
        return title
    return text

def convert_atom_to_markdown(feed_path, output_dir, source_key, language):
    """Convert an Atom feed to Markdown files."""
    print(f"Processing: {feed_path}")

    feed = feedparser.parse(feed_path)

    if not feed.entries:
        print(f"  No entries found in {feed_path}")
        return

    # Create output directory
    os.makedirs(output_dir, exist_ok=True)

    # Create HTML to Markdown converter
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = False
    h.body_width = 0

    count = 0
    for entry in feed.entries:
        # Extract title
        title = entry.title if hasattr(entry, 'title') else "Untitled"
        title = title.strip()

        # Extract date
        if hasattr(entry, 'published'):
            date_str = entry.published
            try:
                # Try parsing with timezone
                date_obj = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S%z')
                date = date_obj.strftime('%Y-%m-%d')
            except ValueError:
                try:
                    # Try without timezone
                    date_obj = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S')
                    date = date_obj.strftime('%Y-%m-%d')
                except:
                    date = '2024-01-01'
        else:
            date = '2024-01-01'

        # Extract content
        content = ''
        if hasattr(entry, 'content') and entry.content:
            content = entry.content[0].value
        elif hasattr(entry, 'summary'):
            content = entry.summary

        # If no content, skip
        if not content:
            print(f"  Skipping: {title} (no content)")
            continue

        # Generate description
        description = extract_description(content, title)

        # Extract tags
        tags = extract_tags(entry)
        if not tags:
            tags = ['general']

        # Generate slug from title
        slug = slugify(title)

        # Convert content to Markdown
        markdown_content = h.handle(content)

        # Build frontmatter
        frontmatter = f"""---
title: {title}
date: {date}
description: {description[:200]}{'...' if len(description) > 200 else ''}
tags: {str(tags) if tags else '[]'}
source: {source_key}
language: {language}
---
"""

        # Write file
        filename = f"{slug}.md"
        filepath = os.path.join(output_dir, filename)

        # Handle duplicate slugs
        if os.path.exists(filepath):
            filename = f"{slug}-{count}.md"
            filepath = os.path.join(output_dir, filename)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(frontmatter)
            f.write('\n')
            f.write(markdown_content)

        count += 1
        print(f"  Wrote: {filename}")

    print(f"  ✓ Converted {count} posts from {source_key}")

def main():
    # Get the current directory
    base_dir = Path.cwd()

    # Find the Blogs directory inside Blogger
    blogs_dir = base_dir / 'Blogger' / 'Blogs'
    if not blogs_dir.exists():
        print("Error: 'Blogger/Blogs' directory not found.")
        print("Please run this script from the Takeout folder (where 'Blogger/' is located).")
        return

    # Output directory for articles
    output_dir = base_dir / 'articles_markdown'
    os.makedirs(output_dir, exist_ok=True)

    # Process each blog
    for blog_name, source_key in SOURCE_MAP.items():
        blog_path = blogs_dir / blog_name
        feed_path = blog_path / 'feed.atom'

        if feed_path.exists():
            language = LANGUAGE_MAP.get(blog_name, 'ar')
            blog_output = output_dir / source_key
            convert_atom_to_markdown(str(feed_path), str(blog_output), source_key, language)
        else:
            print(f"Feed not found: {feed_path}")

    print("\n✅ Done! Markdown files saved to:", output_dir)
    print("Copy them to your Astro project:")
    print(f"  cp -r {output_dir}/* ../al-qaddari/src/content/articles/")

if __name__ == "__main__":
    main()
