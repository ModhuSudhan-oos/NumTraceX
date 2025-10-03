def check_social_and_spam(number: str):
    print("Checking social media presence...")
    # Example mock
    fake_db = {"+8801712345678": ["Facebook", "WhatsApp"]}
    if number in fake_db:
        print(f"Found on: {', '.join(fake_db[number])}")
    else:
        print("No social presence found.")

    print("Checking spam database...")
    spam_db = {"+8801999999999": True}
    if number in spam_db:
        print("⚠️ Marked as spam!")
    else:
        print("Not marked as spam.")
