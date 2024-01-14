import random
import tkinter as tk
from tkinter import messagebox

def read_words(filename):
    with open(filename, 'r') as file:
        return file.read().splitlines()

adjectives = read_words('adjectives.txt')
nouns = read_words('nouns.txt')

symbol_dict = {"a": "@", "c": "(", "e": "3", "i": "!", "o": "0", "s": "$", "t": "+", "x": "%", "b": "8"}

def generate_password(simplicity):
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    password = list(adjective.capitalize() + noun.capitalize())

    if simplicity >= 4:
        # Add an extra adjective if simplicity is 4 or 5
        extra_adjective = random.choice(adjectives)
        password = list(extra_adjective.capitalize() + ''.join(password))

    # Ensure the first letter is always lowercase
    password[0] = password[0].lower()

    # Get a list of indices for letters in the password that can be replaced
    replaceable_indices = [i for i, letter in enumerate(password) if letter.lower() in symbol_dict]

    if replaceable_indices and simplicity >= 3:
        # Determine the number of letters to replace based on the simplicity
        num_letters_to_replace = 1 if simplicity == 3 else 2 if simplicity == 4 else 3 if simplicity == 5 else 0

        # Choose random indices to replace
        indices_to_replace = random.sample(replaceable_indices, num_letters_to_replace)

        # Replace the letters at the chosen indices with their corresponding symbols
        for index in indices_to_replace:
            password[index] = symbol_dict[password[index].lower()]

    # Generate a random number and append it to the password
    num_digits = 4 if simplicity == 5 else 3 if simplicity >= 4 else 2 if simplicity == 3 else 1 if simplicity == 2 else 0
    if num_digits > 0:
        password.append(str(random.randint(10 ** (num_digits - 1), 10 ** num_digits - 1)))

    return ''.join(password)

def display_password():
    simplicity = slider.get()
    password = generate_password(simplicity)
    password_label.config(text=password)

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_label.cget("text"))

root = tk.Tk()
root.geometry('500x330')  # Set the size of the window
root.configure(bg='lightblue')  # Set the background color of the window
root.title("Eddie's Password Generator")  # Set the title of the window
root.resizable(False, False)  # Disable resizing the window

title_label = tk.Label(root, text="Eddie's Password Generator", font=('Century Gothic', 24), bg='lightblue')  # Increase the font size and set the background color
title_label.pack(pady=5)  # Add vertical padding

simplicity_label = tk.Label(root, text="Simplicity", font=('Century Gothic', 16), bg='lightblue')  # Increase the font size and set the background color
simplicity_label.pack(pady=5)  # Add vertical padding

slider = tk.Scale(root, from_=1, to=5, orient=tk.HORIZONTAL, font=('Century Gothic', 16), bg='lightblue')  # Increase the font size and set the background color
slider.pack(pady=5)  # Add vertical padding

generate_button = tk.Button(root, text="Generate Password", command=display_password, font=('Century Gothic', 16), bg='lightgrey')  # Increase the font size and set the background color
generate_button.pack(pady=5)  # Add vertical padding

password_label = tk.Label(root, text="", font=('Century Gothic', 24), bg='lightblue')  # Increase the font size and set the background color
password_label.pack(pady=5)  # Add vertical padding

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, font=('Century Gothic', 16), bg='lightgrey')  # Increase the font size and set the background color
copy_button.pack(pady=5)  # Add vertical padding

root.mainloop()
