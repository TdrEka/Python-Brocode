# Step 1 prompt the user for input + remove any ' ' or '-'
card_number = input("Please enter your card number: ")
card_number = card_number.replace(' ', '').replace('-', '')
card_number = card_number[::-1]
sum_odd_digits = 0
sum_even_digits = 0
total = 0


# Step 2 add all digits in odd places from right to left

for x in card_number[::2]:
    sum_odd_digits = sum_odd_digits + int(x)

# Step 3 double every second digit from right to left
# if result is a two-digit number add together to get a single digit.

for x in card_number[1::2]:
    x = int(x) * 2
    if x >= 10:
        sum_even_digits += (1 + (x % 10))
    else:
        sum_even_digits += x


# Step 4 add it all together.

total = sum_even_digits + sum_odd_digits

# Step 5 if sum is divisible by 10 print valid else invalid

if total % 10 == 0:
    print("Valid")
else: print("Invalid")