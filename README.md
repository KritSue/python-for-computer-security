# Python for Computer Security

**Learn Python from zero, then apply it to practical defensive security.** This free course begins with a first program and builds toward safe networking examples, synthetic log analysis, secure coding, guided labs, and small automation projects.

[Start the course](https://kritsue.github.io/python-for-computer-security/) · [View the roadmap](https://kritsue.github.io/python-for-computer-security/roadmap/) · [Browse the labs](https://kritsue.github.io/python-for-computer-security/labs/) · [View the repository](https://github.com/KritSue/python-for-computer-security)

## Who this is for

Complete beginners are welcome. You do not need previous programming, terminal, Git, or networking experience. Start with the setup pages and move through the course in order. Examples are written for Python 3.10+ using invented data; networking labs use localhost or an explicitly authorized system.

## Learning path

1. **Get set up:** [install Python](docs/getting-started/install-python.md), [set up VS Code](docs/getting-started/vscode.md), learn [terminal basics](docs/getting-started/terminal.md), and run [your first program](docs/getting-started/first-program.md).
2. **Learn Python fundamentals:** values, conditions, loops, functions, and errors in [Python Basics](docs/python-basics/variables.md).
3. **Work with data:** lists and dictionaries, then files, CSV, JSON, and regex in [Data Structures](docs/data-structures/lists.md) and [Practical Python](docs/practical-python/files.md).
4. **Use Python tooling:** modules, packages, virtual environments, and command-line arguments in [Practical Python](docs/practical-python/modules.md).
5. **Build networking foundations:** IP addresses, sockets, and HTTP in [Python for Computer Security](docs/security-python/networking-basics.md).
6. **Apply Python defensively:** hashing, secure coding, and synthetic log analysis in [Security Python](docs/security-python/hashing.md).
7. **Practice:** complete the [labs](docs/labs/index.md), then choose a [mini project](docs/mini-projects/index.md).

The [full roadmap](docs/roadmap.md) includes an eight-week plan and checkpoints.

## Hands-on practice

Ten guided [labs](docs/labs/index.md) progress from printing text to parsing invented security events, hashing a sample file, and inspecting a local HTTP or socket service. The [mini projects](docs/mini-projects/index.md) offer a local log summary, file-integrity manifest, or loopback HTTP metadata report. Try each [exercise](docs/exercises/index.md) before opening its [worked solution](docs/exercises/solutions.md).

## Run an example

From the repository folder, run `python examples/hello.py` (Windows may use `py` instead of `python`). Run a lab with `python examples/ip_validator.py`. These examples need no third-party Python packages.

## Preview the website locally

Install Python, open a terminal in this folder, then run:

```console
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
mkdocs serve
```

Open the local URL printed in the terminal. To build exactly as CI does, run `mkdocs build --strict`; generated pages go into `site/`.

## Safety and ethical use

Security activities are educational and defensive. Use network examples only on localhost or systems you own or are explicitly authorized to inspect. Never commit real secrets or personal log data. Course examples use synthetic data.

## Contributing and license

Corrections and beginner-friendly improvements are welcome; see [CONTRIBUTING.md](CONTRIBUTING.md). Course text, examples, and configuration use the [MIT License](LICENSE); third-party dependencies keep their own licenses.

Explore more engineering work on my [GitHub profile](https://github.com/KritSue).
