# Eyleme website

The product and website identity is **Eyleme**. The repository is **eyleme-dev/eylemedotdev**, and the prepared canonical domain is **eyleme.dev**. The maintainer closed eylema.dev and has now purchased eyleme.dev at GoDaddy. The [custom-domain launch](records/eyleme-domain.md) connects the existing Azure Free site to the new domain; DNS, Azure validation and normal HTTPS are separate acceptance gates. See the [website identity record](records/website-identity.md).

Public source repository [eyleme-dev/eylemedotdev](https://github.com/eyleme-dev/eylemedotdev) for the bilingual promotional website at the intended domain `eyleme.dev`.

Public open-source project: [eyleme-dev/eyleme](https://github.com/eyleme-dev/eyleme). **Eyleme** is both the shared brand and an independently usable community tool. First-party core code and documentation use Apache-2.0; third-party/model/data terms and website assets retain their own boundaries. **Eyleme Derleme** and **Eyleme Onama** are private-source, paid subscription products in development. Their public descriptions appear at [eyleme.dev/#products](https://eyleme.dev/#products), without private source links, invented prices or an active checkout. See the [single-brand product record](records/single-brand-family.md).

This repository introduces the implemented local task foundation and the proposed cooperative-loop platform; it does not contain or run the Rust platform. The commercial products are optional: Eyleme retains local permission checks and works without their subscriptions. The family presentation order is Derleme → Onama → Eyleme; policy enforcement also crosses stages.

The [ecosystem and subscription revision](records/ecosystem-positioning.md) makes the development status explicit: Eyleme aims to grow as an open-source community ecosystem; Derleme covers collecting physical-world field data and recording it in the cloud or on premises; Onama covers cybersecurity, authority, responsibility and regulatory compliance workflows. The [subscription section](https://eyleme.dev/#subscriptions) explains the specialist commercial focus without announcing prices, packages or service availability.

[Türkçe](README.tr.md)

Search policy: the maintainer explicitly authorized Google/Bing discovery of the new eyleme.dev domain on 15 October 2026. Canonical landing pages are indexable, the sitemap lists English and Turkish, and the genuine 404 remains noindex. Old eylema.dev removal tracking is separate. Engine verification/submission and actual indexing are distinct; see [search visibility](docs/en/discovery.md) and [WEB-020](records/search-launch.md).

IndexNow for eyleme.dev is explicitly enabled through the [bounded submission helper](records/eyleme-indexnow.md): default preview has no network access; --submit verifies ownership/pages before one batch. Protocol receipts and real engine indexing remain separate.

## Website

English is the default at `/`; Turkish is at `/tr/`. Both are complete HTML documents, with reciprocal hreflang and self-canonical URLs. The architecture tabs progressively enhance content that is already in the HTML. FAQ answers use native disclosure controls. No accounts, analytics, cookies, hosted fonts, model API or third-party runtime package.

Serve locally:

```sh
python3 -m venv .venv
.venv/bin/python tools/build.py
.venv/bin/python -m http.server 4187 --bind 127.0.0.1 --directory public
```

Open `http://127.0.0.1:4187/`. The static publishing directory is `public/`; Python is development/CI tooling only. Do not expose the repository root or development server as production hosting.

## Sources and checks

- [Contributor workflow](CONTRIBUTING.md), [quality gates](docs/en/quality-gates.md), [tooling and assets](docs/en/tooling.md).
- [SEO, generative discovery and launch](docs/en/discovery.md).
- [Task plan](records/plan.md), [design specification](records/design.md) and [verification](records/verification.md).
- `content/*.json`: reviewed bilingual copy; `tools/build.py`: deterministic HTML, JSON-LD, robots, sitemap and 404 generation; `public/assets/`: original CSS/JS and brand imagery.

Run the exact verification commands in [AGENTS.md](AGENTS.md). Generated documents are committed; CI rejects stale output. Translation hashes record a review checkpoint, not proof of semantic equivalence. Website checks do not establish core, GPU, model, training or full-product acceptance. The [current platform alignment](records/platform-v07-alignment.md) cites a [pinned source snapshot](records/platform-source-snapshot.json); the [v0.7 bilingual illustration](records/architecture-v07-visuals.md) now depicts the same harness, project knowledge/memory and planned native improvement, with scoped component acceptance kept separate. Its [built-in generation prompts](records/architecture-v07-prompts.json) and asset hashes are recorded.

## Publication boundary

The authorized release target is [eyleme.dev](https://eyleme.dev/). The deployment workflow verifies the exact release SHA, hashes, MIME, indexable responses, routing and real 404 on the canonical host. After both certificates are valid, www and the generated Azure host redirect to the root domain while preserving paths. See [WEB-018](records/eyleme-domain.md) for current acceptance evidence. Do not purchase a domain or restore indexing implicitly.

The source repository is public, as explicitly requested by the maintainer. Published HTML, CSS, JavaScript and images will be publicly retrievable. The authorized production target is Azure Static Web Apps Free in `umayos subscription`, West Europe, `rg-eylema-dev / swa-eylema-dev`. The production workflow validates and uploads only `public/`, then checks live file hashes, MIME types, routing and the commit in `/release.json`. See the [release contract](records/deployment.md) and the launch checklist. Search Console/Bing verification, indexing and field performance are separate evidence. Local checks alone do not establish deployment.

The [human-directed design](records/agentic-design.md) adds light/dark themes, model recipes and local-model direction, three human oversight roles, and a planned field-support journey. The Derleme/Onama team is being formed; field services are planned. A local browser preference remembers the chosen theme across both languages; no preference is sent to a server.
