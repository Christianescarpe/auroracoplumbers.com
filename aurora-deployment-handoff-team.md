# Aurora Plumbing Guide: deployment handoff

Date: November 7, 2026. Domain: auroracoplumbers.com. Nothing has been deployed or purchased yet.

This guide covers the files that were actually built: a 111-page static site (37 service pages, 48 community pages, 15 guides, plus utility pages), covering all 44 Arroyo plumbing categories. Phone only, no forms. It is not a keyword-volume study.

## Who does what

- **Gowrish:** buy auroracoplumbers.com now under our account, after checking current availability and price. Confirm by reply once it is bought.
- **Christian:** upload the review copy (dist contents) to the host, password-protected if possible, and reply with the preview URL. Then prepare the launch changes below in the source.
- **Public indexable launch** (removing noindex, connecting a phone number, Search Console) waits on Saravanan's written sign-off on call routing, coverage, and payout. That approval gates the public launch only, not the domain purchase.

Note: `config/launch-private.json` in the source contains older planning metadata, including `doNotPurchaseDomain: true` and a "not purchased" status. That metadata predates the current instruction to buy the domain. This guide supersedes it. It does not change the requirement for approval before public launch.

## Files

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| `aurora_preview_dist_v5.zip` | 341950 | `e4f82e0a30f8e59adac382832eaaf4a8cb4717b09587029f7ea8844345c65ac6` |
| `aurora_preview_source_v5.zip` | 417051 | `4923fabff6745aa6910f389bc83e8aa64d4fa222924f793f5ba2e9edf259d5d0` |

`aurora_preview_dist_v5.zip` is the review upload. Unzip it; the zip root is the web root. It contains 112 HTML files (111 pages as `index.html` inside directories, plus `404.html` at the root), `robots.txt`, `sitemap.xml`, `css/site.css`, `js/site.js`, `js/quote.js`, `img/lateral.svg`, and `favicon.svg`. It has no server program, `_redirects`, `vercel.json`, `netlify.toml`, or `.htaccess`.

`aurora_preview_source_v5.zip` is the rebuild source, for the team only. Keep it private and never upload it to a web root. Only the dist contents go on the server. It includes `config/launch-private.json` (internal gates and notes). Keep that file off the server and out of public pages.

## Review copy vs. public launch

**Review upload (do now).** Upload the built dist files unchanged. Every page already says `noindex`. The canonical host in every page and in `sitemap.xml` is `http://127.0.0.1:43217`, and a yellow banner marks the site as an unpublished preview. This applies on any review host too: the localhost canonical and banner will show there. That is fine for review but not for the public site. Password-protect the directory if the host allows it.

**Public indexable launch (after written approval).** Do not remove noindex, connect a phone, or submit to Search Console until Saravanan approves the live call route, the coverage it accepts, and the economics. Do not activate any old phone numbers.

## Domain host setup

The source does not choose `www` vs. the bare domain. It has no SSL certificate, HSTS setting, or host redirect. For launch, pick one HTTPS origin and redirect the other three (http/https, with/without `www`) to it. The canonical tag and the sitemap must use that same origin.

## What actually controls each switch

Current `config/site.json`:

| Key | Current value | What the code does with it |
| --- | --- | --- |
| `noindex` | `true` | `src/build.py` function `guard` refuses to build if this is not `true`. The HTML robots tags are not read from this key. They are fixed strings. |
| `canonicalHost` | `http://127.0.0.1:43217` | `render` sets `<link rel="canonical">` to this host plus the page path. `write_sitemap` writes the same host into every `<loc>`. The footer prints this host. |
| `allowNonLocalCanonical` | `false` | If `false`, `guard` allows only `http://127.0.0.1:` or `http://localhost:`. |
| `productionHost` | `null` | `guard` refuses the build if this is not null or empty. No renderer reads it. Setting it does not change the canonical. |
| `referralMarketConfirmed` | `false` | `guard` refuses the build unless this stays `false`. |
| `referralContactEnabled` | `false` | `guard` refuses the build unless this stays `false`. No template prints a call button from this key. |
| `callsEnabled` | `false` | Same. There is no call-button branch. |
| `formSubmissionEnabled` | `false` | Same. There is no form renderer. |
| `referralPhone.live` | `false` | `guard` refuses the build if `live`, `e164`, or `display` is set. |
| `referralPhone.e164` | `null` | Not read by any HTML template. |
| `referralPhone.display` | `null` | Not read by any HTML template. |
| `marketStatus` | `provisional_unconfirmed` | `guard` refuses any other value. |
| `port` | `43217` | `serve.py` `load_port` uses this unless the environment variable `PREVIEW_PORT` is set. A static host ignores it. |
| `contentDate` / `contentDateLabel` | `2026-11-07` / `November 7, 2026` | Sitemap `lastmod` and the visible draft date. |

