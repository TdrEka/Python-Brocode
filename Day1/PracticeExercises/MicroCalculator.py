###   ---   MICRO CALCULATOR FOR PRACTICING IF ELSE SYNTAX IN PYTHON   ---   ###

operator = input("Enter an operator (+, -, *, /): ")
n1 = float(input("First number: "))
n2 = float(input("Second number: "))
result = None

if operator == '+':
    result = round(n1 + n2, 2)
elif operator == '-':
    result = round(n1 - n2, 2)
elif operator == '*':
    result = round(n1 * n2, 2)
elif operator == '/':
    result = round(n1 / n2, 2)
else: print("Please enter a valid operator ('+', '-', '*', '/')")

print(result)
