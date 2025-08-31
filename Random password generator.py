import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showerror("Error", "Password length must be at least 4.")
            return
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for length.")
        return

    characters = list(string.ascii_lowercase)
    if upper_var.get():
        characters.extend(string.ascii_uppercase)
    if digits_var.get():
        characters.extend(string.digits)
    if symbols_var.get():
        characters.extend("!@#$%^&*()-_=+[]{};:,.<>?/")

    password = []
    if upper_var.get():
        password.append(random.choice(string.ascii_uppercase))
    if digits_var.get():
        password.append(random.choice(string.digits))
    if symbols_var.get():
        password.append(random.choice("!@#$%^&*()-_=+[]{};:,.<>?/"))

    while len(password) < length:
        password.append(random.choice(characters))

    random.shuffle(password)
    result_var.set(''.join(password))

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(result_var.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# GUI setup
root = tk.Tk()
root.title("Strong password generator")
root.geometry("400x250")
root.resizable(False, False)

# Length input
tk.Label(root, text="Password length:").pack(pady=5)
length_entry = tk.Entry(root)
length_entry.insert(0, "16")
length_entry.pack()

# Options
upper_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include uppercase", variable=upper_var).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Include digits", variable=digits_var).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Include symbols", variable=symbols_var).pack(anchor="w", padx=20)

# Generate button
tk.Button(root, text="Generate password", command=generate_password).pack(pady=10)

# Result display
result_var = tk.StringVar()
tk.Entry(root, textvariable=result_var, width=40).pack()

# Copy button
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack(pady=5)

root.mainloop()