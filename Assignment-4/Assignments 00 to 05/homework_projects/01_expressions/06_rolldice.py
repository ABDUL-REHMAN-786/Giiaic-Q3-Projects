# Simulate rolling two dice, and prints results of each roll as well as the total.


import random  # Import the random module to generate random numbers

# Simulate rolling two dice
die1 = random.randint(1, 6)  # Generate a random number between 1 and 6 for the first die
die2 = random.randint(1, 6)  # Generate a random number between 1 and 6 for the second die

# Calculate the total
total = die1 + die2

# Display the results
print(f"Die 1: {die1}")
print(f"Die 2: {die2}")
print(f"Total: {total}")
# The program simulates rolling two dice and displays the result of each die and their total.
# It uses the random module to generate random numbers between 1 and 6 for each die.