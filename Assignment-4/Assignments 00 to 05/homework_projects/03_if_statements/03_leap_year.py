# Write a program that reads a year from the user and tells whether a given year is a leap year or not.

# A leap year (also known as an intercalary year or bissextile year) is a calendar year that contains an additional day 
# (or, in the case of a lunisolar calendar, a month) added to keep the calendar year synchronized 
# with the astronomical year or seasonal year. In the Gregorian calendar, each leap year has 366 days 
# instead of 365, by extending February to 29 days rather than the common 28.

# In the Gregorian calendar, three criteria must be checked to identify leap years:

# The given year must be evenly divisible by 4;
# If the year can also be evenly divided by 100, it is NOT a leap year; unless:
# The year is also evenly divisible by 400. Then it is a leap year.
# Your code should use the above criteria to check for a leap year and then print either 
# "That's a leap year!" or "That's not a leap year."


def is_leap_year(input_year):
    """Returns True if the given year is a leap year, otherwise False."""
    if (input_year % 4 == 0 and input_year % 100 != 0) or (input_year % 400 == 0):
        return True
    return False

# Prompt the user for input
year = int(input("Enter a year: "))

# Check and print the result
if is_leap_year(year):
    print("That's a leap year!")
else:
    print("That's not a leap year.")
# The code checks if a given year is a leap year based on the Gregorian calendar rules.
# It defines a function `is_leap_year` that returns True or False based on the criteria provided.