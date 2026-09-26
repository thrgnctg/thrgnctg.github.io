# ShiftLife public site

Static, bilingual GitHub Pages site for ShiftLife. The Turkish pages use `/`, `/privacy/`, `/support/`, and `/terms/`; English versions use `/en/` and matching paths. The app's legal links use the Turkish root URLs, with an English switch visible on every page.

## Publishing

The public origin is `https://lifedevlabs.com`. GitHub Pages publishes `main` from the repository root with `lifedevlabs.com` as its custom domain. The apex points to GitHub Pages using the four official A records; `www` is a CNAME to `thrgnctg.github.io`. GitHub Pages redirects the default `thrgnctg.github.io` host and `www` to the apex while preserving page paths. Keep the GitHub Pages domain-verification TXT record in DNS, and enforce HTTPS after GitHub provisions its certificate. Verify the live pages and the `lifedevlabs.com` Search Console Domain Property before submitting Google OAuth branding.

## Updating

Edit `build_site.py`, then run `python3 build_site.py`. This regenerates the eight HTML pages and `sitemap.xml`. The site uses no JavaScript, cookies, analytics, external fonts, or third-party runtime dependencies. Its bundled Figtree font files are licensed under the SIL Open Font License in `fonts/LICENSE.txt`.

The policy is prepared for the September 27, 2026 calendar scope update: shifts and optional handovers for 90 days, plus other timed plan blocks for 30 days. Publish this site update alongside the matching iOS build and App Privacy revision. Review the policy whenever app data practices change. Automatic iCloud sync is **not** active in this release.
