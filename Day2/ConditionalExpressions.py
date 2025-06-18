# Conditional expression = A one line shortcut for an if else statement (Ternary operator)
#                          Print or assign one of two values based on a condition
#                          X if condition else Y


num = 6
a = 6
b = 7
age = 25
temperature = 30
user_role = "Admin"

print("positive" if num > 0 else "negative")
result = "EVEN" if num % 2 == 0 else "ODD"
print(result)
max_num = a if a > b else b
min_num = a if a < b else b

status = "Adult" if age >= 18 else "Child"
weather = "HOT" if temperature >= 20 else "CHILL"
access_level = "Full Access" if user_role == "Admin" else "Limited Access"
