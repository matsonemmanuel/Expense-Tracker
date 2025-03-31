import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import csv

# Function to add expense
def add_expense():
    name = name_entry.get()
    amount = amount_entry.get()
    category = category_var.get()
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if not name or not amount or not category:
        messagebox.showwarning("Input Error", "All fields must be filled!")
        return
    
    try:
        amount = float(amount)  # Convert amount to float
    except ValueError:
        messagebox.showwarning("Input Error", "Amount must be a number!")
        return

    expense_list.insert("", "end", values=(name, f"${amount:.2f}", category, date))
    update_total()
    name_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    category_var.set("")

# Function to update total expense
def update_total():
    total = 0.0
    for item in expense_list.get_children():
        total += float(expense_list.item(item, "values")[1][1:])  # Extract numeric value
    total_label.config(text=f"Total: ${total:.2f}")

# Function to clear all expenses
def clear_all():
    expense_list.delete(*expense_list.get_children())
    update_total()

# Function to delete selected expense
def delete_expense():
    selected_item = expense_list.selection()
    if not selected_item:
        messagebox.showwarning("Selection Error", "Please select an expense to delete!")
        return
    
    expense_list.delete(selected_item)
    update_total()

# Function to search expenses
def search_expense():
    query = search_entry.get().lower()
    for item in expense_list.get_children():
        values = expense_list.item(item, "values")
        if query in values[0].lower() or query in values[2].lower():
            expense_list.selection_set(item)
            expense_list.focus(item)
            return
    messagebox.showinfo("Search Result", "No matching expense found.")

# Create main window
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("600x500")
root.configure(bg="#f4f4f4")

# Styling
style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=5)
style.configure("Treeview.Heading", font=("Arial", 12, "bold"))

# Frame for input fields
frame = tk.Frame(root, bg="darkgreen", padx=20, pady=20, relief=tk.RIDGE, bd=2)
frame.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

# Input fields
tk.Label(frame, text="Expense Name:", bg="#ffffff", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(frame, font=("Arial", 12))
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame, text="Amount:", bg="#ffffff", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5)
amount_entry = tk.Entry(frame, font=("Arial", 12))
amount_entry.grid(row=1, column=1, padx=10, pady=5)

# Dropdown for categories
category_options = ["Food", "Transport", "Entertainment", "Shopping", "Bills", "Education", "Other"]
category_var = tk.StringVar()

tk.Label(frame, text="Category:", bg="#ffffff", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=5)
category_entry = ttk.Combobox(frame, textvariable=category_var, font=("Arial", 12), values=category_options, state="editable")
category_entry.grid(row=2, column=1, padx=10, pady=5)
category_entry.set("")  # Default empty

# Buttons
button_frame = tk.Frame(root, bg="darkgreen")
button_frame.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

ttk.Button(button_frame, text="Add Expense", command=add_expense).grid(row=0, column=0, padx=10, pady=10)
ttk.Button(button_frame, text="Clear All", command=clear_all).grid(row=0, column=1, padx=10, pady=10)

delete_button = tk.Button(button_frame, text="Delete Expense", command=delete_expense, bg="red", fg="white", font=("Arial", 12))
delete_button.grid(row=0, column=2, padx=10, pady=10)

# Search Bar
search_frame = tk.Frame(root)
search_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
search_entry = tk.Entry(search_frame, font=("Arial", 12))
search_entry.grid(row=0, column=0, padx=10, pady=5)
ttk.Button(search_frame, text="Search", command=search_expense).grid(row=0, column=1, padx=10, pady=5)

# Expense List
list_frame = tk.Frame(root, bg="darkgreen", padx=10, pady=10, relief=tk.RIDGE, bd=2)
list_frame.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

columns = ("Name", "Amount", "Category", "Date")
expense_list = ttk.Treeview(list_frame, columns=columns, show="headings")
expense_list.heading("Name", text="Name")
expense_list.heading("Amount", text="Amount")
expense_list.heading("Category", text="Category")
expense_list.heading("Date", text="Date")
expense_list.pack()

# Total Label
total_label = tk.Label(root, text="Total: $0.00", font=("Arial", 14, "bold"), bg="Orange")
total_label.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

# Run the application
root.mainloop()
