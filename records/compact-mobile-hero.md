# Compact mobile introduction

[Türkçe](compact-mobile-hero.tr.md). Task WEB-025, revision 0.1.0, 15 October 2026.

Authority: the maintainer directly requested moving the triangle immediately below the mobile slogan, making the introduction more compact, checking both languages and publishing. Base: `e38f04d1fd0c7d9a6ae9add4a0bbb21abc0b68cf`, current `origin/main`. Branch: `codex/compact-mobile-hero` in the existing isolated website worktree.

Plan: give the shared hero a heading → figure → introduction document order and responsive grid areas; keep the desktop two-column composition; tighten mobile spacing, heading size and paragraph rhythm without removing copy or the diagram caption. Allowed paths: `tools/build.py`, `public/assets/site.css`, generated `public/index.html` and `public/tr/index.html`, this bilingual record and `tools/translation-pairs.json`.

Acceptance: at mobile widths the visible triangle follows the slogan and precedes the introduction, the whole hero is shorter than the preceding release, and content does not overlap or overflow. Verify both exact slogans, the informative figure/caption, desktop composition, language switching, keyboard navigation and disclosure controls. Run the exact contributor commands, deterministic output and filled PR checks; self-review the complete diff before push. After exact-head PR checks and review-thread inspection, verify main CI, Azure state, canonical HTTPS release/hash checks and both live languages before branch cleanup.

Budget: 30 minutes, at most three focused repairs per failing gate, no new dependency or paid resource. Risks: grid row sizing, desktop drift and diagram readability on narrow screens. Browser geometry, screenshots and interactions provide layout evidence; static checks alone do not. Rollback: revert the scoped layout revision and redeploy.

Architect, implementer, verifier and self-reviewer: this Codex GPT-6 session using Python, Git/GitHub CLI, Azure CLI and existing bundled Playwright/Chromium. Browser plugin not available. No independent reviewer is claimed. English/Turkish copy remains semantically unchanged; both generated pages and this companion record are reviewed. Evidence is recorded in the PR and delivery report. Product runtime, commercial service and field acceptance are not applicable.
