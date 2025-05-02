# Write the helper function print_divisors(num), which takes in a 
# number and prints all of its divisors (all the numbers from 1 to num 
# inclusive that num can be cleanly divided by (there is no remainder to the division). 
# Don't forget to call your function in main()!

# Here's a sample run (user input is in blue):

# Enter a number: 12 Here are the divisors of 12 1 2 3 4 6 12

def print_divisors(num):
    print(f"Here are the divisors of {num}")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=" ")
    print()  # Print a new line at the end

def main():
    num = int(input("Enter a number: "))
    print_divisors(num)

main()
# Note: The print_divisors function takes a number as input and prints all of its divisors.
# The main function prompts the user for a number and calls print_divisors to display the divisors.