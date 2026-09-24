# Loops

**Goal:** repeat instructions for each item or a fixed number of times.

A loop avoids copying the same instruction many times. A `for` loop visits items in a sequence. `range(3)` produces the numbers 0, 1, 2.

~~~python
usernames = ["alex", "lee", "morgan"]
for username in usernames:
    print("Review account:", username)
~~~

The indented body runs once for each item. A `while` loop repeats while its condition stays true:

~~~python
attempt = 1
while attempt <= 3:
    print("Attempt", attempt)
    attempt = attempt + 1
~~~

Update a `while` condition's values so it eventually becomes false, or the loop may never stop.

**Security connection:** loops can count matching synthetic log events. Keep the input file and summary bounded so an accidental loop is easy to stop and understand.

**Common mistakes:** forgetting the colon or indentation; changing a list while iterating over it; forgetting to increment a `while` counter.

**Exercises:** print each of three sample IP strings; count numbers over 10 in a list; use `range(1, 4)` to print three steps. Guidance: make a counter variable and update it inside the loop.
