# Validate user input exercise
# 1. Username is no more than 12 characters
# 2. Username must not contain spaces
# 3. Username must not contain digits


username = input("Enter username: ")

if len(username) > 12 or not username.isalpha():
    print("not valid username")
else:
    print("Valid username")