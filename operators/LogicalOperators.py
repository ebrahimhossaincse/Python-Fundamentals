# This program demonstrates the use of logical operators in Python.

# Function to demonstrate Logical AND (and)
def logical_and_example(a, b):
    print(f"Logical AND (and): {a} and {b} = {a and b}")

# Function to demonstrate Logical OR (or)
def logical_or_example(a, b):
    print(f"Logical OR (or): {a} or {b} = {a or b}")

# Function to demonstrate Logical NOT (not)
def logical_not_example(a):
    print(f"Logical NOT (not): not {a} = {not a}")

# Main function to take user input and call logical operations
if __name__ == "__main__":
    print("Demonstration of Logical Operators in Python:\n")

    # Take user input for the boolean values
    a = input("Enter the first boolean value (true/false): ").strip().lower() == 'true'
    b = input("Enter the second boolean value (true/false): ").strip().lower() == 'true'

    print("\nResults:\n")

    # Perform and display results of logical operations
    logical_and_example(a, b)
    logical_or_example(a, b)
    logical_not_example(a)
    logical_not_example(b)
