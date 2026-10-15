# Website quality gates

[Türkçe](../tr/quality-gates.md).

The website is separate from the platform documentation repository. Its standard-library validator checks the website boundary rather than inheriting application-schema or Rust-runtime tests. The platform's gates are not changed by this repository.

| Gate | Evidence and limits |
|---|---|
| Generated output | HTML, sitemap, robots and 404 match the builder and bilingual content |
| Discovery | One H1/main, language, self-canonical, reciprocal hreflang/x-default, descriptions, single index,follow policy, JSON-LD consistency, local assets/anchors, crawl-permitted robots and exact bilingual sitemap, visible current-foundation scope and architecture-illustration scope notice |
| Translation | Key/array shape and step identifiers agree; reviewed SHA-256 fingerprints are current; semantic review remains separate |
| Regression tests | Missing translations/assets, identifier drift, wrong canonical/hreflang, renewed noindex or conflicting directives, duplicate IDs, structured claim drift, stale hashes and HTML/script injection are rejected |
| Static budget | CSS/JS total under 35 KB raw; this is a size budget, not a Core Web Vitals measurement |
| PR description | Required sections contain specific values; truth and authority require review |
| Browser | Real navigation, languages, tabs/keyboard, disclosures, mobile layout, console and visual comparison are checked separately |
| Release | Reject short/wrong commit, missing artifact, symlinks and changed live inventory; host config rejects SPA fallback, soft 404, asset redirects and global/route indexing overrides; live checks reject blocking headers on resources and normalized landing pages; production workflow uses the scoped secret only after validation |
| CI | Read-only PR workflow, pinned actions, no secrets or deployment in PR checks; actual PR head and checked-out SHA printed |

Run the commands in [AGENTS.md](../../AGENTS.md) and `python tools/build.py --check` using the virtual environment. `--allow-template` only checks the blank PR form. A green CI run is not independent or maintainer review. Branch protection has not been configured by this repository.

Hosting, HTTPS/redirects, actual HTTP 404, search-engine indexing, field performance, model/GPU/Rust execution and international reach require separate evidence. Missing hardware evidence must never be inferred from website checks.

IndexNow defaults to a zero-network preview; explicit submission must pass host/key/page preflight, send one POST without redirects/retries and retain the actual200/202/error receipt. New-domain indexable deployment, owner-panel submission acceptance and observed indexing status are separate evidence. Old-domain removal evidence remains historical. Canonical DNS failure remains a failed live gate. See [search visibility](discovery.md).
