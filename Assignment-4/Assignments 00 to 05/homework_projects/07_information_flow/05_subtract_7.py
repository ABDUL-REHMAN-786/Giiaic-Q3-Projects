# Fill out the subtract_seven helper function to subtract 7 from num, and fill out 
# the main() method to call the subtract_seven helper function! 
# If you're stuck, revisit the add_five example from lecture.


def subtract_seven(num):
    """Subtracts 7 from the given number."""
    return num - 7

def main():
    number = int(input("Enter a number: "))  # Get user input
    result = subtract_seven(number)  # Call the function
    print("Result after subtracting 7:", result)

# Run the main function
main()
# # The subtract_seven function takes a number as input and subtracts 7 from it.
# # The main function prompts the user for a number, calls the subtract_seven function, and prints the result.