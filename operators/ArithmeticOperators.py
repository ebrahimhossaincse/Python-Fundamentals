# This program demonstrates arithmetic operations in Python.
# It takes two numbers as input from the user and performs various arithmetic calculations.

# Prompt the user for two numbers
x = int(input("Enter the first number (x): "))  # Convert input to an integer
y = int(input("Enter the second number (y): "))  # Convert input to an integer

# Perform and display arithmetic operations with detailed descriptions
print("\nArithmetic Operations:")

# Addition
print(f"1. Using '+' operator: {x} + {y} = {x + y}")  # Adds x and y

# Subtraction
print(f"2. Using '-' operator: {x} - {y} = {x - y}")  # Subtracts y from x

# Multiplication
print(f"3. Using '*' operator: {x} * {y} = {x * y}")  # Multiplies x and y

# Integer Division
if y != 0:
    print(f"4. Using '/' operator (integer division): {x} / {y} = {x / y}")  # Divides x by y (integer result)
else:
    print("4. Using '/' operator (integer division): Division by zero is not allowed.")

# Modulus
if y != 0:
    print(f"5. Using '%' operator: {x} % {y} = {x % y}")  # Finds remainder of x divided by y
else:
    print("5. Using '%' operator: Modulus by zero is not allowed.")

# Float Division
if y != 0:
    print(f"6. Using '/' operator (float division): {x} / {y} = {x / y:.2f}")  # Divides x by y (float result)
else:
    print("6. Using '/' operator (float division): Division by zero is not allowed.")
