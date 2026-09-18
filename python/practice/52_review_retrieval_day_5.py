# Practice 52 — review day 5: retrieval across six more lessons
# Run:  cd ~/learning/python && uv run python3 practice/52_review_retrieval_day_5.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# No new syntax here — every mechanism below was taught in Days 10, 14, 27,
# 31, 39, and 42. Replace each `...` (or the marked TODO body) and re-run
# until every check prints ✓. Try each from memory before reopening the old
# lesson.
#
# Exercise 1 tests the same *rule* Day 10 taught (loose constraint vs.
# pinned exact version) with a plain string-comparison function standing in
# for pyproject.toml vs. uv.lock, since parsing real TOML isn't the point of
# today's review — matching Day 49's precedent for topics whose original
# lesson used a file format or third-party tool rather than plain syntax.

from datetime import datetime, timezone
from itertools import groupby
import argparse


# ---------------------------------------------------------------------------
# Exercise 1 (Day 10 — pyproject.toml vs. uv.lock: loose constraint vs.
# exact pinned version)
# is_exact_pin(constraint) should return True if the constraint string is an
# exact pin (uses "==", the uv.lock shape) and False if it's a loose,
# human-editable constraint (">=", "~=", or no operator at all, the
# pyproject.toml shape).
def is_exact_pin(constraint):
    # TODO: return constraint.strip().startswith("==")
    ...


# ---------------------------------------------------------------------------
# Exercise 2 (Day 14 — datetime: naive vs. aware datetimes cannot be
# subtracted)
# subtract_or_none(a, b) should return (a - b) if that succeeds, or None if
# it raises TypeError (mixing a naive and an aware datetime). Catch ONLY
# TypeError — Day 8's narrow-catch habit, same as this review's own Day 39
# question about argparse.
def subtract_or_none(a, b):
    # TODO: try: return a - b
    #       except TypeError: return None
    ...


# ---------------------------------------------------------------------------
# Exercise 3 (Day 27 — itertools.groupby: consecutive runs only, sorted
# input required)
# group_by_city(rows) should use itertools.groupby (imported above) to group
# rows by their "city" key, returning a list of (city, [amounts]) tuples in
# the order groupby produces them. Do NOT sort the input yourself — the
# point is to see groupby's real behavior on whatever order it's given.
def group_by_city(rows):
    # TODO:
    #     return [
    #         (city, [r["amount"] for r in group])
    #         for city, group in groupby(rows, key=lambda r: r["city"])
    #     ]
    ...


# ---------------------------------------------------------------------------
# Exercise 4 (Day 31 — __hash__: a matching hand-written hash for an
# immutable-in-practice class)
# Ticket's fields never change after construction, so a hand-matched
# __hash__ is safe. Add __hash__ so two Tickets with the same `code` hash
# equal, matching __eq__'s own comparison.
class Ticket:
    def __init__(self, code):
        self.code = code

    def __eq__(self, other):
        if not isinstance(other, Ticket):
            return NotImplemented
        return self.code == other.code

    # TODO: def __hash__(self):
    #           return hash(self.code)


# ---------------------------------------------------------------------------
# Exercise 5 (Day 39 — argparse: bad input raises SystemExit, not a normal
# exception)
# build_parser() should return an ArgumentParser with one required
# positional argument "infile" and one optional "-n"/"--top" argument,
# type=int, default=5.
def build_parser():
    parser = argparse.ArgumentParser(prog="reviewtool")
    # TODO: parser.add_argument("infile")
    #       parser.add_argument("-n", "--top", type=int, default=5)
    ...
    return parser


# ---------------------------------------------------------------------------
# Exercise 6 (Day 42 — the walrus operator: one call site instead of two)
# Rewrite read_all(reader) to use a walrus inside its while condition,
# calling reader() exactly once per loop iteration (priming AND advancing
# in the same expression), collecting every non-empty chunk into a list.
# reader() returns "" when there's nothing left to read.
def read_all(reader):
    chunks = []
    # TODO:
    #     while (chunk := reader()) != "":
    #         chunks.append(chunk)
    ...
    return chunks


