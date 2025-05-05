def check_age():
    age_input = input("Enter your age: ")
    
    if not age_input.isdigit():
        print("Error: Please enter a valid positive number for age.")
        return

    age = int(age_input)

    if age < 0:
        print("Error: Age cannot be negative.")
    else:
        if age % 2 == 0:
            print(f"The age {age} is even.")
        else:
            print(f"The age {age} is odd.")

# Run the function
check_age()