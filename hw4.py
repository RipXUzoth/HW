def shutdown(command):
    if command.lower() == "yes":
        return "Shutting down..."
    elif command.lower() == "no":
        return "Shutdown aborted."
    else:
        return "Invalid input. Please type 'yes' or 'no'."

# Example usage
user_input = input("Do you want to shut down the computer? (yes/no): ")
print(shutdown(user_input))