`src/build.py` also has a hardcoded blocklist that refuses a canonical host containing `auroracoplumbers.com` (and several other domain names), even if `allowNonLocalCanonical` is later set true. That blocklist must be changed in code for launch.

So flipping `config/site.json` today cannot produce a public build. `guard` exits before pages are written. A launch build requires a code change to `guard` and to the hardcoded strings below, then a new `python3 src/build.py`, then a new zip. Prepare that change, but do not publish it until the approval above exists.

### Preview banner, header, footer, robots

These are literal strings in `src/build.py` `render`, not flags:

- The banner is the paragraph with class `preview-banner`: “Unpublished preview of … Pages ask search engines not to list them. Calls, email, and forms are off…”
- The header kicker is the text `Provisional preview`.
- The header status is `Preview · noindex · phone not connected`.
- `<meta name="robots" content="noindex, follow">` and the matching `googlebot` meta are fixed. They do not consult `site["noindex"]`.
- The footer says the guide does not publish a phone number or a request form in this preview, then prints `canonicalHost` and “Pages send noindex.”
- Homepage JSON-LD in `organization_graph` says contact is not enabled and that the preview is not accepting requests. Only the homepage gets Organization, WebSite, and Service. Other pages get BreadcrumbList only. There is no FAQPage, Review, or AggregateRating, and the schema has no telephone.

`src/static/css/site.css` only styles `.preview-banner` and `.header-status`. Hiding them with CSS would leave the “unpublished preview” sentence in the HTML. Do not do that as a launch step. Remove or replace the strings in `render`, then rebuild, after approval.

`serve.py` `end_headers` adds `X-Robots-Tag: noindex, follow` on every response, including CSS and the 404. That header is not inside the zip. A static host will not send it unless the host is configured to. The meta tag inside each HTML file still says noindex, which is enough for the review upload to ask search engines not to list the pages.

`write_robots` writes `dist/robots.txt` as `User-agent: *` and `Allow: /`, plus a comment that the file is not a launch configuration. It does not contain a `Sitemap:` line. `Allow: /` is intentional so a crawler can see the noindex meta. It is not an instruction to index.

### Phone-only call to action

**The number implementation does not exist.** It has to be added. There is no function that prints `referralPhone.display` or an `href="tel:"` link. Searches of the built HTML found zero `tel:` and zero `mailto:` strings.

What exists today:

- `config/site.json` `referralPhone` is a lock. The build refuses to run if a number is filled in.
- `/contact/` is static copy in `src/pages_site.py` `contact`. The H1 is “Call is not connected.” The body says the guide’s phone is not published.
- `/how-it-works/` says a number is not on the page.
- City and utility numbers in the articles are ordinary text, not links. They are those offices’ numbers. They must not become the referral button.
- `config/launch-private.json` `phonesDoNotActivate` lists old numbers that must not be used. Do not type those into `referralPhone` or the banner. The live number has to be a new route Saravanan confirms.

After Saravanan confirms the number, the code change is: allow one number through `guard`, render one `tel:` link from `referralPhone.e164` with visible `referralPhone.display`, use that same snippet in the header or contact panel and nowhere else, and update the contact, how-it-works, privacy, terms, and footer sentences that currently say no number is published. Privacy already says a future number would be shown in one place and that the policy would name who receives the call before that happens. Do that naming in the same change. Do not add a form.

`tests/test_preview.py` currently fails the build output if it contains `tel:`, `mailto:`, `auroracoplumbers.com`, or a canonical that does not start with `http://127.0.0.1:43217`. Those tests match the preview. They have to be updated in the same approved launch change, or `python3 -m unittest tests.test_preview` will reject the launch HTML.

### Forms

No page template emits `<form>`. The built HTML has zero `<form` tags. `/guides/plumbing-quote-checklist/` is a local checklist. `src/pages_site.py` attaches `/js/quote.js` only on that page. `quote.js` reads checkboxes, writes text into the page, can copy with `navigator.clipboard`, and can call `window.print`. It does not call `fetch`, and it does not save to `localStorage`.

`serve.py` `do_POST` reads any POST body and answers `403` with “Nothing was stored or forwarded.” That behavior exists only while `serve.py` is the server. A static host will not run it. The review upload still has nothing to submit. Do not add a form handler at the host.

Known checklist defect (not yet fixed): after someone clicks “build briefing,” `quote.js` inserts links to `/draft/research-notes/` and `/service-area/`. Those paths are not HTML files in `dist`. `serve.py` redirects only `/service-area` and `/service-area/` to `/areas/`. `/draft/research-notes/` is a 404 even on the preview server. On a static host, both targets 404 unless redirects are added.

