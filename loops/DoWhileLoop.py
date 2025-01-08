# Main function to demonstrate do-while loop equivalent in Python
if __name__ == "__main__":
    i = 1
    while True:  # Infinite loop to mimic do-while behavior
        print(f"Iteration: {i}")
        i += 1
        if i > 5:  # Check condition at the end
            break
