#####     -----     TEMPERATURE CONVERSION (PRIMITIVE)     -----     #####

temperature = float(input("Enter the temperature you want to convert: "))
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F). ")

if unit.lower() == 'c':
    temperature = (temperature * 9) / 5 + 32
    unit = "Degrees Fahrenheit."
elif unit.lower() == 'f':
    temperature = (temperature - 32) * 5/9
    unit = "Degrees Celsius."
else:
    print("Your input was invalid :C ")
    exit(1)

print(f"The temperature (converted) is {temperature} {unit}")