# International search and generative discovery

[Türkçe](../tr/discovery.md). Reviewed 11 October 2026.

English is the default, geographically unrestricted language at `/`; Turkish is at `/tr/`. Each page is self-canonical and lists both languages plus English `x-default`. There is no automatic browser-language or country redirect. Full copy, sources and FAQ answers are in the first HTML response. `robots.txt` permits crawling and points to the two-page sitemap. Open Graph and social cards share a real brand asset.

JSON-LD describes Eylema as an Organization/project, WebSite and WebPage with source citations. It makes no incorporation, shipped SoftwareApplication, price, rating, performance or customer claim. No hidden content, keyword stuffing or fabricated endorsements. Visible design-stage language stays aligned with metadata.

Google's current guidance applies established SEO fundamentals to generative search. It explicitly says special AI markup and `llms.txt` are not required for Google Search and do not improve Google rankings. We therefore prioritize original project facts, source links, clear language, crawlability and usable pages. No special AI file or FAQ rich-result promise is needed. [Google generative AI guidance](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide), [localized pages](https://developers.google.com/search/docs/specialty/international/localized-versions), [organization data](https://developers.google.com/search/docs/appearance/structured-data/organization).

## Launch acceptance

1. After hosting authorization, deploy **only `public/`**. The GitHub source is public by maintainer request; only the website output belongs on the web host. Configure HTTPS for `eylema.dev`; redirect alternate hosts and HTTP to the chosen canonical HTTPS origin.
2. Serve `/` and `/tr/` with HTTP 200, assets with correct MIME types, missing routes with real HTTP 404 and `404.html`. Avoid a blanket single-page-app fallback. Redirect duplicate `/index.html` forms to their directory URLs at the host.
3. Use revalidation for HTML, CSS/JS, sitemap and robots. Asset names are not content-hashed, so do not cache them as immutable. Compression, TLS, security headers and CDN behavior are host configuration, unverified locally.
4. Check the exact deployed revision, both languages, canonical/hreflang, JSON-LD, robots/sitemap, error route and responsive browser behavior against the local artifact. Measure Lighthouse/PageSpeed and later field Core Web Vitals; local size budgets are not field results.
5. With account/domain authority, verify Google Search Console and Bing Webmaster Tools, submit the sitemap, inspect both URLs and review generative-search inclusion controls available in Search Console. Do not invent verification tokens or report a URL indexed just because it was submitted.

## Building international recognition

Publish useful, evidence-bearing English updates with Turkish companions: explain one architecture decision, walk through the first actual application when it runs, publish reproducible benchmarks when measured, and document accepted changes with their limits. Give each substantial future article a durable URL, author/project attribution, real update date and links to evidence. Do not mass-generate thin language or keyword pages.

Track a baseline after indexing: branded and non-branded impressions/clicks, geography/language, indexed pages, referring publications, referral traffic and qualified GitHub contributions. Use the available Search Console search/generative reports; record report scope and date. Growth requires continued original work and distribution, not only tags. Outreach, social posting, analytics installation and recurring monitoring are separate authorized work. Rankings, citations and worldwide recognition are outcomes to measure, not guarantees.
