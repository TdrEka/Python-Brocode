rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))
symbol = input("Whats your rectangle made out of? (char): ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end='')
    print()



