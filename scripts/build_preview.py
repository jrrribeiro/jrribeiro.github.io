"""Build a dependency-light local preview of the Jekyll site.

This helper mirrors the site's Liquid/layout pipeline closely enough for visual
review on machines where Ruby's native build toolchain is not available. The
published site continues to be built by GitHub Pages/Jekyll.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml
from liquid import Environment, FileSystemLoader


ROOT = Path(__file__).resolve().parents[1]


def normalize_jekyll_liquid(source: str) -> str:
    """Quote Jekyll's static include names for python-liquid."""
    return re.sub(
        r"({%\s*include\s+)([A-Za-z0-9_.-]+)(\s*%})",
        r"\1'\2'\3",
        source,
    )


class JekyllIncludeLoader(FileSystemLoader):
    def get_source(self, env: Environment, template_name: str, **kwargs: Any):
        template_source = super().get_source(env, template_name, **kwargs)
        return template_source._replace(text=normalize_jekyll_liquid(template_source.text))


def split_front_matter(path: Path) -> tuple[dict[str, Any], str]:
    source = path.read_text(encoding="utf-8-sig").replace("\r\n", "\n")
    if not source.startswith("---\n"):
        return {}, source
    _, raw_metadata, body = source.split("---\n", 2)
    return yaml.safe_load(raw_metadata) or {}, body


def load_data() -> dict[str, Any]:
    data: dict[str, Any] = {}
    for path in sorted((ROOT / "_data").glob("*.yml")):
        data[path.stem] = yaml.safe_load(path.read_text(encoding="utf-8"))
    return data


def output_path(destination: Path, permalink: str) -> Path:
    clean = permalink.split("?", 1)[0].split("#", 1)[0]
    if clean.endswith("/"):
        return destination / clean.lstrip("/") / "index.html"
    return destination / clean.lstrip("/")


def build(destination: Path) -> None:
    config = yaml.safe_load((ROOT / "_config.yml").read_text(encoding="utf-8")) or {}
    config["baseurl"] = ""
    config["url"] = "http://localhost:4000"
    config["time"] = datetime.now(timezone.utc)
    config["data"] = load_data()

    source_paths = [ROOT / "index.html", ROOT / "404.html"]
    excluded_roots = {".git", ".preview", "_includes", "_layouts", "assets", "scripts"}
    source_paths.extend(
        sorted(
            path for path in ROOT.rglob("index.html")
            if path != ROOT / "index.html"
            and path.relative_to(ROOT).parts[0] not in excluded_roots
        )
    )
    source_paths.extend([ROOT / "robots.txt", ROOT / "sitemap.xml"])

    documents: list[tuple[Path, dict[str, Any], str]] = []
    site_pages: list[dict[str, Any]] = []
    for path in source_paths:
        metadata, body = split_front_matter(path)
        permalink = metadata.get("permalink")
        if not permalink:
            relative = path.relative_to(ROOT).as_posix()
            permalink = "/" + relative.replace("index.html", "")
        metadata["url"] = permalink
        metadata["path"] = path.relative_to(ROOT).as_posix()
        documents.append((path, metadata, body))
        if path.name not in {"robots.txt", "sitemap.xml"}:
            site_pages.append(metadata.copy())
    config["pages"] = site_pages

    environment = Environment(loader=JekyllIncludeLoader(ROOT / "_includes"))

    def relative_url(value: Any) -> str:
        text = str(value or "")
        if "://" in text or text.startswith("mailto:"):
            return text
        return "/" + text.lstrip("/")

    def absolute_url(value: Any) -> str:
        text = relative_url(value)
        if "://" in text:
            return text
        return config["url"].rstrip("/") + text

    def strip_html(value: Any) -> str:
        return re.sub(r"<[^>]*>", "", str(value or ""))

    def strip_newlines(value: Any) -> str:
        return str(value or "").replace("\r", "").replace("\n", "")

    def jsonify(value: Any) -> str:
        return json.dumps(value, ensure_ascii=False, separators=(",", ":"), default=str)

    def date_filter(value: Any, pattern: str = "%Y-%m-%d") -> str:
        if isinstance(value, (datetime,)):
            return value.strftime(pattern)
        return str(value or "")

    def date_to_xmlschema(value: Any) -> str:
        if isinstance(value, datetime):
            return value.isoformat()
        return str(value or "")

    environment.add_filter("relative_url", relative_url)
    environment.add_filter("absolute_url", absolute_url)
    environment.add_filter("strip_html", strip_html)
    environment.add_filter("strip_newlines", strip_newlines)
    environment.add_filter("jsonify", jsonify)
    environment.add_filter("date", date_filter)
    environment.add_filter("date_to_xmlschema", date_to_xmlschema)
    environment.add_filter("xml_escape", lambda value: html.escape(str(value or ""), quote=True))

    if destination == ROOT or not destination.is_relative_to(ROOT):
        raise ValueError("Preview destination must be a subdirectory of the repository")
    if destination.exists():
        shutil.rmtree(destination)
    destination.mkdir(parents=True)
    shutil.copytree(ROOT / "assets", destination / "assets")

    def render(source: str, page: dict[str, Any], content: str = "") -> str:
        source = normalize_jekyll_liquid(source)
        return environment.from_string(source).render(site=config, page=page, content=content)

    for _, page, body in documents:
        rendered = render(body, page)
        layout_name = page.get("layout")
        while layout_name:
            layout_metadata, layout_body = split_front_matter(ROOT / "_layouts" / f"{layout_name}.html")
            rendered = render(layout_body, page, rendered)
            layout_name = layout_metadata.get("layout")
        target = output_path(destination, page["url"])
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(rendered, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--destination", type=Path, default=ROOT / ".preview")
    args = parser.parse_args()
    build(args.destination.resolve())
    print(f"Preview built at {args.destination.resolve()}")
