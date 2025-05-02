# Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.

# Here's a sample run of the program (user input is in bold italics):

# Please enter an integer to be divided: 5

# Please enter an integer to divide by: 3

# The result of this division is 1 with a remainder of 2

# Prompt the user to enter two integers
num1 = int(input("Please enter an integer to be divided: "))
num2 = int(input("Please enter an integer to divide by: "))

# Calculate quotient and remainder
quotient = num1 // num2  # Integer division
remainder = num1 % num2  # Modulus operator for remainder

# Display the result
print(f"\nThe result of this division is {quotient} with a remainder of {remainder}")
# The program prompts the user for two integers, performs integer division, and calculates the remainder.
# It then displays the results in a formatted message.