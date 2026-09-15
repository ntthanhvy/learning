# Practice 69 — sample(): random rows, reproducibly
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/69_sample.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

# Same real fixture as recent lessons, cleaned the same way.
df = pd.read_csv("practice/data/orders_raw.csv")
amount_col = pd.to_numeric(df["amount"], errors="coerce")
order_date_col = pd.to_datetime(df["order_date"], errors="coerce")
clean = (
    df.assign(amount=amount_col, order_date=order_date_col)
    .dropna(subset=["amount", "order_date"])
    .sort_values(["customer", "order_date"])
    .reset_index(drop=True)
)

# ---------------------------------------------------------------------------
# Exercise 1 — a seeded 2-row sample. Two separate calls with the SAME
# random_state must return identical rows. Use random_state=0 for both.
try:
    ex1_first = clean.sample(n=2, random_state=...)
    ex1_second = clean.sample(n=2, random_state=...)
except Exception:
    ex1_first, ex1_second = None, None

# ---------------------------------------------------------------------------
# Exercise 2 — passing both n= and frac= in the same call raises ValueError,
# regardless of frac's actual value. Fill in the literal float 0.5 (not just
# any placeholder -- this checks the value actually assigned, not merely
# that *some* exception fires, so a blank left as "..." doesn't pass by
# accident).
ex2_frac_value = ...
try:
    clean.sample(n=2, frac=ex2_frac_value)
    ex2_raised = False
except ValueError:
    ex2_raised = True
except Exception:
    ex2_raised = False

# ---------------------------------------------------------------------------
# Exercise 3 — replace=True allows drawing more rows than exist (clean only
# has 4 rows), and the result can contain duplicate row labels. Fill in the
# literal boolean True (not just any truthy value -- a bare "..." left
# unfilled is ALSO truthy to pandas here, so this checks the literal value
# itself, not merely the resulting behavior, to avoid a freebie pass).
ex3_replace_value = ...
try:
    ex3_sample = clean.sample(n=10, replace=ex3_replace_value, random_state=0)
    ex3_has_dupes = ex3_sample.index.duplicated().any()
except Exception:
    ex3_sample, ex3_has_dupes = None, False

# ---------------------------------------------------------------------------
# Exercise 4 — stratified sampling: exactly one row per customer via
# groupby("customer", group_keys=False).sample(n=..., random_state=0).
# Fill in the literal integer 1 (one row per group).
try:
    ex4_sample = clean.groupby("customer", group_keys=False).sample(n=..., random_state=0)
except Exception:
    ex4_sample = None

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
    check("Exercise 1: same random_state gives identical rows across calls",
          lambda: ex1_first is not None and ex1_second is not None
          and ex1_first.equals(ex1_second)),
    check("Exercise 2: n= and frac= together raises ValueError",
          lambda: ex2_frac_value == 0.5 and ex2_raised is True),
    check("Exercise 3: replace=True allows oversampling with duplicate rows",
          lambda: ex3_replace_value is True and ex3_sample is not None
          and len(ex3_sample) == 10 and bool(ex3_has_dupes) is True),
    check("Exercise 4: groupby().sample(n=1) gives exactly one row per customer",
          lambda: ex4_sample is not None
          and sorted(ex4_sample["customer"].tolist()) == ["An", "Binh"]
          and len(ex4_sample) == 2),
]

print("\nAll green — lesson 69 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
