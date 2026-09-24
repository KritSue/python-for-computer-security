# Data types

**Goal:** recognize the basic kinds of values Python can work with.

The type tells Python what kind of value it has. The four common beginner types are text (`str`), whole number (`int`), decimal number (`float`), and true/false (`bool`).

~~~python
username = "sam"          # str: text
failed_count = 4          # int: whole number
response_time = 0.25      # float: decimal number
is_authorized = True      # bool: True or False
print(type(username))
~~~

`type(...)` reports a value's type. Text needs quotation marks. Boolean values use capital `T` and `F`. Convert text to a number with `int("4")` or `float("0.25")` when appropriate.

~~~python
attempts = int(input("Number of attempts: "))
print(attempts + 1)
~~~

**Security connection:** an IP address is commonly kept as text until you use a networking tool to interpret it. A count is an integer. A flag such as `is_blocked` is a boolean.

**Common mistakes:** adding a number to text (`TypeError`); converting nonnumeric input (`ValueError`); writing `true` instead of `True`. `input()` always returns a string.

**Exercises:** identify the type of `"200"`, `200`, `200.0`, and `False`; convert a typed value to an integer; predict `"2" + "3"` versus `2 + 3`. Guidance: the first combines text to `23`; the second adds to `5`.