# ---------------------------------------------------------------------------
# Checks — don't edit below this line.
def check(name, cond):
    try:
        ok = bool(cond())
    except SystemExit:
        # argparse's own bad-input path (Ex 5) raises SystemExit, not a
        # normal Exception (Day 39) — catch it here too so an unfinished
        # build_parser() prints a clean ✗ instead of crashing this whole
        # script and skipping every check listed after it.
        ok = False
    except Exception:
        ok = False
    print(("✓" if ok else "✗"), name)
    return ok


def _ex2_naive_aware_mix_returns_none():
    naive = datetime(2026, 9, 18, 12, 0, 0)
    aware = datetime(2026, 9, 18, 12, 0, 0, tzinfo=timezone.utc)
    return subtract_or_none(aware, naive) is None


def _ex2_same_kind_subtracts_fine():
    a = datetime(2026, 9, 18, 15, 0, 0, tzinfo=timezone.utc)
    b = datetime(2026, 9, 18, 12, 0, 0, tzinfo=timezone.utc)
    result = subtract_or_none(a, b)
    return result is not None and result.total_seconds() == 10800.0


def _ex3_groupby_on_sorted_input():
    rows = [
        {"city": "Hanoi", "amount": 120},
        {"city": "Hanoi", "amount": 45},
        {"city": "HCMC", "amount": 80},
    ]
    return group_by_city(rows) == [("Hanoi", [120, 45]), ("HCMC", [80])]


def _ex3_groupby_splits_on_unsorted_input():
    # Same cities, but a Hanoi row now comes after an HCMC row — groupby
    # should report THREE groups, not two, since it never sorts for you.
    rows = [
        {"city": "Hanoi", "amount": 120},
        {"city": "HCMC", "amount": 80},
        {"city": "Hanoi", "amount": 45},
    ]
    return len(group_by_city(rows)) == 3


def _ex4_ticket_hashable_and_equal_hash():
    t1 = Ticket("A100")
    t2 = Ticket("A100")
    return (t1 == t2) and (hash(t1) == hash(t2)) and ({t1, t2} == {t1})


def _ex5_good_args_parse():
    parser = build_parser()
    args = parser.parse_args(["data.csv", "--top", "3"])
    return args.infile == "data.csv" and args.top == 3


def _ex5_default_applies():
    parser = build_parser()
    args = parser.parse_args(["data.csv"])
    return args.top == 5


def _ex5_bad_input_raises_system_exit():
    parser = build_parser()
    try:
        parser.parse_args(["data.csv", "--top", "not-a-number"])
        return False
    except SystemExit:
        return True
    except Exception:
        return False


def _ex6_read_all_collects_every_chunk():
    values = iter(["a", "b", "c", ""])

    def reader():
        return next(values)

    return read_all(reader) == ["a", "b", "c"]


results = [
    check("Ex 1: is_exact_pin tells a pinned '==' constraint from a loose one",
          lambda: is_exact_pin("==2.31.0") is True and is_exact_pin(">=0.27") is False),
    check("Ex 2: subtract_or_none returns None on a naive/aware mix, a timedelta otherwise",
          lambda: _ex2_naive_aware_mix_returns_none() and _ex2_same_kind_subtracts_fine()),
    check("Ex 3: group_by_city groups sorted input correctly, splits on unsorted input",
          lambda: _ex3_groupby_on_sorted_input() and _ex3_groupby_splits_on_unsorted_input()),
    check("Ex 4: Ticket.__hash__ matches __eq__, so equal tickets share one set slot",
          _ex4_ticket_hashable_and_equal_hash),
    check("Ex 5: build_parser() parses good input, applies defaults, raises SystemExit on bad input",
          lambda: _ex5_good_args_parse() and _ex5_default_applies() and _ex5_bad_input_raises_system_exit()),
    check("Ex 6: read_all uses a walrus to prime and advance in one call site",
          _ex6_read_all_collects_every_chunk),
]

print("\nAll green — lesson 52 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
