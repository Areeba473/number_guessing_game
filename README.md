# 🎯 Number Guessing Game

A modern, full-screen number guessing game built with Python and Tkinter. Challenge yourself to guess a random number between 1 and 100 in just 8 attempts!

## 🚀 Features

- **🎮 Full-Screen Experience**: Immersive full-screen gameplay
- **🎯 8-Attempt Challenge**: Test your guessing skills with limited attempts
- **📊 Real-Time Feedback**: Get instant "too high" or "too low" hints
- **🎨 Multiple Themes**: Choose from Dark, Light, and Purple themes
- **⌨️ Keyboard Support**: Press Enter to submit your guess
- **🎲 Random Number Generation**: Each game features a new random number
- **📈 Detailed Statistics**: Track your gaming performance over time
- **🏆 Global Leaderboard**: Compete with other players worldwide

## 🎮 How to Play

1. **Start the Game**: Run the application to begin
2. **Read Instructions**: The game will tell you the rules
3. **Make Your Guess**: Enter a number between 1 and 100
4. **Get Feedback**: The game will tell you if your guess is too high or too low
5. **Keep Guessing**: You have 8 attempts to find the correct number
6. **Win or Lose**: Find the number to win, or run out of attempts to lose

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.6 or higher
- Tkinter (usually comes with Python)

### Installation Steps

1. **Clone or Download** the project files
2. **Navigate** to the project directory:
   ```bash
   cd number_guessing_game
   ```

3. **Run the Game**:
   ```bash
   python number_guessing_game.py
   ```

### Alternative Installation
If you don't have Python installed:

1. **Download Python** from [python.org](https://www.python.org/downloads/)
2. **Install Python** (make sure to check "Add Python to PATH")
3. **Run the game** using the command above

## 🎯 Game Rules

- **Objective**: Guess the secret number between 1 and 100
- **Attempts**: You have exactly 8 attempts
- **Feedback**: After each guess, you'll get a hint:
  - 📈 "Too low! Try a higher number"
  - 📉 "Too high! Try a lower number"
- **Invalid Input**: Numbers outside 1-100 don't count as attempts
- **Winning**: Guess the correct number within 8 attempts
- **Losing**: Run out of attempts without guessing correctly

## 🏆 Scoring System

- **Best Score**: Tracks your lowest number of attempts to win
- **Perfect Game**: Win in 1 attempt = Best score of 1
- **Challenge**: Try to beat your best score!

## 🎨 Interface Features

### Visual Elements
- **🎯 Title**: Clear game identification
- **📊 Attempts Counter**: Shows current attempts (X/8) at the top
- **💬 Instructions**: Clear game rules and warnings
- **⌨️ Input Field**: Easy-to-use number entry
- **🎯 Submit Button**: Click or press Enter to submit
- **💬 Feedback Box**: Blue box showing hints and messages
- **🎨 Theme Buttons**: Switch between Dark, Light, and Purple themes
- **📊 Statistics Button**: View detailed game statistics
- **🏆 Leaderboard Button**: View global leaderboard

### Color Schemes
- **Dark Theme**: Classic dark blue interface
- **Light Theme**: Clean white and gray interface
- **Purple Theme**: Vibrant purple and pink interface

## 🔧 Technical Details

### Built With
- **Python 3.x**: Core programming language
- **Tkinter**: GUI framework
- **Random Module**: Number generation
- **JSON**: Data persistence for statistics and leaderboard

### File Structure
```
number_guessing_game/
├── number_guessing_game.py    # Main game file
├── game_data.json             # Statistics and leaderboard data
└── README.md                  # This file
```

### Key Features
- **Full-Screen Mode**: Uses `root.state('zoomed')` for Windows
- **Responsive Layout**: Grid-based layout system
- **Event Handling**: Keyboard and mouse interactions
- **Dynamic Updates**: Real-time UI updates
- **Error Handling**: Invalid input validation
- **Theme System**: Dynamic color scheme switching
- **Data Persistence**: JSON-based statistics and leaderboard storage
- **Statistics Tracking**: Comprehensive game performance metrics

## 🎮 Game Mechanics

### Number Generation
- Random number between 1 and 100
- New number for each game
- Uses Python's `random.randint()`

### Attempt Tracking
- Increments with each valid guess
- Invalid guesses don't count
- Resets to 0 for new games

### Win/Lose Conditions
- **Win**: Correct guess within 8 attempts
- **Lose**: Run out of attempts
- **Invalid**: Numbers outside 1-100 range

## 📊 Statistics & Leaderboard

### Statistics Window
- **Games Played**: Total number of games
- **Games Won/Lost**: Win/loss ratio
- **Win Rate**: Percentage of games won
- **Best Score**: Lowest attempts to win
- **Average Attempts**: Average attempts per game
- **Last Played**: Date and time of last game

### Leaderboard
- **Top 10 Players**: Sorted by best scores
- **Player Names**: Auto-generated player IDs
- **Scores**: Number of attempts to win
- **Dates**: When the score was achieved
- **Medals**: 🥇🥈🥉 for top 3 positions

## 🐛 Troubleshooting

### Common Issues

**Game won't start:**
- Ensure Python is installed and in PATH
- Check that Tkinter is available
- Try running: `python -c "import tkinter"`

**Full-screen issues:**
- The game uses Windows-specific full-screen mode
- On other operating systems, it will run in a large window

**Input problems:**
- Only numbers 1-100 are accepted
- Letters or special characters will show an error message

**Statistics not saving:**
- Check if `game_data.json` file is writable
- Ensure the game has permission to create files in the directory

## 🚀 Future Enhancements

Potential improvements for future versions:
- **🌍 Multi-language**: Support for different languages
- **🎲 Difficulty Levels**: Different number ranges
- **📱 Mobile Version**: Android/iOS app version
- **🌐 Online Multiplayer**: Real-time multiplayer gameplay
- **🎨 More Themes**: Additional color schemes and animations
- **🎵 Custom Sound Effects**: Optional audio feedback
- **👤 Player Profiles**: Custom player names and avatars


## 🤝 Contributing

Feel free to contribute to this project by:
- Reporting bugs
- Suggesting new features
- Improving the code
- Enhancing the documentation


**Enjoy playing the Number Guessing Game! 🎯🎮**

*Challenge yourself to beat your best score and become a number guessing master!* 