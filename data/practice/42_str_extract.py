# Practice 42 — str.extract()
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/42_str_extract.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

# Small inline order_code fixture (same customer/order domain as Lessons 6-41).
# One code ("bad-code") deliberately does not match the region-seq pattern.
orders = pd.DataFrame({
    "order_id": [1, 2, 3, 4, 5, 6],
    "customer": ["An", "Binh", "An", "Chi", "Binh", "An"],
    "order_code": ["NA-0231", "EU-0089", "NA-0245", "AP-0012", "EU-0104", "bad-code"],
})

# ---------------------------------------------------------------------------
# Exercise 1 — extract the 2-letter region prefix (e.g. "NA" from "NA-0231")
# as a Series (one capture group, expand=False).
try:
    region_series = orders["order_code"].str.extract(r"([A-Z]{2})-\d+", expand=...)
except Exception:
    region_series = pd.Series(dtype=object)

# ---------------------------------------------------------------------------
# Exercise 2 — extract BOTH the region and the sequence number in one call,
# using named groups so the result columns are already labeled "region" and
# "seq" (no rename() needed).
try:
    parts = orders["order_code"].str.extract(r"(?P<region>[A-Z]{2})-(?P<seq>\d+)")
except Exception:
    parts = pd.DataFrame()

# ---------------------------------------------------------------------------
# Exercise 3 — "bad-code" (row 5) doesn't match the pattern at all. Confirm
# it becomes NaN rather than raising: count how many rows in parts["region"]
# are NaN.
try:
    non_match_count = parts[...].isna().sum()
except Exception:
    non_match_count = -1

# ---------------------------------------------------------------------------
# Exercise 4 — assign the extracted region back onto orders as a new column,
# then count orders per region with groupby() (row 5's NaN region is
# excluded automatically, same rule as any groupby key).
try:
    orders["region"] = orders["order_code"].str.extract(r"([A-Z]{2})-\d+", expand=False)
    region_counts = orders.groupby(...)["order_id"].count()
except Exception:
    region_counts = pd.Series(dtype=int)

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
    check("Exercise 1: region_series is a Series (expand=False, one group)",
          lambda: isinstance(region_series, pd.Series)),
    check("Exercise 1: region_series values are NA/EU/NA/AP/EU/NaN",
          lambda: region_series.tolist()[:5] == ["NA", "EU", "NA", "AP", "EU"]
          and pd.isna(region_series.tolist()[5])),
    check("Exercise 2: parts is a DataFrame with columns region, seq",
          lambda: list(parts.columns) == ["region", "seq"]),
    check("Exercise 2: parts['seq'] captured the digits (e.g. '0231' for row 0)",
          lambda: parts.loc[0, "seq"] == "0231"),
    check("Exercise 3: non_match_count is exactly 1 (only 'bad-code' fails to match)",
          lambda: non_match_count == 1),
    check("Exercise 4: region_counts has exactly 3 regions (NA, EU, AP)",
          lambda: len(region_counts) == 3),
    check("Exercise 4: region_counts['NA'] is 2, region_counts['EU'] is 2",
          lambda: region_counts.loc["NA"] == 2 and region_counts.loc["EU"] == 2),
]
print("\nAll green — lesson 42 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
