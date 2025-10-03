import os, hashlib, getpass

PASSWORD_FILE = ".password"


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def ensure_password():
    if not os.path.exists(PASSWORD_FILE):
        pwd = getpass.getpass("Set a new password: ")
        with open(PASSWORD_FILE, "w") as f:
            f.write(hash_password(pwd))
        print("Password set successfully.")


def login() -> bool:
    pwd = getpass.getpass("Enter password: ")
    with open(PASSWORD_FILE, "r") as f:
        stored = f.read().strip()
    if stored == hash_password(pwd):
        print("✔️ Access granted.")
        return True
    else:
        print("❌ Access denied.")
        return False
