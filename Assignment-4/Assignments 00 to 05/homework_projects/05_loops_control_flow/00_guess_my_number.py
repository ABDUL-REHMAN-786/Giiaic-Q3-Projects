# Guess My Number

# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high

# Enter a new number: 25 Your guess is too low

# Enter a new number: 40 Your guess is too low

# Enter a new number: 45 Your guess is too low

# Enter a new number: 48 Congrats! The number was: 48


import random

def guess_my_number():
    """A simple number guessing game."""
    number = random.randint(0, 99)  # Generate a random number between 0 and 99
    print("I am thinking of a number between 0 and 99...")

    while True:
        try:
            guess = int(input("Enter a guess: "))  # Get user input and convert to integer
            if guess < number:
                print("Your guess is too low")
            elif guess > number:
                print("Your guess is too high")
            else:
                print(f"Congrats! The number was: {number}")
                break  # Exit the loop when guessed correctly
        except ValueError:
            print("Please enter a valid number.")  # Handle non-numeric input

# Run the game
guess_my_number()
