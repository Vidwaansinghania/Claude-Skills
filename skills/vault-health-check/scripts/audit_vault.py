#!/usr/bin/env python3
"""Audit an Obsidian vault for orphan notes, broken links and stale index notes.

Usage: python3 audit_vault.py <vault_path> [--json] [--ignore DIR ...]

Read-only. Prints a report; never modifies the vault.
"""
import argparse
import json
import os
import re
import sys
from collections import defaultdict

WIKILINK = re.compile(r"(!?)\[\[([^\]|#^]+)(?:[#^][^\]|]*)?(?:\|[^\]]*)?\]\]")
MDLINK = re.compile(r"\[[^\]]*\]\((?!https?://|mailto:)([^)#\s]+\.md)(?:#[^)]*)?\)")
FENCE = re.compile(r"```.*?```", re.S)
INLINE_CODE = re.compile(r"`[^`\n]*`")
DEFAULT_IGNORE = {".obsidian", ".trash", ".git", "node_modules"}
INDEX_HINTS = ("index", "moc", "home", "readme", "dashboard")


def scan(vault, ignore):
    notes, attachments = {}, set()
    for root, dirs, files in os.walk(vault):
        dirs[:] = [d for d in dirs if d not in ignore and not d.startswith(".")]
        for f in files:
            rel = os.path.relpath(os.path.join(root, f), vault)
            if f.endswith(".md"):
                notes[rel] = None
            else:
                attachments.add(rel)
    return notes, attachments


def resolve(target, src, by_name, notes, attachments):
    """Resolve a link target the way Obsidian does: path, then basename."""
    target = target.strip()
    cands = [target, target + ".md", os.path.normpath(os.path.join(os.path.dirname(src), target))]
    for c in cands:
        if c in notes or c in attachments:
            return c
        if c + ".md" in notes:
            return c + ".md"
    base = os.path.basename(target)
    base = base[:-3] if base.endswith(".md") else base
    hits = by_name.get(base.lower())
    if hits:
        return hits[0]
    for a in attachments:
        if os.path.basename(a).lower() == os.path.basename(target).lower():
            return a
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("vault")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--ignore", nargs="*", default=[])
    args = ap.parse_args()
    vault = os.path.abspath(args.vault)
    if not os.path.isdir(vault):
        sys.exit(f"not a directory: {vault}")

    notes, attachments = scan(vault, DEFAULT_IGNORE | set(args.ignore))
    by_name = defaultdict(list)
    for n in notes:
        by_name[os.path.basename(n)[:-3].lower()].append(n)

    inbound = defaultdict(set)
    outbound = defaultdict(set)
    broken = []
    used_attachments = set()
    for n in notes:
        with open(os.path.join(vault, n), encoding="utf-8", errors="replace") as fh:
            text = fh.read()
        body = INLINE_CODE.sub("", FENCE.sub("", text))
        targets = [m.group(2) for m in WIKILINK.finditer(body)] + MDLINK.findall(body)
        for t in targets:
            hit = resolve(t, n, by_name, notes, attachments)
            if hit is None:
                broken.append({"note": n, "link": t})
            elif hit in notes:
                if hit != n:
                    inbound[hit].add(n)
                    outbound[n].add(hit)
            else:
                used_attachments.add(hit)

    orphans = sorted(n for n in notes if not inbound[n] and not outbound[n])
    no_inbound = sorted(n for n in notes if not inbound[n] and outbound[n])
    dup_names = {k: v for k, v in by_name.items() if len(v) > 1}
    unused = sorted(a for a in attachments if a not in used_attachments
                    and os.path.splitext(a)[1].lower() in {".png", ".jpg", ".jpeg", ".gif", ".pdf", ".svg", ".webp"})
    indexes = [n for n in notes if any(h in os.path.basename(n).lower() for h in INDEX_HINTS)
               or os.path.basename(n)[:-3] == os.path.basename(os.path.dirname(n))]
    stale = []
    for idx in indexes:
        folder = os.path.dirname(idx)
        siblings = [n for n in notes if os.path.dirname(n) == folder and n != idx]
        missing = sorted(s for s in siblings if s not in outbound[idx])
        if missing:
            stale.append({"index": idx, "missing": missing})

    report = {
        "vault": vault,
        "notes": len(notes),
        "attachments": len(attachments),
        "orphans": orphans,
        "no_inbound_links": no_inbound,
        "broken_links": broken,
        "duplicate_names": dup_names,
        "unused_attachments": unused,
        "stale_indexes": stale,
    }
    if args.json:
        print(json.dumps(report, indent=2))
        return
    print(f"Vault: {vault}\nNotes: {len(notes)}  Attachments: {len(attachments)}\n")
    for key, label in [("orphans", "Orphans (no links in or out)"),
                       ("no_inbound_links", "No inbound links"),
                       ("unused_attachments", "Unused attachments")]:
        print(f"## {label}: {len(report[key])}")
        for x in report[key]:
            print(f"  - {x}")
    print(f"## Broken links: {len(broken)}")
    for b in broken:
        print(f"  - {b['note']} -> [[{b['link']}]]")
    print(f"## Duplicate note names: {len(dup_names)}")
    for k, v in dup_names.items():
        print(f"  - {k}: {', '.join(v)}")
    print(f"## Index notes missing siblings: {len(stale)}")
    for s in stale:
        print(f"  - {s['index']}: {len(s['missing'])} missing")
        for m in s["missing"]:
            print(f"      {m}")


if __name__ == "__main__":
    main()
