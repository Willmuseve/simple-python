# A Python program that simulates the "Rock, Paper, Scissors" game.

import random

options = ("rock", "paper", "scissors")

comp = options[random.randint(0, 2)]

print("===== Welcome =====")

player = input("Please enter rock, paper or scissors: ")

if player.lower() == comp:
    print("It's a tie, please try again")
elif player.lower() == "rock":
    if comp == "paper":
        print("You Lose!")
    else:
        print("You win")
elif player.lower() == "paper":
    if comp == "scissors":
        print("You lose!")
    else:
        print("You win")
elif player.lower() == "scissors":
    if comp == "rock":
        print("You lose!")
    else:
        print("You win")
else:
    print("Please enter a valid option")
