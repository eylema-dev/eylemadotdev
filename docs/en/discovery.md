# International search and generative discovery

[Türkçe](../tr/discovery.md). Reviewed 13 October 2026.

English is the default, geographically unrestricted language at `/`; Turkish is at `/tr/`. Each page is self-canonical and lists both languages plus English `x-default`. There is no automatic browser-language or country redirect. Full copy, sources and FAQ answers are in the first HTML response. `robots.txt` permits crawling and points to the two-page sitemap. Open Graph and social cards share a real brand asset.

JSON-LD describes Eylema as an Organization/project, WebSite and WebPage with source citations. It makes no incorporation, shipped SoftwareApplication, price, rating, performance or customer claim. No hidden content, keyword stuffing or fabricated endorsements. Visible copy and metadata distinguish the implemented local task foundation from proposed cooperative-loop/model/training integrations. The current v0.5 illustration carries a visible proposed-integration scope notice and descriptive alternatives in both languages; it does not establish runtime/model or performance acceptance.

Google's current guidance applies established SEO fundamentals to generative search. It explicitly says special AI markup and `llms.txt` are not required for Google Search and do not improve Google rankings. We therefore prioritize original project facts, source links, clear language, crawlability and usable pages. No special AI file or FAQ rich-result promise is needed. [Google generative AI guidance](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide), [localized pages](https://developers.google.com/search/docs/specialty/international/localized-versions), [organization data](https://developers.google.com/search/docs/appearance/structured-data/organization).

## Launch acceptance

1. After hosting authorization, deploy **only `public/`**. The GitHub source is public by maintainer request; only the website output belongs on the web host. Configure HTTPS for `eylema.dev`; redirect alternate hosts and HTTP to the chosen canonical HTTPS origin.
2. Serve `/` and `/tr/` with HTTP 200, assets with correct MIME types, missing routes with real HTTP 404 and `404.html`. Avoid a blanket single-page-app fallback. Redirect duplicate `/index.html` forms to their directory URLs at the host.
3. Use revalidation for HTML, CSS/JS, sitemap and robots. Asset names are not content-hashed, so do not cache them as immutable. Compression, TLS, security headers and CDN behavior are host configuration, unverified locally.
4. Check the exact deployed revision, both languages, canonical/hreflang, JSON-LD, robots/sitemap, error route and responsive browser behavior against the local artifact. Measure Lighthouse/PageSpeed and later field Core Web Vitals; local size budgets are not field results.
5. With account/domain authority, verify Google Search Console and Bing Webmaster Tools, submit the sitemap, inspect both URLs and review generative-search inclusion controls available in Search Console. Do not invent verification tokens or report a URL indexed just because it was submitted.

## IndexNow notifications

`PAGE_MODIFIED` in `tools/build.py` records the actual modification date of each language page. It supplies sitemap `lastmod` and WebPage `dateModified`, independently of the visible design-review date. Update only the entry for a page that really changes; never use the current build/deployment time. After verifying the live release, send the change notification below once. [Bing freshness guidance](https://blogs.bing.com/webmaster/2025/7/Keeping-Content-Discoverable-with-Sitemaps-in-AI-Powered-Search/).

The builder generates a root UTF-8 ownership file from `INDEXNOW_KEY` in `tools/build.py`. This key is public verification data, not an account credential. Generated-output checks reject missing or changed content; the release manifest and live checker include its hash and `text/plain` MIME type.

After publishing a change to either page, preview the fixed two-page payload, then submit once:

```sh
.venv/bin/python tools/indexnow.py
.venv/bin/python tools/indexnow.py --submit
```

The submission command first checks the live key bytes and both canonical HTTP 200 routes, then sends one JSON POST to `https://api.indexnow.org/indexnow`. It stops on validation or HTTP errors and does not retry automatically. HTTP 200 confirms receipt; 202 means receipt with key validation pending. Neither establishes crawling, indexing or rankings. Keep the key file published while using it. [IndexNow protocol](https://www.indexnow.org/documentation).

This notification reaches participating search engines; it does not replace Search Console or the sitemap. Google and Bing indexing status must still be checked in their own webmaster tools. Submit for actual page changes, not periodically to force indexing.

## Building international recognition

Publish useful, evidence-bearing English updates with Turkish companions: explain one architecture decision, walk through the first actual application when it runs, publish reproducible benchmarks when measured, and document accepted changes with their limits. Give each substantial future article a durable URL, author/project attribution, real update date and links to evidence. Do not mass-generate thin language or keyword pages.

Track a baseline after indexing: branded and non-branded impressions/clicks, geography/language, indexed pages, referring publications, referral traffic and qualified GitHub contributions. Use the available Search Console search/generative reports; record report scope and date. Growth requires continued original work and distribution, not only tags. Outreach, social posting, analytics installation and recurring monitoring are separate authorized work. Rankings, citations and worldwide recognition are outcomes to measure, not guarantees.
