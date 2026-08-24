# Practice 28 — Unpacking: naming the pieces instead of indexing for them
# Run:  cd ~/learning/python && uv run python3 practice/28_unpacking.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each function body below (the `...` line) and re-run until every
# check prints ✓. Each function should return the unpacked value(s) asked
# for in its docstring/comment, using unpacking — not manual indexing.

# ---------------------------------------------------------------------------
# Exercise 1 — basic tuple unpacking.
# point is a (x, y) tuple. Unpack it directly into x and y — no indexing —
# and return them as (x, y).
point = (3, 4)


def unpack_point():
    ...                           # TODO: x, y = point; return x, y


# ---------------------------------------------------------------------------
# Exercise 2 — star-unpacking a header off a list of rows.
# csv_lines is a header line followed by data lines. Star-unpack it into
# a header (the first line) and the rest (a list of every line after it),
# and return them as (header, rest).
csv_lines = ["id,name", "1,An", "2,Binh", "3,Chi"]


def split_header():
    ...                           # TODO: header, *rest = csv_lines; return header, rest


# ---------------------------------------------------------------------------
# Exercise 3 — the no-temp swap idiom.
# Swap two given values in a single unpacking assignment, no temporary
# third variable, and return the swapped pair as (b, a).
def swap(a, b):
    ...                           # TODO: a, b = b, a; return a, b


# ---------------------------------------------------------------------------
# Exercise 4 — unpacking a for loop over (name, score) pairs.
# Return the sum of every score, by unpacking each pair in the loop header
# itself (for name, score in pairs:), not by indexing pair[1].
pairs = [("An", 30), ("Binh", 25), ("Chi", 41)]


def total_score():
    total = 0
    ...                           # TODO: for name, score in pairs: total += score
    return total


# ---------------------------------------------------------------------------
# Exercise 5 — unpacking a function's returned tuple at the call site.
# min_max returns one (min, max) tuple. Call it and unpack the result
# directly into lowest and highest — no intermediate variable holding
# the whole tuple, no indexing — and return them as (lowest, highest).
def min_max(values):
    return min(values), max(values)


def lowest_and_highest():
    ...                           # TODO: lowest, highest = min_max([120, 80, 200, 45]); return lowest, highest


# ---------------------------------------------------------------------------
# Checks — don't edit below this line.
def check(name, cond):
    try:
        ok = bool(cond())
    except Exception:
        ok = False
    print(("✓" if ok else "✗"), name)
    return ok


results = [
    check("Ex 1: unpack_point unpacks point directly into x and y",
          lambda: unpack_point() == (3, 4)),
    check("Ex 2: split_header star-unpacks csv_lines into header and rest",
          lambda: split_header() == ("id,name", ["1,An", "2,Binh", "3,Chi"])),
    check("Ex 3: swap swaps its two arguments with no temp variable",
          lambda: swap("left", "right") == ("right", "left")),
    check("Ex 4: total_score sums every score via unpacked (name, score) pairs",
          lambda: total_score() == 96),
    check("Ex 5: lowest_and_highest unpacks min_max's return directly",
          lambda: lowest_and_highest() == (45, 200)),
]
print("\nAll green — lesson 28 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
