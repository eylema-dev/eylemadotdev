# Eylema website plan

[Türkçe](plan.tr.md). Task `WEB-001`, revision `0.2.0`.

Maintainer requests (11 October 2026, current Codex conversation): a promotional site for `eylema.dev`, SEO/GEO foundations, default English, and a separate source repository. The latest explicit requests rename that repository to `eylema-dev/eylemadotdev` and make it public; they supersede the earlier private-repository choice. Repository publication is authorized. Live hosting and domain changes are a separate acceptance step.

Base: `a08b78d9210035aafdd2db35958f0c2d854c94c2`, the website repository bootstrap on `origin/main`. Branch: `codex/eylema-website`. Allowed paths: this separate website repository; do not edit the platform checkout. Deliver site changes through a draft PR. Public visibility and the canonical Git remote are checked after the authorized rename.

## Scope and acceptance

1. Explain the architecture-stage project truthfully using the architecture 0.3 and API 0.1 contracts. Check every product statement against those sources; clearly distinguish planned capability from available documentation.
2. Deliver English and Turkish static pages with the existing Eylema identity. Check translation key parity, review meaning, validate generated files and record reviewed hashes.
3. Provide responsive navigation, language switching, architecture explanation and real source links. Exercise desktop/mobile, keyboard, reduced motion, JavaScript-disabled baseline and core interactions in a browser.
4. Use zero third-party website runtime packages, hosted fonts, analytics, account flows or model services. Inventory the browser HTML/CSS/JavaScript surface separately from the proposed first-party Rust platform.
5. Run applicable repository contribution commands, report unavailable foundation gates honestly, inspect the publication diff, and deliver a draft PR using the supplied template. No merge or deployment.

## Design and resources

Four coordinated concepts: introduction, architecture loop, source-linked FAQ, roadmap/contribution. Paper `#F7F6F2`, ink `#17252B`, orange `#EE5638`; Helvetica Neue/Arial system typography, large editorial headings, thin rules, open layouts and one generated sculpture. Reuse the existing logo without modifying its geometry.

Budget: 120 minutes implementation and verification, at most 5 Image Gen calls, at most 3 focused repair rounds per failing check. Stop and report an unresolved failure or missing required authority rather than weaken a check.

## Roles and risks

Architect, implementer, verifier and self-reviewer: this Codex session, GPT-6-family model (specific runtime model identifier not exposed). Tools actually used will be recorded with verification. No separate reviewer is claimed; independent review and maintainer review remain pending.

Main risks: accidentally promoting a design into a product claim; inheriting unrelated dirty work; linking documentation that is not yet on main; conflating website JavaScript with the planned Rust runtime. Mitigations: source-bound copy, isolated branch, explicit dependency/status inventory and live link checks. No account data, secret, model weight or training record is needed.
