import random

print("Password Generator")

length = int(input("Enter password length: "))

password = ""

for i in range(length):
    password += random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")

print("Your password is:", password)

# This line keeps the screen open
input("Press Enter to exit...")
