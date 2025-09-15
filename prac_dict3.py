#Write a Python script that checks if the key "email" exists in this dictionary:
info = {"name": "Ravi", "phone": "123456"}
if "email" in info:
    print("Email already exit ")
else:
    print("Email doesnot exit ")
    info["email"]="ravi@example.com"
print(info)