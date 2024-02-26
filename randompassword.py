import string
import random
from tkinter import *

def generate_password():
    try:
        password_length = int(val_length.get())
        if password_length <= 0:
            raise ValueError("Please enter a positive password length.")

        selected_characters = ""

        if include_uppercase.get():
            selected_characters += string.ascii_uppercase
        if include_lowercase.get():
            selected_characters += string.ascii_lowercase
        if include_digits.get():
            selected_characters += string.digits
        if include_symbols.get():
            selected_characters += string.punctuation

        if not selected_characters:
            raise ValueError("Please select at least one character type.")

        generated_password = ''.join(random.choice(selected_characters) for _ in range(password_length))
        result.config(text="Generated Password: " + generated_password)
    except ValueError as e:
        result.config(text=str(e))

def clear_result():
    result.config(text="")

root = Tk()
root.title("Password Generator")
root.geometry("500x400")
root.configure(bg='lightgray')

frame_strength = Frame(root, bg='blue')
frame_strength.pack(pady=10)

label_strength = Label(frame_strength, text="Select Password Strength", fg='white', bg='blue',
                        font=('Helvetica', 12))
label_strength.pack(pady=5)

include_uppercase = IntVar()
include_lowercase = IntVar()
include_digits = IntVar()
include_symbols = IntVar()

cb_uppercase = Checkbutton(frame_strength, text="Uppercase", variable=include_uppercase)
cb_lowercase = Checkbutton(frame_strength, text="Lowercase", variable=include_lowercase)
cb_digits = Checkbutton(frame_strength, text="Digits", variable=include_digits)
cb_symbols = Checkbutton(frame_strength, text="Symbols", variable=include_symbols)

cb_uppercase.pack()
cb_lowercase.pack()
cb_digits.pack()
cb_symbols.pack()

frame_length = Frame(root, bg='red')
frame_length.pack(pady=10)

label_length = Label(frame_length, text="Enter Password Length", fg='white', bg='red',
                     font=('Helvetica', 12))
label_length.pack(pady=5)

val_length = StringVar()
password_length_entry = Entry(frame_length, textvariable=val_length)
password_length_entry.pack(pady=5)

generate_button = Button(root, text="Generate Password", command=generate_password, bg='green', fg='white',
                         font=('Helvetica', 12))
generate_button.pack(pady=10)

clear_button = Button(root, text="Clear Result", command=clear_result, bg='gray', fg='white',
                      font=('Helvetica', 12))
clear_button.pack(pady=5)

result = Label(root, text="", font=('Helvetica', 12))
result.pack()

root.mainloop()
