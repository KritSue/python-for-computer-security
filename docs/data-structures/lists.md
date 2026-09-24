# Lists and slicing

**Goal:** keep an ordered collection and select parts of it.

A list stores items in order. Use square brackets and commas. Positions start at zero.

~~~python
addresses = ["192.0.2.10", "198.51.100.7", "203.0.113.4"]
print(addresses[0])
addresses.append("192.0.2.11")
print(len(addresses))
~~~

These addresses are reserved for documentation examples. append adds an item; len counts items. Slicing selects a range: addresses[0:2] gets positions 0 and 1 (the ending index is not included), addresses[:2] starts at the beginning, and addresses[-1] gets the final item.

~~~python
for address in addresses:
    print(address)
~~~

**Security connection:** lists can hold usernames, status codes, or event rows. A list does not validate an IP address; use the ipaddress module for that.

**Common mistakes:** position 1 is the second item; accessing past the end causes IndexError; mixing text and numbers without reason makes later processing harder.

**Exercises:** add one sample address; print the first two items; count status codes above 399. Guidance: use append, a slice, and a loop with a counter.
