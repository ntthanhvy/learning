# Practice 104 — Series.str.strip(): the whitespace bug hiding in every merge key
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/104_str_strip.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Exercise 1 — Section 1: .str.strip() collapses whitespace-padded duplicate
# keys so groupby() produces the correct number of groups.
df = pd.DataFrame({
    "name": ["Binh", "Binh ", " Binh", "An"],
    "amount": [100, 50, 30, 20],
})

# ex1_before = df.groupby("name")["amount"].sum()
ex1_before = ...
# ex1_clean_key = df["name"].str.strip()
ex1_clean_key = ...
# ex1_after = df.groupby(ex1_clean_key)["amount"].sum()
ex1_after = ...
try:
    ex1_before_groups_ok = bool(ex1_before.shape[0] == 4)
    ex1_after_groups_ok = bool(ex1_after.shape[0] == 2)
    ex1_binh_total_ok = bool(ex1_after.loc["Binh"] == 180)
except Exception:
    ex1_before_groups_ok = False
    ex1_after_groups_ok = False
    ex1_binh_total_ok = False

# ---------------------------------------------------------------------------
# Exercise 2 — Section 2: lstrip()/rstrip() each remove only one side,
# leaving the other side's whitespace untouched.
s = pd.Series([" Binh ", "  An", "Chi  "])

# ex2_left = s.str.lstrip()
ex2_left = ...
# ex2_right = s.str.rstrip()
ex2_right = ...
try:
    ex2_left_ok = bool((ex2_left == ["Binh ", "An", "Chi  "]).all())
    ex2_right_ok = bool((ex2_right == [" Binh", "  An", "Chi"]).all())
except Exception:
    ex2_left_ok = False
    ex2_right_ok = False

# ---------------------------------------------------------------------------
# Exercise 3 — Section 3: NaN passes through .str.strip() untouched while a
# real string in the same Series gets stripped.
mixed = pd.Series([" Binh ", np.nan, "  An  "])


def strip_keep_nan(values):
    # Call values.str.strip() and return the result -- NaN entries should
    # pass straight through unchanged, real strings should get stripped.
    # return values.str.strip()
    ...


# ex3_result = strip_keep_nan(mixed)
ex3_result = ...
try:
    ex3_binh_ok = bool(ex3_result[0] == "Binh")
    ex3_nan_ok = bool(pd.isna(ex3_result[1]))
    ex3_an_ok = bool(ex3_result[2] == "An")
except Exception:
    ex3_binh_ok = False
    ex3_nan_ok = False
    ex3_an_ok = False

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
    check("Exercise 1: .str.strip() on the key collapses whitespace dupes into correct groups",
          lambda: ex1_before_groups_ok is True
          and ex1_after_groups_ok is True
          and ex1_binh_total_ok is True),
    check("Exercise 2: lstrip() leaves trailing space, rstrip() leaves leading space",
          lambda: ex2_left_ok is True
          and ex2_right_ok is True),
    check("Exercise 3: NaN passes through .str.strip() untouched, real strings get stripped",
          lambda: ex3_binh_ok is True
          and ex3_nan_ok is True
          and ex3_an_ok is True),
]

print("\nAll green — lesson 104 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
