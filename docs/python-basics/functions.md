# Functions and scope

**Goal:** package a named set of steps so it can be reused.

A function is a small named task. Define one with `def`. Inputs in parentheses are parameters. `return` sends a result back to the code that called the function.

~~~python
def is_failed_login(status_code):
    return status_code == 401

event_needs_review = is_failed_login(401)
print(event_needs_review)
~~~

Output: `True`. A parameter such as `status_code` is available inside the function. This limited availability is called **scope**. Names created inside a function are usually local to it.

~~~python
def count_failures(events):
    total = 0
    for event in events:
        if event == "failed":
            total += 1
    return total
~~~

**Security connection:** a function lets you test one clear rule, such as deciding whether an event's result is `"failed"`, then reuse it consistently.

**Common mistakes:** defining a function but never calling it; confusing `print` (shows a value) with `return` (gives a value back); inconsistent indentation; expecting a local variable outside its function.

**Exercises:** write `is_private_label(label)` for one known label; write a function that returns the larger of two counts; write `count_failed(events)`. Guidance: return a boolean for the first and a number for the last.
