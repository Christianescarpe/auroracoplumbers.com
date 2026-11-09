#!/usr/bin/env python3
"""Local preview server.

Sends X-Robots-Tag on every response, serves clean URLs, and refuses POST
so a preview cannot pretend a lead was accepted.
"""

from __future__ import annotations

import json
import os
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent
DIST = ROOT / "dist"
CONFIG = ROOT / "config" / "site.json"

CONTENT_TYPES = {
    ".css": "text/css; charset=utf-8",
    ".js": "text/javascript; charset=utf-8",
    ".svg": "image/svg+xml",
    ".html": "text/html; charset=utf-8",
    ".xml": "application/xml; charset=utf-8",
    ".txt": "text/plain; charset=utf-8",
    ".json": "application/json; charset=utf-8",
}


class PreviewHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, directory: str, **kwargs):
        super().__init__(*args, directory=directory, **kwargs)

    def end_headers(self) -> None:
        self.send_header("X-Robots-Tag", "noindex, follow")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Referrer-Policy", "no-referrer")
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def do_POST(self) -> None:  # noqa: N802
        length = int(self.headers.get("Content-Length", "0") or "0")
        if length:
            self.rfile.read(length)
        body = (
            "<!DOCTYPE html><html lang='en'><head><meta charset='utf-8'>"
            "<title>Submissions are disabled</title>"
            "<meta name='robots' content='noindex, follow'></head>"
            "<body><h1>Submissions are disabled</h1>"
            "<p>Nothing was stored or forwarded. This preview has no lead endpoint.</p>"
            "<p><a href='/contact/'>Contact status</a></p></body></html>"
        ).encode("utf-8")
        self.send_response(403)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:  # noqa: N802
        self._serve(allow_redirect=True)

    def do_HEAD(self) -> None:  # noqa: N802
        self._serve(allow_redirect=True)

    def _serve(self, allow_redirect: bool) -> None:
        split = urlsplit(self.path)
        raw_path = unquote(split.path)
        legacy = {
            "/sewer-line-repair": "/services/sewer-line-repair/",
            "/sewer-line-repair/": "/services/sewer-line-repair/",
            "/drain-cleaning": "/services/drain-cleaning/",
            "/drain-cleaning/": "/services/drain-cleaning/",
            "/hydro-jetting": "/services/hydro-jetting/",
            "/hydro-jetting/": "/services/hydro-jetting/",
            "/sewer-camera-inspection": "/services/sewer-camera-inspection/",
            "/sewer-camera-inspection/": "/services/sewer-camera-inspection/",
            "/water-heater-replacement": "/services/water-heater-replacement/",
            "/water-heater-replacement/": "/services/water-heater-replacement/",
            "/water-heater-repair": "/services/water-heater-repair/",
            "/water-heater-repair/": "/services/water-heater-repair/",
            "/service-area": "/areas/",
            "/service-area/": "/areas/",
            "/quote-readiness": "/guides/plumbing-quote-checklist/",
            "/quote-readiness/": "/guides/plumbing-quote-checklist/",
        }
        if raw_path in legacy:
            self._redirect(legacy[raw_path])
            return
        if raw_path != "/" and raw_path.endswith("/index.html"):
            self._redirect(raw_path[: -len("index.html")])
            return
        if ".." in raw_path.split("/"):
            self._not_found()
            return
        rel = raw_path.lstrip("/")
        root = DIST.resolve()
        if raw_path.endswith("/") or raw_path == "":
            candidate = (DIST / rel / "index.html").resolve()
        else:
            candidate = (DIST / rel).resolve()
            if candidate.is_dir():
                if allow_redirect:
                    self._redirect(raw_path + "/")
                return
            if not candidate.suffix:
                pretty = (DIST / rel / "index.html").resolve()
                if pretty.is_file():
                    if allow_redirect:
                        self._redirect(raw_path + "/")
                    return
        if not str(candidate).startswith(str(root)) or not candidate.is_file():
            self._not_found()
            return
        self._file(candidate)

    def _file(self, path: Path) -> None:
        data = path.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", CONTENT_TYPES.get(path.suffix, "application/octet-stream"))
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(data)

    def _redirect(self, location: str) -> None:
        self.send_response(301)
        self.send_header("Location", location)
        self.send_header("Content-Length", "0")
        self.end_headers()

    def _not_found(self) -> None:
        page = DIST / "404.html"
        data = page.read_bytes() if page.is_file() else b"Not found"
        self.send_response(404)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(data)

    def log_message(self, fmt: str, *args) -> None:
        if os.environ.get("PREVIEW_QUIET") == "1":
            return
        super().log_message(fmt, *args)


def load_port() -> int:
    if os.environ.get("PREVIEW_PORT"):
        return int(os.environ["PREVIEW_PORT"])
    with CONFIG.open(encoding="utf-8") as handle:
        return int(json.load(handle)["port"])


def main() -> None:
    if not (DIST / "index.html").is_file():
        raise SystemExit("dist/ is missing. Run python3 src/build.py first.")
    port = load_port()
    handler = partial(PreviewHandler, directory=str(DIST))
    server = ThreadingHTTPServer(("0.0.0.0", port), handler)
    print(f"Preview http://127.0.0.1:{port}/", flush=True)
    server.serve_forever()


if __name__ == "__main__":
    main()
