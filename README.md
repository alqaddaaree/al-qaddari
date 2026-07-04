# موقع عبد الرحمن القداري

موقع شخصي وبحثي يُعنى بنشر الكتب المحققة، والتطبيقات الرقمية، والمقالات العلمية، وفق منهج السلف الصالح.  
مبني باستخدام **Astro**، ويُدار محتواه عبر **Pages CMS**، ويُستضاف على **Vercel**.

## 📦 التقنيات المستخدمة

- [Astro](https://astro.build/) — الإطار الرئيسي.
- [Pages CMS](https://pagescms.org/) — إدارة المحتوى.
- [Vercel](https://vercel.com/) — النشر والاستضافة.
- [Sharp](https://sharp.pixelplumbing.com/) — تحسين الصور.
- [@astrojs/sitemap](https://docs.astro.build/en/guides/integrations-guide/sitemap/) — خريطة الموقع التلقائية.

---

## 📂 هيكل المجلدات

```
src/
├── components/
│   ├── layout/               # التخطيطات العامة (Base, Page)
│   └── ui/                   # مكونات قابلة لإعادة الاستخدام (بطاقات، تنقل، تذييل)
├── content/
│   ├── books/                # ملفات الكتب (Markdown)
│   ├── apps/                 # ملفات التطبيقات (Markdown)
│   ├── articles/             # ملفات المقالات (Markdown)
│   └── pages/                # صفحات ثابتة (عن، تواصل)
├── pages/
│   ├── index.astro           # الصفحة الرئيسية
│   ├── books/                # قائمة الكتب وتفاصيل كل كتاب
│   ├── apps/                 # قائمة التطبيقات وتفاصيل كل تطبيق
│   ├── articles/             # قائمة المقالات وتفاصيل كل مقال
│   ├── about.astro           # صفحة "نبذة"
│   └── 404.astro             # صفحة الخطأ 404
├── styles/
│   └── global.css            # الأنماط العامة (الخطوط، الألوان، التباعد)
├── content.config.ts         # تعريف مجموعات المحتوى (كولكشن)
└── astro.config.mjs          # إعدادات Astro (مع Sitemap)
```

---

## 📝 مجموعات المحتوى (Collections)

| المجموعة | المسار | الوصف |
|----------|--------|--------|
| **كتب** | `/books` | كتب محققة، مع رابط تحميل (PDF/Google Drive). |
| **تطبيقات** | `/apps` | تطبيقات ويب ومواقع (PWA، مواقع). |
| **مقالات** | `/articles` | مقالات وبحوث علمية (مع دعم المصادر المتعددة). |

### حقول كل مجموعة

#### الكتب
```yaml
title: عنوان الكتاب
author: المؤلف
description: وصف مختصر
file: رابط التحميل
date: تاريخ الإصدار (اختياري)
tags: [وسوم]
featured: true/false (اختياري)
```

#### التطبيقات
```yaml
title: اسم التطبيق
description: وصف مختصر
type: pwa / website
category: تعليمي / نشر / مجتمعي / أداة / أخرى
tags: [وسوم]
featured: true/false
url: رابط التطبيق
note: ملاحظة إضافية
date: تاريخ الإصدار
```

#### المقالات
```yaml
title: عنوان المقال
date: تاريخ النشر
description: وصف مختصر
tags: [وسوم]
draft: true/false
source: armalqaddaaree / en-armalqaddaaree / al-albaanee / scourgeofphotography / raqmanat / islaamchildrenbooks
language: ar / en
sourceUrl: رابط المصدر الأصلي
featured: true/false
```

---

## 🛠️ التطوير المحلي

1. **استنساخ المشروع**
   ```bash
   git clone https://github.com/al-qaddaaree/al-qaddari.git
   cd al-qaddari
   ```

2. **تثبيت الاعتماديات**
   ```bash
   npm install
   ```

3. **تشغيل خادم التطوير**
   ```bash
   npm run dev
   ```
   الموقع متاح على `http://localhost:4321`.

4. **بناء الموقع للإنتاج**
   ```bash
   npm run build
   ```

5. **معاينة البناء**
   ```bash
   npm run preview
   ```

---

## 📬 التواصل

- البريد الإلكتروني: alqaddaaree@gmail.com

**بُنِيَ هذا الموقع بنية اتباع منهج الكتاب والسنة وسلف الأمة الصالح.**  
**والحمد لله رب العالمين.**