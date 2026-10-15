# Ecosystem, field data and specialist subscriptions

[Türkçe](ecosystem-positioning.tr.md). Task WEB-023, revision 0.1.0, 15 October 2026.

## Request and plan

Authority: the maintainer's direct request in this chat to revise the website around Eyleme's open-source community ecosystem, Derleme's physical-world data collection and cloud/on-premises recording, and Onama's cybersecurity, authority, responsibility and regulatory workflows. Derleme and Onama are the paid specialist products. This request authorizes the website revision and draft PR; it does not authorize deployment, billing, repository visibility or permission changes.

Base: `b3b5e14382be7e87bf6ade2aa027e9c5db55c256`, current website `origin/main`. Branch: `codex/website-ecosystem-positioning`. A separate worktree preserves other checkouts. Allowed paths: `content/en.json`, `content/tr.json`, `tools/build.py`, `public/assets/site.css`, generated landing pages, README companions, this bilingual record and `tools/translation-pairs.json`.

Plan: make development status visible in the hero; explain the three complementary product roles; add a public subscription section that explains the specialist value; synchronize metadata, FAQ and community copy; regenerate and validate both languages; inspect rendered desktop/mobile navigation and disclosures; self-review and deliver a draft PR. Existing component evidence remains scoped to its original review date. No new runtime acceptance is claimed.

## Acceptance, risk and budgets

- Ecosystem and current development status: inspect both hero sections and metadata.
- Derleme: visible field/sensor/machine data and planned cloud or on-premises recording, with source and quality context.
- Onama: visible cybersecurity, access authority, responsibilities, audit records and regulatory compliance workflows, without a certification or guaranteed-compliance claim.
- Subscriptions: public open-source core remains independently usable; commercial expertise is described without invented prices, packages, service levels or checkout availability.
- Verification: exact contributor commands, deterministic build/check, reviewed EN/TR fingerprints, filled PR-body validation, browser identity/nonblank/console/screenshots, language switching, subscription navigation, FAQ and architecture keyboard behavior.

Budget: 60 minutes, at most three focused repairs per failed gate; no new dependencies, paid service, image generation or runtime/model training. Risks: confusing product direction with delivered service, implying shared-brand access rights, or making legal guarantees. Keep future wording and explicit availability boundaries. Rollback: revert the scoped website change; no data migration.

## Roles and evidence

Architect, implementer, verifier and self-reviewer: this Codex GPT-6 session, using Python, Git/GitHub CLI and browser automation. No separate reviewer is claimed. Browser plugin/skill is not available; regular Playwright uses the existing bundled runtime. Independent/maintainer review is pending. Local and PR-CI results are recorded in the PR; website checks do not establish Rust, GPU, model, training, field deployment or commercial service acceptance.

Local verification: passed on macOS arm64 with Python 3.15.0 (the exact `python3` contributor commands), all 54 repository tests, generated-output check, reviewed EN/TR fingerprints, blank-template structure and whitespace check. No dependency was installed: the hash-locked CI inventory is standard-library only. CI separately uses Python 3.14. Browser verification: passed in bundled Playwright 1.62.1 / Chromium at 1280 × 900 and 390 × 844 in both languages, plus 320-pixel overflow checks and JavaScript-disabled subscription/FAQ checks. The tested flow was landing page → subscription navigation → specialist scope and development status, with reciprocal language switching, product and community navigation, FAQ open/close, Assign → ArrowRight → Inspect, loaded images and zero console warnings/errors. Desktop product/subscription sections and mobile/desktop hero screenshots were visually reviewed; artifacts are outside the repository. Runtime, cloud/on-premises installation, legal compliance and paid subscriptions: not_run, outside this website task. PR CI and independent review are separate gates.
