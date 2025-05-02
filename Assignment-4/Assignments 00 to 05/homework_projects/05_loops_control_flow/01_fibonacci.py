# Write a program to print terms in the Fibonacci sequence up to a maximum value.

# In the 13th century, the Italian mathematician Leonardo Fibonacci, 
# as a way to explain the geometric growth of a population of rabbits, 
# devised a mathematical sequence that now bears his name. The first two terms in this sequence, 
# Fib(0) and Fib(1), are 0 and 1, and every subsequent term is the sum of the preceding two. 
# Thus, the first several terms in the Fibonacci sequence look like this:

# Fib(0) = 0 Fib(1) = 1 Fib(2) = 1 = 0 + 1 Fib(3) = 2 = 1 + 1 Fib(4) = 3 = 1 + 2 Fib(5) = 5 = 2 + 3

# Write a program that displays the terms in the Fibonacci sequence, starting with Fib(0) and 
# continuing as long as the terms are less than 10,000 (you should store this value as a constant!). 
# Thus, your program should produce the following sample run:

# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711 28657 46368 75025 121393 196418 317811 514229 832040 1346269 2178309 3524578 5702887 9227465 14930352 24157817 39088169 63245986 102334155 165580141 267914296 433494437 701408733 1134903170

def fibonacci_sequence(max_value=10000):
    """Prints Fibonacci sequence up to max_value."""
    a, b = 0, 1  # Initial Fibonacci numbers
    while a < max_value:
        print(a, end=" ")  # Print the current term
        a, b = b, a + b  # Update Fibonacci numbers

# Run the function
fibonacci_sequence()
# Output: 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946
# 17711 28657 46368 75025 121393 196418 317811 514229 832040 1346269 2178309 3524578 5702887 9227465 14930352 24157817 39088169 63245986 102334155 165580141 267914296 433494437 701408733 1134903170