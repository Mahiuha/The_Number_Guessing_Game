from random import randint
from time import sleep
import banner
import os

# Header Area
os.system("clear")
banner.logo()

# Scores Initialization
winnerscore = 0
failurescore = 0

# Scores Counter
def scores():
    print(f"Won {winnerscore} time")
    print(f"Lost {failurescore} time")

# Control Statements
try:
    while True:
        guessing = int(input("Enter Guessing Number: "))
        checkandlimit = randint(1,5)
        if guessing == checkandlimit:
            print("You have won")
            winnerscore += 1
            sleep(1)
            os.system("clear")
            banner.logo()
        elif guessing == 0:
            break
        else:
            print("Sorry, you lose")
            failurescore += 1
            sleep(1)
            os.system("clear")
            banner.logo()
except:
    print("Something went wrong, try again")
    usage = input("Need usage details: ")
    usage = usage.lower()
    if usage == "yes":
            print("\nGuess one by one the numbers from one to five,\nif your guess is correct you can win and if the guess is wrong you are loser.\nif you want to exit the game please enter 0\n")
    else:
        print("Something went wrong, try again")
        os.system("exit")

# Show Scores
scores()