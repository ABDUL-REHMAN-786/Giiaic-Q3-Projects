# This program counts the number of times each number appears in a list.
#  It uses a dictionary to keep track of the information.

# An example run of the program looks like this (user input is in blue):

# Enter a number: 3 Enter a number: 4 Enter a number: 3 Enter a number: 6 Enter a number: 4 
# Enter a number: 3 Enter a number: 12 Enter a number: 3 appears 3 times. 4 appears 2 times. 
# 6 appears 1 times. 12 appears 1 times.

def count_numbers():
    """Counts the occurrences of numbers entered by the user."""
    number_counts = {}  # Dictionary to store counts

    while True:
        num = input("Enter a number (or press Enter to finish): ")
        if num == "":  # Stop if the user presses Enter
            break

        try:
            num = int(num)  # Convert input to integer
            number_counts[num] = number_counts.get(num, 0) + 1  # Update count
        except ValueError:
            print("Please enter a valid number.")

    # Print results
    for number, count in number_counts.items():
        print(f"{number} appears {count} times.")

# Run the function
count_numbers()
# This code is a simple program that counts the occurrences of numbers entered by the user.
# It uses a dictionary to keep track of the counts and prints the results at the end.