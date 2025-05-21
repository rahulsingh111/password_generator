from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import os

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!#$%&()*+'

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get().strip()
    email = email_entry.get().strip()
    password = password_entry.get().strip()

    if not website or not password or not email:
        messagebox.showerror(title="Error", message="Please fill all fields.")
        return

    is_ok = messagebox.askokcancel(title=website,
                                   message=f"Save the following details?\n\nWebsite: {website}\nEmail: {email}\nPassword: {password}")
    if is_ok:
        with open('password.txt', 'a') as file:
            file.write(f"{website} | {email} | {password}\n")
        website_entry.delete(0, END)
        password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
def start_app():
    global password_entry, website_entry, email_entry

    window = Tk()
    window.title("Password Manager")
    window.config(padx=50, pady=20)

    canvas = Canvas(width=200, height=200)
    logo_path = os.path.join("assets", "logo.png")
    try:
        logo_img = PhotoImage(file=logo_path)
        canvas.create_image(100, 100, image=logo_img)
    except TclError:
        pass
    canvas.grid(row=0, column=1)

    Label(text="Website").grid(row=1, column=0)
    Label(text="Email").grid(row=2, column=0)
    Label(text="Password").grid(row=3, column=0)

    website_entry = Entry(width=35)
    website_entry.grid(row=1, column=1, columnspan=2)
    website_entry.focus()

    email_entry = Entry(width=35)
    email_entry.grid(row=2, column=1, columnspan=2)

    password_entry = Entry(width=21)
    password_entry.grid(row=3, column=1)

    Button(text="Generate Password", command=generate_password).grid(row=3, column=2)
    Button(text="Add", width=36, command=save).grid(row=4, column=1, columnspan=2)

    window.mainloop()

if __name__ == "__main__":
    start_app()
