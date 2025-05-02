# Fill out the double(num) function to return the result 
# of multiplying num by 2.
# We've written a main() function for you which asks the user for a number, calls'
# ' your code for double(num) , and prints the result.

# Here's a sample run of the program (user input in bold italics):

# Enter a number: 2 Double that is 4


def double(num):
    """Returns the result of multiplying num by 2."""
    return num * 2

def main():
    num = float(input("Enter a number: "))
    print(f"Double that is {double(num)}")

# Run the main function
main()
# Note: The program will prompt the user for a number and print the result of doubling it.
# The double function takes a single argument and returns its double.