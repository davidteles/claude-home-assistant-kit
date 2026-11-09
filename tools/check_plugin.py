"""Check the plugin manifests and that every skill and command has front matter
with a description, and that no skill and command share a name."""
import glob
import json
import sys

import yaml

errors = []
plugin = json.load(open(".claude-plugin/plugin.json"))
market = json.load(open(".claude-plugin/marketplace.json"))
for key in ("name", "version", "description"):
    if not plugin.get(key):
        errors.append(f"plugin.json: {key} is missing")
if plugin.get("name") not in {p.get("name") for p in market.get("plugins", [])}:
    errors.append("marketplace.json does not list the plugin")

names = {}
for path in sorted(glob.glob("skills/*/SKILL.md") + glob.glob("commands/*.md")):
    text = open(path, encoding="utf-8").read()
    if not text.startswith("---\n"):
        errors.append(f"{path}: no front matter")
        continue
    meta = yaml.safe_load(text.split("---\n", 2)[1]) or {}
    if not meta.get("description"):
        errors.append(f"{path}: no description")
    name = meta.get("name") or path.split("/")[-2 if path.startswith("skills/") else -1].removesuffix(".md")
    if name in names:
        errors.append(f"{path}: '{name}' is also {names[name]}")
    names[name] = path

print(f"{len(names)} skills and commands checked")
for error in errors:
    print("ERROR", error)
sys.exit(1 if errors else 0)
