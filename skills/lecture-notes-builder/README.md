# Lecture notes builder

A Claude skill that merges a lecture transcript and the lecture slides into one exam-ready note, filed in the right Obsidian course folder.

Transcripts carry the explanation but ramble; slides carry the structure but say little. The skill walks the slides in order, pulls the matching stretch of transcript for each, keeps the lecturer's examples and anything they stressed, and drops the rest. Slides that were skipped stay in the note and are marked as such, and anything the recording garbled is flagged rather than guessed.

## Install

```bash
git clone https://github.com/Vidwaansinghania/Claude-Skills.git
cp -r Claude-Skills/skills/lecture-notes-builder ~/.claude/skills/
```

Works best with a Granola connector (to pull transcripts directly) and access to the vault folder.

## Using it

```
Write up today's Corporate Finance lecture. Slides are in Downloads/FIN2001_L6.pdf.
```

## What it returns

A note in the course folder with frontmatter, key takeaways, notes in lecture order, a definitions table, likely exam points, and open questions. It links back to the previous lecture, updates the course index, and matches whatever note style the folder already uses.

## Licence

MIT. See [LICENSE](../../LICENSE).
