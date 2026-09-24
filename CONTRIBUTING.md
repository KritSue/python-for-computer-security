# Contributing

Corrections and beginner-friendly improvements are welcome. Keep examples runnable with Python 3.10 or newer, explain new terminology, and use synthetic or authorized data. Network exercises must stay on localhost or a clearly authorized service. Do not contribute malware, credential theft, persistence, destructive tooling, or unauthorized exploitation.

## Preview changes

```console
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
mkdocs serve
```

Open the local address printed by MkDocs. Before opening a pull request, run `mkdocs build --strict` and run any changed examples with the documented Python version.
