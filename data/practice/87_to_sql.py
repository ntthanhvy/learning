# Practice 87 — df.to_sql(): writing a DataFrame into a SQL table
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/87_to_sql.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import sqlite3
import pandas as pd

# ---------------------------------------------------------------------------
# Shared fixture: an in-memory SQLite DB (stdlib sqlite3 -- no SQLAlchemy
# install needed, same approach as Lesson 86's practice file). A small
# DataFrame to write out.
_conn = sqlite3.connect(":memory:")
_df = pd.DataFrame({
    "order_id": [1, 2, 3],
    "customer": ["An", "Binh", "Chi"],
    "amount": [120.0, 35.5, 99.9],
})

# ---------------------------------------------------------------------------
# Exercise 1 — writing with index=False avoids the Section 3 trap (a junk
# "index" column). Fill in the keyword value to pass.
# ex1_index_value = False
ex1_index_value = ...
try:
    ex1_value_is_real_false = ex1_index_value is False
    _df.to_sql("orders", _conn, index=ex1_index_value)
    ex1_columns = sorted(pd.read_sql("SELECT * FROM orders", _conn).columns.tolist())
except Exception:
    ex1_value_is_real_false = False
    ex1_columns = None

# ---------------------------------------------------------------------------
# Exercise 2 — the Section 2 trap: writing to the same table name again with
# no if_exists= raises ValueError (the default is "fail"). Fill in the
# exception type that gets raised.
# ex2_exception_type = ValueError
ex2_exception_type = ...
try:
    _df.to_sql("orders", _conn, index=False)  # table already exists from Exercise 1
    ex2_raised_correct_type = False
except Exception as e:
    ex2_raised_correct_type = isinstance(e, ex2_exception_type) if ex2_exception_type is not ... else False

# ---------------------------------------------------------------------------
# Exercise 3 — if_exists="append" keeps the table and inserts more rows,
# with no uniqueness check, so writing the same 3 rows again doubles the
# row count (Section 2). Fill in the if_exists value to pass.
# ex3_if_exists = "append"
ex3_if_exists = ...
try:
    _df.to_sql("orders", _conn, index=False, if_exists=ex3_if_exists)
    ex3_row_count = len(pd.read_sql("SELECT * FROM orders", _conn))
except Exception:
    ex3_row_count = None

# ---------------------------------------------------------------------------
# Exercise 4 — the Section 4 dtype trap: a nullable Int64 column with a real
# gap, written with to_sql() then read back with plain read_sql() (no
# dtype_backend=), comes back float64, not Int64. Fill in the dtype string
# to check the round-tripped column against.
# ex4_expected_dtype = "float64"
ex4_expected_dtype = ...
try:
    _df4 = pd.DataFrame({"qty": pd.array([3, None, 1], dtype="Int64")})
    _df4.to_sql("qty_table", _conn, index=False, if_exists="replace")
    ex4_roundtrip_dtype = str(pd.read_sql("SELECT * FROM qty_table", _conn)["qty"].dtype)
    ex4_matches = ex4_roundtrip_dtype == ex4_expected_dtype
except Exception:
    ex4_roundtrip_dtype = None
    ex4_matches = None

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
    check("Exercise 1: to_sql(index=False) writes no junk index column",
          lambda: ex1_value_is_real_false is True
          and ex1_columns == ["amount", "customer", "order_id"]),
    check("Exercise 2: writing to an existing table with no if_exists= raises ValueError",
          lambda: ex2_raised_correct_type is True),
    check("Exercise 3: if_exists='append' doubles the row count (3 -> 6)",
          lambda: ex3_row_count == 6),
    check("Exercise 4: nullable Int64 round-trips through to_sql() as float64",
          lambda: ex4_matches is True and ex4_roundtrip_dtype == "float64"),
]

print("\nAll green — lesson 87 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
