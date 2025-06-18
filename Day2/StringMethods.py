name = input("Whats your name? (full): ")
phone_number = input("Enter your phone number: ")

strlen = len(name)

result = name.find(" ")
reverse = name.rfind('i')
uppercase = name.upper()
lowercase = name.lower()
is_it_a_digit = name.isdigit()
alpha = name.isalpha()
dashes = phone_number.count("-")
fixed_number = phone_number.replace("-", "")



print(strlen)
print(result)
print(reverse)
print(lowercase)
print(uppercase)
print(is_it_a_digit)