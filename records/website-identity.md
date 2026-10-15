# Website identity migration

Task WEB-017, revision 0.1.0, 15 October 2026. Base main: `81410a45c4cdd0ad8176e775f284e488fa11dc1d`. Branch: `codex/eyleme-website-identity`.

Authority: the maintainer directly requested renaming the promotional repository to eylemedotdev and aligning all content and images with Eyleme, then selected eyleme.dev. The maintainer confirms that eylema.dev is closed and eyleme.dev has not been purchased. Prepare the new identity; no domain purchase, DNS mutation or deployment is performed. Retain the existing search-exclusion policy and historical evidence.

Repository rename: GitHub returned repository ID 1414388661 at eyleme-dev/eylemedotdev, public, default main; the ID matches the original repository. The local origin now uses the new URL.

Allowed paths: active README/docs, build/release and regression fixtures, deployment canonical URL, public generated pages and image filenames/content, asset provenance and this bilingual record. Historical receipts, prompts, source snapshots and prior plans remain evidence of their original revisions. Azure resource and secret identifiers remain unchanged.

Acceptance: active links/canonical/hreflang/social/JSON-LD text use eyleme.dev and the renamed repository; EN/TR artwork reads Eyleme and eyleme.dev; no old product name appears in active HTML or asset URLs; English remains default; noindex, empty sitemap and disabled IndexNow remain. Verify exact local contract commands, deterministic build, translation meaning/fingerprints, raster integrity and desktop/mobile EN/TR browser behavior. Deliver a draft PR. Public DNS/TLS/deployment are not_run: new domain is unpurchased.

Budgets: one scoped branch/PR, two image edits plus at most one targeted repair per image, two local repair cycles, one browser session with four locale/viewport checks. Risks: generated text drift, stale image paths, premature canonical-host deployment. Inspect image text and reference links; do not merge/deploy before the new domain can satisfy release gates.

Roles: Codex is architect, implementer, verifier and self-reviewer, using GitHub CLI, Python standard-library tooling, built-in Image Gen and browser automation. Independent review is pending; no separate reviewer is claimed. Website validation is not Rust/GPU/model/training evidence.

## Verification checkpoint

Passed on this PR head (CI records exact SHAs), macOS arm64, Python 3.15.0: exact venv/hash-locked setup, 43 unit tests, deterministic generated output, repository gate, blank-template and whitespace checks. EN/TR meaning was reviewed before refreshing fingerprints. Two built-in Image Gen edits changed only the intended footer domain; full-size PNGs were visually reviewed against the input for labels, arrows, permission boundaries and acceptance caveats. Both 1672 x 941 WebP decodes exactly match their PNG pixels; current inventory hashes and bytes were refreshed. [Exact prompts](website-identity-prompts.json).

Browser plugin not available; documented CUA Playwright in the Codex in-app browser tested local 127.0.0.1 ports 4196 and 4197 at 1280 x 800 and 390 x 844. English default and both language transitions, page identity/nonblank/no error overlay, Eyleme logos, canonical new-domain metadata, decoded images, no horizontal overflow, arrow-key architecture selection and native FAQ expansion passed. Console warnings/errors: none for the successful site session. The initial connection-refused preview was opened before the server started, then recovered; an old in-memory Turkish poster was checked again at the fresh local origin and showed eyleme.dev. These are local checks, not canonical-host evidence. JavaScript-disabled/reduced-motion overrides: not_run in this turn; existing structural tests still verify initial HTML answers. Browser screenshots are kept outside the public repository.

The repository About description is now Eyleme with the prepared eyleme.dev host; homepage remains unset until publication. Self-review inspected the scoped diff, current public HTML/asset names, provenance, search policy, and public-path/secret checks. Independent review is pending. CI is pending at this checkpoint. Merge, deployment, purchase, DNS, Azure changes and indexing submissions: not_run; the new domain is not purchased. Historical reports and search monitors are unchanged.
