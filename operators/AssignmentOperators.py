# This program demonstrates the use of assignment operators in Python.
# It takes two numbers as input from the user and performs calculations using assignment operators.

# Prompt the user for two numbers
value1 = int(input("Enter the first value (value1): "))  # Convert input to an integer
value2 = int(input("Enter the second value (value2): "))  # Convert input to an integer

# Display initial values
print(f"\nInitial values: value1 = {value1}, value2 = {value2}\n")

# Using '+=' operator
value1 += value2  # value1 = value1 + value2
print(f"1. Used '+=' operator: value1 = {value1}")

# Using '-=' operator
value1 -= value2  # value1 = value1 - value2
print(f"2. Used '-=' operator: value1 = {value1}")

# Using '*=' operator
value1 *= value2  # value1 = value1 * value2
print(f"3. Used '*=' operator: value1 = {value1}")

# Using '/=' operator
if value2 != 0:
    value1 //= value2  # value1 = value1 // value2 (integer division)
    print(f"4. Used '/=' operator: value1 = {value1}")
else:
    print("4. Used '/=' operator: Division by zero is not allowed.")

# Using '%=' operator
if value2 != 0:
    value1 %= value2  # value1 = value1 % value2
    print(f"5. Used '%=' operator: value1 = {value1}")
else:
    print("5. Used '%=' operator: Modulus by zero is not allowed.")
