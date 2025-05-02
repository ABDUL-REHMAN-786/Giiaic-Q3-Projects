# Write a program which continuously asks the user to enter values which are 
# added one by one into a list. When the user presses enter without typing anything, print the list.

# Here's a sample run (user input is in blue):

# Enter a value: 1 Enter a value: 2 Enter a value: 3 Enter a value: Here's the list: ['1', '2', '3']


def get_user_list():
    """Continuously asks the user for input and adds values to a list until Enter is pressed."""
    user_list = []  # Initialize an empty list

    while True:
        value = input("Enter a value: ")  # Ask the user for input
        if value == "":  # If the user presses Enter without typing anything, break the loop
            break
        user_list.append(value)  # Add the value to the list

    print(f"Here's the list: {user_list}")  # Print the final list

# Run the function
get_user_list()
# Sample Output:
# Enter a value: 1