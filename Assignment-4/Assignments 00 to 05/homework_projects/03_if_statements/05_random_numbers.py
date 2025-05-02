# Print 10 random numbers in the range 1 to 100.

# Here is an example run:

# 45 79 61 47 52 10 16 83 19 12

# Each time you run your program you should get different numbers

# 81 76 70 1 27 63 96 100 32 92

# Recall that the python random library has a function randint which returns an integer 
# in the range set by the parameters (inclusive). For example this call would produce a random 
# integer between 1 and 6, which could include 1 and could include 6:

# value = random.randint(1, 6)

import random  # Import the random module

def print_random_numbers():
    """Generates and prints 10 random numbers between 1 and 100."""
    for _ in range(10):  # Loop 10 times
        print(random.randint(1, 100), end=" ")  # Print random number with space

# Run the function
print_random_numbers()
# The code generates and prints 10 random integers between 1 and 100 using the `random.randint` function.
# Each time the program is run, different numbers are produced.