import tkinter as tk
import random

# Function to play the game
def play(user_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    # Decide the winner
    if user_choice == computer_choice:
        result = "It's a Draw!"
        color = "blue"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
        color = "green"
    else:
        result = "You Lose!"
        color = "red"

    # Update labels
    user_label.config(text=f"Your Choice: {user_choice}")
    comp_label.config(text=f"Computer's Choice: {computer_choice}")
    result_label.config(text=result, fg=color)

# Main Window
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x300")
root.resizable(False, False)

# Title Label
tk.Label(root, text="Rock Paper Scissors", font=("Arial", 16, "bold")).pack(pady=10)

# Choice Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Rock", font=("Arial", 12), width=10, command=lambda: play("Rock")).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Paper", font=("Arial", 12), width=10, command=lambda: play("Paper")).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Scissors", font=("Arial", 12), width=10, command=lambda: play("Scissors")).grid(row=0, column=2, padx=5)

# Result Labels
user_label = tk.Label(root, text="Your Choice: None", font=("Arial", 12))
user_label.pack(pady=5)

comp_label = tk.Label(root, text="Computer's Choice: None", font=("Arial", 12))
comp_label.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=15)

# Run the App
root.mainloop()
