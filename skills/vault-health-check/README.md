# Vault health check

A Claude skill that audits an Obsidian vault for structural rot and repairs it with the smallest safe edits.

It runs a bundled, read-only Python script (standard library only) that finds orphan notes, broken links, duplicate note names, unused attachments, and index notes that no longer list everything in their folder. The skill then makes the fixes that are unambiguous, like adding missing index entries and correcting obvious link typos. It asks before anything destructive or judgement-based, and logs a dated baseline so the next audit can show the trend.

## Install

```bash
git clone https://github.com/Vidwaansinghania/Claude-Skills.git
cp -r Claude-Skills/skills/vault-health-check ~/.claude/skills/
```

## Using it

```
Run a health check on my vault at ~/Obsidian/Main and fix what's safe.
```

You can also run the audit on its own:

```bash
python3 ~/.claude/skills/vault-health-check/scripts/audit_vault.py ~/Obsidian/Main --ignore Templates Archive
```

## What it returns

Headline counts, the safe fixes it made, a numbered list of decisions it needs from you, and a new line in `Vault Health.md` recording the result.

## Licence

MIT. See [LICENSE](../../LICENSE).
