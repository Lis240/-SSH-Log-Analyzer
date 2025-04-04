# 🛡️ SSH Log Analyzer (auth.log)

A simple Python tool to analyze `auth.log` files (Linux) and detect suspicious login attempts.

## 🚀 Features

- Detects failed SSH login attempts
- Lists most common attacking IPs
- Identifies usernames targeted by brute-force attempts

## 🧪 Example Output
Enter path to auth.log file: /var/log/auth.log

🔐 Top 5 attacking IP addresses:
192.168.1.100: 34 attempts
203.0.113.5: 12 attempts

👤 Most targeted usernames:
root: 20 attempts
admin: 15 attempts



## 🧰 How to Use

1. Save the script as `log_analyzer.py`
2. Run it:

```bash
python log_analyzer.py
