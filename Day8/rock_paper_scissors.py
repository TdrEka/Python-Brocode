# Ok... lets keep the momentum going, my brain feels like mush though, three month break wasn't a good idea.

import random

options = ("rock", "paper", "scissors", "lizard", "spock")

state = True

while state:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors, lizard, spock): ")


    print(f"Player: {player} VS Computer: {computer}")

    if player == computer:
        print("------ It's a tie! ------")
    elif player == "rock" and computer == "paper" or player == "rock" and computer == "spock":
        print("------ YOU LOOSE ------")
    elif player == "lizard" and computer == "rock" or player == "lizard" and computer == "scissors":
        print("------ YOU LOOSE ------")
    elif player == "spock" and computer == "paper" or player == "spock" and computer == "lizard":
        print("------ YOU LOOSE ------")
    elif player == "scissors" and computer == "spock" or player == "scissors" and computer == "rock":
        print("------ YOU LOOSE ------")
    elif player == "paper" and computer == "rock" or player == "paper" and computer == "lizard":
        print("------ YOU LOOSE ------")
    elif player == "rock" and computer == "scissors" or player == "rock" and computer == "lizard":
        print("------ YOU WIN ------")
    elif player == "lizard" and computer == "spock" or player == "lizard" and computer == "paper":
        print("------ YOU WIN ------")
    elif player == "spock" and computer == "rock" or player == "spock" and computer == "scissors":
        print("------ YOU WIN ------")
    elif player == "scissors" and computer == "paper" or player == "scissors" and computer == "lizard":
        print("------ YOU WIN ------")
    elif player == "paper" and computer == "spock" or player == "paper" and computer == "rock":
        print("------ YOU WIN ------")

    if not input("Play again? (y/n): ").lower() == "y":
        state = False

print("Thanks for playing!")