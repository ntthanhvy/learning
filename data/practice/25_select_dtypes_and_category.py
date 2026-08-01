# Practice 25 — select_dtypes() and the category dtype
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/25_select_dtypes_and_category.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

raw = pd.read_csv("practice/data/orders_raw.csv")

# Same cleaned rows as Lessons 6-24, merged with customers.csv (Lesson 5):
# An 120.0/01-05/North, An 42.0/01-10/North, Binh 35.5/01-06/South, Binh 180.0/01-09/South
clean = raw.dropna(subset=["order_date"]).copy()
clean = clean[pd.to_numeric(clean["amount"], errors="coerce").notna()]
clean["amount"] = clean["amount"].astype(float)
clean = clean.sort_values(["customer", "order_date"]).reset_index(drop=True)
customers = pd.read_csv("practice/data/customers.csv")
merged = clean.merge(customers, on="customer", how="left")

# ---------------------------------------------------------------------------
# Exercise 1 — pull out only the numeric columns (order_id, amount) with
# select_dtypes(), no column names hardcoded.
# merged.select_dtypes(include="number")
try:
    numeric_only = merged.select_dtypes(include=...)
except Exception:
    numeric_only = pd.DataFrame()

# ---------------------------------------------------------------------------
# Exercise 2 — the mirror: pull out everything EXCEPT the numeric columns.
# merged.select_dtypes(exclude="number")
try:
    non_numeric_only = merged.select_dtypes(exclude=...)
except Exception:
    non_numeric_only = pd.DataFrame()

# ---------------------------------------------------------------------------
# Exercise 3 — convert "region" to category, then prove the memory drop is
# real with memory_usage(deep=True), same as section 4's hand-verified numbers
# (216 bytes as str -> 112 bytes as category on this 4-row fixture).
# merged_cat["region"] = merged["region"].astype("category")
try:
    merged_cat = merged.copy()
    merged_cat["region"] = merged["region"].astype(...)
    bytes_before = merged.memory_usage(deep=True)["region"]
    bytes_after = merged_cat.memory_usage(deep=True)["region"]
except Exception:
    merged_cat = merged.copy()
    bytes_before, bytes_after = None, None

# ---------------------------------------------------------------------------
# Exercise 4 — reproduce section 5's gotcha: converting to an EXPLICIT fixed
# CategoricalDtype that's missing a real value ("West") silently turns that
# value into NaN, no error raised. Build the fixed dtype with only North and
# South (deliberately excluding West), then convert a small test Series
# containing all three regions and see "West" vanish.
# fixed_dtype = pd.CategoricalDtype(categories=["North", "South"])
# test_regions = pd.Series(["North", "West", "South"]).astype(fixed_dtype)
try:
    fixed_dtype = pd.CategoricalDtype(categories=...)
    test_regions = pd.Series(["North", "West", "South"]).astype(fixed_dtype)
except Exception:
    test_regions = pd.Series([None, None, None])

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
    check("Exercise 1: select_dtypes(include='number') keeps only order_id and amount",
          lambda: sorted(numeric_only.columns.tolist()) == ["amount", "order_id"]),
    check("Exercise 2: select_dtypes(exclude='number') keeps customer, order_date, region",
          lambda: sorted(non_numeric_only.columns.tolist()) == ["customer", "order_date", "region"]),
    check("Exercise 3: region becomes category dtype",
          lambda: str(merged_cat["region"].dtype) == "category"),
    check("Exercise 3: category region uses real fewer bytes than the original (216 -> 112 on this fixture)",
          lambda: bytes_before is not None and bytes_after is not None
          and bytes_after < bytes_before
          and bytes_before == 216 and bytes_after == 112),
    check("Exercise 4: fixed_dtype categories are exactly North and South (West deliberately excluded)",
          lambda: fixed_dtype.categories.tolist() == ["North", "South"]),
    check("Exercise 4: 'West' silently becomes NaN under the fixed dtype -- no error, just missing",
          lambda: test_regions.tolist()[0] == "North"
          and pd.isna(test_regions.tolist()[1])
          and test_regions.tolist()[2] == "South"),
]
print("\nAll green — lesson 25 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
