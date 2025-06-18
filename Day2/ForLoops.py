# For loops = execute a code a fixed number of times
#             You can iterate over a range, a string a sequence etc


for x in reversed(range(1,11)):
    print(x)
print("HAPPY NEW YEAR")


credit_card = "1234-1234-1234-1234"

for i in credit_card:
    print(i)

for x in range (1, 21):
    if x == 13:
        continue
    else: print(x)