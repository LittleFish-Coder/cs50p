words = input("Input: ")
output = ""

for c in words:
    if c.lower() in ["a", "e", "i", "o", "u"]:
        pass
    else:
        output += c

print(f"Output: {output}")
