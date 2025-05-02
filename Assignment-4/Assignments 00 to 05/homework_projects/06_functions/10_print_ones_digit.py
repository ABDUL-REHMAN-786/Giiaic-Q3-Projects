# Write a function called print_ones_digit , which takes as a 
# an integer num and prints its ones digit. The modulo (remainder) operator, %, 
# should be helpful to you here. Call your function from main()!

# Here's a sample run (user input is in blue):

# Enter a number: 42 The ones digit is 2


def print_ones_digit(num):
    ones_digit = num % 10  # Get the ones digit using modulo operator
    print(f"The ones digit is {ones_digit}")

def main():
    num = int(input("Enter a number: "))  # Take user input and convert to integer
    print_ones_digit(num)  # Call the function

main()  # Run the program
# Note: The print_ones_digit function takes an integer as input and prints its ones digit using the modulo operator.
# The main function prompts the user for a number and calls print_ones_digit to display the ones digit.