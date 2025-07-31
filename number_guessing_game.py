import tkinter as tk
from tkinter import messagebox, ttk
import random

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        
        # Make window full screen
        self.root.state('zoomed')  # For Windows
        self.root.configure(bg='#2c3e50')
        
        # Game variables
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.max_attempts = 8
        self.best_score = float('inf')
        
        # Configure grid weights for responsive layout
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
        self.create_widgets()
        
    def create_widgets(self):
        # Main container frame - more compact
        main_frame = tk.Frame(self.root, bg='#2c3e50')
        main_frame.grid(row=1, column=0, sticky='nsew', padx=30, pady=30)
        main_frame.grid_columnconfigure(0, weight=1)
        
        # Title
        title_label = tk.Label(
            main_frame,
            text="🎯 NUMBER GUESSING GAME",
            font=('Arial', 20, 'bold'),
            fg='#ecf0f1',
            bg='#2c3e50'
        )
        title_label.grid(row=0, column=0, pady=(0, 10))
        
        # Simple attempts counter at top - always visible
        self.simple_attempts_label = tk.Label(
            main_frame,
            text=f"🎯 ATTEMPTS: {self.attempts}/{self.max_attempts}",
            font=('Arial', 14, 'bold'),
            fg='#e74c3c',
            bg='#2c3e50'
        )
        self.simple_attempts_label.grid(row=1, column=0, pady=(0, 10))
        
        # Game info frame
        info_frame = tk.Frame(main_frame, bg='#34495e', relief='raised', bd=2)
        info_frame.grid(row=2, column=0, pady=10, sticky='ew', padx=20)
        info_frame.grid_columnconfigure(0, weight=1)
        
        # Instructions
        instruction_label = tk.Label(
            info_frame,
            text="I'm thinking of a number between 1 and 100.\nCan you guess it?\n\n⚠️ You have just 8 attempts to guess the number!",
            font=('Arial', 12),
            fg='#ecf0f1',
            bg='#34495e',
            justify='center'
        )
        instruction_label.grid(row=0, column=0, pady=15)
        
        # Input frame
        input_frame = tk.Frame(main_frame, bg='#2c3e50')
        input_frame.grid(row=3, column=0, pady=10)
        
        # Guess label
        guess_label = tk.Label(
            input_frame,
            text="Enter your guess:",
            font=('Arial', 12, 'bold'),
            fg='#ecf0f1',
            bg='#2c3e50'
        )
        guess_label.grid(row=0, column=0, pady=(0, 10))
        
        # Entry frame with styling
        entry_frame = tk.Frame(input_frame, bg='#34495e', relief='sunken', bd=2)
        entry_frame.grid(row=1, column=0, pady=10)
        
        self.guess_entry = tk.Entry(
            entry_frame,
            font=('Arial', 16),
            width=15,
            justify='center',
            bg='#ecf0f1',
            fg='#2c3e50',
            relief='flat'
        )
        self.guess_entry.grid(row=0, column=0, padx=10, pady=10)
        self.guess_entry.focus()
        
        # Bind Enter key
        self.guess_entry.bind('<Return>', lambda event: self.check_guess())
        
        # Submit button
        submit_button = tk.Button(
            input_frame,
            text="🎯 SUBMIT GUESS",
            command=self.check_guess,
            font=('Arial', 12, 'bold'),
            bg='#3498db',
            fg='white',
            relief='flat',
            padx=30,
            pady=10,
            cursor='hand2'
        )
        submit_button.grid(row=2, column=0, pady=15)
        
        # Bind hover effects
        submit_button.bind('<Enter>', lambda e: submit_button.config(bg='#2980b9'))
        submit_button.bind('<Leave>', lambda e: submit_button.config(bg='#3498db'))
        
        # Feedback frame - positioned immediately after submit button for better visibility
        feedback_frame = tk.Frame(main_frame, bg='#3498db', relief='raised', bd=3)
        feedback_frame.grid(row=4, column=0, pady=8, sticky='ew', padx=20)
        feedback_frame.grid_columnconfigure(0, weight=1)
        
        # Hint/Result Label - more prominent with better visibility
        self.hint_label = tk.Label(
            feedback_frame,
            text="🎲 Start guessing!",
            font=('Arial', 16, 'bold'),
            fg='white',
            bg='#3498db'
        )
        self.hint_label.grid(row=0, column=0, pady=12)
        

        
        # Stats frame - centered best score
        stats_frame = tk.Frame(main_frame, bg='#34495e', relief='raised', bd=2)
        stats_frame.grid(row=5, column=0, pady=8, sticky='ew', padx=20)
        stats_frame.grid_columnconfigure(0, weight=1)
        
        # Best score label - centered
        self.best_score_label = tk.Label(
            stats_frame,
            text="🏆 Best Score: -",
            font=('Arial', 12, 'bold'),
            fg='#f1c40f',
            bg='#34495e'
        )
        self.best_score_label.grid(row=0, column=0, pady=8)

    def check_guess(self):
        try:
            guess = int(self.guess_entry.get())
            self.attempts += 1
            # Update simple attempts counter at top
            simple_attempts_text = f"🎯 ATTEMPTS: {self.attempts}/{self.max_attempts}"
            self.simple_attempts_label.config(text=simple_attempts_text)

            if guess < 1 or guess > 100:
                self.hint_label.config(text="⚠️ Please enter a number between 1 and 100!", fg='white', bg='#e74c3c')
                self.attempts -= 1  # Don't count invalid attempts
                # Update simple attempts counter at top
                simple_attempts_text = f"🎯 ATTEMPTS: {self.attempts}/{self.max_attempts}"
                self.simple_attempts_label.config(text=simple_attempts_text)
            elif guess < self.secret_number:
                if self.attempts >= self.max_attempts:
                    self.game_over()
                else:
                    self.hint_label.config(text="📈 Too low! Try a higher number.", fg='white', bg='#3498db')
            elif guess > self.secret_number:
                if self.attempts >= self.max_attempts:
                    self.game_over()
                else:
                    self.hint_label.config(text="📉 Too high! Try a lower number.", fg='white', bg='#e67e22')
            else:
                # Update best score
                if self.attempts < self.best_score:
                    self.best_score = self.attempts
                    self.best_score_label.config(text=f"🏆 Best Score: {self.best_score}")
                
                messagebox.showinfo(
                    "🎉 CONGRATULATIONS!",
                    f"🎯 You won! The number was {self.secret_number}\n"
                    f"📊 You found it in {self.attempts} attempts!\n"
                    f"🏆 Best score: {self.best_score if self.best_score != float('inf') else self.attempts}"
                )
                self.reset_game()
            
            self.guess_entry.delete(0, tk.END)
            self.guess_entry.focus()
            
        except ValueError:
            self.hint_label.config(text="⚠️ Please enter a valid number!", fg='white', bg='#e74c3c')
            self.guess_entry.delete(0, tk.END)

    def game_over(self):
        messagebox.showinfo(
            "😔 GAME OVER!",
            f"💔 You lose! The number was {self.secret_number}\n"
            f"📊 You used all {self.max_attempts} attempts\n"
            f"🍀 Better luck next time!"
        )
        self.reset_game()

    def reset_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        # Reset simple attempts counter at top
        simple_attempts_text = f"🎯 ATTEMPTS: {self.attempts}/{self.max_attempts}"
        self.simple_attempts_label.config(text=simple_attempts_text)
        
        self.hint_label.config(text="🎲 Guess a new number!", fg='white', bg='#3498db')
        self.guess_entry.config(state=tk.NORMAL)
        self.guess_entry.delete(0, tk.END)
        self.guess_entry.focus()

if __name__ == "__main__":
    root = tk.Tk()
    app = NumberGuessingGame(root)
    root.mainloop()
