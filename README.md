# Kotlin, in five connected ideas

A static site that teaches Kotlin as five "one-idea" lessons — built with
[Astro](https://astro.build) and deployed to GitHub Pages on every push.

## What's here

- **6 pages**: 1 landing + 5 lessons (syntax, classes + null safety, data modeling, scope functions, functional)
- **Zero client-side JS by default** — Astro ships HTML + CSS only
- **One design system** (`src/styles/global.css`) shared across all pages
- **A lesson layout** (`src/layouts/LessonLayout.astro`) for the head, nav, and footer
- **A CI/CD pipeline** (`.github/workflows/deploy.yml`) that builds with Bun and deploys to GitHub Pages

## Quickstart (deploy in 4 minutes)

1. **Create a GitHub repo** (public, so Pages is free).
2. **Push this code** to it:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin git@github.com:<your-user>/<your-repo>.git
   git push -u origin main
   ```
3. **Enable GitHub Pages**: in the repo, go to **Settings → Pages → Build and deployment → Source: GitHub Actions**. (If you skip this step, the first workflow run will fail with a permissions error.)
4. **Watch the workflow run**: **Actions → "Deploy to GitHub Pages"** should turn green in ~30 seconds.
5. **Visit your site**: it'll be at `https://<your-user>.github.io/<your-repo>/`.

That's it. Every push to `main` rebuilds and redeploys.

## Why Bun

The CI uses [Bun](https://bun.sh) — installs in ~5s vs ~30s for npm/yarn, and
Astro's CLI works with it out of the box. The first CI run will create
`bun.lockb`; commit it afterwards for reproducible installs.

## Project layout

```
kotlin-series-astro/
├── .github/workflows/deploy.yml    # CI/CD
├── astro.config.mjs                 # GitHub Pages base + site config
├── package.json
├── public/                          # static assets (favicon, etc.)
├── src/
│   ├── components/
│   │   ├── Nav.astro                # sticky top nav (prev/next/lessons)
│   │   └── Footer.astro
│   ├── layouts/
│   │   └── LessonLayout.astro       # shared head + nav + footer
│   ├── pages/
│   │   ├── index.astro              # landing
│   │   ├── 01-syntax.astro
│   │   ├── 02-classes-null-safety.astro
│   │   ├── 03-data-modeling.astro
│   │   ├── 04-scope-functions.astro
│   │   └── 05-functional.astro
│   └── styles/
│       └── global.css               # design system
└── scripts/                         # build helpers (extract_bodies, build_astro)
```

## Design system

Every page reads from the same CSS custom properties defined in
`src/styles/global.css`:

```css
:root {
  --bg, --bg-card, --line, --line-soft
  --ink, --ink-mid, --ink-soft
  --primary, --primary-soft, --primary-deep   /* per-page */
  --accent, --accent-soft                      /* per-page */
  --code-bg, --code-keyword, ...               /* code colors */
  --space-1 ... --space-30, --fs-*, --r-*
}
```

To recolor a lesson, change the `primary` and `accent` props on
`<LessonLayout>`. To change a global color, edit `global.css`.

## Adding a new lesson

1. Drop a new `.astro` file in `src/pages/`, e.g. `06-coroutines.astro`.
2. Import the layout and pass the props:
   ```astro
   ---
   import LessonLayout from '../layouts/LessonLayout.astro';
   ---
   <LessonLayout title="..." description="..." number={6} primary="..." accent="...">
     ... your content ...
   </LessonLayout>
   ```
3. Update `src/components/Nav.astro` to include the new lesson in the array
   (so the prev/next links work).
4. Commit, push, done.

## Local development (optional)

You don't need to run this locally — the CI handles everything. But if you want to:

```bash
bun install
bun run dev      # http://localhost:4321
bun run build    # → dist/
bun run preview  # serve the built site
```

If you don't have Bun, `npm install && npm run dev` works too — the scripts
in `package.json` are all standard Astro commands.

## How the CI works

```
push to main
     ↓
[Build job, ubuntu + Bun]
   • checkout
   • cache Astro/Vite build artifacts
   • bun install --frozen-lockfile
   • bun run build  →  ./dist
   • upload dist as Pages artifact
     ↓
[Deploy job]
   • actions/deploy-pages → publishes to GitHub Pages
     ↓
Live at https://<user>.github.io/<repo>/
```

Build time: ~20s with cache, ~40s cold.
Deployment: ~5s.

## Custom domain

Drop a `CNAME` file in `public/` containing your domain (e.g. `kotlin.example.com`).
Configure your DNS to point at GitHub Pages, and the workflow will pick it up
on the next run.

## Notes on the build

- **HTML compression** (`compressHTML: true`) ships smaller payloads
- **Inline stylesheets** (`inlineStylesheets: 'auto'`) inlines small CSS files
- **Asset prefix** (`assets: '_assets'`) gives deterministic, cacheable URLs
- **Prefetch on viewport** warms up nav links as the user scrolls

These are tuned for "fast first paint" and "almost-zero JS" out of the box.
