# 🏓 Pong Game

A classic Pong game implementation using Python and Pygame. Play against the computer or challenge a friend in this timeless arcade-style paddle game.

## Features

- 🎮 **Two Game Modes**:
  - Player vs Computer (PvE)
  - Player vs Player (PvP)
- 🎯 **Classic Pong Gameplay** with smooth ball physics
- 📊 **Score Tracking** for both players
- 🎨 **Simple, Clean Interface** with easy-to-use menu system
- ⌨️ **Keyboard Controls** for intuitive gameplay

## Requirements

- Python 3.x
- Pygame library

## Installation

1. Clone or download this repository

2. Install Pygame (if not already installed):
   ```bash
   pip install pygame
   ```

## How to Run

Simply run the Python script:
```bash
python pong.py
```

## Controls

### Menu
- **1** - Select Player vs Computer mode
- **2** - Select Player vs Player mode
- **ESC** - Quit the game

### During Gameplay

**Player 1 (Right Paddle):**
- **↑ (Up Arrow)** - Move paddle up
- **↓ (Down Arrow)** - Move paddle down

**Player 2 (Left Paddle) - PvP Mode:**
- **W** - Move paddle up
- **S** - Move paddle down

**In-Game:**
- **ESC** - Return to main menu

## Game Modes

### Player vs Computer (PvE)
Play against an AI opponent that follows the ball. The computer controls the left paddle.

### Player vs Player (PvP)
Play with a friend! Each player controls one paddle using different keyboard keys.

## How to Play

1. Start the game and select your preferred mode from the menu
2. Use the arrow keys (or W/S in PvP mode) to move your paddle up and down
3. Hit the ball with your paddle to bounce it back
4. Score points when the ball passes your opponent's side
5. Press ESC anytime to return to the main menu

## Game Settings

- **Screen Size**: 800x600 pixels
- **Frame Rate**: 60 FPS
- **Paddle Speed**: 7 pixels per frame
- **Ball Speed**: 5 pixels per frame (adjustable in code)

Enjoy the game! 🎮

