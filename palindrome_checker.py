import tkinter as tk

# Function to check if a word or phrase is a palindrome
def is_palindrome(s):
    # Remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()

    # Check if the string is equal to its reverse
    return s == s[::-1]

# Function to handle button click and update the result label
def check_palindrome():
    user_input = entry.get()
    if is_palindrome(user_input):
        result_label.config(text=f"'{user_input}' is a palindrome!", fg="green")
    else:
        result_label.config(text=f"'{user_input}' is not a palindrome.", fg="red")

# Create the main window
root = tk.Tk()
root.title("Palindrome Checker")
root.geometry("400x250")  # Set window size
root.resizable(False, False)  # Prevent resizing

# Add a label for instructions
label = tk.Label(root, text="Enter a word or phrase:", font=("Helvetica", 14))
label.pack(pady=20)

# Add an entry widget for user input
entry = tk.Entry(root, font=("Helvetica", 12), width=30)
entry.pack(pady=10)

# Add a button to check if the input is a palindrome
check_button = tk.Button(root, text="Check Palindrome", font=("Helvetica", 12), command=check_palindrome)
check_button.pack(pady=10)

# Label to display the result
result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=20)

# Run the main loop
root.mainloop()
