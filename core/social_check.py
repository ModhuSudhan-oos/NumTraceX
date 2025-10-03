# core/social_check.py
import requests
from bs4 import BeautifulSoup
import re
import time
from urllib.parse import quote_plus

USER_AGENT = "NumTraceX/1.0 (+https://github.com/Mon-oos/NumTraceX)"

SOCIAL_DOMAINS = [
    "facebook.com",
    "instagram.com",
    "twitter.com",
    "linkedin.com",
    "t.me",            # telegram
    "wa.me",           # whatsapp quick link
    "youtube.com",
]

def ddg_search(query, max_results=10, pause=1.0):
    """
    Simple DuckDuckGo HTML search scraping (no JS).
    Returns list of URLs found.
    """
    urls = []
    try:
        q = quote_plus(query)
        url = f"https://duckduckgo.com/html/?q={q}"
        headers = {"User-Agent": USER_AGENT}
        r = requests.get(url, headers=headers, timeout=8)
        if r.status_code != 200:
            return urls
        soup = BeautifulSoup(r.text, "html.parser")
        results = soup.find_all("a", attrs={"class": "result__a"}, limit=max_results)
        for a in results:
            href = a.get("href")
            if not href:
                continue
            # DuckDuckGo returns redirect links like /l/?uddg=<encoded-url>
            m = re.search(r"uddg=(https?%3A%2F%2F[^&]+)", href)
            if m:
                real = requests.utils.unquote(m.group(1))
            else:
                real = href
            urls.append(real)
        time.sleep(pause)
    except Exception as e:
        print(f"[!] Error in search: {e}")
    return urls

def extract_social_links_from_urls(urls):
    found = {}
    for u in urls:
        for domain in SOCIAL_DOMAINS:
            if domain in u:
                found.setdefault(domain, []).append(u)
    return found

def check_social_and_spam(number: str):
    """
    Best-effort check:
     - search for the phone number string in web
     - look for known social domains in results
     - quick spam complaint check
    """
    print("\n[🔍] Searching public web for social links (best-effort)...")

    queries = set()
    norm = number.strip()
    queries.add(norm)
    # variations
    queries.add(norm.replace("+", ""))
    queries.add(norm.replace("+", "").replace("-", "").replace(" ", ""))
    queries.add(f"\"{norm}\"")  # exact match

    all_urls = []
    for q in queries:
        urls = ddg_search(q, max_results=15, pause=0.8)
        all_urls.extend(urls)

    found = extract_social_links_from_urls(all_urls)

    if not found:
        print("    - No public social profile links found.")
    else:
        print("    - Potential public links found:")
        for domain, links in found.items():
            print(f"      • {domain}:")
            for l in links:
                print(f"         - {l}")

    # Simple spam-check
    print("\n[⚠️] Checking simple spam/leak mentions...")
    spam_check_queries = [f"{norm} scam", f"{norm} spam", f"{norm} leak"]
    spam_found = False
    for sq in spam_check_queries:
        urls = ddg_search(sq, max_results=8, pause=0.6)
        for u in urls:
            if any(x in u for x in ["complaints", "scam", "trustpilot", "tellows", "who-called"]):
                print(f"    - Possible spam/complaint mention: {u}")
                spam_found = True
    if not spam_found:
        print("    - No obvious spam/complaint results found.")
