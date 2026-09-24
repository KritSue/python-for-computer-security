# Install Python

**Goal:** install the program that runs Python code and check that your computer can find it.

Python is both a language (the instructions you write) and an interpreter (the program that reads those instructions and runs them). Use Python 3.10 or newer for this course.

## Windows

1. Visit [python.org/downloads](https://www.python.org/downloads/) and download the current Python 3 installer.
2. Open the installer. Select **Add python.exe to PATH**, then choose **Install Now**.
3. Open PowerShell from the Start menu and type `py --version`, then press Enter. You should see `Python 3.x.x`.

## macOS

Download the current Python 3 installer from [python.org/downloads](https://www.python.org/downloads/). After installation, open Terminal and run `python3 --version`.

## Linux

Many Linux systems include Python 3. Check with `python3 --version`. If it is missing, use your distribution's official package manager and documentation.

!!! warning "Use Python 3"
    Python 2 is obsolete and is not suitable for this course. The version command should begin with `Python 3`.

If the command is not found, close and reopen the terminal. On Windows try `py --version`; on macOS or Linux try `python3 --version`. See the [glossary](../glossary.md) for “terminal” and “PATH.”

**Try it:** write down the full version number printed. You will use the same command (`py`, `python`, or `python3`) whenever these pages show `python`.
