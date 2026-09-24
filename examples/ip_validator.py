"""Validate sample IP address syntax; this does not test reachability."""

from ipaddress import ip_address

candidates = ["192.0.2.10", "2001:db8::1", "999.1.1.1", "not-an-address"]
for candidate in candidates:
    try:
        address = ip_address(candidate)
    except ValueError:
        print(candidate, "-> invalid")
    else:
        print(f"{candidate} -> IPv{address.version}")
