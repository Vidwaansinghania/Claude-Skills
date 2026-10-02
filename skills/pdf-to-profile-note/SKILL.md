---
name: pdf-to-profile-note
description: "Ingests a PDF (personality or psychometric report, assessment results, study guide, career report) into a structured, cited Obsidian Profile note, and merges it with what the Profile already says. Use when the user shares a PDF about themselves or a study guide and wants it added to their vault or Profile."
---

You maintain the user's Profile: a set of Obsidian notes that capture who they are, how they work, and what they have learned about themselves.

Your job is to turn a long PDF into a short, structured note that keeps the substance, cites the source page for every claim, and fits alongside what the Profile already holds.

You do NOT flatter, generalise, or add interpretation the document does not support.

---

Core rules:

- Extract, don't paraphrase into mush. Keep scores, type codes, percentiles and named traits exactly as the report states them.
- Cite every claim to a page: `(p. 4)`.
- Separate what the document says from your synthesis. Synthesis goes in its own section and is labelled as such.
- Note the instrument's limits. A personality test is a self-report, a study guide is one author's view. Say what kind of evidence this is.
- When the new document conflicts with an existing Profile note, flag the conflict. Do not silently overwrite.
- Personal data stays in the vault. Do not paste it anywhere else.

---

Step 1 — Read the PDF

Read the whole document, including tables, charts and appendices. Record:

- Document type (e.g. personality assessment, aptitude test, study guide, career report).
- Issuer or author, date, and the instrument or framework (e.g. Big Five, MBTI, CliftonStrengths, Hogan).
- All quantitative results: scores, percentiles, rankings, type codes.
- The document's own key conclusions and recommendations.

If pages are scanned images, OCR them and say so.

---

Step 2 — Check the existing Profile

Look for a `Profile/` folder (or the user's equivalent) and its index note. Read related notes: earlier reports from the same instrument, other personality or strengths notes, any "How I work" note.

Match the existing file naming, frontmatter and heading style.

---

Step 3 — Write the note

Default template (override with the folder's existing style):

```markdown
---
type: profile-source
source: <document title>
issuer: <organisation or author>
instrument: <framework>
date: <YYYY-MM-DD of the report>
ingested: <YYYY-MM-DD>
file: "[[<pdf filename>]]"
tags: [profile, <instrument-tag>]
---

# <Instrument> — <short title>

## Summary
3 to 5 bullets. The most decision-relevant findings, each cited.

## Results
Table of every score or ranking as reported, with page references.

## What the report says
Sections mirroring the report's own structure, condensed. Cited.

## Practical implications
What the report recommends for study, work, career or relationships. Cited.

## Synthesis (my reading)
Clearly labelled. How this fits with other Profile notes, patterns across instruments, and where they disagree. Link the related notes.

## Caveats
What kind of evidence this is, its known limitations, and anything that looked inconsistent.
```

For a study guide rather than a self-assessment, replace Results with **Key concepts** and Practical implications with **How to use this**, and link to the relevant course folder.

---

Step 4 — Merge into the Profile

- Save the note in the Profile folder and attach or link the source PDF.
- Add it to the Profile index under the right heading.
- If the findings update a summary note (e.g. "Strengths" or "How I work"), propose the specific line edits and apply them only after the user agrees.
- List any conflicts with existing notes.

---

Step 5 — Report

Three lines: where the note was saved, the headline findings, and any conflicts or proposed edits that need a decision.
