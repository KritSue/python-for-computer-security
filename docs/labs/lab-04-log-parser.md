# Lab 04 — Security log parser

Use `examples/data/sample.log`, which contains only invented events and documentation-only addresses. Run `python examples/log_parser.py` to count results.

**Task:** count only failed results and report malformed lines. A substring check is a first step; for a robust parser, split fields and validate that required keys are present. A log count is a review signal, not a conclusion about intent.
