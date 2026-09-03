# Practice 37 — Descriptors: how @property and @classmethod actually work
# Run:  cd ~/learning/python && uv run python3 practice/37_descriptors.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓.


# ---------------------------------------------------------------------------
# Exercise 1 — a reusable validated-attribute descriptor.
# Write NonNegative as a data descriptor: __set_name__ stores the attribute
# name (and a "_"-prefixed private name to store the real value under),
# __get__ returns the stored value, and __set__ raises ValueError if value
# is negative, otherwise stores it. One descriptor class, reused for two
# differently-named attributes on Inventory below (quantity and restock_at).
class NonNegative:
    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = "_" + name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        # TODO: if value < 0, raise ValueError(f"{self.public_name} can't be negative")
        # otherwise, setattr(obj, self.private_name, value)
        ...


class Inventory:
    quantity = NonNegative()
    restock_at = NonNegative()

    def __init__(self, quantity, restock_at):
        self.quantity = quantity
        self.restock_at = restock_at


def run_validated_descriptor():
    inv = Inventory(10, 3)
    try:
        inv.quantity = -1
        raised = False
    except ValueError:
        raised = True
    return inv.quantity, inv.restock_at, raised


# ---------------------------------------------------------------------------
# Exercise 2 — data descriptor beats instance __dict__; non-data loses to it.
# DataDesc defines both __get__ and __set__ (a data descriptor).
# NonDataDesc defines only __get__ (a non-data descriptor).
# Fill in both __get__ bodies to return the given marker strings, then
# confirm (via the check below) that writing straight into an instance's
# own __dict__ under the same name still loses to DataDesc, but wins over
# NonDataDesc.
class DataDesc:
    def __get__(self, obj, objtype=None):
        return "from DataDesc"

    def __set__(self, obj, value):
        pass  # defining __set__ at all is what makes this a data descriptor


class NonDataDesc:
    def __get__(self, obj, objtype=None):
        # TODO: return "from NonDataDesc"
        ...


class Holder:
    data_attr = DataDesc()
    nondata_attr = NonDataDesc()


def run_data_vs_nondata():
    h = Holder()
    h.__dict__["data_attr"] = "instance value"
    h.__dict__["nondata_attr"] = "instance value"
    return h.data_attr, h.nondata_attr


# ---------------------------------------------------------------------------
# Exercise 3 — property is a data descriptor, confirmed by introspection.
# Return a tuple of three booleans: whether property defines __get__,
# whether it defines __set__, and whether it defines __delete__.
def property_descriptor_methods():
    # TODO: return (hasattr(property, "__get__"),
    #               hasattr(property, "__set__"),
    #               hasattr(property, "__delete__"))
    ...


def run_property_check():
    return property_descriptor_methods()


# ---------------------------------------------------------------------------
# Exercise 4 — tell classmethod and staticmethod apart from __get__ behavior.
# Both are non-data descriptors (only __get__, no __set__). Given the class
# below, report which stdlib decorator each of `built` and `helped` needs
# by returning the two decorator names as strings: "classmethod" for the
# method that must receive the class itself, "staticmethod" for the one
# that takes no automatic first argument at all.
class Widget:
    def __init__(self, label):
        self.label = label

    # `built` should build and return a new Widget — it needs the class.
    @classmethod
    def built(cls, label):
        return cls(label)

    # `helped` should just double a number — it needs neither self nor cls.
    @staticmethod
    def helped(x):
        return x * 2


def which_decorator(name):
    # TODO: return "classmethod" if name == "built" else "staticmethod"
    ...


def run_which_decorator():
    return which_decorator("built"), which_decorator("helped")


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
    check("Ex 1: NonNegative validates on write, stores per attribute name",
          lambda: run_validated_descriptor() == (10, 3, True)),
    check("Ex 2: data descriptor wins over instance dict, non-data loses",
          lambda: run_data_vs_nondata() == ("from DataDesc", "instance value")),
    check("Ex 3: property defines __get__, __set__, and __delete__",
          lambda: run_property_check() == (True, True, True)),
    check("Ex 4: classmethod for built, staticmethod for helped",
          lambda: run_which_decorator() == ("classmethod", "staticmethod")),
]
print("\nAll green — lesson 37 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
