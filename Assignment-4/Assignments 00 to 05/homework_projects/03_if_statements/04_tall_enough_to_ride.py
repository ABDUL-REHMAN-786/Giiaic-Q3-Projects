# Write a program which asks the user how tall they are and prints whether or not 
# they're taller than a pre-specified minimum height.

# In amusement parks (ah, the good old pre-pandemic days...), rollercoasters frequently 
# have minimum height requirements for safety reasons. Assume for now that the minimum height is 50 
# of whatever height unit you'd like

# Here's two sample runs (user input is in bold italics):

# How tall are you? 100

# You're tall enough to ride!

# How tall are you? 10

# You're not tall enough to ride, but maybe next year!

# (For an extra challenge, write code which will repeatedly ask a user how tall they 
#  are and tell them whether or not they're tall enough to ride, until the user doesn't
#    enter a height at all, in which case the program stops. Curious about how to do this? 
#  See the function tall_enough_extension() in the solution code!)




MIN_HEIGHT = 50  # Set the minimum height requirement

def check_height():
    """Continuously asks the user for their height and checks if they can ride."""
    while True:
        height = input("How tall are you? (Press Enter to exit) ")

        if height == "":  # Stop if the user enters nothing
            print("Goodbye!")
            break

        try:
            height = float(height)  # Convert input to a float
            if height >= MIN_HEIGHT:
                print("You're tall enough to ride!")
            else:
                print("You're not tall enough to ride, but maybe next year!")
        except ValueError:
            print("Please enter a valid number.")

# Run the program
check_height()
# The code checks if the user is tall enough to ride a rollercoaster based on a minimum height requirement.
# It continuously prompts the user for their height until they choose to exit by pressing Enter.