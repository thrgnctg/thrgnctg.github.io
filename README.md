# ShiftLife public site

Static, bilingual GitHub Pages site for ShiftLife. The Turkish pages use `/`, `/privacy/`, `/support/`, and `/terms/`; English versions use `/en/` and matching paths. The app's legal links use the Turkish root URLs, with an English switch visible on every page.

## Publishing

Create the public repository `thrgnctg/thrgnctg.github.io`, push `main`, and enable GitHub Pages from the root of `main`. The intended public origin is `https://thrgnctg.github.io`. Verify the live HTTPS pages and add this host to Google Search Console before submitting Google OAuth branding. Google's verified-domain review may require a domain registered to the developer; if so, point a purchased domain at these same files and update `BASE`, `robots.txt`, and App Store/app links.

## Updating

Edit `build_site.py`, then run `python3 build_site.py`. This regenerates the eight HTML pages and `sitemap.xml`. The site uses no JavaScript, cookies, analytics, external fonts, or third-party runtime dependencies. Its bundled Figtree font files are licensed under the SIL Open Font License in `fonts/LICENSE.txt`.

The policy describes the current iOS implementation as of September 26, 2026. Review it whenever app data practices change. In particular, automatic iCloud sync is **not** active in this release.
