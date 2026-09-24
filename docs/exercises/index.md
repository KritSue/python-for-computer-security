# Exercises

Try these without opening the [worked solutions](solutions.md). Write your answer or script in a separate file. Use the [glossary](../glossary.md) when a term is new.

## Beginner

1. Store a sample username and print a greeting.
2. Convert typed text to an integer and print the next number; handle invalid input.
3. Use an if statement to label a made-up event as failed or successful.
4. Loop over three documentation IP addresses and print each one.
5. Write a function that returns whether a number is at least five.

## Practice

1. Count failed items in a list of result strings.
2. Count failed events per username using a dictionary.
3. Read `examples/data/failed_logins.csv` and count rows with result `failed`.
4. Parse `examples/data/events.json`, print IDs of high severity events, and handle a missing severity.
5. Validate each candidate in `examples/data/ip_candidates.txt` with `ipaddress`.

## Challenge

1. Parse each line in the synthetic sample log and count malformed lines separately.
2. Write a command-line program that accepts a JSON file path and an optional threshold, then reports counts only.
3. Extend defensive_monitor.py to write a JSON summary with event totals and malformed-record count.
4. Write a short README for your tool that states its input format, limits, and safe use.

For each task, test a normal case, an empty input, and a malformed input. Compare your program's behavior to the problem statement before polishing it.
