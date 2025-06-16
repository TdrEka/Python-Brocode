### --- HYPOTENUSE OF A TRIANGLE --- ###
import math

opposite = float(input("What is the length of the opposite side of your triangle (cm): "))
adjacent = float(input("And the adjacent?: "))

hypotenuse = math.sqrt(math.pow(opposite, 2) + math.pow(adjacent, 2))

print(f"The hypotenuse of your triangle is {round(hypotenuse, 2)}")