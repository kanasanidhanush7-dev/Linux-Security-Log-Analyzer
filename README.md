# Linux Security Log Analyzer

A Python-based security log analysis tool that analyzes Linux authentication logs and generates a security report.

## Features

- Detects failed SSH login attempts
- Extracts IP addresses
- Counts failed attempts from each IP address
- Identifies suspicious IP addresses
- Extracts usernames
- Extracts failed-login timestamps
- Creates detailed SSH security events
- Detects errors and warnings
- Generates a security report
- Command-line log file support

## Technologies Used

- Python 3
- Regular Expressions (`re`)
- Argparse
- File Handling
- Dictionaries
- Lists
- Functions
- Modular Python programming

## Project Structure

```text
Linux-Security-Log-Analyzer/
│
├── main.py
├── log_analyzer.py
├── report_generator.py
├── .gitignore
└── README.md
```
