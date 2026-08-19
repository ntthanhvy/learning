# Practice 43 — str.extractall()
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/43_str_extractall.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

# Small inline notes fixture (same customer/order domain as Lessons 6-42).
# Row 3 ("no tags here") deliberately has zero matches for the tag pattern.
orders = pd.DataFrame({
    "order_id": [1, 2, 3, 4],
    "customer": ["An", "Binh", "An", "Chi"],
    "notes": [
        "tags: urgent, gift",
        "tags: bulk",
        "tags: urgent, fragile, gift",
        "no tags here",
    ],
})

TAG_PATTERN = r"(?P<tag>urgent|gift|bulk|fragile)"

# ---------------------------------------------------------------------------
# Exercise 1 — extractall() every tag match (not just the first) into a
# DataFrame with a MultiIndex (original row, match number).
try:
    matches = orders["notes"].str.extractall(...)
except Exception:
    matches = pd.DataFrame()

# ---------------------------------------------------------------------------
# Exercise 2 — count matches per ORIGINAL row using groupby on the outer
# MultiIndex level (level=0). Row 3 will be absent here (zero matches).
try:
    tag_count_by_row = matches.groupby(level=...).size()
except Exception:
    tag_count_by_row = pd.Series(dtype=int)

# ---------------------------------------------------------------------------
# Exercise 3 — map that count back onto orders' own index, filling missing
# rows (no matches at all, like row 3) with a real 0 instead of leaving NaN.
try:
    orders["tag_count"] = orders.index.map(tag_count_by_row).fillna(0).astype(...)
except Exception:
    orders["tag_count"] = pd.Series(dtype=int)

# ---------------------------------------------------------------------------
# Exercise 4 — compare against str.findall(), which returns one Python list
# per row (empty list, not NaN, for a non-matching row like row 3).
try:
    tag_lists = orders["notes"].str.findall(...)
except Exception:
    tag_lists = pd.Series(dtype=object)

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
    check("Exercise 1: matches has a MultiIndex (2 levels)",
          lambda: matches.index.nlevels == 2),
    check("Exercise 1: matches has 6 rows total (2 + 1 + 3 across matching rows)",
          lambda: len(matches) == 6),
    check("Exercise 2: tag_count_by_row has exactly 3 entries (row 3 has none)",
          lambda: len(tag_count_by_row) == 3),
    check("Exercise 2: tag_count_by_row for row 2 (index label 2) is 3",
          lambda: tag_count_by_row.loc[2] == 3),
    check("Exercise 3: orders['tag_count'] is [2, 1, 3, 0] (row 3 correctly 0, not NaN)",
          lambda: orders["tag_count"].tolist() == [2, 1, 3, 0]),
    check("Exercise 4: tag_lists row 3 is an empty list, not NaN",
          lambda: tag_lists.iloc[3] == []),
    check("Exercise 4: tag_lists row 2 has all 3 tags (urgent, fragile, gift)",
          lambda: tag_lists.iloc[2] == ["urgent", "fragile", "gift"]),
]
print("\nAll green — lesson 43 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
