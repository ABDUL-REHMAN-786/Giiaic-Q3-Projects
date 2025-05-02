# In this program we show an example of using dictionaries to keep track of information in a phonebook.


def phonebook_program():
    """Simple phonebook using a dictionary."""
    phonebook = {}  # Dictionary to store contacts

    while True:
        print("\nOptions:")
        print("1 - Add contact")
        print("2 - Look up contact")
        print("3 - Delete contact")
        print("4 - View all contacts")
        print("5 - Exit")

        choice = input("Choose an option: ")

        if choice == "1":  # Add contact
            name = input("Enter name: ")
            number = input("Enter phone number: ")
            phonebook[name] = number
            print(f"Added {name} with number {number}")

        elif choice == "2":  # Look up contact
            name = input("Enter name to look up: ")
            if name in phonebook:
                print(f"{name}'s number is {phonebook[name]}")
            else:
                print(f"{name} not found in the phonebook.")

        elif choice == "3":  # Delete contact
            name = input("Enter name to delete: ")
            if name in phonebook:
                del phonebook[name]
                print(f"{name} has been removed.")
            else:
                print(f"{name} not found.")

        elif choice == "4":  # View all contacts
            if phonebook:
                print("\nPhonebook Contacts:")
                for name, number in phonebook.items():
                    print(f"{name}: {number}")
            else:
                print("Phonebook is empty.")

        elif choice == "5":  # Exit
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

# Run the phonebook program
phonebook_program()
# This code implements a simple phonebook program using a dictionary to store contacts.
# The user can add, look up, delete contacts, and view all contacts.