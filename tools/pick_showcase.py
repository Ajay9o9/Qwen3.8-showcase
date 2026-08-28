#!/usr/bin/env python3
"""Local picker for which benchmark pages go into the public showcase.

    python3 tools/pick_showcase.py
    python3 tools/pick_showcase.py --source-root /path/to/compare --port 8777
"""
from __future__ import annotations

import argparse
import json
import mimetypes
import re
import subprocess
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any
from urllib.parse import parse_qs, unquote, urlparse

sys.path.insert(0, str(Path(__file__).resolve().parent))
from export_showcase import canonical_tag, record_map, tag_folders, title_for

SHOWCASE = Path(__file__).resolve().parent.parent
DEFAULT_SOURCE = Path("/media/aj-homeserver/windows/krea2-model/qwen-3.8/compare")
PICKER_HTML = Path(__file__).resolve().parent / "picker.html"
SAFE = re.compile(r"^[a-zA-Z0-9._-]+$")
TRACK_PREFIX = {"web": "web_"}
# Think-off first-10 and non-Qwen runs are not a second model in this repo.
SKIP_TAGS = {
    "qwen38-27b-q4_k_m",
    "openrouter-ox-alpha",
}


def die(message: str) -> None:
    raise SystemExit(message)


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def pretty_tag(tag: str) -> str:
    text = tag
    for old, new in (("qwen3.8", "Qwen3.8"), ("qwen38", "Qwen3.8"),
                     ("qwen3.6", "Qwen3.6"), ("-27b", "-27B")):
        text = text.replace(old, new)
    return text.replace("-", " ")


def scan_library(source_root: Path) -> list[dict[str, Any]]:
    results = source_root / "results"
    if not results.is_dir():
        die(f"no results directory at {results}")
    items: list[dict[str, Any]] = []
    seen: set[tuple[str, str, str]] = set()
    for tag_dir in sorted(results.iterdir()):
        if not tag_dir.is_dir() or tag_dir.name.startswith(("_", ".")):
            continue
        if tag_dir.name in {"data", "_retries"}:
            continue
        if not SAFE.match(tag_dir.name):
            continue
        if tag_dir.name in SKIP_TAGS:
            continue
        for track, prefix in TRACK_PREFIX.items():
            records: dict[str, dict[str, Any]] = {}
            run_path = tag_dir / f"{track}.json"
            if run_path.is_file():
                try:
                    records = record_map(load_json(run_path))
                except Exception:
                    records = {}
            for html in sorted(tag_dir.glob(f"{prefix}*.html")):
                stem = html.stem
                if not SAFE.match(stem):
                    continue
                record = records.get(stem, {})
                shot = tag_dir / "web-shots" / stem / "desktop.png"
                group = canonical_tag(tag_dir.name)
                key = (group, track, stem)
                if key in seen:
                    continue
                seen.add(key)
                items.append({
                    "tag": group,
                    "source_tag": tag_dir.name,
                    "track": track,
                    "id": stem,
                    "title": title_for(stem, record),
                    "status": record.get("status"),
                    "has_shot": shot.is_file(),
                    "shot": f"/shot/{group}/{track}/{stem}.png" if shot.is_file() else None,
                    "preview": f"/preview/{group}/{stem}.html",
                })
    return items


def catalog_selected(manifest: dict[str, Any]) -> list[dict[str, str]]:
    selected: list[dict[str, str]] = []
    for entry in manifest.get("entries") or []:
        sources = entry.get("sources") or {}
        for track, config in sources.items():
            if not isinstance(config, dict):
                continue
            tag = canonical_tag(str(config.get("tag") or ""))
            tasks = config.get("tasks") or []
            if tasks == "all":
                continue
            if not isinstance(tasks, list):
                continue
            for task_id in tasks:
                selected.append({"tag": tag, "track": track, "id": str(task_id)})
    return selected


