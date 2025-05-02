# Problem #1: List Practice
# Now practice writing code with lists! Implement the functionality described in the comments below.

# def main(): # Create a list called fruit_list that contains the following fruits: 
#     # 'apple', 'banana', 'orange', 'grape', 'pineapple'.


def main():
    # Create a list called fruit_list
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    
    # Print the entire list
    print("Fruit list:", fruit_list)

    # Print the first fruit in the list
    print("First fruit:", fruit_list[0])

    # Print the last fruit in the list
    print("Last fruit:", fruit_list[-1])

    # Add 'mango' to the list
    fruit_list.append('mango')
    print("After adding mango:", fruit_list)

    # Remove 'banana' from the list
    fruit_list.remove('banana')
    print("After removing banana:", fruit_list)

    # Sort the list alphabetically
    fruit_list.sort()
    print("Sorted list:", fruit_list)

    # Print the length of the list
    print("Number of fruits:", len(fruit_list))

main()
# Problem #2: Dictionary Practice
# Now practice writing code with dictionaries! Implement the functionality described in the comments below.