## Source layout and commands

From the source zip, the files that produce the site are:

- `config/site.json` — public preview settings. Safe to discuss. Not a launch switch by itself.
- `config/launch-private.json` — private gates. Never copy into the web root.
- `src/build.py` — generator, guards, banner, canonical, sitemap, robots.
- `src/content.py` — page order.
- `src/pages_*.py` and `src/markup.py` — article HTML.
- `src/static/` — CSS, JS, SVG, favicon, copied into `dist/` unchanged.
- `src/expansion/validate.py` — refuses a city page that is only a renamed Aurora page.
- `serve.py` — local preview server only.
- `tests/test_preview.py` — preview QA.
- `research/aurora-expanded/` — architecture CSV the build counts against.

Commands, from the source tree, with Python 3 and no extra packages:

```bash
python3 src/build.py
python3 -m unittest tests.test_preview
python3 serve.py
```

`src/build.py` deletes `dist/` and writes it again. The last successful build printed `Built 111 indexable-path pages (all noindex) and a 404.` `reports/build-phases.json` then records `builtCount` 111, `architectureRows` 111, `architectureBuilt` 111, `architectureMerged` 0, `architectureGated` 0, and 44 of 44 plumbing labels with the owning page present.

`serve.py` listens on `0.0.0.0` and the port from `config/site.json` (`43217`) or `PREVIEW_PORT`. It is not a production server. It sends `X-Content-Type-Options: nosniff`, `Referrer-Policy: no-referrer`, and `Cache-Control: no-store`.

Two generated sentences are stale and should not be used as the publishing description. `src/build.py` `write_page_map` still writes “Neighboring cities are not published” into `reports/page-map.md`. The phase report still contains an older sentence that 111 is not a count of pages on the site. The JSON counts above are the ones that match this export. `docs/launch-gates.md` is also older: it still says Lakewood and several specialty pages were not written. They are in this `dist`.

## Static hosting

The export is static files. It does not need PHP, a database, or Node on the server. Any host that can serve those files can hold a review copy.

What the host must do for the URLs to match the HTML:

- Serve `index.html` for a directory. The page `/services/sewer-line-repair/` is the file `services/sewer-line-repair/index.html`. Apache and IIS normally do this when the directory index is `index.html`. Confirm that on the account.
- A request for the same path without the trailing slash is not a file. `serve.py` answers `301` to the slash form. The zip does not. The host needs that redirect, or slashless links 404.
- A request for `.../index.html` is `301` to the directory URL in `serve.py` only. Add the same redirect on the host if those URLs should not be a second copy.
- Unknown paths: `serve.py` returns `404` and the body of `404.html`. The file in the zip is `404.html`. The host must be told to use it as the error document and to send HTTP 404, not HTTP 200. This repo has no `.htaccess` and no `web.config`.
- Legacy paths exist only in `serve.py` `legacy`, as `301` responses. They are not files. If old links matter, copy this map to the host:

| Request | 301 target |
| --- | --- |
| `/sewer-line-repair` and `/sewer-line-repair/` | `/services/sewer-line-repair/` |
| `/drain-cleaning` and `/drain-cleaning/` | `/services/drain-cleaning/` |
| `/hydro-jetting` and `/hydro-jetting/` | `/services/hydro-jetting/` |
| `/sewer-camera-inspection` and `/sewer-camera-inspection/` | `/services/sewer-camera-inspection/` |
| `/water-heater-replacement` and `/water-heater-replacement/` | `/services/water-heater-replacement/` |
| `/water-heater-repair` and `/water-heater-repair/` | `/services/water-heater-repair/` |
| `/service-area` and `/service-area/` | `/areas/` |
| `/quote-readiness` and `/quote-readiness/` | `/guides/plumbing-quote-checklist/` |

Gowrish chooses the hosting provider and coordinates account access with Christian. Christian uploads the files and does the configuration and QA below. With any provider:

- Upload the unzipped `dist` contents into the document root the chosen provider specifies for the domain. Do not upload the source zip or `config/launch-private.json`.
- Use the provider's SSL certificate, and its HTTPS redirect method, only for launch and only after the canonical host is the HTTPS origin you chose. This repository does not ship `.htaccess` or `web.config` files.
- Use a domain alias or redirect so the non-canonical hostname redirects. Do not serve the same HTML on two hostnames without a redirect. This repo does not pick apex versus `www`.
- Do not rebuild this site in a site builder or WordPress. That would replace the researched pages. Uploading the static `dist` files is the compatible path.
- Set the account's error document to `/404.html` and check that it returns HTTP status 404.

