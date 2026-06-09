import random
length = int(input("Enter your password length: "))

upper = input("Include uppercase letters? (yes/no): ")
lower = input("Include lowercase letters? (yes/no): ")
digits = input("Include digits? (yes/no): ")
special = input("Include special characters? (yes/no): ")

chars = ""

if upper == "yes":
    chars += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
if lower == "yes":
    chars += "abcdefghijklmnopqrstuvwxyz"
if digits == "yes":
       chars += "0123456789"
if special == "yes":
    chars += "!@#$%^&*()"

if chars == "":
    print("You must choose atleast one type!")
else:
    password = ""
    for i in range (length):
        password += random.choice(chars)
    print("Your password is: ", password)