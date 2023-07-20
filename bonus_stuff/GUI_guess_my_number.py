import random
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Guess My Number")
root.geometry("450x300")
root.resizable(False, False)

ttk.Label(root, text="Guess My Number", font=("Arial", 20)).pack(pady=10)

guess = tk.StringVar()
guess.set("0")

ttk.Label(root, text="Enter a number between 1 and 10", font=("Arial", 20)).pack(pady=10)

entry = ttk.Entry(root, width=5, textvariable=guess, font=("Arial", 20))
entry.pack(pady=10)

tries = 0
number = random.randint(1, 10)


def check():
    global tries
    global number
    tries += 1

    if int(guess.get()) == number:
        info.configure(text=f"Tries: {tries}\n"
                            f"You guessed it!")
        tries = 0
        number = random.randint(1, 10)
    elif int(guess.get()) > number:
        info.configure(text=f"Tries: {tries}\n"
                            f"Too high!")
    else:
        info.configure(text=f"Tries: {tries}\n"
                            f"Too low!")


ttk.Button(root, text="Check", command=check).pack(pady=10)

info = ttk.Label(root, text=f"Tries: {tries}\n"
                            f"Pick a number.", font=("Arial", 20))
info.pack(pady=10)

root.mainloop()
