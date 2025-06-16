### --- CALCULATE AREA OF A CIRCLE --- ###
import math

radius = float(input("What is the radius of your circle? (in cm): "))

A = math.pi * (radius ** 2)

print(f"The area of your circle is {round(A, 2)}cm^2.")