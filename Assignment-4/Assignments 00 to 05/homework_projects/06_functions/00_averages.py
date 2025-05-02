# Write a function that takes two numbers and finds the average between the two.

def find_average(num1, num2):
    """Returns the average of two numbers."""
    return (num1 + num2) / 2

# Example usage
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
average = find_average(a, b)
print(f"The average of {a} and {b} is {average}")
