# Set up VS Code

**Goal:** create and run a Python file in a code editor.

Visual Studio Code (VS Code) is an editor: a program for writing and organizing text files. Python runs your `.py` file; the editor helps you write it.

1. Install [Visual Studio Code](https://code.visualstudio.com/).
2. Open VS Code, select the Extensions icon, search for **Python** by Microsoft, and install it.
3. Make a folder named `python-practice` in a place you can find again.
4. In VS Code choose **File → Open Folder** and select `python-practice`.
5. Choose **New File**, name it `hello.py`, and type:

```python
print("Hello, Python!")
```

Save with **Ctrl+S** (Windows/Linux) or **Cmd+S** (macOS). The `.py` ending tells you this file contains Python code. The editor may offer to choose an interpreter; select your installed Python 3 version if asked.

To run it, use the terminal instructions on the [next page](terminal.md), or click the play button labeled **Run Python File**. Expected output: `Hello, Python!`.

**Common mistake:** if the filename becomes `hello.py.txt`, show file extensions in your file manager and rename it to end in `.py` only.
