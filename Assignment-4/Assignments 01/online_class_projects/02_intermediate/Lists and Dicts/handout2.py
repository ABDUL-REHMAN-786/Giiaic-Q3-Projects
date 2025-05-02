# Problem #2: Index Game
# As a warmup, read this code and play the game a few times. Use this mental model of the list:

# Objective:
# Create a Python program that helps you practice accessing and manipulating elements in a list. This exercise will help you get comfortable with indexing, slicing, and modifying list elements.

# Instructions:
# Initialize a List:
# Create a list with at least 5 different elements. They can be numbers, strings, or a mix of both.

# Accessing Elements:
# Write a function that:

# Accepts a list and an index as inputs.
# Returns the element at the specified index.
# If the index is out of range, return an appropriate message.
# Modifying Elements:
# Write a function that:

# Accepts a list, an index, and a new value as inputs.
# Replaces the element at the specified index with the new value.
# If the index is out of range, return an appropriate message.
# Slicing the List:
# Write a function that:

# Accepts a list, a start index, and an end index as inputs.
# Returns a new list containing the elements from the start index up to (but not including) the end index.
# Handles cases where the indices are out of range.
# Game Interaction:
# Create a simple text-based game that:

# Prompts the user to select an operation (access, modify, slice).
# Asks for the necessary inputs (index, new value, etc.).
# Displays the result and the updated list.


def access_element(lst, index):
    """Returns the element at the given index, or an error message if out of range."""
    if 0 <= index < len(lst):
        return f"Element at index {index}: {lst[index]}"
    else:
        return "Index out of range!"

def modify_element(lst, index, new_value):
    """Modifies the element at the given index, or returns an error if out of range."""
    if 0 <= index < len(lst):
        lst[index] = new_value
        return f"Updated list: {lst}"
    else:
        return "Index out of range!"

def slice_list(lst, start, end):
    """Returns a sliced portion of the list, handling out-of-range indices."""
    if 0 <= start < len(lst) and 0 < end <= len(lst) and start < end:
        return f"Sliced list: {lst[start:end]}"
    else:
        return "Invalid slice range!"

def main():
    my_list = ["apple", "banana", "orange", "grape", "pineapple"]

    while True:
        print("\nCurrent list:", my_list)
        print("Choose an operation:\n1. Access an element\n2. Modify an element\n3. Slice the list\n4. Exit")
        choice = input("Enter choice (1-4): ")

        if choice == "1":
            index = int(input("Enter index to access: "))
            print(access_element(my_list, index))
        
        elif choice == "2":
            index = int(input("Enter index to modify: "))
            new_value = input("Enter new value: ")
            print(modify_element(my_list, index, new_value))
        
        elif choice == "3":
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            print(slice_list(my_list, start, end))
        
        elif choice == "4":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice! Please enter 1, 2, 3, or 4.")

main()
# This program allows the user to practice accessing, modifying, and slicing elements in a list.
# It provides a simple text-based interface for interaction, making it easy to understand and use.