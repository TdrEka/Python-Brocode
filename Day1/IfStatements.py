# if = Do some code only IF some condition is True
#      Else do something else

age = int(input("Enter your age: "))

if 16 <= age <= 18:
    print("You can drink beer but not spirits.")
elif age >= 18:
    print("You can drink beer and spirits.")
else:
    print("You can't drink beer or spirits.")



