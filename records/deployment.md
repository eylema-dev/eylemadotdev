# Azure website release

12 October 2026 follow-up: the generated Azure hostname now responds with HTTP 301 to the canonical eylema.dev host, including asset paths. The production workflow verifies the canonical host directly, preserving the strict commit, file inventory, hash, MIME, no-asset-redirect and true-404 checks. It allows at most three complete verification attempts with ten-second gaps for release propagation, and still fails if none passes. No DNS, Azure resource or permission change is part of this correction.

[Türkçe](deployment.tr.md). Task `WEB-002 / 0.1.0`, 11 October 2026.

Authority: the maintainer explicitly requested merging PR #1 and publishing `eylema.dev` using `umayos subscription`, `rg-eylema-dev`, `swa-eylema-dev`, Free SKU. This overrides the generic portfolio skill's naming/subscription/no-custom-domain defaults. GoDaddy is the stated domain provider. No paid tier, DNS-provider migration or unrelated resource change is authorized.

Base: `1dc595e166e3a84b687d42370a84a8a55b78d0d5`, main after the authorized PR #1 squash merge. Branch: `codex/azure-eylema-release`. Allowed paths: deployment workflow, public host configuration, release/live-check tooling and regression tests, bilingual deployment/contribution docs and translation hashes. Preserve the website design and all unrelated platform work.

Target: `eylema-dev/eylemadotdev`, main, West Europe, Free, `rg-eylema-dev / swa-eylema-dev`. The live subscription is Enabled and contained two Free apps before this release. Artifact: `public/`; workflow: `.github/workflows/deploy-swa-eylema-dev.yml`; secret: `AZURE_STATIC_WEB_APPS_API_TOKEN_SWA_EYLEMA_DEV`; concurrency group: `production-swa-eylema-dev`. Only this scoped deployment token is transferred directly from Azure to GitHub without printing or storing it.

Acceptance: exact local AGENTS commands and negative release/config tests; one production workflow with validation, prebuilt upload and live HTTP verification; matching Git/Actions/release SHA; Azure Free/Ready; generated-host and eylema.dev HTTPS, source hashes/MIME, real 404, canonical locale routes, desktop/mobile browser and logo checks. DNS saves, public propagation and certificate readiness are separate evidence. Search indexing and field Core Web Vitals remain unmeasured.

Risks: duplicate deploy workflows, wrong subscription, stale release, accidental SPA fallback, broken static assets, apex DNS limitations or propagation. Use explicit subscription IDs, no source-generated workflow, serialized deployment, trailingSlash auto, true 404 and release file hashes. Preserve unrelated DNS/mail records and inspect routing records before editing.

Budget: 90 minutes implementation and verification, at most three targeted repairs per failing check, bounded propagation polling with meaningful progress updates. Architect, implementer, verifier and self-reviewer: the same Codex GPT-6-family session; independent review is not fabricated. Publication/merge is explicitly authorized by the maintainer. Tools: Git/GitHub CLI, Azure CLI, Python standard library, CUA browser/native Chrome and official Microsoft/Azure documentation.

Apex-domain setup follows [Microsoft's external apex guide](https://learn.microsoft.com/en-us/azure/static-web-apps/apex-domain-external). Prefer ALIAS/ANAME/flattening where supported; if GoDaddy exposes only an A record, use the exact app's stableInboundIP and record the regional-routing limit. A standard CNAME is not placed at the zone apex. Hosting configuration follows [Azure configuration](https://learn.microsoft.com/en-us/azure/static-web-apps/configuration).

## Pending identity migration — 15 October 2026

Current repository: [eyleme-dev/eylemedotdev](https://github.com/eyleme-dev/eylemedotdev). The prepared canonical verification host is now eyleme.dev; it is not purchased. The previous eylema.dev host is closed per the maintainer. Do not merge/deploy this identity migration before the new canonical host can pass the existing strict release gates. No deployment, domain purchase, DNS, Azure resource or secret changes are included. Historical release evidence above applies only to its recorded host/revision. See [WEB-017](website-identity.md).

## Eyleme domain launch — 15 October 2026

The latest maintainer request authorizes connecting the purchased eyleme.dev domain to the existing Free Azure site and completing the scoped launch PR/merge/deployment. The production checker now targets https://eyleme.dev with the same exact-SHA, inventory/hash/MIME/noindex, true404 and locale-normalization gates. Enable the root default only after root and www certificates pass normal validation. New Azure/www redirects preserve paths; the generated preview URL then reaches the canonical domain. No paid service, mail/nameserver change or search submission is part of this launch. See [WEB-018](eyleme-domain.md) for actual observations. Older notes above describe their own historical hosts and authority.
