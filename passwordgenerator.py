import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())

    characters = ""
    if var_letters.get():
        characters += string.ascii_letters
    if var_numbers.get():
        characters += string.digits
    if var_symbols.get():
        characters += string.punctuation

    if characters == "":
        password_var.set("Select options!")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_var.set(password)

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_var.get())

# GUI
root = tk.Tk()
root.title("Password Generator")
root.geometry("350x350")

tk.Label(root, text="Password Generator", font=("Arial", 18, "bold")).pack(pady=10)

tk.Label(root, text="Password Length:").pack()
length_entry = tk.Entry(root)
length_entry.pack()
length_entry.insert(0, "12")

var_letters = tk.IntVar(value=1)
var_numbers = tk.IntVar(value=1)
var_symbols = tk.IntVar(value=1)

tk.Checkbutton(root, text="Include Letters", variable=var_letters).pack()
tk.Checkbutton(root, text="Include Numbers", variable=var_numbers).pack()
tk.Checkbutton(root, text="Include Symbols", variable=var_symbols).pack()

tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

password_var = tk.StringVar()
tk.Entry(root, textvariable=password_var, font=("Arial", 14), width=25).pack(pady=10)

tk.Button(root, text="Copy to Clipboard", command=copy_password).pack()

root.mainloop()
