# A single variable used to store multiple values
#   list = [] ordered and changeable. duplicates ok.
#   set = {} unordered and immutable, but add/remove ok. NO duplicates
#   tuple = () ordered and unchangeable. duplicates ok (fastest)

fruits = ["apple", "orange", "banana", "papaya"]

print(fruits)
print(fruits[::-1])
#print(dir(fruits))
#print(help(fruits))
print(len(fruits))
print("apple" in fruits)

for fruit in fruits:
    print(fruit)

fruits[0] = "pineapple"
fruits.insert(0, "apple")
fruits.append("cherry")
fruits.remove("apple")
fruits.sort()
fruits.reverse()
print(fruits)

