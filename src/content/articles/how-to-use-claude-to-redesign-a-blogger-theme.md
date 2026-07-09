---
title: "How to Use Claude to Redesign a Blogger Theme"
date: 2024-01-01
description: |
  Go to Blogger. Open your blog. Go to: Theme → Customize arrow/dropdown → Edit HTML Click inside the code area. Select all: Ctrl + A Copy it: Ctrl + C Go to Claude. Paste your full Blogger template.
tags: ['general']
source: raqmanat
language: ar
---

  1. Go to **Blogger**.
  2. Open your blog.
  3. Go to: 
         
         Theme → Customize arrow/dropdown → Edit HTML

  4. Click inside the code area.
  5. Select all: 
         
         Ctrl + A

  6. Copy it: 
         
         Ctrl + C

  7. Go to Claude.
  8. Paste your full Blogger template.
  9. Then paste this prompt under it: 
         
         I have a Blogger XML template. I want you to redesign it into a serene, elegant, readable blog theme, but you must preserve valid Blogger XML syntax and avoid breaking the Blogger theme parser.
         
         Critical Blogger-specific safety rules:
         - The skin variables inside <b:skin><![CDATA[ ... ]]></b:skin> are extremely sensitive.
         - Never use straight single quotes (') or double quotes (") inside the value attribute of a font-type variable.
         - If a font name contains spaces or needs quotes, escape them:
           use &#39; for single quotes and &quot; for double quotes.
         - Example correct value:
           value="16px &#39;Source Sans 3&#39;, sans-serif"
         - Incorrect:
           value="16px 'Source Sans 3', sans-serif"
         - Do not duplicate any existing variable names.
         - Keep all original Variable definitions unless intentionally changing them.
         - Preserve the exact Blogger XML structure.
         - Preserve Blogger-specific tags like <b:skin>, <b:section>, <b:widget>, <b:include>, <data:...>, and expr:...
         - Prefer a CSS-first redesign.
         - Do not rewrite the whole template unless necessary.
         - Keep the template valid XML.
         - Put CSS changes inside the existing <b:skin><![CDATA[ ... ]]></b:skin> block.
         - Avoid JavaScript unless absolutely necessary.
         - Do not add external libraries unless needed.
         
         Design direction:
         Create a serene, polished, literary blog design.
         
         Mood:
         calm, scholarly, warm, quiet, spacious, slightly archival, elegant but not flashy.
         
         Visual style:
         warm parchment / soft cream background, deep forest green accents, muted gold details, soft card-like reading surface, generous spacing, beautiful typography, readable longform posts, subtle borders, no heavy shadows, no loud colors, no clutter.
         
         Typography:
         - English posts should be highly readable.
         - Arabic text should look dignified and comfortable.
         - Improve line-height, paragraph spacing, post title styling, blockquotes, code blocks, and pre blocks.
         
         Content type:
         The blog will include reflections, translations, Arabic-English material, technical notes, and longform essays.
         
         Specific improvements:
         1. Calmer homepage.
         2. Individual posts should feel like dedicated reading pages.
         3. Improved post cards.
         4. Improved post titles.
         5. Improved header area.
         6. Improved blockquotes.
         7. Improved code/pre blocks.
         8. Improved Arabic RTL sections.
         9. Excellent mobile reading.
         10. Keep everything simple and robust.
         
         Output:
         Give me the full modified Blogger XML template, ready to paste back into Blogger Theme HTML editor.

  10. When Claude gives you the new template, copy it.
  11. Go back to Blogger: 
         
         Theme → Edit HTML

  12. Select all the old code again: 
         
         Ctrl + A

  13. Paste the new code: 
         
         Ctrl + V

  14. Click **Preview** first.
  15. If it looks good, click **Save**.



Important: before doing this, download a backup:
    
    
    Theme → Customize arrow/dropdown → Backup → Download

That way, if Blogger gets angry, you can restore the old theme.

Old theme: 

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg4gyIhT1ICr5SxBbRI_mFqdwriOO9D6hC4VUPUYiWer43DSVvzCKoY3VNYxckBlOnWUDN0WEAU-kAa8mjqcIHm1-CICbWQLOYL1fbJ12yKjncfUtEU0F19Q4awAOGIDL_xHmEFMmjjFuQP_XN8AZosUqQ5Z1zpFHEnPzoGyfnc64vjXk3KLUvi7DJ7ieU/s16000/Screenshot_20260510_180823.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg4gyIhT1ICr5SxBbRI_mFqdwriOO9D6hC4VUPUYiWer43DSVvzCKoY3VNYxckBlOnWUDN0WEAU-kAa8mjqcIHm1-CICbWQLOYL1fbJ12yKjncfUtEU0F19Q4awAOGIDL_xHmEFMmjjFuQP_XN8AZosUqQ5Z1zpFHEnPzoGyfnc64vjXk3KLUvi7DJ7ieU/s1366/Screenshot_20260510_180823.png)

  


[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh9g1Ckl0YbFasZQADZ4w65tlHYkmmPpVEYh1rTCGVjhaCeVAKrjBIx2F3W9vBP6v5Vj0l-uqNmPEaHlEV6wsug1HTGPda81lps7yEdC4DmiPcEF17LQ_C3B0s-w0nYjAsgFJUBdMk22AhSbLxUMVqDPqtFwD_v329xvoBMQzZV3zsOGbRBEWTlLh_gX0Q/s16000/Screenshot_20260510_180858.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh9g1Ckl0YbFasZQADZ4w65tlHYkmmPpVEYh1rTCGVjhaCeVAKrjBIx2F3W9vBP6v5Vj0l-uqNmPEaHlEV6wsug1HTGPda81lps7yEdC4DmiPcEF17LQ_C3B0s-w0nYjAsgFJUBdMk22AhSbLxUMVqDPqtFwD_v329xvoBMQzZV3zsOGbRBEWTlLh_gX0Q/s1366/Screenshot_20260510_180858.png)

  
 New Design: You're experiencing it.
