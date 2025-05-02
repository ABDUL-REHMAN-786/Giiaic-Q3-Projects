# Write a program that continually reads in mass from the user and then outputs the equivalent energy using Einstein's mass-energy equivalence formula (E stands for energy, m stands for mass, and C is the speed of light:

# E = m * c**2

# Almost 100 years ago, Albert Einstein famously discovered that mass and energy are interchangeable and are related by the above equation. You should ask the user for mass (m) in kilograms and use a constant value for the speed of light -- C = 299792458 m/s.

# Here's a sample run of the program (user input is in bold italics):

# Enter kilos of mass: 100

# e = m * C^2...

# m = 100.0 kg

# C = 299792458 m/s

# 8.987551787368176e+18 joules of energy!

# Define the speed of light as a constant (in meters per second)
C = 299792458  

while True:
    try:
        # Prompt the user to enter mass in kilograms
        mass = float(input("Enter kilos of mass (or type 0 to exit): "))

        # Exit condition
        if mass == 0:
            print("Exiting program. Goodbye!")
            break

        # Calculate energy using Einstein's equation E = m * C^2
        energy = mass * C**2

        # Display the results
        print("\ne = m * C^2...\n")
        print(f"m = {mass} kg")
        print(f"C = {C} m/s\n")
        print(f"{energy} joules of energy!\n")

    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except KeyboardInterrupt:
        print("\nExiting program. Goodbye!")