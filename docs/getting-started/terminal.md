# Terminal basics

**Goal:** move into a folder and run a Python script by typing a command.

A terminal is a text-based way to give commands to your computer. A command is an instruction such as “show the files here.” It is separate from Python code: `python hello.py` is a terminal command, while `print("Hi")` belongs inside a `.py` file.

Open the VS Code terminal using **Terminal → New Terminal**. It starts in the folder you opened. List the files with `dir` in Windows PowerShell or `ls` on macOS/Linux. To run your saved file, enter the appropriate command:

```console
py hello.py
```

On macOS/Linux, use `python3 hello.py`; if your installation uses `python`, that also works. You should see the printed greeting.

| Word | Meaning |
|---|---|
| folder / directory | A place that contains files and other folders |
| current folder | The folder where the terminal is looking right now |
| path | The address that identifies a file or folder |
| command | Text typed into the terminal for the computer to act on |

**Common mistake:** `can't open file` usually means Python is looking in the wrong folder or the filename differs. Run `dir`/`ls` to see whether the file is there.

**Try it:** run `py --version` (or `python3 --version`) and then run `hello.py`. The first command checks the interpreter; the second runs your program.
