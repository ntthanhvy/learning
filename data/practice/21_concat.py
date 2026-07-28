# Practice 21 — pd.concat(): stacking DataFrames, merge()'s sibling
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/21_concat.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

batch_a = pd.DataFrame({"customer": ["An", "Binh"], "amount": [120.0, 35.5]})
batch_b = pd.DataFrame({"customer": ["Chi", "Danh"], "amount": [99.9, 200.0]})
batch_c = pd.DataFrame({"customer": ["Danh"], "amount": [200.0], "region": ["West"]})

# ---------------------------------------------------------------------------
# Exercise 1 — stack batch_a and batch_b, with a clean 0..N index instead of
# each batch's own repeated 0/1 labels.
# pd.concat([batch_a, batch_b], ignore_index=True)
try:
    stacked = pd.concat([...], ignore_index=True)
except Exception:
    stacked = pd.DataFrame(columns=["customer", "amount"])

# ---------------------------------------------------------------------------
# Exercise 2 — stack with keys= so each row remembers which batch it came
# from, then slice back out just the "feb" batch with .loc[].
# combined = pd.concat([batch_a, batch_b], keys=["jan", "feb"])
# combined.loc["feb"]
try:
    combined = pd.concat([batch_a, batch_b], keys=[...])
    feb_only = combined.loc["feb"]
except Exception:
    feb_only = pd.DataFrame(columns=["customer", "amount"])

# ---------------------------------------------------------------------------
# Exercise 3 — concat batch_a and batch_c, which have DIFFERENT columns
# (batch_c has an extra "region"). Confirm concat fills the gap with NaN
# instead of raising or dropping the column.
# pd.concat([batch_a, batch_c], ignore_index=True)
try:
    mismatched = pd.concat([batch_a, ...], ignore_index=True)
except Exception:
    mismatched = pd.DataFrame(columns=["customer", "amount", "region"])

# ---------------------------------------------------------------------------
# Exercise 4 — axis=1: glue two same-length, same-index Series side by side
# as columns (not stacked as rows).
# pd.concat([amount, ranks], axis=1)
amount = pd.Series([120.0, 35.5, 180.0, 42.0], name="amount")
ranks = amount.rank(ascending=False).astype(int).rename("rank")
try:
    side_by_side = pd.concat([amount, ranks], axis=...)
except Exception:
    side_by_side = pd.DataFrame(columns=["amount", "rank"])

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
    check("Exercise 1: ignore_index=True gives a clean 0..3 index, 4 rows total",
          lambda: len(stacked) == 4 and list(stacked.index) == [0, 1, 2, 3]
          and stacked.loc[2, "customer"] == "Chi"),
    check("Exercise 2: keys= lets .loc['feb'] pull back just Chi/Danh",
          lambda: list(feb_only["customer"]) == ["Chi", "Danh"]),
    check("Exercise 3: mismatched columns — An/Binh get NaN region, Danh gets West",
          lambda: mismatched.loc[mismatched["customer"] == "Danh", "region"].iloc[0] == "West"
          and mismatched.loc[mismatched["customer"] == "An", "region"].isna().iloc[0]),
    check("Exercise 4: axis=1 lines up amount+rank by index — row 2 (180.0) is rank 1",
          lambda: side_by_side.loc[2, "amount"] == 180.0 and side_by_side.loc[2, "rank"] == 1),
]
print("\nAll green — lesson 21 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
