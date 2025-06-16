#####     -----     RUDIMENTAL WEIGHT CONVERSION     -----     #####

weight = float(input("Enter your weight: "))
unit = input("Is that in Kilograms or Pounds? (K or L)")

if unit.lower() == 'k':
    weight = weight * 2.205
    unit = "Lbs."
elif unit.lower() == 'l':
    weight = weight / 2.205
    unit = "Kgs."
else:
    print(f"{unit} isn't a valid input")

print(f"Your weight is: {round(weight, 2)}{unit}")
