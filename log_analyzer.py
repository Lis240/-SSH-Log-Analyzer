import re
from collections import Counter

def parse_auth_log(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    failed_logins = []
    suspicious_users = []

    for line in lines:
        # Match lines with "Failed password"
        if "Failed password" in line:
            # Extract IP
            ip_match = re.search(r'from ([\d.]+)', line)
            if ip_match:
                failed_logins.append(ip_match.group(1))

            # Extract username
            user_match = re.search(r'for (invalid user )?(\w+)', line)
            if user_match:
                suspicious_users.append(user_match.group(2))

    return failed_logins, suspicious_users

def display_results(failed_ips, users):
    ip_counter = Counter(failed_ips)
    user_counter = Counter(users)

    print("\n🔐 Top 5 attacking IP addresses:")
    for ip, count in ip_counter.most_common(5):
        print(f" - {ip}: {count} attempts")

    print("\n👤 Most targeted usernames:")
    for user, count in user_counter.most_common(5):
        print(f" - {user}: {count} attempts")

if __name__ == "__main__":
    path = input("Enter path to auth.log file: ")
    try:
        ips, users = parse_auth_log(path)
        display_results(ips, users)
    except FileNotFoundError:
        print("File not found. Please check the path.")
