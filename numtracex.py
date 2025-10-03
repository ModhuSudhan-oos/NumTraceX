from utils.banner import show_banner
from utils.auth import ensure_password, login
from core.analyzer import analyze_number

if __name__ == "__main__":
    show_banner()
    ensure_password()
    if login():
        while True:
            number = input("Enter a phone number (or 'q' to quit): ")
            if number.lower() == 'q':
                break
            analyze_number(number)
