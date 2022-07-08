# Python guessing game project.

# Import here.
import time
import random

# Declare variables here.
numberAnswer = random.randint(1, 10)
numberOfGuesses = 0
guess = None

# This is the code of the actual game.
print("Welcome to the guessing game!")
time.sleep(1)
print("Your goal is to guess a number between 1 and 10 in three guesses.")
time.sleep(1)

while numberOfGuesses < 3:
    guess = int(input("Please enter your best guess: "))
    if guess > numberAnswer:
        print("Your guess is too high, try again!")
    elif guess < numberAnswer:
        print("Your guess is too low, try again!")
    elif guess == numberAnswer:
        break

if guess == numberAnswer:
    print("Congratulations, you guessed correctly!")
else:
    print("Sorry, the answer was " + str(numberAnswer) + ".")
