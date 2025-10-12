"""
Canvas setup and drawing utilities.
"""
import tkinter as tk
from game.constants import (
    CANVAS_WIDTH,
    CANVAS_HEIGHT,
    COLOR_CANVAS_BG,
    CELL_SIZE,
    GRID_OFFSET_Y,
    GRID_WIDTH,
    COLOR_GRID_LINE,
    GRID_LINE_WIDTH,
)


class GameCanvas:
    """Manages the game canvas and grid drawing."""

    def __init__(self, root):
        """
        Initialize the game canvas.

        Args:
            root: Tkinter root window
        """
        self.canvas = tk.Canvas(
            root,
            width=CANVAS_WIDTH,
            height=CANVAS_HEIGHT,
            bg=COLOR_CANVAS_BG,
            highlightthickness=0,
        )
        self.canvas.pack(padx=20, pady=20)

        # Calculate grid offset for centering
        self.grid_offset_x = (CANVAS_WIDTH - GRID_WIDTH) // 2
        self.grid_offset_y = GRID_OFFSET_Y

    def draw_grid(self):
        """Draw the game grid with straight lines."""
        # Draw vertical lines
        for i in range(1, 3):
            x = self.grid_offset_x + i * CELL_SIZE
            y_start = self.grid_offset_y
            y_end = self.grid_offset_y + 3 * CELL_SIZE

            self.canvas.create_line(
                x,
                y_start,
                x,
                y_end,
                fill=COLOR_GRID_LINE,
                width=GRID_LINE_WIDTH,
                capstyle=tk.BUTT,
                tags="grid",
            )

        # Draw horizontal lines
        for i in range(1, 3):
            y = self.grid_offset_y + i * CELL_SIZE
            x_start = self.grid_offset_x
            x_end = self.grid_offset_x + 3 * CELL_SIZE

            self.canvas.create_line(
                x_start,
                y,
                x_end,
                y,
                fill=COLOR_GRID_LINE,
                width=GRID_LINE_WIDTH,
                capstyle=tk.BUTT,
                tags="grid",
            )

    def get_cell_from_click(self, x, y):
        """
        Convert click coordinates to cell indices.

        Args:
            x: X coordinate of click
            y: Y coordinate of click

        Returns:
            tuple: (row, col) or (None, None) if outside grid
        """
        rel_x = x - self.grid_offset_x
        rel_y = y - self.grid_offset_y

        if rel_x < 0 or rel_y < 0:
            return None, None

        col = int(rel_x // CELL_SIZE)
        row = int(rel_y // CELL_SIZE)

        if 0 <= row < 3 and 0 <= col < 3:
            return row, col
        return None, None

    def clear_marks(self):
        """Clear all game marks from the canvas."""
        for row in range(3):
            for col in range(3):
                self.canvas.delete(f"mark_{row}_{col}")

    def clear_results(self):
        """Clear result overlays and buttons."""
        self.canvas.delete("winning_line")
        self.canvas.delete("result")
        self.canvas.delete("play_again")
