import re

email=input("Enter Email: ").strip()

username,domain=email.split("@")

# if username and domain.endswith(".com"):
#     print("valid")
# else:
#     print("invalid")

if re.search(r"^[^@]+@[^@]+\.edu$",email):
    print("valid")
else:
    print("invalid")
