# Search discovery

[Türkçe](../tr/discovery.md). Reviewed 15 October 2026.

The maintainer explicitly requested adding https://eyleme.dev/ to Google Search Console and Bing Webmaster Tools, submitting its sitemap and requesting indexing of English and Turkish. This supersedes the inherited new-domain exclusion policy; it does not cancel or change old eylema.dev removal reports or monitors. See [WEB-020](../../records/search-launch.md) and the historical [removal record](../../records/search-removal.md).

## Crawlable canonical pages

English https://eyleme.dev/ and Turkish https://eyleme.dev/tr/ declare index,follow, self-canonical URLs and reciprocal en/tr/x-default links. Azure has no global X-Robots-Tag exclusion and no route-specific bot override. The genuine HTTP404 document retains noindex. robots.txt allows crawling and advertises https://eyleme.dev/sitemap.xml. The XML sitemap contains exactly the two canonical pages and their actual modification dates; builds do not invent fresh dates. www and the generated Azure host redirect to the canonical root while preserving paths. [Google sitemap guidance](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap), [Google noindex guidance](https://developers.google.com/search/docs/crawling-indexing/block-indexing).

## Ownership and submission

Use the signed-in owner sessions to add the new property, verify only the engine-issued public proof and submit the sitemap. Google Domain verification may require a new GoDaddy TXT record; preserve existing Azure, mail and DNS records. Bing can use its offered verification methods without granting new broad account permissions. Submit each canonical URL once per engine; repeated submissions do not guarantee faster processing. IndexNow stays disabled; this launch uses the explicitly requested owner-panel submissions. Historical ownership bytes/receipts remain unchanged. [Bing verification](https://www2.bing.com/webmasters/help/add-and-verify-site-12184f8b), [Bing sitemaps](https://www2.bing.com/webmasters/help/sitemaps-3b5cf6ed), [Bing URL submission](https://www.bing.com/webmasters/help/URL-Submission-62f2860b).

## Evidence boundary

Source/live gates reject noindex landing pages, blocking or conflicting response headers, crawler blocks, missing/duplicate/foreign sitemap URLs and stale dates. Exact release identity, file inventory/hashes/MIME, security headers, real404 and locale routing remain mandatory.

Read back property ownership, sitemap processing and URL request acceptance from the actual panels. Only Google Index / Bing Index URL Inspection explicitly showing indexed proves indexing; a live test, sitemap discovery or accepted request does not. Engines choose whether and when to index. Record current states honestly; user-required login/CAPTCHA or inaccessible panels are access blockers, not evidence of non-indexing. Automated follow-up needs an explicitly requested monitor; do not silently change old-domain monitors.
