# Practice 77 — str.replace(): rewriting text in place, and its flipped regex= default
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/77_str_replace.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import numpy as np
import pandas as pd

orders = pd.DataFrame({
    "sku_path": ["ELEC/PHONE/CASE-01", "HOME/KITCHEN/MUG-02", "ELEC/LAPTOP/DOCK-03",
                 "HOME/BEDROOM/LAMP-04", "TOYS/BLOCK-05"],
    "customer_full": ["An Nguyen-North", "Binh Tran-South", "Chi Le-East",
                       "Danh Vo-West", np.nan],
    "price_note": ["price: $19.99", "price: $8.50", "price: $45.00",
                    "price: $12.25", "price: $3.10"],
})
skus = pd.Series(["A.1", "A21", "B.5"])

# ---------------------------------------------------------------------------
# Exercise 1 — basic literal swap: replace every "/" in sku_path with "-".
# str.replace() returns a NEW Series -- the original orders["sku_path"] column
# stays untouched unless the result is assigned back. Fill in the literal
# string "/" for the pattern being replaced (not just any placeholder --
# checks the literal value itself, to avoid a freebie pass).
ex1_pat = ...
try:
    ex1_replaced = orders["sku_path"].str.replace(ex1_pat, "-")
    ex1_row0 = ex1_replaced.iloc[0]
    ex1_original_untouched = orders["sku_path"].iloc[0] == "ELEC/PHONE/CASE-01"
except Exception:
    ex1_row0 = ex1_original_untouched = None

# ---------------------------------------------------------------------------
# Exercise 2 — regex=False is str.replace()'s DEFAULT (the opposite default
# from str.contains(), which defaults to regex=True). On skus = ["A.1", "A21",
# "B.5"], replacing "A." with "X" using the default treats "." literally, so
# only "A.1" matches. Fill in the literal bool True for what regex= must be
# set to so that "A21" ALSO gets replaced (not just any placeholder -- checks
# the literal value, to avoid a freebie pass).
ex2_regex_for_any_char = ...
try:
    ex2_literal = skus.str.replace("A.", "X")          # default regex=False
    ex2_asregex = skus.str.replace("A.", "X", regex=ex2_regex_for_any_char)
    ex2_literal_row1_untouched = ex2_literal.iloc[1] == "A21"
    ex2_asregex_row1_matched = ex2_asregex.iloc[1] == "X1"
except Exception:
    ex2_literal_row1_untouched = ex2_asregex_row1_matched = None

# ---------------------------------------------------------------------------
# Exercise 3 — regex=True unlocks capture-group backreferences in repl.
# Rewrite "price: $19.99" style strings to "price: USD 19.99" by capturing
# the numeric amount and reinserting it after "USD ". Fill in the literal
# backreference string r"USD \1" for repl (not just any placeholder -- checks
# the literal value, to avoid a freebie pass).
ex3_repl = ...
try:
    ex3_rewritten = orders["price_note"].str.replace(
        r"\$(\d+\.\d+)", ex3_repl, regex=True)
    ex3_row0 = ex3_rewritten.iloc[0]
except Exception:
    ex3_row0 = None

# ---------------------------------------------------------------------------
# Exercise 4 — n= caps the replacement count per string (default -1 = all).
# Splitting "a-b-c-d" style strings with n=1 replaces only the FIRST "-".
# Separately, confirm a missing value in customer_full stays NaN through
# str.replace() rather than becoming the literal string "NaN". Fill in the
# literal int 1 for n= (not just any placeholder -- checks the literal
# value, to avoid a freebie pass).
ex4_n = ...
try:
    s = pd.Series(["a-b-c-d", "x-y-z"])
    ex4_capped = s.str.replace("-", "_", n=ex4_n)
    ex4_row0 = ex4_capped.iloc[0]
    ex4_customer_replaced = orders["customer_full"].str.replace("-", " ")
    ex4_row4_is_na = pd.isna(ex4_customer_replaced.iloc[4])
except Exception:
    ex4_row0 = None
    ex4_row4_is_na = None

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
    check("Exercise 1: literal swap replaces every '/' with '-', source column untouched",
          lambda: ex1_pat == "/" and ex1_row0 == "ELEC-PHONE-CASE-01"
          and ex1_original_untouched is True),
    check("Exercise 2: regex=False (default) is literal, regex=True treats '.' as any char",
          lambda: ex2_regex_for_any_char is True
          and ex2_literal_row1_untouched is True and ex2_asregex_row1_matched is True),
    check("Exercise 3: regex=True capture-group backreference rewrites the matched amount",
          lambda: ex3_repl == r"USD \1" and ex3_row0 == "price: USD 19.99"),
    check("Exercise 4: n= caps replacement count; NaN passes through untouched",
          lambda: ex4_n == 1 and ex4_row0 == "a_b-c-d" and ex4_row4_is_na is True),
]

print("\nAll green — lesson 77 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
