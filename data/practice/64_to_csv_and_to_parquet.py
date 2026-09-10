# Practice 64 — to_csv() and to_parquet(): the ETL Load step, and its silent traps
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/64_to_csv_and_to_parquet.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import os
import shutil

import pandas as pd

# Same real fixture as recent lessons, cleaned the same way.
df = pd.read_csv("practice/data/orders_raw.csv")
amount = pd.to_numeric(df["amount"], errors="coerce")
order_date = pd.to_datetime(df["order_date"], errors="coerce")
clean = (
    df.assign(amount=amount, order_date=order_date)
    .dropna(subset=["amount", "order_date"])
    .sort_values(["customer", "order_date"])
    .reset_index(drop=True)
)

# Scratch output folder for this practice run only.
OUT_DIR = "practice/.out64"
shutil.rmtree(OUT_DIR, ignore_errors=True)
os.makedirs(OUT_DIR, exist_ok=True)

# ---------------------------------------------------------------------------
# Exercise 1 — write `clean` to CSV the CORRECT way: no extra index column.
# Use the right keyword argument so the row index is NOT written to the file.
try:
    clean.to_csv(f"{OUT_DIR}/correct.csv", index=...)
    correct_cols = pd.read_csv(f"{OUT_DIR}/correct.csv").columns.tolist()
except Exception:
    correct_cols = []

# ---------------------------------------------------------------------------
# Exercise 2 — write `clean` to CSV using to_csv()'s DEFAULT (no index=
# argument at all) to see the junk column appear directly. Call to_csv()
# with ONLY a path -- no other arguments.
try:
    clean.to_csv(...)
    wrong_cols = pd.read_csv(f"{OUT_DIR}/default.csv").columns.tolist()
except Exception:
    wrong_cols = []

# ---------------------------------------------------------------------------
# Exercise 3 — round-trip the order_date column through plain to_csv()/
# read_csv() (no index, but no parse_dates= on the read either) and check
# what dtype comes back. Write with to_csv(..., index=False), then read
# with plain pd.read_csv() (no parse_dates=).
try:
    clean.to_csv(f"{OUT_DIR}/dates.csv", index=False)
    reread_plain = pd.read_csv(...)
    plain_date_dtype = str(reread_plain["order_date"].dtype)
except Exception:
    plain_date_dtype = ""

# ---------------------------------------------------------------------------
# Exercise 4 — re-read that same file, this time passing parse_dates= to
# restore the datetime dtype.
try:
    reread_parsed = pd.read_csv(f"{OUT_DIR}/dates.csv", parse_dates=...)
    parsed_date_dtype = str(reread_parsed["order_date"].dtype)
except Exception:
    parsed_date_dtype = ""

# ---------------------------------------------------------------------------
# Exercise 5 — append a second batch WITHOUT turning the header off, and
# confirm the numeric "amount" column gets silently demoted to text/object
# because the column names get re-written as a literal data row in the
# middle of the file. Write once normally (index=False), then append the
# same data again with mode="a", index=False -- but do NOT pass header=False.
try:
    clean.to_csv(f"{OUT_DIR}/appended.csv", index=False)
    clean.to_csv(f"{OUT_DIR}/appended.csv", mode=..., index=False)
    reread_appended = pd.read_csv(f"{OUT_DIR}/appended.csv")
    appended_amount_dtype = str(reread_appended["amount"].dtype)
    appended_row_count = len(reread_appended)
except Exception:
    appended_amount_dtype = ""
    appended_row_count = -1

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
    check("Exercise 1: index=False writes no extra index column",
          lambda: "Unnamed: 0" not in correct_cols
          and correct_cols == ["order_id", "customer", "amount", "order_date"]),
    check("Exercise 2: the default (index=True) DOES write a junk 'Unnamed: 0' column",
          lambda: "Unnamed: 0" in wrong_cols),
    check("Exercise 3: plain read_csv() silently demotes order_date to a string dtype",
          lambda: plain_date_dtype in ("object", "str")),
    check("Exercise 4: parse_dates= restores the real datetime64 dtype",
          lambda: plain_date_dtype != parsed_date_dtype and "datetime64" in parsed_date_dtype),
    check("Exercise 5: appending without header=False silently corrupts 'amount' to text",
          lambda: appended_amount_dtype in ("object", "str")
          and appended_row_count == 2 * len(clean) + 1),
]

shutil.rmtree(OUT_DIR, ignore_errors=True)

print("\nAll green — lesson 64 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
