# English action slogan

[Türkçe](english-action-slogan.tr.md). Task WEB-024, revision 0.1.0, 15 October 2026.

## Request and plan

Authority: the maintainer directly requested “Don’t stop. Take action.” as the English slogan, matching “Durma Eyleme Geç”, and authorized completing checks and publishing the site. Base: `871b9dd6730cc7335f82a49a18dc339c283039da`, current `origin/main`. Branch: `codex/english-action-slogan` in the existing isolated website worktree.

Allowed paths: `content/en.json`, generated `public/index.html`, this bilingual record and `tools/translation-pairs.json`. Plan: update the English headline within the existing three-line layout, review its meaning against Turkish, regenerate the page and translation fingerprints, run repository checks, verify desktop/mobile rendering, self-review the diff, deliver through a PR and verify the published merge revision.

## Acceptance, risk and budgets

- Exact slogans: inspect normalized rendered headings in English and Turkish.
- Responsive presentation: inspect desktop and mobile screenshots, including 320-pixel overflow, loaded triangle diagrams and language switching.
- Local gates: exact contributor commands, deterministic build check, translation review, filled PR-body validation and whitespace check.
- Publication: exact-head PR checks and review threads, post-merge main checks, Azure deployment state, canonical HTTPS release identity and file hashes, then live browser verification.

Budget: 30 minutes and at most three focused repairs per failing gate; no new dependency or paid resource. Risk: headline wrapping or a stale generated page. Rollback: revert this scoped copy change and redeploy. The Turkish headline and shared triangle remain current; the two slogans express the same call to act.

## Roles and evidence

Architect, implementer, verifier and self-reviewer: this Codex GPT-6 session using Python, Git/GitHub CLI, Azure CLI and existing bundled Playwright/Chromium. No separate reviewer is claimed. Check results are recorded in the PR and delivery report; this plan does not itself establish passing checks or publication. Product runtime, field deployment and commercial service acceptance are not applicable to this copy revision.
