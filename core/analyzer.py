import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from core.social_check import check_social_and_spam


def analyze_number(number: str):
    try:
        parsed = phonenumbers.parse(number, None)
        if not phonenumbers.is_valid_number(parsed):
            print("❌ Invalid phone number.")
            return

        country = geocoder.description_for_number(parsed, "en")
        operator = carrier.name_for_number(parsed, "en")
        timezones = timezone.time_zones_for_number(parsed)

        print("--- Analysis Result ---")
        print(f"Country: {country}")
        print(f"Carrier: {operator}")
        print(f"Timezones: {', '.join(timezones)}")

        check_social_and_spam(number)
    except Exception as e:
        print(f"Error: {e}")
