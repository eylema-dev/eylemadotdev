# Turkish action wording

WEB-019 revision 0.1.0, 15 October 2026. Base main 9470abae7221cde5de512d38ba1eda5ef8ad1d28; branch codex/turkish-action-copy. Authority: the maintainer asked to use the Turkish expression "eyleme geçmek" during the authorized site publication.

Plan and allowed paths: change the Turkish hero from "Niyetten / eyleme. / Tasarımla." to "Niyetten / eyleme geç. / Tasarımla." in content/tr.json, regenerate public/tr/index.html, and update this bilingual record and tools/translation-pairs.json. English "From intent / to action. / By design." already carries the same meaning and needs no wording change. No architecture, assets, search policy, permissions or dependency changes.

Acceptance: existing 43 tests and repository/build/PR/diff gates; semantic EN/TR review before fingerprints; desktop and 390px mobile visual inspection for wrapping/overflow; exact merged SHA and canonical live hash/MIME/noindex/404 verification after deployment. No new test mirrors a reversible copy edit. Website checks provide no platform execution evidence.

Budget: one scoped PR/merge/deployment, at most two repair cycles. Risk: a longer Turkish line may wrap; retain readable complete text. Revert the scoped copy commit if needed. Roles: Codex architect, implementer, verifier and self-reviewer using GitHub CLI, Python and documented CUA; no independent reviewer claimed. Local, CI, browser and release gates are recorded separately in the PR.
