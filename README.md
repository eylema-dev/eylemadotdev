# Eylema website

Public source repository [eylema-dev/eylemadotdev](https://github.com/eylema-dev/eylemadotdev) for the bilingual promotional website at the intended domain `eylema.dev`.

Public platform project: [eylema-dev/eylema](https://github.com/eylema-dev/eylema). This repository introduces the implemented local task foundation and the proposed cooperative-loop platform; it does not contain or run the Rust platform.

[Türkçe](README.tr.md)

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

Run the exact verification commands in [AGENTS.md](AGENTS.md). Generated documents are committed; CI rejects stale output. Translation hashes record a review checkpoint, not proof of semantic equivalence. Website checks do not establish core, GPU, model, training or full-product acceptance. The [current platform alignment](records/platform-alignment.md) cites a [pinned source snapshot](records/platform-source-snapshot.json); the [current v0.5 bilingual illustration](records/architecture-v05-visuals.md) separates the implemented task foundation from proposed integration. Its [built-in generation prompts](records/architecture-v05-prompts.json) and asset hashes are recorded.

## Publication boundary

The source repository is public, as explicitly requested by the maintainer. Published HTML, CSS, JavaScript and images will be publicly retrievable. The authorized production target is Azure Static Web Apps Free in `umayos subscription`, West Europe, `rg-eylema-dev / swa-eylema-dev`. The production workflow validates and uploads only `public/`, then checks live file hashes, MIME types, routing and the commit in `/release.json`. See the [release contract](records/deployment.md) and the launch checklist. Search Console/Bing verification, indexing and field performance are separate evidence. Local checks alone do not establish deployment.
