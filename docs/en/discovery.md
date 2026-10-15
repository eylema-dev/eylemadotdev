# Search visibility and removal

[Türkçe](../tr/discovery.md). Reviewed 14 October 2026.

The maintainer requested removal of the existing `eylema.dev` site from Google and Bing results. The website remains a public site; search exclusion is not access control. The original 14 October removal change excluded domain migration, DNS changes, account/property deletion and verification-token removal. See the domain preparation decision below for the later host change.

Both English `/` and Turkish `/tr/` pages declare `noindex,follow`. Azure's global `X-Robots-Tag: noindex,follow` header covers HTML, images and other resources. The custom 404 remains noindex. Existing canonical/hreflang, social metadata, bilingual content and normal navigation remain available.

`robots.txt` explicitly allows crawling so search engines can fetch the removal directives. It does not advertise a sitemap. The existing `/sitemap.xml` remains valid XML with an empty URL set, avoiding further URL promotion. Blocking crawlers would prevent them from observing noindex. [Google noindex guidance](https://developers.google.com/search/docs/crawling-indexing/block-indexing), [Azure response headers](https://learn.microsoft.com/en-us/azure/static-web-apps/configuration).

## Submission and ownership

IndexNow submission is disabled before any network request. `tools/indexnow.py` prints only an explicitly non-submitting preview; `--submit` exits nonzero with the search-removal policy reason. Public ownership-key bytes and previous submission receipts are preserved as historical evidence. Do not submit URLs or sitemaps to promote indexing while this policy applies.

## Acceptance and tracking

1. Verify generated noindex meta, global headers, crawl-permitted robots, empty sitemap and refusal to submit. Negative tests reject indexable/duplicate/bot-specific directives, header overrides, crawl blocks and renewed URL promotion.
2. Deploy only `public/` using the existing authorized Azure resource. Verify normal HTTPS, exact release commit, full resource hashes/MIME, global noindex headers, routing and true 404. Local `http.server` does not implement Azure headers; a source check is not header-deployment evidence.
3. Preserve Google Search Console and Bing Webmaster properties and inspection access. The separate authorized owner-panel removal requests are temporary actions whose actual scope/status must be read back. [Google removal tool](https://support.google.com/webmasters/answer/9689846?hl=en), [Bing URL blocking](https://www.bing.com/webmasters/help/?topicid=264e560a).
4. Record three distinct states: deployed persistent noindex, temporary removal-request status and observed search-engine indexing status. Neither an uploaded artifact nor an accepted removal request proves final removal. Search engines process these changes asynchronously.

Canonical DNS currently returns NXDOMAIN in the 14 October 2026 verification. Azure upload can succeed while normal canonical verification fails. That historical run deferred the domain decision. The maintainer subsequently closed the old domain; the new identity remains unpublished as explained below. Crawlers cannot observe the directives until the host resolves. See the [current removal record](../../records/search-removal.md). A future direct maintainer decision is required to restore indexing or resume submissions.

## Domain preparation — 15 October 2026

The maintainer has now selected eyleme.dev and closed eylema.dev. The new domain is not purchased. The [identity migration](../../records/website-identity.md) prepares canonical, reciprocal-language and social metadata for the new host, without publishing or changing DNS. This supersedes the deferred-domain statement above. Keep noindex, the empty sitemap and disabled submissions until an explicit indexing decision. The old domain removal reports remain separate historical and monitoring evidence. New-domain owner-panel verification and live-host evidence have not been established.

## Registered domain launch — 15 October 2026

The maintainer has now purchased eyleme.dev at GoDaddy and explicitly authorized connecting the existing Azure site. This supersedes the unpurchased-domain preparation note. The [domain launch record](../../records/eyleme-domain.md) separates DNS ownership/routing, certificates, redirects, deployed release identity and browser evidence. The existing noindex/empty-sitemap/disabled-submission policy remains in force; buying or connecting the new host does not authorize renewed search submissions. Old-domain removal monitoring stays separate.
