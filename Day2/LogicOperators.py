# Logical operators are used in conditional statements 
#           and(C &&) = check two or more conditions if true
#           or(C ||) = checks if at least one condition is True
#           not = True if condition is False, and vice versa

temp = 25
sunny = True

if temp > 0 and temp < 30:
    print("GUD")
else: print("BAD")

if not sunny:
    print("cloudy")
else: print("sunny")

