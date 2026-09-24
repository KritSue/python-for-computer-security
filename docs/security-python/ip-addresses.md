# IP addresses with Python

**Goal:** validate an address's format using Python's standard library.

IPv4 addresses contain four decimal numbers separated by dots, such as the documentation-only address 192.0.2.10. IPv6 uses a longer colon-separated format. Python's ipaddress module parses both correctly.

~~~python
from ipaddress import ip_address

candidate = "192.0.2.10"
try:
    address = ip_address(candidate)
except ValueError:
    print("Not a valid IP address")
else:
    print("Valid address version:", address.version)
~~~

Parsing checks whether the text represents an IP address. It does not prove the address is active, safe, reachable, or yours. Use the loopback address 127.0.0.1 for local networking labs.

**Common mistakes:** splitting on dots and accepting malformed ranges; confusing validation with a network connection; treating private, public, and documentation ranges as identical.

**Exercises:** validate one IPv4 and one IPv6 sample; handle invalid text; print whether 127.0.0.1 is loopback. Guidance: parse first, then inspect the resulting object's properties.
