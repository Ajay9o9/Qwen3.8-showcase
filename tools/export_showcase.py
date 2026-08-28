#!/usr/bin/env python3
"""Export selected benchmark HTML artifacts into the public showcase site."""
from __future__ import annotations
import argparse, json, re, shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

TRACKS = ("web",)

# Retry / concurrency folders that are the same model run.
TAG_GROUPS = {
    "qwen38-27b-q4_k_m-thinking": (
        "qwen38-27b-q4_k_m-thinking",
        "qwen38-27b-q4_k_m-thinking-np3",
    ),
}
_CANONICAL_TAG = {
    alias: canon
    for canon, aliases in TAG_GROUPS.items()
    for alias in aliases
}


def canonical_tag(tag: str) -> str:
    return _CANONICAL_TAG.get(tag, tag)


def tag_folders(tag: str) -> tuple[str, ...]:
    canon = canonical_tag(tag)
    return TAG_GROUPS.get(canon, (canon,))

def die(message: str) -> None:
    raise SystemExit(f"export error: {message}")

def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        die(f"missing {path}")
    except json.JSONDecodeError as exc:
        die(f"invalid JSON in {path}: {exc}")
    if not isinstance(value, dict):
        die(f"expected an object in {path}")
    return value

def safe_slug(value: str) -> str:
    original = value
    value = re.sub(r"^(web|three)_", "", value)
    value = re.sub(r"[^a-zA-Z0-9]+", "-", value).strip("-").lower()
    if not value:
        die(f"cannot make URL slug from {original!r}")
    return value

def safe_relative(value: str) -> Path:
    path = Path(value)
    if path.is_absolute() or ".." in path.parts:
        die(f"unsafe relative path: {value!r}")
    return path

def record_map(run: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {str(item.get("id")): item for item in run.get("results", []) if item.get("id")}

def title_for(task_id: str, record: dict[str, Any]) -> str:
    grade, legacy = record.get("grade") or {}, record.get("legacy") or {}
    title = grade.get("title") or legacy.get("title")
    return str(title) if title else safe_slug(task_id).replace("-", " ").title()

def task_record(track: str, task_id: str, records: dict[str, dict[str, Any]]) -> dict[str, Any]:
    record, grade = records.get(task_id, {}), records.get(task_id, {}).get("grade") or {}
    return {"id": task_id, "title": title_for(task_id, record),
            "track": track}

def copy_one(src: Path, dst: Path) -> None:
    if not src.is_file(): die(f"missing selected artifact: {src}")
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)

def export_track(source_root: Path, site_root: Path, entry: dict[str, Any], track: str) -> list[dict[str, Any]]:
    config = (entry.get("sources") or {}).get(track)
    if not config: return []
    tag = canonical_tag(str(config.get("tag", "")).strip())
    if not tag: die(f"{entry.get('id')}: {track} source has no tag")
    folders = [source_root / "results" / safe_relative(name) for name in tag_folders(tag)]
    records: dict[str, dict[str, Any]] = {}
    for folder in folders:
        run_path = folder / f"{track}.json"
        if run_path.is_file():
            records.update(record_map(load_json(run_path)))
    selected = config.get("tasks", "all")
    prefix = "web_" if track == "web" else "three_"
    if selected == "all":
        stems: set[str] = set()
        for folder in folders:
            stems.update(path.stem for path in folder.glob(f"{prefix}*.html"))
        task_ids = sorted(stems)
    elif isinstance(selected, list):
        task_ids = [str(task) for task in selected]
    else:
        die(f"{entry.get('id')}: {track}.tasks must be 'all' or a list")
    allowed_dirs = {folder.resolve() for folder in folders}
    output, seen = [], set()
    for task_id in task_ids:
        task_stem = Path(task_id).stem
        if task_stem in seen: die(f"{entry.get('id')}: duplicate {track} task {task_id}")
        seen.add(task_stem)
        html_path = None
        source_dir = None
        for folder in folders:
            candidate = folder / safe_relative(f"{task_stem}.html")
            if candidate.is_file():
                html_path, source_dir = candidate, folder
                break
        if html_path is None or source_dir is None:
            die(f"{entry.get('id')}: missing {track} html for {task_stem} under {tag}")
        if html_path.resolve().parent not in allowed_dirs:
            die(f"{entry.get('id')}: task must be in source root: {task_id!r}")
        slug = safe_slug(task_stem)
        destination = site_root / "demos" / safe_slug(str(entry["id"])) / track / f"{slug}.html"
        copy_one(html_path, destination)
        item = task_record(track, task_stem, records)
        item.update({"url": destination.relative_to(site_root).as_posix(), "source_tag": source_dir.name})
        shots = []
        for kind in ("desktop", "mobile"):
            source_shot = source_dir / "web-shots" / task_stem / f"{kind}.png"
            if source_shot.is_file():
                shot_destination = site_root / "screenshots" / safe_slug(str(entry["id"])) / track / slug / f"{kind}.png"
                copy_one(source_shot, shot_destination)
                shots.append({"kind": kind, "url": shot_destination.relative_to(site_root).as_posix()})
        item["screenshots"] = shots
        output.append(item)
    return output

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, required=True)
    parser.add_argument("--catalog", type=Path, default=Path("catalog.json"))
    parser.add_argument("--output", type=Path, default=Path("site"))
    parser.add_argument("--clean", action="store_true")
    args = parser.parse_args()
    manifest = load_json(args.catalog)
    entries = manifest.get("entries")
    if not isinstance(entries, list) or not entries: die("catalog.json needs a non-empty entries list")
    site_root = args.output.resolve(); site_root.mkdir(parents=True, exist_ok=True)
    if args.clean:
        for name in ("demos", "screenshots"):
            target = site_root / name
            if target.exists(): shutil.rmtree(target)
    models, ids = [], set()
    for entry in entries:
        if not isinstance(entry, dict) or not entry.get("id"): die("each entry needs an id")
        entry_id = str(entry["id"])
        if entry_id in ids: die(f"duplicate entry id {entry_id}")
        ids.add(entry_id)
        tracks = {track: export_track(args.source_root.resolve(), site_root, entry, track) for track in TRACKS}
        models.append({"id": entry_id, "name": entry.get("name", entry_id), "version": entry.get("version", ""),
                       "quant": entry.get("quant", ""), "label": entry.get("label", entry_id),
                       "notes": entry.get("notes", ""), "tracks": tracks})
    generated = {"schema_version": 1, "generated_at": datetime.now(timezone.utc).isoformat(),
                 "title": manifest.get("title", "Qwen Showcase"), "description": manifest.get("description", ""),
                 "models": models}
    (site_root / "catalog.json").write_text(json.dumps(generated, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    count = sum(len(model["tracks"][track]) for model in models for track in TRACKS)
    print(f"exported {count} demos for {len(models)} model entries into {site_root}")

if __name__ == "__main__":
    main()
