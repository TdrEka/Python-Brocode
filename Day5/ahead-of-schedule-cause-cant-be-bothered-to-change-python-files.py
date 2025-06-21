# The chaos inventory

class Thing:

    def __init__(self, name, price, stock = 0):
        self.name = name
        self.price = price
        self.stock = stock

    def purchasification(self, quantity):
        if quantity > self.stock:
            print(f"The LLM overlords wont allow for that.. we only have {self.stock} of that item, cope.")
            return
        else:
            self.stock -= quantity
            return print("You've successfully purchased a thing. ")

    def restockification(self, quantity):
        self.stock += quantity
        return print("Thank you for cogging")

    def isthing(self):
        if self.stock > 0: print("Youp we got it. ")

    def greedcheck(self):
        return print(f"Total sales value of {self.name}s currently in stock is {self.price * self.stock}. (That's not how much you'll be making though)")



