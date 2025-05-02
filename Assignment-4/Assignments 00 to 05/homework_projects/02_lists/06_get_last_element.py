# Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints 
# the last element in the list. The list is guaranteed to be non-empty, 
# but there are no guarantees on its length.


def get_last_element(lst):
    """Prints the last element of the given non-empty list."""
    print(f"The last element in the list is: {lst[-1]}")  # Access the last element using negative indexing

# Prompt the user to enter list elements
n = int(input("Enter the number of elements in the list: "))  # Get list size
user_list = []  # Initialize an empty list

for i in range(n):
    element = input(f"Enter element {i + 1}: ")  # Take user input
    user_list.append(element)  # Add the element to the list

# Call the function to print the last element
get_last_element(user_list)
# Output:
# Enter the number of elements in the list: 3