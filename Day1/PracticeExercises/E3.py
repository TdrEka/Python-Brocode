### --- MEGAPRIMITIVE SHOPPING CART --- ###

item = input("What item do you want to buy?: ")
price = float(input("What is the price of the item?: "))
quantity = int(input("And how many do you want?: "))

print(f"You're trying to buy {quantity} units of the item {item}, priced at ${price}.\nYour total will be ${quantity * price}")