def new_entry(tag: str) -> dict[str, Any]:
    slug = re.sub(r"[^a-z0-9]+", "-", tag.lower()).strip("-")
    label = pretty_tag(tag)
    return {
        "id": slug,
        "name": label,
        "version": "",
        "quant": "",
        "label": label,
        "notes": "Added from the picker.",
        "sources": {},
    }


def apply_selection(manifest: dict[str, Any], selected: list[dict[str, str]]) -> dict[str, Any]:
    grouped: dict[tuple[str, str], list[str]] = {}
    for item in selected:
        tag, track, task_id = canonical_tag(item["tag"]), item["track"], item["id"]
        if track not in TRACK_PREFIX or not SAFE.match(tag) or not SAFE.match(task_id):
            continue
        grouped.setdefault((tag, track), []).append(task_id)

    entries = list(manifest.get("entries") or [])
    used_pairs: set[tuple[str, str]] = set()

    def find_entry(tag: str, track: str) -> dict[str, Any] | None:
        for entry in entries:
            config = ((entry.get("sources") or {}).get(track) or {})
            if isinstance(config, dict) and canonical_tag(str(config.get("tag") or "")) == tag:
                return entry
        for entry in entries:
            sources = entry.get("sources") or {}
            if any(isinstance(cfg, dict) and canonical_tag(str(cfg.get("tag") or "")) == tag for cfg in sources.values()):
                return entry
        return None

    for (tag, track), task_ids in grouped.items():
        entry = find_entry(tag, track)
        if entry is None:
            entry = new_entry(tag)
            entries.append(entry)
        sources = entry.setdefault("sources", {})
        sources[track] = {"tag": canonical_tag(tag), "tasks": sorted(set(task_ids))}
        used_pairs.add((canonical_tag(tag), track))

    kept: list[dict[str, Any]] = []
    for entry in entries:
        sources = entry.get("sources") or {}
        sources.pop("threejs", None)
        for track, config in list(sources.items()):
            if track not in TRACK_PREFIX or not isinstance(config, dict):
                sources.pop(track, None)
                continue
            tag = canonical_tag(str(config.get("tag") or ""))
            config["tag"] = tag
            if (tag, track) not in used_pairs:
                config["tasks"] = []
            if not config.get("tasks"):
                sources.pop(track, None)
        if sources:
            entry["sources"] = sources
            kept.append(entry)

    manifest = dict(manifest)
    manifest["entries"] = kept
    return manifest


def shot_path(source_root: Path, tag: str, track: str, stem: str) -> Path | None:
    if track not in TRACK_PREFIX:
        return None
    for folder in tag_folders(tag):
        path = source_root / "results" / folder / "web-shots" / stem / "desktop.png"
        if path.is_file():
            return path
    return None


def preview_path(source_root: Path, tag: str, stem: str) -> Path | None:
    for folder in tag_folders(tag):
        path = source_root / "results" / folder / f"{stem}.html"
        if path.is_file():
            return path
    return None


