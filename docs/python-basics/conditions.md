# Conditions

**Goal:** choose which instructions run based on a condition.

An `if` statement checks a true/false expression. Its body is indented four spaces. `elif` checks another case; `else` handles what remains.

~~~python
status_code = 401
if status_code == 200:
    print("Request succeeded")
elif status_code == 401:
    print("Authentication is required")
else:
    print("Another status code")
~~~

Only one matching branch runs. The colon `:` starts the indented block. Indentation is part of Python syntax.

**Security connection:** a program can label a known status code, but a 401 response alone does not explain why a request failed or prove malicious activity.

**Common mistakes:** forgetting the colon; inconsistent indentation (`IndentationError`); using `=` where `==` belongs; making a later branch unreachable by putting a broad condition first.

**Exercises:** print “review” when a made-up failure count is at least 3; label a number as positive, negative, or zero; handle HTTP status 200, 404, and all others. Guidance: use `if`, `elif`, and `else` in that order.
