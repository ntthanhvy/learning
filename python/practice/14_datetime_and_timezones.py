# Practice 14 — datetime & timezones
# Run:  cd ~/learning/python && uv run python3 practice/14_datetime_and_timezones.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓.

from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo


# ---------------------------------------------------------------------------
# Exercise 1 — build an aware UTC datetime.
# Given year/month/day/hour/minute (all ints), return an AWARE datetime
# anchored to UTC — do NOT use datetime.now(), build it from the given pieces
# with tzinfo=timezone.utc.
def make_utc_datetime(year, month, day, hour, minute):
    ...                              # TODO:
    # return datetime(year, month, day, hour, minute, tzinfo=timezone.utc)


# ---------------------------------------------------------------------------
# Exercise 2 — timedelta arithmetic.
# Given an aware datetime `start` and an int `days`, return the datetime
# `days` days after `start`, using timedelta — do NOT compute this by hand
# with a fixed number of seconds.
def days_later(start, days):
    ...                              # TODO:
    # return start + timedelta(days=days)


# ---------------------------------------------------------------------------
# Exercise 3 — naive vs. aware comparison raises TypeError.
# Given an aware datetime `aware_dt` and a naive datetime `naive_dt`, return
# True if subtracting naive_dt from aware_dt raises TypeError, False if it
# doesn't raise anything. Use try/except — do not just assume the answer.
def subtracting_raises_type_error(aware_dt, naive_dt):
    ...                              # TODO:
    # try:
    #     aware_dt - naive_dt
    #     return False
    # except TypeError:
    #     return True


# ---------------------------------------------------------------------------
# Exercise 4 — isoformat() / fromisoformat() round trip.
# Given an aware datetime, convert it to an ISO string with .isoformat(),
# then parse that string back with datetime.fromisoformat(), and return the
# parsed result — it should equal the original datetime exactly.
def iso_round_trip(dt):
    ...                              # TODO:
    # text = dt.isoformat()
    # return datetime.fromisoformat(text)


# ---------------------------------------------------------------------------
# Exercise 5 — convert an aware datetime to a named zone with zoneinfo.
# Given an aware UTC datetime and a zone name string (e.g. "Asia/Ho_Chi_Minh"),
# return the same instant re-expressed in that zone via .astimezone().
def convert_to_zone(utc_dt, zone_name):
    ...                              # TODO:
    # return utc_dt.astimezone(ZoneInfo(zone_name))


# ---------------------------------------------------------------------------
# Checks — don't edit below this line.
def check(name, cond):
    try:
        ok = bool(cond())
    except Exception:
        ok = False
    print(("✓" if ok else "✗"), name)
    return ok


_aware_ref = datetime(2026, 8, 11, 15, 0, 0, tzinfo=timezone.utc)
_naive_ref = datetime(2026, 8, 11, 15, 0, 0)

results = [
    check("Ex 1: make_utc_datetime() builds an aware UTC datetime",
          lambda: make_utc_datetime(2026, 8, 11, 15, 0) == _aware_ref
          and make_utc_datetime(2026, 8, 11, 15, 0).tzinfo is not None),
    check("Ex 2: days_later() shifts a datetime forward by N days via timedelta",
          lambda: days_later(_aware_ref, 7) == _aware_ref + timedelta(days=7)),
    check("Ex 3: subtracting_raises_type_error() detects the naive/aware TypeError",
          lambda: subtracting_raises_type_error(_aware_ref, _naive_ref) is True
          and subtracting_raises_type_error(_aware_ref, _aware_ref) is False),
    check("Ex 4: iso_round_trip() preserves the datetime through isoformat()/fromisoformat()",
          lambda: iso_round_trip(_aware_ref) == _aware_ref),
    check("Ex 5: convert_to_zone() re-expresses the same instant in a named zone",
          lambda: convert_to_zone(_aware_ref, "Asia/Ho_Chi_Minh") == _aware_ref
          and convert_to_zone(_aware_ref, "Asia/Ho_Chi_Minh").utcoffset() == timedelta(hours=7)),
]

print("\nAll green — lesson 14 done!" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
