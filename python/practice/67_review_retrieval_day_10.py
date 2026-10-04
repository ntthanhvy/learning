# Practice 67 — review day 10: retrieval across Days 64-66
# Run:  cd ~/learning/python && uv run python3 practice/67_review_retrieval_day_10.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# No new syntax here — every mechanism below was taught in Days 64, 65, and 66.
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓. Try each from memory before reopening the old lesson.

import csv
import tempfile
import zipfile
from pathlib import Path


# ---------------------------------------------------------------------------
# Exercise 1 (Day 64 — zipfile: write a small archive with chosen internal
# names via arcname=, then read one member's bytes back WITHOUT extracting
# the rest, via zf.open(name))
def write_archive(zip_path, files):
    """files is a dict of {arcname: text_content}. Write a new zip archive
    at zip_path containing one member per entry, with that exact arcname."""
    # TODO: with zipfile.ZipFile(zip_path, "w") as zf:
    #           for arcname, content in files.items():
    #               zf.writestr(arcname, content)
    ...


def read_one_member(zip_path, arcname):
    """Open the archive read-only and return just one member's text content,
    without extracting anything to disk."""
    # TODO: with zipfile.ZipFile(zip_path) as zf:
    #           with zf.open(arcname) as f:
    #               return f.read().decode("utf-8")
    ...


# ---------------------------------------------------------------------------
# Exercise 2 (Day 65 — tempfile: TemporaryDirectory() deletes itself, and
# everything staged inside it, the moment the with block exits)
def stage_and_report(contents):
    """Inside one TemporaryDirectory(), write `contents` (a str) to a file
    named 'staged.txt', read it back, and return a tuple:
    (text_read_back, path_that_was_used_as_a_string).
    The caller will check that the returned path no longer exists once this
    function has returned (because the TemporaryDirectory() already closed)."""
    # TODO: with tempfile.TemporaryDirectory() as tmp_dir:
    #           p = Path(tmp_dir) / "staged.txt"
    #           p.write_text(contents)
    #           return p.read_text(), str(p)
    ...


# ---------------------------------------------------------------------------
# Exercise 3 (Day 66 — csv.DictWriter: fieldnames=, writeheader()+writerows(),
# newline="", and extrasaction="ignore" for a dict with an unexpected key)
def write_rows_csv(csv_path, fieldnames, rows):
    """Write `rows` (a list of dicts, possibly with keys not in fieldnames)
    out to csv_path as a header plus data rows. Extra keys not listed in
    fieldnames must be silently dropped, not raise."""
    # TODO: with open(csv_path, "w", newline="") as f:
    #           writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
    #           writer.writeheader()
    #           writer.writerows(rows)
    ...


def read_rows_csv(csv_path):
    """Read csv_path back with csv.DictReader (Day 6) and return a list of
    plain dicts, one per data row."""
    # TODO: with open(csv_path, newline="") as f:
    #           return list(csv.DictReader(f))
    ...


# ---------------------------------------------------------------------------
# Checks — don't edit below this line.
def check(name, cond):
    try:
        ok = bool(cond())
    except Exception:
        ok = False
    print(("✓" if ok else "✗"), name)
    return ok


def _ex1_member_reads_back_without_extracting():
    with tempfile.TemporaryDirectory() as d:
        zip_path = Path(d) / "drop.zip"
        write_archive(zip_path, {
            "orders.csv": "id,amount\n1,10\n",
            "readme.txt": "hello",
        })
        if not zip_path.exists():
            return False
        text = read_one_member(zip_path, "orders.csv")
        # confirm nothing was extracted alongside the archive itself
        only_zip_present = [p.name for p in Path(d).iterdir()] == ["drop.zip"]
        return text == "id,amount\n1,10\n" and only_zip_present


def _ex2_staged_file_readable_inside_block():
    text, _ = stage_and_report("hello from the pipeline")
    return text == "hello from the pipeline"


def _ex2_path_gone_after_block_exits():
    _, used_path = stage_and_report("temporary")
    return not Path(used_path).exists()


def _ex3_round_trips_through_dictreader():
    with tempfile.TemporaryDirectory() as d:
        csv_path = Path(d) / "out.csv"
        rows = [
            {"city": "Hanoi", "amount": "120"},
            {"city": "Hue", "amount": "45"},
        ]
        write_rows_csv(csv_path, ["city", "amount"], rows)
        result = read_rows_csv(csv_path)
        return result == rows


def _ex3_extra_key_silently_dropped():
    with tempfile.TemporaryDirectory() as d:
        csv_path = Path(d) / "out.csv"
        rows = [{"city": "Hanoi", "amount": "120", "note": "q3"}]
        write_rows_csv(csv_path, ["city", "amount"], rows)
        result = read_rows_csv(csv_path)
        return result == [{"city": "Hanoi", "amount": "120"}]


results = [
    check("Ex 1: one zip member reads back without extracting the rest",
          _ex1_member_reads_back_without_extracting),
    check("Ex 2: a file staged inside TemporaryDirectory() is readable in the block",
          _ex2_staged_file_readable_inside_block),
    check("Ex 2: the staged path no longer exists once the with block exits",
          _ex2_path_gone_after_block_exits),
    check("Ex 3: DictWriter rows round-trip through Day 6's DictReader",
          _ex3_round_trips_through_dictreader),
    check("Ex 3: extrasaction='ignore' silently drops an unlisted dict key",
          _ex3_extra_key_silently_dropped),
]

print("\nAll green — lesson 67 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
