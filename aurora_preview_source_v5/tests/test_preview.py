#!/usr/bin/env python3
"""QA for the Aurora noindex preview. Counts are whatever the build actually emitted."""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import threading
import unittest
import urllib.request
from html.parser import HTMLParser
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
REPORTS = ROOT / "reports"

BANNED = [
    "stockton",
    "california",
    "arroyo",
    "857-201",
    "708-350",
    "137.20",
    "164.15",
    "rev share",
    "payout",
    "tel:",
    "mailto:",
    "faqpage",
    "aggregaterating",
    "auroracoplumbers.com",
]


class Parser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.title = []
        self.in_title = False
        self.h1 = []
        self.hrefs = []
        self.forms = 0
        self.inputs = 0
        self.robots = []
        self.canonical = ""
        self.scripts = []
        self.in_script = False
        self.script_type = ""
        self.main = []
        self.in_main = False
        self.qa = []
        self.in_qa = False
        self.skip = False
        self.lang = ""

    def handle_starttag(self, tag, attrs):
        attr = dict(attrs)
        if tag == "html":
            self.lang = attr.get("lang", "")
        if tag == "title":
            self.in_title = True
        if tag == "h1":
            self.h1.append("")
            self._h1 = True
        else:
            self._h1 = getattr(self, "_h1", False) and tag != "h1"
        if tag == "h1":
            self._in_h1 = True
        if tag == "a":
            if attr.get("href"):
                self.hrefs.append(attr["href"])
            if attr.get("href") == "#content":
                self.skip = True
        if tag == "link" and attr.get("rel") == "canonical":
            self.canonical = attr.get("href", "")
        if tag == "meta" and attr.get("name") in {"robots", "googlebot"}:
            self.robots.append(attr.get("content", ""))
        if tag == "form":
            self.forms += 1
        if tag == "input":
            self.inputs += 1
        if tag == "script":
            self.in_script = True
            self.script_type = attr.get("type", "")
            self.scripts.append("")
        if tag == "main":
            self.in_main = True
        if tag == "p" and "qa-a" in attr.get("class", ""):
            self.in_qa = True
            self.qa.append("")

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
        if tag == "h1":
            self._in_h1 = False
        if tag == "script":
            self.in_script = False
        if tag == "main":
            self.in_main = False
        if tag == "p" and self.in_qa:
            self.in_qa = False

    def handle_data(self, data):
        if self.in_title:
            self.title.append(data)
        if getattr(self, "_in_h1", False):
            self.h1[-1] += data
        if self.in_script and self.script_type == "application/ld+json":
            self.scripts[-1] += data
        if self.in_main:
            self.main.append(data)
        if self.in_qa:
            self.qa[-1] += data


def words(text: str) -> int:
    return len(re.findall(r"[A-Za-z0-9’']+", text))


class PreviewTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        subprocess.run([sys.executable, str(ROOT / "src" / "build.py")], check=True, cwd=ROOT)
        cls.pages = []
        for path in sorted(DIST.rglob("*.html")):
            parser = Parser()
            text = path.read_text(encoding="utf-8")
            parser.feed(text)
            rel = "/" + str(path.relative_to(DIST)).replace("index.html", "")
            if str(path.relative_to(DIST)) == "index.html":
                rel = "/"
            if str(path.relative_to(DIST)) == "404.html":
                rel = "/404.html"
            cls.pages.append({"rel": rel, "text": text, "parsed": parser})

    def test_counts_match_the_phase_report(self):
        phase = json.loads((REPORTS / "build-phases.json").read_text(encoding="utf-8"))
        public = [page for page in self.pages if page["rel"] != "/404.html"]
        self.assertEqual(phase["builtCount"], len(public))
        self.assertEqual(phase["architectureRows"], 111)
        self.assertEqual(phase["architectureBuilt"], len(public))
        self.assertEqual(phase["architectureAddressed"], 111)
        self.assertEqual(phase["architectureGated"], 0)
        self.assertEqual(phase["arroyoLabels"]["count"], 44)
        self.assertEqual(phase["arroyoLabels"]["owningPagePublished"], 44)
        self.assertIn("/areas/denver/", {page["rel"] for page in public})
        self.assertIn("/areas/golden/", {page["rel"] for page in public})
        self.assertIn("/areas/morrison/", {page["rel"] for page in public})
        self.assertIn("not a target", phase["notBuilt"]["pageCountNote"])

    def test_uniqueness_noindex_and_links(self):
        host = "http://127.0.0.1:43217"
        titles, h1s, canonicals = [], [], []
        rels = {page["rel"] for page in self.pages}
        for page in self.pages:
            parsed = page["parsed"]
            title = " ".join(parsed.title).strip()
            h1 = " ".join(parsed.h1).strip()
            self.assertTrue(title and h1, page["rel"])
            self.assertEqual(page["text"].lower().count("<h1"), 1, page["rel"])
            self.assertIn("noindex", " ".join(parsed.robots).lower())
            self.assertTrue(parsed.canonical.startswith(host), parsed.canonical)
            self.assertEqual(parsed.lang, "en")
            self.assertTrue(parsed.skip, page["rel"])
            self.assertEqual(parsed.forms, 0, page["rel"])
            titles.append(title)
            h1s.append(h1)
            canonicals.append(parsed.canonical)
            for href in parsed.hrefs:
                if href.startswith(("http://", "https://", "#")):
                    continue
                self.assertIn(href.split("#", 1)[0], rels | {
                    "/css/site.css", "/js/site.js", "/js/quote.js", "/favicon.svg", "/img/lateral.svg"
                }, f"{href} from {page['rel']}")
        self.assertEqual(len(titles), len(set(titles)))
        self.assertEqual(len(h1s), len(set(h1s)))
        self.assertEqual(len(canonicals), len(set(canonicals)))
        self.assertEqual(sum(1 for h in h1s if h == "Plumber Aurora CO"), 1)
        inbound = {}
        for page in self.pages:
            for href in page["parsed"].hrefs:
                path = href.split("#", 1)[0]
                if path.startswith("/") and not path.startswith("/css") and not path.startswith("/js") and not path.startswith("/img") and path != "/favicon.svg":
                    inbound.setdefault(path, set()).add(page["rel"])
        for page in self.pages:
            if page["rel"] in {"/", "/404.html"}:
                continue
            self.assertIn(page["rel"], inbound, page["rel"])

    def test_banned_and_schema(self):
        blob = "\n".join(page["text"].lower() for page in self.pages)
        js = (DIST / "js" / "quote.js").read_text(encoding="utf-8").lower()
        for phrase in BANNED:
            self.assertNotIn(phrase, blob, phrase)
            self.assertNotIn(phrase, js, phrase)
        self.assertNotIn("$", blob)
        self.assertNotIn("fetch(", js)
        parker = next(page for page in self.pages if page["rel"] == "/areas/parker/")
        self.assertIn("will not", parker["text"].lower())
        self.assertIn("property line", parker["text"].lower())
        for page in self.pages:
            for script in page["parsed"].scripts:
                if not script.strip():
                    continue
                raw = json.dumps(json.loads(script)).lower()
                self.assertNotIn("faqpage", raw)
                self.assertNotIn("telephone", raw)
                self.assertNotIn("aggregaterating", raw)

    def test_answers_and_depth(self):
        phase = json.loads((REPORTS / "build-phases.json").read_text(encoding="utf-8"))
        kinds = {row["path"]: row["kind"] for row in phase["built"]}
        for page in self.pages:
            if page["rel"] == "/404.html":
                continue
            kind = kinds[page["rel"]]
            answers = [words(answer) for answer in page["parsed"].qa]
            for count in answers:
                self.assertGreaterEqual(count, 40, page["rel"])
                self.assertLessEqual(count, 70, page["rel"])
            if kind in {"service", "primary"}:
                self.assertGreaterEqual(len(answers), 4, page["rel"])
            if kind in {"place", "guide"}:
                self.assertGreaterEqual(len(answers), 3, page["rel"])
            text_words = words(" ".join(page["parsed"].main))
            if kind == "service":
                self.assertGreaterEqual(text_words, 380, page["rel"])
            if kind == "place":
                self.assertGreaterEqual(text_words, 380, page["rel"])

    def test_sitemap_allows_crawl(self):
        robots = (DIST / "robots.txt").read_text(encoding="utf-8")
        self.assertIn("Allow: /", robots)
        self.assertNotIn("Disallow: /", robots)
        sitemap = (DIST / "sitemap.xml").read_text(encoding="utf-8")
        self.assertNotIn("404", sitemap)
        self.assertIn("lakewood", sitemap)
        contact = next(page for page in self.pages if page["rel"] == "/contact/")
        self.assertEqual(contact["parsed"].inputs, 0)


class ServerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        env = os.environ.copy()
        env["PREVIEW_PORT"] = "43231"
        env["PREVIEW_QUIET"] = "1"
        cls.proc = subprocess.Popen(
            [sys.executable, str(ROOT / "serve.py")],
            cwd=ROOT,
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        for _ in range(40):
            try:
                urlopen("http://127.0.0.1:43231/", timeout=0.3)
                break
            except Exception:
                threading.Event().wait(0.05)
        else:
            raise RuntimeError("server did not start")

    @classmethod
    def tearDownClass(cls):
        cls.proc.terminate()
        cls.proc.wait(timeout=5)

    def get(self, path, method="GET", data=None, follow=True):
        request = Request(f"http://127.0.0.1:43231{path}", data=data, method=method)
        opener = urlopen
        if not follow:
            class Stay(urllib.request.HTTPRedirectHandler):
                def redirect_request(self, req, fp, code, msg, headers, newurl):
                    return None
            opener = urllib.request.build_opener(Stay).open
        try:
            with opener(request, timeout=3) as response:
                return response.status, dict(response.headers), response.read()
        except HTTPError as error:
            return error.code, dict(error.headers), error.read()

    def test_headers_legacy_404_post(self):
        status, headers, _ = self.get("/")
        self.assertEqual(status, 200)
        self.assertIn("noindex", headers.get("X-Robots-Tag", ""))
        status, headers, _ = self.get("/sewer-line-repair/", follow=False)
        self.assertEqual(status, 301)
        self.assertEqual(headers.get("Location"), "/services/sewer-line-repair/")
        status, _, body = self.get("/areas/byers/")
        text = body.decode()
        self.assertEqual(status, 200)
        self.assertIn("Arapahoe County", text)
        self.assertNotIn("unincorporated Adams County", text)
        status, _, body = self.get("/areas/watkins/")
        text = body.decode()
        self.assertEqual(status, 200)
        self.assertIn("Adams County and Arapahoe County", text)
        self.assertNotIn("Byers is on this page", text)
        status, _, body = self.get("/areas/franktown/")
        text = body.decode()
        self.assertEqual(status, 200)
        self.assertIn("not on that list", text)
        status, _, body = self.get("/areas/the-pinery/")
        text = body.decode()
        self.assertEqual(status, 200)
        self.assertNotIn("six census places", text)
        status, _, body = self.get("/no-such-city/")
        self.assertEqual(status, 404)
        self.assertIn(b"not in this preview", body.lower())
        status, _, body = self.get("/contact/", data=b"name=nope", method="POST")
        self.assertEqual(status, 403)
        self.assertIn(b"Nothing was stored", body)
        self.assertNotIn(b"name=nope", body)


class ExpansionTests(unittest.TestCase):
    def test_swap_is_rejected(self):
        sys.path.insert(0, str(ROOT / "src"))
        from expansion.validate import ExpansionError, publishable_overlay

        with self.assertRaises(ExpansionError):
            publishable_overlay(
                {
                    "id": "thin",
                    "place": "Centennial",
                    "decision_delta": "word " * 20,
                    "local_fact": "short",
                    "body": "Aurora owns the tap " * 30,
                },
                "Aurora owns the tap " * 30,
            )


if __name__ == "__main__":
    unittest.main()
