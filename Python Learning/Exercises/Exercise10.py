# Exercise 10: Random Number Guessing Game

import random

computer_number = random.randint(1, 100)
user_guess = 0

print("Welcome to my python: random number guessing program.")

while True:
    if user_guess != computer_number:
        print("Please enter a number between 1-100")
        user_guess = int(input(">: "))
        if user_guess > computer_number:
            print("The number is lower, try again.")
            print("")
        else:
            print("The number is higher, try again.")
            print("")
    else:
        print(f"Correct! The generated number was {computer_number}")
        break