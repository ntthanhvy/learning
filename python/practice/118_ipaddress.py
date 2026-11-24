# Practice 118 — ipaddress: IP addresses as real objects, not strings
# Run:  cd ~/learning/python && uv run python3 practice/118_ipaddress.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `pass`/TODO body and re-run until every check prints ✓.
# Try each from memory before reopening the lesson.

import ipaddress


# ---------------------------------------------------------------------------
# Exercise 1 — separate genuinely valid IP strings from invalid ones.
# Write split_valid(candidates) that returns a tuple (valid, invalid) of two
# lists: `valid` holds each string from `candidates` that
# ipaddress.ip_address() can parse without raising, in original order;
# `invalid` holds every string that raises ValueError, in original order.
def split_valid(candidates):
    # TODO: walk candidates, try ipaddress.ip_address(c) in a try/except
    # ValueError, and append c to `valid` or `invalid` accordingly.
    pass


# ---------------------------------------------------------------------------
# Exercise 2 — check whether an address falls inside a CIDR range.
# Write address_in_range(address_str, cidr_str) that returns True if
# ipaddress.ip_address(address_str) is a member of
# ipaddress.ip_network(cidr_str) (use the `in` operator), False otherwise.
def address_in_range(address_str, cidr_str):
    # TODO: return ipaddress.ip_address(address_str) in ipaddress.ip_network(cidr_str)
    pass


# ---------------------------------------------------------------------------
# Exercise 3 — build a network from an address that isn't the range's exact
# start, without raising.
# Write network_from_any_address(address_with_prefix) that returns the
# ipaddress.ip_network() built from a string like "192.168.1.5/24", using
# strict=False so a non-start address rounds down to the range's real start
# instead of raising ValueError.
def network_from_any_address(address_with_prefix):
    # TODO: return ipaddress.ip_network(address_with_prefix, strict=False)
    pass


# ---------------------------------------------------------------------------
# Checks — don't edit below this line.
def check(name, cond):
    try:
        ok = bool(cond())
    except Exception:
        ok = False
    print(("✓" if ok else "✗"), name)
    return ok


def _ex1():
    candidates = ["192.168.1.10", "192.168.1.999", "10.0.0.1", "not-an-ip", "::1"]
    valid, invalid = split_valid(candidates)
    return (
        valid == ["192.168.1.10", "10.0.0.1", "::1"]
        and invalid == ["192.168.1.999", "not-an-ip"]
    )


def _ex2():
    return (
        address_in_range("192.168.1.10", "192.168.1.0/24") is True
        and address_in_range("192.168.2.1", "192.168.1.0/24") is False
        and address_in_range("192.168.1.255", "192.168.1.0/24") is True
    )


def _ex3():
    net = network_from_any_address("192.168.1.5/24")
    return str(net) == "192.168.1.0/24" and net.num_addresses == 256


results = [
    check("Ex 1: split_valid separates valid IPs from invalid strings", _ex1),
    check("Ex 2: address_in_range checks CIDR membership with `in`", _ex2),
    check("Ex 3: network_from_any_address rounds down with strict=False", _ex3),
]
print("\nAll green — lesson 118 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
