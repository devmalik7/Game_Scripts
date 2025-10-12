"""
Animation system for game marks and effects.
"""
import math
import tkinter as tk
from game.constants import (
    ANIMATION_STEPS_X,
    ANIMATION_STEPS_O,
    ANIMATION_DELAY_X,
    ANIMATION_DELAY_O,
    ANIMATION_STEPS_WINNING_LINE,
    ANIMATION_DELAY_WINNING_LINE,
    BOUNCE_STEPS,
    BOUNCE_DELAY,
    MARK_SIZE,
    MARK_LINE_WIDTH,
    COLOR_X_MARK,
    COLOR_O_MARK,
    COLOR_WINNING_LINE,
    CELL_SIZE,
    WINNING_LINE_PADDING,
    WINNING_LINE_CORNER_PADDING,
)


class AnimationManager:
    """Manages all animations in the game."""

    def __init__(self, root, canvas, grid_offset_x, grid_offset_y):
        """
        Initialize the animation manager.

        Args:
            root: Tkinter root window
            canvas: Canvas widget to draw on
            grid_offset_x: X offset of the game grid
            grid_offset_y: Y offset of the game grid
        """
        self.root = root
        self.canvas = canvas
        self.grid_offset_x = grid_offset_x
        self.grid_offset_y = grid_offset_y
        self.animation_ids = []
        self.animation_in_progress = False

    def cancel_all_animations(self):
        """Cancel all pending animations."""
        for anim_id in self.animation_ids:
            try:
                self.root.after_cancel(anim_id)
            except (tk.TclError, Exception):
                pass
        self.animation_ids.clear()

    def animate_x(self, row, col, on_complete=None):
        """
        Animate drawing an X mark.

        Args:
            row: Row index (0-2)
            col: Column index (0-2)
            on_complete: Callback function to call when animation completes
        """
        self.animation_in_progress = True
        center_x = self.grid_offset_x + col * CELL_SIZE + CELL_SIZE // 2
        center_y = self.grid_offset_y + row * CELL_SIZE + CELL_SIZE // 2

        # First stroke: top-left to bottom-right
        x1, y1 = center_x - MARK_SIZE, center_y - MARK_SIZE
        x2, y2 = center_x + MARK_SIZE, center_y + MARK_SIZE
        current_step = [0]

        def draw_first_stroke():
            if current_step[0] <= ANIMATION_STEPS_X:
                progress = current_step[0] / ANIMATION_STEPS_X
                curr_x = x1 + (x2 - x1) * progress
                curr_y = y1 + (y2 - y1) * progress

                if current_step[0] > 0:
                    prev_progress = (current_step[0] - 1) / ANIMATION_STEPS_X
                    prev_x = x1 + (x2 - x1) * prev_progress
                    prev_y = y1 + (y2 - y1) * prev_progress

                    self.canvas.create_line(
                        prev_x,
                        prev_y,
                        curr_x,
                        curr_y,
                        fill=COLOR_X_MARK,
                        width=MARK_LINE_WIDTH,
                        capstyle=tk.ROUND,
                        smooth=True,
                        tags=f"mark_{row}_{col}",
                    )

                current_step[0] += 1
                anim_id = self.root.after(ANIMATION_DELAY_X, draw_first_stroke)
                self.animation_ids.append(anim_id)
            else:
                # Start second stroke
                draw_second_stroke()

        # Second stroke: top-right to bottom-left
        x3, y3 = center_x + MARK_SIZE, center_y - MARK_SIZE
        x4, y4 = center_x - MARK_SIZE, center_y + MARK_SIZE
        current_step2 = [0]

        def draw_second_stroke():
            if current_step2[0] <= ANIMATION_STEPS_X:
                progress = current_step2[0] / ANIMATION_STEPS_X
                curr_x = x3 + (x4 - x3) * progress
                curr_y = y3 + (y4 - y3) * progress

                if current_step2[0] > 0:
                    prev_progress = (current_step2[0] - 1) / ANIMATION_STEPS_X
                    prev_x = x3 + (x4 - x3) * prev_progress
                    prev_y = y3 + (y4 - y3) * prev_progress

                    self.canvas.create_line(
                        prev_x,
                        prev_y,
                        curr_x,
                        curr_y,
                        fill=COLOR_X_MARK,
                        width=MARK_LINE_WIDTH,
                        capstyle=tk.ROUND,
                        smooth=True,
                        tags=f"mark_{row}_{col}",
                    )

                current_step2[0] += 1
                anim_id = self.root.after(ANIMATION_DELAY_X, draw_second_stroke)
                self.animation_ids.append(anim_id)
            else:
                self.animation_in_progress = False
                if on_complete:
                    on_complete()

        draw_first_stroke()

    def animate_o(self, row, col, on_complete=None):
        """
        Animate drawing an O mark.

        Args:
            row: Row index (0-2)
            col: Column index (0-2)
            on_complete: Callback function to call when animation completes
        """
        self.animation_in_progress = True
        center_x = self.grid_offset_x + col * CELL_SIZE + CELL_SIZE // 2
        center_y = self.grid_offset_y + row * CELL_SIZE + CELL_SIZE // 2
        radius = MARK_SIZE

        current_step = [0]
        prev_point = [None, None]

        def draw_circle_stroke():
            if current_step[0] <= ANIMATION_STEPS_O:
                angle = (current_step[0] / ANIMATION_STEPS_O) * 2 * math.pi
                curr_x = center_x + radius * math.cos(angle - math.pi / 2)
                curr_y = center_y + radius * math.sin(angle - math.pi / 2)

                if prev_point[0] is not None:
                    self.canvas.create_line(
                        prev_point[0],
                        prev_point[1],
                        curr_x,
                        curr_y,
                        fill=COLOR_O_MARK,
                        width=MARK_LINE_WIDTH,
                        capstyle=tk.ROUND,
                        smooth=True,
                        tags=f"mark_{row}_{col}",
                    )

                prev_point[0] = curr_x
                prev_point[1] = curr_y
                current_step[0] += 1
                anim_id = self.root.after(ANIMATION_DELAY_O, draw_circle_stroke)
                self.animation_ids.append(anim_id)
            else:
                self.animation_in_progress = False
                if on_complete:
                    on_complete()

        draw_circle_stroke()

    def animate_winning_line(self, winning_combo, on_complete=None):
        """
        Animate drawing the winning line.

        Args:
            winning_combo: Tuple like ('row', 0), ('col', 1), ('diag', 0)
            on_complete: Callback function to call when animation completes
        """
        combo_type, index = winning_combo

        # Calculate line coordinates
        if combo_type == "row":
            x1 = self.grid_offset_x + WINNING_LINE_PADDING
            y1 = self.grid_offset_y + index * CELL_SIZE + CELL_SIZE // 2
            x2 = self.grid_offset_x + 3 * CELL_SIZE - WINNING_LINE_PADDING
            y2 = y1
        elif combo_type == "col":
            x1 = self.grid_offset_x + index * CELL_SIZE + CELL_SIZE // 2
            y1 = self.grid_offset_y + WINNING_LINE_PADDING
            x2 = x1
            y2 = self.grid_offset_y + 3 * CELL_SIZE - WINNING_LINE_PADDING
        elif combo_type == "diag" and index == 0:
            x1 = self.grid_offset_x + WINNING_LINE_CORNER_PADDING
            y1 = self.grid_offset_y + WINNING_LINE_CORNER_PADDING
            x2 = self.grid_offset_x + 3 * CELL_SIZE - WINNING_LINE_CORNER_PADDING
            y2 = self.grid_offset_y + 3 * CELL_SIZE - WINNING_LINE_CORNER_PADDING
        else:  # diag 1
            x1 = self.grid_offset_x + 3 * CELL_SIZE - WINNING_LINE_CORNER_PADDING
            y1 = self.grid_offset_y + WINNING_LINE_CORNER_PADDING
            x2 = self.grid_offset_x + WINNING_LINE_CORNER_PADDING
            y2 = self.grid_offset_y + 3 * CELL_SIZE - WINNING_LINE_CORNER_PADDING

        current_step = [0]

        def draw_line_step():
            if current_step[0] <= ANIMATION_STEPS_WINNING_LINE:
                progress = current_step[0] / ANIMATION_STEPS_WINNING_LINE
                curr_x = x1 + (x2 - x1) * progress
                curr_y = y1 + (y2 - y1) * progress

                if current_step[0] > 0:
                    prev_progress = (
                        current_step[0] - 1
                    ) / ANIMATION_STEPS_WINNING_LINE
                    prev_x = x1 + (x2 - x1) * prev_progress
                    prev_y = y1 + (y2 - y1) * prev_progress

                    self.canvas.create_line(
                        prev_x,
                        prev_y,
                        curr_x,
                        curr_y,
                        fill=COLOR_WINNING_LINE,
                        width=8,
                        capstyle=tk.ROUND,
                        tags="winning_line",
                    )

                current_step[0] += 1
                anim_id = self.root.after(
                    ANIMATION_DELAY_WINNING_LINE, draw_line_step
                )
                self.animation_ids.append(anim_id)
            else:
                if on_complete:
                    on_complete()

        draw_line_step()

    def animate_bounce_text(self, text_id, start_y, end_y, on_complete=None):
        """
        Animate text with a bounce effect.

        Args:
            text_id: Canvas text item ID
            start_y: Starting Y position
            end_y: Ending Y position
            on_complete: Callback function to call when animation completes
        """
        current_step = [0]

        def animate_bounce():
            if current_step[0] < BOUNCE_STEPS:
                # Bounce effect using sine wave
                progress = current_step[0] / BOUNCE_STEPS
                bounce = math.sin(progress * math.pi) * 30
                y_pos = end_y - bounce

                coords = self.canvas.coords(text_id)
                self.canvas.coords(text_id, coords[0], y_pos)
                current_step[0] += 1
                anim_id = self.root.after(BOUNCE_DELAY, animate_bounce)
                self.animation_ids.append(anim_id)
            else:
                if on_complete:
                    on_complete()

        animate_bounce()
