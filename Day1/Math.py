# Arithmetics operators, math functions
import math


#################
####OPERATORS####
#################

friends = 0
friends += 2
friends -= 1
friends *= 3
friends /= 2
friends **= 2
remainder = friends % 2

print(friends)
print(remainder)

########################
#####MATH FUNCTIONS#####
########################

x = 3.14
y = -4
z = 5
a = 9.9

result = round(x)
result1 = abs(y)
result2 = pow(z, 9)
result3 = max(x, y, z)
result4 = min(x, y, z)

print(result)
print(result1)
print(result2)
print(result3)
print(result4)

print(math.pi)
print(math.e)
result5 = math.sqrt(math.pi)
print(result5)
result6 = math.floor(a)
result7 = math.ceil(a)
print(f"{result6} and {result7}")


