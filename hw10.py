import tkinter as tk
from tkinter import messagebox

def check_strength():
    password = entry_password.get()
    length = len(password)

    if length == 0:
        messagebox.showwarning("Empty Password", "Please enter a password.")
        return

    # Strength based on length
    if length < 5:
        strength = "Weak"
        color = "red"
    elif 5 <= length <= 8:
        strength = "Medium"
        color = "orange"
    else:
        strength = "Strong"
        color = "green"

    result_label.config(text=f"Password Strength: {strength}", fg=color)


# Create main window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x250")
root.resizable(False, False)

# Label & Entry
tk.Label(root, text="Enter Password:", font=("Arial", 12)).pack(pady=10)
entry_password = tk.Entry(root, show="*", font=("Arial", 12), width=25)
entry_password.pack(pady=5)

# Button
btn_check = tk.Button(root, text="Check Strength", font=("Arial", 12), command=check_strength)
btn_check.pack(pady=15)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=10)

# Run the app
root.mainloop()
