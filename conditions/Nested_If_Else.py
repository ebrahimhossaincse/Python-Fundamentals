# Main function to take user input and simulate switch-case behavior in Python
if __name__ == "__main__":
    # Take user input for year and branch
    year = int(input("Enter the year (1, or 2): "))
    branch = input("Enter the branch (C for CSE, E for ECE, M for Mech): ").upper()

    # Check for year and branch, and print corresponding subjects
    if year == 1:
        if branch == 'C':
            print("Data structures, Java, Computer Organization")
        elif branch == 'E':
            print("Micro processors, Logic switching theory")
        elif branch == 'M':
            print("Drawing, Manufacturing Machines")
        else:
            print("Invalid branch input!")
    elif year == 2:
        if branch == 'C':
            print("Operating System, RDBMS")
        elif branch == 'E':
            print("Fundamentals of Logic Design, Microelectronics")
        elif branch == 'M':
            print("Internal Combustion Engines, Mechanical Vibration")
        else:
            print("Invalid branch input!")
    else:
        print("Invalid year input!")
