# Cho-Han Game

Welcome to **Cho-Han Game**, a traditional Japanese dice game of even-odd, implemented in Python. This game involves betting on the outcome of two dice, guessing whether their sum will be even (Cho) or odd (Han).

## Table of Contents

- [About the Game](#about-the-game)
- [Game Rules](#game-rules)
- [Features](#features)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [File Overview](#file-overview)
- [Future Improvements](#future-improvements)
- [Credits](#credits)

## About the Game

**Cho-Han Game** simulates the traditional Japanese dice game played by betting on the even or odd outcome of two rolled dice. The game involves a betting mechanism, balance tracking, and feedback on wins and losses.

## Game Rules

1. The player starts with an initial balance.
2. In each round:
   - The player places a bet amount.
   - The dice are rolled, and the player guesses if the sum will be even (Cho) or odd (Han).
3. If the player’s guess is correct, they win their bet amount minus a 10% house fee.
4. If incorrect, the bet amount is subtracted from their balance.
5. The game ends when the player decides to quit or runs out of balance.

## Features

- Traditional Cho-Han betting gameplay.
- Customizable starting balance.
- Automatic balance updates and 10% house fee deduction for each winning round.
- User-friendly console interface.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Pinger1456/Cho-Xan-Game.git
   cd Cho-Xan-Game
   ```

2. **Run the game**:
   ```bash
   python main.py
   ```

*Note*: This game requires Python 3.x.

## How to Play

1. Run `main.py` to start the game.
2. Follow the on-screen prompts:
   - Enter a bet amount.
   - Choose `CHO` for even or `HAN` for odd.
3. The outcome of each round is displayed, along with your updated balance.
4. Quit anytime by entering `QUIT`.

## File Overview

- **main.py**: Entry point for the game. Initializes and starts the game loop.
- **game.py**: Contains the `Game` class, which controls the game logic, dice rolls, and main gameplay loop.
- **player.py**: Defines the `Player` class, managing the player's balance and bets.

## Future Improvements

- Add more detailed game statistics and session history.
- Implement additional betting options or side bets.
- Enhance the user interface with graphical elements.

## Credits

**Cho-Han Game** was adapted from the code by Al Sweigart (al@inventwithpython.com). This project was designed to demonstrate fundamental game mechanics, object-oriented programming, and console interaction in Python.

Enjoy the game, and may luck be on your side!
```

This `README.md` provides an overview, game rules, instructions, and descriptions of the files in the project, which should give new users a clear understanding of how to set up and play the game. Let me know if you’d like to add anything specific!
