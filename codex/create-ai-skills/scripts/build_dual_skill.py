#!/usr/bin/env python3
"""Generate Claude and Codex skill folders from a small JSON spec."""

import argparse
import json
import re
import shutil
import sys
from pathlib import Path


def hyphen_name(value):
    name = re.sub(r"[^a-z0-9]+", "-", value.strip().lower()).strip("-")
    name = re.sub(r"-{2,}", "-", name)
    if not name or len(name) > 64:
        raise ValueError("name must normalize to 1-64 lowercase letters, digits, or hyphens")
    return name


def yaml_quote(value):
    return json.dumps(str(value))


def write_text(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def copy_tree(source, dest):
    if not source:
        return
    src = Path(source).expanduser().resolve()
    if not src.exists():
        raise FileNotFoundError(f"resource path does not exist: {src}")
    if src.is_dir():
        shutil.copytree(src, dest, dirs_exist_ok=True)
    else:
        dest.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest / src.name)


def render_skill_md(spec):
    name = hyphen_name(spec["name"])
    title = spec.get("title") or " ".join(part.capitalize() for part in name.split("-"))
    description = spec["description"].strip()
    body = spec["body"].strip() + "\n"
    return (
        "---\n"
        f"name: {name}\n"
        f"description: {description}\n"
        "---\n\n"
        f"# {title}\n\n"
        f"{body}"
    )


def render_openai_yaml(spec, name):
    codex = spec.get("codex", {})
    display_name = codex.get("display_name") or spec.get("title") or name
    short_description = codex.get("short_description") or spec["description"][:64].rstrip()
    default_prompt = codex.get("default_prompt") or f"Use ${name} to help with this task."
    return (
        "interface:\n"
        f"  display_name: {yaml_quote(display_name)}\n"
        f"  short_description: {yaml_quote(short_description)}\n"
        f"  default_prompt: {yaml_quote(default_prompt)}\n"
    )


def generate(spec, out_dir):
    name = hyphen_name(spec["name"])
    skill_md = render_skill_md(spec)

    codex_dir = out_dir / "codex" / name
    claude_dir = out_dir / "claude" / name
    for target in (codex_dir, claude_dir):
        write_text(target / "SKILL.md", skill_md)

    write_text(codex_dir / "agents" / "openai.yaml", render_openai_yaml(spec, name))

    resources = spec.get("resources", {})
    for resource_name in ("scripts", "references", "assets"):
        copy_tree(resources.get(resource_name), codex_dir / resource_name)
        copy_tree(resources.get(resource_name), claude_dir / resource_name)

    return codex_dir, claude_dir


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("spec", type=Path, help="Path to the JSON skill spec")
    parser.add_argument("--out", type=Path, default=Path("dist"), help="Output directory")
    args = parser.parse_args()

    try:
        spec = json.loads(args.spec.read_text(encoding="utf-8"))
        codex_dir, claude_dir = generate(spec, args.out)
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    print(f"wrote {codex_dir}")
    print(f"wrote {claude_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
