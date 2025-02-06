import re

name = input("What's your name? ").strip()

# if "," in name: # Malan, David
#     last, first = name.split(", ")
#     name = f"{first} {last}"
# print(f"Hello, {name}")

matches = re.search(r"^(.+), *(.+)$", name) # try Malan,   David
print(matches)

if matches:
    last, first = matches.groups()
    name = f"{first} {last}"
    # name = matched.group(2) + " " + matches.group(1)
print(f"Hello, {name}")
