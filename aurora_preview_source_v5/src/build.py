#!/usr/bin/env python3
"""Build the noindex plumbing preview scaffold into dist/."""

from __future__ import annotations

import html
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

import content  # noqa: E402
from expansion.validate import assert_catalog  # noqa: E402

DIST = ROOT / "dist"
SITE_PATH = ROOT / "config" / "site.json"
PRIVATE_PATH = ROOT / "config" / "launch-private.json"
STATIC = ROOT / "src" / "static"
REPORTS = ROOT / "reports"

BANNED_CANONICAL_FRAGMENTS = (
    "auroracoplumbers.com",
    "auroraplumbingrepair.com",
    "auroraplumberco.com",
    "auroracoloradoplumber.com",
    "plumberauroraco.net",
    "plumberauroraco.com",
    "plumberstocktonca.com",
)


def load_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def guard(site: dict) -> None:
    if site.get("noindex") is not True:
        raise SystemExit("Refusing to build: noindex must stay true on this preview.")
    if site.get("referralMarketConfirmed") is not False:
        raise SystemExit("Refusing to build: referral market is not confirmed.")
    for key in ("referralContactEnabled", "callsEnabled", "formSubmissionEnabled"):
        if site.get(key) is not False:
            raise SystemExit(f"Refusing to build: {key} must stay false.")
    phone = site.get("referralPhone") or {}
    if phone.get("live") or phone.get("e164") or phone.get("display"):
        raise SystemExit("Refusing to build: referral phone is not confirmed and must stay unpublished.")
    if site.get("productionHost") not in (None, ""):
        raise SystemExit("Refusing to build: productionHost must stay empty.")
    if site.get("marketStatus") != "provisional_unconfirmed":
        raise SystemExit("Refusing to build: marketStatus is not provisional_unconfirmed.")
    host = site.get("canonicalHost") or ""
    lowered = host.lower()
    for fragment in BANNED_CANONICAL_FRAGMENTS:
        if fragment in lowered:
            raise SystemExit(f"Refusing to build: canonical host must not claim {fragment}.")
    if not site.get("allowNonLocalCanonical"):
        if not (
            lowered.startswith("http://127.0.0.1:")
            or lowered.startswith("http://localhost:")
        ):
            raise SystemExit(
                "Refusing to build: canonical host must be a local preview origin."
            )
    if PRIVATE_PATH.exists():
        private_text = PRIVATE_PATH.read_text(encoding="utf-8")
        if "activateAnyPhone" not in private_text:
            raise SystemExit("Private launch file is missing activateAnyPhone.")


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def json_ld(payload: dict) -> str:
    raw = json.dumps(payload, ensure_ascii=True, indent=2)
    return raw.replace("<", "\\u003c")


def organization_graph(site: dict) -> str:
    host = site["canonicalHost"].rstrip("/")
    return json_ld(
        {
            "@context": "https://schema.org",
            "@graph": [
                {
                    "@type": "Organization",
                    "@id": f"{host}/#organization",
                    "name": site["brandName"],
                    "url": f"{host}/",
                    "description": (
                        "Referral guide to plumbing decisions in Aurora, Colorado. "
                        "Not a plumbing contractor. Contact is not enabled in this preview."
                    ),
                },
                {
                    "@type": "WebSite",
                    "@id": f"{host}/#website",
                    "name": site["brandName"],
                    "url": f"{host}/",
                    "publisher": {"@id": f"{host}/#organization"},
                },
                {
                    "@type": "Service",
                    "@id": f"{host}/#service",
                    "name": "Plumbing decision guidance",
                    "serviceType": "Consumer information",
                    "provider": {"@id": f"{host}/#organization"},
                    "areaServed": {
                        "@type": "City",
                        "name": "Aurora",
                        "containedInPlace": {
                            "@type": "State",
                            "name": "Colorado",
                        },
                    },
                    "description": (
                        "Explains plumbing decisions for properties in Aurora, Colorado. "
                        "This preview does not perform plumbing and is not accepting requests."
                    ),
                },
            ],
        }
    )


def breadcrumb_ld(site: dict, page: dict) -> str:
    host = site["canonicalHost"].rstrip("/")
    items = [
        {
            "@type": "ListItem",
            "position": 1,
            "name": "Home",
            "item": f"{host}/",
        }
    ]
    parents = inferred_parents(page)
    for index, parent in enumerate(parents, start=2):
        items.append(
            {
                "@type": "ListItem",
                "position": index,
                "name": parent["name"],
                "item": host + parent["href"],
            }
        )
    if page["path"] != "/":
        items.append(
            {
                "@type": "ListItem",
                "position": len(items) + 1,
                "name": page["breadcrumb"],
                "item": host + page["path"],
            }
        )
    return json_ld(
        {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": items,
        }
    )


