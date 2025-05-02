# Write a program which asks a user for their age and lets them know if they can or can't vote in the '
# 'following three fictional countries.

# Around the world, different countries have different voting ages. In the fictional countries of 
# Peturksbouipo, Stanlau, and Mayengua, the voting ages are very different:

# the voting age in Peturksbouipo is 16 (in real life, this is the voting age in, for example, Scotland, 
#                                        Ethiopia, and Austria)

# the voting age in Stanlau is 25 (in real life this is the voting age in the United Arab Emirates)

# the voting age in Mayengua is 48 (in real life, as far as we can tell, this isn't the voting age anywhere)

# Your code should prompt the for their age and print whether or not they can vote in Peturksbouipo, Stanlau, 
# or Mayengua.

# Here's a sample run of the program (user input is in blue):

# How old are you? 20 You can vote in Peturksbouipo where the voting age is 16. 
# You cannot vote in Stanlau where the voting age is 25. 
# You cannot vote in Mayengua where the voting age is 48.


def check_voting_eligibility(age):
    """Checks and prints where the user can and cannot vote."""
    
    # Define voting ages for each fictional country
    voting_ages = {
        "Peturksbouipo": 16,
        "Stanlau": 25,
        "Mayengua": 48
    }
    
    # Iterate through the countries and check eligibility
    for country, min_age in voting_ages.items():
        if age >= min_age:
            print(f"You can vote in {country} where the voting age is {min_age}.")
        else:
            print(f"You cannot vote in {country} where the voting age is {min_age}.")

# Prompt user for their age
user_age = int(input("How old are you? "))

# Check voting eligibility
check_voting_eligibility(user_age)
# The code checks the user's age against the voting ages of three fictional countries and prints whether they can vote or not.
# It uses a dictionary to store the voting ages and a loop to iterate through the countries.