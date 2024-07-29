import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x350")

       
        self.length_label = tk.Label(root, text="Password Length:")
        self.length_label.grid(row=0, column=0, padx=20, pady=20)
        self.length_entry = tk.Entry(root)
        self.length_entry.grid(row=0, column=1, padx=20, pady=20)

      
        self.uppercase_var = tk.IntVar()
        self.uppercase_checkbox = tk.Checkbutton(root, text="Include Uppercase Letters", variable=self.uppercase_var)
        self.uppercase_checkbox.grid(row=1, column=0, columnspan=2)

       
        self.numbers_var = tk.IntVar()
        self.numbers_checkbox = tk.Checkbutton(root, text="Include Numbers", variable=self.numbers_var)
        self.numbers_checkbox.grid(row=2, column=0, columnspan=2)

        self.special_chars_var = tk.IntVar()
        self.special_chars_checkbox = tk.Checkbutton(root, text="Include Special Characters", variable=self.special_chars_var)
        self.special_chars_checkbox.grid(row=3, column=0, columnspan=2)

        
        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=4, column=0, columnspan=2, pady=30)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for password length")
            return

        if length < 1:
            messagebox.showerror("Error", "Please enter a valid password length")
            return

        chars = string.ascii_lowercase
        if self.uppercase_var.get():
            chars += string.ascii_uppercase
        if self.numbers_var.get():
            chars += string.digits
        if self.special_chars_var.get():
            chars += string.punctuation

        if not chars:
            messagebox.showerror("Error", "Please select at least one character type")
            return

        password = "".join(random.choice(chars) for _ in range(length))
        messagebox.showinfo("Password", password)

root = tk.Tk()
my_password_generator = PasswordGenerator(root)
root.mainloop()
