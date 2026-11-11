# Aurora Plumbing Guide — Launch Readiness & Cutover Runbook

## What Is Already Completed & Launch-Ready

1. **Source Build & Guard Updates (`aurora_preview_source_v5/src/build.py`)**
   - `guard()` updated to support both `noindex=true` (staging/review) and `noindex=false` (production launch) modes.
   - `auroracoplumbers.com` allowed as production canonical host; legacy unused candidate domains and retired phone numbers (`857-201-2772`, `708-350-9399`, `857-201-0860`) remain strictly blocked.
   - Dynamic `<meta name="robots">`, `.preview-banner` omission, production header/footer copy, and `robots.txt` `Sitemap:` line implemented.
   - Dynamic phone CTA renderer (`phone_cta_html`) and CSS styles (`.btn-call`, `.call-panel`) built in `site.css`.
   - `src/pages_site.py` updated for production Contact, How It Works, About, Privacy, Terms, and 404 pages.
   - `tests/test_preview.py` updated to validate both preview and production launch builds.

2. **Checklist Defect Fixed (`js/quote.js`)**
   - Broken links `/draft/research-notes/` and `/service-area/` replaced with `/guides/` and `/areas/`.

3. **Hosting, Redirects & SSL (`vercel.json`)**
   - Vercel Project Domains currently sets `https://www.auroracoplumbers.com` as primary and redirects `auroracoplumbers.com` to `www` (managed in Vercel Dashboard -> Domains; do not duplicate conflicting host redirects in `vercel.json`).
   - Trailing slash and clean URLs enabled; all 9 legacy URL redirects configured (`/sewer-line-repair/`, `/drain-cleaning/`, `/hydro-jetting/`, `/sewer-camera-inspection/`, `/water-heater-replacement/`, `/water-heater-repair/`, `/service-area/`, `/quote-readiness/`, `/draft/research-notes/`).
   - Security headers (`Strict-Transport-Security`, `X-Content-Type-Options`, `Referrer-Policy`) active.
   - HTTP 404 status with custom `/404.html` verified.
   - Staging safety lock: `X-Robots-Tag: noindex, follow` and Vercel Authentication remain active until sign-off.

4. **Media & Links Verified**
   - 112 HTML pages (111 content + `404.html`), 0 broken links across 2,647 link checks, 100% authentic plumbing photography with 0 per-page image repetitions.

---

## Final Cutover Steps (After Saravanan's Written Sign-Off)

1. **Update `aurora_preview_source_v5/config/site.json`** using `config/site.production.template.json`:
   - Set `"noindex": false`
   - Set `"canonicalHost": "https://auroracoplumbers.com"` and `"productionHost": "https://auroracoplumbers.com"`
   - Set `"allowNonLocalCanonical": true`, `"referralMarketConfirmed": true`, `"marketStatus": "confirmed"`
   - Fill in the approved phone number in `"referralPhone"` (`"live": true`, `"e164"`, `"display"`) and `"callsEnabled": true`
   - Rebuild & test (`python3 src/build.py` && `python3 -m unittest tests.test_preview`) and sync `aurora_preview_dist_v5/`.

2. **Update `vercel.json` & Domain DNS**:
   - Remove the `"X-Robots-Tag": "noindex, follow"` header from `vercel.json`.
   - Attach `auroracoplumbers.com` and `www.auroracoplumbers.com` in Vercel Dashboard -> Project Domains (automatic Let's Encrypt SSL).
   - Disable Vercel Deployment Protection / password gate for public access.

3. **Post-Launch**:
   - Verify `https://auroracoplumbers.com/robots.txt`, `https://auroracoplumbers.com/sitemap.xml`, `tel:` CTA link, and `www` -> apex redirect.
   - Submit `https://auroracoplumbers.com/sitemap.xml` to Google Search Console after approval.
