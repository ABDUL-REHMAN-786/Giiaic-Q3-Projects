# We've written a helper function for you called greet(name) '
# 'which takes as input a string name and prints a greeting. '
# 'Write some code in main() to get the user's name and then greet them, 
# being sure to call the greet(name) helper function.

# Here's a sample run of the program (user input in bold italics):

# What's your name? Sophia

# Greetings Sophia!


def greet(name):
    print(f"Greetings {name}!")

def main():
    name = input("What's your name? ")  # Get user input
    greet(name)  # Call the greet function

main()  # Run the program
# The greet function takes a name as input and prints a greeting message.
# The main function gets the user's name and calls the greet function to display the greeting.