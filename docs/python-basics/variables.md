# Variables and input/output

**Goal:** store a value under a readable name and display it.

A variable is a name that refers to a value. Think of it as a labeled place your program can look up. The `=` symbol assigns a value; it does not mean “is equal to” in a math equation.

~~~python
username = "maya"
failed_logins = 3
print(username)
print("Failed attempts:", failed_logins)
~~~

Expected output:

~~~text
maya
Failed attempts: 3
~~~

Names are case-sensitive: `count` and `Count` differ. Use lowercase words joined by underscores, such as `event_count`. A name cannot start with a number. `input()` displays a prompt and returns what the person typed as text:

~~~python
name = input("Your name: ")
print("Hello", name)
~~~

**Security example:** store a made-up username or event count in a variable. Never put a real password or API key in a source file.

**Common mistakes:** using a name before assigning it (`NameError`); confusing `=` assignment with `==` comparison; expecting `input()` to produce a number automatically.

**Exercises:** store an IP address as text and print it; ask for a username; store a count and print a sentence containing it. Guidance: use quotes around text and no quotes around a number.
