import tkinter as tk
from tkinter import messagebox
import sqlite3

# Function to create the database and table if they don't exist
def create_db():
    conn = sqlite3.connect("todo_list.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT)''')
    conn.commit()
    conn.close()

# Function to load tasks from the database
def load_tasks():
    conn = sqlite3.connect("todo_list.db")
    c = conn.cursor()
    c.execute("SELECT task FROM tasks")
    tasks = c.fetchall()
    tasks_list.delete(0, tk.END)  # Clear the listbox
    for task in tasks:
        tasks_list.insert(tk.END, task[0])
    conn.close()

# Function to save a new task to the database
def add_task():
    task = task_entry.get()
    if task:
        conn = sqlite3.connect("todo_list.db")
        c = conn.cursor()
        c.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
        conn.commit()
        conn.close()
        tasks_list.insert(tk.END, task)  # Add task to the listbox
        task_entry.delete(0, tk.END)  # Clear the input field
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Function to remove a selected task from the database and listbox
def remove_task():
    try:
        selected_task_index = tasks_list.curselection()[0]
        selected_task = tasks_list.get(selected_task_index)

        conn = sqlite3.connect("todo_list.db")
        c = conn.cursor()
        c.execute("DELETE FROM tasks WHERE task = ?", (selected_task,))
        conn.commit()
        conn.close()

        tasks_list.delete(selected_task_index)  # Remove from the listbox
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to remove.")

# Function to clear all tasks from the database and listbox
def clear_tasks():
    conn = sqlite3.connect("todo_list.db")
    c = conn.cursor()
    c.execute("DELETE FROM tasks")
    conn.commit()
    conn.close()
    
    tasks_list.delete(0, tk.END)  # Clear all tasks from the listbox

# Create the main window
root = tk.Tk()
root.title("To-Do List Application")

# Set the window size
root.geometry("400x400")

# Task entry label
task_label = tk.Label(root, text="Enter a new task:", font=("Helvetica", 12))
task_label.pack(pady=10)

# Entry widget for new task
task_entry = tk.Entry(root, font=("Helvetica", 12), width=30)
task_entry.pack(pady=5)

# Buttons to add, remove, and clear tasks
add_button = tk.Button(root, text="Add Task", font=("Helvetica", 12), command=add_task)
add_button.pack(pady=5)

remove_button = tk.Button(root, text="Remove Task", font=("Helvetica", 12), command=remove_task)
remove_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear All Tasks", font=("Helvetica", 12), command=clear_tasks)
clear_button.pack(pady=10)

# Listbox to display tasks
tasks_list = tk.Listbox(root, font=("Helvetica", 12), width=40, height=10)
tasks_list.pack(pady=10)

# Load existing tasks from the database when starting the app
create_db()  # Ensure the database and table exist
load_tasks()  # Load tasks from the database

# Run the main loop
root.mainloop()
