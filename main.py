import tkinter as tk
from tkinter import messagebox
import random

words = ["apple", "banana", "orange", "mango", "grape", "kiwi, mango"]


def new_game():
    global chosen_word, guessed_letters, attempts_left

    chosen_word = random.choice(words)
    guessed_letters = []
    attempts_left = 6

    canvas.delete("all")

    canvas.create_line(20, 180, 120, 180, width=3)  # Base
    canvas.create_line(70, 20, 70, 180, width=3)  # Post
    canvas.create_line(70, 20, 120, 20, width=3)  # Top
    canvas.create_line(120, 20, 120, 40, width=3)  # Rope

    word_length = len(chosen_word)
    blank_space = "_" * word_length
    word_text = canvas.create_text(200, 100, text=blank_space, font=("Arial", 24), tag="word")

    attempts_label.config(text=f"Attempts Left: {attempts_left}")


def guess_letter(letter):
    global attempts_left

    letter_button[letter].config(state=tk.DISABLED)

    if letter in chosen_word:
        guessed_letters.append(letter)
        update_word_display()

        # Check if the word has been completely guessed
        if "_" not in canvas.itemcget("word", "text"):
            messagebox.showinfo("Hangman", "Congratulations! You won!")
            new_game()
    else:
        attempts_left -= 1
        update_attempts_display()

        if attempts_left == 0:
            messagebox.showinfo("Hangman", "You lost! The word was: " + chosen_word)
            new_game()


def update_word_display():
    word = canvas.itemcget("word", "text")
    new_word = ""

    for i, char in enumerate(chosen_word):
        if char in guessed_letters:
            new_word += char
        else:
            new_word += word[i]

    canvas.itemconfigure("word", text=new_word)


def update_attempts_display():
    attempts_label.config(text=f"Attempts Left: {attempts_left}")


window = tk.Tk()
window.title("Hangman")

canvas = tk.Canvas(window, width=400, height=200)
canvas.pack()

button_frame = tk.Frame(window)
button_frame.pack()

letter_button = {}
for letter in "abcdefghijklmnopqrstuvwxyz":
    letter_button[letter] = tk.Button(button_frame, text=letter, width=3,
                                      command=lambda l=letter: guess_letter(l))
    letter_button[letter].pack(side=tk.LEFT)

attempts_label = tk.Label(window, text="Attempts Left: 6")
attempts_label.pack()

new_game()

window.mainloop()
