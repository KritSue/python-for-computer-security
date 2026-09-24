# Modules, packages, and pip

**Goal:** reuse Python code and understand add-on libraries.

A module is a Python file containing reusable code. A package groups modules. Python includes a standard library with pathlib, csv, json, re, hashlib, ipaddress, and socket.

~~~python
from ipaddress import ip_address

address = ip_address("192.0.2.10")
print(address.version)
~~~

import makes module names available. Third-party packages are installed separately, commonly with python -m pip install package-name. pip downloads and manages Python packages. Use a virtual environment so packages for one project stay separate.

**Security connection:** prefer the standard IP parser over inventing your own. Third-party code becomes part of your software supply chain, so install only what a task needs.

**Common mistakes:** naming your file json.py or socket.py and shadowing a standard module; installing into one environment and running another; copying unknown install commands.

**Exercises:** import Path; find a standard-library module for JSON; create a helper module with one function and import it from a neighboring script.
