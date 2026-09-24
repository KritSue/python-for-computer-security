# Mini projects

Choose a project after completing the labs. Start small: write down the input, output, and one limitation before writing code.

## 1. Local log summary

Read a synthetic CSV file, count outcomes by type, and write a JSON summary. Add clear handling for missing columns and malformed rows. Include total rows, processed rows, and skipped rows.

## 2. File integrity manifest

Calculate SHA-256 digests for files in a folder of sample files, then compare a later run. Restrict paths to a folder you created for the exercise. Explain that the manifest must be protected separately to provide trustworthy comparison.

## 3. Local HTTP metadata report

Start the provided loopback server and request its root page. Report status and a small allowlist of non-sensitive headers. Add timeouts and explain that metadata does not prove content is safe.

## Project checklist

- Explain how to run the program and provide synthetic sample data.
- Handle missing or malformed input without hiding errors.
- Avoid secrets and unnecessary personal data.
- Keep any network destination explicit and authorized.
- Describe what the output can and cannot conclude.
