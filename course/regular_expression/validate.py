email = input("What's your email ").strip()

# if "@" in email and "." in email: # try malan@harvard.edu
#     print("Valid")
# else:
#     print("Invalid")

username, domain = email.split("@")

if username and "." in domain:  # try malan@harvard
    print("Valid")
else:
    print("Invalid")

if username and domain.endswith("edu"):  # try malan@harvard.edu
    print("Valid")
else:
    print("Invalid")
