# Practice 46 — f-strings and the format spec mini-language
# Run:  cd ~/learning/python && uv run python3 practice/46_fstrings_and_format_spec.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓.


# ---------------------------------------------------------------------------
# Exercise 1 — format a price with exactly two decimal places and a
# thousands separator, e.g. 1234.5 -> "1,234.50".
def format_price(amount):
    # TODO: return f"{amount:,.2f}"
    ...


# ---------------------------------------------------------------------------
# Exercise 2 — build one report line: label left-aligned in a 10-char field,
# then the number right-aligned in a 6-char field with a thousands
# separator, e.g. ("Hanoi", 1200) -> "Hanoi      1,200".
def report_line(label, total):
    # TODO: return f"{label:<10}{total:>6,}"
    ...


# ---------------------------------------------------------------------------
# Exercise 3 — return the !r (repr) form of a string, e.g. "hi" -> "'hi'"
# (quotes included, exactly what repr() itself would show).
def debug_repr(text):
    # TODO: return f"{text!r}"
    ...


# ---------------------------------------------------------------------------
# Exercise 4 — use the `=` debug specifier to build a string showing both an
# expression's source text and its value, e.g. count=3 -> "count=3".
# The function receives the already-evaluated value; build the same shape
# the `=` specifier would produce for a bare name called "count".
def debug_equals(count):
    # TODO: return f"{count=}"
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


results = [
    check("Ex 1: format_price adds two decimals and a thousands separator",
          lambda: format_price(1234.5) == "1,234.50"),
    check("Ex 1b: format_price handles a small value with no separator needed",
          lambda: format_price(9) == "9.00"),
    check("Ex 2: report_line left-aligns label, right-aligns grouped number",
          lambda: report_line("Hanoi", 1200) == "Hanoi      1,200"),
    check("Ex 2b: report_line handles a longer label and a smaller number",
          lambda: report_line("HCMC", 980) == "HCMC         980"),
    check("Ex 3: debug_repr shows the quoted, unambiguous repr() form",
          lambda: debug_repr("hi") == "'hi'"),
    check("Ex 3b: debug_repr distinguishes a string containing a digit from an int",
          lambda: debug_repr("42") == "'42'"),
    check("Ex 4: debug_equals shows name=value using the = specifier's shape",
          lambda: debug_equals(3) == "count=3"),
    check("Ex 4b: debug_equals works for zero too",
          lambda: debug_equals(0) == "count=0"),
]
print("\nAll green — lesson 46 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
