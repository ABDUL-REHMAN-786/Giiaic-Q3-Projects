# Write a program which prompts the user for a temperature in Fahrenheit (this can be a number with decimal places!) and outputs the temperature converted to Celsius.

# The Celsius scale is widely used to measure temperature, but places still use Fahrenheit. Fahrenheit is another unit for temperature, but the scale is different from Celsius -- for example, 0 degrees Celsius is 32 degrees Fahrenheit!

# The equation you should use for converting from Fahrenheit to Celsius is the following:

# degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0

# (Note. The .0 after the 5 and 9 matters in the line above!!!)

# Here's a sample run of the program (user input is in bold italics):

# Enter temperature in Fahrenheit: 76

# Temperature: 76.0F = 24.444444444444443C

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0 / 9.0

# Prompt user for input
temp_fahrenheit = float(input("Enter temperature in Fahrenheit: "))

# Convert to Celsius
temp_celsius = fahrenheit_to_celsius(temp_fahrenheit)

# Display the result
print(f"Temperature: {temp_fahrenheit}F = {temp_celsius}C")
# This program converts a temperature from Fahrenheit to Celsius using the formula provided.
# It prompts the user for input, performs the conversion, and displays the result.