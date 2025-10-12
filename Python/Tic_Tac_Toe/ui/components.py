"""
UI components like buttons and text displays.
"""
import tkinter as tk
from tkinter import font as tkfont
from game.constants import (
    CANVAS_WIDTH,
    BUTTON_WIDTH,
    BUTTON_HEIGHT,
    BUTTON_Y,
    COLOR_BUTTON_BG,
    COLOR_BUTTON_HOVER,
    COLOR_BUTTON_OUTLINE,
    COLOR_BUTTON_TEXT,
    FONT_FAMILY_PRIMARY,
    FONT_FAMILY_FALLBACK,
    BUTTON_FONT_SIZE,
    RESULT_FONT_SIZE,
    TITLE_FONT_SIZE,
    TITLE_Y,
    COLOR_TITLE,
    CANVAS_HEIGHT,
    COLOR_CANVAS_BG,
)


class UIComponents:
    """Manages UI components like buttons and text."""

    def __init__(self, canvas):
        """
        Initialize UI components manager.

        Args:
            canvas: Canvas widget to draw on
        """
        self.canvas = canvas

    @staticmethod
    def get_font(size, weight="bold"):
        """
        Get a font with fallback support.

        Args:
            size: Font size
            weight: Font weight (normal, bold)

        Returns:
            tkfont.Font object
        """
        try:
            return tkfont.Font(family=FONT_FAMILY_PRIMARY, size=size, weight=weight)
        except (tk.TclError, Exception):
            return tkfont.Font(family=FONT_FAMILY_FALLBACK, size=size, weight=weight)

    def draw_title(self):
        """Draw the game title."""
        title_font = self.get_font(TITLE_FONT_SIZE)

        self.canvas.create_text(
            CANVAS_WIDTH // 2,
            TITLE_Y,
            text="Tic Tac Toe",
            font=title_font,
            fill=COLOR_TITLE,
            tags="title",
        )

    def show_result_message(self, message, color, on_text_created=None):
        """
        Show result message with semi-transparent background.

        Args:
            message: Message to display
            color: Text color
            on_text_created: Callback with text_id as parameter

        Returns:
            int: Canvas text item ID
        """
        result_font = self.get_font(RESULT_FONT_SIZE)

        # Create semi-transparent background
        self.canvas.create_rectangle(
            0,
            0,
            CANVAS_WIDTH,
            CANVAS_HEIGHT,
            fill=COLOR_CANVAS_BG,
            stipple="gray50",
            tags="result",
        )

        # Create result text
        text_id = self.canvas.create_text(
            CANVAS_WIDTH // 2,
            150,
            text=message,
            font=result_font,
            fill=color,
            tags="result",
        )

        if on_text_created:
            on_text_created(text_id)

        return text_id

    def create_play_again_button(self, on_click):
        """
        Create and show the play again button.

        Args:
            on_click: Callback function for button clicks
        """
        button_font = self.get_font(BUTTON_FONT_SIZE)

        button_x = CANVAS_WIDTH // 2
        button_y = BUTTON_Y

        # Create button background
        button_bg = self.canvas.create_rectangle(
            button_x - BUTTON_WIDTH // 2,
            button_y - BUTTON_HEIGHT // 2,
            button_x + BUTTON_WIDTH // 2,
            button_y + BUTTON_HEIGHT // 2,
            fill=COLOR_BUTTON_BG,
            outline=COLOR_BUTTON_OUTLINE,
            width=3,
            tags="play_again",
        )

        # Create button text
        self.canvas.create_text(
            button_x,
            button_y,
            text="Play Again",
            font=button_font,
            fill=COLOR_BUTTON_TEXT,
            tags="play_again",
        )

        # Bind click event
        def on_button_click(event):
            x, y = event.x, event.y
            bounds = self.canvas.coords(button_bg)
            if bounds[0] <= x <= bounds[2] and bounds[1] <= y <= bounds[3]:
                on_click()

        self.canvas.tag_bind("play_again", "<Button-1>", on_button_click)

        # Add hover effects
        def on_button_enter(event):
            self.canvas.itemconfig(button_bg, fill=COLOR_BUTTON_HOVER)

        def on_button_leave(event):
            self.canvas.itemconfig(button_bg, fill=COLOR_BUTTON_BG)

        self.canvas.tag_bind("play_again", "<Enter>", on_button_enter)
        self.canvas.tag_bind("play_again", "<Leave>", on_button_leave)
