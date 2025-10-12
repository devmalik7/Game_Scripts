"""
Main entry point for the Tic Tac Toe game.
"""
import tkinter as tk
from game.controller import GameController


def main():
    """Initialize and run the game."""
    root = tk.Tk()
    GameController(root)
    root.mainloop()


if __name__ == "__main__":
    main()
