import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    try:
        length = int(length_entry.get())  # Get user input for password length
        if length < 4:
            messagebox.showerror("Error", "Password length must be at least 4.")
            return

        # Characters to use in password
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choices(characters, k=length))

        password_entry.delete(0, tk.END)  # Clear old password
        password_entry.insert(0, password)  # Insert new password

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    root.update()
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# GUI Setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("500x400")
root.resizable(False, False)

# Heading
tk.Label(root, text="Random Password Generator", font=("Arial", 14, "bold")).pack(pady=10)

# Password Length Input
tk.Label(root, text="Enter Password Length:", font=("Arial", 12)).pack()
length_entry = tk.Entry(root, font=("Arial", 12))
length_entry.pack(pady=5)

# Generate Button
generate_btn = tk.Button(root, text="Generate Password", font=("Arial", 12), command=generate_password)
generate_btn.pack(pady=10)

# Password Display
password_entry = tk.Entry(root, font=("Arial", 12), justify="center", width=30)
password_entry.pack(pady=5)

# Copy Button
copy_btn = tk.Button(root, text="Copy to Clipboard", font=("Arial", 12), command=copy_to_clipboard)
copy_btn.pack(pady=10)

# Run GUI
root.mainloop()
