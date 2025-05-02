# Sophia has a fruit store. She has written a function num_in_stock 
# which takes a string fruit as a parameter and returns how many of that 
# fruit are in her inventory. Write code in main() which will:

# Prompt the user to enter a fruit ("Enter a fruit: ")

# Call num_in_stock(fruit) to get the number of that fruit that Sophia has in stock

# Print the number which are in stock if Sophia has that fruit in her inventory (there are more than 0 in stock)

# Print "This fruit is not in stock." if Sophia has none of that fruit in her inventory.

# Here's two sample runs of the program (user input in bold italics):

# Enter a fruit: pear

# This fruit is in stock! Here is how many:

# 1000

# Enter a fruit: lychee

# This fruit is not in stock.


# Example inventory dictionary
inventory = {
    "apple": 500,
    "banana": 300,
    "pear": 1000,
    "orange": 450,
    "grape": 600
}

def num_in_stock(fruit):
    """Returns the number of a given fruit in stock."""
    return inventory.get(fruit.lower(), 0)  # Returns count if available, else 0

def main():
    fruit = input("Enter a fruit: ").strip().lower()  # Get user input, normalize case
    stock = num_in_stock(fruit)

    if stock > 0:
        print("\nThis fruit is in stock! Here is how many:\n", stock)
    else:
        print("\nThis fruit is not in stock.")

# Run the main function
main()
# The num_in_stock function checks the inventory for the specified fruit and returns the count.
# The main function prompts the user for a fruit, checks its stock, and prints the appropriate message.