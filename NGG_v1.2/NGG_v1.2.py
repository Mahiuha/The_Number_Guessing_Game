from random import randint
from time import sleep
import random
import time
import banner
import os

# Header Area
os.system("clear")
banner.logo()

#prompts the user to input if they want to play the game or not
print()
initialAsk = input("# Shall we play a game? Type YES or NO: ")

# --  Function to quit the game
def quitGame():
    print("\n"
        "Goodbye, I hope to see you again!")
    time.sleep(3)
    quit()

while str.upper(initialAsk) != "YES":

    if str.upper(initialAsk) == "NO":
        quitGame()

    else:
        print("\n"
            "Sorry, I don't understand. \n")
        os.system("clear")
        banner.logo()
        initialAsk = input("# Shall we play a game? Type YES or NO: ")

else:
    play = True
    print("\n"
        "Let's get started! \n")
    os.system("clear")
    banner.logo()



#  --  This function is the code for the game
def gameStart():
###

    print("# This game is called, 'Number Guessing Game (NGG)!' \n"
        "\n"
        "# Here's how we'll play: \n"
        "# I generate a random number from a certain range depending on the level you choose, \n"
        "  and you will have to guess it. \n"
        "\n"
        "# There are 3 difficulties: easy, medium or hard. \n"
        "# The number ranges for each are as follows: \n"
        "  EASY: 1 - 10 \n"
        "  MEDIUM: 1 - 50 \n"
        "  HARD: 1- 100 \n")

    #  --  this is the difficulty selection and number generation
    guessRangeList = []

    modeSelectList = ["EASY", "MEDIUM", "HARD"]

    modeSelected = str.upper(input("? Please enter your desired difficulty:  "))

    while modeSelected not in modeSelectList:
        print("\n"
        "Oops, that's not a valid difficulty. \n")
        os.system("clear")
        banner.logo()
        modeSelected = str.upper(input("Please enter your desired difficulty:  "))

    else:
        if modeSelected == "EASY":
            for num in range(1, 11):
                guessRangeList.append(num)
            randomNumber = random.randint(1, 10)

        elif modeSelected == "MEDIUM":
            for num in range(1, 51):
                guessRangeList.append(num)
            randomNumber = random.randint(1, 50)

        elif modeSelected == "HARD":
            for num in range(1, 101):
                guessRangeList.append(num)
            randomNumber = random.randint(1, 100)
    os.system("clear")
    banner.logo()
    print("\n"
    "%s mode selected. You have 5 tries to guess the correct number. \n" % (modeSelected))
    ###

    #  --  Determines how many hints the user gets based on the selected difficulty
    if modeSelected == "EASY":
        print("You have up to 3 hints.")
        hintsLeft = 3

    elif modeSelected == "MEDIUM":
        print("You have up to 12 hints.")
        hintsLeft = 12

    else:
        print("You have up to 21 hints.")
        hintsLeft = 21
    ###

#  -- Take out the hastags to check the number of tries the player starts with and what the generated number is
#print("\n"
    #"triesLeft \n")
#print(triesLeft)
#print("\n"
    #"random number")
