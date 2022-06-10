"""
# Computer gives random number
# Save random number to variable (make sure its an int)
# Prompt user to guess random number between given range, min int to max int
# Save user prompt value
# Define function that accepts two parameters, min int and max int
## Within func definition, while user prompt value is not equal to comp's random number
### If user value(guess) is lower than random num, print a hint (ex. "Too low, try again"), prompt to guess
### If guess is higher than random num, print hint (ex. "Too high, try again"), prompt to guess
# If guess equals comp's random number
## print success message (ex. "Congrats! You guessed the number {guess} correctly!")
"""
import random

def guess_num(a, b):
    random_num = int(random.randint(a, b))
    guess = 0
    while guess != random_num:
        guess = int(input(f"Guess a number between {a} and {b}: "))
        if guess < random_num:
            print(f"Too low! You guessed {guess}. Try again.")
        elif guess > random_num:
            print(f"Too high! You guessed {guess}. Try again.")

    print(f"YES! You guessed {random_num} and you were correct!")

guess_num(1, 20)