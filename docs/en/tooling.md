# Website tools and asset provenance

[Türkçe](../tr/tooling.md).

| Boundary | Inventory |
|---|---|
| Published runtime | Browser HTML, CSS, 1.7 KB first-party JavaScript; no package downloads, remote fonts, analytics or inference engine |
| Build and CI | Python 3.14 standard library; empty dependency lock is intentional; development only |
| CI actions | checkout v7.0.1 at `3d3c42e5aac5ba805825da76410c181273ba90b1`; setup-python v7.0.0 at `5fda3b95a4ea91299a34e894583c3862153e4b97`; official tag SHAs checked on 11 October 2026; Azure/static-web-apps-deploy v1 at `4d27395796ac319302594769cfe812bd207490b1` verified from its official repository for the production workflow |
| Local visual authoring | Codex, built-in Image Gen; four section concepts plus one standalone asset; no website API key |
| Asset encoding | Bundled sharp 0.35.5, development only; 1024px and 640px WebP, quality 88; not required to serve/build HTML |
| Browser verification | Codex in-app browser through CUA; supplemental bundled Playwright Chromium 151.0.7922.34 for JavaScript-disabled and reduced-motion overrides unavailable in IAB; development only |
| Host platform | Browser/OS image rendering and system Helvetica Neue/Helvetica/Arial; not a claim of a Rust-only stack |

`public/assets/eylema.svg`, `favicon.svg`, `apple-touch-icon.png` and `social.png` are unchanged copies of the maintainer's Eylema brand pack present in the source workspace on 11 October 2026. The pack's editable vector sources remain in the platform workspace. No third-party font binary or stock art is redistributed. Asset hashes are in [asset-provenance.json](../../records/asset-provenance.json).

The ribbon is original generated illustrative art. Its prompt and intended use are in the [design record](../../records/design.md). The selected standalone image was encoded as `eylema-loop-1024.webp` (47,100 bytes) and `eylema-loop-640.webp` (20,088 bytes). It is a visual metaphor, not an implemented GPU scene or product screenshot.

The [technology visual update](../../records/technology-visual.md) adds the maintainer-approved English poster and its Turkish counterpart, both 1672 × 941. Original PNGs are offered at full size; lossless WebP copies supply in-page previews. Built-in Image Gen matched the Turkish heading to the approved English EylemA mark and extracted a transparent wordmark from the same reference. Sharp 0.35.5 resized the wordmark to 960 × 320 while retaining alpha. The orange E icon is the initial E, followed by `ylemA`. The new header/footer image does not load an extra font or browser package. Original brand-pack assets remain available.

The PR description checker and template were copied from the maintainer's pending Eylema contribution foundation; they remain first-party repository tooling. This site does not choose a distribution license for the platform or grant a trademark license.

The [v0.5 illustration replacement](../../records/architecture-v05-visuals.md) uses three built-in Image Gen calls: English redesign, a targeted arrow repair and Turkish localization. Both new sources are 1672 × 941 PNG, with lossless WebP previews encoded by the same bundled sharp 0.35.5. Existing image URLs are replaced by explicit maintainer request; the header wordmark, hero and other brand assets remain unchanged. The [prompt set](../../records/architecture-v05-prompts.json) records exact copy and arrow constraints. Proposed integration and the separate implemented task foundation are visible in-image and in HTML.
