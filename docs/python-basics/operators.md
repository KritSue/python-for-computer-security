# Operators and comparisons

**Goal:** calculate values and ask true/false questions about them.

Arithmetic operators include `+`, `-`, `*`, and `/`. Comparisons include `==` (equal), `!=` (not equal), `<`, `<=`, `>`, and `>=`. A comparison produces `True` or `False`.

~~~python
event_count = 8
limit = 5
print(event_count + 2)
print(event_count > limit)
print(event_count == 8)
~~~

Output is `10`, `True`, and `True`. Use `and`, `or`, and `not` to combine true/false values:

~~~python
failed = 4
locked = failed >= 5
review = failed >= 3 and not locked
print(review)
~~~

**Security example:** comparisons can flag a synthetic event count for review. A threshold is an alerting rule, not proof that an account is under attack.

**Common mistakes:** use `==` to compare, not `=`; write `and`/`or` between complete conditions; remember division `/` produces a decimal number.

**Exercises:** check whether `status_code` equals 401; check whether `count` is from 1 through 4; combine “event is failed” and “source is local.” Guidance: use `and` for both conditions to be true.
