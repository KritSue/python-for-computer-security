# Tuples and comprehensions

**Goal:** understand fixed groups and a compact way to build a collection.

A tuple is an ordered group that is not meant to be changed after creation. Comprehensions build a collection from an existing sequence.

~~~python
event = ("casey", "failed", 401)
username, result, status = event
print(username, result, status)

failure_codes = [code for code in [200, 401, 404, 401] if code >= 400]
print(failure_codes)
~~~

The comprehension is equivalent to looping through codes, checking each one, and appending matches. Use the expanded loop while learning; use the compact form only when readable.

**Security connection:** tuples can represent a small fixed record, though a dictionary is often clearer when fields need names.

**Common mistakes:** trying to assign to a tuple position; writing an overly dense comprehension; forgetting a one-item tuple needs a comma, such as (401,).

**Exercises:** unpack a 3-item tuple; use a comprehension to keep even numbers; rewrite it as a normal loop. Guidance: place the output expression first, then for, then optional if.
