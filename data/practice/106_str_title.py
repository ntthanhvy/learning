# Practice 106 — Series.str.title(): title-casing a column, and the
#                apostrophe trap it shares with plain Python
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/106_str_title.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Exercise 1 — Section 1: .str.title() title-cases a simple multi-word
# Series the expected way: first letter of each space-separated word up,
# everything else down.
s = pd.Series(["JOHN SMITH", "jane doe", "MaRy Jones"])

# ex1_result = s.str.title()
ex1_result = ...
try:
    ex1_ok = bool((ex1_result == ["John Smith", "Jane Doe", "Mary Jones"]).all())
except Exception:
    ex1_ok = False

# ---------------------------------------------------------------------------
# Exercise 2 — Section 2: the apostrophe/digit trap reproduces the exact
# same result as Python's own built-in str.title() applied one string at a
# time -- .str.title() is a thin vectorized wrapper, not a separate
# pandas-only implementation.
trappy = pd.Series(["o'brien's shop", "mcdonald's", "3rd street"])


def title_matches_python_builtin(values):
    # Return True if values.str.title() exactly matches calling Python's
    # own builtin str.title() on each element one at a time (a list
    # comprehension), element for element.
    #   pandas_result = values.str.title().tolist()
    #   python_result = [v.title() for v in values]
    #   return pandas_result == python_result
    ...


# ex2_matches = title_matches_python_builtin(trappy)
ex2_matches = ...
try:
    ex2_matches_ok = ex2_matches is True
except Exception:
    ex2_matches_ok = False

# ---------------------------------------------------------------------------
# Exercise 3 — Sections 2-3: .str.capitalize() gives a different,
# single-first-character-only result on the same trappy input (no per-word
# logic), and NaN passes through .str.title() untouched while a real
# string in the same Series gets title-cased.
mixed = pd.Series(["abc", np.nan, "def"])

# ex3_capitalize = trappy.str.capitalize()
ex3_capitalize = ...
# ex3_title_nan = mixed.str.title()
ex3_title_nan = ...
try:
    ex3_capitalize_ok = bool(ex3_capitalize.iloc[0] == "O'brien's shop")
    ex3_abc_ok = bool(ex3_title_nan.iloc[0] == "Abc")
    ex3_nan_ok = bool(pd.isna(ex3_title_nan.iloc[1]))
    ex3_def_ok = bool(ex3_title_nan.iloc[2] == "Def")
except Exception:
    ex3_capitalize_ok = False
    ex3_abc_ok = False
    ex3_nan_ok = False
    ex3_def_ok = False

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
    check("Exercise 1: .str.title() title-cases each space-separated word",
          lambda: ex1_ok is True),
    check("Exercise 2: .str.title() exactly matches Python's own builtin str.title(), apostrophe trap included",
          lambda: ex2_matches_ok is True),
    check("Exercise 3: .str.capitalize() differs from .str.title(); NaN passes through .str.title() untouched",
          lambda: ex3_capitalize_ok is True
          and ex3_abc_ok is True
          and ex3_nan_ok is True
          and ex3_def_ok is True),
]

print("\nAll green — lesson 106 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