def nav_html(site: dict, page: dict) -> str:
    del site
    links = [
        ("/", "Home"),
        ("/services/", "Which repair"),
        ("/services/sewer-line-repair/", "Sewer lines"),
        ("/services/water-heater-replacement/", "Water heaters"),
        ("/guides/plumbing-quote-checklist/", "Quote list"),
        ("/areas/", "Nearby cities"),
        ("/how-it-works/", "How it works"),
    ]
    parts = []
    for href, label in links:
        current = " aria-current=\"page\"" if href == page["path"] else ""
        parts.append(f'<li><a href="{esc(href)}"{current}>{esc(label)}</a></li>')
    return "\n".join(parts)


def inferred_parents(page: dict) -> list[dict]:
    if page.get("parents") is not None:
        return page["parents"]
    path = page["path"]
    parts = [part for part in path.split("/") if part]
    if len(parts) == 2 and parts[0] == "services":
        return [{"name": "Which repair", "href": "/services/"}]
    if len(parts) == 2 and parts[0] == "guides":
        return [{"name": "Guides", "href": "/guides/"}]
    if len(parts) == 2 and parts[0] == "areas":
        return [{"name": "Nearby cities", "href": "/areas/"}]
    if len(parts) == 3 and parts[0] == "areas":
        slug = parts[1]
        label = slug.replace("-", " ").title()
        return [
            {"name": "Nearby cities", "href": "/areas/"},
            {"name": label, "href": f"/areas/{slug}/"},
        ]
    return []


def crumbs_html(page: dict) -> str:
    if page["path"] == "/":
        return '<nav class="crumbs" aria-label="Breadcrumb"><ol><li>Home</li></ol></nav>'
    items = ['<li><a href="/">Home</a></li>']
    for parent in inferred_parents(page):
        items.append(f'<li><a href="{esc(parent["href"])}">{esc(parent["name"])}</a></li>')
    items.append(f"<li>{esc(page['breadcrumb'])}</li>")
    return '<nav class="crumbs" aria-label="Breadcrumb"><ol>' + "".join(items) + "</ol></nav>"


def render(site: dict, page: dict) -> str:
    host = site["canonicalHost"].rstrip("/")
    canonical = host + page["path"]
    title = page["title"]
    description = page["description"]
    org = organization_graph(site) if page["path"] == "/" else ""
    org_script = f'<script type="application/ld+json">\n{org}\n</script>' if org else ""
    crumbs_ld = breadcrumb_ld(site, page)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(description)}">
  <meta name="robots" content="noindex, follow">
  <meta name="googlebot" content="noindex, follow">
  <link rel="canonical" href="{esc(canonical)}">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <meta name="theme-color" content="#163e3c">
  <link rel="stylesheet" href="/css/site.css">
  {org_script}
  <script type="application/ld+json">
{crumbs_ld}
  </script>
</head>
<body>
  <a class="skip" href="#content">Skip to content</a>
  <p class="preview-banner">Unpublished preview of {esc(site["brandName"])}. Pages ask search engines not to list them. Calls, email, and forms are off, and a contractor is not dispatched from this site.</p>
  <header class="site-header">
    <div class="header-inner">
      <a class="brand" href="/">
        <span class="brand-mark" aria-hidden="true">AP</span>
        <span class="brand-text">
          <span class="brand-name">{esc(site["brandName"])}</span>
          <span class="brand-kicker">Provisional preview</span>
        </span>
      </a>
      <p class="header-status">Preview · noindex · phone not connected</p>
      <button type="button" class="nav-toggle" aria-expanded="false" aria-controls="site-nav">Menu</button>
      <nav id="site-nav" class="site-nav" aria-label="Primary">
        <ul>
          {nav_html(site, page)}
        </ul>
      </nav>
    </div>
  </header>
  <main id="content" class="site-main">
    {crumbs_html(page)}
    {page["body"]}
  </main>
  <footer class="site-footer">
    <div class="footer-inner">
      <p class="footer-brand">{esc(site["brandName"])}</p>
      <p>{esc(site["brandName"])} explains plumbing decisions. It is not a licensed plumbing contractor, and it does not publish a phone number or a request form in this preview. Nothing here confirms that a contractor will accept a {esc(site["cityName"])} job.</p>
      <ul class="footer-links">
        <li><a href="/about/">About</a></li>
        <li><a href="/contact/">Contact</a></li>
        <li><a href="/privacy/">Privacy</a></li>
        <li><a href="/terms/">Terms</a></li>
        <li><a href="/how-it-works/">How it works</a></li>
      </ul>
      <p class="footer-meta">Draft dated {esc(site["contentDateLabel"])}. Canonical host for this preview only: {esc(site["canonicalHost"])}. No production domain is attached. Pages send noindex.</p>
    </div>
  </footer>
  <script src="/js/site.js"></script>
  {page.get("extra_scripts", "")}
