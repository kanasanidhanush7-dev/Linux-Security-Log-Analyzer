# Linux Security Log Analyzer

A Python-based security log analysis tool that analyzes Linux authentication logs, detects suspicious SSH login activity, and generates a security report.

## Features

- Detects failed SSH login attempts
- Extracts timestamps from authentication logs
- Extracts source IP addresses
- Counts failed login attempts by IP address
- Detects suspicious IP addresses based on a configurable threshold
- Extracts attempted usernames
- Creates detailed SSH security events
- Detects errors and warnings
- Generates a structured security report
- Supports command-line log file input
- Uses modular Python components

## Technologies Used

- Python 3
- Regular Expressions (`re`)
- Argparse
- File Handling
- Dictionaries
- Lists
- Functions
- Modular Python Programming

## Project Structure

```text
Linux-Security-Log-Analyzer/
│
├── main.py
├── log_analyzer.py
├── report_generator.py
├── sample_auth.log
├── .gitignore
└── README.md
```

## How It Works

The application follows three main steps:

```text
Linux Authentication Log
          │
          ▼
     Log Analyzer
          │
          ▼
   Security Analysis
          │
          ▼
  Report Generator
          │
          ▼
    Security Report
```

### 1. Log Analysis

`log_analyzer.py` reads the authentication log and extracts:

- Failed login attempts
- IP addresses
- Usernames
- Timestamps
- Security events
- Errors
- Warnings

### 2. Security Analysis

The analyzer counts failed login attempts for each IP address.

By default, an IP address with **5 or more failed attempts** is marked as suspicious.

### 3. Report Generation

`report_generator.py` creates a structured security report containing:

- Total failed SSH attempts
- IP addresses
- IP attack frequency
- Suspicious IP addresses
- Failed-login timestamps
- SSH security events
- Errors
- Warnings

## How to Run

### Clone the Repository

```bash
git clone https://github.com/kanasanidhanush7-dev/Repository-name-Linux-Security-Log-Analyzer.git
```

### Move into the Project Directory

```bash
cd Repository-name-Linux-Security-Log-Analyzer
```

### Run the Analyzer

The repository includes a safe sample authentication log for testing.

```bash
python main.py --log "sample_auth.log"
```

Then select:

```text
1. Analyze Log File
2. Generate Security Report
3. Exit
```

Select option `1` to analyze the log file.

Select option `2` to generate the security report.

## Example Output

```text
==================================================
       LINUX SECURITY LOG ANALYZER
==================================================

1. Analyze Log File
2. Generate Security Report
3. Exit

Enter your choice: 1

Analyzing log file...

Analysis completed successfully!
```

A security report is generated after selecting option `2`.

### Example Security Report

```text
1. FAILED SSH LOGIN ATTEMPTS

Total Failed Attempts: 8

3. IP ATTACK FREQUENCY

192.168.1.50 → 6 failed attempts
192.168.1.51 → 1 failed attempts
10.0.0.15 → 1 failed attempts

4. SUSPICIOUS IP ADDRESSES

🚨 192.168.1.50 → 6 failed attempts (SUSPICIOUS)
```

## Purpose

This project was created as a practical Python and Linux security project to demonstrate:

- Log analysis
- Basic security monitoring
- Python file handling
- Regular expression processing
- Data extraction
- Security-event detection
- Modular programming
- Command-line application development

## Future Improvements

Planned improvements include:

- Real-time log monitoring
- Multiple log format support
- CSV/JSON report generation
- Email alerts for suspicious activity
- IP geolocation
- Graphical statistics
- Improved command-line options
- Additional Linux security event detection

## Author

**K. Venkata Dhanush**

GitHub:

https://github.com/kanasanidhanush7-dev

## License

This project is for educational and portfolio purposes.
