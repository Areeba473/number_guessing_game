import tkinter as tk
from tkinter import messagebox, ttk
import random
import json
import os
from datetime import datetime

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
        
        # Statistics tracking
        self.stats = {
            'games_played': 0,
            'games_won': 0,
            'games_lost': 0,
            'total_attempts': 0,
            'best_score': float('inf'),
            'average_attempts': 0,
            'last_played': None
        }
        
        # Theme system
        self.themes = {
            'dark': {
                'bg': '#2c3e50',
                'frame_bg': '#34495e',
                'text': '#ecf0f1',
                'accent': '#3498db',
                'success': '#27ae60',
                'warning': '#e74c3c',
                'attempts': '#e74c3c',
                'best_score': '#f1c40f'
            },
            'light': {
                'bg': '#ecf0f1',
                'frame_bg': '#bdc3c7',
                'text': '#2c3e50',
                'accent': '#3498db',
                'success': '#27ae60',
                'warning': '#e74c3c',
                'attempts': '#e74c3c',
                'best_score': '#f39c12'
            },
            'purple': {
                'bg': '#4a148c',
                'frame_bg': '#6a1b9a',
                'text': '#f3e5f5',
                'accent': '#ab47bc',
                'success': '#66bb6a',
                'warning': '#ef5350',
                'attempts': '#ef5350',
                'best_score': '#ffd54f'
            }
        }
        self.current_theme = 'dark'
        
        # Leaderboard
        self.leaderboard = []
        self.load_data()
        
        # Configure grid weights for responsive layout
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
        self.create_widgets()
        
    def load_data(self):
        """Load statistics and leaderboard from file"""
        try:
            if os.path.exists('game_data.json'):
                with open('game_data.json', 'r') as f:
                    data = json.load(f)
                    self.stats = data.get('stats', self.stats)
                    self.leaderboard = data.get('leaderboard', [])
                    self.best_score = self.stats['best_score']
        except:
            pass
    
    def save_data(self):
        """Save statistics and leaderboard to file"""
        try:
            data = {
                'stats': self.stats,
                'leaderboard': self.leaderboard
            }
            with open('game_data.json', 'w') as f:
                json.dump(data, f, indent=2)
        except:
            pass
    

    
    def change_theme(self, theme_name):
        """Change the game theme"""
        if theme_name in self.themes:
            self.current_theme = theme_name
            theme = self.themes[theme_name]
            
            # Update main window
            self.root.configure(bg=theme['bg'])
            
            # Update all widgets with new theme
            self.apply_theme(theme)
    
    def apply_theme(self, theme):
        """Apply theme colors to all widgets"""
        # Update main frame
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Frame):
                widget.configure(bg=theme['bg'])
                for child in widget.winfo_children():
                    if isinstance(child, tk.Label):
                        child.configure(bg=theme['bg'], fg=theme['text'])
                    elif isinstance(child, tk.Frame):
                        child.configure(bg=theme['frame_bg'])
                        for grandchild in child.winfo_children():
                            if isinstance(grandchild, tk.Label):
                                grandchild.configure(bg=theme['frame_bg'], fg=theme['text'])
    
    def show_statistics(self):
        """Show detailed statistics window"""
        stats_window = tk.Toplevel(self.root)
        stats_window.title("📊 Game Statistics")
        stats_window.geometry("400x500")
        stats_window.configure(bg=self.themes[self.current_theme]['bg'])
        
        # Calculate statistics
        win_rate = (self.stats['games_won'] / max(self.stats['games_played'], 1)) * 100
        avg_attempts = self.stats['total_attempts'] / max(self.stats['games_played'], 1)
        
        stats_text = f"""
📊 GAME STATISTICS

🎮 Games Played: {self.stats['games_played']}
🏆 Games Won: {self.stats['games_won']}
💔 Games Lost: {self.stats['games_lost']}
📈 Win Rate: {win_rate:.1f}%
🎯 Best Score: {self.stats['best_score'] if self.stats['best_score'] != float('inf') else 'None'}
📊 Average Attempts: {avg_attempts:.1f}
📅 Last Played: {self.stats['last_played'] or 'Never'}
        """
        
        stats_label = tk.Label(
            stats_window,
            text=stats_text,
            font=('Arial', 12),
            bg=self.themes[self.current_theme]['bg'],
            fg=self.themes[self.current_theme]['text'],
            justify='left'
        )
        stats_label.pack(pady=20, padx=20)
        
        # Close button
        close_btn = tk.Button(
            stats_window,
            text="❌ Close",
            command=stats_window.destroy,
            font=('Arial', 10, 'bold'),
            bg=self.themes[self.current_theme]['warning'],
            fg='white',
            relief='flat',
            padx=20,
            pady=10
        )
        close_btn.pack(pady=10)
    
    def show_leaderboard(self):
        """Show leaderboard window"""
        leaderboard_window = tk.Toplevel(self.root)
        leaderboard_window.title("🏆 Leaderboard")
        leaderboard_window.geometry("500x400")
        leaderboard_window.configure(bg=self.themes[self.current_theme]['bg'])
        
        # Title
        title_label = tk.Label(
            leaderboard_window,
            text="🏆 TOP PLAYERS",
            font=('Arial', 16, 'bold'),
            bg=self.themes[self.current_theme]['bg'],
            fg=self.themes[self.current_theme]['text']
        )
        title_label.pack(pady=10)
        
        # Create leaderboard display
        if not self.leaderboard:
            no_data_label = tk.Label(
                leaderboard_window,
                text="No scores yet! Play some games to see the leaderboard.",
                font=('Arial', 12),
                bg=self.themes[self.current_theme]['bg'],
                fg=self.themes[self.current_theme]['text']
            )
            no_data_label.pack(pady=20)
        else:
            # Sort leaderboard by score (ascending)
            sorted_leaderboard = sorted(self.leaderboard, key=lambda x: x['score'])
            
            # Create frame for leaderboard
            lb_frame = tk.Frame(leaderboard_window, bg=self.themes[self.current_theme]['bg'])
            lb_frame.pack(pady=10, padx=20, fill='both', expand=True)
            
            # Headers
            headers = tk.Frame(lb_frame, bg=self.themes[self.current_theme]['frame_bg'])
            headers.pack(fill='x', pady=5)
            
            tk.Label(headers, text="Rank", font=('Arial', 10, 'bold'), 
                    bg=self.themes[self.current_theme]['frame_bg'], 
                    fg=self.themes[self.current_theme]['text'], width=8).pack(side='left')
            tk.Label(headers, text="Score", font=('Arial', 10, 'bold'), 
                    bg=self.themes[self.current_theme]['frame_bg'], 
                    fg=self.themes[self.current_theme]['text'], width=8).pack(side='left')
            tk.Label(headers, text="Player", font=('Arial', 10, 'bold'), 
                    bg=self.themes[self.current_theme]['frame_bg'], 
                    fg=self.themes[self.current_theme]['text'], width=15).pack(side='left')
            tk.Label(headers, text="Date", font=('Arial', 10, 'bold'), 
                    bg=self.themes[self.current_theme]['frame_bg'], 
                    fg=self.themes[self.current_theme]['text'], width=15).pack(side='left')
            
            # Display entries
            for i, entry in enumerate(sorted_leaderboard[:10], 1):  # Top 10
                row = tk.Frame(lb_frame, bg=self.themes[self.current_theme]['frame_bg'])
                row.pack(fill='x', pady=2)
                
                # Rank with medal emoji
                rank_text = f"{'🥇' if i==1 else '🥈' if i==2 else '🥉' if i==3 else f'{i}.'}"
                tk.Label(row, text=rank_text, font=('Arial', 10), 
                        bg=self.themes[self.current_theme]['frame_bg'], 
                        fg=self.themes[self.current_theme]['text'], width=8).pack(side='left')
                
                tk.Label(row, text=str(entry['score']), font=('Arial', 10), 
                        bg=self.themes[self.current_theme]['frame_bg'], 
                        fg=self.themes[self.current_theme]['text'], width=8).pack(side='left')
                
                tk.Label(row, text=entry['player'], font=('Arial', 10), 
                        bg=self.themes[self.current_theme]['frame_bg'], 
                        fg=self.themes[self.current_theme]['text'], width=15).pack(side='left')
                
                tk.Label(row, text=entry['date'], font=('Arial', 10), 
                        bg=self.themes[self.current_theme]['frame_bg'], 
                        fg=self.themes[self.current_theme]['text'], width=15).pack(side='left')
        
        # Close button
        close_btn = tk.Button(
            leaderboard_window,
            text="❌ Close",
            command=leaderboard_window.destroy,
            font=('Arial', 10, 'bold'),
            bg=self.themes[self.current_theme]['warning'],
            fg='white',
            relief='flat',
            padx=20,
            pady=10
        )
        close_btn.pack(pady=10)
    
    def add_to_leaderboard(self, score):
        """Add current score to leaderboard"""
        player_name = f"Player_{len(self.leaderboard) + 1}"
        entry = {
            'player': player_name,
            'score': score,
            'date': datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        self.leaderboard.append(entry)
        self.save_data()
        
    def create_widgets(self):
        # Main container frame - more compact
        main_frame = tk.Frame(self.root, bg=self.themes[self.current_theme]['bg'])
        main_frame.grid(row=1, column=0, sticky='nsew', padx=20, pady=20)
        main_frame.grid_columnconfigure(0, weight=1)
        
        # Title
        title_label = tk.Label(
            main_frame,
            text="🎯 NUMBER GUESSING GAME",
            font=('Arial', 18, 'bold'),
            fg=self.themes[self.current_theme]['text'],
            bg=self.themes[self.current_theme]['bg']
        )
        title_label.grid(row=0, column=0, pady=(0, 8))
        
        # Simple attempts counter at top - always visible
        self.simple_attempts_label = tk.Label(
            main_frame,
            text=f"🎯 ATTEMPTS: {self.attempts}/{self.max_attempts}",
            font=('Arial', 12, 'bold'),
            fg=self.themes[self.current_theme]['attempts'],
            bg=self.themes[self.current_theme]['bg']
        )
        self.simple_attempts_label.grid(row=1, column=0, pady=(0, 8))
        
        # Game info frame
        info_frame = tk.Frame(main_frame, bg=self.themes[self.current_theme]['frame_bg'], relief='raised', bd=2)
        info_frame.grid(row=2, column=0, pady=8, sticky='ew', padx=20)
        info_frame.grid_columnconfigure(0, weight=1)
        
        # Instructions
        instruction_label = tk.Label(
            info_frame,
            text="I'm thinking of a number between 1 and 100.\nCan you guess it?\n\n⚠️ You have just 8 attempts to guess the number!",
            font=('Arial', 11),
            fg=self.themes[self.current_theme]['text'],
            bg=self.themes[self.current_theme]['frame_bg'],
            justify='center'
        )
        instruction_label.grid(row=0, column=0, pady=12)
        
        # Input frame
        input_frame = tk.Frame(main_frame, bg=self.themes[self.current_theme]['bg'])
        input_frame.grid(row=3, column=0, pady=8)
        
        # Guess label
        guess_label = tk.Label(
            input_frame,
            text="Enter your guess:",
            font=('Arial', 12, 'bold'),
            fg=self.themes[self.current_theme]['text'],
            bg=self.themes[self.current_theme]['bg']
        )
        guess_label.grid(row=0, column=0, pady=(0, 10))
        
        # Entry frame with styling
        entry_frame = tk.Frame(input_frame, bg=self.themes[self.current_theme]['frame_bg'], relief='sunken', bd=2)
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
            bg=self.themes[self.current_theme]['accent'],
            fg='white',
            relief='flat',
            padx=30,
            pady=10,
            cursor='hand2'
        )
        submit_button.grid(row=2, column=0, pady=10)
        
        # Bind hover effects
        submit_button.bind('<Enter>', lambda e: submit_button.config(bg='#2980b9'))
        submit_button.bind('<Leave>', lambda e: submit_button.config(bg=self.themes[self.current_theme]['accent']))
        
        # Feedback frame - positioned immediately after submit button for better visibility
        feedback_frame = tk.Frame(main_frame, bg=self.themes[self.current_theme]['accent'], relief='raised', bd=3)
        feedback_frame.grid(row=4, column=0, pady=8, sticky='ew', padx=20)
        feedback_frame.grid_columnconfigure(0, weight=1)
        
        # Hint/Result Label - more prominent with better visibility
        self.hint_label = tk.Label(
            feedback_frame,
            text="🎲 Start guessing!",
            font=('Arial', 16, 'bold'),
            fg='white',
            bg=self.themes[self.current_theme]['accent']
        )
        self.hint_label.grid(row=0, column=0, pady=12)
        
        # Enhanced controls frame
        controls_frame = tk.Frame(main_frame, bg=self.themes[self.current_theme]['bg'])
        controls_frame.grid(row=5, column=0, pady=8)
        
        # Theme buttons
        theme_frame = tk.Frame(controls_frame, bg=self.themes[self.current_theme]['bg'])
        theme_frame.grid(row=0, column=0, pady=5)
        
        tk.Label(theme_frame, text="🎨 Theme:", font=('Arial', 10, 'bold'),
                bg=self.themes[self.current_theme]['bg'], fg=self.themes[self.current_theme]['text']).pack(side='left')
        
        for theme_name in self.themes.keys():
            theme_btn = tk.Button(
                theme_frame,
                text=theme_name.title(),
                command=lambda t=theme_name: self.change_theme(t),
                font=('Arial', 8, 'bold'),
                bg=self.themes[self.current_theme]['accent'],
                fg='white',
                relief='flat',
                padx=10,
                pady=5
            )
            theme_btn.pack(side='left', padx=2)
        
        # Stats and leaderboard buttons
        buttons_frame = tk.Frame(controls_frame, bg=self.themes[self.current_theme]['bg'])
        buttons_frame.grid(row=1, column=0, pady=5)
        
        stats_button = tk.Button(
            buttons_frame,
            text="📊 Statistics",
            command=self.show_statistics,
            font=('Arial', 10, 'bold'),
            bg=self.themes[self.current_theme]['success'],
            fg='white',
            relief='flat',
            padx=15,
            pady=8,
            cursor='hand2'
        )
        stats_button.pack(side='left', padx=5)
        
        leaderboard_button = tk.Button(
            buttons_frame,
            text="🏆 Leaderboard",
            command=self.show_leaderboard,
            font=('Arial', 10, 'bold'),
            bg=self.themes[self.current_theme]['best_score'],
            fg='white',
            relief='flat',
            padx=15,
            pady=8,
            cursor='hand2'
        )
        leaderboard_button.pack(side='left', padx=5)
        


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
                
                # Update statistics
                self.update_stats(True)
                
                # Add to leaderboard
                self.add_to_leaderboard(self.attempts)
                
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
        # Update statistics
        self.update_stats(False)
        
        messagebox.showinfo(
            "😔 GAME OVER!",
            f"💔 You lose! The number was {self.secret_number}\n"
            f"📊 You used all {self.max_attempts} attempts\n"
            f"🍀 Better luck next time!"
        )
        self.reset_game()

    def update_stats(self, won):
        """Update game statistics"""
        self.stats['games_played'] += 1
        self.stats['total_attempts'] += self.attempts
        self.stats['last_played'] = datetime.now().strftime("%Y-%m-%d %H:%M")
        
        if won:
            self.stats['games_won'] += 1
            if self.attempts < self.stats['best_score']:
                self.stats['best_score'] = self.attempts
        else:
            self.stats['games_lost'] += 1
        
        # Update best score
        if self.stats['best_score'] < self.best_score:
            self.best_score = self.stats['best_score']
        
        self.save_data()

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
