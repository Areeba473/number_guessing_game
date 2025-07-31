import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.secret_number = random.randint(1, 100)
        self.attempts = 0

        # Guess Entry
        tk.Label(root, text="Enter your guess (1-100):").pack(pady=5)
        self.guess_entry = tk.Entry(root)
        self.guess_entry.pack(pady=5)

        # Guess Button
        tk.Button(root, text="Submit Guess", command=self.check_guess).pack(pady=5)

        # Hint/Result Label
        self.hint_label = tk.Label(root, text="Guess a number!")
        self.hint_label.pack(pady=10)

        # Attempts Label
        self.attempts_label = tk.Label(root, text=f"Attempts: {self.attempts}")
        self.attempts_label.pack(pady=5)

    def check_guess(self):
        try:
            guess = int(self.guess_entry.get())
            self.attempts += 1
            self.attempts_label.config(text=f"Attempts: {self.attempts}")

            if guess < 1 or guess > 100:
                self.hint_label.config(text="Please enter a number between 1 and 100!")
            elif guess < self.secret_number:
                self.hint_label.config(text="Too low! Try again.")
            elif guess > self.secret_number:
                self.hint_label.config(text="Too high! Try again.")
            else:
                messagebox.showinfo("Congratulations!", f"You won! The number was {self.secret_number} in {self.attempts} attempts.")
                self.reset_game()
            self.guess_entry.delete(0, tk.END)
        except ValueError:
            self.hint_label.config(text="Please enter a valid number!")

    def reset_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.attempts_label.config(text=f"Attempts: {self.attempts}")
        self.hint_label.config(text="Guess a new number!")
        self.guess_entry.config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    app = NumberGuessingGame(root)
    root.mainloop()
