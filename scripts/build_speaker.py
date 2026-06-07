#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Convert speaker files in speaker/*.md into 学术报告 posts under content/post/,
matching the site's current post format (see content/post/2023-07-29_CXY.md).

The site is built from source by Netlify (Hugo, Blackfriday), so this script only
needs to emit a correct content/post/*.md; Netlify rebuilds and deploys.

Run:  python3 scripts/build_speaker.py
Idempotent: re-running regenerates the same output from the same input.
"""

import os
import re
import sys
import glob

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required.")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SPEAKER_DIR = os.path.join(ROOT, "speaker")
POST_DIR = os.path.join(ROOT, "content", "post")
SKIP = {"README.md", "TEMPLATE.md"}

IMAGE_REPO = os.environ.get("CGM_IMAGE_REPO", "cgmonline/cgmonline")
FRONT_MATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", re.DOTALL)


def parse_file(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    m = FRONT_MATTER_RE.match(text)
    if not m:
        raise ValueError(f"{path}: missing YAML front matter (--- ... ---)")
    return yaml.safe_load(m.group(1)) or {}, m.group(2).strip()


def split_sections(body):
    sections, current, buf = {}, None, []
    for line in body.splitlines():
        h = re.match(r"^#{1,6}\s+(.*\S)\s*$", line)
        if h:
            if current is not None:
                sections[current] = "\n".join(buf).strip()
            current, buf = h.group(1).strip(), []
        else:
            buf.append(line)
    if current is not None:
        sections[current] = "\n".join(buf).strip()
    return sections


def pick(sections, *aliases):
    for a in aliases:
        for k, v in sections.items():
            if k.replace(" ", "").lower() == a.replace(" ", "").lower():
                return v
    return ""


def require(fm, path, *keys):
    missing = [k for k in keys if not fm.get(k)]
    if missing:
        raise ValueError(f"{path}: missing required field(s): {', '.join(missing)}")


def image_block(fm):
    photo = fm.get("photo")
    if not photo:
        return ""
    url = photo if str(photo).startswith("http") else \
        f"https://github.com/{IMAGE_REPO}/blob/master/image/{photo}?raw=true"
    return f'<div align="center">\n<img src="{url}" height=250>\n</div>'


def render_post(fm, sections):
    date = str(fm["date"]).split()[0]            # YYYY-MM-DD
    y, m, d = date.split("-")
    title = str(fm["title"]).strip()
    keywords = [str(k).strip() for k in (fm.get("keywords") or [])]
    bio = pick(sections, "主讲人简介", "主讲人", "嘉宾介绍", "Bio", "Speaker")
    abstract = pick(sections, "中文摘要", "摘要", "Abstract")

    out = []
    out.append("---")
    out.append(f"title: '{m}-{d}-{y} {title}'")
    out.append(f"date: '{date}'")
    out.append(f'archive: ["{y}", "{y}-{m}", "{date}"]')
    out.append("categories:")
    out.append("  - 学术报告")
    out.append("tags: [" + ", ".join(keywords) + "]")
    out.append("show_comments: true")
    out.append('thumbnail: ""')
    out.append("---")
    out.append("")
    out.append(f"- **题目**：{title}")
    if fm.get("location"):
        out.append(f"- **地点**：{fm['location']}")
    if fm.get("time"):
        out.append(f"- **时间**：{fm['time']}")
    if fm.get("zoom_link"):
        out.append(f"- **ZOOM会议链接**：[点击进入]({fm['zoom_link']})")
    out.append(f"- **主讲人**：{fm['speaker']}")
    if fm.get("affiliation"):
        out.append(f"  - 所属机构：{fm['affiliation']}")
    if fm.get("position"):
        out.append(f"  - 职称：{fm['position']}")
    if bio:
        # indent the bio so it nests under 主讲人, matching the current format
        out.append("  - 简介：" + bio.replace("\n", " "))
    img = image_block(fm)
    if img:
        out.append("")
        out.append(img)
    if abstract:
        out.append("")
        out.append("# 中文摘要")
        out.append("")
        out.append(abstract)
    if fm.get("references"):
        out.append("")
        out.append("# 参考文献")
        out.append("")
        out.append("- " + str(fm["references"]).strip())
    if keywords:
        out.append("")
        out.append("# 关键词")
        out.append("")
        out.append("- " + ", ".join(keywords))
    out.append("")
    return "\n".join(out), date


def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    print(f"  wrote {os.path.relpath(path, ROOT)}")


def main():
    files = sorted(p for p in glob.glob(os.path.join(SPEAKER_DIR, "*.md"))
                   if os.path.basename(p) not in SKIP)
    if not files:
        print("No speaker/*.md files to process.")
        return
    errors = []
    for path in files:
        rel = os.path.relpath(path, ROOT)
        print(f"Processing {rel}")
        try:
            fm, body = parse_file(path)
            require(fm, rel, "title", "speaker", "date", "slug")
            content, date = render_post(fm, split_sections(body))
            write(os.path.join(POST_DIR, f"{date}_{fm['slug']}.md"), content)
        except Exception as e:  # noqa: BLE001
            errors.append(str(e))
            print(f"  ERROR: {e}", file=sys.stderr)
    if errors:
        sys.exit(f"\n{len(errors)} file(s) failed.")
    print("Done.")


if __name__ == "__main__":
    main()
