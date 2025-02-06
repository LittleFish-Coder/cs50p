import re

# url: https://twitter.com/davidmalan
url = input("URL: ").strip()
print(url)

# username = url.replace("https://twitter.com/", "")

# userename = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", name)
# print(f"Username: {username}")

# matches = re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
matches = re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/([a-z0-9_]+)$", url, re.IGNORECASE)

if matches:
    print(f"Username: {matches.group(1)}")


