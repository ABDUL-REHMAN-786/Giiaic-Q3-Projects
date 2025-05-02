# Write a program that prints the first 20 even numbers. 
# There are several correct approaches, but they all use a loop of some sort. 
# Do no write twenty print statements

# The first even number is 0:

# 0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38

def print_even_numbers(n=20):
    """Prints the first n even numbers."""
    for i in range(n):
        print(i * 2, end=" ")  # Multiply index by 2 to get even numbers

# Run the function
print_even_numbers()
# Output: 0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38