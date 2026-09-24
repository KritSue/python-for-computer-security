# Sets

**Goal:** keep unique values and compare groups.

A set contains unique items and does not promise a useful display order. It is handy for removing duplicates or asking whether a value is already present.

~~~python
seen_users = {"alex", "sam", "alex"}
print(len(seen_users))
seen_users.add("lee")
print("sam" in seen_users)
~~~

There are two unique users initially, so the first output is 2; membership prints True. An empty set is set(); {} creates an empty dictionary. Set operations include intersection (a & b), union (a | b), and difference (a - b).

**Security connection:** compare synthetic sets of usernames to identify overlap. A set is not an audit trail because it discards duplicate events and order.

**Common mistakes:** relying on order; using {} for an empty set; converting event records to a set and losing repeated records.

**Exercises:** find unique sample IP strings; find users present in both groups; preserve a separate list if event order matters. Guidance: use set(...), &, and keep duplicates in the original list.
