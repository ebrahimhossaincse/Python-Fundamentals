# Main function to take user input and check the condition
if __name__ == "__main__":
    # Take user input for two integer values
    value1 = int(input("Enter the first integer value: "))
    value2 = int(input("Enter the second integer value: "))
    expected_value = int(input("Enter the expected value: "))

    # Check if the sum of the two values is equal to 17
    if (value2 + value1) == expected_value:
        print("Condition Matched")
