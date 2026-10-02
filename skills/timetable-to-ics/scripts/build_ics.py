#!/usr/bin/env python3
"""Build and verify an .ics calendar from a structured timetable spec.

Usage: python3 build_ics.py <spec.json> <out.ics>

Each class occurrence becomes its own VEVENT with UTC times converted from the
spec's timezone, so daylight-saving changes and client RRULE quirks cannot
shift a class. The script then re-parses the file it wrote and checks it
against the spec. Exit code 1 means a check failed and the file must not be
used.

Spec format (JSON):
{
  "calendar_name": "Term 1 2026",
  "timezone": "Europe/London",
  "term_start": "2026-09-28",          # week 1 is the Mon-Sun week containing this
  "term_end": "2026-12-11",
  "skip_weeks": [6],                   # optional, week numbers with no classes
  "skip_dates": ["2026-11-05"],        # optional, single days with no classes
  "events": [
    {"title": "FIN2001 Lecture", "day": "MON", "start": "09:00", "end": "10:50",
     "location": "LT1", "weeks": [1,2,3,4,5,7,8,9,10,11],   # optional, default all
     "notes": "optional description"}
  ]
}
"""
import hashlib
import json
import re
import sys
from datetime import date, datetime, timedelta, timezone
from zoneinfo import ZoneInfo

DAYS = {"MON": 0, "TUE": 1, "WED": 2, "THU": 3, "FRI": 4, "SAT": 5, "SUN": 6}
errors, warnings = [], []


def fail(msg):
    errors.append(msg)


def esc(s):
    return s.replace("\\", "\\\\").replace(";", "\\;").replace(",", "\\,").replace("\n", "\\n")


def fold(line):
    out, b = [], line.encode()
    while len(b) > 75:
        cut = 75
        while (b[cut] & 0xC0) == 0x80:
            cut -= 1
        out.append(b[:cut].decode())
        b = b" " + b[cut:]
    out.append(b.decode())
    return "\r\n".join(out)


def parse_hm(s, where):
    if not re.fullmatch(r"\d{2}:\d{2}", s or ""):
        fail(f"{where}: time '{s}' is not HH:MM")
        return None
    h, m = map(int, s.split(":"))
    if h > 23 or m > 59:
        fail(f"{where}: time '{s}' is out of range")
        return None
    return h, m


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    spec = json.load(open(sys.argv[1]))
    try:
        tz = ZoneInfo(spec["timezone"])
    except Exception:
        sys.exit(f"Unknown timezone: {spec.get('timezone')}")
    t0 = date.fromisoformat(spec["term_start"])
    t1 = date.fromisoformat(spec["term_end"])
    if t1 < t0:
        sys.exit("term_end is before term_start")
    week1 = t0 - timedelta(days=t0.weekday())
    n_weeks = (t1 - week1).days // 7 + 1
    skip_weeks = set(spec.get("skip_weeks", []))
    skip_dates = {date.fromisoformat(d) for d in spec.get("skip_dates", [])}
    for d in skip_dates:
        if not t0 <= d <= t1:
            warnings.append(f"skip_date {d} is outside the term")

    occurrences = []  # (event_index, local_start, local_end)
    for i, ev in enumerate(spec["events"]):
        where = f"event {i + 1} '{ev.get('title', '?')}'"
        for k in ("title", "day", "start", "end"):
            if not ev.get(k):
                fail(f"{where}: missing '{k}'")
        day = DAYS.get(str(ev.get("day", "")).upper()[:3])
        if day is None:
            fail(f"{where}: day '{ev.get('day')}' not recognised")
        s, e = parse_hm(ev.get("start"), where), parse_hm(ev.get("end"), where)
        if day is None or not s or not e:
            continue
        if e <= s:
            fail(f"{where}: end {ev['end']} is not after start {ev['start']}")
            continue
        weeks = ev.get("weeks") or list(range(1, n_weeks + 1))
        for w in weeks:
            if not 1 <= w <= n_weeks:
                fail(f"{where}: week {w} is outside the term (1-{n_weeks})")
        for w in sorted(set(weeks) - skip_weeks):
            d = week1 + timedelta(weeks=w - 1, days=day)
            if d < t0 or d > t1 or d in skip_dates:
                continue
            ls = datetime(d.year, d.month, d.day, *s, tzinfo=tz)
            le = datetime(d.year, d.month, d.day, *e, tzinfo=tz)
            occurrences.append((i, ls, le))

    # Overlap check (warning: clashes can be real, but are usually typos)
    occ = sorted(occurrences, key=lambda o: o[1])
    for a, b in zip(occ, occ[1:]):
        if b[1] < a[2]:
            warnings.append(f"overlap on {a[1]:%a %Y-%m-%d}: '{spec['events'][a[0]]['title']}' "
                            f"{a[1]:%H:%M}-{a[2]:%H:%M} and '{spec['events'][b[0]]['title']}' "
                            f"{b[1]:%H:%M}-{b[2]:%H:%M}")

    if errors:
        report(spec, occurrences)
        sys.exit(1)

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    lines = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//claude-skills//timetable-to-ics//EN",
             "CALSCALE:GREGORIAN", "METHOD:PUBLISH", f"X-WR-CALNAME:{esc(spec.get('calendar_name', 'Timetable'))}",
             f"X-WR-TIMEZONE:{spec['timezone']}"]
    for i, ls, le in occurrences:
        ev = spec["events"][i]
        us, ue = ls.astimezone(timezone.utc), le.astimezone(timezone.utc)
        uid = hashlib.sha1(f"{ev['title']}|{ls.isoformat()}".encode()).hexdigest()[:20]
        lines += ["BEGIN:VEVENT", f"UID:{uid}@timetable-to-ics", f"DTSTAMP:{stamp}",
                  f"DTSTART:{us:%Y%m%dT%H%M%SZ}", f"DTEND:{ue:%Y%m%dT%H%M%SZ}",
                  f"SUMMARY:{esc(ev['title'])}"]
        if ev.get("location"):
            lines.append(f"LOCATION:{esc(ev['location'])}")
        if ev.get("notes"):
            lines.append(f"DESCRIPTION:{esc(ev['notes'])}")
        lines.append("END:VEVENT")
    lines.append("END:VCALENDAR")
    with open(sys.argv[2], "w", newline="") as fh:
        fh.write("\r\n".join(fold(l) for l in lines) + "\r\n")

    verify(sys.argv[2], spec, occurrences, tz)
    report(spec, occurrences)
    sys.exit(1 if errors else 0)


