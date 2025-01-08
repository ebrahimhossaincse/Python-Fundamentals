# Main function to demonstrate the ternary operator with user input
if __name__ == "__main__":
    print("Demonstration of Ternary Operator in Python:\n")

    # Take user input for the two integer values
    val1 = int(input("Enter the first integer value: "))
    val2 = int(input("Enter the second integer value: "))

    # Using ternary operator equivalent in Python
    result = (val2 * val1) if (val2 > val1) else val1

    # Output the result
    print(f"Ternary Operator Output: {result}")
