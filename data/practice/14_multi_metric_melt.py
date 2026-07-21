# Practice 14 — Melt revisited: multiple metrics at once
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/14_multi_metric_melt.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

df = pd.read_csv("practice/data/orders_raw.csv")
df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
# Same clean 4-row slice as Lessons 6-13: An x2, Binh x2, one order per date.
clean = df.dropna(subset=["amount", "order_date"])

# ---------------------------------------------------------------------------
# Exercise 1 — a multi-metric wide table: pivot_table with TWO aggfuncs at
# once (sum and count) over the same values column produces a MultiIndex on
# the columns — level 0 is the aggfunc name ("sum"/"count"), level 1 is
# order_date. index="customer", values="amount", aggfunc=["sum", "count"],
# fill_value=0.
wide = ...

# ---------------------------------------------------------------------------
# Exercise 2 — melt needs flat (single-level) column names, so flatten the
# MultiIndex first: join each column tuple's two levels with "_" so
# ("sum", "2026-01-05") becomes the single string "sum_2026-01-05":
# wide.set_axis(["_".join(map(str, c)) for c in wide.columns.to_flat_index()], axis=1)
try:
    flat = wide.set_axis(..., axis=1)
except Exception:
    flat = pd.DataFrame()

# ---------------------------------------------------------------------------
# Exercise 3 — now it melts exactly like Lesson 6: reset_index() (customer is
# still the index), then melt(id_vars="customer", var_name="metric_date",
# value_name="value").
try:
    long = flat.reset_index().melt(id_vars=..., var_name=..., value_name=...)
except Exception:
    long = pd.DataFrame(columns=["customer", "metric_date", "value"])

# ---------------------------------------------------------------------------
# Exercise 4 — metric_date is still one merged string ("sum_2026-01-05");
# split it back into two real columns on the FIRST "_" only (dates contain
# no underscores, but splitting without a limit would still work here — n=1
# is the safe habit for when a metric name itself might contain "_"):
# long["metric_date"].str.split("_", n=1, expand=True)
try:
    long[["metric", "order_date"]] = long["metric_date"].str.split("_", n=1, expand=True)
except Exception:
    long["metric"] = None
    long["order_date"] = None

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
    check("Exercise 1: wide has a 2-level MultiIndex column, An sum/01-05 is 120.0",
          lambda: wide.columns.nlevels == 2
          and wide.loc["An", ("sum", "2026-01-05")] == 120.0
          and wide.loc["An", ("count", "2026-01-06")] == 0),
    check("Exercise 2: flat has single-level string columns like 'sum_2026-01-05'",
          lambda: flat.columns.nlevels == 1 and "sum_2026-01-05" in list(flat.columns)),
    check("Exercise 3: long has 16 rows (2 customers x 4 dates x 2 metrics)",
          lambda: len(long) == 16 and list(long.columns)[:3] == ["customer", "metric_date", "value"]),
    check("Exercise 4: split out metric='sum' and order_date='2026-01-05' for An's 120.0 row",
          lambda: len(long[(long["customer"] == "An") & (long["metric"] == "sum")
                            & (long["order_date"] == "2026-01-05")
                            & (long["value"] == 120.0)]) == 1),
]
print("\nAll green — lesson 14 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
