# Guess My Number

# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high

# Enter a new number: 25 Your guess is too low

# Enter a new number: 40 Your guess is too low

# Enter a new number: 45 Your guess is too low

# Enter a new number: 48 Congrats! The number was: 48

import random

# Generate a random number between 0 and 99
secret_number = random.randint(0, 99)

print("I am thinking of a number between 0 and 99...")

# Loop until the user guesses correctly
while True:
    guess = int(input("Enter a guess: "))  # Get user input

    if guess > secret_number:
        print("Your guess is too high\n")
    elif guess < secret_number:
        print("Your guess is too low\n")
    else:
        print(f"Congrats! The number was: {secret_number}")
        break  # Exit the loop when the guess is correct
