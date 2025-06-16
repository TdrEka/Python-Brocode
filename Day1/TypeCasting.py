# Typecasting = The process of converting a data type to another
#               This can be done implicitly or explicitly


name = "Eka"
age = 28
gpa = 1.9
student = True

print(type(name))

age = float(age)
print(age)
print(type(age))

gpa = int(gpa)
print(gpa) #Truncated

student = str(student)
print(type(student))

age = bool(age)
print(age)

### IMPLICIT TYPE CASTING ###

x = 2
y = 2.0

x = x / y
print(x)