def verify(path, spec, occurrences, tz):
    """Re-parse the written file and check it matches the spec exactly."""
    raw = open(path, newline="").read()
    text = re.sub(r"\r\n ", "", raw)
    events = re.findall(r"BEGIN:VEVENT\r\n(.*?)END:VEVENT", text, re.S)
    if len(events) != len(occurrences):
        fail(f"file has {len(events)} events, expected {len(occurrences)}")
    uids = re.findall(r"^UID:(.*)$", text, re.M)
    if len(uids) != len(set(uids)):
        fail("duplicate UIDs in file")
    expected = {(spec["events"][i]["title"], ls.strftime("%Y-%m-%d %H:%M"), le.strftime("%H:%M"))
                for i, ls, le in occurrences}
    got = set()
    for ev in events:
        f = dict(re.findall(r"^([A-Z-]+):(.*?)\r?$", ev, re.M))
        ls = datetime.strptime(f["DTSTART"], "%Y%m%dT%H%M%SZ").replace(tzinfo=timezone.utc).astimezone(tz)
        le = datetime.strptime(f["DTEND"], "%Y%m%dT%H%M%SZ").replace(tzinfo=timezone.utc).astimezone(tz)
        title = re.sub(r"\\([\\;,])", r"\1", f["SUMMARY"]).replace("\\n", "\n")
        got.add((title, ls.strftime("%Y-%m-%d %H:%M"), le.strftime("%H:%M")))
    if got != expected:
        for x in sorted(expected - got):
            fail(f"missing from file: {x}")
        for x in sorted(got - expected):
            fail(f"unexpected in file: {x}")


def report(spec, occurrences):
    print(f"Calendar: {spec.get('calendar_name', 'Timetable')}  ({spec['timezone']})")
    print(f"Term: {spec['term_start']} to {spec['term_end']}\n")
    print(f"{'Event':<34} {'Day':<4} {'Time':<12} {'Count':>5}  First       Last")
    for i, ev in enumerate(spec["events"]):
        mine = [o for o in occurrences if o[0] == i]
        first = mine[0][1].strftime("%Y-%m-%d") if mine else "-"
        last = mine[-1][1].strftime("%Y-%m-%d") if mine else "-"
        print(f"{ev.get('title', '?')[:34]:<34} {str(ev.get('day', '?'))[:3]:<4} "
              f"{ev.get('start', '?')}-{ev.get('end', '?'):<6} {len(mine):>5}  {first}  {last}")
    print(f"\nTotal events: {len(occurrences)}")
    for w in warnings:
        print(f"WARNING: {w}")
    for e in errors:
        print(f"ERROR: {e}")
    print("\nRESULT: " + ("FAIL - do not use this file" if errors else "PASS"))


if __name__ == "__main__":
    main()
