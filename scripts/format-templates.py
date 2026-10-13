#!/usr/bin/env python3
"""Sort Docker template keys into the canonical order and format them consistently.

Usage:
  scripts/format-templates.py          # rewrite docker/*.json in place
  scripts/format-templates.py --check  # only report files that need formatting
"""

import json
import sys
from pathlib import Path

KEY_ORDER = [
    # what it is
    "name", "description", "category", "icon",
    # links
    "project", "readme_url", "support",
    # image
    "repo", "registry", "architecture",
    # runtime
    "network", "custom_ip", "privileged", "default_shell", "no_autoupdate",
    "extra_parameters", "post_parameters", "web_ui_url",
    # mappings
    "paths", "ports", "variables", "devices", "labels", "gpus",
]


def render(value, indent=0):
    pad = "  " * indent
    if isinstance(value, dict):
        if not value:
            return "{}"
        items = [f'{pad}  {json.dumps(k)}: {render(v, indent + 1)}' for k, v in value.items()]
        return "{\n" + ",\n".join(items) + f"\n{pad}}}"
    if isinstance(value, list):
        if not value:
            return "[]"
        # Lists of scalars stay on one line: [ "amd64", "arm64" ]
        if all(not isinstance(v, (dict, list)) for v in value):
            return "[ " + ", ".join(json.dumps(v, ensure_ascii=False) for v in value) + " ]"
        items = [f"{pad}  {render(v, indent + 1)}" for v in value]
        return "[\n" + ",\n".join(items) + f"\n{pad}]"
    return json.dumps(value, ensure_ascii=False)


def format_template(path):
    data = json.loads(path.read_text())
    unknown = [k for k in data if k not in KEY_ORDER]
    if unknown:
        print(f"{path}: unknown keys kept at the end: {', '.join(unknown)}", file=sys.stderr)
    ordered = {k: data[k] for k in KEY_ORDER if k in data}
    ordered.update({k: data[k] for k in unknown})
    return render(ordered) + "\n"


def main():
    check = "--check" in sys.argv[1:]
    root = Path(__file__).resolve().parent.parent
    dirty = []
    for path in sorted((root / "docker").glob("*.json")):
        formatted = format_template(path)
        if path.read_text() != formatted:
            dirty.append(path.relative_to(root))
            if not check:
                path.write_text(formatted)
    for path in dirty:
        print(f"{'needs formatting' if check else 'formatted'}: {path}")
    return 1 if check and dirty else 0


if __name__ == "__main__":
    sys.exit(main())
