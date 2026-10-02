# PDF to Profile note

A Claude skill that turns a long PDF (a personality report, assessment results or a study guide) into a short, cited note in your Obsidian Profile, merged with what the Profile already says.

It keeps scores, type codes and named traits exactly as the report states them and cites every claim to a page. It keeps its own synthesis in a separate, labelled section and says what kind of evidence the document is. When a new report contradicts an existing note, it flags the conflict instead of overwriting.

## Install

```bash
git clone https://github.com/Vidwaansinghania/Claude-Skills.git
cp -r Claude-Skills/skills/pdf-to-profile-note ~/.claude/skills/
```

## Using it

```
Add this Hogan report to my Profile.
```

## What it returns

A Profile note with frontmatter, summary, results table, condensed findings, practical implications, a labelled synthesis linking related notes, and caveats. It also adds the note to the Profile index, proposes edits to any summary notes, and lists conflicts with existing notes.

## Licence

MIT. See [LICENSE](../../LICENSE).
