# Practice 26 — SettingWithCopy and .copy()
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/26_settingwithcopy_and_copy.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

raw = pd.read_csv("practice/data/orders_raw.csv")

# Same cleaned rows as Lessons 6-25:
# An 120.0/01-05, An 42.0/01-10, Binh 35.5/01-06, Binh 180.0/01-09
clean = raw.dropna(subset=["order_date"]).copy()
clean = clean[pd.to_numeric(clean["amount"], errors="coerce").notna()]
clean["amount"] = clean["amount"].astype(float)
clean = clean.sort_values(["customer", "order_date"]).reset_index(drop=True)

# ---------------------------------------------------------------------------
# Exercise 1 — reproduce the two-line chained-indexing trap from section 3.
# Filter clean to An's rows into `an_rows` (its own variable, no .copy()),
# then try to set an_rows["amount"] to 0. On current pandas (Copy-on-Write)
# this raises nothing and silently does NOT touch `clean` -- prove that by
# checking clean's An amounts are still the original 120.0 and 42.0 after.
# an_rows = clean[clean["customer"] == "An"]
try:
    an_rows = clean[clean[...] == "An"]
    an_rows["amount"] = 0
except Exception:
    an_rows = pd.DataFrame()

# ---------------------------------------------------------------------------
# Exercise 2 — the explicit .copy() fix: filter An's rows, call .copy(),
# THEN mutate. an_only ends up independently changed to 0; clean is
# guaranteed untouched (same fixture, so also still 120.0/42.0).
# an_only = clean[clean["customer"] == "An"].copy()
try:
    an_only = clean[clean[...] == "An"].copy()
    an_only["amount"] = 0
except Exception:
    an_only = pd.DataFrame()

# ---------------------------------------------------------------------------
# Exercise 3 — the other correct fix: mutate clean ITSELF, on purpose, via
# one combined .loc[row_selector, col_selector] = value call (no chained
# indexing, no intermediate object). Work on a fresh copy of clean first
# (clean_loc) so Exercise 1/2's checks above aren't affected by this one.
# clean_loc.loc[clean_loc["customer"] == "An", "amount"] = 0
try:
    clean_loc = clean.copy()
    clean_loc.loc[clean_loc[...] == "An", "amount"] = 0
except Exception:
    clean_loc = pd.DataFrame()

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
    check("Exercise 1: an_rows itself got mutated to 0 for both An rows",
          lambda: an_rows["amount"].tolist() == [0, 0]),
    check("Exercise 1: clean is UNTOUCHED -- chained indexing silently failed to update it",
          lambda: clean.loc[clean["customer"] == "An", "amount"].tolist() == [120.0, 42.0]),
    check("Exercise 2: an_only (the explicit .copy()) is mutated to 0 for both An rows",
          lambda: an_only["amount"].tolist() == [0, 0]),
    check("Exercise 2: clean is still untouched by the .copy()-based fix",
          lambda: clean.loc[clean["customer"] == "An", "amount"].tolist() == [120.0, 42.0]),
    check("Exercise 3: clean_loc's An rows ARE now 0 -- the single .loc[] call mutated it on purpose",
          lambda: clean_loc.loc[clean_loc["customer"] == "An", "amount"].tolist() == [0, 0]),
    check("Exercise 3: clean_loc's Binh rows are untouched (35.5, 180.0)",
          lambda: clean_loc.loc[clean_loc["customer"] == "Binh", "amount"].tolist() == [35.5, 180.0]),
]
print("\nAll green — lesson 26 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