Any static host is compatible if it can serve `index.html`, lets you set a 404 document, and lets you add the redirects above. Redirect mechanisms vary by provider, for example: Netlify `_redirects`, Cloudflare Pages `_redirects`, Apache `.htaccess`, IIS `web.config`, S3 plus CloudFront custom error and routing. None of those files are in the zip today.

For a review upload, prefer a hostname that is not the future public domain, or a password on the directory. If the files are reachable without a password, the baked-in `noindex` meta is what asks crawlers not to list them. The banner and the `127.0.0.1` canonical will be visible. That is acceptable for review and not acceptable as the public site.

## Launch change list, only after written approval (prepare now, publish after sign-off)

Do these in the source tree, then rebuild. Do not hand-edit the current `dist` zip.

1. Saravanan confirms the call route, what that route accepts, and the economics in writing. Leave `config/launch-private.json` off the server.
2. Domain bought by Gowrish (assigned now; not gated on this approval). Point DNS to the host.
3. Choose one HTTPS origin. Set `config/site.json` `canonicalHost` to that origin, including `https://` and no path. Point `productionHost` at the same origin only after `guard` is changed to allow it. Redirect http, and the other hostname, to that origin.
4. Change `guard` so an approved launch is allowed. Keep the refusal for the do-not-activate numbers. Keep the refusal if more than one referral number would be rendered.
5. Add the phone renderer that does not exist yet. One `tel:` link, same number in the contact panel. No form. Update contact, how-it-works, privacy, terms, footer, banner, header kicker, and header status.
6. Replace the fixed `noindex, follow` meta with the indexable robots policy Saravanan approves, in `render`. Stop sending `X-Robots-Tag: noindex` from any host config. Update `robots.txt` in `write_robots` if a sitemap line is wanted. The sitemap `<loc>` values change automatically once `canonicalHost` changes, because `write_sitemap` uses that host.
7. Remove or replace the preview banner in `render`. Do not hide it only with CSS.
8. Update `organization_graph` so the homepage schema no longer says the preview is not accepting requests, and still does not claim a contractor license, a review, or a phone in schema unless Saravanan wants the telephone property. Default remains no telephone in schema until that is an explicit decision.
9. Add host redirects for trailing slash, `index.html`, and the legacy table above. Point the error document at `/404.html` with status 404.
10. Update `tests/test_preview.py` so it checks the launch rules instead of the preview locks. Run `python3 -m unittest tests.test_preview`.
11. Rebuild with `python3 src/build.py`. Upload only the new `dist` contents. Confirm `launch-private.json` is not on the server.

## End-to-end checks

Review upload, against the current v5 dist, before anyone calls it public:

- Unzip and confirm 112 HTML files, `robots.txt`, and `sitemap.xml`.
- Open `/`. One H1: “Plumber Aurora CO”. Banner visible. Header says “Preview · noindex · phone not connected”. View source: `noindex, follow`, canonical `http://127.0.0.1:43217/`.
- Count `<loc>` in `sitemap.xml`: 111. Every loc starts with `http://127.0.0.1:43217/`. `404.html` is not in the sitemap.
- `robots.txt` is `Allow: /` and has no sitemap line.
- Click “Which repair,” one city (Byers should say Arapahoe County and must not say the census place is unincorporated Adams County), and one service. Internal links use root-relative paths such as `/areas/byers/`.
- On the quote checklist, build a briefing. Confirm the status text says nothing was sent. Expect the two stale links noted above.
- Search the HTML for `<form`, `tel:`, and `mailto:`. Expect none.
- POST to `/contact/` only does something special if `serve.py` is running: status 403 and a page that says nothing was stored. A static host will not show that page.
- A nonsense path shows `404.html` with status 404 only when the host is configured. On `serve.py`, `/no-such-city/` does this.
- Legacy `/sewer-line-repair/` returns 301 to `/services/sewer-line-repair/` only on `serve.py`, until the host map is added.
- Mobile width: the header becomes a Menu button. That behavior is `src/static/js/site.js` at 860px.

Approved launch, after the code change, in addition:

- Canonical and every sitemap loc use the single HTTPS origin. Requesting `http://`, and the non-canonical hostname, returns a redirect to that origin. The certificate matches the hostname.
- View source has no preview banner, no “phone not connected,” and no `noindex`, unless a specific page was deliberately left noindex.
- Exactly one referral `tel:` link, and the visible digits match `referralPhone.display`. City numbers are still not `tel:` links.
- Still zero forms. POST still stores nothing.
- Trailing-slash, slashless, and legacy URLs behave as the table above. Unknown URL is HTTP 404 with `404.html`.
- `config/launch-private.json` is not reachable as a URL.
- `python3 -m unittest tests.test_preview` passes against the launch rules.

Do not submit to Google Search Console until Saravanan approves the final launch.
