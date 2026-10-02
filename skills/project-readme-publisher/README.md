# Project README publisher

A Claude skill that turns a project's Obsidian notes into tab-style GitHub documentation and publishes it through a pull request.

The README is the landing tab: what the project is, why it matters and how to use it. Longer material (methodology, results, data notes) goes in linked `docs/` pages with a shared navigation bar, so the repo reads like a small tabbed site. The skill converts Obsidian-only syntax (wikilinks, embeds, callouts, Dataview) into Markdown that GitHub renders, strips private material, and flags anything it inferred rather than read. It always publishes on a branch with a PR and never pushes to main.

## Install

```bash
git clone https://github.com/Vidwaansinghania/Claude-Skills.git
cp -r Claude-Skills/skills/project-readme-publisher ~/.claude/skills/
```

## Using it

```
Publish my Congress Trading Monitor project from the vault to GitHub with a proper README.
```

## What it returns

A README, `docs/` pages and assets on a new branch, a pull request link, and a list of anything inferred, removed or unresolved for you to check before merging.

## Licence

MIT. See [LICENSE](../../LICENSE).
