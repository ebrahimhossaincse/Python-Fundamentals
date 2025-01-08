# Main function to take user input and compare two numbers
if __name__ == "__main__":
    # Take user input for two integer values
    value1 = int(input("Enter your 1st number: "))
    value2 = int(input("Enter your 2nd number: "))

    # Compare the values and print the appropriate result
    if value1 > value2:
        print(f"{value1} is greater than {value2}")
    elif value1 < value2:
        print(f"{value1} is less than {value2}")
    elif value1 == value2:
        print(f"{value1} is equal to {value2}")
    else:
        print("Something went wrong...")
