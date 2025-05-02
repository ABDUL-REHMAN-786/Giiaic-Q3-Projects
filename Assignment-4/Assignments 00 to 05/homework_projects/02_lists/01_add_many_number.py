# Write a function that takes a list of numbers and returns the sum of those numbers.


def sum_of_numbers(numbers):
    """Returns the sum of all numbers in the list."""
    return sum(numbers)  # Uses the built-in sum() function to calculate the total sum

# Example usage
numbers_list = [1, 2, 3, 4, 5]  # Define a list of numbers
result = sum_of_numbers(numbers_list)  # Call the function and store the result

# Display the result
print(f"The sum of {numbers_list} is {result}")
# Output: The sum of [1, 2, 3, 4, 5] is 15
# The function works correctly and efficiently for any list of numbers.
