# Fill out the function get_first_element(lst) which takes in a list lst as a parameter 
# and prints the first element in the list. The list is guaranteed to be non-empty. 
# We've written some code for you which prompts the user to input the list one element at a time.


def get_first_element(lst):
    """Prints the first element of the given non-empty list."""
    print(f"The first element in the list is: {lst[0]}")

# Prompt the user to enter list elements
n = int(input("Enter the number of elements in the list: "))  # Get list size
user_list = []  # Initialize an empty list

for i in range(n):
    element = input(f"Enter element {i + 1}: ")  # Take user input
    user_list.append(element)  # Add the element to the list

# Call the function to print the first element
get_first_element(user_list)
# Output:
# Enter the number of elements in the list: 3