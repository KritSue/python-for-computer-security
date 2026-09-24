# Python for Computer Security

A free, beginner-first course for an MSc Computer Security student starting with **zero programming experience**. It begins with installing Python and running one file, then builds toward defensive log analysis and safe networking examples.

## Who this is for

You do not need previous programming, terminal, Git, or networking experience. You need a computer where you can install Python and a text editor. Examples are written for Python 3.10+; the networking labs use localhost and the course data is synthetic.

## Start here

1. Read the [learning roadmap](docs/roadmap.md).
2. Follow [Install Python](docs/getting-started/install-python.md), [VS Code](docs/getting-started/vscode.md), and [Terminal basics](docs/getting-started/terminal.md).
3. Run [your first program](docs/getting-started/first-program.md).
4. Work through each section in order. Try the [exercises](docs/exercises/index.md) before opening [solutions](docs/exercises/solutions.md).

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

## Roadmap

Zero programming knowledge → Python fundamentals → data structures → files, JSON, and regex → Python tooling → networking fundamentals → security Python → defensive automation → mini projects. The [roadmap page](docs/roadmap.md) includes a visual diagram and an eight-week schedule.

## GitHub Pages

The GitHub Actions workflow builds and deploys the site on pushes to `main`. Create an empty GitHub repository named `python-for-computer-security`, then from this folder connect and push the prepared local repository:

```console
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/python-for-computer-security.git
git push -u origin main
```

In GitHub, open **Settings → Pages** and set the build source to **GitHub Actions**. Replace `YOUR_GITHUB_USERNAME` in `mkdocs.yml` with your GitHub username before publishing.

## Safety and license

Security activities are educational and defensive. Use network examples only on localhost or systems you are authorized to inspect. Never commit real secrets or personal log data. Course text, examples, and configuration use the MIT License; third-party dependencies keep their own licenses.
