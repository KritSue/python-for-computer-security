# Your first program

**Goal:** run a Python instruction and tell Python data apart from a command.

Programming means describing steps clearly enough that a computer can carry them out. Python code is text saved in a file, usually with the `.py` ending.

```python
print("Hello, World!")
print("I am learning Python.")
```

`print` asks Python to display something. Parentheses hold what should be displayed. Text is written between matching quotation marks. Run `py hello.py` from the terminal in the file's folder (or use the matching command from the [terminal page](terminal.md)).

Expected output:

```text
Hello, World!
I am learning Python.
```

### Interactive Python shell

The interactive shell lets you type one Python instruction and see its result immediately. In a terminal, run `py` on Windows or `python3` on macOS/Linux. When you see `>>>`, type `print(2 + 3)` and press Enter. Python displays `5`. Type `exit()` to leave. The `>>>` prompt is not part of your Python file.

### Security connection

Tools often print a summary for a human to read. Later you might print how many failed sign-in events appeared in an authorized log. For now, printing a fixed message is enough.

**Common mistakes:** forgetting a closing quote or parenthesis causes a syntax error; typing the shell prompt `>>>` into a `.py` file also causes an error.

**Exercises:** change the greeting; add a third `print` line; predict what happens if the lines are swapped. You should see one output line per `print` instruction.
