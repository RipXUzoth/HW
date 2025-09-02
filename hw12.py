import tkinter as tk
from tkinter import filedialog, ttk, messagebox
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Function to load dataset
def load_dataset():
    global df
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if file_path:
        try:
            df = pd.read_csv(file_path)
            messagebox.showinfo("Success", "Dataset Loaded Successfully!")
            col_list = df.columns.tolist()
            combo_x['values'] = col_list
            combo_y['values'] = col_list
        except Exception as e:
            messagebox.showerror("Error", f"Could not load dataset: {e}")

# Function to visualize data
def visualize():
    try:
        plot_type = combo_plot.get()
        x = combo_x.get()
        y = combo_y.get()

        if df is None:
            messagebox.showerror("Error", "Please load a dataset first.")
            return

        plt.figure(figsize=(8, 6))

        if plot_type == "Histogram":
            sns.histplot(df[x], kde=True)
        elif plot_type == "Scatter Plot":
            sns.scatterplot(data=df, x=x, y=y)
        elif plot_type == "Boxplot":
            sns.boxplot(data=df, x=x, y=y)
        elif plot_type == "Heatmap":
            sns.heatmap(df.corr(), annot=True, cmap="coolwarm")

        plt.title(f"{plot_type}")
        plt.show()

    except Exception as e:
        messagebox.showerror("Error", f"Could not create visualization: {e}")


# Main window
root = tk.Tk()
root.title("Dataset Visualizer")
root.geometry("500x300")
root.resizable(False, False)

df = None  # dataset placeholder

# Load dataset button
btn_load = tk.Button(root, text="Load Dataset", font=("Arial", 12), command=load_dataset)
btn_load.pack(pady=10)

# Plot type selection
tk.Label(root, text="Select Plot Type:", font=("Arial", 12)).pack(pady=5)
combo_plot = ttk.Combobox(root, values=["Histogram", "Scatter Plot", "Boxplot", "Heatmap"], font=("Arial", 12))
combo_plot.pack(pady=5)

# X-axis selection
tk.Label(root, text="Select X-axis:", font=("Arial", 12)).pack(pady=5)
combo_x = ttk.Combobox(root, font=("Arial", 12))
combo_x.pack(pady=5)

# Y-axis selection
tk.Label(root, text="Select Y-axis:", font=("Arial", 12)).pack(pady=5)
combo_y = ttk.Combobox(root, font=("Arial", 12))
combo_y.pack(pady=5)

# Visualize button
btn_plot = tk.Button(root, text="Visualize", font=("Arial", 12), command=visualize)
btn_plot.pack(pady=15)

root.mainloop()
