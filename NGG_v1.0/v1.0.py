
#So the goal here is that there's no break, code runs as long as not the secret number is guessed.
#import the random module
import random 

#declare a variable and using random.randint store a random number
ans_number = random.randint(1, 100)
tries, guess = 0, 0

#if the guess is not the stored number in the declared variable
#then hint the player if it higher hint lower.. if its lower hint higher..
#if guess is equal to the number stored in our variable then go ahead and output
#you guessed it the number was 'maybe' 43 in  'maybe' 3 tries.
while guess != ans_number:
    #prompts user for a number less than 100
    guess = int(input("Guess a number less than 100: "))
    if guess > ans_number:
        print("Lower...")
    elif guess < ans_number:
        print("Higher...")
    tries += 1
 
print('You guessed it! The number was {} in {} tries'.format(guess, tries))