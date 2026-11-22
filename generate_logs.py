
import random
from datetime import datetime, timedelta

# ==========================================
# BREW & BEAN CAFE
# SECURITY LOG GENERATOR
# Generate 500 simulated web server log entries
# ==========================================

# Sample IP addresses
normal_ips = [
    "192.168.1.10",
    "192.168.1.15",
    "192.168.1.20",
    "10.0.0.5"
]

suspicious_ips = [
    "185.220.101.10",
    "45.155.205.15",
    "103.75.201.22"
    "192.168.1.25"
]

all_ips = normal_ips + suspicious_ips

# HTTP status codes
status_codes = [200, 200, 200, 301, 404]

# Normal and suspicious request paths
normal_paths = [
    "/",
    "/login",
    "/products",
    "/inventory",
    "/menu",
    "/checkout",
    "/about"
]

attack_paths = [
    "/../../etc/passwd",
    "/../../etc/shadow",
    "/admin",
    "/login",
    "/../../windows/system32"
]

# Starting timestamp
start_time = datetime.now() - timedelta(days=1)

logs = []

# Generate 500 log entries
for i in range(500):

    # Random IP address
    ip = random.choice(all_ips)

    # Random timestamp
    timestamp = start_time + timedelta(
        seconds=random.randint(0, 86400)
    )

    # Select request and status
    if ip in suspicious_ips:
        path = random.choice(attack_paths)
        status = random.choice([401, 401, 401, 403, 404])
    else:
        path = random.choice(normal_paths)
        status = random.choice(status_codes)

    # Create web server log entry
    log_entry = (
        f'{ip} - - '
        f'[{timestamp.strftime("%d/%b/%Y:%H:%M:%S +0000")}] '
        f'"GET {path} HTTP/1.1" '
        f'{status} {random.randint(100, 5000)}'
    )

    logs.append(log_entry)

# Save logs into access.log
with open("access.log", "w", encoding="utf-8") as file:
    for log in logs:
        file.write(log + "\n")

print("===================================")
print("BREW & BEAN CAFE LOG GENERATOR")
print("===================================")
print("Total log entries generated:", len(logs))
print("File created successfully: access.log")
print("===================================")
