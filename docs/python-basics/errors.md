# Errors and exceptions

**Goal:** recognize common errors and handle expected bad input without hiding problems.

An error is information that something prevented the program from continuing correctly. A syntax error means Python cannot understand the code. A runtime exception occurs while it runs. A traceback shows where the exception happened; start by reading its final line.

`try` and `except` let you handle a specific expected problem:

~~~python
text = input("Enter a whole number: ")
try:
    count = int(text)
except ValueError:
    print("Please enter digits such as 3")
else:
    print("Next count:", count + 1)
~~~

`ValueError` means the conversion could not use the supplied text. `else` runs only when the `try` block succeeded. Avoid a bare `except:` because it can conceal programming mistakes.

**Security connection:** malformed records are normal when reading files. Handle a known bad field and report which record needs review; do not silently discard every error.

**Common mistakes:** catching too broadly; putting unrelated code inside `try`; printing “success” after a failed conversion.

**Exercises:** handle an invalid integer; handle a missing optional file using `FileNotFoundError`; explain a `NameError` by finding the misspelled name. Guidance: catch only the exception you expect.
