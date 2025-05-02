# Simulate rolling two dice, three times. Prints the results of each die roll.
#  This program is used to show how variable scope works.


import random  # Import the random module to generate random numbers

def roll_dice():
    """Simulates rolling two dice and prints the results."""
    die1 = random.randint(1, 6)  # Generate a random number between 1 and 6 for the first die
    die2 = random.randint(1, 6)  # Generate a random number between 1 and 6 for the second die
    print(f"Die 1: {die1}, Die 2: {die2}")  # Print the result of both dice

# Simulate rolling two dice three times
for i in range(3):  # Loop runs 3 times
    print(f"Roll {i + 1}:")  # Print the roll number
    roll_dice()  # Call the function to roll the dice
