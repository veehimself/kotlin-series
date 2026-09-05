import { defineConfig } from 'astro/config';

// GitHub Pages config.
// The `site` and `base` are wired up by the CI workflow so this works
// for both `username.github.io/repo-name/` deployments and
// custom-domain deployments.
const repo = process.env.GITHUB_REPOSITORY?.split('/')[1] || 'kotlin-series';
const isUserSite = process.env.GITHUB_REPOSITORY?.endsWith('.github.io') ?? false;

export default defineConfig({
  site: `https://${process.env.GITHUB_REPOSITORY_OWNER ?? 'YOUR_USER'}.github.io`,
  base: isUserSite ? '/' : `/${repo}/`,
  trailingSlash: 'always',
  build: {
    inlineStylesheets: 'auto',
    assets: '_assets',
  },
  compressHTML: true,
  prefetch: {
    prefetchAll: true,
    defaultStrategy: 'viewport',
  },
  vite: {
    build: {
      cssMinify: 'esbuild',
      cssCodeSplit: true,
    },
  },
});