</body>
</html>
"""


def write_page(page: dict, html_text: str) -> None:
    if page["path"] == "/":
        target = DIST / "index.html"
    elif page["path"].endswith(".html"):
        target = DIST / page["path"].lstrip("/")
    else:
        target = DIST / page["path"].strip("/") / "index.html"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(html_text, encoding="utf-8")


def write_sitemap(site: dict, pages: list[dict]) -> None:
    host = site["canonicalHost"].rstrip("/")
    urls = []
    for page in pages:
        if not page.get("in_sitemap", True):
            continue
        loc = host + page["path"]
        urls.append(
            "  <url>\n"
            f"    <loc>{esc(loc)}</loc>\n"
            f"    <lastmod>{esc(site['contentDate'])}</lastmod>\n"
            "  </url>"
        )
    body = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(urls)
        + "\n</urlset>\n"
    )
    (DIST / "sitemap.xml").write_text(body, encoding="utf-8")


def write_robots() -> None:
    text = (
        "User-agent: *\n"
        "Allow: /\n"
        "\n"
        "# Preview only. HTML pages send noindex. Crawling is allowed so that\n"
        "# noindex can be seen. This file is not a launch configuration.\n"
    )
    (DIST / "robots.txt").write_text(text, encoding="utf-8")


def write_page_map(site: dict, pages: list[dict]) -> None:
    REPORTS.mkdir(parents=True, exist_ok=True)
    rows = []
    for page in pages:
        rows.append(
            {
                "path": page["path"],
                "title": page["title"],
                "h1": page["h1"],
                "intendedKeyword": page.get("intended_keyword", ""),
                "keywordStatus": page.get(
                    "keyword_status",
                    "Provisional draft. Not a launched ranking page.",
                ),
                "inSitemap": bool(page.get("in_sitemap", True)),
                "httpStatus": 200 if page.get("in_sitemap", True) else 404,
            }
        )
    payload = {
        "canonicalHost": site["canonicalHost"],
        "productionHost": None,
        "noindex": True,
        "marketStatus": site["marketStatus"],
        "referralMarketConfirmed": False,
        "pages": rows,
    }
    (REPORTS / "page-map.json").write_text(
        json.dumps(payload, indent=2) + "\n", encoding="utf-8"
    )
    lines = [
        "# Page map",
        "",
        "Aurora, Colorado consumer guide. Noindex preview. Neighboring cities are not published.",
        f"Canonical host: `{site['canonicalHost']}` (local preview only).",
        "",
        "| URL | Title | H1 | Intended keyword | Status |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in rows:
        lines.append(
            "| {path} | {title} | {h1} | {intendedKeyword} | {keywordStatus} |".format(
                **{key: str(row[key]).replace("|", "/") for key in row}
            )
        )
    lines.append("")
    (REPORTS / "page-map.md").write_text("\n".join(lines), encoding="utf-8")


def build() -> list[dict]:
    site = load_json(SITE_PATH)
    guard(site)
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir(parents=True)
    shutil.copytree(STATIC, DIST, dirs_exist_ok=True)
    assert_catalog()
    pages = content.pages(site)
    write_phase_report(pages)
    h1s = [page["h1"] for page in pages]
    titles = [page["title"] for page in titles_check(pages)]
    if len(h1s) != len(set(h1s)):
        raise SystemExit("Duplicate H1 in page set.")
    if len(titles) != len(set(titles)):
        raise SystemExit("Duplicate title in page set.")
    paths = [page["path"] for page in pages]
    if len(paths) != len(set(paths)):
        raise SystemExit("Duplicate path in page set.")
    for page in pages:
        write_page(page, render(site, page))
    write_sitemap(site, pages)
    write_robots()
    write_page_map(site, pages)
    private_copy = DIST / "launch-private.json"
    if private_copy.exists():
        raise SystemExit("Private launch file was copied into dist.")
    return pages


def titles_check(pages: list[dict]) -> list[dict]:
    return pages


def write_phase_report(pages: list[dict]) -> None:
    REPORTS.mkdir(parents=True, exist_ok=True)
    phase_path = ROOT / "src" / "expansion" / "next_phase.json"
    pending = json.loads(phase_path.read_text(encoding="utf-8"))
    built = []
    for page in pages:
        if not page.get("in_sitemap", True):
            continue
        built.append(
            {
                "path": page["path"],
                "title": page["title"],
                "h1": page["h1"],
                "kind": page.get("kind", "support"),
                "intendedKeyword": page.get("intended_keyword", ""),
            }
        )
    payload = {
        "builtCount": len(built),
        "built": built,
        "notBuilt": pending,
        "keywordResearch": (
            "No search-volume or keyword-difficulty study was run. "
            "Topics follow the Aurora city sources and the November 6, 2026 research handoff. "
            "Competitor pages were discovery reading, not a ranking report."
        ),
    }
    (REPORTS / "build-phases.json").write_text(
        json.dumps(payload, indent=2) + "\n", encoding="utf-8"
    )
    lines = [
        "# What is built, and what is not",
        "",
        f"Built and covered by the preview QA checks: {len(built)} public URLs, plus a 404 that is not in the sitemap.",
        "",
        "These are Aurora, Colorado pages. A contractor route is not confirmed. Calls and forms are off.",
        "",
        "| URL | H1 | Kind |",
        "| --- | --- | --- |",
    ]
    for row in built:
        lines.append(f"| {row['path']} | {row['h1']} | {row['kind']} |")
    lines.extend(
        [
            "",
            "## Not built",
            "",
            pending["locationHubs"],
            "",
            pending["serviceCityPages"],
            "",
            pending["moreGuides"],
            "",
            pending["moreServices"],
            "",
            pending["pageCountNote"],
            "",
            payload["keywordResearch"],
            "",
        ]
    )
    arch = ROOT / "research" / "aurora-expanded" / "expanded-architecture.csv"
    labels = ROOT / "research" / "aurora-expanded" / "all-44-arroyo-category-mapping.csv"
    built_paths = {row["path"] for row in built}
    if arch.is_file():
        import csv
        planned = list(csv.DictReader(arch.open(encoding="utf-8")))
        merged = {}
        gated = [
            row for row in planned
            if row["url"] not in built_paths and row["url"] not in merged
        ]
        payload["merged"] = merged
        payload["architectureRows"] = len(planned)
        payload["architectureBuilt"] = sum(1 for row in planned if row["url"] in built_paths)
        payload["architectureMerged"] = len(merged)
        payload["architectureAddressed"] = payload["architectureBuilt"] + payload["architectureMerged"]
        payload["architectureGated"] = len(gated)
        payload["gatedUrls"] = [
            {
                "url": row["url"],
                "status": row["research_and_publish_status"],
                "priority": row["first_release_priority"],
                "whyHeld": row["editorial_distinction"][:240],
            }
            for row in gated
        ]
        lines.append(f"Architecture rows described: {len(planned)}.")
        lines.append(f"Of those, published in this preview: {len(planned) - len(gated)}.")
        lines.append(f"Gated, not generated: {len(gated)}.")
        lines.append("")
        lines.append("111 is the researched architecture count, not a count of pages on this site.")
        lines.append("271 is a planning envelope that includes 160 unvalidated service-city hypotheses. Those URLs were not generated.")
        lines.append("")
    if labels.is_file():
        import csv
        mapped = list(csv.DictReader(labels.open(encoding="utf-8")))
        label_rows = []
        for row in mapped:
            owner = row["primary_owning_url"]
            label_rows.append(
                {
                    "label": row["source_label_verbatim"],
                    "owningUrl": owner,
                    "onThisPreview": owner in built_paths,
                }
            )
        payload["arroyoLabels"] = {
            "count": len(label_rows),
            "owningPagePublished": sum(1 for row in label_rows if row["onThisPreview"]),
            "rows": label_rows,
        }
        lines.append(f"Plumbing labels mapped: {len(label_rows)}. Labels whose owning page is published: {payload['arroyoLabels']['owningPagePublished']}.")
        lines.append("HVAC labels are excluded. Unpublished owners are gated, not cloned.")
        lines.append("")
    (REPORTS / "build-phases.json").write_text(
        json.dumps(payload, indent=2) + "\n", encoding="utf-8"
    )
    (REPORTS / "build-phases.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    pages = build()
    public = [page["path"] for page in pages if page.get("in_sitemap", True)]
    print(f"Built {len(public)} indexable-path pages (all noindex) and a 404.")


if __name__ == "__main__":
    main()
