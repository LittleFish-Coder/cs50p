"""
re.search(pattern, string, flags=0)
"""
import re

email = input("What's your email? ").strip()

# if re.search(".*@.*", email):   # try malan@harvard.edu | malan@
#     print("Valid")
# else:
#     print("Invalid")

# if re.search(".+@.+", email):   # try malan@harvard.edu | malan@
#     print("Valid")
# else:
#     print("Invalid")

# as well as .+@.+
# if re.search("..*@..*", email):   # try malan@harvard.edu | malan@
#     print("Valid")
# else:
#     print("Invalid")

# if re.search(r".+@.+\.edu", email): # raw string
#     print("Valid")
# else:
#     print("Invalid")

# '^' matches the start of the string
# '$' matches the end of the string
# if re.search(r"^.+@.+\.edu$", email): # try malan@@@harvard.edu
#     print("Valid")
# else:
#     print("Invalid")

# [] set of characters
# [^] complementing the set
# if re.search(r"^[^@]+@[^@]+\.edu$", email): # try malan@@@harvard.edu
#     print("Valid")
# else:
#     print("Invalid")

# a-z A-Z
# if re.search(r"^[a-zA-Z0-9_.]+@[a-zA-Z0-9_.]+\.edu$", email): # try malan@@@harvard.edu
# if re.search(r"^\w+@[a-zA-Z0-9_.]+\.edu$", email): # \w represents "word character" (alphanumeric and underscore)
#     print("Valid")
# else:
#     print("Invalid")

# (...) a group, A|B either A or B, (?:...) non-capturing version
# if re.search(r"^\w+@\w+\.(com|edu|gov|net|org)$", email): # \w represents "word character" (alphanumeric and underscore)
#     print("Valid")
# else:
#     print("Invalid")

# ignore case
# if re.search(r"^\w+@\w+\.edu$", email, re.IGNORECASE): # try MALAN@HARVARD.EDU
#     print("Valid")
# else:
#     print("Invalid")

# ?: 0 or 1
if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE): # try malan@cs50.harvard.edu and malan@harvard.edu
    print("Valid")
else:
    print("Invalid")