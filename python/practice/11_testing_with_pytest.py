# Practice 11 — Testing with pytest
# Run:  cd ~/learning/python && uv run --with pytest pytest practice/11_testing_with_pytest.py -v
#
# The ONE deliberate exception to "standard library only" in this course:
# pytest is third-party, installed ad hoc via `uv run --with pytest` (no
# pyproject.toml exists yet in this course, so this is Day 10's "one-off
# dependency, no file changes" case, not `uv add`).
#
# Unlike every prior practice file, this one does NOT use a hand-rolled
# check()/✓/✗ tally — pytest already reports pass/fail per test far better
# than that idiom can (see lesson section 5), so today adopts pytest's own
# reporting instead of reinventing it. Replace each TODO and re-run until
# `pytest` reports "X passed" with no failures.
#
# Builds on Day 8's safe_int()/extract() shape — same functions, pytest-ified.

import tempfile
from pathlib import Path

import pytest


# ---------------------------------------------------------------------------
# Code under test — this would normally live in its own module (e.g.
# parsing.py) and be imported by the test file, per Day 9's lesson. Kept in
# one file here only to keep this practice self-contained.
def safe_int(text):
    try:
        return int(text)
    except ValueError:
        return None


def extract(csv_path):
    import csv
    with open(csv_path, newline="") as f:
        for row in csv.DictReader(f):
            amount = safe_int(row["amount"])
            if amount is not None:
                yield {"city": row["city"], "amount": amount}


# ---------------------------------------------------------------------------
# Exercise 1 — a plain assert test, no fixture needed.
# Write a test (name must start with test_) asserting safe_int("42") == 42.
# TODO: replace the line below with a real assert.
def test_safe_int_parses_a_valid_number():
    assert False, "TODO: assert safe_int('42') == 42"


# ---------------------------------------------------------------------------
# Exercise 2 — a fixture with setup only (no teardown needed for a temp file).
# Fill in the fixture body: create a temp dir, write a small CSV with a
# header row "city,amount" and two data rows, yield the Path to that file.
@pytest.fixture
def sales_csv():
    tmp = Path(tempfile.mkdtemp(prefix="py11_"))
    path = tmp / "sales.csv"
    raise NotImplementedError(       # TODO: delete this line, then uncomment:
        "fill in sales_csv() — write the CSV and yield its path")
    # path.write_text("city,amount\nHanoi,120\nDanang,80\n")
    # yield path


# ---------------------------------------------------------------------------
# Exercise 3 — a test that uses the sales_csv fixture above.
# Name `sales_csv` as a parameter and pytest supplies the fixture's value.
# Assert that list(extract(sales_csv)) has exactly 2 rows.
def test_extract_reads_every_row(sales_csv):
    assert False, "TODO: assert len(list(extract(sales_csv))) == 2"


# ---------------------------------------------------------------------------
# Exercise 4 — parametrize: one test body, four cases.
# Fill in the parametrize list with (text, expected) pairs covering:
#   "7"    -> 7
#   ""     -> None
#   "nope" -> None
#   "-3"   -> -3
# then use those two parameters inside the test body.
@pytest.mark.parametrize("text, expected", [
    ("TODO", "TODO"),                # TODO: replace this placeholder tuple, then
    # add the other three, e.g.:
    # ("7", 7),
    # ("", None),
    # ("nope", None),
    # ("-3", -3),
])
def test_safe_int_parametrized(text, expected):
    assert False, "TODO: assert safe_int(text) == expected"


# ---------------------------------------------------------------------------
# Exercise 5 — setup AND teardown: prove code after yield really runs.
# `_state` simulates something that must be "opened" before a test and
# "closed" after — a real fixture might open a DB connection instead.
# Fill in the fixture so _state["open"] is True during the test (after
# setup, before yield) and it appends "closed" to _log AFTER yield
# (teardown), regardless of whether the test passed.
_log = []


@pytest.fixture
def tracked_resource():
    state = {"open": True}
    ...                              # TODO:
    # yield state
    # _log.append("closed")


def test_resource_is_open_during_the_test(tracked_resource):
    assert tracked_resource["open"] is True


def test_teardown_already_ran_for_the_previous_test():
    # By the time THIS test runs, the previous test's tracked_resource
    # fixture has already finished (including its teardown) — pytest runs
    # fixtures/tests one at a time, in order, within a file by default.
    assert _log == ["closed"]