def make_handler(source_root: Path, catalog_path: Path) -> type[BaseHTTPRequestHandler]:
    class Handler(BaseHTTPRequestHandler):
        def log_message(self, fmt: str, *args: Any) -> None:
            sys.stderr.write("%s - %s\n" % (self.address_string(), fmt % args))

        def _send(self, code: int, body: bytes, content_type: str) -> None:
            self.send_response(code)
            self.send_header("Content-Type", content_type)
            self.send_header("Cache-Control", "no-store")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def _json(self, payload: Any, code: int = 200) -> None:
            self._send(code, json.dumps(payload).encode("utf-8"), "application/json")

        def _read_json(self) -> dict[str, Any]:
            length = int(self.headers.get("Content-Length") or 0)
            raw = self.rfile.read(length) if length else b"{}"
            try:
                value = json.loads(raw.decode("utf-8"))
            except json.JSONDecodeError:
                return {}
            return value if isinstance(value, dict) else {}

        def do_GET(self) -> None:
            parsed = urlparse(self.path)
            path = unquote(parsed.path)
            if path in {"/", "/index.html"}:
                return self._send(200, PICKER_HTML.read_bytes(), "text/html; charset=utf-8")
            if path == "/favicon.ico":
                self.send_response(204)
                self.end_headers()
                return
            if path == "/api/library":
                return self._json({"items": scan_library(source_root)})
            if path == "/api/catalog":
                manifest = load_json(catalog_path)
                return self._json({"catalog": manifest, "selected": catalog_selected(manifest)})
            if path.startswith("/shot/"):
                parts = path.strip("/").split("/")
                if len(parts) != 4:
                    return self.send_error(404)
                _, tag, track, filename = parts
                stem = Path(filename).stem
                if not (SAFE.match(tag) and SAFE.match(stem) and track in TRACK_PREFIX):
                    return self.send_error(404)
                target = shot_path(source_root, tag, track, stem)
                if not target:
                    return self.send_error(404)
                ctype = mimetypes.guess_type(str(target))[0] or "image/png"
                return self._send(200, target.read_bytes(), ctype)
            if path.startswith("/preview/"):
                parts = path.strip("/").split("/")
                if len(parts) != 3:
                    return self.send_error(404)
                _, tag, filename = parts
                stem = Path(filename).stem
                if not (SAFE.match(tag) and SAFE.match(stem)):
                    return self.send_error(404)
                target = preview_path(source_root, tag, stem)
                if not target:
                    return self.send_error(404)
                return self._send(200, target.read_bytes(), "text/html; charset=utf-8")
            return self.send_error(404)

        def do_POST(self) -> None:
            parsed = urlparse(self.path)
            path = parsed.path
            if path == "/api/catalog":
                body = self._read_json()
                selected = body.get("selected") or []
                if not isinstance(selected, list):
                    return self._json({"error": "selected must be a list"}, 400)
                clean: list[dict[str, str]] = []
                for item in selected:
                    if not isinstance(item, dict):
                        continue
                    clean.append({
                        "tag": str(item.get("tag") or ""),
                        "track": str(item.get("track") or ""),
                        "id": str(item.get("id") or ""),
                    })
                manifest = apply_selection(load_json(catalog_path), clean)
                catalog_path.write_text(
                    json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
                    encoding="utf-8",
                )
                return self._json({"ok": True, "selected": catalog_selected(manifest), "catalog": manifest})
            if path == "/api/export":
                query = parse_qs(urlparse(self.path).query)
                clean = query.get("clean", ["1"])[0] != "0"
                cmd = [
                    sys.executable,
                    str(SHOWCASE / "tools" / "export_showcase.py"),
                    "--source-root", str(source_root),
                    "--catalog", str(catalog_path),
                    "--output", str(SHOWCASE / "site"),
                ]
                if clean:
                    cmd.append("--clean")
                result = subprocess.run(cmd, capture_output=True, text=True, cwd=str(SHOWCASE))
                payload = {
                    "ok": result.returncode == 0,
                    "output": (result.stdout + result.stderr)[-4000:],
                }
                return self._json(payload, 200 if result.returncode == 0 else 500)
            return self.send_error(404)

    return Handler


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--catalog", type=Path, default=SHOWCASE / "catalog.json")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8777)
    args = parser.parse_args()
    if not PICKER_HTML.is_file():
        die(f"missing {PICKER_HTML}")
    source_root = args.source_root.resolve()
    catalog_path = args.catalog.resolve()
    if not catalog_path.is_file():
        die(f"missing catalog {catalog_path}")
    httpd = ThreadingHTTPServer((args.host, args.port), make_handler(source_root, catalog_path))
    print(f"picker  http://{args.host}:{args.port}/")
    print(f"source  {source_root}")
    print(f"catalog {catalog_path}")
    httpd.serve_forever()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
