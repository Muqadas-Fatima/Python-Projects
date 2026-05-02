import tkinter as tk
from tkinter import messagebox

def is_prime(number):
    """Function to check if a number is prime"""
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False  # Even numbers (except 2) are not prime

    # Check for divisibility up to √number
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    return True

def check_prime():
    try:
        num = int(entry.get())  # Get user input
        
        if num < 0:
            messagebox.showerror("Error", "Please enter a positive number.")
            return
        
        if is_prime(num):
            result_label.config(text=f"{num} is a Prime Number ✅", fg="green")
        else:
            result_label.config(text=f"{num} is NOT a Prime Number ❌", fg="red")

    except ValueError:
        messagebox.showerror("Error", "Invalid input! Please enter a valid number.")

# Create main window
root = tk.Tk()
root.title("Prime Number Checker")
root.geometry("400x300")
root.resizable(False, False)

# Title label
title_label = tk.Label(root, text="Prime Number Checker", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Input field
entry_label = tk.Label(root, text="Enter a Number:")
entry_label.pack()
entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=5)

# Check button
check_button = tk.Button(root, text="Check Prime", command=check_prime, bg="blue", fg="white", font=("Arial", 12))
check_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=10)

# Run the application
root.mainloop()
