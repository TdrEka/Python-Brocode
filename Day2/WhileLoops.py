# While loops execute code while something is true

name = input("enter your name: ")

while name == '':
    print("you didnt enter your name")
    name = input("enter your name: ")
print(f"Hello {name.capitalize()}")