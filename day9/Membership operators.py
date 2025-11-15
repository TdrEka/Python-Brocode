# in and not in

word = "APPLE"

letter = input("Guess a letter in the secret word: ")

if letter in word:
    print(f"There is a {letter} in the secret word")
else:
    print(f"The letter {letter} was not found in the word.")

email = "lucas_reig_weidgraaf@gmail.com"

if "@" in email and "." in email:
    print("That is a valid email")
else: print("Invalid email")