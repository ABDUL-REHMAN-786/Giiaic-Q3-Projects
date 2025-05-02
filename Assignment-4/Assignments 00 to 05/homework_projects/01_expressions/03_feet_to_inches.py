# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. 
# Foot is the singular, and feet is the plural.

# Constant: Number of inches in one foot
INCHES_PER_FOOT = 12  

# Prompt the user to enter the number of feet
feet = float(input("Enter the number of feet: "))

# Convert feet to inches
inches = feet * INCHES_PER_FOOT

# Display the result with proper singular/plural formatting
unit = "foot" if feet == 1 else "feet"
print(f"{feet} {unit} is equal to {inches} inches.")
# The program converts feet to inches, where 1 foot = 12 inches.
# It prompts the user for input, performs the conversion, and displays the result.