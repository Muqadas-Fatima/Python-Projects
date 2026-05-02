import tkinter as tk
import random

# Function to start a new game
def new_game():
    global secret_number
    secret_number = random.randint(1, 100)
    result_label.config(text="Guess a number between 1 and 100")
    guess_button.config(state=tk.NORMAL)
    guess_entry.delete(0, tk.END)

# Function to check the guess
def check_guess():
    try:
        guess = int(guess_entry.get())
        if guess < secret_number:
            result_label.config(text="Too low! Try again.")
        elif guess > secret_number:
            result_label.config(text="Too high! Try again.")
        else:
            result_label.config(text="Congratulations! You guessed it right.")
            guess_button.config(state=tk.DISABLED)
    except ValueError:
        result_label.config(text="Please enter a valid number.")

# Create the main window
root = tk.Tk()
root.title("Number Guessing Game")

# Set the window size
root.geometry("300x200")

# Label for instructions or results
result_label = tk.Label(root, text="Guess a number between 1 and 100", font=("Helvetica", 12))
result_label.pack(pady=10)

# Entry widget for user input
guess_entry = tk.Entry(root, font=("Helvetica", 12))
guess_entry.pack(pady=5)

# Button to submit the guess
guess_button = tk.Button(root, text="Guess", font=("Helvetica", 12), command=check_guess)
guess_button.pack(pady=5)

# Button to start a new game
new_game_button = tk.Button(root, text="Start New Game", font=("Helvetica", 12), command=new_game)
new_game_button.pack(pady=10)

# Start the first game
new_game()

# Run the main loop
root.mainloop()