#print(randomNumber)

    #  --  This is the guessing portion
    triesLeft = 5
    numbersAlreadyGuessed = []
    print("\n"
        "Tips: \n"
        "1. Type HINT and I will give you a number that is not the correct number. \n"
        "2. Type LIST to see your previous guesses. \n")
    userGuess = input("Can you guess the number?  ")
    os.system("clear")
    banner.logo()

    while userGuess != randomNumber:

    #  --  If player wants to see a list
        if str.upper(userGuess) == "LIST":
        
            if len(numbersAlreadyGuessed) > 0:
                numbersAlreadyGuessed.sort()
                print("\n"
                    "The numbers", numbersAlreadyGuessed, "have been guessed already. \n")
                userGuess = input("Can you guess the number?  ")
                os.system("clear")
                banner.logo()
            
            else:
                print("\n"
                    "You have not currently guessed any number. \n")
                userGuess = input("Can you guess the number?  ")
                os.system("clear")
                banner.logo()
    ###

    #  --  If player wants to use a hint
        elif str.upper(userGuess) == "HINT":
        
            if hintsLeft > 0:
                numberOptions = [num for num in guessRangeList if num != randomNumber and num not in numbersAlreadyGuessed]
                hintedNumber = (random.choice(numberOptions))
                numbersAlreadyGuessed.append(hintedNumber)

                print("\n"
                    "You used a hint. %d is NOT the number you're looking for. \n" % (hintedNumber))

                hintsLeft -= 1

                if hintsLeft > 1 or hintsLeft == 0:
                    print("You have %d hints left." % (hintsLeft))

                else:
                    print("You have %d hint left." % (hintsLeft))

                print()
                userGuess = input("Can you guess the number?  ")
                os.system("clear")
                banner.logo()
            
            else:
                print("\n"
                    "Sorry, you have no more hints. \n")
                userGuess = input("Can you guess the number?  ")
            os.system("clear")
            banner.logo()
    ###

    #  --  if player makes a guess
        elif userGuess.isdigit() == True:

            if int(userGuess) != randomNumber:      # (1A)
                print()

                if int(userGuess) in guessRangeList:     # (2A)
            
                    if int(userGuess) not in numbersAlreadyGuessed:     # (3A)
                        print("Oops, that's not the number I'm looking for. \n")
                        numbersAlreadyGuessed.append(int(userGuess))
                        triesLeft -= 1
                        if int(userGuess) > randomNumber:
                            print("Try Lower...")
                        elif int(userGuess) < randomNumber:
                            print("Try Higher...")

                        if triesLeft >= 1:     # (4A)

                            if triesLeft > 1:     # (4A.1)
                                print("You have %d tries left." % (triesLeft))

                            elif triesLeft == 1:     # (4A.2)
                                print("You have %d try left." % (triesLeft))

                            print()
                            userGuess = input("Can you guess the number?  ")
                            os.system("clear")
                            banner.logo()

                        else:     # (4B)
                            print("Sorry, you have run out of tries. The correct number was %d. \n" % (randomNumber))
                            askPlayAgain = input("Type 'EXIT' to exit, or 'PLAY' to play again: ")

                            while str.upper(askPlayAgain) != "PLAY":     # (5A.1)

                                if str.upper(askPlayAgain) == "EXIT":     # (5B)
                                    quitGame()

                                else:     # (5C)
                                    print("\n"
                                        "Sorry, I don't understand. \n")
                                    askPlayAgain = input("Type 'EXIT' to exit, or 'PLAY' to play again: ")

                            else:     #(5A.2)
                                print()
                                gameStart()

                    else:       # (3B)
                        print("Oops, you've already guessed that number. \n")
                        userGuess = input("Can you guess the number?  ")
                        os.system("clear")
                        banner.logo()

                else:       # (2B)
                    print("Oops, that's not in the range. \n")
                    userGuess = input("Can you guess the number?  ")
                    os.system("clear")
                    banner.logo()

            else:       # (1B)
                print("\n"
                    "Congratulations! You guessed correctly!")
                time.sleep(3)
                quit()


        # Number Directory:
        # (1) - If player guess is wrong or right
        # (2) - If player guess is within the range
        # (3) - If player guess has been previously been stated
        # (4) - Sees how many tries player has left, and what to do if tries = 0
        # (5) - Asks the player if he/she wants to play again

    ###

    #  --  If the user doesn't type 'hint', 'list' or a string solely made of intgers
        else:
            print("\n"
                "Sorry, I don't understand. \n")
            userGuess = input("Can you guess the number?  ")
            os.system("clear")
            banner.logo()
    ###

#  --  Starts the Game
gameStart()
###
