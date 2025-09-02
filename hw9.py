import tkinter as tk
from tkinter import messagebox

def calculate_interest():
    try:
        # Get values from input fields
        principal = float(entry_principal.get())
        time = float(entry_time.get())
        rate = float(entry_rate.get())
        
        # Simple Interest formula
        si = (principal * rate * time) / 100
        
        # Compound Interest formula
        ci = principal * ((1 + rate / 100) ** time) - principal
        
        # Show results
        result_label.config(text=f"Simple Interest: {si:.2f}\nCompound Interest: {ci:.2f}")
    
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

# Create main window
root = tk.Tk()
root.title("Interest Calculator")
root.geometry("400x300")
root.resizable(False, False)

# Labels and input fields
tk.Label(root, text="Principal Amount:", font=("Arial", 12)).pack(pady=5)
entry_principal = tk.Entry(root, font=("Arial", 12))
entry_principal.pack(pady=5)

tk.Label(root, text="Time Period (years):", font=("Arial", 12)).pack(pady=5)
entry_time = tk.Entry(root, font=("Arial", 12))
entry_time.pack(pady=5)

tk.Label(root, text="Rate of Interest (%):", font=("Arial", 12)).pack(pady=5)
entry_rate = tk.Entry(root, font=("Arial", 12))
entry_rate.pack(pady=5)

# Button
btn_calc = tk.Button(root, text="Calculate", font=("Arial", 12), command=calculate_interest)
btn_calc.pack(pady=15)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 14), fg="blue")
result_label.pack(pady=10)

# Run the app
root.mainloop()
