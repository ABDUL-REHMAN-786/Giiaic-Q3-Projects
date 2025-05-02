# Write a program to solve this age-related riddle!

# Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:

# Anton is 21 years old.

# Beth is 6 years older than Anton.

# Chen is 20 years older than Beth.

# Drew is as old as Chen's age plus Anton's age.

# Ethan is the same age as Chen.

# Your code should store each person's age to a variable and print their names and ages at the end. '
# 'The autograder is sensitive to capitalization and punctuation, be careful! '
# 'Your solution should look like this (the below numbers are made up -- your solution should have the correct values!):



# Define ages based on the given conditions
anton_age = 21  # Anton's age is given
beth_age = anton_age + 6  # Beth is 6 years older than Anton
chen_age = beth_age + 20  # Chen is 20 years older than Beth
drew_age = chen_age + anton_age  # Drew's age is the sum of Chen's and Anton's ages
ethan_age = chen_age  # Ethan is the same age as Chen

# Print the ages of each friend
print(f"Anton is {anton_age} years old.")
print(f"Beth is {beth_age} years old.")
print(f"Chen is {chen_age} years old.")
print(f"Drew is {drew_age} years old.")
print(f"Ethan is {ethan_age} years old.")
# This program calculates and prints the ages of five friends based on given relationships.
# It uses simple arithmetic operations to derive each friend's age from Anton's age.