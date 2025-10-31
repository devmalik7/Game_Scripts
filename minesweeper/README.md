# Minesweeper Game

A classic Minesweeper game built with Python and Pygame. Test your logic and strategy as you clear the minefield!

## Features

- Classic Minesweeper gameplay
- 10x10 grid with 15 mines
- Flagging system for marking suspected mines
- Auto-reveal of empty cells
- Win/lose detection
- Automatic game restart after game over

## Requirements

- Python 3.x
- Pygame

## Installation

1. Make sure you have Python 3.x installed on your system.

2. Install Pygame:
   ```bash
   pip install pygame
   ```

## How to Run

Simply run the Python file:
```bash
python "Minesweeper Game.py"
```

## How to Play

### Objective
Reveal all tiles without mines to win the game. If you click on a mine, you lose!

### Controls

- **Left Click**: Reveal a tile
- **Right Click**: Place or remove a flag on a tile

### Game Rules

1. Click on a tile to reveal it
2. Numbers indicate how many mines are adjacent to that tile
3. Use flags (right-click) to mark tiles you suspect contain mines
4. Reveal all non-mine tiles to win
5. If you click on a mine, the game ends

### Tips

- Start with tiles that have fewer adjacent mines
- Use the numbers to deduce where mines are located
- Flag suspected mines to avoid clicking them accidentally
- Empty tiles will automatically reveal surrounding tiles

## Game Settings

You can customize the game by modifying these variables at the top of the file:
- `ROWS`, `COLS`: Grid dimensions (default: 10x10)
- `MINES_COUNT`: Number of mines (default: 15)
- `WIDTH`, `HEIGHT`: Window size (default: 600x700)

## License

This project is open source and available for educational purposes.

