# Timetable to ICS

A Claude skill that turns a timetable into an .ics calendar file, and won't hand it over until scripted checks show it matches the source.

Claude extracts the timetable into a structured spec and confirms it with you. A bundled script (Python standard library only) then generates the calendar. Each class occurrence becomes its own event in UTC, with the daylight-saving offset correct for that date, so clocks changing mid-term cannot shift a class. The script then re-reads the file it wrote, checks every event against the spec, and prints a PASS or FAIL summary with counts and first and last dates per class.

## Install

```bash
git clone https://github.com/Vidwaansinghania/Claude-Skills.git
cp -r Claude-Skills/skills/timetable-to-ics ~/.claude/skills/
```

## Using it

```
Turn this timetable into a calendar. Term runs 28 Sep to 11 Dec, reading week is week 6.
```

You can also run the script directly on a spec:

```bash
python3 ~/.claude/skills/timetable-to-ics/scripts/build_ics.py spec.json term1.ics
```

The spec format is documented at the top of `scripts/build_ics.py`.

## What it returns

An .ics file, a per-class summary table, overlap warnings, and a list of any assumptions. Import it into a separate calendar so it can be replaced cleanly if the timetable changes.

## Licence

MIT. See [LICENSE](../../LICENSE).
