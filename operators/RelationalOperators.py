# This program demonstrates the use of relational operators in Python with user input.

# Function to demonstrate Equal Operator (==)
def equal_operator_example(val1, val2):
    if val1 == val2:
        print(f"Equal Operator (==): {val1} == {val2} = True")
    else:
        print(f"Equal Operator (==): {val1} == {val2} = False")

# Function to demonstrate Not Equal Operator (!=)
def not_equal_operator_example(val1, val2):
    if val1 != val2:
        print(f"Not Equal Operator (!=): {val1} != {val2} = True")
    else:
        print(f"Not Equal Operator (!=): {val1} != {val2} = False")

# Function to demonstrate Greater Than Operator (>)
def greater_than_example(val1, val2):
    if val1 > val2:
        print(f"Greater Than Operator (>): {val1} > {val2} = True")
    else:
        print(f"Greater Than Operator (>): {val1} > {val2} = False")

# Function to demonstrate Less Than Operator (<)
def less_than_example(val1, val2):
    if val1 < val2:
        print(f"Lesser Than Operator (<): {val1} < {val2} = True")
    else:
        print(f"Lesser Than Operator (<): {val1} < {val2} = False")

# Function to demonstrate Greater Than or Equal Operator (>=)
def greater_than_or_equal_example(val1, val2):
    if val1 >= val2:
        print(f"Greater Than or Equal Operator (>=): {val1} >= {val2} = True")
    else:
        print(f"Greater Than or Equal Operator (>=): {val1} >= {val2} = False")

# Function to demonstrate Lesser Than or Equal Operator (<=)
def less_than_or_equal_example(val1, val2):
    if val1 <= val2:
        print(f"Lesser Than or Equal To Operator (<=): {val1} <= {val2} = True")
    else:
        print(f"Lesser Than or Equal To Operator (<=): {val1} <= {val2} = False")

# Main function to take user input and call relational operators
if __name__ == "__main__":
    print("Demonstration of Relational Operators in Python:\n")

    # Take user input for the two integers
    val1 = int(input("Enter the first integer value: "))
    val2 = int(input("Enter the second integer value: "))

    print("\nResults:\n")

    # Call functions to demonstrate relational operators
    equal_operator_example(val1, val2)
    not_equal_operator_example(val1, val2)
    greater_than_example(val1, val2)
    less_than_example(val1, val2)
    greater_than_or_equal_example(val1, val2)
    less_than_or_equal_example(val1, val2)
