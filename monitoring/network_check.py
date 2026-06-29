import requests
import time

# List of critical endpoints to check
ENDPOINTS = [
    "https://www.google.com",
    "https://www.github.com",
    "https://www.microsoft.com"
]

# Timeout for requests (in seconds)
TIMEOUT = 5

def check_endpoint(url):
    try:
        response = requests.get(url, timeout=TIMEOUT)
        if response.status_code == 200:
            print(f"✅ {url} is reachable.")
        else:
            print(f"⚠️ {url} returned status {response.status_code}.")
    except Exception as e:
        print(f"🚨 {url} is unreachable. Error: {e}")

if __name__ == "__main__":
    print("Starting network connectivity check...")
    for endpoint in ENDPOINTS:
        check_endpoint(endpoint)
    print("Check complete.")
