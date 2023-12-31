import tkinter as tk
import random

class NumberGuessingGame(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Number Guessing Game")
        self.geometry("400x200")

        self.secret_number = random.randint(1, 100)
        self.attempts = 7

        self.label = tk.Label(self, text="Welcome to the Number Guessing Game!")
        self.label.pack(pady=10)

        self.entry = tk.Entry(self)
        self.entry.pack(pady=5)

        self.submit_button = tk.Button(self, text="Submit Guess", command=self.check_guess)
        self.submit_button.pack(pady=5)

        self.result_label = tk.Label(self, text="")
        self.result_label.pack(pady=10)

    def check_guess(self):
        guess = int(self.entry.get())
        self.entry.delete(0, tk.END)

        if guess < self.secret_number:
            self.result_label.config(text="Too low! Try again.")
        elif guess > self.secret_number:
            self.result_label.config(text="Too high! Try again.")
        else:
            self.result_label.config(text=f"Congratulations! You've guessed the number ({self.secret_number}) correctly!")
            self.submit_button.config(state=tk.DISABLED)
        
        self.attempts -= 1

        if self.attempts <= 0:
            self.result_label.config(text=f"Sorry, you're out of attempts. The secret number was {self.secret_number}.")
            self.submit_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    app = NumberGuessingGame()
    app.mainloop()
