# Tic Tac Toe

## Game Details
- **Language:** Python
- **Description:** A Tic Tac Toe game built with Python and Tkinter.

## Dependencies

- Python 3.6+
- tkinter (usually included with Python)

## How to Run
1. Open a terminal/command prompt.  
2. Navigate to the `Python/Tic_Tac_Toe` folder.  
3. Run the game with:
```bash
python main.py
```

## Project Structure

```
game/
├── main.py                     # Entry point - run this to start the game
├── tic_tac_toe.py              # Original monolithic version (deprecated)
├── game/                       # Game logic layer
│   ├── __init__.py
│   ├── board.py                # Board state and win detection logic
│   ├── controller.py           # Main game controller coordinating components
│   └── constants.py            # All configuration values and constants
└── ui/                         # User interface layer
    ├── __init__.py
    ├── animations.py           # Animation system (X, O, winning line, bounce)
    ├── canvas.py               # Canvas setup and grid drawing
    └── components.py           # UI components (buttons, text displays)
```