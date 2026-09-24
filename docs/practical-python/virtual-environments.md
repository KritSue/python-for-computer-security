# Virtual environments and command-line arguments

**Goal:** keep project packages separate and let a script accept a file path.

A virtual environment is a private Python package area for one project. Create it from the repository folder with python -m venv .venv, then activate it:

~~~console
# Windows PowerShell
.venv\Scripts\Activate.ps1
# macOS/Linux
source .venv/bin/activate
~~~

Install website requirements with python -m pip install -r requirements.txt. Use deactivate to leave the environment. A command-line argument is extra text given when starting a script. Python's argparse module helps read it:

~~~python
import argparse

parser = argparse.ArgumentParser(description="Summarize a sample log")
parser.add_argument("log_file", help="path to an authorized log file")
args = parser.parse_args()
print("Would summarize:", args.log_file)
~~~

Run it with python script.py examples/data/sample.log. Do not point it at private files without authorization.

**Common mistakes:** forgetting to activate the environment; using pip for the wrong interpreter (prefer python -m pip); running without the required argument.

**Exercises:** create and activate .venv; run python script.py --help; add an optional --limit integer argument.
