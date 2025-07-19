try:
    import requests
except ModuleNotFoundError:
    import subprocess, sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    import requests

target = input("Enter the target URL (e.g., http://example.com): ").strip()
if not target.endswith("/"):
    target += "/"

with open("wordlist.txt", "r") as file:
        wordlist = file.read().splitlines()
        
print(f"\n[+] Scanning {target}...\n")

for word in wordlist:
    url = target + word + "/"
    try:
        r = requests.get(url)
        if r.status_code == 200:
            print(f"[FOUND] {url}")
        elif r.status_code == 403:
            print(f"[FORBIDDEN] {url}")
    except requests.ConnectionError:
        print("[-] Connection Error: Cannot reach the target.")
        break

print("\n[+] Scan Completed.")
