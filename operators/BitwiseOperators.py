# This program demonstrates the use of bitwise operators in Python with user input.

# Function to perform Bitwise AND (&)
def bitwise_and(value1, value2):
    result = value1 & value2
    print(f"Bitwise AND (&): {value1} & {value2} = {result}")

# Function to perform Bitwise OR (|)
def bitwise_or(value1, value2):
    result = value1 | value2
    print(f"Bitwise OR (|): {value1} | {value2} = {result}")

# Function to perform Bitwise XOR (^)
def bitwise_xor(value1, value2):
    result = value1 ^ value2
    print(f"Bitwise XOR (^): {value1} ^ {value2} = {result}")

# Function to perform Bitwise Complement (~)
def bitwise_complement(value):
    result = ~value
    print(f"Bitwise Complement (~): ~{value} = {result}")

# Main function to take user input and call bitwise operations
if __name__ == "__main__":
    print("Demonstration of Bitwise Operators in Python:\n")

    # Take user input for the values
    value1 = int(input("Enter the first integer value: "))
    value2 = int(input("Enter the second integer value: "))

    print("\nResults:\n")

    # Perform and display results of bitwise operations
    bitwise_and(value1, value2)
    bitwise_or(value1, value2)
    bitwise_xor(value1, value2)
    bitwise_complement(value1)  # Complement for the first value
    bitwise_complement(value2)  # Complement for the second value
