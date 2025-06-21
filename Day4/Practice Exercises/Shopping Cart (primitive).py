### Shopping cart program

foods = []
prices = []
total = 0

while True:
    food = input("enter a food to buy (q to quit): ")
    if food.lower() == 'q':
        break
    elif food not in foods:
        foods.append(food)
        price = float(input(f"Enter the price of a {food}: $"))
        prices.append(price)

print("----- YOUR CART -----")
for food in foods:
    print(food, end= ' ')

for price in prices:
    total += price

print()
print(f"Your total is: ${total}")