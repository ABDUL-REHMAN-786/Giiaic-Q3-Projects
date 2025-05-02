# Fill out the function shorten(lst) which removes elements from the end of lst, which is a list, 
# and prints each item it removes until lst is MAX_LENGTH items long. 
# If lst is already shorter than MAX_LENGTH you should leave it unchanged. 
# We've written a main() function for you which gets a list and passes it into your '
# 'function once you run the program. For the autograder to pass you will need MAX_LENGTH to be 3, '
# 'but feel free to change it around to test your program.


MAX_LENGTH = 3  # Define the maximum allowed length of the list

def shorten(lst):
    """Removes elements from the end of lst until its length is MAX_LENGTH."""
    while len(lst) > MAX_LENGTH:  # Keep removing elements if list is too long
        removed_item = lst.pop()  # Remove the last element
        print(f"Removed: {removed_item}")  # Print the removed item

    print(f"Final list: {lst}")  # Print the final shortened list

# Example main function to test
def main():
    # Prompt the user to enter list elements
    n = int(input("Enter the number of elements in the list: "))  # Get list size
    user_list = []  # Initialize an empty list

    for i in range(n):
        element = input(f"Enter element {i + 1}: ")  # Take user input
        user_list.append(element)  # Add the element to the list

    print(f"\nOriginal list: {user_list}")
    shorten(user_list)  # Call the shorten function

# Run the program
main()
# Sample Output:
# Enter the number of elements in the list: 5