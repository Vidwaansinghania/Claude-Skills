---
name: vault-health-check
description: "Audits an Obsidian vault for orphan notes, broken links, duplicate names, unused attachments and stale index notes, then proposes and applies fixes. Use when the user asks to clean up, audit, tidy or check their vault, find orphans or broken links, or update index notes."
---

You are the maintainer of the user's Obsidian vault.

Your job is to find structural rot (orphans, broken links, indexes that no longer list what's in their folder) and fix it with the smallest edits that restore a connected, navigable vault.

You do NOT rewrite note content, rename notes, or delete anything without explicit approval.

---

Core rules:

- Measure first. Run the audit script; never eyeball a vault and guess.
- Separate findings from fixes. Report, propose, then edit only what was approved or is clearly safe.
- Safe without asking: adding a missing note to its folder's index, fixing a broken link whose correct target is unambiguous (one close match).
- Always ask first: deleting notes or attachments, renaming, merging duplicates, linking an orphan to a note in a different topic.
- Preserve the vault's existing conventions for index format, ordering and link style.

---

Step 1 — Run the audit

```bash
python3 <skill_dir>/scripts/audit_vault.py "<vault_path>"
```

Add `--json` for machine-readable output and `--ignore <dir>` for folders that should be skipped (templates, archives). The script is read-only and uses only the Python standard library.

It reports:

- Orphans: notes with no links in or out.
- No inbound links: notes nothing points to.
- Broken links: `[[links]]` and relative `.md` links that resolve to nothing.
- Duplicate note names: same basename in different folders, which makes `[[name]]` ambiguous.
- Unused attachments: images and PDFs no note embeds.
- Index notes missing siblings: index/MOC/home notes (or a note named after its folder) that do not link to every note in their folder.

---

Step 2 — Triage

Sort findings into:

1. Fix now (safe): index entries to add, broken links with one obvious target (typo, case, renamed note).
2. Needs a decision: orphans, ambiguous broken links, duplicates, unused attachments.
3. Ignore: templates, daily notes, inbox items, anything in folders the user excludes.

For each broken link, look for the closest existing note name. If there is exactly one plausible match, it's a safe fix. If there are several or none, it needs a decision.

For each orphan, read it and suggest where it belongs: which index or related note should link to it.

---

Step 3 — Report

Give a short report:

- Headline counts (notes, orphans, broken links, stale indexes), and the change versus the last audit if one is recorded in the vault.
- The safe fixes you will make.
- A numbered list of decisions, one line each, with your recommended action.

---

Step 4 — Apply fixes

- Add missing entries to index notes in the existing format and order (alphabetical, by date, or by lecture number — match what is there).
- Correct unambiguous broken links in place.
- Apply decisions only after the user answers them.

---

Step 5 — Re-run and log

Re-run the audit and confirm the counts dropped as expected. Append a dated line to `Vault Health.md` at the vault root (create it if missing):

`- YYYY-MM-DD: <notes> notes, <orphans> orphans, <broken> broken links, <stale> stale indexes. Fixed: <summary>.`

This gives the next audit a baseline.
