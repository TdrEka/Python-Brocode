# A single variable used to store multiple values
#   list = [] ordered and changeable. duplicates ok.
#   set = {} unordered and immutable, but add/remove ok. NO duplicates
#   tuple = () ordered and unchangeable. duplicates ok (fastest)

fruits = ["apple", "orange", "banana", "papaya"]

print(fruits)
print(fruits[::-1])
print(dir(fruits))

for fruit in fruits:
    print(fruit)