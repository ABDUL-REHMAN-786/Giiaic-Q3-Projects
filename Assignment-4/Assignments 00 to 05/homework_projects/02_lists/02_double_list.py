# Write a program that doubles each element in a list of numbers. For example, if you start with this list:

# numbers = [1, 2, 3, 4]

# You should end with this list:

# numbers = [2, 4, 6, 8]


def double_list(num_list):
    """Returns a new list with each element doubled."""
    return [num * 2 for num in num_list]  # List comprehension to double each element

# Example usage
numbers = [1, 2, 3, 4]  # Original list
doubled_numbers = double_list(numbers)  # Call the function to double the values

# Display the result
print(f"Original list: {numbers}")
print(f"Doubled list: {doubled_numbers}")
# Output:
# Original list: [1, 2, 3, 4]